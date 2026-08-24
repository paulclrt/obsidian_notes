#flashcards/maths/prépa/premiere_annee/cours/18_proba/variables_lois
## 1. Variable aléatoire discrète
Qu'est-ce qu'une variable aléatoire discrète réelle ?
?
**Réponse:**
C'est une application $X:\Omega\to\mathbb R$ prenant un ensemble fini ou dénombrable de valeurs, dont les événements $\{X=x\}$ sont mesurables.

## 2. Loi d'une variable discrète
Comment une loi discrète est-elle décrite ?
?
**Réponse:**
Par les valeurs $x_i$ possibles et les probabilités $\mathbb P(X=x_i)$.
Elles sont positives et leur somme vaut $1$.

## 3. Lois usuelles
Donner les lois de Bernoulli et binomiale.
?
**Réponse:**
$X\sim\mathcal B(p)$ si $\mathbb P(X=1)=p$ et $\mathbb P(X=0)=1-p$.
$X\sim\mathcal B(n,p)$ compte les succès de $n$ épreuves de Bernoulli indépendantes de paramètre $p$.

## 4. Loi conjointe et marginales
Comment définir la loi conjointe de $(X,Y)$ et ses marginales ?
?
**Réponse:**
La loi conjointe donne $\mathbb P(X=x,Y=y)$.
Les marginales s'obtiennent par sommation : $\mathbb P(X=x)=\sum_y\mathbb P(X=x,Y=y)$.

## 5. Indépendance de variables
Quel critère caractérise l'indépendance de variables discrètes $X,Y$ ?
?
**Réponse:**
Elles sont indépendantes si, pour tous $x,y$, $\mathbb P(X=x,Y=y)=\mathbb P(X=x)\mathbb P(Y=y)$.

## 6. Espérance
Comment définit-on $\mathbb E(X)$ pour une variable discrète intégrable ?
?
**Réponse:**
$\mathbb E(X)=\sum_xx\,\mathbb P(X=x)$, lorsque la somme est absolument convergente.
L'espérance est linéaire.

## 7. Variance
Donner les deux formules essentielles de variance.
?
**Réponse:**
$\operatorname{Var}(X)=\mathbb E((X-\mathbb E(X))^2)$.
$\operatorname{Var}(X)=\mathbb E(X^2)-\mathbb E(X)^2$.

## 8. Covariance
Définir la covariance et donner son lien avec l'indépendance.
?
**Réponse:**
$\operatorname{Cov}(X,Y)=\mathbb E(XY)-\mathbb E(X)\mathbb E(Y)$.
Des variables indépendantes intégrables ont une covariance nulle ; la réciproque est fausse en général.
