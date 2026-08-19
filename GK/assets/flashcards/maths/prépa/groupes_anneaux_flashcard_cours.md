#flashcards/maths/prépa/groupes_anneaux/cours

## 1. Définition d'un groupe
Qu'est-ce qu'un groupe $(G, \times)$ ?
?
**Réponse:**
Un monoïde dont tout élément possède un symétrique pour la loi interne :
$$
\forall x \in G,\ \exists y \in G,\quad x \times y = y \times x = 1_G
$$

## 2. Les trois axiomes d'un groupe
Quelles sont les 3 axiomes d'un groupe $(G, \cdot)$ ?
?
**Réponse:**
1. **Associativité** :
$$
\forall x, y, z \in G,\quad x(yz) = (xy)z
$$
2. **Élément neutre $1_G$** :
$$
\forall x \in G,\quad 1_G \cdot x = x \cdot 1_G = x
$$
3. **Symétrique** :
$$
\forall x \in G,\ \exists x^{-1} \in G,\quad xx^{-1} = x^{-1}x = 1_G
$$

## 3. Unicité du symétrique
Le symétrique d'un élément d'un groupe est-il unique ?
?
**Réponse:**
Oui. Si $y$ et $z$ sont deux symétriques de $x$, alors :
$$
y = y \cdot e = y \cdot (xz) = (yx)z = e \cdot z = z
$$

## 4. Groupe commutatif
Quelle notation utilise-t-on pour un groupe commutatif (abélien) ?
?
**Réponse:**
La notation additive $(G, +)$ : neutre noté $0_G$, symétrique de $x$ noté $-x$.

## 5. Exemples de groupes
Citer des exemples de groupes commutatifs et de groupe non commutatif.
?
**Réponse:**
$(\mathbb{Z}, +)$, $(\mathbb{Q}, +)$, $(\mathbb{R}^*, \times)$ sont commutatifs ; l'ensemble des matrices inversibles de $M_n(\mathbb{R})$ muni de la multiplication est un groupe non commutatif.

## 6. Ordre d'un groupe fini
Que vaut le cardinal d'un groupe fini ?
?
**Réponse:**
C'est son **ordre**.

## 7. Commutatif et abélien
« Commutatif » et « abélien » sont-ils synonymes pour un groupe ?
?
**Réponse:**
Oui.

## 8. Élément régulier
Pourquoi dit-on qu'un élément $a$ d'un groupe est régulier (simplifiable) ?
?
**Réponse:**
Car il est simplifiable à gauche et à droite :
$$
\forall x, y \in G,\quad ax = ay \implies x = y \quad\text{et}\quad xa = ya \implies x = y
$$

## 9. Inverse d'un produit
Calculer $(xy)^{-1}$ dans un groupe.
?
**Réponse:**
$(xy)^{-1} = y^{-1}x^{-1}$ (on « retourne » le produit).

## 10. Double inverse
Calculer $(x^{-1})^{-1}$ dans un groupe.
?
**Réponse:**
$(x^{-1})^{-1} = x$.

## 11. Règles de calcul additives
Rappeler les deux règles de calcul en notation additive.
?
**Réponse:**
$x - (y + z) = x - y - z$ et $x - (y - z) = x - y + z$.

## 12. Groupe produit
Quelle est la loi du groupe produit $G_1 \times \cdots \times G_n$ ?
?
**Réponse:**
La loi composante par composante :
$$
(x_1, \ldots, x_n) \cdot (y_1, \ldots, y_n) = (x_1 \cdot_1 y_1, \ldots, x_n \cdot_n y_n)
$$

## 13. Produit abélien
Quand un groupe produit est-il abélien ?
?
**Réponse:**
Si et seulement si chacun des groupes $G_i$ est abélien.

## 14. Groupe fonctionnel
Quelle est la loi du groupe fonctionnel $G^A$ ?
?
**Réponse:**
$$
\forall f, g \in G^A,\ \forall a \in A,\quad (f \cdot g)(a) = f(a) \cdot g(a)
$$
Neutre : l'application constante $a \mapsto 1_G$. Symétrique : $f^{-1} : a \mapsto [f(a)]^{-1}$.

## 15. Groupe symétrique
Qu'est-ce que le groupe symétrique $S(E)$ ?
?
**Réponse:**
L'ensemble des bijections de $E$ dans $E$, muni de la loi de composition. Neutre $= Id_E$, symétrique de $f$ $= f^{-1}$ (bijection réciproque).

## 16. Commutativité de $S(E)$
$S(E)$ est-il toujours commutatif ?
?
**Réponse:**
Non. $S(E)$ est commutatif si et seulement si $E$ a moins de 2 éléments.

## 17. Caractérisation d'un sous-groupe
Donner la caractérisation d'un sous-groupe $H$ de $G$ (3 conditions).
?
**Réponse:**
$H$ est un sous-groupe de $G$ ssi :
$$
\begin{cases}
H \neq \emptyset \\
\forall x, y \in H,\ xy \in H \quad \text{(stabilité du produit)} \\
\forall x \in H,\ x^{-1} \in H \quad \text{(stabilité du symétrique)}
\end{cases}
$$

## 18. Caractérisation en une condition
Donner la caractérisation équivalente en une seule condition.
?
**Réponse:**
$H$ sous-groupe de $G$ ssi $H \neq \emptyset$ et $\forall x, y \in H,\ xy^{-1} \in H$.

## 19. Plus petit sous-groupe
Quel est le plus petit sous-groupe d'un groupe $G$ ?
?
**Réponse:**
$\{1_G\}$ (et $G$ est le plus grand).

## 20. Transitivité des sous-groupes
Un sous-groupe d'un sous-groupe de $G$ est-il un sous-groupe de $G$ ?
?
**Réponse:**
Oui (propriété de transitivité).

## 21. Intersection de sous-groupes
L'intersection de sous-groupes est-elle un sous-groupe ?
?
**Réponse:**
Oui. La réunion ne l'est pas en général.

## 22. Groupe engendré par une partie
Qu'est-ce que le groupe engendré par une partie $A$, noté $\mathrm{Gr}(A)$ ?
?
**Réponse:**
L'intersection de tous les sous-groupes de $G$ contenant $A$ : c'est le **plus petit** sous-groupe contenant $A$.

## 23. Écriture de $\mathrm{Gr}(A)$
Comment s'écrit $\mathrm{Gr}(A)$ en général ?
?
**Réponse:**
$$
\mathrm{Gr}(A) = \left\{ \prod_{i=1}^{n} a_i \ \middle|\ n \in \mathbb{N},\ \forall i,\ a_i \in A \cup A^{-1} \right\}
$$
(produits finis d'éléments de $A$ et de leurs inverses)

## 24. $\mathrm{Gr}(\emptyset)$
Que vaut $\mathrm{Gr}(\emptyset)$ ?
?
**Réponse:**
$\mathrm{Gr}(\emptyset) = \{1_G\}$.

## 25. Partie génératrice
Quand dit-on que $A$ est une partie génératrice de $G$ ?
?
**Réponse:**
Lorsque $\mathrm{Gr}(A) = G$.

## 26. $\mathrm{Gr}(A)$ en notation additive
Comment s'écrit $\mathrm{Gr}(A)$ en notation additive ?
?
**Réponse:**
$$
\mathrm{Gr}(A) = \left\{ \sum_{a \in A} n_a \cdot a \ \middle|\ (n_a) \in \mathbb{Z}^{(A)} \right\}
$$
où $\mathbb{Z}^{(A)}$ est l'ensemble des familles presque nulles d'entiers.

## 27. Définition de $a^n$
Comment définit-on $a^n$ pour $n \in \mathbb{Z}$ ?
?
**Réponse:**
$$
a^0 = 1_G, \qquad a^{n+1} = a \cdot a^n \ \text{pour } n \in \mathbb{N}, \qquad a^n = (a^{-n})^{-1} \ \text{pour } n < 0
$$

## 28. Formules de puissances
Donner les formules sur les puissances.
?
**Réponse:**
$\forall n, m \in \mathbb{Z},\ a^n a^m = a^{n+m}$ et $(a^n)^m = a^{nm}$.

## 29. Puissance d'un produit
Quand a-t-on $(ab)^n = a^n b^n$ ?
?
**Réponse:**
Lorsque $a$ et $b$ commutent ($ab = ba$).

## 30. Puissances d'éléments commutants
Si $a$ et $b$ commutent, que peut-on dire de $a^n$ et $b^k$ ?
?
**Réponse:**
Elles commutent entre elles pour tout $n, k \in \mathbb{Z}$.

## 31. Multiple additif
Que signifie $n \cdot a$ en notation additive ?
?
**Réponse:**
La somme de $n$ copies de $a$ :
$$
0 \cdot a = 0_G, \qquad (n+1) \cdot a = a + n \cdot a, \qquad n \cdot a = -((-n) \cdot a) \ \text{pour } n < 0
$$

## 32. Formules additives
Donner les formules additives.
?
**Réponse:**
$(n \cdot a) + (m \cdot a) = (n+m) \cdot a$ ; $m \cdot (n \cdot a) = (nm) \cdot a$ ; $n \cdot (a+b) = n \cdot a + n \cdot b$.

## 33. Groupe engendré par un élément
Qu'est-ce que le groupe engendré par un élément $a$ ?
?
**Réponse:**
$\mathrm{Gr}(a) = \{a^n / n \in \mathbb{Z}\}$ (ou $\{n \cdot a / n \in \mathbb{Z}\}$ en notation additive).

## 34. Sous-groupes de $(\mathbb{Z}, +)$
Quels sont les sous-groupes de $(\mathbb{Z}, +)$ ?
?
**Réponse:**
Les $n\mathbb{Z}$, pour $n \in \mathbb{N}$.

## 35. Ordre d'un élément
Qu'est-ce que l'ordre d'un élément $a$ ?
?
**Réponse:**
Le cardinal de $\mathrm{Gr}(a)$ (s'il est fini).

## 36. Groupe monogène
Qu'est-ce qu'un groupe monogène ?
?
**Réponse:**
Un groupe $(G, \cdot)$ pour lequel il existe $a \in G$ tel que $G = \mathrm{Gr}(a)$ ; $a$ est alors un générateur.

## 37. Monogène et abélien
Tout groupe monogène est-il abélien ?
?
**Réponse:**
Oui.

## 38. Groupe cyclique
Qu'est-ce qu'un groupe cyclique ?
?
**Réponse:**
Un groupe monogène et fini.

## 39. Propriétés d'un groupe cyclique
Quelles sont les 4 propriétés équivalentes pour $\mathrm{Gr}(a)$ cyclique de cardinal $n$ ?
?
**Réponse:**
1. $\mathrm{Gr}(a)$ est cyclique de cardinal $n$
2. $\{k \in \mathbb{N}^* / a^k = 1\}$ est non vide et son minimum vaut $n$
3. $\forall k \in \mathbb{Z},\ a^k = 1 \iff k \in n\mathbb{Z}$
4. Les éléments de $\mathrm{Gr}(a)$ sont exactement $1, a, \ldots, a^{n-1}$, deux à deux distincts
<!--SR:!2026-08-19,0,230-->

## 40. Puissances dans un groupe cyclique
Quand $\mathrm{Gr}(a)$ est cyclique d'ordre $n$, que valent les puissances de $a$ ?
?
**Réponse:**
Elles sont $1_G, a, \ldots, a^{n-1}$ puis $a^n = 1_G$ : le « cycle » se referme.

## 41. Exemple de groupe cyclique
Donner un exemple de groupe cyclique.
?
**Réponse:**
$U_n = \{e^{2i\pi k/n} / k \in \{0, \ldots, n-1\}\}$, les racines $n$-ièmes de l'unité dans $(\mathbb{C}^*, \times)$.

## 42. Morphisme de groupes
Qu'est-ce qu'un morphisme (homomorphisme) de groupes ?
?
**Réponse:**
Une application $f : (G, \Delta) \to (H, \nabla)$ telle que :
$$
\forall x, y \in G,\quad f(x \Delta y) = f(x) \nabla f(y)
$$

## 43. Isomorphisme, endomorphisme, automorphisme
Donner les définitions d'isomorphisme, endomorphisme, automorphisme.
?
**Réponse:**
Isomorphisme $=$ morphisme bijectif ; endomorphisme $=$ morphisme de $G$ dans lui-même ; automorphisme $=$ endomorphisme bijectif.

## 44. Image du neutre
Que vaut $f(1_G)$ pour un morphisme $f$ ?
?
**Réponse:**
$f(1_G) = 1_H$.

## 45. Image d'un inverse
Que vaut $f(x^{-1})$ pour un morphisme $f$ ?
?
**Réponse:**
$f(x^{-1}) = f(x)^{-1}$.

## 46. Image d'une puissance
Que vaut $f(a^n)$ pour un morphisme ?
?
**Réponse:**
$f(a^n) = f(a)^n$ pour tout $n \in \mathbb{Z}$.

## 47. Composition de morphismes
La composée de deux morphismes de groupes est-elle un morphisme ?
?
**Réponse:**
Oui.

## 48. Inverse d'un isomorphisme
Si $f$ est un isomorphisme, que dire de $f^{-1}$ ?
?
**Réponse:**
$f^{-1}$ est encore un isomorphisme.

## 49. Automorphismes
Qu'est-ce que $\mathrm{Aut}(G)$ ?
?
**Réponse:**
L'ensemble des automorphismes de $G$ ; c'est un sous-groupe de $S(G)$.

## 50. Image et préimage de sous-groupes
Que valent $f(G_0)$ et $f^{-1}(H_0)$ quand $G_0$ et $H_0$ sont des sous-groupes ?
?
**Réponse:**
$f(G_0)$ est un sous-groupe de $H$ et $f^{-1}(H_0)$ un sous-groupe de $G$.
<!--SR:!2026-08-19,0,230-->

## 51. Noyau et image
Définir le noyau et l'image d'un morphisme.
?
**Réponse:**
$\mathrm{Ker}(f) = f^{-1}(\{1_H\}) = \{x \in G / f(x) = 1_H\}$ ; $\mathrm{Im}(f) = f(G) = \{f(x) / x \in G\}$.

## 52. Injectivité d'un morphisme
Quand $f$ est-il injectif ?
?
**Réponse:**
$f$ est injective $\iff \mathrm{Ker}(f) = \{1_G\}$.

## 53. Monogène non cyclique
Un groupe monogène non cyclique est isomorphe à quoi ?
?
**Réponse:**
À $(\mathbb{Z}, +)$.

## 54. Cyclique d'ordre $n$
Un groupe cyclique d'ordre $n$ est isomorphe à quoi ?
?
**Réponse:**
À $\mathbb{Z}/n\mathbb{Z}$.

## 55. Le groupe symétrique $S_n$
Qu'est-ce que $S_n$ ?
?
**Réponse:**
Le groupe symétrique de degré $n$ : les bijections de $N_n = \{1, \ldots, n\}$ dans lui-même (les permutations).

## 56. Cycle et support
Qu'est-ce qu'un cycle de longueur $k$ et son support ?
?
**Réponse:**
Un cycle $(a_1\ a_2\ \ldots\ a_k)$ est la permutation $f$ telle que $f(a_i) = a_{i+1}$, $f(a_k) = a_1$, les autres éléments étant fixes. Sa longueur est $k$, son support $\{a_1, \ldots, a_k\}$.

## 57. Transposition
Qu'est-ce qu'une transposition ?
?
**Réponse:**
Un cycle de longueur 2.

## 58. Cycles à supports disjoints
Deux cycles à supports disjoints commutent-ils ?
?
**Réponse:**
Oui.

## 59. Décomposition en cycles
Quel est le théorème de décomposition en cycles ?
?
**Réponse:**
Toute permutation de $S_n$ se décompose de manière unique en un produit (commutatif) de cycles à supports deux à deux disjoints.

## 60. Produit de transpositions
Toute permutation est-elle produit de transpositions ? La décomposition est-elle unique ?
?
**Réponse:**
Oui, toute permutation est produit de transpositions, mais cette décomposition n'est pas unique.

## 61. Cycle en transpositions
Décomposer un cycle en transpositions.
?
**Réponse:**
$(a_1\ a_2\ \ldots\ a_k) = (a_1\ a_2) \circ (a_2\ a_3) \circ \cdots \circ (a_{k-1}\ a_k)$.

## 62. Signature d'une permutation
Qu'est-ce que la signature d'une permutation ?
?
**Réponse:**
$\varepsilon(\sigma) = (-1)^k$ où $\sigma$ est produit de $k$ transpositions : la parité de $k$ ne dépend que de $\sigma$. Signature $1$ $=$ paire, signature $-1$ $=$ impaire.

## 63. Propriété universelle de la signature
Quelle propriété universelle a la signature ?
?
**Réponse:**
C'est l'unique morphisme de $S_n$ dans $(\{-1, 1\}, \times)$ qui envoie toute transposition sur $-1$.

## 64. Signature d'un cycle
Quelle est la signature d'un cycle de longueur $k$ ?
?
**Réponse:**
$(-1)^{k+1}$.

## 65. Groupe alterné
Qu'est-ce que le groupe alterné $A_n$ ?
?
**Réponse:**
L'ensemble des permutations paires, c'est-à-dire $\mathrm{Ker}(\varepsilon)$ ; c'est un sous-groupe de $S_n$.

## 66. Cardinal de $A_n$
Que vaut $|A_n|$ pour $n \geq 2$ ?
?
**Réponse:**
$|A_n| = \dfrac{n!}{2}$.

## 67. Définition d'un anneau
Qu'est-ce qu'un anneau $(A, +, \cdot)$ ?
?
**Réponse:**
$(A, +)$ est un groupe commutatif, le produit est associatif, admet un élément neutre, et est distributif par rapport à l'addition :
$$
\forall x, y, z \in A,\quad x(y+z) = xy + xz \quad\text{et}\quad (y+z)x = yx + zx
$$

## 68. Anneau commutatif
Quand dit-on qu'un anneau est commutatif ?
?
**Réponse:**
Lorsque son produit est commutatif ($xy = yx$).

## 69. Exemples d'anneaux
Citer des exemples d'anneaux commutatifs et non commutatifs.
?
**Réponse:**
$(\mathbb{Z}, +, \cdot)$, $(\mathbb{Q}, +, \cdot)$, $(\mathbb{R}, +, \cdot)$, $(\mathbb{C}, +, \cdot)$ sont commutatifs ; $(M_n(\mathbb{R}), +, \times)$ est non commutatif pour $n \geq 2$.

## 70. Anneau de Boole
Qu'est-ce que l'anneau de Boole ?
?
**Réponse:**
$(\mathcal{P}(E), \Delta, \cap)$ est un anneau.

## 71. Produit par zéro
Que vaut $0 \cdot x$ et $x \cdot 0$ dans un anneau ?
?
**Réponse:**
$0 \cdot x = x \cdot 0 = 0$.

## 72. Produit par $-1_A$
Que vaut $(-1_A) \cdot x$ ?
?
**Réponse:**
$(-1_A) \cdot x = -x$.

## 73. Neutre et zéro
Que peut-on dire de $1_A$ si $A$ a au moins deux éléments ?
?
**Réponse:**
$1_A \neq 0_A$.

## 74. Distributivité généralisée
Donner la formule de distributivité généralisée.
?
**Réponse:**
$\left( \sum_{i=1}^{n} a_i \right) \left( \sum_{j=1}^{p} b_j \right) = \sum_{1 \leq i \leq n,\ 1 \leq j \leq p} a_i \cdot b_j$.

## 75. Élément inversible
Qu'est-ce qu'un élément inversible d'un anneau ?
?
**Réponse:**
Un élément $a$ qui admet un symétrique (inverse) pour la loi $\cdot$.

## 76. Élément nilpotent
Qu'est-ce qu'un élément nilpotent ?
?
**Réponse:**
$a \in A \setminus \{0\}$ tel qu'il existe $n \geq 2$ avec $a^n = 0$.

## 77. Formules de puissances dans un anneau
Quelles formules de puissances sont valables ?
?
**Réponse:**
$$
a^n a^m = a^{n+m} \quad\text{et}\quad (a^n)^m = a^{nm}
$$
valables pour $n, m \in \mathbb{N}$ si $a$ quelconque, et pour $n, m \in \mathbb{Z}$ si $a$ inversible.

## 78. Puissance d'un produit dans un anneau
Quand a-t-on $(ab)^n = a^n b^n$ dans un anneau ?
?
**Réponse:**
Quand $a$ et $b$ commutent ($ab = ba$).

## 79. Sous-anneau
Qu'est-ce qu'un sous-anneau $B$ de $A$ ?
?
**Réponse:**
$B$ muni des restrictions de $+$ et $\cdot$ est un anneau avec les mêmes éléments neutres que $A$.

## 80. Caractérisation d'un sous-anneau
Caractériser un sous-anneau.
?
**Réponse:**
$B$ est un sous-anneau de $A$ ssi :
$$
1_A \in B, \qquad \forall x, y \in B,\ x - y \in B, \qquad \forall x, y \in B,\ xy \in B
$$

## 81. $\{0_A\}$ comme sous-anneau
$\{0_A\}$ est-il un sous-anneau de $A$ (si $A \neq \{0_A\}$) ?
?
**Réponse:**
Non : c'est un anneau mais pas un sous-anneau, car $1_A \notin \{0_A\}$.

## 82. Plus petit sous-anneau
Quel est le plus petit sous-anneau de $A$ ?
?
**Réponse:**
$\mathbb{Z} \cdot 1_A = \{n \cdot 1_A / n \in \mathbb{Z}\}$.

## 83. Sous-anneaux de $\mathbb{Z}$
Combien de sous-anneaux possède $\mathbb{Z}$ ?
?
**Réponse:**
Un seul : lui-même.

## 84. Groupe des inversibles
Qu'est-ce que le groupe des inversibles $A^*$ (ou $U(A)$) ?
?
**Réponse:**
L'ensemble des éléments inversibles de $A$ muni de la loi $\cdot$ ; c'est un groupe.

## 85. Définition d'un corps
Qu'est-ce qu'un corps ?
?
**Réponse:**
Un anneau $A$ tel que :
$$
A \neq \{0_A\}, \qquad A \ \text{commutatif}, \qquad \forall a \in A \setminus \{0\},\ a \ \text{inversible}
$$

## 86. Corps gauche
Qu'est-ce qu'un corps gauche ?
?
**Réponse:**
Un anneau non nul dans lequel tout élément non nul est inversible, sans exiger la commutativité.

## 87. Sous-corps
Qu'est-ce qu'un sous-corps de $K$ ?
?
**Réponse:**
$L \subset K$ tel que $L$ muni des lois restreintes est un corps avec les mêmes éléments neutres que $K$.

## 88. Caractérisation d'un sous-corps
Caractériser un sous-corps.
?
**Réponse:**
$B$ est un sous-corps de $K$ ssi $B$ est un sous-anneau de $K$ et $\forall x \in B \setminus \{0\},\ x^{-1} \in B$.

## 89. Exemple de sous-corps
Citer un exemple de sous-corps de $\mathbb{R}$.
?
**Réponse:**
$\mathbb{Q} + \sqrt{2}\,\mathbb{Q} = \{\alpha + \sqrt{2}\,\beta / (\alpha, \beta) \in \mathbb{Q}^2\}$.

## 90. Binôme de Newton
Donner la formule du binôme de Newton (anneau).
?
**Réponse:**
Si $ab = ba$ :
$$
(a+b)^n = \sum_{k=0}^{n} \binom{n}{k}\, a^k b^{n-k}
$$

## 91. Formule de Bernoulli
Donner la formule de Bernoulli.
?
**Réponse:**
Si $ab = ba$ :
$$
a^{n+1} - b^{n+1} = (a - b) \sum_{k=0}^{n} a^k b^{n-k}
$$

## 92. Sommes partielles d'une série géométrique
Donner la formule des sommes partielles d'une série géométrique.
?
**Réponse:**
$$
(1_A - x) \sum_{i=m}^{n} x^i = x^m - x^{n+1}
$$

## 93. Diviseur de zéro
Qu'est-ce qu'un diviseur de zéro ?
?
**Réponse:**
$a \neq 0$ est un diviseur de zéro (à gauche) s'il existe $b \neq 0$ tel que $ab = 0$ (resp. $ba = 0$ à droite).

## 94. Anneau intègre
Quand dit-on qu'un anneau est intègre ?
?
**Réponse:**
Non réduit à $\{0_A\}$ et sans diviseur de zéro (ni à gauche ni à droite).

## 95. Régularité et diviseur de zéro
Quand un élément non nul est-il régulier ?
?
**Réponse:**
$a$ est régulier $\iff$ $a$ n'est pas un diviseur de zéro.

## 96. Corps et anneaux intègres
Tout corps est-il intègre ? La réciproque ?
?
**Réponse:**
Oui, tout corps est intègre. La réciproque est fausse (ex : $K[X]$ est intègre mais pas un corps).

## 97. Intégrité de $\mathcal{F}(\mathbb{R}, \mathbb{R})$
$\mathcal{F}(\mathbb{R}, \mathbb{R})$ est-il intègre ?
?
**Réponse:**
Non, c'est un anneau non intègre.

## 98. Morphisme d'anneaux
Qu'est-ce qu'un morphisme d'anneaux ?
?
**Réponse:**
$f : A \to B$ telle que :
$$
f(1_A) = 1_B, \qquad f(x + y) = f(x) + f(y), \qquad f(x \cdot y) = f(x) \cdot f(y)
$$

## 99. Morphisme de corps
Qu'est-ce qu'un morphisme de corps ?
?
**Réponse:**
Un morphisme d'anneaux entre deux corps.
<!--SR:!2026-08-19,0,230-->

## 100. Propriété remarquable des morphismes de corps
Quelle propriété remarquable a un morphisme de corps ?
?
**Réponse:**
Il est toujours injectif.

## 101. Image d'une puissance (anneaux)
Que vaut $f(a^n)$ pour un morphisme d'anneaux ?
?
**Réponse:**
$f(a^n) = f(a)^n$ ; et si $a$ inversible, $f(a^{-1}) = f(a)^{-1}$.

## 102. Noyau d'un morphisme d'anneaux
Que peut-on dire de $\mathrm{Ker}(f)$ pour un morphisme d'anneaux ?
?
**Réponse:**
$\mathrm{Ker}(f) = f^{-1}(\{0\})$ est un idéal de $A$, et $\mathrm{Im}(f)$ est un sous-anneau de $B$.

## 103. Loi de l'anneau produit
Quelle est la loi de l'anneau produit ?
?
**Réponse:**
Composante par composante :
$$
(x_1, \ldots, x_n) + (y_1, \ldots, y_n) = (x_1 + y_1, \ldots, x_n + y_n)
$$
$$
(x_1, \ldots, x_n) \cdot (y_1, \ldots, y_n) = (x_1 y_1, \ldots, x_n y_n)
$$

## 104. Définition d'un idéal
Qu'est-ce qu'un idéal (bilatère) d'un anneau commutatif ?
?
**Réponse:**
$I \neq \emptyset$, stable pour $+$, et superstable pour le produit :
$$
\forall x, y \in I,\ x + y \in I, \qquad \forall a \in A,\ \forall x \in I,\ a \cdot x \in I
$$
($I$ est « absorbant » pour le produit)

## 105. Idéal comme groupe
Tout idéal est-il un groupe pour $+$ ?
?
**Réponse:**
Oui.

## 106. Idéal contenant $1$
Quand a-t-on $1 \in I$ pour un idéal $I$ ?
?
**Réponse:**
$1 \in I \iff I = A$.

## 107. Intersection d'idéaux
L'intersection d'idéaux est-elle un idéal ?
?
**Réponse:**
Oui.

## 108. Idéal engendré par une partie
Qu'est-ce que l'idéal engendré par $B$, noté $\mathrm{Id}(B)$ ?
?
**Réponse:**
L'intersection de tous les idéaux contenant $B$ ; c'est le plus petit idéal contenant $B$.

## 109. Écriture de $\mathrm{Id}(B)$
Comment s'écrit $\mathrm{Id}(B)$ ?
?
**Réponse:**
$$
\mathrm{Id}(B) = \left\{ \sum_{i=1}^{n} a_i b_i \ \middle|\ n \in \mathbb{N},\ a_i \in A,\ b_i \in B \right\}
$$

## 110. Idéal engendré par $\emptyset$
Que vaut $\mathrm{Id}(\emptyset)$ ?
?
**Réponse:**
$\mathrm{Id}(\emptyset) = \{0\}$.

## 111. Idéal engendré par un élément
Que vaut $\mathrm{Id}(b)$ pour $b \in A$ ?
?
**Réponse:**
$\mathrm{Id}(b) = Ab = \{ab / a \in A\}$ : l'ensemble des multiples de $b$ (idéal principal).

## 112. Anneau principal
Qu'est-ce qu'un anneau principal ?
?
**Réponse:**
Un anneau commutatif intègre dont tous les idéaux sont principaux.

## 113. $\mathbb{Z}$ principal
$\mathbb{Z}$ est-il un anneau principal ?
?
**Réponse:**
Oui.

## 114. Préimage d'un idéal
Si $f : A \to B$ est un morphisme d'anneaux, que peut-on dire de $f^{-1}(I)$ pour $I$ idéal de $B$ ?
?
**Réponse:**
$f^{-1}(I)$ est un idéal de $A$ contenant $\mathrm{Ker}(f)$.

## 115. Groupe quotient
Qu'est-ce que le groupe quotient $G/H$ ?
?
**Réponse:**
$$
G/H = \{ \overline{x} = xH / x \in G \}
$$
l'ensemble des classes d'équivalence pour la relation $x\, \mathcal{R}_H\, y \iff x^{-1}y \in H$.

## 116. Quotient de groupe abélien
Quand $G/H$ est-il un groupe ?
?
**Réponse:**
Si $G$ est abélien, $G/H$ est un groupe pour $\overline{x} + \overline{y} = \overline{x + y}$.

## 117. Surjection canonique
Qu'est-ce que la surjection canonique ?
?
**Réponse:**
$\pi : G \to G/H$, $x \mapsto \overline{x}$ ; c'est un morphisme surjectif de groupes.

## 118. Égalité dans $\mathbb{Z}/n\mathbb{Z}$
Dans $\mathbb{Z}/n\mathbb{Z}$, à quoi est équivalent $\overline{x} = \overline{y}$ ?
?
**Réponse:**
$\overline{x} = \overline{y} \iff x \equiv y \ [n]$.

## 119. $\mathbb{Z}/0\mathbb{Z}$
Si $n = 0$, qu'est-ce que $\mathbb{Z}/n\mathbb{Z}$ ?
?
**Réponse:**
$\mathbb{Z}/0\mathbb{Z}$ est monogène non cyclique, isomorphe à $\mathbb{Z}$.

## 120. Cardinal de $\mathbb{Z}/n\mathbb{Z}$
Si $n \geq 1$, que vaut $\mathbb{Z}/n\mathbb{Z}$ ?
?
**Réponse:**
$\mathbb{Z}/n\mathbb{Z}$ est un groupe cyclique de cardinal $n$, et $\mathbb{Z}/n\mathbb{Z} = \{\overline{0}, \overline{1}, \ldots, \overline{n-1}\}$.

## 121. Cyclique isomorphe
Tout groupe cyclique de cardinal $n$ est isomorphe à quoi ?
?
**Réponse:**
À $\mathbb{Z}/n\mathbb{Z}$ (via $\overline{k} \mapsto a^k$ si $a$ engendre le groupe).

## 122. Générateurs de $(\mathbb{Z}/n\mathbb{Z}, +)$
Quand $\overline{k}$ engendre-t-il $(\mathbb{Z}/n\mathbb{Z}, +)$ ?
?
**Réponse:**
$\overline{k}$ engendre $(\mathbb{Z}/n\mathbb{Z}, +) \iff k$ et $n$ sont premiers entre eux.

## 123. Inversibles de $\mathbb{Z}/n\mathbb{Z}$
Quand $\overline{k}$ est-il inversible dans $\mathbb{Z}/n\mathbb{Z}$ ?
?
**Réponse:**
$\overline{k}$ est inversible dans $(\mathbb{Z}/n\mathbb{Z}, \cdot) \iff k$ et $n$ sont premiers entre eux.

## 124. Générateurs et inversibles
Quels sont les générateurs de $(\mathbb{Z}/n\mathbb{Z}, +)$ ?
?
**Réponse:**
Exactement les inversibles de l'anneau $(\mathbb{Z}/n\mathbb{Z}, +, \cdot)$.

## 125. Inverse dans $\mathbb{Z}/n\mathbb{Z}$
Comment calculer l'inverse de $k$ dans $\mathbb{Z}/n\mathbb{Z}$ ?
?
**Réponse:**
Grâce à l'algorithme d'Euclide : trouver $u, v \in \mathbb{Z}$ tels que $uk + vn = 1$ (identité de Bézout) ; alors $k^{-1} = \overline{u}$.

## 126. $\mathbb{Z}/n\mathbb{Z}$ corps
Quand $\mathbb{Z}/n\mathbb{Z}$ est-il un corps ?
?
**Réponse:**
$$
\mathbb{Z}/n\mathbb{Z} \ \text{corps} \iff \mathbb{Z}/n\mathbb{Z} \ \text{intègre} \iff n \ \text{premier}
$$

## 127. Notation $\mathbb{F}_p$
Quelle notation pour $\mathbb{Z}/p\mathbb{Z}$ avec $p$ premier ?
?
**Réponse:**
$\mathbb{F}_p$ (field).

## 128. Théorème des restes chinois
Énoncer le théorème des restes chinois.
?
**Réponse:**
Si $a$ et $b \geq 2$ sont premiers entre eux, l'application $f : \mathbb{Z}/ab\mathbb{Z} \to \mathbb{Z}/a\mathbb{Z} \times \mathbb{Z}/b\mathbb{Z}$, $\overline{k} \mapsto (\overline{k}, \overline{k})$ est un isomorphisme d'anneaux.

## 129. Version constructive du théorème chinois
Donner la version constructive du théorème chinois.
?
**Réponse:**
Si $ua + vb = 1$ (Bézout), alors $\ell = kua + hvb$ vérifie $\ell \equiv h\ [a]$ et $\ell \equiv k\ [b]$.

## 130. Indicatrice d'Euler
Qu'est-ce que l'indicatrice d'Euler $\varphi(n)$ ?
?
**Réponse:**
Le nombre d'éléments inversibles de $\mathbb{Z}/n\mathbb{Z}$. Pour $n \geq 2$ : $\varphi(n) = \#\{k \in \{1, \ldots, n-1\} / k \wedge n = 1\}$.

## 131. $\varphi(p)$
Que vaut $\varphi(p)$ si $p$ est premier ?
?
**Réponse:**
$\varphi(p) = p - 1$.

## 132. $\varphi(p^k)$
Que vaut $\varphi(p^k)$ si $p$ est premier ?
?
**Réponse:**
$\varphi(p^k) = p^k - p^{k-1}$.

## 133. Multiplicativité de $\varphi$
Si $a \wedge b = 1$, que vaut $\varphi(ab)$ ?
?
**Réponse:**
$\varphi(ab) = \varphi(a) \cdot \varphi(b)$ (multiplicativité).

## 134. Formule générale de $\varphi(n)$
Donner la formule générale de $\varphi(n)$.
?
**Réponse:**
Si $n = \prod_{i} p_i^{m_i}$, alors :
$$
\varphi(n) = n \prod_{i} \left( 1 - \frac{1}{p_i} \right)
$$

## 135. Théorème d'Euler-Fermat
Énoncer le théorème d'Euler-Fermat.
?
**Réponse:**
Si $k \wedge n = 1$, alors $k^{\varphi(n)} \equiv 1\ [n]$.

## 136. Petit théorème de Fermat
Énoncer le petit théorème de Fermat.
?
**Réponse:**
Si $p$ est premier, alors $\forall k \in \mathbb{Z},\ k^p \equiv k\ [p]$.

## 137. Théorème RSA
Énoncer le théorème RSA.
?
**Réponse:**
$p, q$ premiers distincts, $n = pq$, $e \wedge \varphi(n) = 1$, $ed \equiv 1\ [\varphi(n)]$ :
$$
\forall M \in \mathbb{Z},\quad M^{ed} \equiv M\ [n]
$$

## 138. Caractéristique d'un anneau
Définir la caractéristique d'un anneau.
?
**Réponse:**
$$
\mathrm{car}(A) = \begin{cases} \min\{n \in \mathbb{N}^* / n \cdot 1_A = 0\} & \text{si cela existe} \\ 0 & \text{sinon} \end{cases}
$$

## 139. Caractéristique d'un anneau intègre
Que peut-on dire de la caractéristique d'un anneau intègre non nul ?
?
**Réponse:**
Si $\mathrm{car}(A) \neq 0$, alors $\mathrm{car}(A)$ est premier.

## 140. Endomorphisme de Frobenius
Qu'est-ce que l'endomorphisme de Frobenius ?
?
**Réponse:**
Si $\mathrm{car}(A) = p$ premier, l'application $x \mapsto x^p$ est un endomorphisme d'anneau (car tous les $\binom{p}{k}$ sont divisibles par $p$ pour $1 \leq k \leq p-1$).

## 141. Caractéristique d'un corps
Quelle est la caractéristique d'un corps ?
?
**Réponse:**
Ou bien $0$, ou bien un nombre premier.

## 142. Sous-corps premier
Quel est le sous-corps premier d'un corps ?
?
**Réponse:**
Si $\mathrm{car}(K) = p$ : $\mathbb{Z}/p\mathbb{Z}$. Si $\mathrm{car}(K) = 0$ : il est isomorphe à $\mathbb{Q}$.
