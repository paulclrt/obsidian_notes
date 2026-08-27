#flashcards/maths/prépa/premiere_annee/td/03_logique/applications_denombrement
## 1. Image réciproque
Soit $f:\mathbb R\to\mathbb R$, $f(x)=x^2$. Calculer $f^{-1}([1,4])$.
?
**Réponse:**
$f^{-1}([1,4])=\{x\in\mathbb R\mid1\le x^2\le4\}=[-2,-1]\cup[1,2]$.
<!--SR:!2026-08-27,1,230-->

## 2. Bijectivité sur un domaine
Montrer que $f:x\mapsto x^3+x$ est une bijection de $\mathbb R$ sur $\mathbb R$.
?
**Réponse:**
$f'(x)=3x^2+1>0$, donc $f$ est strictement croissante et injective.
Ses limites en $-\infty$ et $+\infty$ sont respectivement $-\infty$ et $+\infty$ ; elle est donc surjective.
<!--SR:!2026-08-27,1,230-->

## 3. Choix sans ordre
Combien y a-t-il de mains de $5$ cartes dans un jeu de $52$ cartes ?
?
**Réponse:**
L'ordre des cartes ne compte pas : il y a $\binom{52}{5}$ mains.
<!--SR:!2026-08-30,4,270-->

## 4. Principe des tiroirs
Montrer que parmi $13$ entiers, deux ont le même reste modulo $12$.
?
**Réponse:**
Il n'existe que $12$ restes possibles modulo $12$.
Le principe des tiroirs impose que deux des $13$ entiers aient le même reste.
<!--SR:!2026-08-26,0,230-->

## 5. Somme télescopique
Calculer $\sum_{k=1}^n\frac1{k(k+1)}$.
?
**Réponse:**
$\frac1{k(k+1)}=\frac1k-\frac1{k+1}$.
La somme télescope et vaut $1-\frac1{n+1}=\frac n{n+1}$.
<!--SR:!2026-08-26,0,230-->
