#flashcards/machine_learning/pytorch/general_overview
## 1. Complete PyTorch Workflow - Bird's Eye View

Quelles sont les 6 étapes fondamentales d'un projet PyTorch complet, de l'idée au modèle déployé ?
?
**Réponse:**
1. **DATA** : Préparer données → `Dataset` + `DataLoader` (batch, shuffle, transforms)
2. **MODEL** : Construire architecture → subclass `nn.Module` + définir `forward()`
3. **TRAIN** : Boucle d'entraînement → `forward → loss → backward → optimizer.step()` par epoch
4. **EVALUATE** : Valider → `model.eval()` + `torch.inference_mode()` + métriques
5. **SAVE** : Persister → `torch.save(model.state_dict(), "model.pth")`
6. **LOAD/USE** : Charger → recréer classe identique + `load_state_dict()` + `eval()`

Mantra : **Data → Model → Train → Eval → Save → Load**

## 2. Minimal Working Training Loop

À quoi ressemble la boucle d'entraînement minimale qui fonctionne pour TOUS les problèmes ?
?
**Réponse:**
```python
# 1. SETUP
model = MyModel().to(device)
loss_fn = nn.CrossEntropyLoss()  # ou BCEWithLogitsLoss, MSELoss, etc.
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 2. TRAIN LOOP
for epoch in range(epochs):
    model.train()
    for X, y in train_dataloader:
        X, y = X.to(device), y.to(device)
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # 3. EVAL LOOP
    model.eval()
    with torch.inference_mode():
        for X, y in test_dataloader:
            X, y = X.to(device), y.to(device)
            test_pred = model(X)
            # compute metrics...
```
Ce pattern (train/eval, zero_grad/backward/step, device management) est **universel**.

## 3. Creating ANY Custom Dataset

Comment créer un Dataset pour N'IMPORTE QUEL type de données (images, CSV, texte, audio) ?
?
**Réponse:**
```python
from torch.utils.data import Dataset

class MyCustomDataset(Dataset):
    def __init__(self, data_path, transform=None):
        self.samples = self._load_data(data_path)  # liste de (input, target)
        self.transform = transform
    
    def _load_data(self, path):
        # LOGIQUE SPÉCIFIQUE À VOS DONNÉES
        # Ex: lire CSV, scanner dossiers, charger JSON, etc.
        return [(input_tensor, target_tensor), ...]
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        x, y = self.samples[idx]
        if self.transform:
            x = self.transform(x)
        return x, y

# Utilisation
dataset = MyCustomDataset("data/", transform=my_transforms)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```
**3 méthodes obligatoires** : `__init__`, `__len__`, `__getitem__`. Le reste est votre logique.

## 4. Designing ANY Model Architecture

Comment concevoir sa propre architecture (CNN, RNN, Transformer, hybride) ?
?
**Réponse:**
```python
class MyArchitecture(nn.Module):
    def __init__(self, input_shape, num_classes, custom_params):
        super().__init__()
        # 1. DÉFINIR TOUS LES LAYERS ICI (avec paramètres apprenables)
        self.feature_extractor = nn.Sequential(...)  # CNN, RNN, Attention, etc.
        self.classifier = nn.Linear(final_features, num_classes)
    
    def forward(self, x):
        # 2. DÉFINIR LE FLUX DE DONNÉES (operator fusion = plus rapide)
        x = self.feature_extractor(x)
        x = x.flatten(1)  # si besoin
        x = self.classifier(x)
        return x  # LOGITS BRUTS (pas de softmax/sigmoid ici)

# Instanciation
model = MyArchitecture(input_shape=..., num_classes=..., custom_params=...).to(device)
```
Règles d'or : layers dans `__init__`, flux dans `forward`, **retourner logits bruts**.

## 5. Replicating a Paper - Step by Step

Quelle est la checklist pour répliquer un paper (ViT, ResNet, nouveau SOTA) ?
?
**Réponse:**
```
□ 1. Trouver paper + code officiel (PapersWithCode, GitHub, arXiv)
□ 2. Lire : architecture, hyperparams (LR, schedule, WD, batch, epochs), data aug
□ 3. Implémenter composant par composant (test shapes à chaque étape)
□ 4. Sanity check : overfit 1 batch (loss → 0, acc → 100%)
□ 5. Entraîner complet, comparer courbes au paper
□ 6. Si écart : vérifier seeds, augmentations, LR schedule, weight decay, batch size
□ 7. Documenter config finale + différences notées
```
Clé : **implémenter modulairement** (patch embed → encoder → head) et **tester chaque pièce**.

## 6. Transfer Learning - The Practical Shortcut

Comment adapter un modèle SOTA pré-entraîné à votre problème en 5 minutes ?
?
**Réponse:**
```python
import torchvision

# 1. Charger modèle + weights + transforms automatiques
weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT
model = torchvision.models.efficientnet_b0(weights=weights)
transform = weights.transforms()

# 2. Freeze backbone (feature extraction)
for param in model.features.parameters():
    param.requires_grad = False

# 3. Remplacer classifier pour VOS classes
in_features = model.classifier[-1].in_features
model.classifier = nn.Sequential(
    nn.Dropout(0.2),
    nn.Linear(in_features, YOUR_NUM_CLASSES)
).to(device)

# 4. Entraîner SEULEMENT le classifier (LR ~1e-3, 5-10 epochs)
optimizer = torch.optim.Adam(model.classifier.parameters(), lr=1e-3)
# ... boucle standard ...
```
Pour fine-tuning : dégeler derniers blocs + LR plus bas (1e-4).

## 7. Experiment Tracking - Never Lose Results

Comment organiser ses expériences pour comparer et reproduire ?
?
**Réponse:**
```python
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime
import os

def make_writer(exp_name, model_name, extra=""):
    log_dir = os.path.join("runs", datetime.now().strftime("%Y-%m-%d"), exp_name, model_name, extra)
    return SummaryWriter(log_dir)

# Dans training loop :
writer = make_writer("pizza_classification", "effnetb0", "lr1e-3_bs32")
for epoch in range(epochs):
    train_loss, train_acc = train_step(...)
    test_loss, test_acc = test_step(...)
    writer.add_scalars("Loss", {"train": train_loss, "test": test_loss}, epoch)
    writer.add_scalars("Acc", {"train": train_acc, "test": test_acc}, epoch)
writer.close()
# Lancer: tensorboard --logdir runs/
```
Structure : `runs/YYYY-MM-DD/experiment/model/hyperparams/` → comparatif instantané.

## 8. Saving & Loading - The Right Way

Quelles sont les 2 façons de sauvegarder et quand les utiliser ?
?
**Réponse:**
```python
# MÉTHODE 1: state_dict (RECOMMANDÉE - portable, léger)
torch.save(model.state_dict(), "model.pth")
# Charger:
model = MyArchitecture(...)
model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()

# MÉTHODE 2: Modèle complet (déconseillé - lie au code exact)
torch.save(model, "model_full.pth")
# Charger:
model = torch.load("model_full.pth", map_location=device)
```
**Toujours préférer `state_dict`** : architecture séparée des poids, compatible versionning, transfer learning.

## 9. Key PyTorch Modules Cheatsheet

Quels modules importer pour quelle tâche ?
?
**Réponse:**
| Tâche | Module / Classe |
|---|---|
| **Tenseurs de base** | `torch.tensor`, `torch.randn`, `torch.arange` |
| **Opérations** | `+`, `-`, `*`, `/`, `@`, `.T`, `.view()`, `.permute()` |
| **Layers** | `nn.Linear`, `nn.Conv2d`, `nn.LSTM`, `nn.TransformerEncoder` |
| **Activations** | `nn.ReLU`, `nn.GELU`, `nn.Sigmoid`, `nn.Softmax` |
| **Conteneurs** | `nn.Sequential`, `nn.ModuleList`, `nn.ModuleDict` |
| **Loss** | `nn.CrossEntropyLoss`, `nn.BCEWithLogitsLoss`, `nn.MSELoss` |
| **Optimizers** | `torch.optim.Adam`, `torch.optim.SGD`, `torch.optim.AdamW` |
| **Data** | `Dataset`, `DataLoader`, `torchvision.datasets`, `transforms` |
| **Prétrainés** | `torchvision.models`, `timm.create_model` |
| **Métriques** | `torchmetrics.Accuracy`, `Precision`, `Recall`, `F1Score` |
| **Logging** | `torch.utils.tensorboard.SummaryWriter` |
| **Device** | `"cuda" if torch.cuda.is_available() else "cpu"` |

## 10. Mental Model: How PyTorch Thinks

Quels sont les 4 concepts mentaux pour "penser en PyTorch" ?
?
**Réponse:**
1. **Tensor = Data** : Tout est tenseur (images, texte, audio, labels, gradients). Shape = `(batch, channels, ...)`.
2. **Module = Function with State** : `nn.Module` encapsule paramètres + `forward()`. Composables via `Sequential`.
3. **Autograd = Magic** : `loss.backward()` calcule TOUS les gradients automatiquement. `optimizer.step()` met à jour.
4. **Device = Where Compute Happens** : `.to(device)` déplace tenseurs ET modèle. Tout doit être sur même device.

Workflow mental : **Data → Tensor → Module → Loss → Backward → Step → Repeat**