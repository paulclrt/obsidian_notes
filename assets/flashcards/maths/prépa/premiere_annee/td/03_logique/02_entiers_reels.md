#flashcards/maths/prépa/premiere_annee/td/03_logique/entiers_reels
## 1. Bézout effectif
Calculer $\gcd(252,198)$ et donner une relation de Bézout.
?
**Réponse:**
L'algorithme d'Euclide donne $\gcd(252,198)=18$.
Une remontée fournit $18=4\times252-5\times198$.

## 2. Congruence et puissances
Déterminer le reste de $7^{100}$ dans la division par $13$.
?
**Réponse:**
$7^2\equiv10\ [13]$, $7^3\equiv5\ [13]$ et $7^6\equiv-1\ [13]$.
Donc $7^{100}\equiv7^4\equiv9\ [13]$.

## 3. Équation diophantienne
Résoudre dans $\mathbb Z^2$ l'équation $14x+21y=35$.
?
**Réponse:**
On divise par $7$ : $2x+3y=5$.
Les solutions sont $x=1+3k$ et $y=1-2k$ pour $k\in\mathbb Z$.

## 4. Borne supérieure
Déterminer $\sup\{\frac n{n+1}\mid n\in\mathbb N\}$ et dire s'il est atteint.
?
**Réponse:**
Le supremum vaut $1$.
Chaque terme est strictement inférieur à $1$, donc $1$ n'est pas atteint ; la suite tend vers $1$.

## 5. Partie entière
Résoudre dans $\mathbb R$ l'équation $\lfloor x\rfloor+\lfloor2x\rfloor=5$.
?
**Réponse:**
Poser $n=\lfloor x\rfloor$ et examiner les intervalles $[n,n+1[$.
Les solutions sont $x\in[2,\frac52[$.
