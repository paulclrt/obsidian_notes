#flashcards/machine_learning/pytorch/custom_datasets
## 1. ImageFolder for Custom Data

Comment charger un dataset d'images organisé en dossiers par classe avec `ImageFolder` ?
?
**Réponse:**
```
data/
├── train/
│   ├── pizza/
│   ├── steak/
│   └── sushi/
└── test/
    ├── pizza/
    ├── steak/
    └── sushi/
```
```python
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])
train_data = datasets.ImageFolder(root="data/train", transform=transform)
test_data = datasets.ImageFolder(root="data/test", transform=transform)

train_dataloader = DataLoader(train_data, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=32, shuffle=False)

class_names = train_data.classes          # ['pizza', 'steak', 'sushi']
class_to_idx = train_data.class_to_idx    # {'pizza': 0, 'steak': 1, 'sushi': 2}
```
Structure : dossier par classe, `ImageFolder` infère labels automatiquement.
<!--SR:!2026-08-26,1,230-->

## 2. Custom Dataset Class (Subclassing Dataset)

Comment créer un Dataset personnalisé en subclassant `torch.utils.data.Dataset` ?
?
**Réponse:**
```python
from torch.utils.data import Dataset
from PIL import Image
import pathlib
import os

class ImageFolderCustom(Dataset):
    def __init__(self, targ_dir: str, transform=None):
        self.paths = list(pathlib.Path(targ_dir).glob("*/*.jpg"))
        self.transform = transform
        self.classes, self.class_to_idx = self.find_classes(targ_dir)
    
    def find_classes(self, directory):
        classes = sorted(entry.name for entry in os.scandir(directory) if entry.is_dir())
        class_to_idx = {cls: i for i, cls in enumerate(classes)}
        return classes, class_to_idx
    
    def __len__(self):
        return len(self.paths)
    
    def __getitem__(self, index):
        img_path = self.paths[index]
        class_name = img_path.parent.name
        class_idx = self.class_to_idx[class_name]
        img = Image.open(img_path)
        if self.transform:
            img = self.transform(img)
        return img, class_idx
```
3 méthodes obligatoires : `__init__`, `__len__`, `__getitem__`.
<!--SR:!2026-08-26,1,230-->

## 3. Transforms Composition

Comment composer plusieurs transformations d'images ?
?
**Réponse:**
```python
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.Resize((64, 64)),           # Redimensionner
    transforms.RandomHorizontalFlip(p=0.5), # Data augmentation
    transforms.ToTensor()                   # PIL → Tensor [0,1], (H,W,C)→(C,H,W)
])

test_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()                   # Pas d'augmentation sur test
])
```
`Compose` applique séquentiellement. Augmentation (flip, rotation, color jitter) **uniquement sur train**.
<!--SR:!2026-08-26,1,230-->

## 4. Data Augmentation Transforms

Quelles sont les transformations de data augmentation courantes ?
?
**Réponse:**
```python
transforms.RandomHorizontalFlip(p=0.5)      # Flip horizontal aléatoire
transforms.RandomVerticalFlip(p=0.5)        # Flip vertical
transforms.RandomRotation(degrees=30)       # Rotation aléatoire ±30°
transforms.RandomResizedCrop(size=224)      # Crop aléatoire + resize
transforms.ColorJitter(brightness=0.2, contrast=0.2)  # Variations couleur
transforms.RandomAffine(degrees=10, translate=(0.1, 0.1))  # Affine
transforms.RandomPerspective()              # Perspective
```
Rendent le modèle plus robuste en créant variété artificielle.
<!--SR:!2026-08-25,0,230-->

## 5. Normalization Transform

Comment normaliser les images avec mean/std (ex: ImageNet stats) ?
?
**Réponse:**
```python
transforms.Normalize(
    mean=[0.485, 0.456, 0.406],  # ImageNet RGB mean
    std=[0.229, 0.224, 0.225]    # ImageNet RGB std
)
```
Appliqué **après** `ToTensor()` (qui met en [0,1]). Pour grayscale : `mean=[0.5], std=[0.5]`.
Formule : `(pixel - mean) / std` → centré sur 0, écart-type 1.
<!--SR:!2026-08-25,0,230-->

## 6. DataLoader Parameters

Quels sont les paramètres importants de `DataLoader` ?
?
**Réponse:**
```python
DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,              # Train: True, Test: False
    num_workers=4,             # Processus parallèles pour chargement (0 = main process)
    pin_memory=True,           # Accélère transfert CPU→GPU
    drop_last=False,           # Garder dernier batch incomplet
    persistent_workers=True    # Garde workers vivants entre epochs (num_workers>0)
)
```
- `num_workers` > 0 : chargement parallèle (Linux: fork, Windows: spawn)
- `pin_memory` : alloue mémoire page-locked pour GPU transfer plus rapide
<!--SR:!2026-08-25,0,230-->

## 7. Custom Dataset vs ImageFolder

Quand utiliser un Dataset custom vs `ImageFolder` ?
?
**Réponse:**
| `ImageFolder` | Dataset Custom |
|---|---|
| Structure standard (dossier/classe) | Structure non-standard |
| Pas de logique spéciale | Labels depuis CSV, JSON, DB |
| Rapide à mettre en place | Contrôle total sur `__getitem__` |
| | Multi-labels, segmentation, etc. |
<!--SR:!2026-08-29,4,270-->

## 8. Accessing Data from DataLoader

Comment récupérer un batch depuis un DataLoader ?
?
**Réponse:**
```python
# Un seul batch
img_batch, label_batch = next(iter(train_dataloader))
print(img_batch.shape)   # [batch_size, C, H, W] ex: [32, 3, 64, 64]
print(label_batch.shape) # [batch_size] ex: [32]

# Itérer
for batch_idx, (images, labels) in enumerate(train_dataloader):
    # training step
```
`images` = tenseur float32 [0,1], `labels` = tenseur int64 (indices classes).
<!--SR:!2026-08-25,0,230-->

## 9. Single Image Inference

Comment faire l'inférence sur une seule image custom ?
?
**Réponse:**
```python
from PIL import Image
import torchvision.transforms as transforms

# 1. Charger et transformer
img = Image.open("path/to/image.jpg")
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])
img_tensor = transform(img).unsqueeze(0).to(device)  # [1, C, H, W]

# 2. Prédiction
model.eval()
with torch.inference_mode():
    logits = model(img_tensor)
    probs = torch.softmax(logits, dim=1)
    pred_class = probs.argmax(dim=1).item()
    pred_label = class_names[pred_class]
```
`unsqueeze(0)` ajoute dimension batch. `argmax` donne indice classe.
<!--SR:!2026-08-25,0,230-->

## 10. Downloading Data Programmatically

Comment télécharger et dézipper un dataset automatiquement ?
?
**Réponse:**
```python
import requests, zipfile
from pathlib import Path

data_path = Path("data")
zip_path = data_path / "pizza_steak_sushi.zip"

# Download
with open(zip_path, "wb") as f:
    response = requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip")
    f.write(response.content)

# Extract
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(data_path / "pizza_steak_sushi")

# Cleanup
zip_path.unlink()
```
Utile pour scripts reproductibles / CI/CD.
<!--SR:!2026-08-28,3,250-->

## 11. Class Names from Dataset

Comment récupérer les noms de classes depuis un dataset ?
?
**Réponse:**
```python
# ImageFolder
class_names = train_data.classes           # List[str]
class_to_idx = train_data.class_to_idx     # Dict[str, int]
idx_to_class = {v: k for k, v in class_to_idx.items()}

# Custom Dataset
class_names = train_data.classes
class_to_idx = train_data.class_to_idx
```
Ordre alphabétique par défaut. `idx_to_class` utile pour mapping prédiction → nom.
<!--SR:!2026-08-26,1,230-->

## 12. Train/Val/Test Split from Single Folder

Comment splitter un dossier unique en train/val/test ?
?
**Réponse:**
```python
from torch.utils.data import random_split

full_dataset = datasets.ImageFolder(root="data/all", transform=transform)
total = len(full_dataset)
train_size = int(0.7 * total)
val_size = int(0.15 * total)
test_size = total - train_size - val_size

train_ds, val_ds, test_ds = random_split(full_dataset, [train_size, val_size, test_size])

train_dl = DataLoader(train_ds, batch_size=32, shuffle=True)
val_dl = DataLoader(val_ds, batch_size=32, shuffle=False)
test_dl = DataLoader(test_ds, batch_size=32, shuffle=False)
```
`random_split` garde la distribution des classes. Pour split stratifié → `sklearn.model_selection.train_test_split` sur indices.
<!--SR:!2026-08-25,0,230-->

## 13. WeightedRandomSampler for Imbalanced Data

Comment gérer des classes déséquilibrées avec `WeightedRandomSampler` ?
?
**Réponse:**
```python
from torch.utils.data import WeightedRandomSampler

# Calculer poids par classe
class_counts = [len([l for _, l in train_data if l == i]) for i in range(num_classes)]
class_weights = [1.0 / c for c in class_counts]
sample_weights = [class_weights[label] for _, label in train_data]

sampler = WeightedRandomSampler(
    weights=sample_weights,
    num_samples=len(sample_weights),
    replacement=True
)

train_dataloader = DataLoader(train_data, batch_size=32, sampler=sampler)
# Note: shuffle=False car sampler gère l'ordre
```
Échantillonne plus souvent les classes sous-représentées.
<!--SR:!2026-08-25,0,230-->