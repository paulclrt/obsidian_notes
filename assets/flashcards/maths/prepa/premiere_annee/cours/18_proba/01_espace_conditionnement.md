#flashcards/maths/prépa/premiere_annee/cours/18_proba/espace_conditionnement
## 1. Espace probabilisé
Quels objets composent un espace probabilisé ?
?
**Réponse:**
Il est formé d'un univers $\Omega$, d'une tribu $\mathcal F$ d'événements et d'une probabilité $\mathbb P$ définie sur $\mathcal F$.

## 2. Système complet d'événements
Qu'est-ce qu'un système complet d'événements ?
?
**Réponse:**
C'est une famille d'événements deux à deux disjoints dont la réunion est $\Omega$.
On l'appelle aussi une partition de l'univers.
<!--SR:!2026-09-03,4,270-->

## 3. Formules élémentaires
Quelles formules de probabilité faut-il savoir utiliser immédiatement ?
?
**Réponse:**
$\mathbb P(A^c)=1-\mathbb P(A)$.
$\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)$.
Si $A\subset B$, $\mathbb P(B\setminus A)=\mathbb P(B)-\mathbb P(A)$.

## 4. Probabilité conditionnelle
Définir $\mathbb P(A\mid B)$ lorsque $\mathbb P(B)>0$.
?
**Réponse:**
$\mathbb P(A\mid B)=\frac{\mathbb P(A\cap B)}{\mathbb P(B)}$.
Donc $\mathbb P(A\cap B)=\mathbb P(A\mid B)\mathbb P(B)$.

## 5. Probabilités totales
Énoncer la formule des probabilités totales.
?
**Réponse:**
Si $(B_i)$ est un système complet avec $\mathbb P(B_i)>0$, alors $\mathbb P(A)=\sum_i\mathbb P(A\mid B_i)\mathbb P(B_i)$.

## 6. Formule de Bayes
Comment calculer $\mathbb P(B_j\mid A)$ à partir d'une partition $(B_i)$ ?
?
**Réponse:**
$\mathbb P(B_j\mid A)=\frac{\mathbb P(A\mid B_j)\mathbb P(B_j)}{\sum_i\mathbb P(A\mid B_i)\mathbb P(B_i)}$, si $\mathbb P(A)>0$.

## 7. Indépendance d'événements
Quel critère caractérise l'indépendance de $A$ et $B$ ?
?
**Réponse:**
$A$ et $B$ sont indépendants si $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$.
Si $\mathbb P(B)>0$, cela équivaut à $\mathbb P(A\mid B)=\mathbb P(A)$.
