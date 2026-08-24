#flashcards/machine_learning/pytorch/computer_vision
## 1. torchvision Datasets

Comment charger un dataset d'images standard (ex: FashionMNIST) avec torchvision ?
?
**Réponse:**
```python
from torchvision import datasets
from torchvision.transforms import ToTensor

train_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
```
`transform=ToTensor()` convertit images PIL → tenseurs [0,1] et (H,W,C) → (C,H,W).

## 2. DataLoader for Batching

Comment créer un DataLoader pour charger les données par batches ?
?
**Réponse:**
```python
from torch.utils.data import DataLoader

BATCH_SIZE = 32
train_dataloader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=False)
```
- `shuffle=True` pour training (mélange à chaque epoch)
- `shuffle=False` pour test (ordre fixe)
- Retourne tuples `(batch_images, batch_labels)` shape `(B, C, H, W)` et `(B,)`

## 3. CNN Architecture - Conv2d

Quels sont les paramètres clés de `nn.Conv2d` ?
?
**Réponse:**
```python
nn.Conv2d(
    in_channels=3,      # canaux entrée (3=RGB, 1=grayscale)
    out_channels=16,    # nombre de filtres (feature maps)
    kernel_size=3,      # taille filtre (3x3)
    stride=1,           # pas du filtre
    padding=1           # padding (1 = "same" pour kernel=3)
)
```
Sortie shape : `H_out = (H_in + 2*padding - kernel_size) // stride + 1`

## 4. CNN Architecture - MaxPool2d

À quoi sert `nn.MaxPool2d` et comment l'utiliser ?
?
**Réponse:**
Réduit la résolution spatiale (downsampling) en gardant le max par fenêtre.
```python
nn.MaxPool2d(kernel_size=2, stride=2)  # divise H,W par 2
```
- `kernel_size=2` : fenêtre 2x2
- `stride=2` : pas de 2 (pas de chevauchement)
- Pas de paramètres apprenables

## 5. CNN Architecture - Flatten

Pourquoi et comment utiliser `nn.Flatten()` avant la couche finale ?
?
**Réponse:**
Aplatit les dimensions spatiales en vecteur 1D pour la couche Linear.
```python
nn.Flatten()  # (batch, C, H, W) → (batch, C*H*W)
```
Exemple : sortie Conv `(32, 12, 7, 7)` → `Flatten()` → `(32, 588)` → `Linear(588, 10)`

## 6. TinyVGG Architecture

À quoi ressemble l'architecture TinyVGG (CNN simple) ?
?
**Réponse:**
```python
class TinyVGG(nn.Module):
    def __init__(self, input_shape, hidden_units, output_shape):
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
            nn.Linear(hidden_units * 7 * 7, output_shape)  # 7x7 après 2 MaxPool sur 28x28
        )
    
    def forward(self, x):
        return self.classifier(self.conv_block_2(self.conv_block_1(x)))
```
2 blocs Conv+ReLU+MaxPool, puis classifier.

## 7. Operator Fusion in Forward

Pourquoi écrire `return self.classifier(self.conv_block_2(self.conv_block_1(x)))` au lieu de réassigner x ?
?
**Réponse:**
**Operator fusion** : PyTorch peut fusionner les opérations en un seul kernel CUDA, évitant lectures/écritures mémoire intermédiaires.
```python
# Optimisé (fusion possible)
def forward(self, x):
    return self.classifier(self.conv_block_2(self.conv_block_1(x)))

# Moins optimal
def forward(self, x):
    x = self.conv_block_1(x)
    x = self.conv_block_2(x)
    x = self.classifier(x)
    return x
```
Gain de vitesse mémoire sur GPU.

## 8. CrossEntropyLoss for Computer Vision

Quelle loss utiliser pour classification d'images multi-classes ?
?
**Réponse:**
`nn.CrossEntropyLoss()` — attend logits bruts `(batch, num_classes)` et targets indices `(batch,)`.
```python
loss_fn = nn.CrossEntropyLoss()
y_pred = model(X)  # logits (batch, 10)
loss = loss_fn(y_pred, y)  # y shape (batch,) valeurs 0-9
```
Pas de softmax manuel nécessaire.

## 9. Training Loop with DataLoader (CV)

Comment écrire une boucle d'entraînement complète pour Computer Vision ?
?
**Réponse:**
```python
for epoch in range(epochs):
    model.train()
    train_loss, train_acc = 0, 0
    for X, y in train_dataloader:
        X, y = X.to(device), y.to(device)
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        train_acc += accuracy_fn(y, y_pred.argmax(dim=1))
    train_loss /= len(train_dataloader)
    train_acc /= len(train_dataloader)
    
    # Evaluation
    model.eval()
    with torch.inference_mode():
        test_loss, test_acc = 0, 0
        for X, y in test_dataloader:
            X, y = X.to(device), y.to(device)
            test_loss += loss_fn(model(X), y).item()
            test_acc += accuracy_fn(y, model(X).argmax(dim=1))
        test_loss /= len(test_dataloader)
        test_acc /= len(test_dataloader)
```

## 10. torchmetrics Accuracy for CV

Comment utiliser torchmetrics pour l'accuracy en Computer Vision ?
?
**Réponse:**
```python
from torchmetrics import Accuracy

accuracy = Accuracy(task="multiclass", num_classes=10)

# Dans la boucle :
train_acc += accuracy(y_pred, y)  # gère logits directement
# ou
train_acc += accuracy(y_pred.softmax(dim=1), y)
```
`task="multiclass"` pour classification multi-classes. `num_classes` requis.

## 11. Device Agnostic Code

Comment écrire du code compatible CPU/GPU ?
?
**Réponse:**
```python
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Dans la boucle :
X, y = X.to(device), y.to(device)
```
Vérifier : `next(model.parameters()).device` doit correspondre à `X.device`.

## 12. Timing Training

Comment mesurer le temps d'entraînement ?
?
**Réponse:**
```python
from timeit import default_timer as timer

start = timer()
# ... training loop ...
end = timer()
print(f"Train time: {end - start:.3f} seconds")
```
Utile pour comparer CPU vs GPU, différents modèles, batch sizes.

## 13. Model Summary with torchinfo

Comment afficher un résumé du modèle (shapes, paramètres) ?
?
**Réponse:**
```python
from torchinfo import summary
summary(model, input_size=[1, 3, 224, 224])  # [batch, channels, H, W]
```
Affiche : input/output shapes par couche, nombre paramètres, MACs (opérations), taille mémoire.

## 14. FashionMNIST Classes

Combien de classes dans FashionMNIST et comment les récupérer ?
?
**Réponse:**
10 classes : `['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']`
```python
class_names = train_data.classes
print(len(class_names))  # 10
```

## 15. Image Tensor Shape

Quelle est la shape d'un tenseur d'image unique après ToTensor() ?
?
**Réponse:**
`(C, H, W)` — **Channels First** (PyTorch convention).
- FashionMNIST grayscale : `(1, 28, 28)`
- RGB : `(3, 224, 224)` typique
Batch : `(B, C, H, W)` ex: `(32, 3, 224, 224)`

## 16. CNN vs MLP for Images

Pourquoi utiliser un CNN au lieu d'un MLP pour les images ?
?
**Réponse:**
- **Translation invariance** : mêmes filtres détectent patterns partout
- **Local connectivity** : chaque neurone voit région locale (champ réceptif)
- **Parameter sharing** : mêmes poids réutilisés spatialement
- **Moins de paramètres** : MLP sur 28x28=784 inputs → énorme matrice
- **Hiérarchie features** : bords → textures → objets

## 17. Padding in Conv2d

Quel padding utiliser pour conserver la résolution spatiale ?
?
**Réponse:**
`padding = (kernel_size - 1) // 2` pour stride=1.
- kernel=3 → padding=1 ("same")
- kernel=5 → padding=2
- kernel=1 → padding=0
Formule sortie : `H_out = (H_in + 2*pad - kernel) // stride + 1`

## 18. Receptive Field

Qu'est-ce que le champ réceptif (receptive field) dans un CNN ?
?
**Réponse:**
Région de l'image d'entrée qui influence une activation donnée.
- Augmente avec la profondeur (plus de couches)
- Augmente avec kernel_size et stride
- MaxPool augmente aussi le champ réceptif effectif
Couches profondes "voient" plus grand contexte.

## 19. Batch Size Trade-offs

Comment choisir la batch size ?
?
**Réponse:**
- **Grande** (64, 128, 256) : gradient plus stable, meilleur parallélisme GPU, mais plus de mémoire
- **Petite** (16, 32) : gradient plus bruit (régularisation implicite), moins de mémoire
- Typique CV : 32, 64, 128
- Ajuster selon VRAM disponible

## 20. Epochs for CV

Combien d'epochs pour l'entraînement Computer Vision ?
?
**Réponse:**
- **FashionMNIST (simple)** : 3-10 epochs suffisent
- **CIFAR-10/100** : 50-200 epochs
- **ImageNet** : 90-120 epochs (avec scheduling LR)
- Surveiller validation loss → early stopping si overfitting
- Transfer learning : moins d'epochs (5-20) car features déjà apprises