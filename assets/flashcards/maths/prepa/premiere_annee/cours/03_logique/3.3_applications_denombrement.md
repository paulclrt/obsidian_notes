#flashcards/maths/prépa/premiere_annee/cours/03_logique/applications_denombrement
## 1. Composition d'applications
Comment définit-on $g\circ f$ lorsque $f:E\to F$ et $g:F\to G$ ?
?
**Réponse:**
$(g\circ f):E\to G$ est définie par $(g\circ f)(x)=g(f(x))$.
La composition est associative mais n'est pas commutative en général.
<!--SR:!2026-09-14,15,290-->

## 2. Image directe et image réciproque
Définir $f(A)$ et $f^{-1}(B)$ pour $A\subset E$ et $B\subset F$.
?
**Réponse:**
$f(A)=\{f(x)\mid x\in A\}$.
$f^{-1}(B)=\{x\in E\mid f(x)\in B\}$.
L'image réciproque est définie même si $f$ n'est pas bijective.
<!--SR:!2026-09-02,3,250-->

## 3. Injectivité, surjectivité et bijectivité
Donner les trois définitions pour $f:E\to F$.
?
**Réponse:**
Injective : $f(x)=f(y)\Rightarrow x=y$.
Surjective : $\forall y\in F,\ \exists x\in E,\ f(x)=y$.
Bijective : injective et surjective ; $f$ admet alors une réciproque $f^{-1}:F\to E$.
<!--SR:!2026-09-01,2,230-->

## 4. Monotonie et injectivité
Quel lien entre stricte monotonie et injectivité sur un intervalle réel ?
?
**Réponse:**
Une fonction strictement croissante ou strictement décroissante sur un intervalle est injective.
Une fonction monotone non stricte n'est pas nécessairement injective.
<!--SR:!2026-09-02,3,250-->

## 5. Cardinal d'un ensemble fini
Quel est le cardinal d'une union disjointe et d'un produit cartésien finis ?
?
**Réponse:**
Si $A\cap B=\varnothing$, alors $|A\cup B|=|A|+|B|$.
Pour tous ensembles finis $A,B$, $|A\times B|=|A|\,|B|$.
<!--SR:!2026-09-02,3,250-->

## 6. Principe des tiroirs
Énoncer le principe des tiroirs.
?
**Réponse:**
Toute application d'un ensemble fini de cardinal strictement supérieur à celui de l'ensemble d'arrivée n'est pas injective.
Donc deux éléments distincts ont la même image.
<!--SR:!2026-09-02,3,250-->

## 7. Arrangements et combinaisons
Quelle différence entre arrangements et combinaisons de $p$ éléments parmi $n$ ?
?
**Réponse:**
Les arrangements, où l'ordre compte, sont au nombre de $\frac{n!}{(n-p)!}$.
Les combinaisons, où l'ordre ne compte pas, sont au nombre de $\binom np=\frac{n!}{p!(n-p)!}$.
<!--SR:!2026-09-02,3,250-->

## 8. Coefficients binomiaux
Quelles identités de base vérifient les coefficients binomiaux ?
?
**Réponse:**
$\binom nk=\binom n{n-k}$.
$\binom nk=\binom{n-1}k+\binom{n-1}{k-1}$ pour $1\le k\le n-1$.
$\sum_{k=0}^n\binom nk=2^n$.
<!--SR:!2026-09-02,3,230-->

## 9. Binôme de Newton
Énoncer la formule du binôme de Newton.
?
**Réponse:**
Pour $n\in\mathbb N$, $(a+b)^n=\sum_{k=0}^n\binom nk a^kb^{n-k}$.
<!--SR:!2026-08-31,1,210-->

## 10. Somme télescopique
Quelle méthode utiliser pour calculer une somme dont le terme général s'écrit $u_k=v_{k+1}-v_k$ ?
?
**Réponse:**
$\sum_{k=m}^n u_k=v_{n+1}-v_m$.
Les termes intermédiaires s'annulent deux à deux.
<!--SR:!2026-09-02,3,230-->
