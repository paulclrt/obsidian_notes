#flashcards/maths/prépa/ev/fiche

## 1. Définition d'un K-espace vectoriel
Rappeler la définition d'un K-espace vectoriel.
?
**Réponse:**
$(E, +, \cdot)$ avec $(E, +)$ groupe abélien et $\cdot : K \times E \to E$ vérifiant, pour tout $x, y \in E$, $\alpha, \beta \in K$ :
$$
\alpha(x+y) = \alpha x + \alpha y, \quad (\alpha + \beta) x = \alpha x + \beta x, \quad (\alpha \beta) x = \alpha (\beta x), \quad 1_K x = x.
$$

## 2. Règles de calcul essentielles
Donner les règles de calcul fondamentales dans un K-espace vectoriel.
?
**Réponse:**
$$
0_K \cdot x = 0_E, \quad \lambda \cdot 0_E = 0_E, \quad (-1_K) \cdot x = -x, \quad (\lambda - \mu)x = \lambda x - \mu x,
$$
$$
\lambda x = 0 \iff \lambda = 0 \text{ ou } x = 0, \quad (\lambda x = \lambda y \text{ et } \lambda \neq 0) \implies x = y.
$$

## 3. Caractérisation d'un sous-espace vectoriel
Quand une partie F de E est-elle un sous-espace vectoriel ?
?
**Réponse:**
$F \neq \emptyset$, stable par somme et produit par un scalaire, ce qui équivaut à la condition unique :
$$
F \neq \emptyset \quad \text{et} \quad \forall (\alpha, x, y) \in K \times F \times F, \ \alpha x + y \in F.
$$

## 4. Sous-espaces et vecteur nul
Que contient tout sous-espace vectoriel ?
?
**Réponse:**
Tout sous-espace vectoriel contient $0_E$ : $\{0_E\}$ est le plus petit sous-espace vectoriel, $E$ le plus grand. Pour montrer $F = \{0\}$, il suffit de montrer $F \subset \{0\}$.

## 5. Intersection et somme de sous-espaces
L'intersection et la somme de sous-espaces sont-elles des sous-espaces ?
?
**Réponse:**
Oui, toutes deux :
$$
\bigcap_{i \in I} F_i \text{ est un sous-espace,} \qquad F_1 + \cdots + F_p = \operatorname{Vect}\left( \bigcup_{i=1}^p F_i \right).
$$
En revanche la réunion de sous-espaces n'est pas un sous-espace en général.

## 6. Vect(A) : définition et description
Définir Vect(A) et le décrire.
?
**Réponse:**
$\operatorname{Vect}(A)$ est le plus petit sous-espace vectoriel contenant $A$ :
$$
\operatorname{Vect}(A) = \bigcap_{F \text{ sev contenant } A} F = \left\{ \sum_{a \in A} \alpha_a a \ \Big| \ (\alpha_a)_{a \in A} \in K^{(A)} \right\}.
$$
Si $A = \{x_1, \ldots, x_n\}$ : $\operatorname{Vect}(A) = \{\sum_{i=1}^n \alpha_i x_i / \alpha_i \in K\}$.

## 7. Opérations qui conservent Vect
Quelles opérations sur la famille ne changent pas le Vect engendré ?
?
**Réponse:**
Multiplier un vecteur par un scalaire non nul, ou lui ajouter une combinaison linéaire des autres vecteurs. Si $x \in \operatorname{Vect}(A)$ alors $\operatorname{Vect}(A \cup \{x\}) = \operatorname{Vect}(A)$.

## 8. Monotonie de Vect
Que dire de Vect(A) et Vect(B) si $A \subset B$ ?
?
**Réponse:**
Si $A \subset B$, alors $\operatorname{Vect}(A) \subset \operatorname{Vect}(B)$.

## 9. Définition d'application linéaire
Définir une application linéaire.
?
**Réponse:**
$f : E \to F$ linéaire ssi
$$
\forall (\alpha, x, y) \in K \times E \times E, \quad f(\alpha x + y) = \alpha f(x) + f(y),
$$
ce qui équivaut à $f(x+y) = f(x)+f(y)$ et $f(\alpha x) = \alpha f(x)$.

## 10. Vocabulaire des morphismes
Définir isomorphisme, endomorphisme, automorphisme, forme linéaire.
?
**Réponse:**
Isomorphisme = morphisme bijectif ; endomorphisme = morphisme $E \to E$ ; automorphisme = endomorphisme bijectif ; forme linéaire = application linéaire à valeurs dans $K$.

## 11. L(E,F), L(E), E*
Donner les notations $L(E,F)$, $L(E)$ et $E^*$.
?
**Réponse:**
$$
L(E,F) = \{f : E \to F \text{ linéaires}\}, \quad L(E) = L(E,E), \quad E^* = L(E,K) \text{ (dual de } E).
$$
$(L(E), +, \cdot, \circ)$ est une K-algèbre ; son groupe des inversibles est $GL(E)$.

## 12. Formes linéaires sur K^n
Comment s'écrivent les formes linéaires sur $K^n$ ?
?
**Réponse:**
Ce sont exactement les applications
$$
(x_i)_{1 \le i \le n} \mapsto \sum_{i=1}^n \alpha_i x_i, \quad (\alpha_1, \ldots, \alpha_n) \in K^n.
$$

## 13. Linéarité et combinaisons / Vect
Comment une application linéaire agit sur les combinaisons et les Vect ?
?
**Réponse:**
$$
u\left( \sum_{i \in I} \alpha_i x_i \right) = \sum_{i \in I} \alpha_i u(x_i), \qquad u(\operatorname{Vect}(x_i)) = \operatorname{Vect}(u(x_i)).
$$

## 14. Noyau, image, injectivité, surjectivité
Caractériser l'injectivité et la surjectivité d'une application linéaire.
?
**Réponse:**
$\operatorname{Ker}(f)$ et $\operatorname{Im}(f)$ sont des sous-espaces vectoriels et
$$
f \text{ injective} \iff \operatorname{Ker}(f) = \{0\}, \qquad f \text{ surjective} \iff \operatorname{Im}(f) = F.
$$
Une forme linéaire non nulle est toujours surjective.

## 15. Image directe et réciproque de sous-espaces
Que dire des images directes et réciproques de sous-espaces par un morphisme ?
?
**Réponse:**
Si $f$ est linéaire, $E'$ sev de $E$, $F'$ sev de $F$ : $f(E')$ est un sev de $F$ et $f^{-1}(F')$ un sev de $E$. En particulier $\operatorname{Ker}(f), \operatorname{Im}(f)$ sont des sous-espaces.

## 16. Composition et réciproque
Que dire de la composée et de la réciproque d'un isomorphisme ?
?
**Réponse:**
La composée de deux applications linéaires est linéaire ; la réciproque d'un isomorphisme est un isomorphisme. Le morphisme réciproque de $w \mapsto uwu^{-1}$ (automorphisme intérieur) illustre ces propriétés sur $GL(E)$.

## 17. Équation linéaire
Comment résoudre une équation linéaire $f(x) = y$ ?
?
**Réponse:**
$$
\text{Compatible} \iff y \in \operatorname{Im}(f), \qquad S_E = x_0 + \operatorname{Ker}(f)
$$
où $x_0$ est une solution particulière et $S_H = \operatorname{Ker}(f)$ les solutions de l'équation homogène.

## 18. Familles génératrice, libre, base
Définir famille génératrice, famille libre et base.
?
**Réponse:**
Génératrice : $\operatorname{Vect}(x_i) = E$. Libre : $\sum \alpha_i x_i = 0 \implies \forall i, \ \alpha_i = 0$. Liée : sinon. Une **base** est une famille libre et génératrice.

## 19. Dimension et base incomplète
Enoncer les théorèmes de dimension et de la base incomplète.
?
**Réponse:**
En dimension finie, toutes les bases ont $n = \dim E$ éléments, et toute famille libre se complète en une base de $E$ (base incomplète). Une famille libre a au plus $n$ éléments, une famille génératrice au moins $n$.

## 20. Théorème du rang
Enoncer la relation rang-noyau.
?
**Réponse:**
Si $\dim E < +\infty$ et $f \in L(E,F)$ :
$$
\dim E = \dim \operatorname{Ker}(f) + \dim \operatorname{Im}(f), \qquad \operatorname{rg}(f) = \dim \operatorname{Im}(f).
$$
En dimension finie et égale, injectif, surjectif et isomorphisme sont équivalents.

## 21. Rang d'une famille
Définir le rang d'une famille de vecteurs.
?
**Réponse:**
$$
\operatorname{rg}((x_i)_{i \in I}) = \dim \operatorname{Vect}((x_i)_{i \in I}),
$$
conservé par multiplication d'un vecteur par un scalaire non nul et par addition d'une combinaison linéaire des autres.

## 22. Matrice d'une application linéaire
Que représente la matrice d'une application linéaire ?
?
**Réponse:**
Dans des bases $\mathcal{B}$ de $E$ et $\mathcal{B}'$ de $F$, $\mathrm{Mat}_{\mathcal{B}, \mathcal{B}'}(f) \in M_{m,n}(K)$ a pour colonnes les coordonnées de $f(e_1), \ldots, f(e_n)$ dans $\mathcal{B}'$. Si $Y$ désigne les coordonnées de $f(x)$, alors $Y = \mathrm{Mat}_{\mathcal{B}, \mathcal{B}'}(f) X$.

## 23. Espace affine
Rappeler la définition d'un K-espace affine.
?
**Réponse:**
$(\mathcal{E}, E, +)$ avec $\mathcal{E} \neq \emptyset$, $E$ K-espace vectoriel (la direction), $+ : \mathcal{E} \times E \to \mathcal{E}$ telle que $x \mapsto M + x$ est bijective et $(M + x) + y = M + (x + y)$. Tout espace vectoriel est canoniquement affine ; muni d'une origine $A$, un espace affine devient un espace vectoriel (vectorialisé).

## 24. K-algèbre
Définir une K-algèbre.
?
**Réponse:**
$(A, +, \cdot, \star)$ K-algèbre si $(A, +, \cdot)$ est un K-espace vectoriel, $(A, +, \star)$ un anneau et
$$
\forall (\lambda, a, b) \in K \times A \times A, \quad \lambda \cdot (a \star b) = (\lambda \cdot a) \star b = a \star (\lambda \cdot b).
$$
Exemples : $\mathbb{C}$ $\mathbb{R}$-algèbre, $K[X]$ algèbre commutative intègre, $L(E)$ algèbre.