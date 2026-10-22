#flashcards/maths/prépa/premiere_annee/perso/algebre_lineaire
## Somme directe et supplémentaire
Définir la somme directe de deux sev $F$ et $G$ de $E$.
Définir le supplémentaire $G$ d'un sous ev $F$ de $E$.
?
*Somme directe:*
L'idée c'est de décomposer l'espace en plusieurs sous espaces tel que chaque vecteur peut puisse s'écrire de façon unique comme une somme de vecteurs apparetenant à ces sous-espaces.
Dans $\mathbb{R}^2$:
Si on prend les droites $F=\{(x,0) | x \in \mathbb{R}\}$ et $F=\{(0,y) | y \in \mathbb{R}\}$. Alors tu peux prendre n'importe quel vecteur $(x,y)$ qui se décompose dans chaque espace. Donc $\mathbb{R}²=F\oplus G$
Formellement:
$$
F\oplus G \iff \begin{cases} F + G = E \\ F \cap G = \{0\}\end{cases}
$$
*Supplémentaire:*
On dit que $G$ est un supplémentaire de $F$ dans $E$ si $E=F\oplus G$ donc par déf:
$$
F\cap G = \{0\} \quad\quad F + G = E
$$
<!--SR:!2026-10-26,4,270-->

## Applications GL
C'est quoi une matrice $\in GL_k\{K\}$
?
Une matrice $A\in GL_k\{K\}$ c'est une matice apparetenant à l'ensemble des matrices carrée à $k$ coéfficients inversibles (donc det non nul btw).
Gl $\iff$ General linear group. *C'est un groupe pour la multiplication des matrices : le produit de deux matrices inversibles est inversible, la matrice identité en fait partie et chaque matrice possède un inverse.*
<!--SR:!2026-10-26,4,270-->

## matrice cannoniquement associée
Détermine la matrice associé à l'endomorphisme suivant: $f(x,y) = (2x+y,3y)$
?
Dans la base $e_1 = (1,0)\ et\ e_2=(0,1)$
D'abord $f(e_1)=(2, 0)$ et $f(e_2) = (1,3)$
On les mets en colone:
$$ A =
\begin{pmatrix}
2 & 1 \\
0 & 3
\end{pmatrix}
$$
la matrice cannoniquement associé à l'endorphisme $f$ est $A$
<!--SR:!2026-10-26,4,270-->


## trace d'une matrice
Définir la trace d'une matrice
?
C'est simplement la multiplication des éléments de la diagonale d'une matrice carrée (elle n'existe pas pour une matrice non carrée).
Elle sert pour l'étude des endormphismes et de leurs valeurs propres
$$
Tr(A+B) = Tr(A) + Tr(B) \\
Tr(AB) = Tr(BA)
$$
<!--SR:!2026-10-25,3,250-->


## Décrire une applicaiton k-lipschitzienne

Décrire une applicaiton k-lipschitzienne
?
Une application $f$ est k-lipschitzienne si elle ne peut pas trop éloigner  deux points l'un de l'autre.
$$
\boxed{
\forall x,y \in \mathbb{E}, \quad ||f(x)-f(y)|| \leq k||x-y||
}
$$
ou $k$ est une constante.
La distance entre les images de deux points ne peut pas dépasser \(k\) fois leur distance initiale
<!--SR:!2026-10-26,4,270-->
