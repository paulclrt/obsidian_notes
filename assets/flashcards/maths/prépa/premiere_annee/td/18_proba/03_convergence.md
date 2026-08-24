#flashcards/maths/prépa/premiere_annee/td/18_proba/convergence
## 1. Moyenne de Bernoulli
Soient $X_1,\ldots,X_n$ i.i.d. de loi $\mathcal B(p)$. Majoriser $\mathbb P(|\overline X_n-p|\ge\varepsilon)$.
?
**Réponse:**
$\mathbb E(\overline X_n)=p$ et $\operatorname{Var}(\overline X_n)=\frac{p(1-p)}n$.
Par Tchebychev, $\mathbb P(|\overline X_n-p|\ge\varepsilon)\le\frac{p(1-p)}{n\varepsilon^2}$.
