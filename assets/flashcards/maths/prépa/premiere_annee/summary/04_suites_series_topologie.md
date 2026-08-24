#flashcards/maths/prépa/premiere_annee/summary/suites_series_topologie
## 1. Limite d'une suite dans un espace normé
Que signifie $u_n\to\ell$ dans un espace normé ?
?
**Réponse:**
Pour tout $\varepsilon>0$, il existe $N\in\mathbb N$ tel que $n\ge N\Rightarrow\|u_n-\ell\|<\varepsilon$.
La limite, si elle existe, est unique.

## 2. Suite de Cauchy
Définir une suite de Cauchy et rappeler le lien avec la convergence.
?
**Réponse:**
$(u_n)$ est de Cauchy si $\forall\varepsilon>0$, il existe $N$ tel que $p,q\ge N\Rightarrow\|u_p-u_q\|<\varepsilon$.
Toute suite convergente est de Cauchy.
Dans un espace complet, toute suite de Cauchy converge.

## 3. Suites adjacentes
Quel résultat donne le théorème des suites adjacentes ?
?
**Réponse:**
Si $(u_n)$ est croissante, $(v_n)$ décroissante et $v_n-u_n\to0$, alors les deux suites convergent vers la même limite.

## 4. Sous-suite et valeur d'adhérence
Qu'est-ce qu'une valeur d'adhérence d'une suite ?
?
**Réponse:**
$\ell$ est une valeur d'adhérence de $(u_n)$ s'il existe une sous-suite $(u_{\varphi(n)})$ qui converge vers $\ell$.
Une suite réelle bornée admet au moins une valeur d'adhérence.

## 5. Série convergente
Définir la convergence d'une série $\sum u_n$.
?
**Réponse:**
La série converge si la suite de ses sommes partielles $S_n=\sum_{k=0}^n u_k$ converge.
Sa somme est alors $\sum_{k=0}^{\infty}u_k=\lim S_n$.
Condition nécessaire : $u_n\to0$.

## 6. Série géométrique
Quand la série géométrique $\sum_{n\ge0}q^n$ converge-t-elle, et quelle est sa somme ?
?
**Réponse:**
Elle converge si et seulement si $|q|<1$.
Dans ce cas, $\sum_{n=0}^{\infty}q^n=\frac1{1-q}$.

## 7. Séries à termes positifs : comparaison
Quel est le critère de comparaison pour deux séries à termes positifs ?
?
**Réponse:**
Si $0\le u_n\le v_n$ à partir d'un certain rang et si $\sum v_n$ converge, alors $\sum u_n$ converge.
Si $u_n\ge v_n\ge0$ à partir d'un certain rang et si $\sum v_n$ diverge, alors $\sum u_n$ diverge.

## 8. Séries de Riemann
Quel est le critère de convergence de $\sum_{n\ge1}\frac1{n^\alpha}$ ?
?
**Réponse:**
La série de Riemann converge si et seulement si $\alpha>1$.
Elle diverge pour $\alpha\le1$.

## 9. Convergence absolue
Quel est le lien entre convergence absolue et convergence d'une série réelle ou complexe ?
?
**Réponse:**
Si $\sum |u_n|$ converge, alors $\sum u_n$ converge.
On dit que $\sum u_n$ converge absolument.

## 10. Ouverts et fermés
Définir un ouvert et un fermé d'un espace métrique $E$.
?
**Réponse:**
$U\subset E$ est ouvert si, pour tout $x\in U$, il existe $r>0$ tel que $B(x,r)\subset U$.
$F\subset E$ est fermé si son complémentaire $E\setminus F$ est ouvert.
Un fermé contient les limites de toutes les suites convergentes de ses éléments.

## 11. Continuité séquentielle
Comment caractériser la continuité de $f:E\to F$ en $a$ par les suites ?
?
**Réponse:**
$f$ est continue en $a$ si et seulement si, pour toute suite $(x_n)$ telle que $x_n\to a$, on a $f(x_n)\to f(a)$.

## 12. Compacité en dimension finie
Quel critère caractérise les compacts de $\mathbb R^n$ ?
?
**Réponse:**
Dans un espace vectoriel normé de dimension finie, une partie est compacte si et seulement si elle est fermée et bornée.
