#flashcards/maths/prépa/premiere_annee/summary/denombrement_probabilites_riemann
## 1. Cardinal d'une union disjointe
Quelle est la formule du cardinal d'une union finie de parties deux à deux disjointes ?
?
**Réponse:**
Si $A_1,\ldots,A_n$ sont deux à deux disjointes, alors $\left|\bigcup_{k=1}^n A_k\right|=\sum_{k=1}^n|A_k|$.

## 2. Arrangements et combinaisons
Quelle différence entre arrangements et combinaisons de $p$ éléments parmi $n$ ?
?
**Réponse:**
Le nombre d'arrangements est $A_n^p=\frac{n!}{(n-p)!}$ : l'ordre compte.
Le nombre de combinaisons est $\binom np=\frac{n!}{p!(n-p)!}$ : l'ordre ne compte pas.

## 3. Formule du binôme
Énoncer la formule du binôme de Newton.
?
**Réponse:**
Pour $n\in\mathbb N$, $(a+b)^n=\sum_{k=0}^n\binom nk a^kb^{n-k}$.

## 4. Axiomes d'une probabilité
Quelles propriétés définit une probabilité $\mathbb P$ sur un univers $\Omega$ ?
?
**Réponse:**
$\mathbb P(A)\in[0,1]$, $\mathbb P(\Omega)=1$.
Pour des événements deux à deux disjoints, $\mathbb P(\bigcup A_n)=\sum\mathbb P(A_n)$.
En particulier, $\mathbb P(A^c)=1-\mathbb P(A)$.

## 5. Probabilité conditionnelle
Comment définit-on $\mathbb P(A\mid B)$ lorsque $\mathbb P(B)>0$ ?
?
**Réponse:**
$\mathbb P(A\mid B)=\frac{\mathbb P(A\cap B)}{\mathbb P(B)}$.
Donc $\mathbb P(A\cap B)=\mathbb P(A\mid B)\mathbb P(B)$.

## 6. Formule des probabilités totales
Énoncer la formule des probabilités totales pour une partition $(B_i)$.
?
**Réponse:**
Si les $B_i$ forment une partition et $\mathbb P(B_i)>0$, alors $\mathbb P(A)=\sum_i\mathbb P(A\mid B_i)\mathbb P(B_i)$.

## 7. Indépendance de deux événements
Quel critère caractérise l'indépendance de $A$ et $B$ ?
?
**Réponse:**
$A$ et $B$ sont indépendants si $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$.
Si $\mathbb P(B)>0$, cela équivaut à $\mathbb P(A\mid B)=\mathbb P(A)$.

## 8. Espérance d'une variable aléatoire discrète
Comment définit-on l'espérance de $X$ discrète ?
?
**Réponse:**
Si $X$ prend les valeurs $x_i$, alors $\mathbb E(X)=\sum_i x_i\mathbb P(X=x_i)$, lorsque la somme est absolument convergente.
L'espérance est linéaire : $\mathbb E(aX+bY)=a\mathbb E(X)+b\mathbb E(Y)$.

## 9. Variance
Comment définit-on la variance et quelle formule de Koenig-Huygens faut-il connaître ?
?
**Réponse:**
$\operatorname{Var}(X)=\mathbb E((X-\mathbb E(X))^2)$.
$\operatorname{Var}(X)=\mathbb E(X^2)-\mathbb E(X)^2$.
L'écart-type est $\sigma(X)=\sqrt{\operatorname{Var}(X)}$.

## 10. Lois usuelles
Donner l'espérance et la variance des lois de Bernoulli et binomiale.
?
**Réponse:**
Si $X\sim\mathcal B(p)$, alors $\mathbb E(X)=p$ et $\operatorname{Var}(X)=p(1-p)$.
Si $X\sim\mathcal B(n,p)$, alors $\mathbb E(X)=np$ et $\operatorname{Var}(X)=np(1-p)$.

## 11. Convergence en loi
Que signifie $X_n\xrightarrow{\mathcal L}X$ pour des variables aléatoires réelles ?
?
**Réponse:**
Cela signifie que, pour tout point $x$ où la fonction de répartition $F_X$ est continue, $F_{X_n}(x)\to F_X(x)$.

## 12. Sommes de Riemann
Quel est le théorème de convergence des sommes de Riemann pour $f$ continue sur $[a,b]$ ?
?
**Réponse:**
$\frac{b-a}{n}\sum_{k=0}^{n-1}f\left(a+k\frac{b-a}{n}\right)\longrightarrow\int_a^b f(t)\,dt$.
