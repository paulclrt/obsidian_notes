#flashcards/maths/prépa/premiere_annee/fiche/09_suites_vecteurs

## 1. Définition d'une norme
Définir une norme sur un $\mathbb{K}$-espace vectoriel $E$.
?
**Réponse:**
Application $N : E \to \mathbb{R}$ vérifiant pour tout $(x, y, \lambda) \in E \times E \times \mathbb{K}$ : $N(x) \geq 0$ (positivité), $N(x) = 0 \Rightarrow x = 0$ (définie), $N(\lambda x) = |\lambda| N(x)$ (homogène), $N(x + y) \leq N(x) + N(y)$ (inégalité triangulaire). Le couple $(E, N)$ est un espace vectoriel normé.

## 2. Corollaire de l'inégalité triangulaire
Énoncer le corollaire de l'inégalité triangulaire et ses conséquences.
?
**Réponse:**
$$
\forall (x, y) \in E^2, \quad |N(x) - N(y)| \leq N(x - y)
$$
En particulier la norme est 1-lipschitzienne, donc si $x_n \to l$ alors $\|x_n\| \to \|l\|$.

## 3. Normes usuelles sur $\mathbb{K}^n$
Donner les trois normes classiques sur $\mathbb{K}^n$.
?
**Réponse:**
$$
\|x\|_1 = \sum_{i=1}^{n} |x_i|, \qquad
\|x\|_2 = \sqrt{\sum_{i=1}^{n} |x_i|^2}, \qquad
\|x\|_{\infty} = \max_{1 \leq i \leq n} |x_i|
$$
Pour $p \geq 1$, $\|x\|_p = \left( \sum |x_i|^p \right)^{1/p}$ est une norme (hors programme) et $\|x\|_p \to \|x\|_{\infty}$.

## 4. Normes usuelles sur $\mathcal{C}([a, b], \mathbb{K})$
Donner les trois normes classiques sur $\mathcal{C}([a, b], \mathbb{K})$.
?
**Réponse:**
$$
\|f\|_1 = \int_a^b |f|, \qquad
\|f\|_2 = \sqrt{\int_a^b |f|^2}, \qquad
\|f\|_{\infty} = \sup_{x \in [a, b]} |f(x)|
$$
Sur un produit $E_1 \times \cdots \times E_p$ : $N_1 = \sum \|x_i\|_i$, $N_2 = \sqrt{\sum \|x_i\|_i^2}$, $N_{\infty} = \max \|x_i\|_i$.

## 5. Distance, boules, sphères
Définir la distance associée à la norme, les boules et la sphère.
?
**Réponse:**
$d(x, y) = \|x - y\|$ ; $(E, d)$ est un espace métrique. Boule ouverte $B_o(a, r) = \{d(a, x) < r\}$, boule fermée $B_f(a, r) = \{d(a, x) \leq r\}$, sphère $S(a, r) = \{d(a, x) = r\}$. Les boules sont convexes (propriété propre aux e.v.n.).

## 6. Parties bornées et diamètre
Caractériser une partie bornée et définir le diamètre.
?
**Réponse:**
$A \subset E$ est bornée ssi $\{\|x\| \mid x \in A\}$ est borné, ce qui équivaut à $A \subset B_f(x_0, R)$ pour un certain $(x_0, R)$. Diamètre : $\delta(A) = \sup_{x, y \in A} d(x, y)$ ; $\delta(B_f(a, r)) \leq 2r$, avec égalité si $E \neq \{0\}$.

## 7. Applications lipschitziennes
Définir une application k-lipschitzienne et citer des exemples.
?
**Réponse:**
$f$ est $k$-lipschitzienne ssi $\forall (x, y) \in D_f^2$, $d(f(x), f(y)) \leq k \, d(x, y)$ ($k < 1$ : $k$-contractante). La composée de $k$ et $k'$-lipschitziennes est $kk'$-lipschitzienne. Exemples 1-lipschitziennes : la norme, $x \mapsto d(x, A)$, les projections.

## 8. Normes équivalentes
Définir deux normes équivalentes et donner la chaîne classique.
?
**Réponse:**
$\exists (\alpha, \beta) \in (\mathbb{R}_+^*)^2$, $\forall x$, $\|x\|_1 \leq \alpha \|x\|_2$ et $\|x\|_2 \leq \beta \|x\|_1$. Sur un produit : $\|x\|_{\infty} \leq \|x\|_2 \leq \|x\|_1 \leq p \|x\|_{\infty}$. En dimension finie toutes les normes sont équivalentes ; les notions de bornitude, lipschitzianité et convergence sont inchangées.

## 9. Convergence d'une suite de vecteurs
Définir la convergence d'une suite $(x_n)$ vers $l$.
?
**Réponse:**
$$
\forall \varepsilon > 0, \ \exists N \in \mathbb{N}, \ \forall n \geq N, \quad d(x_n, l) \leq \varepsilon
$$
ce qui équivaut à $d(x_n, l) \to 0$ (et à $\|x_n - l\| \to 0$). Inégalités strictes ou larges indifféremment.

## 10. Limite : unicité, normes équivalentes
Citer les propriétés fondamentales de la limite.
?
**Réponse:**
La limite est unique. Si $x_n \to l$, alors $\|x_n\| \to \|l\|$ (réciproque fausse), $\|x_n\| \to 0 \iff x_n \to 0$. Toute suite convergente est bornée. Deux normes équivalentes donnent les mêmes suites convergentes.

## 11. Principe des gendarmes
Énoncer le principe des gendarmes dans un espace vectoriel normé.
?
**Réponse:**
S'il existe une suite réelle $(g_n)$ avec $\forall n$, $d(x_n, l) \leq g_n$ et $g_n \to 0$, alors $x_n \to l$. Version réelle : $g_n \leq p_n \leq g'_n$ et $g_n, g'_n \to l$ impliquent $p_n \to l$ (s'adapte aux limites infinies).

## 12. Opérations sur les limites
Donner les règles de somme et de produit par un scalaire.
?
**Réponse:**
$x_n \to l$, $y_n \to l'$ $\Rightarrow$ $x_n + y_n \to l + l'$ ; $(x_n + y_n)$ converge $\Rightarrow$ $(x_n)$ et $(y_n)$ ont même nature. $\alpha_n \to \alpha$, $l_n \to l$ $\Rightarrow$ $\alpha_n l_n \to \alpha l$. $(\alpha_n)$ bornée et $x_n \to 0$ $\Rightarrow$ $\alpha_n x_n \to 0$.

## 13. Convergence dans un produit et suites de complexes
Caractériser la convergence dans un produit et pour les complexes.
?
**Réponse:**
Dans $E_1 \times \cdots \times E_p$ (norme classique) : $(x_n) \to l$ ssi chaque coordonnée converge. Pour les complexes : $z_n \to l \iff \mathrm{Re}(z_n) \to \mathrm{Re}(l)$ et $\mathrm{Im}(z_n) \to \mathrm{Im}(l)$ ; si $x_n \to l \neq 0$, $\frac{1}{x_n} \to \frac{1}{l}$.

## 14. Récurrences : arithmético-géométrique et ordre 2
Rappeler les formules des suites $u_{n+1} = a u_n + b$ et $u_{n+2} = a u_{n+1} + b u_n$.
?
**Réponse:**
Si $a \neq 1$, point fixe $c = ac + b$ et $u_n - c = a^n (u_0 - c)$. Pour l'ordre 2 : $\chi = X^2 - aX - b$ ; si $\Delta \neq 0$, $u_n = C_1 \lambda_1^n + C_2 \lambda_2^n$ ; si $\Delta = 0$, $u_n = \lambda^n (C_1 + n C_2)$ ; si $\Delta < 0$ dans $\mathbb{R}$, forme réelle $u_n = \rho^n (D_1 \cos(n\theta) + D_2 \sin(n\theta))$.

## 15. Limites infinies et formes indéterminées
Donner les principales règles de calcul et formes indéterminées.
?
**Réponse:**
$\varepsilon \infty + y \to \varepsilon \infty$ ; $\varepsilon \infty \times y > 0 \to \varepsilon \infty$ ; $\varepsilon \infty \times \varepsilon' \infty \to \varepsilon \varepsilon' \infty$ ; $\frac{1}{x_n} \to 0$ si $x_n \to \varepsilon \infty$ ; $\frac{1}{x_n} \to +\infty$ si $x_n \to 0^+$. Formes indéterminées : $\infty - \infty$, $0 \times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$, $1^{\infty}$, $\infty^0$, $0^0$ (pour $a_n^{b_n}$, écrire $e^{b_n \ln a_n}$).

## 16. Relation d'ordre et limites
Citer les résultats reliant limites et inégalités.
?
**Réponse:**
Lemme du tunnel : si $u_n \to l$ et $a < l < b$, alors $a < u_n < b$ à partir d'un certain rang (faux pour des inégalités larges). Si $a_n \leq b_n$ pour tout $n$, alors $\lim a_n \leq \lim b_n$ (valable avec $\pm\infty$).

## 17. Théorème de la limite monotone
Énoncer le théorème de la limite monotone.
?
**Réponse:**
Suite croissante : converge vers $\sup x_n$ si elle est majorée, vers $+\infty$ sinon. Suite décroissante : converge vers $\inf x_n$ si elle est minorée, vers $-\infty$ sinon. Conséquence : suite géométrique $a^n x_0$ tend vers $0$ si $|a| < 1$, est constante si $a = 1$.

## 18. Suites adjacentes et segments emboîtés
Énoncer les théorèmes des suites adjacentes et des segments emboîtés.
?
**Réponse:**
Adjacentes (une croissante, une décroissante, différence $\to 0$) : convergence vers une limite commune $l$ avec $x_p \leq l \leq y_q$ pour tout $(p, q)$. Segments emboîtés : $\bigcap [a_n, b_n]$ avec longueurs $\to 0$ est un singleton $\{l\}$.

## 19. Suites extraites et valeurs d'adhérence
Définir extraction et valeur d'adhérence.
?
**Réponse:**
Extraction : $\phi : \mathbb{N} \to \mathbb{N}$ strictement croissante ; suite extraite $(x_{\phi(n)})$. Toute suite extraite d'une suite convergente converge vers la même limite. Valeur d'adhérence = limite d'une suite extraite ; la limite d'une suite convergente est son unique valeur d'adhérence.

## 20. Bolzano-Weierstrass
Énoncer le théorème de Bolzano-Weierstrass et définir limsup/liminf.
?
**Réponse:**
Toute suite bornée de réels (ou de complexes) possède une valeur d'adhérence.
$$
\overline{\lim} \, x_n = \lim \left( \sup_{k \geq n} x_k \right), \quad
\underline{\lim} \, x_n = \lim \left( \inf_{k \geq n} x_k \right)
$$
limsup = plus grande valeur d'adhérence, liminf = plus petite.

## 21. Suites de Cauchy et complétude
Définir une suite de Cauchy et un espace complet.
?
**Réponse:**
$(x_n)$ de Cauchy : $\forall \varepsilon > 0$, $\exists N$, $\forall p, q \geq N$, $d(x_p, x_q) \leq \varepsilon$. Toute suite convergente est de Cauchy ; toute suite de Cauchy est bornée ; une suite de Cauchy avec valeur d'adhérence converge. Espace complet : toute suite de Cauchy converge. $\mathbb{R}$ et $\mathbb{C}$ sont complets, $\mathbb{Q}$ ne l'est pas.
