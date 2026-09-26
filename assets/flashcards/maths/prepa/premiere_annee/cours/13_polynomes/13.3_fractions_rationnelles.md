#flashcards/maths/prépa/premiere_annee/cours/13_polynomes/fractions_rationnelles
## 1. Fraction rationnelle irréductible
Quand une fraction rationnelle $\frac PQ$ est-elle irréductible ?
?
**Réponse:**
Elle est irréductible si $\gcd(P,Q)=1$.
Toute fraction rationnelle non nulle possède une écriture irréductible unique à multiplication du numérateur et dénominateur par une même constante non nulle près.

## 2. Partie entière
Comment obtenir la partie entière d'une fraction rationnelle $\frac PQ$ ?
?
**Réponse:**
Effectuer la division euclidienne $P=QS+R$.
Alors $\frac PQ=S+\frac RQ$ avec $\deg R<\deg Q$.

## 3. Pôles et ordre
Comment reconnaître un pôle $a$ d'une fraction rationnelle irréductible ?
?
**Réponse:**
$a$ est un pôle si c'est une racine du dénominateur.
Son ordre est la multiplicité de $a$ comme racine du dénominateur.

## 4. Éléments simples sur $\mathbb C$
Quelle forme prend la décomposition en éléments simples sur $\mathbb C$ ?
?
**Réponse:**
Après partie entière, chaque racine $a$ de multiplicité $m$ du dénominateur donne des termes $\frac{c_1}{X-a}+\cdots+\frac{c_m}{(X-a)^m}$.

## 5. Facteurs quadratiques réels
Quelle forme ajoutent les facteurs quadratiques irréductibles sur $\mathbb R$ ?
?
**Réponse:**
Pour un facteur irréductible $Q$ de degré $2$, les termes ont la forme $\frac{aX+b}{Q^k}$.

## 6. Dérivée logarithmique
Quelle est la dérivée logarithmique d'un polynôme scindé ?
?
**Réponse:**
Si $P=\lambda\prod_i(X-a_i)^{m_i}$, alors $\frac{P'}P=\sum_i\frac{m_i}{X-a_i}$.

## 7. Primitives usuelles
Quelles primitives sont fondamentales après une décomposition en éléments simples ?
?
**Réponse:**
$\int\frac{dx}{x-a}=\ln|x-a|+C$.
$\int\frac{dx}{(x-a)^k}=\frac{(x-a)^{1-k}}{1-k}+C$ pour $k\ge2$.
