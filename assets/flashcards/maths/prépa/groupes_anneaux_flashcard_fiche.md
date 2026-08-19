#flashcards/maths/prépa/groupes_anneaux/fiche

## 1. Définition d'un groupe
Définir un groupe.
?
**Réponse:**
$(G, \cdot)$ est un groupe ssi :
$$
\begin{cases}
\forall x, y, z \in G,\ (xy)z = x(yz) & \text{associativité} \\
\forall x \in G,\ \exists 1_G \in G,\ 1_G \cdot x = x \cdot 1_G = x & \text{neutre} \\
\forall x \in G,\ \exists x^{-1} \in G,\ x \cdot x^{-1} = x^{-1} \cdot x = 1_G & \text{symétrique}
\end{cases}
$$

## 2. Groupe abélien
Qu'est-ce qu'un groupe abélien ?
?
**Réponse:**
Un groupe dont la loi est commutative. Si abélien, on note la loi $+$, le neutre $0_G$, le symétrique $-x$.

## 3. Formules de calcul dans un groupe
Donner les formules de calcul dans un groupe.
?
**Réponse:**
$(x^{-1})^{-1} = x$ ; $(xy)^{-1} = y^{-1}x^{-1}$ ; en notation additive : $x - (y + z) = x - y - z$.

## 4. Caractérisation d'un sous-groupe
Caractériser un sous-groupe.
?
**Réponse:**
$H$ est un sous-groupe de $G$ ssi :
$$
\begin{cases}
H \neq \emptyset \\
\forall x, y \in H,\ xy^{-1} \in H
\end{cases}
$$

## 5. Propriétés des sous-groupes
Rappeler les propriétés des sous-groupes.
?
**Réponse:**
$\{1_G\}$ et $G$ sont des sous-groupes ; l'intersection de sous-groupes est un sous-groupe ; un sous-groupe d'un sous-groupe de $G$ est un sous-groupe de $G$.

## 6. Groupe engendré par une partie
Qu'est-ce que le groupe engendré par $A$ ?
?
**Réponse:**
Le plus petit sous-groupe contenant $A$ :
$$
\mathrm{Gr}(A) = \bigcap_{A \subset H,\ H \subset G} H
$$

## 7. Formules de puissances
Donner les formules de puissances.
?
**Réponse:**
$a^0 = 1_G$ ; $a^{n+m} = a^n a^m$ ; $(a^n)^m = a^{nm}$ ; $(ab)^n = a^n b^n$ si $ab = ba$ ; $(a^n)^{-1} = a^{-n}$.

## 8. Ordre d'un élément et d'un groupe
Définir l'ordre d'un élément et l'ordre d'un groupe.
?
**Réponse:**
Ordre d'un groupe $=$ son cardinal. Ordre d'un élément $a$ $=$ l'ordre du sous-groupe $\mathrm{Gr}(a)$.

## 9. Groupe monogène et cyclique
Qu'est-ce qu'un groupe monogène ? cyclique ?
?
**Réponse:**
Monogène : engendré par un seul élément (il est alors abélien). Cyclique : monogène et fini.

## 10. Sous-groupes de $(\mathbb{Z}, +)$
Quels sont les sous-groupes de $(\mathbb{Z}, +)$ ?
?
**Réponse:**
Les $n\mathbb{Z}$, $n \in \mathbb{N}$.

## 11. Morphisme de groupes
Qu'est-ce qu'un morphisme de groupes ?
?
**Réponse:**
$f : G \to H$ avec $\forall x, y,\ f(xy) = f(x) f(y)$.

## 12. Propriétés d'un morphisme
Donner les propriétés élémentaires d'un morphisme.
?
**Réponse:**
$f(1_G) = 1_H$ ; $f(x^{-1}) = f(x)^{-1}$ ; $f(a^n) = f(a)^n$ ; la composée de deux morphismes est un morphisme ; $f^{-1}$ est un isomorphisme si $f$ en est un.

## 13. Noyau et image
Définir noyau et image d'un morphisme.
?
**Réponse:**
$\mathrm{Ker}(f) = f^{-1}(\{1_H\})$ ; $\mathrm{Im}(f) = f(G)$. Les deux sont des sous-groupes (de $G$ et $H$).

## 14. Injectivité d'un morphisme
Caractère injectif du morphisme.
?
**Réponse:**
$f$ injective $\iff \mathrm{Ker}(f) = \{1_G\}$.

## 15. Isomorphisme des groupes monogènes
Quel est le théorème d'isomorphisme pour les groupes monogènes ?
?
**Réponse:**
$$
\begin{cases}
\text{monogène non cyclique} \ \cong \ (\mathbb{Z}, +) \\
\text{cyclique d'ordre } n \ \cong \ (\mathbb{Z}/n\mathbb{Z}, +)
\end{cases}
$$

## 16. Groupe produit
Qu'est-ce que le groupe produit ?
?
**Réponse:**
$G = G_1 \times \cdots \times G_n$ avec loi $(x_1, \ldots, x_n)(y_1, \ldots, y_n) = (x_1 y_1, \ldots, x_n y_n)$. Abélien ssi chaque $G_i$ est abélien.

## 17. Permutation, cycle, transposition
Définir une permutation, un cycle, une transposition.
?
**Réponse:**
$S_n$ : bijections de $\{1, \ldots, n\}$. Cycle de longueur $k$ : fixe le complémentaire d'un support de cardinal $k$ et « tourne » dessus. Transposition : cycle de longueur 2.

## 18. Décomposition en cycles
Énoncer la décomposition en cycles.
?
**Réponse:**
Toute permutation est produit unique (à l'ordre près) de cycles à supports disjoints ; c'est aussi un produit de transpositions (non unique).

## 19. Cycle en transpositions
Décomposer un cycle en transpositions.
?
**Réponse:**
$(a_1 \ldots a_k) = (a_1\, a_2)(a_2\, a_3) \cdots (a_{k-1}\, a_k)$.

## 20. Signature
Définir la signature.
?
**Réponse:**
$\varepsilon(\sigma) = (-1)^k$ où $k$ est le nombre de transpositions d'une décomposition de $\sigma$ (la parité est bien définie). Unique morphisme $S_n \to \{ \pm 1 \}$ envoyant une transposition sur $-1$.

## 21. Propriétés de la signature
Donner les propriétés de la signature.
?
**Réponse:**
$\varepsilon(\sigma \circ \tau) = \varepsilon(\sigma)\varepsilon(\tau)$ ; signature d'un cycle de longueur $k$ : $(-1)^{k+1}$.

## 22. Groupe alterné
Qu'est-ce que le groupe alterné $A_n$ ?
?
**Réponse:**
$\mathrm{Ker}(\varepsilon)$ : permutations paires. $|A_n| = n!/2$ pour $n \geq 2$.

## 23. Définition d'un anneau
Définir un anneau.
?
**Réponse:**
$(A, +, \cdot)$ avec :
$$
\begin{cases}
(A, +) \ \text{groupe abélien} \\
\text{produit associatif à neutre } 1_A \\
\text{distributivité } :\ x(y+z) = xy + xz,\ (y+z)x = yx + zx
\end{cases}
$$

## 24. Formules de calcul dans un anneau
Donner les formules de calcul dans un anneau.
?
**Réponse:**
$0 \cdot x = 0$ ; $(-1_A)x = -x$ ; distributivité généralisée sur les sommes finies.

## 25. Élément nilpotent
Qu'est-ce qu'un élément nilpotent ?
?
**Réponse:**
$a \neq 0$ tel que $a^n = 0$ pour un $n \geq 2$.

## 26. Caractérisation d'un sous-anneau
Caractériser un sous-anneau.
?
**Réponse:**
$B$ sous-anneau de $A$ ssi :
$$
1_A \in B, \qquad \forall x, y \in B,\ x - y \in B \ \text{et}\ xy \in B
$$
$\{0_A\}$ n'est pas un sous-anneau de $A$ ; $\mathbb{Z} \cdot 1_A$ est le plus petit.

## 27. Définition d'un corps
Qu'est-ce qu'un corps ?
?
**Réponse:**
Anneau non nul, commutatif, dont tout élément non nul est inversible.

## 28. Caractérisation d'un sous-corps
Caractériser un sous-corps.
?
**Réponse:**
$L$ est un sous-corps de $K$ ssi $L$ est un sous-anneau de $K$ et $\forall x \in L \setminus \{0\},\ x^{-1} \in L$.

## 29. Formules du cours
Donner les formules : binôme de Newton, Bernoulli, série géométrique.
?
**Réponse:**
Si $ab = ba$ :
$$
(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}
$$
$$
a^{n+1} - b^{n+1} = (a-b) \sum_{k=0}^{n} a^k b^{n-k}
$$
$$
(1_A - x) \sum_{i=m}^{n} x^i = x^m - x^{n+1}
$$

## 30. Diviseur de zéro et anneau intègre
Qu'est-ce qu'un diviseur de zéro ? un anneau intègre ?
?
**Réponse:**
$a \neq 0$ diviseur de zéro ssi $\exists b \neq 0,\ ab = 0$. Anneau intègre : non nul et sans diviseur de zéro.

## 31. Régularité et diviseur de zéro
Lien entre régularité et diviseur de zéro.
?
**Réponse:**
$a$ est régulier $\iff a$ n'est pas un diviseur de zéro.

## 32. Intègre et corps
Un anneau intègre est-il un corps ?
?
**Réponse:**
Non en général ($K[X]$ est intègre, pas un corps) ; mais tout corps est intègre.

## 33. Morphisme d'anneaux
Qu'est-ce qu'un morphisme d'anneaux ?
?
**Réponse:**
$f(1_A) = 1_B$ et $\forall x, y,\ f(x+y) = f(x) + f(y),\ f(xy) = f(x)f(y)$.

## 34. Morphismes de corps
Quelle propriété ont les morphismes de corps ?
?
**Réponse:**
Ils sont injectifs.

## 35. Définition d'un idéal
Définir un idéal.
?
**Réponse:**
$I$ idéal de l'anneau commutatif $A$ ssi :
$$
I \neq \emptyset, \qquad \forall x, y \in I,\ x + y \in I, \qquad \forall a \in A,\ \forall x \in I,\ a \cdot x \in I
$$

## 36. Propriétés des idéaux
Donner les propriétés des idéaux.
?
**Réponse:**
$1_A \in I \iff I = A$ ; l'intersection d'idéaux est un idéal ; $\mathrm{Ker}(f)$ est un idéal, $\mathrm{Im}(f)$ un sous-anneau.

## 37. Idéal engendré, principal, anneau principal
Qu'est-ce qu'un idéal engendré / principal / un anneau principal ?
?
**Réponse:**
$\mathrm{Id}(B)$ $=$ plus petit idéal contenant $B$. $\mathrm{Id}(b) = Ab$ : idéal principal. Anneau principal : intègre dont tout idéal est principal ($\mathbb{Z}$, $K[X]$).

## 38. Groupe quotient
Qu'est-ce que le groupe quotient $G/H$ ?
?
**Réponse:**
$G/H$ $=$ classes $\overline{x} = xH$ ; $G/H$ est un groupe si $G$ est abélien ; $\pi : x \mapsto \overline{x}$ est un morphisme surjectif.

## 39. $\mathbb{Z}/n\mathbb{Z}$
Dans $\mathbb{Z}/n\mathbb{Z}$ :
?
**Réponse:**
$\overline{x} = \overline{y} \iff x \equiv y\ [n]$ ; cardinal $n$ si $n \geq 1$ ; $\mathbb{Z}/0\mathbb{Z} \cong \mathbb{Z}$.

## 40. Générateurs et inversibles
Quand $\overline{k}$ est-il générateur ou inversible ?
?
**Réponse:**
$\overline{k}$ engendre $(\mathbb{Z}/n\mathbb{Z}, +) \iff \overline{k}$ inversible $\iff k \wedge n = 1$.

## 41. $\mathbb{Z}/n\mathbb{Z}$ corps
Quand $\mathbb{Z}/n\mathbb{Z}$ est-il un corps ?
?
**Réponse:**
$\mathbb{Z}/n\mathbb{Z}$ corps $\iff \mathbb{Z}/n\mathbb{Z}$ intègre $\iff n$ premier (alors noté $\mathbb{F}_p$).

## 42. Théorème des restes chinois
Énoncer le théorème des restes chinois.
?
**Réponse:**
Si $a \wedge b = 1$ : $\mathbb{Z}/ab\mathbb{Z} \cong \mathbb{Z}/a\mathbb{Z} \times \mathbb{Z}/b\mathbb{Z}$. Construction : $\ell = kua + hvb$ avec $ua + vb = 1$.

## 43. Indicatrice d'Euler
Définir $\varphi(n)$ et donner ses propriétés.
?
**Réponse:**
$\varphi(n) = \#\{k \in \{1, \ldots, n-1\} / k \wedge n = 1\}$ :
$$
\varphi(p) = p - 1, \quad \varphi(p^k) = p^k - p^{k-1}, \quad \varphi(ab) = \varphi(a)\varphi(b)
$$
$$
\varphi\left(\prod p_i^{m_i}\right) = n \prod \left(1 - \frac{1}{p_i}\right)
$$

## 44. Euler-Fermat et petit Fermat
Énoncer le théorème d'Euler-Fermat et le petit Fermat.
?
**Réponse:**
$$
k^{\varphi(n)} \equiv 1\ [n] \quad (k \wedge n = 1)
$$
$$
k^p \equiv k\ [p] \quad (p \text{ premier})
$$

## 45. Théorème RSA
Énoncer le théorème RSA.
?
**Réponse:**
$n = pq$, $ed \equiv 1\ [\varphi(n)]$ : alors $M^{ed} \equiv M\ [n]$ pour tout $M$.
