#flashcards/maths/prépa/premiere_annee/summary/matrices_determinants_euclidien
## 1. Produit matriciel
Quand le produit $AB$ de deux matrices est-il défini, et quelle est sa taille ?
?
**Réponse:**
Si $A\in M_{n,p}(\mathbb K)$ et $B\in M_{p,q}(\mathbb K)$, alors $AB\in M_{n,q}(\mathbb K)$.
Son coefficient $(i,j)$ vaut $\sum_{k=1}^p a_{ik}b_{kj}$.

## 2. Matrice inversible
Comment caractériser l'inversibilité d'une matrice carrée $A$ ?
?
**Réponse:**
$A$ est inversible s'il existe une matrice $A^{-1}$ telle que $AA^{-1}=A^{-1}A=I$.
Cela équivaut à l'inversibilité de l'endomorphisme représenté par $A$, ou à $\det A\ne0$.

## 3. Pivot de Gauss
Quel est le but du pivot de Gauss pour un système linéaire ?
?
**Réponse:**
Il transforme le système par opérations élémentaires sur les lignes en un système échelonné, puis permet une résolution par remontée.
Les opérations élémentaires préservent l'ensemble des solutions.

## 4. Matrice de changement de base
Comment se transforment les coordonnées d'un vecteur lors d'un changement de base ?
?
**Réponse:**
Si $P$ est la matrice dont les colonnes sont les coordonnées de la nouvelle base dans l'ancienne, alors $[x]_{\text{ancienne}}=P[x]_{\text{nouvelle}}$.
Donc $[x]_{\text{nouvelle}}=P^{-1}[x]_{\text{ancienne}}$.

## 5. Matrices semblables
Quand deux matrices carrées $A$ et $B$ sont-elles semblables ?
?
**Réponse:**
Elles sont semblables s'il existe une matrice inversible $P$ telle que $B=P^{-1}AP$.
Elles représentent le même endomorphisme dans deux bases différentes.

## 6. Valeur propre et vecteur propre
Définir une valeur propre et un vecteur propre d'un endomorphisme $u$.
?
**Réponse:**
$\lambda$ est une valeur propre de $u$ s'il existe $x\ne0$ tel que $u(x)=\lambda x$.
Un tel vecteur $x$ est un vecteur propre associé ; l'ensemble associé avec $0$ est le sous-espace propre $\ker(u-\lambda\operatorname{id})$.

## 7. Diagonalisation
Comment caractériser la diagonalisabilité d'un endomorphisme en dimension finie ?
?
**Réponse:**
$u$ est diagonalisable si et seulement s'il existe une base de vecteurs propres de $u$.
Dans cette base, sa matrice est diagonale.
Des sous-espaces propres associés à des valeurs propres distinctes sont en somme directe.

## 8. Déterminant
Quelles propriétés fondamentales du déterminant faut-il connaître ?
?
**Réponse:**
$\det(AB)=\det(A)\det(B)$ et $\det(A^T)=\det(A)$.
Une matrice carrée est inversible si et seulement si son déterminant est non nul.
Échanger deux lignes change le signe ; multiplier une ligne par $\lambda$ multiplie le déterminant par $\lambda$.

## 9. Produit scalaire et norme
Comment une norme est-elle définie à partir d'un produit scalaire ?
?
**Réponse:**
Dans un espace préhilbertien réel, $\|x\|=\sqrt{\langle x,x\rangle}$.
L'inégalité de Cauchy-Schwarz est $|\langle x,y\rangle|\le\|x\|\|y\|$.

## 10. Orthogonalité et Pythagore
Quel lien entre orthogonalité et norme d'une somme ?
?
**Réponse:**
Si $x\perp y$, alors $\|x+y\|^2=\|x\|^2+\|y\|^2$.
Réciproquement, cette égalité équivaut à $x\perp y$.

## 11. Projection orthogonale
Quel est le théorème de projection orthogonale en dimension finie ?
?
**Réponse:**
Pour tout sous-espace $F$ d'un espace euclidien et tout $x$, il existe un unique $p_F(x)\in F$ minimisant $\|x-y\|$ pour $y\in F$.
On a $x-p_F(x)\in F^\perp$.

## 12. Procédé de Gram-Schmidt
À quoi sert le procédé de Gram-Schmidt ?
?
**Réponse:**
Il transforme une famille libre en une famille orthogonale ayant les mêmes espaces engendrés successifs.
Après normalisation, on obtient une base orthonormée.
