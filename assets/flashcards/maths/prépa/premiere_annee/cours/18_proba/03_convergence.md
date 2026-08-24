#flashcards/maths/prépa/premiere_annee/cours/18_proba/convergence
## 1. Inégalité de Markov
Énoncer l'inégalité de Markov pour une variable positive $X$.
?
**Réponse:**
Pour $a>0$, $\mathbb P(X\ge a)\le\frac{\mathbb E(X)}a$.

## 2. Inégalité de Bienaymé-Tchebychev
Énoncer l'inégalité de Tchebychev.
?
**Réponse:**
Si $X$ admet une variance, alors pour $\varepsilon>0$, $\mathbb P(|X-\mathbb E(X)|\ge\varepsilon)\le\frac{\operatorname{Var}(X)}{\varepsilon^2}$.

## 3. Convergence en probabilité
Que signifie $X_n\xrightarrow{\mathbb P}X$ ?
?
**Réponse:**
Pour tout $\varepsilon>0$, $\mathbb P(|X_n-X|>\varepsilon)\to0$.

## 4. Convergence en loi
Que signifie $X_n\xrightarrow{\mathcal L}X$ ?
?
**Réponse:**
Pour tout point de continuité $x$ de $F_X$, on a $F_{X_n}(x)\to F_X(x)$.

## 5. Loi faible des grands nombres
Quel énoncé retenir pour une moyenne de variables i.i.d. d'espérance $m$ et variance finie ?
?
**Réponse:**
Si $\overline X_n=\frac1n\sum_{k=1}^nX_k$, alors $\overline X_n\xrightarrow{\mathbb P}m$.
