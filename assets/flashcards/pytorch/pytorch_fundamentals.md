#flashcards/code/pytorch/fundamentals
## 1. Tensor Basics

Quelle est la différence principale entre un scalaire, un vecteur et une matrice en PyTorch ?
?
**Réponse:**
Un scalaire est un tenseur 0-dimensionnel (ex: `torch.tensor(7)`), un vecteur est 1-dimensionnel (`torch.tensor([7, 2])`) et une matrice est 2-dimensionnelle (`torch.tensor([[7, 8], [9, 10]])`). La dimensionnalité se compte avec `.ndim` et les tailles avec `.shape`.
<!--SR:!2026-08-29,4,270-->



## 2. Creating Tensors - From Lists

Comment crée-t-on un tenseur à partir d'une liste Python ?
?
**Réponse:**
On utilise `torch.tensor([...])`. Par exemple `torch.tensor([1, 2, 3])` crée un tenseur 1-dimensionnel, et `torch.tensor([[1,2], [3,4]])` crée un tenseur 2-dimensionnel (matrice).
<!--SR:!2026-08-28,3,250-->



## 3. Creating Tensors - Zeros and Ones

Comment initialise-t-on un tenseur rempli de zeros ou de ones avec un dtype spécifique ?
?
**Réponse:**
On utilise `torch.zeros(shape, dtype=...)` et `torch.ones(shape, dtype=...)`. Exemple : `torch.zeros(3, 4, dtype=torch.float32)` crée une matrice 3x4 de floats32.
<!--SR:!2026-08-29,4,270-->



## 4. Creating Tensors - Random

Quelles sont les fonctions pour créer des tenseurs de nombres aléatoires ?
?
**Réponse:**
`torch.rand(shape)` pour des floats en [0, 1), `torch.randn(shape)` pour des floats standard normal, et `torch.randint(low, high, shape)` pour des entiers.
<!--SR:!2026-08-26,1,230-->



## 5. Tensor Attributes

Quels sont les attributs clés d'un tenseur et que retournent-ils ?
?
**Réponse:**
`tensor.ndim` -> nombre de dimensions, `tensor.shape` -> tuple des tailles, `tensor.dtype` -> type de données, `tensor.device` -> appareil (cpu/cuda), `tensor.item()` -> convertit un tenseur 0-d en Python number, `tensor.tolist()` -> convertit en liste Python.
<!--SR:!2026-08-28,3,250-->



## 6. Reshaping - view vs reshape

Quand utilise-t-on `.view()` vs `.reshape()` pour changer la forme d'un tenseur ?
?
**Réponse:**
Utilisez `.view()` si le tenseur est contigu en mémoire sinon utilisez `.reshape()` qui fonctionne toujours. Exemple : `x.view(2, 3)` reshapes un tenseur 1-d de 6 éléments en matrice 2x3.
<!--SR:!2026-08-29,4,270-->



## 7. Reshaping - Flatten

Comment aplatit-on un tenseur (le remet en 1 dimension) ?
?
**Réponse:**
`tensor.view(-1)` ou `tensor.flatten()`. Le `-1` déduit la taille automatique. `flatten()` renvoie un nouveau tenseur contigu tandis que `view()` nécessite la contiguïté.
<!--SR:!2026-08-28,3,230-->



## 8. Reshaping - Permute

Comment permute-t-on les dimensions d'un tenseur (ex: passer de (batch, H, W, C) à (batch, C, H, W)) ?
?
**Réponse:**
Avec `.permute()` en spécifiant l'ordre des dimensions. Exemple : `x.permute(0, 3, 1, 2)` sur un tenseur (2, 224, 224, 3) donne (2, 3, 224, 224).
<!--SR:!2026-08-26,1,230-->



## 9. Reshaping - Squeeze

Que fait `.squeeze()` et quand l'utilise-t-on ?
?
**Réponse:**
`.squeeze()` retire les dimensions de taille 1. Exemple : `torch.randn(1, 3, 224, 1).squeeze()` donne un tenseur de shape (3, 224). Utile après avoir passé à travers une réseau qui ajoute des dimensions singleton.
<!--SR:!2026-08-26,1,230-->



## 10. Reshaping - Unsqueeze

Comment ajoute-t-on une dimension de taille 1 à un tenseur ?
?
**Réponse:**
Avec `.unsqueeze(dim)` qui insère une dimension à l'index spécifié. Exemple : `x.unsqueeze(0)` ajoute une dimension en début de tenseur.
<!--SR:!2026-08-29,4,270-->



## 11. Basic Operations - Element-wise

Comment effectue-t-on des opérations élément par élément entre deux tenseurs ?
?
**Réponse:**
Les opérateurs `+`, `-`, `*`, `/` fonctionnent élément par élément. Exemple : `torch.tensor([1, 2, 3]) + torch.tensor([4, 5, 6])` donne `tensor([5, 7, 9])`.
<!--SR:!2026-08-28,3,250-->



## 12. Basic Operations - Matrix Multiplication

Comment fait-on la multiplication de matrices en PyTorch ?
?
**Réponse:**
Avec `@` ou `torch.matmul()`. Exemple : `A @ B` où A shape (3, 4) et B shape (4, 5) donnent (3, 5). On peut aussi utiliser `A.mm(B)` pour la multiplication matricielle classique.
<!--SR:!2026-08-29,4,270-->



## 13. Basic Operations - Dot Product

Comment calcule-t-on le produit scalaire de deux tenseurs ?
?
**Réponse:**
Avec `torch.dot(x, y)` qui retourne un scalaire. requis que les tenseurs aient la même longueur.
<!--SR:!2026-08-26,1,230-->



## 14. Basic Operations - Transpose

Comment transpose-t-on un tenseur (échanger lignes et colonnes) ?
?
**Réponse:**
Avec `.T` ou `.mT` (nouvelle API). Exemple : `torch.randn(3, 4).T` donne un tenseur (4, 3).
<!--SR:!2026-08-26,1,230-->



## 15. Basic Operations - In-place

Qu'est-ce qu'une opération in-place et pourquoi l'utilise-t-on ?
?
**Réponse:**
Les opérations in-place (notées `_` suffixe, ex: `x.add_(1)`) modifient le tenseur en place sans en créer un nouveau, ce qui économise de la mémoire. Attention : elles modifient la valeur originale qui peut être utilisée ailleurs.
<!--SR:!2026-08-29,4,270-->



## 16. Basic Operations - Clamp

Commentborne-t-on les valeurs d'un tenseur entre une min et une max ?
?
**Réponse:**
Avec `.clamp(min, max)`. Exemple : `x.clamp(min=0, max=1)` met toutes les valeurs < 0 à 0 et > 1 à 1.
<!--SR:!2026-08-26,1,230-->



## 17. Basic Operations - Reduction

Quelles sont les fonctions de réduction communes et que font-elles ?
?
**Réponse:**
`tensor.sum()` → somme de tous les éléments, `tensor.mean()` → moyenne, `tensor.min()` / `tensor.max()` → valeurs extrêmes, `tensor.argmin()` / `tensor.argmax()` → indices des valeurs extrêmes.
<!--SR:!2026-08-28,3,250-->



## 18. Models - Linear Layer

À quoi sert `torch.nn.Linear` et comment l'utilise-t-on ?
?
**Réponse:**
C'est une couche fully-connected : `y = xW^T + b`. Exemple : `linear = torch.nn.Linear(in_features=2, out_features=6)` suivie de `output = linear(x)` où x shape (7, 2) donne output shape (7, 6).
<!--SR:!2026-08-28,3,250-->



## 19. Models - MLP

Comment construire un Multi-Layer Perceptron basique avec `nn.Module` ?
?
**Réponse:**
En subclassesant `torch.nn.Module`, en définissant les couches dans `__init__` et en implémentant `forward`. Exemple : une MLP avec deux couches linéaires et une ReLU entre elles.
<!--SR:!2026-08-28,3,250-->



## 20. Models - Manual Seed

Pourquoi utilise-t-on `torch.manual_seed()` et quel est son effet ?
?
**Réponse:**
Pour rendre la génération de nombres aléatoires reproductible. `torch.manual_seed(42)` assure que `torch.rand()` produira toujours les mêmes valeurs au prochain lancement.
<!--SR:!2026-08-29,4,270-->



## 21. Getting Info - Min/Max/Sum

Comment extrait-on des informations statistiques d'un tenseur ?
?
**Réponse:**
Avec `tensor.min()`, `tensor.max()`, `tensor.sum()`, `tensor.mean()`. Exemple : `torch.arange(0, 100, 10).mean()` retourne 45.0.
<!--SR:!2026-08-29,4,270-->



## 22. Getting Info - Argmin/Argmax

Que retournent `argmin()` et `argmax()` et quel est leur cas d'usage ?
?
**Réponse:**
Ils retournent l'indice (position) de la valeur minimale ou maximale respectivement. Utile pour trouver la classe prédite dans une classification : `x.argmax()` donne l'index du plus haut score.
<!--SR:!2026-08-29,4,270-->



## 23. numpy-torch Interop

Comment passe-t-on d'un tenseur PyTorch vers numpy et inversement ?
?
**Réponse:**
`t.numpy()` convertit un tenseur CPU en array numpy (partage la mémoire). `torch.from_numpy(n)` fait l'inverse (numpy vers tenseur). Pour pandas : passer par `.numpy()` d'abord.
<!--SR:!2026-08-28,3,250-->



## 24. Range Tensors

Quelles sont les fonctions pour créer des tenseurs de ranges et leurs différences ?
?
**Réponse:**
`torch.arange(start, end, step)` crée des valeurs incrémentées (comme range Python). `torch.linspace(start, end, steps)` crée un nombre égal de points entre start et end inclusifs. `torch.range` a été supprimé au profit d'arange.
<!--SR:!2026-08-26,1,230-->



## 25. Tensor Splitting and Concatenation

Comment split et concatène-t-on des tenseurs ?
?
**Réponse:**
`torch.chunk(tensor, chunks, dim)` divise en N chunks le long d'une dimension. `torch.cat([tensor1, tensor2], dim)` concatène plusieurs tenseurs le long d'une dimension donnée, en s'assurant que les autres dimensions correspondent.
<!--SR:!2026-08-26,1,230-->

