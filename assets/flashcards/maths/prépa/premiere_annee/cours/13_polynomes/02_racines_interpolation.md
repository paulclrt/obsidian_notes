#flashcards/maths/prépa/premiere_annee/cours/13_polynomes/racines_interpolation
## 1. Racine et facteur
Comment caractériser une racine $a$ de $P\in\mathbb K[X]$ ?
?
**Réponse:**
$a$ est racine de $P$ si et seulement si $P(a)=0$.
Cela équivaut à $(X-a)\mid P$.

## 2. Nombre de racines
Quel majorant porte sur le nombre de racines d'un polynôme non nul ?
?
**Réponse:**
Un polynôme non nul de degré $n$ a au plus $n$ racines distinctes dans un corps.

## 3. Racine multiple
Comment caractériser une racine $a$ de multiplicité $m$ ?
?
**Réponse:**
$P=(X-a)^mQ$ avec $Q(a)\ne0$.
Équivalemment, $P(a)=P'(a)=\cdots=P^{(m-1)}(a)=0$ et $P^{(m)}(a)\ne0$.

## 4. Polynôme scindé
Qu'appelle-t-on un polynôme scindé sur $\mathbb K$ ?
?
**Réponse:**
Un polynôme scindé est un produit de facteurs de degré $1$ sur $\mathbb K$.
Il s'écrit $\lambda\prod_i(X-a_i)^{m_i}$ avec $\lambda\ne0$.

## 5. Théorème de d'Alembert-Gauss
Quel résultat fondamental vaut dans $\mathbb C[X]$ ?
?
**Réponse:**
Tout polynôme non constant de $\mathbb C[X]$ est scindé.
Un polynôme de degré $n$ possède exactement $n$ racines comptées avec multiplicité.

## 6. Racines réelles d'un polynôme réel
Quelle propriété relie les racines complexes d'un polynôme de $\mathbb R[X]$ ?
?
**Réponse:**
Si $z$ est racine de $P\in\mathbb R[X]$, alors $\overline z$ est aussi racine, avec la même multiplicité.

## 7. Interpolation de Lagrange
Quel théorème d'interpolation faut-il connaître ?
?
**Réponse:**
Pour $n+1$ abscisses distinctes $x_i$ et valeurs $y_i$, il existe un unique polynôme $P$ de degré au plus $n$ tel que $P(x_i)=y_i$.

## 8. Base de Lagrange
Quelle est la formule des polynômes de base de Lagrange ?
?
**Réponse:**
$L_i(X)=\prod_{j\ne i}\frac{X-x_j}{x_i-x_j}$.
Ils vérifient $L_i(x_j)=\delta_{ij}$ et $P=\sum_i y_iL_i$.
