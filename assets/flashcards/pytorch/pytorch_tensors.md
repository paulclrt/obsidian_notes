#flashcards/machine_learning/pytorch/tensors
## 1. Scalar Tensor Creation

Comment créer un tenseur scalaire (0-dimensionnel) en PyTorch ?
?
**Réponse:**
`torch.tensor(7)` crée un tenseur 0-d. Accéder à la valeur Python avec `.item()` : `tensor.item()` retourne `7`.

## 2. Vector Tensor Creation

Comment créer un tenseur vecteur (1-dimensionnel) à partir d'une liste ?
?
**Réponse:**
`torch.tensor([7, 2])` crée un tenseur 1-d de shape `torch.Size([2])`. Vérifier avec `.ndim` (retourne 1) et `.shape`.

## 3. Matrix Tensor Creation

Comment créer une matrice (2-dimensionnel) en PyTorch ?
?
**Réponse:**
`torch.tensor([[7, 8], [9, 10]])` crée un tenseur 2-d de shape `torch.Size([2, 2])`.

## 4. 3D Tensor for Images

Quelle shape a un tenseur 3D représentant un batch d'images grayscale ?
?
**Réponse:**
Shape `(batch, height, width)` par exemple `(3, 2, 2)` pour 3 images de 2x2 pixels. Le nombre de dimensions (`.ndim`) vaut 3.

## 5. Tensor Key Attributes

Quels sont les 5 attributs clés d'un tenseur PyTorch et que retournent-ils ?
?
**Réponse:**
- `tensor.ndim` : nombre de dimensions (rank)
- `tensor.shape` : tuple des tailles par dimension
- `tensor.dtype` : type de données (ex: `torch.float32`)
- `tensor.device` : appareil (`cpu` ou `cuda`)
- `tensor.item()` : convertit un tenseur 0-d en nombre Python

## 6. Creating Tensors - Zeros and Ones

Comment créer un tenseur rempli de zéros ou de uns avec un dtype spécifique ?
?
**Réponse:**
`torch.zeros(3, 4, dtype=torch.float32)` → matrice 3x4 de float32
`torch.ones(2, 3, dtype=torch.int64)` → matrice 2x3 d'entiers

## 7. Creating Tensors - Random

Quelles sont les 3 fonctions principales pour créer des tenseurs aléatoires ?
?
**Réponse:**
- `torch.rand(shape)` : floats uniformes en [0, 1)
- `torch.randn(shape)` : floats distribution normale standard (moyenne 0, écart-type 1)
- `torch.randint(low, high, shape)` : entiers aléatoires dans [low, high)

## 8. Creating Tensors - Like Another

Comment créer un tenseur de même forme qu'un tenseur existant mais rempli de zéros ?
?
**Réponse:**
`torch.zeros_like(x)` où `x` est le tenseur de référence. Même forme, même dtype, même device.

## 9. Range Tensors - arange vs linspace

Quelle est la différence entre `torch.arange` et `torch.linspace` ?
?
**Réponse:**
`torch.arange(start, end, step)` : valeurs incrémentées par step (exclut end)
`torch.linspace(start, end, steps)` : nombre exact de points `steps` répartis uniformément entre start et end INCLUSIFS

## 10. Identity Matrix

Comment créer une matrice identité en PyTorch ?
?
**Réponse:**
`torch.eye(3)` crée une matrice identité 3x3.

## 11. Reshaping - view vs reshape

Quand utiliser `.view()` vs `.reshape()` pour changer la forme d'un tenseur ?
?
**Réponse:**
`.view()` nécessite que le tenseur soit **contigu** en mémoire. `.reshape()` fonctionne toujours (copie si nécessaire). Préférer `.reshape()` sauf si performance critique et contiguïté garantie.

## 12. Flattening a Tensor

Comment aplatir un tenseur (le remettre en 1 dimension) ?
?
**Réponse:**
Deux options : `tensor.view(-1)` ou `tensor.flatten()`. Le `-1` déduit la taille automatiquement. `flatten()` renvoie un tenseur contigu, `view()` nécessite la contiguïté.

## 13. Permute Dimensions

Comment passer d'un tenseur (batch, H, W, C) à (batch, C, H, W) pour les CNN ?
?
**Réponse:**
`x.permute(0, 3, 1, 2)` réordonne les dimensions. Exemple : tenseur `(2, 224, 224, 3)` devient `(2, 3, 224, 224)`.

## 14. Squeeze and Unsqueeze

Que font `.squeeze()` et `.unsqueeze(dim)` ?
?
**Réponse:**
- `.squeeze()` : retire **toutes** les dimensions de taille 1. Ex: `(1, 3, 224, 1)` → `(3, 224)`
- `.unsqueeze(dim)` : insère une dimension de taille 1 à l'index `dim`. Ex: `x.unsqueeze(0)` ajoute dim en position 0.

## 15. Tensor Splitting

Comment diviser un tenseur en chunks le long d'une dimension ?
?
**Réponse:**
`torch.chunk(tensor, chunks, dim)` divise en `chunks` parties égales le long de `dim`. Retourne un tuple de tenseurs.

## 16. Tensor Concatenation

Comment concaténer plusieurs tenseurs le long d'une dimension ?
?
**Réponse:**
`torch.cat([tensor1, tensor2], dim=1)` concatène le long de la dimension `dim`. Toutes les autres dimensions doivent correspondre.

## 17. Stacking Tensors

Quelle est la différence entre `torch.cat` et `torch.stack` ?
?
**Réponse:**
`torch.cat` concatène le long d'une dimension **existante**. `torch.stack([x, y])` crée une **nouvelle dimension** à l'avant : shape `(2, 2)` au lieu de `(4,)`.

## 18. Element-wise Operations

Comment effectuer des opérations élément par élément entre deux tenseurs ?
?
**Réponse:**
Opérateurs standards : `+`, `-`, `*`, `/`. Exemple : `torch.tensor([1,2,3]) + torch.tensor([4,5,6])` → `tensor([5, 7, 9])`. Broadcasting automatique si shapes compatibles.

## 19. Matrix Multiplication

Comment faire une multiplication de matrices en PyTorch ?
?
**Réponse:**
Opérateur `@` ou `torch.matmul(A, B)` ou `A.mm(B)` (pour 2D seulement). Ex: `A @ B` avec A `(3,4)` et B `(4,5)` donne `(3,5)`.

## 20. Dot Product

Comment calculer le produit scalaire de deux tenseurs 1D ?
?
**Réponse:**
`torch.dot(x, y)` retourne un scalaire. Les deux tenseurs doivent avoir la même longueur.

## 21. Transpose

Comment transposer un tenseur 2D (échanger lignes et colonnes) ?
?
**Réponse:**
`x.T` ou `x.mT` (nouvelle API). Exemple : `torch.randn(3, 4).T` donne shape `(4, 3)`.

## 22. In-place Operations

Qu'est-ce qu'une opération in-place et comment la reconnaître ?
?
**Réponse:**
Modifie le tenseur existant sans en créer un nouveau (économise mémoire). Reconnaissable au suffixe `_` : `x.add_(1)`, `x.relu_()`. Attention : modifie la valeur originale potentiellement utilisée ailleurs.

## 23. Clamp Values

Comment borner les valeurs d'un tenseur entre min et max ?
?
**Réponse:**
`x.clamp(min=0, max=1)` met toutes les valeurs < 0 à 0 et > 1 à 1. Utile pour normaliser ou contraindre des sorties.

## 24. Reduction Operations

Quelles sont les fonctions de réduction communes sur un tenseur ?
?
**Réponse:**
- `tensor.sum()` : somme de tous éléments
- `tensor.mean()` : moyenne
- `tensor.min()` / `tensor.max()` : valeurs extrêmes
- `tensor.argmin()` / `tensor.argmax()` : **indices** des valeurs extrêmes

## 25. Argmin/Argmax Usage

À quoi servent `argmin()` et `argmax()` en pratique ?
?
**Réponse:**
Retournent l'**indice** (position) de la valeur min/max. Cas d'usage principal : classification → `logits.argmax(dim=1)` donne la classe prédite (indice du score max).

## 26. NumPy Interop - Tensor to NumPy

Comment convertir un tenseur PyTorch en array NumPy ?
?
**Réponse:**
`t.numpy()` convertit un tenseur **CPU** en array NumPy (partage la mémoire si contigu). Le tenseur ne doit pas nécessiter de gradient.

## 27. NumPy Interop - NumPy to Tensor

Comment convertir un array NumPy en tenseur PyTorch ?
?
**Réponse:**
`torch.from_numpy(numpy_array)` crée un tenseur partageant la mémoire avec l'array NumPy. Modifications affectent les deux.

## 28. Manual Seed for Reproducibility

Pourquoi et comment utiliser `torch.manual_seed()` ?
?
**Réponse:**
Rend la génération aléatoire reproductible. `torch.manual_seed(42)` assure que `torch.rand()` produit toujours les mêmes valeurs. Pour CUDA : `torch.cuda.manual_seed(42)`.

## 29. Linear Layer Basics

À quoi sert `torch.nn.Linear` et comment l'utiliser ?
?
**Réponse:**
Couche fully-connected : `y = x @ W^T + b`.
```python
linear = nn.Linear(in_features=2, out_features=6)
x = torch.randn(7, 2)  # batch 7, 2 features
output = linear(x)     # shape (7, 6)
```

## 30. Building an MLP with nn.Module

Comment construire un MLP basique en subclassant `nn.Module` ?
?
**Réponse:**
```python
class MyMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 16)
        self.fc2 = nn.Linear(16, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```
Définir couches dans `__init__`, implémenter `forward`.

## 31. Getting Tensor Info - Min/Max/Sum/Mean

Comment extraire des statistiques d'un tenseur ?
?
**Réponse:**
```python
x = torch.arange(0, 100, 10)  # [0, 10, 20, ..., 90]
x.min()    # tensor(0)
x.max()    # tensor(90)
x.sum()    # tensor(450)
x.mean()   # tensor(45.)
```
Pour mean sur int, caster : `x.type(torch.float32).mean()`

## 32. Positional Info - Argmin/Argmax

Que retournent `argmin()` et `argmax()` sur un tenseur 1D ?
?
**Réponse:**
L'**indice** (position) de la valeur min/max.
```python
x = torch.arange(0, 100, 10)
x.argmin()  # tensor(0) - index of 0
x.argmax()  # tensor(9) - index of 90
```