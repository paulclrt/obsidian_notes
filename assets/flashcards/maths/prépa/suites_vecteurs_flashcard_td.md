#flashcards/maths/prépa/suites_vecteurs/td

## 1. Exercice 16.1 — Convergence de deux suites majorées
Soient $(u_n)$ et $(v_n)$ deux suites de réels et $a, b \in \mathbb{R}$ tels que, pour tout $n \in \mathbb{N}$, $u_n \leq a$, $v_n \leq b$, et tels que $u_n + v_n \to a + b$. Montrer que $u_n \to a$ et $v_n \to b$.
?
**Réponse:**
Soit $\varepsilon > 0$ : il existe $N$ tel que pour $n \geq N$, $|u_n + v_n - (a + b)| \leq \varepsilon$, i.e. $|(u_n - a) + (v_n - b)| \leq \varepsilon$. Comme $u_n - a \leq 0$ et $v_n - b \leq 0$, on a $0 \leq (a - u_n) + (b - v_n) \leq \varepsilon$, donc $0 \leq a - u_n \leq \varepsilon$, i.e. $|u_n - a| \leq \varepsilon$. De même $|v_n - b| \leq \varepsilon$. Alternative : $0 \leq a - u_n \leq (a - u_n) + (b - v_n) \to 0$ par les gendarmes.

## 2. Exercice 16.2 — Récurrence linéaire d'ordre 2 avec $\Delta < 0$
On suppose que $u_0 = 0$, $u_1 = 1$ et, pour tout $n > 0$, $u_{n+2} = 2u_{n+1} - 3u_n$. Exprimer $u_n$ en fonction de $n$.
?
**Réponse:**
$\chi(X) = X^2 - 2X + 3$, $\Delta = 4 - 12 = -8 = (\pm 2\sqrt{2}\, i)^2$. Racines $1 \pm \sqrt{2}\, i$, de module $\sqrt{3}$ et d'argument $\theta = \arctan(\sqrt{2})$ (avec $\sin \theta = \frac{\sqrt{2}}{\sqrt{3}}$). Donc $u_n = (\sqrt{3})^n (A \cos(n\theta) + B \sin(n\theta))$. $u_0 = A = 0$ et $u_1 = \sqrt{3} B \sin \theta = 1$, d'où $B = \frac{1}{\sqrt{3} \sin \theta} = \frac{1}{\sqrt{2}}$. Finalement $u_n = \frac{(\sqrt{3})^n \sin(n\theta)}{\sqrt{2}}$.

## 3. Exercice 16.3 — Récurrence par passage au logarithme
On suppose que $u_0 = 2$, $u_1 = 4$ et, pour tout $n \geq 0$, $u_{n+2} = \frac{u_{n+1}^4}{u_n^3}$. Exprimer $u_n$ en fonction de $n$.
?
**Réponse:**
Par récurrence $u_n > 0$ pour tout $n$, donc on pose $z_n = \ln u_n$ : $z_{n+2} = 4z_{n+1} - 3z_n$. $\chi(X) = X^2 - 4X + 3$ a pour racines $1$ et $3$, donc $z_n = A + B \cdot 3^n$. Avec $z_0 = \ln 2$ et $z_1 = \ln 4 = 2 \ln 2$, on trouve $A = B = \frac{\ln 2}{2}$. D'où $u_n = \exp\!\left( \frac{\ln 2}{2} (1 + 3^n) \right) = (\sqrt{2})^{1 + 3^n}$.

## 4. Exercice 16.4 — Moyenne arithmético-géométrique
Soient $a, b \in \mathbb{R}$ avec $0 < a < b$, $u_0 = a$, $v_0 = b$, et $u_{n+1} = \sqrt{u_n v_n}$, $v_{n+1} = \frac{u_n + v_n}{2}$. 1) Montrer que $\forall n$, $u_n < v_n$. 2) Montrer que $(u_n)$ est croissante et $(v_n)$ décroissante. 3) En déduire qu'elles convergent vers une même limite.
?
**Réponse:**
1) Récurrence : $0 < u_n < v_n$, puis $0 < \sqrt{u_n} < \sqrt{v_n}$ et $0 < (\sqrt{v_n} - \sqrt{u_n})^2 = u_n + v_n - 2\sqrt{u_n v_n}$, donc $0 < \sqrt{u_n v_n} < \frac{u_n + v_n}{2}$, i.e. $u_{n+1} < v_{n+1}$.
2) $\frac{u_{n+1}}{u_n} = \sqrt{\frac{v_n}{u_n}} > 1$, donc $(u_n)$ croissante ; $v_{n+1} - v_n = \frac{u_n - v_n}{2} < 0$, donc $(v_n)$ décroissante.
3) $(u_n)$ croissante majorée (par $v_0$) et $(v_n)$ décroissante minorée (par $u_0$) convergent vers $l$ et $l'$. Passage à la limite : $l' = \frac{l + l'}{2}$, d'où $l = l'$. Cette limite commune est la moyenne arithmético-géométrique de $a$ et $b$.

## 5. Exercice 16.5 — Limite de $\max(u_n, v_n)$
Soient $(u_n)$ et $(v_n)$ deux suites convergentes de réels. Calculer $\lim_{n \to +\infty} \max(u_n, v_n)$.
?
**Réponse:**
La limite est $\max(l, l')$ où $l = \lim u_n$ et $l' = \lim v_n$. Si $l < l'$ : pour $n$ assez grand $u_n \leq \frac{l + l'}{2} \leq v_n$, donc $\max(u_n, v_n) = v_n \to l'$. Si $l = l'$ : pour $n$ assez grand $u_n, v_n \in B_f(l, \varepsilon)$, donc $\max(u_n, v_n) \in B_f(l, \varepsilon)$. Autre méthode : $\max(a, b) = \frac{a + b + |a - b|}{2}$ donne $\max(u_n, v_n) = \frac{u_n + v_n + |u_n - v_n|}{2} \to \frac{l + l' + |l - l'|}{2} = \max(l, l')$.

## 6. Exercice 16.6 — Convergence via trois sous-suites
Soit $(u_n)$ une suite telle que les sous-suites $(u_{2n})$, $(u_{2n+1})$ et $(u_{3n})$ convergent. Montrer que la suite $(u_n)$ est convergente.
?
**Réponse:**
Posons $l_1 = \lim u_{2n}$, $l_2 = \lim u_{2n+1}$, $l_3 = \lim u_{3n}$. La suite $(u_{6n})$ est extraite de $(u_{2n})$ et de $(u_{3n})$, donc $l_1 = l_3$. La suite $(u_{6n+3})$ est extraite de $(u_{2n+1})$ et de $(u_{3n})$, donc $l_2 = l_3$. Ainsi $(u_{2n})$ et $(u_{2n+1})$ convergent vers la même limite, donc $(u_n)$ converge vers cette limite.

## 7. Exercice 16.7 — Norme $\|f\| = \|f\|_{\infty} + \|f'\|_{\infty}$
On note $E = \mathcal{C}^1([0, 1], \mathbb{R})$ et, pour tout $f \in E$, $kf k = \|f\|_{\infty} + \|f'\|_{\infty}$. Montrer que $k\cdot k$ est une norme sur $E$. Est-elle équivalente à $\|\cdot\|_{\infty}$ ?
?
**Réponse:**
Séparation : si $kfk = 0$, alors $\|f\|_{\infty} + \|f'\|_{\infty} = 0$, donc $\|f\|_{\infty} = 0$ et $f = 0$. Homogénéité, positivité et inégalité triangulaire découlent de celles de $\|\cdot\|_{\infty}$. Non équivalente à $\|\cdot\|_{\infty}$ : pour $f_n(x) = e^{-nx}$, on a $\|f_n\|_{\infty} = 1$ et $f'_n = -ne^{-nx}$, donc $kf_n k = 1 + n \to +\infty$ : le rapport $\frac{kf_n k}{\|f_n\|_{\infty}} \to +\infty$, impossible pour des normes équivalentes.

## 8. Exercice 16.8 — Le problème des magasins
Une personne a dépensé tout ce qu'elle avait en poche dans $N$ magasins. Dans chacun elle a dépensé dix euros de plus que la moitié de ce qu'elle avait en entrant. Combien avait-elle en poche au départ ?
?
**Réponse:**
Soit $u_n$ l'argent restant après le $n$-ième magasin : $u_{n+1} = u_n - \left( \frac{u_n}{2} + 10 \right) = \frac{u_n}{2} - 10$. Le point fixe de $x \mapsto \frac{x}{2} - 10$ est $l = -20$, donc $u_n + 20 = \frac{u_0 + 20}{2^n}$, i.e. $u_n = \frac{u_0 + 20}{2^n} - 20$. Après $N$ magasins il ne reste rien : $u_N = 0 \iff \frac{u_0 + 20}{2^N} = 20$, d'où $u_0 = 20(2^N - 1)$ euros.

## 9. Exercice 16.9 — Inégalité entre diamètres
$E$ est un espace vectoriel normé, $B$ et $C$ deux parties non vides de $E$. Montrer que $\delta(B \cup C) \leq \delta(B) + \delta(C) + d(B, C)$.
?
**Réponse:**
Soient $x, y \in B \cup C$. Si $x, y \in B$ (ou $x, y \in C$) : $d(x, y) \leq \delta(B) \leq \delta(B) + \delta(C) + d(B, C)$. Sinon, supposons $x \in B$ et $y \in C$ : il existe des suites $(b_n) \subset B$, $(c_n) \subset C$ avec $d(b_n, c_n) \to d(B, C)$ (règle de la borne inférieure). Par l'inégalité triangulaire, $d(x, y) \leq d(x, b_n) + d(b_n, c_n) + d(c_n, y) \leq \delta(B) + d(B, C) + \delta(C)$, et on passe à la limite puis au sup sur $x, y$.

## 10. Exercice 16.10 — Normes $N$ et $n$ équivalentes
On note $E$ l'ensemble des applications de classe $\mathcal{C}^1$ de $[0, 1]$ dans $\mathbb{R}$ telles que $f(0) = 0$. Pour $f \in E$, $N(f) = \|f\|_{\infty} + \|f'\|_{\infty}$ et $n(f) = \|f + f'\|_{\infty}$. 1) Montrer que $N$ et $n$ sont des normes. 2) Montrer qu'elles sont équivalentes.
?
**Réponse:**
1) Tous les axiomes découlent de $\|\cdot\|_{\infty}$ sauf la séparation de $n$ : si $n(f) = 0$, alors $f + f' = 0$, donc $f(t) = \lambda e^{-t}$ ; or $f(0) = 0$ impose $\lambda = 0$, donc $f = 0$. Idem pour $N$.
2) $n(f) \leq \|f\|_{\infty} + \|f'\|_{\infty} = N(f)$. Réciproquement, soit $h = f + f'$ : par variation de la constante, $f(t) = e^{-t} \int_0^t h(x) e^x \, dx$, donc $\|f\|_{\infty} \leq \|h\|_{\infty}$. De plus $\|f'\|_{\infty} = \|f + f' - f\|_{\infty} \leq \|h\|_{\infty} + \|f\|_{\infty}$, d'où $N(f) \leq 3\|h\|_{\infty} = 3n(f)$. Les normes sont donc équivalentes.

## 11. Exercice 16.11 — Suite $z_{n+1} = \frac{z_n + |z_n|}{2}$
On considère une suite de complexes $(z_n)$ vérifiant $z_{n+1} = \frac{1}{2}(z_n + |z_n|)$. Déterminer la limite de $z_n$ en fonction de $z_0$.
?
**Réponse:**
Si $z_0 \in \mathbb{R} \setminus \{0\}$ : la suite est stationnaire dès le premier rang ($z_n = z_0$ si $z_0 \geq 0$, $z_n = 0$ si $z_0 < 0$), donc la limite est $\max(z_0, 0)$ (et $z_0 = 0$ donne $z_n = 0$). Si $z_0 \notin \mathbb{R}$ : écrire $z_n = \rho_n e^{i\theta_n}$ avec $\theta_0 \in ]-\pi, \pi[$. Alors $z_{n+1} = \rho_n \cos\!\left( \frac{\theta_n}{2} \right) e^{i\theta_n/2}$, d'où $\theta_{n+1} = \frac{\theta_n}{2}$ ($\theta_n = \frac{\theta_0}{2^n} \to 0$) et $\rho_{n+1} = \rho_n \cos\!\left( \frac{\theta_0}{2^{n+1}} \right)$. Produit télescopique : $\frac{\rho_n}{\rho_0} = \frac{\sin \theta_0}{2^n \sin(\theta_0 / 2^n)} \to \frac{\sin \theta_0}{\theta_0}$. Finalement $z_n \to \rho_0 \frac{\sin \theta_0}{\theta_0}$.

## 12. Exercice 16.12 — Suites homographiques et fraction continue
On suppose que $u_0 = 1$ et que, pour tout $n \in \mathbb{N}$, $u_{n+1} = 1 + \frac{1}{u_n}$. Déterminer $u_n$ en fonction de $n$, puis en déduire la valeur de $\Phi = 1 + \frac{1}{1 + \frac{1}{1 + \cdots}}$.
?
**Réponse:**
Les points fixes de $x \mapsto \frac{x + 1}{x}$ vérifient $\ell^2 - \ell - 1 = 0$ : $\varphi = \frac{1 + \sqrt{5}}{2}$ et $\widetilde{\varphi} = \frac{1 - \sqrt{5}}{2}$. La suite $v_n = \frac{u_n - \varphi}{u_n - \widetilde{\varphi}}$ vérifie $v_{n+1} = \frac{\widetilde{\varphi}}{\varphi} v_n$, donc $v_n = \left( \frac{\widetilde{\varphi}}{\varphi} \right)^n v_0 \to 0$ car $\left| \frac{\widetilde{\varphi}}{\varphi} \right| < 1$. On en déduit $u_n \to \varphi = \frac{1 + \sqrt{5}}{2}$, et $\Phi = \varphi$ : c'est le nombre d'or.

## 13. Exercice 16.13 — Injection de $\mathbb{N}$ dans $\mathbb{N}$
Soit $f$ une application injective de $\mathbb{N}$ dans $\mathbb{N}$. Démontrer que $(f(n))_{n \in \mathbb{N}}$ diverge vers $+\infty$.
?
**Réponse:**
Soit $M \in \mathbb{R}_+$ et $A = \{ n \in \mathbb{N} \mid f(n) \leq M \}$. Si $A$ était infini, par le principe des tiroirs il existerait $x \neq y$ dans $A$ avec $f(x) = f(y) = k \in \{0, \ldots, \lfloor M \rfloor\}$, contredisant l'injectivité. $A$ est donc fini, donc majoré : il existe $N$ tel que $\forall n \geq N$, $n \notin A$, i.e. $f(n) \geq M$. Ceci prouve $f(n) \to +\infty$.

## 14. Exercice 16.14 — Suites sous-additives au logarithme
Soit $(a_n)$ une suite réelle telle que : $\forall n \in \mathbb{N}$, $a_n \geq 1$, et $\forall (m, n) \in \mathbb{N}^2$, $a_{m+n} \leq a_m a_n$. Montrer que $b_n = \frac{\ln(a_n)}{n}$ converge vers sa borne inférieure.
?
**Réponse:**
Posons $v_n = \ln a_n \geq 0$ ; la condition devient $v_{n+m} \leq v_n + v_m$. On sait qu'il existe une suite $(v_{\phi(n)})$ avec $\frac{v_{\phi(n)}}{\phi(n)} \to l = \inf_{i \in \mathbb{N}} \frac{v_i}{i}$. Soit $\varepsilon > 0$ et $n_0$ tel que $\frac{v_{n_0}}{n_0} \leq l + \varepsilon$ ; division euclidienne $n = q n_0 + r$, $0 \leq r < n_0$ : $v_n \leq q v_{n_0} + v_r \leq n_0(l + \varepsilon) + \max_{r < n_0} v_r$, donc $\frac{v_n}{n} \leq l + \varepsilon + \frac{\max v_r}{n} \leq l + 2\varepsilon$ pour $n$ assez grand. Comme $\frac{v_n}{n} \geq l$, on a $\frac{v_n}{n} \to l$.

## 15. Exercice 16.15 — La suite $(\sin n)$ n'a pas de limite
Démontrer que la suite $(\sin n)_{n \in \mathbb{N}}$ n'a pas de limite.
?
**Réponse:**
Supposons $\sin n \to l$. Alors $\sin(n+2) - \sin n = 2\sin(1)\cos(n+1) \to 0$. D'autre part $\sin(n+2) + \sin n = 2\sin(n+1)\cos(1) \to 2l\cos(1)$, mais aussi $\to 2l$, d'où $2l(1 - \cos 1) = 0$, donc $l = 0$ (puisque $\cos 1 \neq 1$). Alors $2\sin(1)\cos(n+1) \to 0$ donne $\cos n \to 0$. Mais $\cos^2 n + \sin^2 n \to 0^2 + 0^2 = 1$ contredit $\cos^2 n + \sin^2 n = 1$. Contradiction : $(\sin n)$ diverge.

## 16. Exercice 16.16 — Normes $N$ et $N'$ sur $\mathcal{C}^1([0,1])$
$E = \mathcal{C}^1([0, 1], \mathbb{R})$, $\phi$ continue avec $\int_0^1 \phi \neq 0$. Pour $f \in E$ : $N(f) = |f(0)| + \int_0^1 |f'(t)| \, dt$ et $N'(f) = \left| \int_0^1 f(t)\phi(t) \, dt \right| + \int_0^1 |f'(t)| \, dt$. Montrer que $N$ et $N'$ sont des normes équivalentes sur $E$.
?
**Réponse:**
Normes : évident sauf la séparation. Si $N(f) = 0$, alors $f(0) = 0$ et $\int_0^1 |f'| = 0$ ; l'intégrale d'une fonction continue positive nulle étant nulle, $f' = 0$, donc $f$ est constante, et $f(0) = 0$ donne $f = 0$. Si $N'(f) = 0$ : $f$ est constante égale à $C$ et $C \int_0^1 \phi = 0$, donc $C = 0$. Équivalence : par intégration par parties avec $\Phi(t) = \int_1^t \phi \, dx$,
$$
\int_0^1 f(t)\phi(t)\,dt = \Phi(1)f(1) - \Phi(0)f(0) - \int_0^1 \Phi(t) f'(t)\,dt
$$
On en tire $|\int_0^1 f\phi| \leq \|\phi\|_{\infty} N(f)$, donc $N'(f) \leq (1 + \|\phi\|_{\infty}) N(f)$. Réciproquement, la même formule donne $|f(0)| \leq C N'(f)$ avec $C = \max\left( \frac{1}{\int_0^1 \phi}, \frac{\|\phi\|_{\infty}}{\int_0^1 \phi} \right)$, d'où $N(f) \leq (1 + C) N'(f)$.

## 17. Exercice 16.17 — Prolongement lipschitzien de McShane
$E$ est un $\mathbb{R}$-espace vectoriel normé, $A$ une partie non vide de $E$, et $f : A \to \mathbb{R}$ une application $k$-lipschitzienne avec $k > 0$. Pour tout $x \in E$, on pose $g(x) = \sup_{t \in A} (f(t) - k\|x - t\|)$. 1) Montrer que $g$ est bien définie. 2) Montrer que $g$ prolonge $f$ sur $E$. 3) Montrer que $g$ est $k$-lipschitzienne.
?
**Réponse:**
1) Fixons $a \in A$ : pour tout $t \in A$, $f(t) - k\|x - t\| \leq f(a) + k\|t - a\| - k\|x - t\| \leq f(a) + k\|x - a\|$ (inégalité triangulaire). L'ensemble est donc majoré : $g(x)$ existe dans $\mathbb{R}$.
2) Pour $a \in A$ : $g(a) = \sup_{t \in A} (f(t) - k\|a - t\|)$. Comme $f$ est $k$-lipschitzienne, $f(a) \geq f(t) - k\|t - a\|$ pour tout $t$, et l'égalité est atteinte en $t = a$, donc $g(a) = f(a)$ : $g$ prolonge $f$.
3) Soit $(t_n) \subset A$ telle que $f(t_n) - k\|x - t_n\| \to g(x)$. Alors $g(y) \geq f(t_n) - k\|y - t_n\|$, donc $f(t_n) - k\|x - t_n\| - g(y) \leq k(\|y - t_n\| - \|x - t_n\|) \leq k\|x - y\|$. En passant à la limite : $g(x) - g(y) \leq k\|x - y\|$ ; par symétrie, $g$ est $k$-lipschitzienne.

## 18. Exercice 16.18 — Espaces de fonctions et complétude
On note $E$ l'ensemble des applications continues de $[0, 1]$ dans $\mathbb{R}$, muni de la norme infinie. 1) Avec $P_n(x) = \sum_{k=0}^{n} \frac{x^k}{k!}$, déterminer la limite de $(P_n)$. 2) Soit $P$ l'ensemble des applications polynomiales de $[0,1]$ dans $\mathbb{R}$ : montrer que $P$ n'est pas complet. 3) Montrer que $(E, \|\cdot\|_{\infty})$ est un espace complet.
?
**Réponse:**
1) $P_n \to \exp$ pour $\|\cdot\|_{\infty}$ : pour $n \geq N$, $\forall x \in [0, 1]$, $0 \leq e^x - P_n(x) = \sum_{k > n} \frac{x^k}{k!} \leq \sum_{k > n} \frac{1}{k!} \leq \varepsilon$ (reste de Cauchy de la série $\sum \frac{1}{k!}$), donc $\|\exp - P_n\|_{\infty} \leq \varepsilon$.
2) $(P_n)$ converge (donc est de Cauchy) dans $E$, mais $\exp \notin P$ : si $\exp = \sum_{i=0}^{n_0} \alpha_i x^i$, alors sa dérivée $(n_0 + 1)$-ième serait nulle, or c'est $e^x \neq 0$. Absurde. Une suite de Cauchy de $P$ converge donc hors de $P$ : $P$ n'est pas complet.
3) Soit $(f_n)$ une suite de Cauchy de $E$ pour $\|\cdot\|_{\infty}$. Pour $x$ fixé, $(f_n(x))$ est de Cauchy dans $\mathbb{R}$, complet, donc converge vers $g(x)$. Soit $\varepsilon > 0$ et $N$ tel que $\forall p, q \geq N$, $\|f_p - f_q\|_{\infty} \leq \varepsilon$ : en passant à la limite, $\forall n \geq N$, $\|f_n - g\|_{\infty} \leq \varepsilon$, donc $f_n \to g$ uniformément. De plus $g$ est continue (argument en $\varepsilon/3$ : $|g(x) - g(y)| \leq |g(x) - f_N(x)| + |f_N(x) - f_N(y)| + |f_N(y) - g(y)|$), donc $g \in E$ et $E$ est complet.

## 19. Exercice 16.19 — Parties négligeables et suites presque convergentes
$T \subset \mathbb{N}^*$ est négligeable ssi $\frac{|T \cap [1, n]|}{n} \to 0$. Une suite $(a_n)$ de complexes est presque convergente vers $\ell$ ssi il existe $T$ négligeable telle que $|a_n - \ell| \leq \varepsilon$ pour tout $n \geq p$, $n \notin T$. 1) Montrer que $P = \{n \in \mathbb{N}^* \mid \exists m, n = m^2\}$ est négligeable. 2a) Montrer que $a_n = n$ si $n \in P$, $\frac{1}{n}$ sinon, est presque convergente vers 0. 2b) Une sous-suite d'une suite presque convergente est-elle presque convergente ? 3) Si $a_n \geq 0$ et la moyenne de Cesàro $b_n \to 0$ : (a) trouver $u_n$ décroissante, $> 0$, $u_n \to 0$, $b_n/u_n \to 0$ ; (b) $T = \{k \mid a_k \geq u_k\}$ négligeable ; (c) $a_n$ presque convergente vers 0. 4) Montrer que l'hypothèse de positivité est essentielle : exemple avec $|a_n| \to +\infty$ et $b_n \to 0$.
?
**Réponse:**
1) $|P \cap [1, n]| = \lfloor \sqrt{n} \rfloor$, donc $\frac{|P \cap [1, n]|}{n} \leq \frac{\sqrt{n}}{n} \to 0$ : $P$ est négligeable.
2a) Avec $T = P$, pour $n \notin T$, $a_n = \frac{1}{n} \to 0$ : $a_n$ est presque convergente vers 0.
2b) Non en général. Pour $a_n = 1$ si $n \in P$, $0$ sinon (presque convergente vers 0), l'extraction $\varphi(2k) = (2k)^2$, $\varphi(2k+1) = 4k^2 + 1$ donne $a_{\varphi(n)} = 1$ si $n$ pair, $0$ si $n$ impair : les valeurs 0 et 1 apparaissent sur des ensembles de densité positive, donc cette sous-suite n'est presque convergente vers aucune limite.
3a) $s_n = \sup_{k \geq n} b_k \to 0$ ; posons $u_n = \max(\sqrt{s_n}, 2^{-n})$ (décroissante, $> 0$, tend vers 0). Alors $b_n \leq s_n$, donc si $u_n = \sqrt{s_n}$ : $b_n/u_n \leq \sqrt{s_n} \to 0$ ; et si $u_n = 2^{-n}$ : $b_n \leq s_n \leq 2^{-2n}$, d'où $b_n/u_n \leq 2^{-n} \to 0$. Donc $b_n/u_n \to 0$. 3b) Pour $k \in T \cap [1, n]$, $a_k \geq u_k \geq u_n$, donc $|T \cap [1, n]| u_n \leq \sum_{k=1}^n a_k = n b_n$, d'où $\frac{|T \cap [1, n]|}{n} \leq \frac{b_n}{u_n} \to 0$ : $T$ est négligeable. 3c) Pour $n \notin T$, $0 \leq a_n < u_n \to 0$ : $a_n$ est presque convergente vers 0.
4) Exemple : $a_n = (-1)^n \sqrt{n}$. Alors $|a_n| = \sqrt{n} \to +\infty$, et $|\sum_{k=1}^n a_k| \leq \sqrt{n}$ (somme alternée), donc $b_n = \frac{1}{n} \sum_{k=1}^n a_k \to 0$.