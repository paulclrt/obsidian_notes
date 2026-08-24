#flashcards/maths/prépa/premiere_annee/td/06_groupes_anneaux

## 1. Réunion filtrante de sous-groupes
Soient $(G, \cdot)$ un groupe et $(G_i)_{i \in I}$ une famille de sous-groupes telle que $\forall (i,j) \in I^2,\ \exists k \in I,\ G_i \cup G_j \subset G_k$. Montrer que $\bigcup_{i \in I} G_i$ est un sous-groupe de $G$.
?
**Réponse:**
La réunion est non vide (les $G_i$ contiennent $1_G$). Soient $x, y \in \bigcup G_i$ : il existe $i, j$ avec $x \in G_i$, $y \in G_j$. Par hypothèse, $\exists k$ tel que $G_i \cup G_j \subset G_k$, donc $x, y \in G_k$, d'où $xy^{-1} \in G_k \subset \bigcup G_i$. C'est le critère de sous-groupe.

## 2. Tous les éléments d'ordre 2
Soit $G$ un groupe tel que $\forall g \in G,\ g^2 = 1_G$. Montrer que $G$ est abélien.
?
**Réponse:**
Pour tout $g$, $g^2 = 1$ donc $g = g^{-1}$. Alors pour tout $a, b$ :
$$
ab = (ab)^{-1} = b^{-1}a^{-1} = ba
$$
donc $G$ est abélien.

## 3. Morphismes de $(\mathbb{Q}, +)$ dans $(\mathbb{Z}, +)$
Déterminer les morphismes de $(\mathbb{Q}, +)$ dans $(\mathbb{Z}, +)$.
?
**Réponse:**
Soit $f$ un tel morphisme et $f\left(\dfrac{p}{q}\right) = n \in \mathbb{Z}$. Alors :
$$
f\left(\frac{2np}{2nq}\right) = 2n \cdot f\left(\frac{p}{2nq}\right) = n
$$
donc $f\left(\dfrac{p}{2nq}\right) = \dfrac{1}{2}$ : impossible dans $\mathbb{Z}$, sauf si $n = 0$. L'unique morphisme est $f = 0$.

## 4. Sous-groupe d'un groupe cyclique
Montrer que tout sous-groupe d'un groupe cyclique est cyclique.
?
**Réponse:**
Soit $G = \mathrm{Gr}(a)$ et $H$ un sous-groupe. Via le morphisme surjectif $\phi : \mathbb{Z} \to G$, $n \mapsto a^n$, on a $\phi^{-1}(H) = b\mathbb{Z}$ (tous les sous-groupes de $\mathbb{Z}$ sont de cette forme), donc :
$$
H = \phi(\phi^{-1}(H)) = \phi(b\mathbb{Z}) = \mathrm{Gr}(a^b)
$$
donc $H$ est cyclique.

## 5. Réunion de deux sous-groupes
Soient $H$ et $K$ deux sous-groupes de $(G, +)$. Montrer que $H \cup K$ est un groupe ssi $H \subset K$ ou $K \subset H$.
?
**Réponse:**
Si $H \subset K$, alors $H \cup K = K$ est un groupe (idem pour $K \subset H$). Réciproquement, si $H \not\subset K$ et $K \not\subset H$, on prend $h \in H \setminus K$, $k \in K \setminus H$ : si $H \cup K$ était un groupe, $h + k \in H \cup K$. Si $h + k \in H$, alors $k = (h+k) - h \in H$ : absurde. De même si $h + k \in K$. Donc $H \cup K$ n'est pas un groupe.

## 6. Sous-groupes distingués
Définir un sous-groupe distingué. Quels sont ceux d'un groupe commutatif ?
?
**Réponse:**
$H$ est distingué dans $G$ si $\forall a \in G,\ \forall h \in H,\ aha^{-1} \in H$ (stable par conjugaison). Dans un groupe abélien :
$$
aha^{-1} = aa^{-1}h = h \in H
$$
donc tous les sous-groupes sont distingués.

## 7. Sous-groupe distingué et conjugaison
Montrer qu'un sous-groupe $H$ est distingué dans $G$ ssi $\forall a \in G,\ \phi_a(H) = H$ où $\phi_a : x \mapsto axa^{-1}$.
?
**Réponse:**
$\phi_a$ est un automorphisme (son inverse est $\phi_{a^{-1}}$). Si $H$ est distingué, $\forall h,\ \phi_a(h) = aha^{-1} \in H$ donc $\phi_a(H) \subset H$ ; comme $\phi_a$ est bijectif, on a aussi $H = \phi_a(\phi_a^{-1}(H)) \subset \phi_a(H)$, donc égalité. Réciproquement $\phi_a(H) = H$ donne directement $aha^{-1} \in H$.

## 8. Centre d'un groupe
Qu'est-ce que le centre $Z(G)$ ? Montrer qu'il est distingué.
?
**Réponse:**
$Z(G) = \{a \in G / \forall h \in G,\ ah = ha\}$ (les éléments qui commutent avec tout le monde). C'est un sous-groupe. Il est distingué car pour $z \in Z(G)$ et $a \in G$ :
$$
aza^{-1} = aa^{-1}z = z \in Z(G)
$$

## 9. Non-isomorphisme $(\mathbb{R}^*, \times)$ et $(\mathbb{C}^*, \times)$
Montrer que les groupes $(\mathbb{R}^*, \times)$ et $(\mathbb{C}^*, \times)$ ne sont pas isomorphes.
?
**Réponse:**
Soit $f : \mathbb{C}^* \to \mathbb{R}^*$ un isomorphisme. Alors $f(1) = 1$ et :
$$
f((-1)^2) = f(-1)^2 = 1, \qquad f(i^4) = f(i)^4 = 1
$$
donc $f(\{1, -1, i\}) \subset \{1\}$ : contradictoire avec l'injectivité de $f$. Pas d'isomorphisme possible.

## 10. Non-isomorphisme $(\mathbb{Q}, +)$ et $(\mathbb{Q}^*_+, \times)$
En admettant que $\sqrt{2}$ est irrationnel, montrer que $(\mathbb{Q}, +)$ et $(\mathbb{Q}^*_+, \times)$ ne sont pas isomorphes.
?
**Réponse:**
Soit $f : (\mathbb{Q}, +) \to (\mathbb{Q}^*_+, \times)$ un isomorphisme. Il existe $x \in \mathbb{Q}$ avec $f(x) = 2$. Alors :
$$
2 = f(x) = f\left(\frac{x}{2} + \frac{x}{2}\right) = f\left(\frac{x}{2}\right)^2
$$
donc $f\left(\dfrac{x}{2}\right) = \sqrt{2} \notin \mathbb{Q}^*_+$ : absurde.

## 11. $|A| + |B| > |G|$ implique $G = AB$
Soit $(G, \cdot)$ un groupe fini et $A, B \subset G$ tels que $|A| + |B| > |G|$. Montrer que $G = AB$.
?
**Réponse:**
Soit $g \in G$. Il faut montrer que $A \cap gB^{-1} \neq \emptyset$. Sinon, $|G| \geq |A \cup gB^{-1}| = |A| + |gB^{-1}|$. Or $x \mapsto gx^{-1}$ est une bijection de $G$, donc $|gB^{-1}| = |B|$, d'où $|G| \geq |A| + |B| > |G|$ : contradiction.

## 12. Groupes à nombre fini de sous-groupes
Quels sont les groupes qui ne possèdent qu'un nombre fini de sous-groupes ?
?
**Réponse:**
Exactement les groupes **finis** (l'ensemble des parties donne au plus $2^{|G|}$ sous-groupes). Si $G$ était infini avec un nombre fini de sous-groupes, il admettrait un sous-groupe $\langle b \rangle$ infini, isomorphe à $\mathbb{Z}$, qui possède une infinité de sous-groupes (les $n\mathbb{Z}$) : contradiction.

## 13. Décomposition $M \times N$
Soit $G$ commutatif fini avec $\forall x \in G,\ x^n = e$, $n = pq$, $p \wedge q = 1$, $M = \{x / x^p = e\}$, $N = \{x / x^q = e\}$. Montrer que $M \times N \cong G$.
?
**Réponse:**
$M = \mathrm{Ker}(x \mapsto x^p)$ et $N = \mathrm{Ker}(x \mapsto x^q)$ sont des sous-groupes. $M \cap N = \{e\}$ par Bézout ($ap + bq = 1$ donne $x = x^{ap+bq} = e$). Le morphisme $(x,y) \mapsto xy$ a pour noyau $\{(e,e)\}$ (injectif) ; pour $g \in G$ :
$$
g = g^{ap} \cdot g^{bq} \in M \cdot N
$$
donc il est surjectif, puis bijectif.

## 14. Quotient $G/H$ et sous-groupe distingué
Soit $x \mathcal{R} y \iff x^{-1}y \in H$. Montrer que $\mathcal{R}$ est une équivalence et que $\overline{x} = xH$.
?
**Réponse:**
Réflexive ($x^{-1}x = 1 \in H$), symétrique ($x^{-1}y \in H \implies y^{-1}x = (x^{-1}y)^{-1} \in H$), transitive ($x^{-1}z = (x^{-1}y)(y^{-1}z) \in H$). De plus :
$$
y \in \overline{x} \iff x^{-1}y \in H \iff \exists h \in H,\ y = xh \iff y \in xH
$$

## 15. $G/H$ groupe et morphisme
Montrer que si $H$ est distingué, alors $(G/H, \cdot)$ est un groupe et $H$ est le noyau d'un morphisme de $G$.
?
**Réponse:**
Si $H$ est distingué, le produit $\overline{x} \cdot \overline{y} = \overline{xy}$ est bien défini : si $x = x'$ et $y = y'$, alors $y^{-1}(x^{-1}x')y \in H$ et $y^{-1}y' \in H$, donc $(xy)^{-1}(x'y') \in H$. Les axiomes de groupe se vérifient, et $\pi : x \mapsto \overline{x}$ est un morphisme surjectif de noyau $H$. Réciproquement, le noyau de tout morphisme de $G$ est distingué.

## 16. Premier théorème d'isomorphisme
Si $f : G \to G'$ est un morphisme de groupes, montrer que $G / \mathrm{Ker}\,f \cong \mathrm{Im}\,f$.
?
**Réponse:**
On définit $\overline{f} : G/\mathrm{Ker}\,f \to \mathrm{Im}\,f$, $\overline{x} \mapsto f(x)$. C'est bien défini : si $x = y$, alors $x^{-1}y \in \mathrm{Ker}\,f$ donc $f(x) = f(y)$. Injective (si $f(x) = 1$, $x \in \mathrm{Ker}\,f$ donc $\overline{x} = \overline{1}$) et surjective par construction, c'est un isomorphisme.

## 17. Ordre de $x^p$
Soit $x$ d'ordre $pq$ dans un groupe commutatif. Déterminer $o(x^p)$.
?
**Réponse:**
$(x^p)^q = x^{pq} = e$ donc $o(x^p) \mid q$. Si $o(x^p) < q$, alors $x^{p \cdot o(x^p)} = e$ avec $p \cdot o(x^p) < pq$ : contradiction avec $o(x) = pq$. Donc $o(x^p) = q$.

## 18. Ordre d'un produit
Dans un groupe commutatif, $o(x) = p$, $o(y) = q$, $p \wedge q = 1$. Déterminer $o(xy)$.
?
**Réponse:**
$(xy)^{pq} = (x^p)^q (y^q)^p = e$ donc $o(xy) \mid pq$. On écrit $o(xy) = p_0 q_0$ avec $p_0 \mid p$, $q_0 \mid q$. Si $p_0 < p$, alors $e = (xy)^{p_0 q_0 q} = x^{p_0 q_0 q}$ (car $y^{p_0 q_0 q} = e$), donc $o(x) = p \mid p_0 q_0 q$, puis $p \mid p_0$ par le théorème de Gauss : absurde. Donc $p_0 = p$ et $q_0 = q$, d'où $o(xy) = pq$.

## 19. Lemme de Cauchy
Énoncer et démontrer le lemme de Cauchy.
?
**Réponse:**
Si $p$ premier divise $|G|$, il existe $a \in G$ d'ordre $p$. Démonstration : on considère $E = \{(x_1, \ldots, x_p) / x_1 \cdots x_p = 1\}$, qui a $|G|^{p-1}$ éléments, et la relation d'équivalence « permutation circulaire ». Ses classes ont pour cardinal $1$ ou $p$ ; $(1, \ldots, 1)$ forme une classe de cardinal $1$. Comme $|E| \equiv 0 \ [p]$ et $|E| \equiv -1 \ [p]$ si toutes les autres classes étaient de cardinal $p$, il existe une classe $(\overline{a}, \ldots, \overline{a}) \neq (\overline{1}, \ldots, \overline{1})$ de cardinal $1$ : alors $a^p = 1$, $a \neq 1$, donc $o(a) = p$.

## 20. Ordre d'une permutation
Quel est l'ordre de $\sigma = (1\ 3\ 2\ 4\ 5)$ et de $\sigma' = (1\ 5\ 3)(2\ 4)$ ?
?
**Réponse:**
$\sigma$ est un 5-cycle : $o(\sigma) = 5$. Pour $\sigma'$, les cycles à supports disjoints commutent et $\sigma'^k = \mathrm{Id} \iff 3 \mid k$ et $2 \mid k$, donc $o(\sigma') = 6$. De manière générale, l'ordre d'une permutation est le ppcm des longueurs des cycles de sa décomposition.

## 21. Centre de $S_n$
Déterminer le centre $Z_n = \{s \in S_n / \forall \sigma,\ s \circ \sigma = \sigma \circ s\}$.
?
**Réponse:**
$Z_1 = S_1$ et $Z_2 = \{\mathrm{Id}, (1\ 2)\}$ (toutes les permutations commutent). Pour $n \geq 3$, on construit $\sigma_i$ fixant $i$ et déplaçant tout le reste ; la relation $s \circ \sigma_i(i) = \sigma_i \circ s(i)$ force $s(i) = i$ pour tout $i$, donc :
$$
Z_n = \{\mathrm{Id}\}
$$

## 22. $S_n$ engendré par les transpositions $(1\ k)$
Montrer que $S_n$ est engendré par les transpositions $(1\ k)$, $k \in \{2, \ldots, n\}$.
?
**Réponse:**
Toute transposition $(a\ b)$ avec $a, b \geq 2$ se factorise en :
$$
(a\ b) = (1\ a)(1\ b)(1\ a)
$$
(vérification : $1 \mapsto a \mapsto 1 \mapsto 1$, $a \mapsto 1 \mapsto b \mapsto b$, $b \mapsto b \mapsto 1 \mapsto a$). Comme toute permutation est un produit de transpositions, $S_n$ est engendré par les $(1\ k)$.

## 23. $A_n$ engendré par les cycles de longueur 3
Montrer que $A_n$ est engendré par les cycles de longueur 3.
?
**Réponse:**
Une permutation paire est un produit d'un nombre pair de transpositions, donc il suffit de traiter les produits de 2 transpositions :
$$
(a\ b)(b\ c) = (a\ b\ c), \qquad (a\ b)(c\ d) = (a\ b\ c)(b\ c\ d) \quad (\text{supports disjoints})
$$
et le cas $a = c$, $b = d$ donne l'identité. De plus $(1\ 2\ k)$ pour $k \in \{3, \ldots, n\}$ suffit : on exprime tout 3-cycle à l'aide de conjugaisons par des transpositions $(1\ 2)$.

## 24. Morphismes de $S_n$ dans $\{-1, 1\}$
Déterminer tous les morphismes de groupes de $S_n$ dans $\{-1, 1\}$.
?
**Réponse:**
Toute transposition $\tau$ est conjuguée à $(1\ 2)$ : $\tau = \sigma^{-1}(1\ 2)\sigma$. Comme $\{-1, 1\}$ est abélien :
$$
f(\tau) = f(\sigma)^{-1} f(1\ 2) f(\sigma) = f(1\ 2)
$$
est constant. Comme toute permutation est un produit de $k$ transpositions, $f(\sigma) = f(1\ 2)^k = (\pm 1)^k$. Les morphismes sont donc la constante $1$ et la signature $\varepsilon$.

## 25. Inversibles de $\mathcal{F}(E, A)$
Si $A$ est un anneau et $E$ un ensemble, montrer que $\mathrm{Inv}(\mathcal{F}(E, A)) = \mathcal{F}(E, \mathrm{Inv}(A))$.
?
**Réponse:**
Si $f \in \mathrm{Inv}(\mathcal{F}(E,A))$, il existe $g$ tel que $fg = 1_{\mathcal{F}(E,A)}$, donc pour tout $x \in E$, $f(x)g(x) = 1_A$ : chaque $f(x)$ est inversible, $f \in \mathcal{F}(E, \mathrm{Inv}(A))$. La réciproque associe à $f$ à valeurs inversibles l'application $x \mapsto f(x)^{-1}$.

## 26. Idéaux d'un corps
Quels sont les idéaux d'un corps $K$ ?
?
**Réponse:**
Les idéaux d'un corps sont $\{0\}$ et $K$ lui-même. Si $I \neq \{0\}$, prenons $x \in I \setminus \{0\}$ : alors pour tout $y \in K$, $y = (yx^{-1})x \in I$, donc $I = K$. Réciproquement, un anneau commutatif non nul dont les seuls idéaux sont $\{0\}$ et $A$ est un corps.

## 27. Morphisme de corps
Soit $f : K \to A$ un morphisme d'anneaux avec $K$ corps et $A \neq \{0\}$. Montrer que $f$ est injectif.
?
**Réponse:**
$\mathrm{Ker}\,f$ est un idéal de $K$, donc $\mathrm{Ker}\,f = \{0\}$ ou $\mathrm{Ker}\,f = K$. Mais $f(1) = 1 \neq 0$ car $A \neq \{0\}$, donc $1 \notin \mathrm{Ker}\,f$ et $\mathrm{Ker}\,f = \{0\}$ : $f$ est injectif.

## 28. Anneau intègre fini
Montrer que tout anneau intègre fini est un corps.
?
**Réponse:**
Soit $a \neq 0$ et $f : A \to A$, $x \mapsto ax$. $f$ est injective car $ax = ay \implies x = y$ (intègre) ; par égalité des cardinaux, $f$ est bijective, donc $\exists x,\ f(x) = 1$, i.e. $ax = 1$ : $a$ est inversible.

## 29. Éléments de la forme $1 + x$ avec $x$ nilpotent
Soit $N$ l'ensemble des éléments nilpotents d'un anneau commutatif $A$. Montrer que $B = \{1 + x / x \in N\}$ est un groupe pour $\times$.
?
**Réponse:**
$0$ est nilpotent donc $1 \in B$. Stabilité : $(1+x)(1+y) = 1 + x + y + xy$ où $x + y$ et $xy$ sont nilpotents. Inverse de $1 + x$ : si $x^n = 0$, alors $1 = (1+x)\left(1 - x + x^2 - \cdots + (-1)^{n-1}x^{n-1}\right)$, et la somme est nilpotente.

## 30. Nombres décimaux : anneau principal
Montrer que l'anneau des nombres décimaux $D$ est principal.
?
**Réponse:**
$D = \{a / (2^p 5^q)\}$ est un sous-anneau de $\mathbb{Q}$, donc intègre. Soit $I$ un idéal non nul : $\exists d = a/(2^p 5^q) \in I$ donc $a = 2^p 5^q d \in I$ et $I \cap \mathbb{N}^* \neq \emptyset$. Soit $k = \min(I \cap \mathbb{N}^*)$ : on montre $I = kD = \mathrm{Id}(k)$ (division euclidienne de $b \in I$ par $k$, reste nul par minimalité).

## 31. $1 - ab$ inversible implique $1 - ba$ inversible
Dans un anneau $A$, si $1 - ab$ est inversible, montrer que $1 - ba$ est aussi inversible.
?
**Réponse:**
Formellement, $\dfrac{1}{1-ba} = 1 + b(1-ab)^{-1}a$. On vérifie :
$$
(1 - ba)\left(1 + b(1-ab)^{-1}a\right) = 1 + b\left[(1-ab)(1-ab)^{-1} - 1\right]a = 1
$$
et de même à gauche. C'est la version algébrique de la série géométrique.

## 32. Inversibles de $\mathbb{Z}[j]$
Soit $j = e^{2i\pi/3}$. Montrer que $u \in \mathbb{Z}[j]$ est inversible ssi $|u| = 1$, et déterminer $U(\mathbb{Z}[j])$.
?
**Réponse:**
$\mathbb{Z}[j]$ est un sous-anneau de $\mathbb{C}$ (stable par produit car $j^2 = 1 - j$). Si $u$ est inversible, $u \cdot u^{-1} = 1$ donne $|u|^2 |u^{-1}|^2 = 1$ avec $|u|^2 = a^2 + b^2 - ab \in \mathbb{Z}$ (entier), donc $|u|^2 = 1$. La condition $a^2 + b^2 \leq 2$ donne :
$$
U(\mathbb{Z}[j]) = \{1, -1, j, -j, 1+j, -1-j\}
$$

## 33. Idéaux de l'anneau $(\mathcal{P}(E), \Delta, \cap)$
Montrer que tous les idéaux de $(\mathcal{P}(E), \Delta, \cap)$, $E$ fini, sont principaux.
?
**Réponse:**
Pour un idéal $I$, on pose $X_0 = \bigcup_{X \in I} X$. On montre que $X_0 \in I$ (car $A \Delta B$ et intersections permettent d'écrire $A \cup B \in I$, et $E$ fini), et alors $I = \mathrm{Id}(X_0) = \mathcal{P}(X_0)$. Si $E$ est infini, c'est faux : l'ensemble des parties finies de $E$ est un idéal non principal.

## 34. Équation dans $\mathbb{Z}/13\mathbb{Z}$
Résoudre dans $\mathbb{Z}/13\mathbb{Z}$ l'équation $x^2 + 2x + 10 = 0$.
?
**Réponse:**
On transforme : $x^2 + 2x + 10 \equiv 0 \iff (x+1)^2 \equiv -9 \equiv 4 \ [13]$. Donc $x + 1 \equiv \pm 2$, soit :
$$
x \equiv 1 \quad \text{ou} \quad x \equiv -3 \equiv 10 \ [13]
$$
On peut aussi vérifier que $1$ est racine évidente du polynôme $X^2 + 2X + 10 \in \mathbb{Z}/13\mathbb{Z}[X]$.

## 35. Idempotents de $\mathbb{Z}/n\mathbb{Z}$
Résoudre $x^2 = x$ dans $\mathbb{Z}/p\mathbb{Z}$, $\mathbb{Z}/34\mathbb{Z}$, $\mathbb{Z}/30\mathbb{Z}$.
?
**Réponse:**
Dans $\mathbb{Z}/p\mathbb{Z}$ intègre : $x(x-1) = 0 \iff x = 0$ ou $x = 1$. Pour $n$ composé, on passe par le théorème chinois. Pour $34 = 2 \times 17$ : $x \in \{0, 1, 17, 18\}$. Pour $30 = 2 \times 3 \times 5$ :
$$
x \in \{0, 1, 6, 10, 15, 16, 21, 25\}
$$

## 36. Ordre de l'image d'un élément
Soit $f : G \to G'$ un morphisme et $x$ d'ordre fini $n$. Montrer que $f(x)$ est d'ordre fini divisant $n$.
?
**Réponse:**
$x^n = 1$ donc $f(x^n) = f(1) = 1$, i.e. $f(x)^n = 1$. L'ordre de $f(x)$ est donc fini et divise $n$. Conséquence : pour compter les morphismes $\mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}$, il suffit que $o(f(1)) \mid n$ et $o(f(1)) \mid m$.

## 37. Morphismes de $\mathbb{Z}/7\mathbb{Z}$ dans $\mathbb{Z}/13\mathbb{Z}$
Déterminer tous les morphismes de groupes de $\mathbb{Z}/7\mathbb{Z}$ dans $\mathbb{Z}/13\mathbb{Z}$.
?
**Réponse:**
Un morphisme est déterminé par $f(1)$, et $o(f(1)) \mid 7$ donc $o(f(1)) \in \{1, 7\}$, mais aussi $o(f(1)) \mid 13$. Seule possibilité : $o(f(1)) = 1$, donc $f(1) = 0$. L'unique morphisme est $f = 0$.

## 38. Morphismes de $\mathbb{Z}/3\mathbb{Z}$ dans $\mathbb{Z}/12\mathbb{Z}$
Déterminer tous les morphismes de groupes de $\mathbb{Z}/3\mathbb{Z}$ dans $\mathbb{Z}/12\mathbb{Z}$.
?
**Réponse:**
$o(f(1)) \mid 3$ donc $o(f(1)) \in \{1, 3\}$. Les éléments d'ordre $3$ de $\mathbb{Z}/12\mathbb{Z}$ sont $4$ et $8$. Donc :
$$
f = 0, \quad f : \overline{k} \mapsto 4k, \quad f : \overline{k} \mapsto 8k
$$

## 39. Bijectivité de $x \mapsto x^k$ sur $\mathbb{Z}/p\mathbb{Z}$
Soit $p$ premier et $k \wedge (p-1) = 1$. Montrer que $\mathbb{Z}/p\mathbb{Z}^* \to \mathbb{Z}/p\mathbb{Z}^*$, $x \mapsto x^k$ est une bijection.
?
**Réponse:**
$k$ est inversible modulo $p-1$ : il existe $u$ tel que $uk \equiv 1 \ [p-1]$, i.e. $uk = a(p-1) + 1$. Alors pour $x \in \mathbb{Z}/p\mathbb{Z}^*$ :
$$
(x^k)^u = x^{a(p-1)+1} = (x^{p-1})^a x = x
$$
par le petit théorème de Fermat : $x \mapsto x^u$ est l'inverse de $x \mapsto x^k$.

## 40. Somme des $k$-èmes puissances
Soit $p$ premier. Montrer que $\displaystyle\sum_{x \in \mathbb{Z}/p\mathbb{Z}} x^k \in \{0, -1\}$.
?
**Réponse:**
Si $k = 0$, la somme vaut $0$. Sinon, pour $y \in \mathbb{Z}/p\mathbb{Z}^*$ fixé, $x \mapsto xy$ est une bijection, donc $S = \sum x^k$ vérifie $S = \sum (xy)^k = Sy^k$, d'où $S(1 - y^k) = 0$. Donc soit $S = 0$, soit $y^k = 1$ pour tout $y$ inversible (c'est le cas $S = -1$ en sommant sur les $y$).

## 41. Éléments nilpotents de $\mathbb{Z}/n\mathbb{Z}$
Soit $n = \prod p_i^{\alpha_i}$. Quels sont les éléments nilpotents de $\mathbb{Z}/n\mathbb{Z}$ ?
?
**Réponse:**
$x$ est nilpotent ssi $n \mid x^m$ pour un $m$, ssi $\forall i,\ \alpha_i \leq m \cdot v_{p_i}(x)$, i.e. $\forall i,\ v_{p_i}(x) \geq 1$. Donc :
$$
\mathrm{Nil}(\mathbb{Z}/n\mathbb{Z}) = \left\{ x \ \middle| \ \prod p_i \mid x \right\}
$$
Il n'y a des nilpotents non nuls que si $n$ n'est pas sans facteur carré.

## 42. Diviseurs de 0 et nilpotents
Donner une CNS pour que tout diviseur de 0 de $\mathbb{Z}/n\mathbb{Z}$ soit nilpotent.
?
**Réponse:**
CNS : $k = 1$, i.e. $n = p^\alpha$ est une puissance d'un nombre premier. Si $k \geq 2$, un facteur $q$ (premier distinct d'un autre) est un diviseur de zéro mais n'est pas nilpotent d'après la caractérisation précédente.

## 43. Théorème de Wilson
Montrer que $(p-1)! \equiv -1 \ [p]$ ssi $p$ est premier.
?
**Réponse:**
Si $p$ premier : dans $\mathbb{Z}/p\mathbb{Z}$, $k = k^{-1} \iff k^2 = 1 \iff k = \pm 1$. Les éléments $2, \ldots, p-2$ se regroupent par paires inverses, donc $(p-1)! = (p-1) \times 1 = -1 \ [p]$. Réciproquement si $n \geq 2$ non premier, $n = pq$ : pour $p \neq q$, $p$ et $q$ divisent $(n-1)!$ donc $n \mid (n-1)!$ ; pour $p = q = k$, $n = k^2$ et $2k \mid (n-1)!$ quand $k \geq 3$, donc $(n-1)! \equiv 0 \ [n]$.

## 44. Morphisme involutif
Soit $G$ fini et $f$ un endomorphisme tel que $\mathrm{Card}\{x / f(x) = x^{-1}\} > |G|/2$. Montrer que $f \circ f = \mathrm{Id}$.
?
**Réponse:**
Soit $F = \{x / f(x) = x^{-1}\}$. Si $x \in F$, $f(f(x)) = f(x^{-1}) = (f(x))^{-1} = x$. On montre que $aF \cap F \neq \emptyset$ pour tout $a$ (sinon $|aF| + |F| > |G|$ contradiction). Alors $a = yx^{-1}$ avec $y, x \in F$, et $f(f(a)) = f(f(yx^{-1})) = yx^{-1} = a$ pour tout $a$ : $f$ est involutive.

## 45. $q$ divise $2^p - 1$
Soient $p, q$ premiers impairs et $q \mid 2^p - 1$. Montrer que $q \equiv 1 \ [2p]$.
?
**Réponse:**
Dans $(\mathbb{Z}/q\mathbb{Z}^*, \times)$, $2^p \equiv 1$ donc $o(2) \mid p$, et $p$ premier donne $o(2) \in \{1, p\}$ ; $2 \neq 1$ donc $o(2) = p$. Comme $|(\mathbb{Z}/q\mathbb{Z})^*| = q - 1$, $p \mid q - 1$. Et $q$ impair donne $2 \mid q - 1$, donc $q \equiv 1 \ [2p]$ (car $p \wedge 2 = 1$).

## 46. Équation diophantienne de degré 3
Résoudre $5x^3 + 11y^3 + 13z^3 = 0$ dans $\mathbb{Z}^3$.
?
**Réponse:**
Unique solution $(0, 0, 0)$. Modulo $13$ : $5x^3 + 11y^3 \equiv 0$. Si $x \neq 0$, $(yx^{-1})^3 \equiv 9$ et $(yx^{-1})^{12} \equiv 9^4 \neq 1$ : contredit le théorème de Fermat. Donc $x = 13x'$ et de même $y = 13y'$ ; l'équation devient $5(13^2 x'^3) + 11(13^2 y'^3) + z^3 = 0$, donc $13 \mid z$. Par récurrence, $13^k \mid x, y, z$ pour tout $k$ : la seule solution est $(0,0,0)$.

## 47. Groupe dérivé
Définir $D(G) = \mathrm{Gr}\{xyx^{-1}y^{-1}\}$. Montrer que $D(G)$ est distingué et que $G/H$ est abélien ssi $D(G) \subseteq H$.
?
**Réponse:**
Les automorphismes intérieurs $x \mapsto gxg^{-1}$ envoient commutateurs sur commutateurs, donc $D(G)$ est distingué. De plus :
$$
G/H \ \text{abélien} \iff \forall x, y,\ \overline{x}\,\overline{y} = \overline{y}\,\overline{x} \iff x^{-1}y^{-1}xy \in H \iff D(G) \subseteq H
$$

## 48. Centre d'un groupe fini non abélien
Soit $G$ fini non abélien et $Z$ son centre. Montrer que $|Z| \leq |G|/4$.
?
**Réponse:**
Pour $x \in G \setminus Z$, le centralisateur $C_x = \{g / gx = xg\}$ est un sous-groupe strict de $G$ contenant $Z$ strictement (car $x \in C_x$, $x \notin Z$). Par Lagrange, $|C_x| \leq |G|/2$, et $|Z| \leq |C_x|/2 \leq |G|/4$ (car $Z \subsetneq C_x$).

## 49. Divisibilité de $n(n^2 + 5)$
Montrer que pour tout $n \in \mathbb{N}$, $6$ divise $n(n^2 + 5)$.
?
**Réponse:**
$$
n(n^2 + 5) = n(n^2 - 1) + 6n = (n-1)n(n+1) + 6n
$$
Le produit de 3 entiers consécutifs $(n-1)n(n+1)$ est divisible par $3$ et par $2$, donc par $6$ (car $2 \wedge 3 = 1$). Comme $6n$ l'est aussi, $6 \mid n(n^2 + 5)$.

## 50. Équation $3x^2 + xy = 11$
Résoudre $3x^2 + xy = 11$ en $(x, y) \in \mathbb{Z}^2$.
?
**Réponse:**
$x(3x + y) = 11$ : $x$ et $3x + y$ sont des diviseurs de $11$. Les possibilités $x \in \{-11, -1, 1, 11\}$ donnent :
$$
(x, y) \in \{(-11, 32), (-1, -8), (1, 8), (11, -32)\}
$$

## 51. Déterminer une fonction type pgcd
Soit $f : \mathbb{N}^* \times \mathbb{N}^* \to \mathbb{N}^*$ symétrique, avec $f(m, m) = m$ et $f(m + n, n) = f(m, n)$. Déterminer $f$.
?
**Réponse:**
$f = \mathrm{pgcd}$. Par récurrence sur $|m - n|$ : si $m = n$, $f(m,m) = m = \mathrm{pgcd}(m,m)$. Sinon, par symétrie et par la troisième propriété, $f(m, n) = f(m - n, n)$ (quitte à supposer $m \geq n$), puis on applique l'hypothèse de récurrence et l'algorithme d'Euclide : $f(m, n) = \mathrm{pgcd}(m - n, n) = \mathrm{pgcd}(m, n)$.

## 52. Nombres premiers entre eux en famille
Soit $a = m!$ et $\alpha_i = a(i+1) + 1$ pour $i \in \{0, \ldots, m\}$. Montrer que les $\alpha_i$ sont deux à deux premiers entre eux.
?
**Réponse:**
Si $q$ premier divise $\alpha_i$ et $\alpha_j$ ($i \neq j$), alors $q \mid \alpha_i - \alpha_j = m!(i - j)$. Donc $q \mid m!$ ou $q \mid (i-j)$, d'où $q \leq m$ (ou $q$ intervient dans $m!$), et alors $q \mid m!(i+1)$ donc $q \mid \alpha_i - m!(i+1) = 1$ : contradiction.

## 53. Indépendance sur les racines carrées
Montrer que si $\alpha + \beta\sqrt{2} + \gamma\sqrt{3} = 0$ avec $\alpha, \beta, \gamma \in \mathbb{Q}$, alors $\alpha = \beta = \gamma = 0$.
?
**Réponse:**
On élève au carré : $(\beta\sqrt{2} + \gamma\sqrt{3})^2 = \alpha^2$ donne $2\beta\gamma\sqrt{6} = \alpha^2 - 2\beta^2 - 3\gamma^2 \in \mathbb{Q}$. Comme $\sqrt{6}$ est irrationnel, $2\beta\gamma = 0$. Si $\gamma = 0$, $\alpha + \beta\sqrt{2} = 0$ donne $\beta = 0$ (irrationalité de $\sqrt{2}$), puis $\alpha = 0$. Idem si $\beta = 0$.

## 54. Équation $x^2 - 2y^2 = 3$
Résoudre $x^2 - 2y^2 = 3$ en $(x, y) \in \mathbb{Z}^2$. Indication : modulo 8.
?
**Réponse:**
Modulo $8$ : les carrés sont $0, 1, 4$ et $2y^2 \in \{0, 2\}$. Donc $x^2 = 3 + 2y^2 \in \{3, 5\}$, ce qui n'est jamais un carré modulo $8$. L'équation n'a aucune solution.

## 55. Nombres de Mersenne et de Fermat
Si $a^n - 1$ est premier ($a \geq 1$, $n \geq 2$), que dire de $a$ et $n$ ?
?
**Réponse:**
$a^n - 1 = (a-1)(a^{n-1} + \cdots + 1)$ : le facteur $a - 1$ doit valoir $1$, donc $a = 2$. Si $n = pq$ composé, $2^n - 1 = (2^p - 1)(\cdots)$ est composé, donc $n$ est premier. Ainsi :
$$
a^n - 1 \ \text{premier} \iff a = 2 \ \text{et} \ n \ \text{premier}
$$

## 56. Nombre de Fermat $a^n + 1$
Si $a^n + 1$ est premier ($a \geq 2$), que dire de $a$ et $n$ ?
?
**Réponse:**
Si $n$ est impair, $a^n + 1 = (a+1)(a^{n-1} - a^{n-2} + \cdots - a + 1)$ est composé, donc $n$ est pair. Si $a$ est impair, $a^n + 1 \equiv 0 \ [2]$ et $a^n + 1 > 2$ : composé, donc $a$ est pair. Si $n = 2^k p$ avec $p$ impair, $(a^{2^k})^p + 1$ est composé, donc $n$ est une puissance de $2$. Donc $a$ pair et $n = 2^k$.

## 57. Équation $ax \equiv b \ [m]$
Expliquer comment résoudre $ax \equiv b \ [m]$.
?
**Réponse:**
Si $a \wedge m = 1$, Bézout donne $au + mv = 1$, donc $x \equiv bu \ [m]$ est l'unique solution. Si $d = a \wedge m > 1$ : si $d \nmid b$, aucune solution ; si $d \mid b$, on simplifie : $(a/d)x \equiv b/d \ [m/d]$, avec $a/d \wedge m/d = 1$, et on applique le premier cas.

## 58. Systèmes de congruences
Résoudre $\begin{cases} x \equiv 1 \ [6] \\ x \equiv 2 \ [7] \end{cases}$ et $\begin{cases} 3x \equiv 2 \ [5] \\ 5x \equiv 1 \ [6] \end{cases}$.
?
**Réponse:**
En multipliant par des facteurs d'inversibilité pour unifier les moduli à $42$ puis $30$ :
$$
x \equiv -5 \ [42], \qquad x \equiv -1 \ [30]
$$
Méthode générale : se ramener à $x \equiv b \ [n]$, $x \equiv b' \ [n']$, puis par Bézout $au + bv = 1$ construire $x_0 = \beta ua + \alpha bv$ ; la solution est $x \equiv x_0 \ [ab]$ (théorème chinois).

## 59. $\binom{p-1}{k}$ modulo $p$
Soit $p$ premier et $k \in \{1, \ldots, p-1\}$. Montrer que $p \mid \binom{p-1}{k} - (-1)^k$.
?
**Réponse:**
$$
k! \binom{p-1}{k} = (p-1)(p-2) \cdots (p-k) \equiv (-1)(-2) \cdots (-k) = k!(-1)^k \ [p]
$$
Comme $p \wedge k! = 1$ (car $p$ premier et $k < p$), on peut simplifier par $k!$ : $\binom{p-1}{k} \equiv (-1)^k \ [p]$.

## 60. Nombre de zéros de $100!$
Par combien de 0 se termine $100!$ ?
?
**Réponse:**
Le nombre de 0 est $\min(v_2(100!), v_5(100!)) = v_5(100!)$ :
$$
v_5(100!) = \left\lfloor \frac{100}{5} \right\rfloor + \left\lfloor \frac{100}{25} \right\rfloor = 20 + 4 = 24
$$
$100!$ se termine par 24 zéros. Formule de Legendre : $v_p(n!) = \sum_{k \geq 1} \left\lfloor \dfrac{n}{p^k} \right\rfloor$.

## 61. Somme des chiffres itérée
Soit $f(n)$ la somme des chiffres de $n$ en base 10. Calculer $f(f(f(N)))$ pour $N = 4444^{4444}$.
?
**Réponse:**
$10^q \equiv 1 \ [9]$ donc $N \equiv f(f(f(N))) \ [9]$. Or $4444 \equiv 7 \ [9]$ et $7^3 \equiv 1 \ [9]$, $4444 \equiv 1 \ [3]$ donc $N \equiv 7 \ [9]$. De plus $f(f(f(N))) \leq 13$ (bornes successives : $N \leq 10^{22220}$, etc.), donc $f(f(f(N))) = 7$ (seul multiple de la bonne valeur à $\equiv 7 \ [9]$ dans $[0, 13]$).

## 62. $\cos(2\pi/7)$ irrationnel
En exprimant $\cos 3\theta$ et $\cos 4\theta$, montrer que $\cos(2\pi/7)$ n'est pas rationnel.
?
**Réponse:**
Pour $\theta = 2\pi/7$, $3\theta + 4\theta = 2\pi$ donne $\cos 3\theta = \cos 4\theta$, donc $x = \cos\theta$ vérifie :
$$
4x^3 - 3x = 8x^4 - 8x^2 + 1
$$
Si $x = p/q$ irréductible, $q \mid 8$ et $p \mid 1$ (théorème de Gauss), donc $x \in \{\pm 1/8, \pm 1/4, \pm 1/2, \pm 1\}$. Or $\cos(2\pi/7) \in ]\cos(\pi/3), 1[$ : aucune de ces valeurs ne convient, donc $\cos(2\pi/7) \notin \mathbb{Q}$.

## 63. Une infinité de premiers $4k - 1$
Montrer qu'il existe une infinité de nombres premiers de la forme $4k - 1$.
?
**Réponse:**
Supposons l'ensemble $A = \{p_1, \ldots, p_n\}$ fini. Soit $N = p_1 \cdots p_n$. Alors $N^2 - 2 \equiv 1 - 2 \equiv -1 \ [4]$, donc $N^2 - 2$ admet un facteur premier $p \equiv -1 \ [4]$ (un produit de nombres $\equiv 1 \ [4]$ reste $\equiv 1 \ [4]$). Alors $p \in A$, donc $p \mid N$, d'où $p \mid (N^2 - 2) - N^2 = -2$ : impossible car $p$ est impair. Contradiction.

## 64. Produits premiers entre eux et puissances
Soient $a, b \in \mathbb{Z}^*$ premiers entre eux et $ab = n^k$ ($k \geq 2$). Montrer que $a$ et $b$ sont des puissances $k$-ièmes.
?
**Réponse:**
Pour chaque premier $p$, $v_p(ab) = v_p(a) + v_p(b)$ est un multiple de $k$. Comme $a \wedge b = 1$, pour chaque $p$ un seul des deux termes est non nul, donc $k \mid v_p(a)$ et $k \mid v_p(b)$ : $a = \pm x^k$ et $b = \pm y^k$.

## 65. Équation $x^2 + x = y^k$
Résoudre $x^2 + x = y^k$ d'inconnues $x, y \in \mathbb{Z}$.
?
**Réponse:**
Si $y \neq 0$ : $x(x+1) = y^k$ avec $x \wedge (x+1) = 1$, donc $x = m^k$ et $x+1 = n^k$ par l'exercice précédent, d'où $n^k - m^k = 1$ avec $n^k - m^k = (n-m)(\cdots) \geq 2$ : impossible. Si $y = 0$ : $x(x+1) = 0$ donne :
$$
(x, y) \in \{(0, 0), (-1, 0)\}
$$

## 66. Équation $x^2 + px = y^2$
Soit $p$ premier. Résoudre $x^2 + px = y^2$ d'inconnues $(x, y) \in \mathbb{N}^2$.
?
**Réponse:**
Si $p \mid x$, $x = pn$ : $p^2 n(n+1) = y^2$ donne $n(n+1)$ carré, donc $n = 0$, d'où $(0, 0)$. Si $p \nmid x$ : $x \wedge (p + x) = 1$ (un diviseur commun divise $p$) et $x(p+x) = y^2$, donc $x = k^2$, $p + x = k'^2$, d'où $k'^2 - k^2 = (k'-k)(k'+k) = p$. Comme $p$ est premier, $k' - k = 1$, $k' + k = p$ :
$$
(x, y) = \left( \left(\frac{p-1}{2}\right)^2, \frac{p^2 - 1}{4} \right)
$$
(pas de solution pour $p = 2$ dans ce cas).

## 67. $\binom{p-1}{k} \equiv (-1)^k$ — application
Vérifier l'identité $k! \binom{p-1}{k} = (p-1)(p-2) \cdots (p-k)$.
?
**Réponse:**
$$
k! \binom{p-1}{k} = k! \frac{(p-1)!}{k!(p-1-k)!} = \frac{(p-1)!}{(p-1-k)!} = (p-1)(p-2) \cdots (p-k)
$$
C'est le point de départ pour montrer $p \mid \binom{p-1}{k} - (-1)^k$ en réduisant chaque facteur modulo $p$.

## 68. Résolution d'un système par le théorème chinois
Énoncer la version constructive du théorème chinois pour $x \equiv \alpha \ [a]$, $x \equiv \beta \ [b]$ avec $a \wedge b = 1$.
?
**Réponse:**
Par Bézout il existe $u, v$ avec $au + bv = 1$. Alors :
$$
x_0 = \beta u a + \alpha b v
$$
vérifie $x_0 \equiv \alpha \ [a]$ et $x_0 \equiv \beta \ [b]$, et l'ensemble des solutions est $x \equiv x_0 \ [ab]$.
