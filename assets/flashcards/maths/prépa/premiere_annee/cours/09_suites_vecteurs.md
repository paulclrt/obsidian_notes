#flashcards/maths/prépa/premiere_annee/cours/09_suites_vecteurs

## 1. Définition d'une norme
Soit $E$ un $\mathbb{K}$-espace vectoriel ($\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$). Définir une norme sur $E$ et un espace vectoriel normé.
?
**Réponse:**
Une norme sur $E$ est une application $N : E \to \mathbb{R}$ telle que, pour tout $(x, y, \lambda) \in E \times E \times \mathbb{K}$ :
$$
\begin{cases}
N(x) \geq 0 & \text{(positivité)} \\
N(x) = 0 \Rightarrow x = 0 & \text{($N$ est définie)} \\
N(\lambda x) = |\lambda| N(x) & \text{($N$ est homogène)} \\
N(x + y) \leq N(x) + N(y) & \text{(inégalité triangulaire)}
\end{cases}
$$
Le couple $(E, N)$ est alors un espace vectoriel normé.

## 2. Notation d'une norme et valeur de $\|0\|$
Comment note-t-on une norme et que vaut $\|0\|$ ?
?
**Réponse:**
On note $\|\cdot\| : E \to \mathbb{R}_+$, $x \mapsto \|x\|$. On a $\|0_E\| = |0_{\mathbb{K}}| \cdot \|0_E\| = 0$. Dire « $E$ est un espace vectoriel normé » sous-entend le choix d'une norme que l'on notera $\|\cdot\|$.

## 3. Corollaire de l'inégalité triangulaire
Énoncer le corollaire de l'inégalité triangulaire pour une norme.
?
**Réponse:**
Pour tout $(x, y) \in E^2$ :
$$
|N(x) - N(y)| \leq N(x - y)
$$
En particulier, l'application norme $\|\cdot\|$ est 1-lipschitzienne.

## 4. Vecteurs unitaires et norme induite
Quand dit-on qu'un vecteur $u$ est unitaire ? Que vaut le vecteur unitaire associé à $u \neq 0$ ? Qu'est-ce que la norme induite ?
?
**Réponse:**
$u$ est unitaire ssi $\|u\| = 1$. Si $u \neq 0$, le vecteur $\frac{u}{\|u\|}$ est unitaire. La norme induite sur un sous-espace vectoriel $F$ de $E$ est la restriction à $F$ de la norme de $E$, et $(F, \text{norme induite})$ est un espace vectoriel normé.

## 5. Les normes 1, 2 et $\infty$ sur $\mathbb{K}^n$
Définir les normes classiques sur $\mathbb{K}^n$.
?
**Réponse:**
Pour $x = (x_1, \ldots, x_n) \in \mathbb{K}^n$ :
$$
\|x\|_1 = \sum_{i=1}^{n} |x_i|, \qquad
\|x\|_2 = \sqrt{\sum_{i=1}^{n} |x_i|^2}, \qquad
\|x\|_{\infty} = \max_{1 \leq i \leq n} |x_i|
$$
Ce sont des normes sur $\mathbb{K}^n$. Plus généralement, pour $p \in [1, +\infty[$, $\|x\|_p = \left( \sum_{i=1}^{n} |x_i|^p \right)^{1/p}$ est une norme (hors programme), et $\|x\|_p \to \|x\|_{\infty}$ lorsque $p \to +\infty$.

## 6. Normes classiques sur un produit d'espaces
Soient $E_1, \ldots, E_p$ des espaces vectoriels normés de normes respectives $\|\cdot\|_1, \ldots, \|\cdot\|_p$. Quelles normes peut-on mettre sur $E = E_1 \times \cdots \times E_p$ ?
?
**Réponse:**
Pour $x = (x_1, \ldots, x_p) \in E$ :
$$
N_1(x) = \sum_{i=1}^{p} \|x_i\|_i, \qquad
N_2(x) = \sqrt{\sum_{i=1}^{p} \|x_i\|_i^2}, \qquad
N_{\infty}(x) = \max_{1 \leq i \leq p} \|x_i\|_i
$$
Ces trois applications sont des normes sur le produit $E$.

## 7. Normes classiques sur $\mathcal{C}([a, b], \mathbb{K})$
Soient $a, b \in \mathbb{R}$ avec $a < b$. Quelles normes met-on sur $\mathcal{C}([a, b], \mathbb{K})$ ?
?
**Réponse:**
Pour $f \in \mathcal{C}([a, b], \mathbb{K})$ :
$$
\|f\|_1 = \int_a^b |f(x)| \, dx, \qquad
\|f\|_2 = \sqrt{\int_a^b |f(x)|^2 \, dx}, \qquad
\|f\|_{\infty} = \sup_{x \in [a, b]} |f(x)|
$$
Ce sont trois normes classiques. Séparation pour $\|\cdot\|_1$ : si $\int_a^b |f| = 0$ avec $f$ continue et positive en module, alors $f = 0$.

## 8. Distance associée à une norme et espace métrique
Définir la distance associée à une norme et la notion d'espace métrique.
?
**Réponse:**
$$
d : E^2 \to \mathbb{R}_+, \quad (x, y) \mapsto \|x - y\|
$$
est la distance associée à la norme. Un espace métrique est un couple $(E, d)$ avec $d : E^2 \to \mathbb{R}_+$ vérifiant : $d(x, y) = 0 \iff x = y$, $d(x, y) = d(y, x)$, et $d(x, z) \leq d(x, y) + d(y, z)$. Tout espace vectoriel normé muni de sa distance est un espace métrique, mais il existe des espaces métriques qui ne sont pas des espaces vectoriels normés.

## 9. Propriétés de la distance associée à une norme
Donner les propriétés de la distance associée à une norme.
?
**Réponse:**
$$
\forall (x, y, z) \in E^3, \quad d(x + z, y + z) = d(x, y) \quad \text{(invariance par translation, propre aux e.v.n.)}
$$
$$
\forall (x, y, z) \in E^3, \quad |d(x, y) - d(y, z)| \leq d(x, z)
$$

## 10. Boules, sphère et boule unité
Définir la boule ouverte, la boule fermée, la sphère et la boule unité.
?
**Réponse:**
$$
B_o(a, r) = \{ x \in E \mid d(a, x) < r \}, \qquad
B_f(a, r) = \{ x \in E \mid d(a, x) \leq r \}, \qquad
S(a, r) = \{ x \in E \mid d(a, x) = r \}
$$
avec $(a, r) \in E \times \mathbb{R}_+^*$. La boule unité de $E$ est la boule fermée $B_f(0, 1)$.

## 11. Boules unités de $\mathbb{R}^2$ et convexité des boules
Décrire les boules unités de $\mathbb{R}^2$ pour les trois normes usuelles, et montrer que les boules sont convexes.
?
**Réponse:**
Pour $\|\cdot\|_2$ : disque de centre $O$ et de rayon $1$. Pour $\|\cdot\|_1$ : losange de sommets $(\pm 1, 0)$ et $(0, \pm 1)$. Pour $\|\cdot\|_{\infty}$ : carré $[-1, 1]^2$. Les boules d'un espace vectoriel normé sont convexes : si $x, y \in B_o(a, r)$ et $t \in [0, 1]$,
$$
\|tx + (1 - t)y - a\| \leq t\|x - a\| + (1 - t)\|y - a\| < tr + (1 - t)r = r
$$
Cette convexité ne se généralise pas aux espaces métriques.

## 12. Distance à une partie, distance entre parties et diamètre
Définir $d(a, A)$, $d(A, B)$ et le diamètre $\delta(A)$ d'une partie.
?
**Réponse:**
$$
d(a, A) = \inf_{x \in A} d(a, x), \qquad
d(A, B) = \inf_{(x, y) \in A \times B} d(x, y), \qquad
\delta(A) = \sup_{(x, y) \in A^2} d(x, y) \in \mathbb{R}_+ \cup \{+\infty\}
$$
Exemple : dans $\mathbb{R}$, $d(a, \mathbb{Q}) = 0$ pour tout $a$. De plus $\delta(B_f(a, r)) \leq 2r$, avec égalité si $E$ est non nul (prendre $e$ unitaire : $d(a + re, a - re) = 2r$), et $\delta$ est croissante pour l'inclusion.

## 13. Parties bornées d'un espace vectoriel normé
Caractériser les parties bornées d'un espace vectoriel normé.
?
**Réponse:**
Une partie $A$ de $E$ est bornée ssi l'une des propriétés équivalentes suivantes est vérifiée :
$$
\text{(i) } \{\|x\| \mid x \in A\} \text{ est borné}, \qquad
\text{(ii) } \forall x_0 \in E,\ \{\|x - x_0\| \mid x \in A\} \text{ est borné}
$$
$$
\text{(iii) } \forall x_0 \in E,\ \exists R \in \mathbb{R}_+, \ A \subset B_f(x_0, R), \qquad
\text{(iv) } \exists (x_0, R) \in E \times \mathbb{R}_+, \ A \subset B_f(x_0, R)
$$
Les boules sont bornées ; les droites affines ne le sont pas.

## 14. Applications bornées : $(B(A, E), \|\cdot\|_{\infty})$ et $l^{\infty}(E)$
Donner la norme uniforme sur les applications bornées et sur les suites bornées.
?
**Réponse:**
$(B(A, E), \|\cdot\|_{\infty})$ où $\|f\|_{\infty} = \sup_{a \in A} \|f(a)\|$ est un espace vectoriel normé. De même, l'ensemble $l^{\infty}(E)$ des suites bornées de $E$, muni de $\|(x_n)\|_{\infty} = \sup_{n \in \mathbb{N}} \|x_n\|$, est un espace vectoriel normé.

## 15. Applications k-lipschitziennes
Définir une application k-lipschitzienne et une application k-contractante.
?
**Réponse:**
$f : E \to F$ est $k$-lipschitzienne (avec $k \in \mathbb{R}_+$) ssi :
$$
\forall (x, y) \in D_f^2, \quad d(f(x), f(y)) \leq k \, d(x, y)
$$
Lorsque $k < 1$, $f$ est dite $k$-contractante. La composée d'une application $k$-lipschitzienne et d'une application $k'$-lipschitzienne est $kk'$-lipschitzienne.

## 16. Exemples d'applications 1-lipschitziennes
Citer des applications 1-lipschitziennes classiques. L'évaluation en 0 est-elle lipschitzienne pour la norme de la convergence en moyenne ?
?
**Réponse:**
La norme $x \mapsto \|x\|$ est 1-lipschitzienne, $x \mapsto d(x, A)$ (pour $A$ non vide) est 1-lipschitzienne, et les projections d'un produit muni d'une norme classique sont 1-lipschitziennes. Sur $\mathcal{C}([0, 1], \mathbb{R})$ muni de $\|\cdot\|_1$, l'application $f \mapsto f(0)$ n'est pas lipschitzienne.

## 17. Normes équivalentes
Définir deux normes équivalentes sur un même espace vectoriel.
?
**Réponse:**
$\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes ssi :
$$
\exists (\alpha, \beta) \in (\mathbb{R}_+^*)^2, \quad \forall x \in E, \quad \|x\|_1 \leq \alpha \|x\|_2 \ \text{ et } \ \|x\|_2 \leq \beta \|x\|_1
$$
Cela équivaut à : $\mathrm{Id}_E : (E, \|\cdot\|_1) \to (E, \|\cdot\|_2)$ et $\mathrm{Id}_E : (E, \|\cdot\|_2) \to (E, \|\cdot\|_1)$ sont lipschitziennes.

## 18. Équivalence des normes classiques sur un produit
Montrer que les trois normes classiques d'un produit sont deux à deux équivalentes, et rappeler les conséquences de l'équivalence des normes.
?
**Réponse:**
Pour $x = (x_1, \ldots, x_p)$ :
$$
\|x\|_{\infty} \leq \|x\|_2 \leq \|x\|_1 \leq p \|x\|_{\infty}
$$
La relation « être équivalente à » est une relation d'équivalence. Deux normes équivalentes donnent les mêmes parties bornées et les mêmes applications lipschitziennes. En dimension finie, toutes les normes sont équivalentes : on peut donc souvent ne pas préciser la norme utilisée.

## 19. Suites d'un espace vectoriel normé
Qu'est-ce qu'une suite d'éléments de $E$, et que sont son support et $E^{\mathbb{N}}$ ?
?
**Réponse:**
Une suite d'éléments de $E$ est une application $\mathbb{N} \to E$, $n \mapsto x_n$, notée $(x_n)_{n \in \mathbb{N}}$ ou simplement $(x_n)$ ; $n$ est une variable muette. $E^{\mathbb{N}}$ est l'ensemble des suites d'éléments de $E$. Le support de $(x_n)$ est l'ensemble $\{x_n \mid n \in \mathbb{N}\}$ des valeurs prises par la suite.

## 20. Convergence d'une suite de vecteurs
Définir la convergence d'une suite $(x_n)$ vers $l \in E$.
?
**Réponse:**
$(x_n)$ converge vers $l$ ssi :
$$
\forall \varepsilon \in \mathbb{R}_+^*, \ \exists N \in \mathbb{N}, \ \forall n \in \mathbb{N}, \quad n \geq N \Rightarrow d(x_n, l) \leq \varepsilon
$$
c'est-à-dire $d(x_n, l) \to 0$. Les inégalités peuvent être prises strictes ou larges, avec $n \geq N$ ou $n > N$, indifféremment. Une suite est convergente si elle converge vers un $l \in E$ ; sinon elle est divergente.

## 21. Unicité de la limite
Montrer qu'une suite convergeant vers $l$ et vers $l'$ vérifie $l = l'$.
?
**Réponse:**
Pour tout $\varepsilon > 0$, il existe $p$ tel que $d(x_p, l) \leq \varepsilon$ et $d(x_p, l') \leq \varepsilon$. Alors $d(l, l') \leq d(l, x_p) + d(x_p, l') \leq 2\varepsilon$ pour tout $\varepsilon > 0$, donc $d(l, l') = 0$ et $l = l'$. On note $l = \lim_{n \to +\infty} x_n$ ou $x_n \to l$.

## 22. Norme et convergence
Quels liens entre la convergence de $(x_n)$ et celle de $(\|x_n\|)$ ?
?
**Réponse:**
Si $x_n \to l$, alors $\|x_n\| \to \|l\|$ (par $|\|x_n\| - \|l\|| \leq \|x_n - l\|$), mais la réciproque est fausse. En revanche $x_n \to 0 \iff \|x_n\| \to 0$, et $x_n \to l \iff d(x_n, l) \to 0$.

## 23. Principe des gendarmes dans un espace vectoriel normé
Énoncer le principe des gendarmes pour une suite de vecteurs.
?
**Réponse:**
S'il existe une suite de réels $(g_n)$ telle que :
$$
\forall n \in \mathbb{N}, \quad d(x_n, l) \leq g_n \quad \text{et} \quad g_n \to 0
$$
alors $x_n \to l$.

## 24. Convergence et normes équivalentes
Que dire de la convergence d'une suite lorsqu'on remplace la norme par une norme équivalente ?
?
**Réponse:**
Si $N$ et $\|\cdot\|$ sont équivalentes ($N \leq \alpha \|\cdot\|$ et $\|\cdot\| \leq \beta N$), alors pour toute suite $(x_n)$ et tout $l \in E$ :
$$
x_n \to l \text{ pour } \|\cdot\| \iff x_n \to l \text{ pour } N
$$
La convergence est donc indépendante du choix d'une norme équivalente.

## 25. Toute suite convergente est bornée
Montrer que toute suite convergente d'un espace vectoriel normé est bornée.
?
**Réponse:**
Si $x_n \to l$, il existe $N$ tel que $d(x_n, l) \leq 1$ pour tout $n \geq N$. En posant $R = \max\left(1, \max_{0 \leq k \leq N-1} d(x_k, l)\right)$, on obtient $\{x_n \mid n \in \mathbb{N}\} \subset B_f(l, R)$, donc la suite est bornée.

## 26. Somme et produit de limites
Énoncer les propriétés de somme et de produit (par un scalaire) de limites.
?
**Réponse:**
Si $x_n \to l$ et $y_n \to l'$, alors $x_n + y_n \to l + l'$. Si $(x_n + y_n)$ converge, alors $(x_n)$ et $(y_n)$ sont toutes deux convergentes ou toutes deux divergentes (même nature). Si $\alpha_n \to \alpha$ et $l_n \to l$, alors $\alpha_n l_n \to \alpha l$, via la décomposition $\alpha_n l_n - \alpha l = (\alpha_n - \alpha) l_n + \alpha (l_n - l)$ et le fait que $(l_n)$ est bornée. Si $(\alpha_n)$ est bornée et $x_n \to 0$, alors $\alpha_n x_n \to 0$ (principe des gendarmes). Attention : le produit de deux suites de fonctions tendant vers 0 peut ne pas tendre vers 0 (exemple dans $\mathcal{C}^0([0,1],\mathbb{R})$ muni de $\|\cdot\|_1$).

## 27. L'ensemble des suites convergentes
Quelle structure possède l'ensemble des suites convergentes de $E$ ?
?
**Réponse:**
L'ensemble $E_{cv}^{\mathbb{N}}$ des suites convergentes de $E$ est un sous-espace vectoriel de $l^{\infty}(E)$, et l'application « limite »
$$
(x_n) \mapsto \lim_{n \to +\infty} x_n
$$
est une application linéaire.

## 28. Suites dans un produit d'espaces
Caractériser la convergence d'une suite dans $E_1 \times \cdots \times E_p$ muni d'une norme classique.
?
**Réponse:**
La suite $(x_n) = ((x_{1,n}, \ldots, x_{p,n}))$ converge vers $l = (l_1, \ldots, l_p)$ ssi, pour tout $i \in \{1, \ldots, p\}$, la suite coordonnée $(x_{i,n})$ converge vers $l_i$. (On travaille avec $\|\cdot\|_1$ : $\sum_{i=1}^{p} N_i(x_{i,n} - l_i) \to 0$.)

## 29. Suites de complexes : inverse, partie réelle et imaginaire
Donner les critères de convergence pour les suites de complexes.
?
**Réponse:**
Si $x_n \to l \in \mathbb{C} \setminus \{0\}$, alors $\frac{1}{x_n} \to \frac{1}{l}$. Une suite $(z_n)$ converge vers $l$ ssi $\mathrm{Re}(z_n) \to \mathrm{Re}(l)$ et $\mathrm{Im}(z_n) \to \mathrm{Im}(l)$ ; dans ce cas $\lim z_n = \lim \mathrm{Re}(z_n) + i \lim \mathrm{Im}(z_n)$.

## 30. Suites arithmético-géométriques
Résoudre la suite définie par $u_{n+1} = a u_n + b$ avec $a, b \in \mathbb{C}$.
?
**Réponse:**
Si $a \neq 1$, il existe un unique $c \in \mathbb{C}$ tel que $c = ac + b$, et :
$$
u_{n+1} - c = a (u_n - c), \quad \text{donc} \quad u_n - c = a^n (u_0 - c)
$$
Si $a = 1$, la suite $(u_n)$ est arithmétique de raison $b$.

## 31. Récurrence linéaire d'ordre 2
Résoudre $u_{n+2} = a u_{n+1} + b u_n$ avec $(a, b) \in \mathbb{K}^2 \setminus \{(0, 0)\}$.
?
**Réponse:**
Polynôme caractéristique : $\chi(X) = X^2 - aX - b$, de discriminant $\Delta = a^2 + 4b$.
$$
\Delta \neq 0 : \quad \exists (C_1, C_2) \in \mathbb{C}^2, \ \forall n \in \mathbb{N}, \quad u_n = C_1 \lambda_1^n + C_2 \lambda_2^n
$$
$$
\Delta = 0 : \quad \exists (C_1, C_2) \in \mathbb{K}^2, \ \forall n \in \mathbb{N}, \quad u_n = \lambda^n (C_1 + n C_2)
$$
Si $\mathbb{K} = \mathbb{R}$ et $\Delta < 0$, avec $\lambda_1 = \rho e^{i\theta}$ : $u_n = \rho^n (D_1 \cos(n\theta) + D_2 \sin(n\theta))$, $(D_1, D_2) \in \mathbb{R}^2$. Exemple : Fibonacci $F_{n+2} = F_{n+1} + F_n$ avec $\lambda = \frac{1 + \sqrt{5}}{2}$.

## 32. Suites homographiques
Quelle est la méthode générale pour étudier une suite homographique ?
?
**Réponse:**
On cherche les points fixes de $x \mapsto \frac{ax + b}{cx + d}$. S'il y a deux points fixes $\phi$ et $\widetilde{\phi}$, le quotient
$$
v_n = \frac{u_n - \phi}{u_n - \widetilde{\phi}}
$$
est une suite géométrique, ce qui permet d'exprimer $u_n$ explicitement et d'étudier sa limite.

## 33. Limites infinies et composition des limites
Définir $x_n \to +\infty$ et $x_n \to -\infty$, les catégories de suites réelles, et énoncer la composition des limites.
?
**Réponse:**
$$
x_n \to +\infty \iff \forall M \geq 0, \ \exists N \in \mathbb{N}, \ \forall n \geq N, \ x_n \geq M
$$
($x_n \to -\infty$ : on impose $x_n \leq -M$). Trois catégories de suites réelles : les suites convergentes, les suites divergentes de première espèce (vers $\pm\infty$), et les autres, dites divergentes de seconde espèce. Si $\phi : \mathbb{N} \to \mathbb{N}$ est strictement croissante, alors $\phi(n) \geq n$, donc $\phi(n) \to +\infty$. Composition : si $x_n \to l \in E \cup \{\infty\}$ et $\phi(n) \to +\infty$, alors $x_{\phi(n)} \to l$.

## 34. Règles de calcul des limites infinies
Donner les règles de calcul des limites infinies et les formes indéterminées.
?
**Réponse:**
$\varepsilon \infty + y \to \varepsilon \infty$ ($y \in \mathbb{R}$) ; $\varepsilon \infty + \varepsilon \infty \to \varepsilon \infty$ ; $-x_n \to -\varepsilon \infty$ ; $\alpha x_n$ ($\alpha > 0$) conserve le signe ; $\varepsilon \infty \times y$ ($y \in \mathbb{R}_+^*$) $\to \varepsilon \infty$ ; $\varepsilon \infty \times \varepsilon' \infty \to \varepsilon \varepsilon' \infty$ ; si $x_n \to \varepsilon \infty$, alors $\frac{1}{x_n} \to 0$ ; si $x_n \to 0^+$, alors $\frac{1}{x_n} \to +\infty$. Formes indéterminées : $\infty - \infty$, $0 \times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$.

## 35. Étude de $u_n = a_n^{b_n}$
Comment étudier la limite d'une suite de la forme $u_n = a_n^{b_n}$ ?
?
**Réponse:**
Écrire systématiquement $u_n = e^{b_n \ln a_n}$, car les formes $\infty^0$, $0^0$ et $1^{\infty}$ sont indéterminées. Exemple : $\left(1 + \frac{1}{n}\right)^n = e^{n \ln(1 + 1/n)} \to e$, car $\frac{\ln(1 + x)}{x} \to 1$ en $x = 0$.

## 36. Gendarmes réels et lemme du tunnel
Énoncer le principe des gendarmes pour les suites réelles et le lemme du tunnel.
?
**Réponse:**
Si $g_n \leq p_n \leq g'_n$ pour tout $n$ et $g_n \to l$, $g'_n \to l$, alors $p_n \to l$. Adaptation aux limites infinies : si $x_n \geq y_n$ pour tout $n$ et $y_n \to +\infty$, alors $x_n \to +\infty$ (idem en $-\infty$). Lemme du tunnel : si $u_n \to l$ et $a < l < b$, alors à partir d'un certain rang $a < u_n < b$ (faux avec des inégalités larges).

## 37. Passage à la limite dans les inégalités
Soient $(a_n)$ et $(b_n)$ deux suites convergentes de réels avec $a_n \leq b_n$ pour tout $n$. Que dire des limites ?
?
**Réponse:**
$\lim a_n \leq \lim b_n$ (propriété encore vraie avec des limites $\pm\infty$). En revanche, des inégalités strictes $a_n < b_n$ ne sont pas conservées à la limite : par exemple $\frac{1}{n} > 0$ pour tout $n \geq 1$ mais $\frac{1}{n} \to 0$.

## 38. Théorème de la limite monotone
Énoncer le théorème de la limite monotone et la règle de comportement des suites géométriques réelles.
?
**Réponse:**
Toute suite croissante converge vers $\sup x_n$ si elle est majorée, et diverge vers $+\infty$ sinon ; toute suite décroissante converge vers $\inf x_n$ si elle est minorée, et diverge vers $-\infty$ sinon. Suite géométrique $x_n = a^n x_0$ avec $x_0 \neq 0$ et $\varepsilon$ le signe de $x_0$ : $|a| < 1 \Rightarrow x_n \to 0$ ; $a = 1 \Rightarrow$ suite constante ; $a > 1 \Rightarrow x_n \to \varepsilon \infty$ ; $a \leq -1 \Rightarrow$ suite divergente.

## 39. Suites adjacentes
Définir deux suites adjacentes et énoncer leur théorème.
?
**Réponse:**
$(x_n)$ et $(y_n)$ sont adjacentes ssi l'une est croissante, l'autre décroissante et $x_n - y_n \to 0$. Alors elles convergent vers une limite commune $l \in \mathbb{R}$, et :
$$
\forall (p, q) \in \mathbb{N}^2, \quad x_p \leq l \leq y_q
$$
avec $l = \sup_{n \in \mathbb{N}} x_n = \inf_{n \in \mathbb{N}} y_n$.

## 40. Théorème des segments emboîtés
Énoncer le théorème des segments emboîtés.
?
**Réponse:**
Soit $(I_n)$ une suite de segments $I_n = [a_n, b_n]$, décroissante au sens de l'inclusion, dont les longueurs tendent vers 0. Alors $\bigcap_{n \in \mathbb{N}} I_n$ est un singleton $\{l\}$, où $l = \lim a_n = \lim b_n$ (les suites $(a_n)$ et $(b_n)$ sont adjacentes).

## 41. Suites extraites et valeurs d'adhérence
Définir une suite extraite et une valeur d'adhérence. Que vaut l'ensemble des valeurs d'adhérence d'une suite périodique ?
?
**Réponse:**
Une suite extraite de $(x_n)$ est une suite $(x_{\phi(n)})$ avec $\phi : \mathbb{N} \to \mathbb{N}$ strictement croissante (on dit que $\phi$ est une extraction). Toute suite extraite d'une suite convergente converge vers la même limite. Une valeur d'adhérence est une limite d'une suite extraite ; la limite d'une suite convergente est son unique valeur d'adhérence, et une suite admettant deux valeurs d'adhérence distinctes est divergente. Une suite périodique de période $p$ admet pour valeurs d'adhérence exactement $x_0, \ldots, x_{p-1}$ (et l'ajout du terme $\frac{1}{n+1}$ ne change pas cet ensemble).

## 42. Caractérisation des valeurs d'adhérence (hors programme)
Caractériser « $a$ est une valeur d'adhérence de $(x_n)$ ».
?
**Réponse:**
Les trois propriétés suivantes sont équivalentes :
$$
\text{(i) } a \text{ est la limite d'une suite extraite de } (x_n)
$$
$$
\text{(ii) } \forall \varepsilon \in \mathbb{R}_+^*, \ \forall N \in \mathbb{N}, \ \exists n \geq N, \quad d(x_n, a) < \varepsilon
$$
$$
\text{(iii) } \forall \varepsilon > 0, \quad \mathrm{Card}\left( \{ n \in \mathbb{N} \mid x_n \in B_o(a, \varepsilon) \} \right) = +\infty
$$

## 43. Théorème de Bolzano-Weierstrass
Énoncer le théorème de Bolzano-Weierstrass (cas réel et cas complexe), et définir limsup et liminf.
?
**Réponse:**
Toute suite bornée de réels possède au moins une valeur d'adhérence ; il en va de même pour toute suite bornée de complexes (via les parties réelles et imaginaires et deux extractions successives).
$$
\overline{\lim} \, x_n = \lim_{n \to +\infty} \left( \sup_{k \geq n} x_k \right), \qquad
\underline{\lim} \, x_n = \lim_{n \to +\infty} \left( \inf_{k \geq n} x_k \right)
$$
La limsup est la plus grande valeur d'adhérence et la liminf la plus petite.

## 44. Suites de Cauchy
Définir une suite de Cauchy et donner ses propriétés.
?
**Réponse:**
$$
\forall \varepsilon \in \mathbb{R}_+^*, \ \exists N \in \mathbb{N}, \ \forall p \geq N, \ \forall q \geq N, \quad d(x_p, x_q) \leq \varepsilon
$$
Toute suite convergente est de Cauchy ; toute suite de Cauchy est bornée ; une suite de Cauchy admettant une valeur d'adhérence converge.

## 45. Espaces complets
Définir un espace métrique complet, et donner les résultats de complétude pour $\mathbb{R}$, $\mathbb{C}$ et $\mathbb{Q}$.
?
**Réponse:**
Un espace métrique $E$ est complet ssi toute suite de Cauchy de $E$ converge. Si toute suite bornée de $E$ possède au moins une valeur d'adhérence, alors $E$ est complet. $\mathbb{R}$ et $\mathbb{C}$ sont complets (conséquence du théorème de Bolzano-Weierstrass). $\mathbb{Q}$ n'est pas complet : une suite de rationnels convergeant vers un irrationnel est de Cauchy dans $\mathbb{Q}$ sans y converger, et $\mathbb{R}$ est une complétion de $\mathbb{Q}$.
