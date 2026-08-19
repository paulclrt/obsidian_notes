#flashcards/maths/prépa/ev/td

## 1. Exercice 15.1 — Sous-espaces vectoriels définis par une équation
On note $A = \{(x,y) \in \mathbb{R}^2 / xy = 0\}$ et $B = \{(x,y) \in \mathbb{R}^2 / 2x + y = 1\}$. Les ensembles A et B sont-ils des sous-espaces vectoriels de $\mathbb{R}^2$ ?
?
**Réponse:**
Non pour $A$ : $A = (Ox) \cup (Oy)$. Avec $a = (0,1) \in A$ et $b = (1,0) \in A$, on a $a + b = (1,1) \notin A$ car $1 \cdot 1 = 1 \neq 0$, donc $A$ n'est pas stable par somme.
Non pour $B$ : $0_{\mathbb{R}^2} \notin B$ (car $2 \cdot 0 + 0 \neq 1$) ; de plus avec $b = (\frac{1}{2}, 0)$, $a + b = (\frac{1}{2}, 1) \notin B$ puisque $2 \cdot \frac{1}{2} + 1 = 2 \neq 1$. $B$ est une droite affine du plan, donc pas un sous-espace vectoriel.

## 2. Exercice 15.2 — Suites arithmétiques et suites monotones
On note $A$ l'ensemble des suites arithmétiques et $B$ l'ensemble des suites monotones de $\mathbb{R}^{\mathbb{N}}$. A et B sont-ils des sous-espaces vectoriels de $\mathbb{R}^{\mathbb{N}}$ ?
?
**Réponse:**
$A$ en est un : si $u_n = u_0 + nr$ et $v_n = v_0 + nq$, alors pour $\alpha \in \mathbb{R}$,
$$
\alpha u_n + v_n = n(\alpha r + q) + (\alpha u_0 + v_0),
$$
donc $\alpha(u_n) + (v_n)$ est encore arithmétique.
$B$ n'en est pas un : la somme d'une suite croissante et d'une suite décroissante n'est pas nécessairement monotone, donc $B$ n'est pas stable par somme.

## 3. Exercice 15.3 — Comparaison de Vect(A∩B) et Vect(A)∩Vect(B)
Si A et B sont deux parties d'un K-espace vectoriel E, comparer $\operatorname{Vect}(A \cap B)$ et $\operatorname{Vect}(A) \cap \operatorname{Vect}(B)$.
?
**Réponse:**
Comme $A \cap B \subset A$ et $A \cap B \subset B$,
$$
\operatorname{Vect}(A \cap B) \subset \operatorname{Vect}(A) \cap \operatorname{Vect}(B).
$$
L'inclusion est stricte en général : dans $\mathbb{R}$ (R-espace vectoriel), pour $a \neq b$, $\operatorname{Vect}(\{a\} \cap \{b\}) = \operatorname{Vect}(\emptyset) = \{0\}$ alors que $\operatorname{Vect}(a) \cap \operatorname{Vect}(b) = \mathbb{R}$.

## 4. Exercice 15.4 — Calcul de Vect(u,v) dans R^3
Dans $\mathbb{R}^3$, on note $u = (1,1,1)$ et $v = (1,0,-1)$. Déterminer $\operatorname{Vect}(u,v)$.
?
**Réponse:**
Par définition, $\operatorname{Vect}(u,v) = \{\alpha u + \beta v / (\alpha, \beta) \in \mathbb{R}^2\}$ avec
$$
\alpha(1,1,1) + \beta(1,0,-1) = (\alpha + \beta, \ \alpha, \ \alpha - \beta),
$$
donc
$$
\operatorname{Vect}(u,v) = \{(\alpha + \beta, \ \alpha, \ \alpha - \beta) / (\alpha, \beta) \in \mathbb{R}^2\}.
$$

## 5. Exercice 15.5 — Application linéaire nulle sur le complémentaire d'un sous-espace
Soient E un R-espace vectoriel, F un sous-espace vectoriel de E différent de E, et u : E → E nulle sur le complémentaire de F. Montrer que u est linéaire si et seulement si elle est nulle.
?
**Réponse:**
Si $u$ est linéaire : soit $x \in F$ et $a \in E \setminus F$. Alors $a + x \notin F$ (sinon $a \in F$), donc $u(a+x) = 0$ et $u(a) = 0$, d'où
$$
u(x) = u(a + x - a) = u(a+x) - u(a) = 0.
$$
Ainsi $u|_F$ est nulle, et comme $u$ est nulle sur $E \setminus F$, $u = 0$.
Réciproquement, l'application nulle est bien linéaire.

## 6. Exercice 15.6 — Fonctions dominées par une fonction linéaire
On note $E$ l'ensemble des fonctions $f : \mathbb{R} \to \mathbb{R}$ telles qu'il existe $(a, A) \in (\mathbb{R}_+)^2$ vérifiant $\forall x \in \mathbb{R}$, $|x| \ge a$ implique $|f(x)| \le A|x|$.
?
**Réponse:**
Cet exercice n'a pas de correction dans la feuille corrigée (« Pas de correction »). Il s'agit de l'ensemble des fonctions au plus linéaires au voisinage de l'infini (croissance dominée par $x \mapsto A|x|$ hors d'un compact).

## 7. Exercice 15.7 — Trois sous-espaces avec intersections et sommes égales
Soient E un K-espace vectoriel et A, B, C trois sous-espaces vectoriels de E tels que $A \cap B = A \cap C$, $A + B = A + C$ et $B \subset C$. Montrer que $B = C$.
?
**Réponse:**
Soit $x \in C$. Comme $0 \in A$, $x \in A + C = A + B$, donc il existe $(a,b) \in A \times B$ tel que $x = a + b$, d'où $a = x - b$. Comme $x \in C$ et $b \in B \subset C$, on a $a = x - b \in C$, donc $a \in A \cap C = A \cap B$, puis $a \in B$ et $x = a + b \in B$. Ainsi $C \subset B$ ; avec $B \subset C$, on conclut $B = C$.

## 8. Exercice 15.8 — Linéarité, noyau et image de M
Pour tout $X = (x,y,z) \in \mathbb{R}^3$, on note $M(X) = (x+2y+4z,\ 3y+3z,\ x+y+3z)$. Montrer que $M \in L(\mathbb{R}^3)$, puis calculer $\operatorname{Ker}(M)$ et $\operatorname{Im}(M)$.
?
**Réponse:**
On vérifie composante par composante que $M(\lambda X + X') = \lambda M(X) + M(X')$ : $M$ est linéaire.
Noyau : $M(X) = 0$ équivaut à $x+2y+4z = 0$, $3y+3z = 0$, $x+y+3z = 0$, soit $y = -z$ et $x = -2z$, d'où
$$
\operatorname{Ker}(M) = \operatorname{Vect}((-2, -1, 1)) = \{(-2z, -z, z) / z \in \mathbb{R}\}.
$$
Image : les colonnes $(1,3,1)$, $(2,3,1)$, $(4,3,3)$ engendrent
$$
\operatorname{Im}(M) = \operatorname{Vect}((1,0,1), (1,3,0)) = \{(x,y,z) / 3x - y - 3z = 0\}
$$
(en effet $y = 3\beta$, $z = \alpha$, $x = \alpha + \beta$, donc $3x - y - 3z = 0$).

## 9. Exercice 15.9 — Distributivité entre intersection et somme
Soient E, F, G trois sous-espaces vectoriels d'un espace A. 1) $E \cap (F+G) = (E \cap F) + (E \cap G)$ ? 2) $E \cap (F + (E \cap G)) = (E \cap F) + (E \cap G)$ ?
?
**Réponse:**
1) Faux en général : si $E$ est un plan et $F$, $G$ deux droites distinctes de $E$, alors $F + G = E$ donc $E \cap (F+G) = E$, tandis que $(E \cap F) + (E \cap G) = \{0\} + \{0\} = \{0\}$.
2) Vrai. Si $x \in (E \cap F) + (E \cap G)$, alors $x = a + b$ avec $a \in E \cap F$ et $b \in E \cap G$ : $x \in E$ et $x \in F + (E \cap G)$. Réciproquement, si $x \in E \cap (F + (E \cap G))$, $x = a + b$ avec $a \in F$, $b \in E \cap G$ ; alors $a = x - b \in E$ donc $a \in E \cap F$, et $x \in (E \cap F) + (E \cap G)$.

## 10. Exercice 15.10 — h^(-1)(h(F)) et h(h^(-1)(F))
Soient E un K-espace vectoriel et h un endomorphisme de E. 1) Montrer que $h^{-1}(h(F)) = F + \operatorname{Ker}(h)$. 2) Exprimer $h(h^{-1}(F))$. 3) Déterminer les F tels que $h^{-1}(h(F)) = h(h^{-1}(F))$.
?
**Réponse:**
1) Si $x = a + b$ avec $a \in F$, $b \in \operatorname{Ker}(h)$, alors $h(x) = h(a) \in h(F)$, donc $x \in h^{-1}(h(F))$. Réciproquement, si $h(x) \in h(F)$, il existe $y \in F$ avec $h(x) = h(y)$, donc $h(x-y) = 0$, soit $x = y + (x-y) \in F + \operatorname{Ker}(h)$.
2) $h(h^{-1}(F)) = F \cap \operatorname{Im}(h)$ : si $x = h(y) \in F$ avec $y \in h^{-1}(F)$, $x \in \operatorname{Im}(h)$ ; réciproquement, si $x \in F \cap \operatorname{Im}(h)$, $x = h(y)$ avec $y \in h^{-1}(F)$.
3) D'après 1) et 2), l'égalité équivaut à $F + \operatorname{Ker}(h) = F \cap \operatorname{Im}(h)$, c'est-à-dire
$$
\operatorname{Ker}(h) \subset F \quad \text{et} \quad F \subset \operatorname{Im}(h).
$$

## 11. Exercice 15.11 — Inversibilité de u + β·Id lorsque uv + αu + βv = 0
Soient u et v deux endomorphismes d'un C-espace vectoriel E, avec $u \circ v = v \circ u$. On suppose qu'il existe $(\alpha, \beta) \in \mathbb{C}^2$ tels que $u \circ v + \alpha u + \beta v = 0$, avec $\alpha \neq 0$ et $\beta \neq 0$. Montrer que $u + \beta \,\mathrm{Id}_E$ est inversible.
?
**Réponse:**
Analyse : si $w = (u + \beta \mathrm{Id}_E)^{-1}$, alors $w(u + \beta \mathrm{Id}_E) = \mathrm{Id}_E$ donne
$$
\alpha \beta w = \alpha \mathrm{Id}_E + v, \quad \text{donc} \quad w = \frac{1}{\beta} \mathrm{Id}_E + \frac{1}{\alpha \beta} v.
$$
Synthèse : posons $w = \frac{1}{\beta} \mathrm{Id}_E + \frac{1}{\alpha \beta} v$. Alors
$$
(u + \beta \mathrm{Id}_E)w = \frac{1}{\alpha\beta}(u + \beta \mathrm{Id}_E)(\alpha \mathrm{Id}_E + v) = \frac{1}{\alpha\beta}(\alpha u + uv + \beta v + \alpha \beta \mathrm{Id}_E)
$$
et comme $uv + \alpha u + \beta v = 0$, on obtient $(u + \beta \mathrm{Id}_E)w = \mathrm{Id}_E$. On vérifie de même à gauche ; donc $u + \beta \mathrm{Id}_E \in GL(E)$.

## 12. Exercice 15.12 — Vect(cos(nx)) et Vect(cos^n x)
Dans $F(\mathbb{R},\mathbb{R})$, comparer les sous-espaces engendrés par $(\phi_n)_{n \in \mathbb{N}}$ et $(\psi_n)_{n \in \mathbb{N}}$, où $\phi_n(x) = \cos(nx)$ et $\psi_n(x) = \cos^n(x)$.
?
**Réponse:**
On montre par récurrence que $\operatorname{Vect}(\cos(nx)) = \operatorname{Vect}(\cos^n x)$.
Initialisation en $n = 0$ et $n = 1$. Hérédité : $\operatorname{Vect}\{\cos kx / 1 \le k \le n+1\} = \operatorname{Vect}(\{\cos kx / 1 \le k \le n\} \cup \{\cos(n+1)x\})$ ; or $\cos(n+1)x = T_{n+1}(\cos x)$ où $T_{n+1}$ est le polynôme de Tchebychev de degré $n+1$, donc par opérations élémentaires (soustraire les combinaisons des premiers termes)
$$
\operatorname{Vect}\{\cos kx / 1 \le k \le n+1\} = \operatorname{Vect}\{\cos^k x / 1 \le k \le n+1\}.
$$
Enfin, $\operatorname{Vect}(\cos(nx))$ et $\operatorname{Vect}(\cos^n x)$ sont les réunions croissantes de ces espaces, donc ils coïncident.

## 13. Exercice 15.13 — Noyau, image et carré d'un endomorphisme
Soit E un K-espace vectoriel et u un élément de L(E). 1) $\operatorname{Ker}(u) \cap \operatorname{Im}(u) = \{0\} \iff \operatorname{Ker}(u^2) = \operatorname{Ker}(u)$ ? 2) $E = \operatorname{Ker}(u) + \operatorname{Im}(u) \iff \operatorname{Im}(u^2) = \operatorname{Im}(u)$ ?
?
**Réponse:**
1) $(\Leftarrow)$ Si $\operatorname{Ker}(u^2) = \operatorname{Ker}(u)$ et $x \in \operatorname{Ker}(u) \cap \operatorname{Im}(u)$, alors $x = u(y)$ et $0 = u(x) = u^2(y)$, donc $y \in \operatorname{Ker}(u^2) = \operatorname{Ker}(u)$ et $x = u(y) = 0$.
$(\Rightarrow)$ Si $\operatorname{Ker}(u) \cap \operatorname{Im}(u) = \{0\}$ : $\operatorname{Ker}(u) \subset \operatorname{Ker}(u^2)$ est immédiat ; si $x \in \operatorname{Ker}(u^2)$, alors $u(x) \in \operatorname{Ker}(u) \cap \operatorname{Im}(u)$, donc $u(x) = 0$ et $x \in \operatorname{Ker}(u)$.
2) $(\Rightarrow)$ Si $E = \operatorname{Ker}(u) + \operatorname{Im}(u)$ : $\operatorname{Im}(u^2) \subset \operatorname{Im}(u)$ ; si $x \in \operatorname{Im}(u)$, $x = u(y)$ avec $y = a + b$, $a \in \operatorname{Ker}(u)$, $b \in \operatorname{Im}(u)$, donc $x = u(b) \in \operatorname{Im}(u^2)$.
$(\Leftarrow)$ Si $\operatorname{Im}(u^2) = \operatorname{Im}(u)$ : pour $x \in E$, $u(x) \in \operatorname{Im}(u) = \operatorname{Im}(u^2)$, donc $u(x) = u^2(y)$ et $x - u(y) \in \operatorname{Ker}(u)$, d'où $x = u(y) + (x - u(y)) \in \operatorname{Ker}(u) + \operatorname{Im}(u)$.

## 14. Exercice 15.14 — Intersection de noyaux de puissances d'endomorphismes commutants
Soit E un K-espace vectoriel et $u, v \in L(E)$ tels que $u \circ v = v \circ u$ et $\operatorname{Ker}(u) \cap \operatorname{Ker}(v) = \{0\}$. Montrer que pour tous $i, j \in \mathbb{N}$, $\operatorname{Ker}(u^i) \cap \operatorname{Ker}(v^j) = \{0\}$.
?
**Réponse:**
Par récurrence sur $i$ avec $j = 1$ (initialisée au rang 1 par hypothèse). Supposons $\operatorname{Ker}(u^i) \cap \operatorname{Ker}(v) = \{0\}$ et soit $x \in \operatorname{Ker}(u^{i+1}) \cap \operatorname{Ker}(v)$ : $0 = u^{i+1}(x) = u(u^i(x))$, donc $u^i(x) \in \operatorname{Ker}(u)$. Comme $uv = vu$,
$$
v(u^i(x)) = u^i(v(x)) = u^i(0) = 0,
$$
donc $u^i(x) \in \operatorname{Ker}(v)$, puis $u^i(x) \in \operatorname{Ker}(u) \cap \operatorname{Ker}(v) = \{0\}$, d'où $x \in \operatorname{Ker}(u^i) \cap \operatorname{Ker}(v) = \{0\}$. Donc $\operatorname{Ker}(u^{i+1}) \cap \operatorname{Ker}(v) = \{0\}$. On applique ensuite ce résultat au couple $(v, u^j)$ pour obtenir le cas général.

## 15. Exercice 15.15 — Isomorphisme E^* × F^* ≃ (E × F)^*
Soient E et F deux K-espaces vectoriels. Montrer que $E^* \times F^*$ est isomorphe à $(E \times F)^*$.
?
**Réponse:**
On pose
$$
\Psi : E^* \times F^* \to (E \times F)^*, \quad (e, f) \mapsto \phi_{e,f}, \quad \phi_{e,f}(x, y) = e(x) + f(y).
$$
$\Psi$ est linéaire. Surjectivité : pour $\phi \in (E \times F)^*$, on définit $e(x) = \phi(x, 0)$ et $f(y) = \phi(0, y)$ ; alors par linéarité de $\phi$, $\phi_{e,f}(x,y) = \phi(x,0) + \phi(0,y) = \phi(x,y)$.
Injectivité : si $\Psi(e, f) = 0$, en prenant $x = 0$ on obtient $f(y) = 0$ pour tout $y$, puis en prenant $y = 0$, $e(x) = 0$ pour tout $x$, donc $(e, f) = (0, 0)$ et $\operatorname{Ker} \Psi = \{(0,0)\}$. $\Psi$ est donc un isomorphisme.

## 16. Exercice 15.16 — Polynômes d'endomorphismes, u-générateur
Soient E un K-espace vectoriel et $u \in L(E)$. On note $P = \{P(u) / P \in K[X]\}$ et $C = \{v \in L(E) / v \circ u = u \circ v\}$. 1) P et C sont des sous-espaces de L(E) et $P \subset C$. 2) Le plus petit sous-espace contenant x stable par u est $F_x = \{P(u)(x) / P \in K[X]\}$. 3) x est u-générateur ssi $\phi_x|_P$ est surjective. 4) Si x est u-générateur, $\phi_x|_C$ est injective et $P = C \cong E$.
?
**Réponse:**
1) $f : K[X] \to L(E)$, $P \mapsto P(u)$, est un morphisme d'algèbres, donc $P = \operatorname{Im}(f)$ est un sous-espace vectoriel de $L(E)$ ; $C$ en est aussi un. Si $P(u) \in P$,
$$
u \circ P(u) = \sum a_n u^{n+1} = P(u) \circ u,
$$
donc $P(u) \in C$ et $P \subset C$.
2) $F_x = \operatorname{Im}(\Psi)$ avec $\Psi : K[X] \to E$, $P \mapsto P(u)(x)$, est un sous-espace. Il est stable par $u$ car $u \circ P(u)(x) = (XP)(u)(x) \in F_x$. Si $G$ est un sous-espace stable par $u$ contenant $x$, par récurrence $u^k(x) \in G$ pour tout $k$, puis par combinaisons linéaires $F_x \subset G$.
3) $x$ est $u$-générateur ssi $F_x = E$ ssi $E \subset \phi_x(P)$ ssi $\phi_x|_P$ est surjective.
4) Si $v \in C$ et $\phi_x(v) = 0$, alors pour tout $P(u) \in P$,
$$
v(P(u)(x)) = P(u)(v(x)) = 0,
$$
donc $v$ est nulle sur $F_x = E$ : $\operatorname{Ker}(\phi_x|_C) = \{0\}$. Soit $v \in C$ : par surjectivité, $v(x) = f(x)$ pour un $f \in P$, donc $\phi_x(f) = \phi_x(v)$ et par injectivité $f = v$ ; ainsi $C = P$ et $\phi_x|_C$ est bijective : $C \cong E$.

## 17. Exercice 15.17 — Réunion de sous-espaces strictement inclus
Soient K un sous-corps de $\mathbb{C}$ et E un K-espace vectoriel. 1) La réunion de deux sous-espaces vectoriels strictement inclus dans E est strictement incluse dans E. 2) Plus généralement, la réunion de n sev strictement inclus est strictement incluse.
?
**Réponse:**
1) Si $E_1 \subset E_2$ ou $E_2 \subset E_1$, c'est clair. Sinon, il existe $x \in E_1 \setminus E_2$ et $y \in E_2 \setminus E_1$. Si $E_1 \cup E_2 = E$, alors $x + y \in E_1 \cup E_2$ ; si $x + y \in E_1$, alors $y = (x+y) - x \in E_1$, contradiction ; le cas $E_2$ est symétrique. Donc $E_1 \cup E_2 \neq E$.
2) Supposons $\bigcup_{j=1}^n E_j = E$ ; quitte à réordonner, $x \in E_1$ mais $x \notin E_i$ pour $i \ge 2$, et $y \in E_i$ pour un $i \ge 2$ avec $y \notin E_1$. La famille $\{x + ky / k \in \mathbb{Z}\}$ est infinie (caractéristique nulle), donc par le principe des tiroirs (où les tiroirs sont les $E_j$) il existe $k_1 \neq k_2$ avec $x + k_1 y, x + k_2 y \in E_\ell$ ; alors $(k_1 - k_2)y \in E_\ell$, donc $y \in E_\ell$, puis $x \in E_\ell$ ; ainsi $x, y \in E_\ell$ impose $\ell = 1$ d'après le choix de $x$, d'où $y \in E_1$, contradiction. La réunion reste donc strictement incluse dans $E$.