#flashcards/maths/prépa/premiere_annee/td/03_logique/ensembles_logique
## 1. Négation d'une suite majorée
Écrire avec des quantificateurs : « la suite réelle $(u_n)$ n'est pas majorée ».
?
**Réponse:**
$\forall M\in\mathbb R,\ \exists n\in\mathbb N,\ u_n>M$.
La négation porte à la fois sur l'existence du majorant et sur l'inégalité $u_n\le M$.

## 2. Négation d'une assertion doublement quantifiée
Nier correctement : « dans chaque devoir, il existe une question qu'aucun élève ne sait résoudre ».
?
**Réponse:**
Il existe un devoir tel que toute question de ce devoir est résolue par au moins un élève.
On inverse successivement les quantificateurs en gardant leur ordre.

## 3. Ensemble défini par une propriété universelle
Montrer que $\{x\in\mathbb R\mid\forall\varepsilon>0,\ x> -\varepsilon\}=\mathbb R_+$.
?
**Réponse:**
Si $x\ge0$, alors $x> -\varepsilon$ pour tout $\varepsilon>0$.
Réciproquement, si $x<0$, choisir $\varepsilon=-x/2>0$ ; alors $x> -\varepsilon=x/2$ est impossible.
<!--SR:!2026-08-27,1,230-->

## 4. Différence symétrique
Montrer que $A\setminus B=B\setminus A$ et interpréter cet ensemble.
?
**Réponse:**
$A\setminus B=A\cap B^c$ et $B\setminus A=B\cap A^c$.
Cet ensemble contient les éléments appartenant à exactement l'un des deux ensembles $A$ et $B$.

## 5. Équation ensembliste
Résoudre dans $\mathcal P(E)$ l'équation $(A\cap X)\cup(B\cap X)=\varnothing$.
?
**Réponse:**
L'équation équivaut à $(A\cup B)\cap X=\varnothing$.
Les solutions sont exactement les parties $X\subset(A\cup B)^c$.

## 6. Produit cartésien et intersection
Montrer que $(A\times C)\cap(B\times D)=(A\cap B)\times(C\cap D)$.
?
**Réponse:**
Pour un couple $(x,y)$, appartenir au membre de gauche signifie $x\in A$, $y\in C$, $x\in B$ et $y\in D$.
Cela équivaut à $x\in A\cap B$ et $y\in C\cap D$, soit l'appartenance au membre de droite.

## 7. Formule logique à transformer
Montrer que $A\Rightarrow(B\land C)$ est équivalente à $(A\Rightarrow B)\land(A\Rightarrow C)$.
?
**Réponse:**
Les deux propositions sont vraies exactement lorsque, dès que $A$ est vraie, $B$ et $C$ le sont toutes les deux.
On peut aussi écrire $A\Rightarrow B$ comme $\neg A\lor B$ et distribuer $\lor$ sur $\land$.
<!--SR:!2026-08-26,0,230-->

## 8. Contraposée utile
Démontrer : si $n^2$ est pair, alors $n$ est pair.
?
**Réponse:**
Raisonner par contraposée.
Si $n$ est impair, $n=2k+1$, donc $n^2=4k(k+1)+1$ est impair.
Ainsi $n^2$ pair implique $n$ pair.

## 9. Existence et unicité
Résoudre dans $\mathbb R$ l'équation $x+\sqrt{x}=2$ et justifier l'unicité.
?
**Réponse:**
Poser $t=\sqrt{x}\ge0$ : l'équation devient $t^2+t-2=0$, donc $t=1$ et $x=1$.
La contrainte $t\ge0$ élimine l'autre racine ; la solution est donc unique.

## 10. Relation d'équivalence
Sur $\mathbb Z$, montrer que $a\sim b\Longleftrightarrow 5\mid(a-b)$ est une relation d'équivalence.
?
**Réponse:**
Réflexivité : $5\mid(a-a)$.
Symétrie : si $5\mid(a-b)$, alors $5\mid(b-a)$.
Transitivité : si $5\mid(a-b)$ et $5\mid(b-c)$, alors $5\mid(a-c)$.

## 11. Récurrence : somme des entiers
Montrer par récurrence que $\sum_{k=1}^n k=\frac{n(n+1)}2$ pour tout $n\in\mathbb N^*$.
?
**Réponse:**
Initialisation : l'égalité est vraie pour $n=1$.
Hérédité : ajouter $n+1$ à $\frac{n(n+1)}2$ donne $\frac{(n+1)(n+2)}2$.

## 12. Analyse-synthèse : système symétrique
Résoudre dans $\mathbb R^2$ le système $x+y=5$ et $x^2+y^2=13$.
?
**Réponse:**
De $(x+y)^2=x^2+y^2+2xy$, on obtient $xy=6$.
Les nombres $x,y$ sont donc les racines de $T^2-5T+6$, soit $2$ et $3$.
Les solutions sont $(2,3)$ et $(3,2)$.
