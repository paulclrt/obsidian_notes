#flashcards/machine_learning/pytorch/going_modular
## 1. Modular Project Structure

Quelle est la structure recommandée pour un projet PyTorch modulaire ?
?
**Réponse:**
```
going_modular/
├── going_modular/
│   ├── data_setup.py      # DataLoaders, transforms
│   ├── engine.py          # train_step, test_step, train
│   ├── model_builder.py   # Architecture du modèle
│   ├── utils.py           # Sauvegarde, helpers
│   └── __init__.py
├── train.py               # Script principal d'entraînement
├── models/                # Modèles sauvegardés
└── data/                  # Datasets
```
Séparation des responsabilités : data, model, training, utils.

## 2. data_setup.py - create_dataloaders

À quoi ressemble la fonction `create_dataloaders` dans `data_setup.py` ?
?
**Réponse:**
```python
def create_dataloaders(
    train_dir: str,
    test_dir: str,
    transform: transforms.Compose,
    batch_size: int,
    num_workers: int = os.cpu_count()
):
    train_data = datasets.ImageFolder(train_dir, transform=transform)
    test_data = datasets.ImageFolder(test_dir, transform=transform)
    class_names = train_data.classes

    train_dataloader = DataLoader(
        train_data, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=True
    )
    test_dataloader = DataLoader(
        test_data, batch_size=batch_size, shuffle=False,
        num_workers=num_workers, pin_memory=True
    )
    return train_dataloader, test_dataloader, class_names
```
Retourne `(train_dl, test_dl, class_names)`. Centralise toute la logique data.

## 3. model_builder.py - TinyVGG Class

Comment définir l'architecture du modèle dans `model_builder.py` ?
?
**Réponse:**
```python
class TinyVGG(nn.Module):
    def __init__(self, input_shape: int, hidden_units: int, output_shape: int):
        super().__init__()
        self.conv_block_1 = nn.Sequential(
            nn.Conv2d(input_shape, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_units, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.conv_block_2 = nn.Sequential(
            nn.Conv2d(hidden_units, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_units, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(hidden_units * 13 * 13, output_shape)  # dépend input size
        )

    def forward(self, x):
        return self.classifier(self.conv_block_2(self.conv_block_1(x)))
```
Utilise `nn.Sequential` pour blocs. `forward` avec operator fusion.

## 4. engine.py - train_step

À quoi ressemble `train_step` dans `engine.py` ?
?
**Réponse:**
```python
def train_step(model, dataloader, loss_fn, optimizer, device):
    model.train()
    train_loss, train_acc = 0, 0
    for X, y in dataloader:
        X, y = X.to(device), y.to(device)
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        train_loss += loss.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        y_pred_class = y_pred.argmax(dim=1)
        train_acc += (y_pred_class == y).sum().item() / len(y_pred)
    return train_loss / len(dataloader), train_acc / len(dataloader)
```
Retourne `(avg_loss, avg_acc)` pour l'epoch. Une seule responsabilité : un epoch de training.

## 5. engine.py - test_step

À quoi ressemble `test_step` dans `engine.py` ?
?
**Réponse:**
```python
def test_step(model, dataloader, loss_fn, device):
    model.eval()
    test_loss, test_acc = 0, 0
    with torch.inference_mode():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            test_pred_logits = model(X)
            loss = loss_fn(test_pred_logits, y)
            test_loss += loss.item()
            test_pred_labels = test_pred_logits.argmax(dim=1)
            test_acc += (test_pred_labels == y).sum().item() / len(test_pred_labels)
    return test_loss / len(dataloader), test_acc / len(dataloader)
```
Pas de `zero_grad`, `backward`, `step`. `inference_mode()` désactive gradients.

## 6. engine.py - train function

À quoi ressemble la fonction `train` qui orchestrate tout ?
?
**Réponse:**
```python
def train(model, train_dataloader, test_dataloader, optimizer, loss_fn, epochs, device):
    results = {"train_loss": [], "train_acc": [], "test_loss": [], "test_acc": []}
    for epoch in tqdm(range(epochs)):
        train_loss, train_acc = train_step(model, train_dataloader, loss_fn, optimizer, device)
        test_loss, test_acc = test_step(model, test_dataloader, loss_fn, device)
        
        print(f"Epoch: {epoch+1} | train_loss: {train_loss:.4f} | train_acc: {train_acc:.4f} | test_loss: {test_loss:.4f} | test_acc: {test_acc:.4f}")
        
        results["train_loss"].append(train_loss)
        results["train_acc"].append(train_acc)
        results["test_loss"].append(test_loss)
        results["test_acc"].append(test_acc)
    return results
```
Boucle sur epochs, appelle `train_step` + `test_step`, loggue, retourne historique.

## 7. utils.py - save_model

Comment implémenter `save_model` dans `utils.py` ?
?
**Réponse:**
```python
def save_model(model, target_dir, model_name):
    target_dir_path = Path(target_dir)
    target_dir_path.mkdir(parents=True, exist_ok=True)
    assert model_name.endswith(".pth") or model_name.endswith(".pt")
    model_save_path = target_dir_path / model_name
    print(f"[INFO] Saving model to: {model_save_path}")
    torch.save(model.state_dict(), model_save_path)
```
Crée dossier si nécessaire, valide extension, sauvegarde `state_dict`.

## 8. train.py - Main Script

À quoi ressemble le script principal `train.py` qui assemble tout ?
?
**Réponse:**
```python
import torch
import data_setup, engine, model_builder, utils
from torchvision import transforms

NUM_EPOCHS = 5
BATCH_SIZE = 32
HIDDEN_UNITS = 10
LEARNING_RATE = 0.001

device = "cuda" if torch.cuda.is_available() else "cpu"

data_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

train_dataloader, test_dataloader, class_names = data_setup.create_dataloaders(
    train_dir="data/pizza_steak_sushi/train",
    test_dir="data/pizza_steak_sushi/test",
    transform=data_transform,
    batch_size=BATCH_SIZE
)

model = model_builder.TinyVGG(
    input_shape=3, hidden_units=HIDDEN_UNITS, output_shape=len(class_names)
).to(device)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

engine.train(model, train_dataloader, test_dataloader, optimizer, loss_fn, NUM_EPOCHS, device)

utils.save_model(model, "models", "tinyvgg_model.pth")
```
Importe modules locaux, configure hyperparams, connecte tout, lance entraînement.

## 9. Benefits of Modular Design

Quels sont les avantages de l'approche modulaire ?
?
**Réponse:**
- **Réutilisabilité** : `data_setup`, `engine`, `model_builder` réutilisables entre projets
- **Testabilité** : tester chaque fonction indépendamment
- **Lisibilité** : `train.py` montre le flux global en ~30 lignes
- **Collaboration** : équipe peut travailler sur modules différents
- **Expérimentation** : swapper modèle/data/optimizer facilement
- **Maintenance** : bug isolé → un seul fichier à corriger

## 10. Importing Local Modules

Comment importer les modules locaux dans `train.py` ?
?
**Réponse:**
```python
# Si going_modular est un package (avec __init__.py)
from going_modular import data_setup, engine, model_builder, utils

# Ou import direct si dans même dossier
import data_setup, engine, model_builder, utils
```
Nécessite `__init__.py` (peut être vide) dans `going_modular/` pour que Python le traite comme package.