#flashcards/maths/prépa/premiere_annee/cours/03_logique/ensembles_logique_relations
## 1. Égalité de deux ensembles
Quel principe permet de démontrer l'égalité de deux ensembles $E$ et $F$ ?
?
**Réponse:**
Le principe d'extensionnalité donne $E=F$ si et seulement si $\forall x,\ x\in E\Longleftrightarrow x\in F$.
En pratique, on démontre les deux inclusions $E\subset F$ et $F\subset E$.

## 2. Ensemble vide et singleton
Comment caractériser l'ensemble vide et un singleton ?
?
**Réponse:**
$\varnothing$ est l'unique ensemble sans élément.
$\{a\}$ est l'ensemble dont l'unique élément est $a$.
Attention : $a\in\{a\}$, tandis que $a\ne\{a\}$ en général.

## 3. Définition en compréhension
Comment lire l'ensemble $\{x\in E\mid P(x)\}$ ?
?
**Réponse:**
C'est l'ensemble des éléments $x$ de $E$ qui vérifient le prédicat $P$.
Pour tout $x\in E$, $x\in\{y\in E\mid P(y)\}\Longleftrightarrow P(x)$.

## 4. Quantificateurs
Quelle est la signification de $\forall x\in E,\ P(x)$, $\exists x\in E,\ P(x)$ et $\exists!x\in E,\ P(x)$ ?
?
**Réponse:**
$\forall$ signifie « pour tout » ; $\exists$ signifie « il existe au moins un ».
$\exists!x\in E,\ P(x)$ signifie qu'il existe un unique $x\in E$ vérifiant $P(x)$.

## 5. Négation des quantificateurs
Comment nie-t-on des propositions quantifiées ?
?
**Réponse:**
$\neg(\forall x\in E,\ P(x))\Longleftrightarrow\exists x\in E,\ \neg P(x)$.
$\neg(\exists x\in E,\ P(x))\Longleftrightarrow\forall x\in E,\ \neg P(x)$.
Pour nier une inégalité, on inverse aussi correctement le symbole : $\neg(x\le y)$ équivaut à $x>y$.

## 6. Inclusion et inclusion stricte
Que signifient $A\subset B$ et $A\subsetneq B$ ?
?
**Réponse:**
$A\subset B$ signifie $\forall x,\ x\in A\Rightarrow x\in B$.
$A\subsetneq B$ signifie $A\subset B$ et $A\ne B$, ou encore qu'il existe $x\in B\setminus A$.

## 7. Union, intersection et différence
Comment caractériser l'union, l'intersection et la différence de deux parties $A,B\subset E$ ?
?
**Réponse:**
$x\in A\cup B\Longleftrightarrow x\in A$ ou $x\in B$.
$x\in A\cap B\Longleftrightarrow x\in A$ et $x\in B$.
$A\setminus B=\{x\in A\mid x\notin B\}$.

## 8. Complémentaire et lois de De Morgan
Quelles sont les lois de De Morgan dans un univers $E$ ?
?
**Réponse:**
Le complémentaire de $A$ dans $E$ est $A^c=E\setminus A$.
$(A\cup B)^c=A^c\cap B^c$.
$(A\cap B)^c=A^c\cup B^c$.

## 9. Produit cartésien
Définir $A\times B$ et expliquer l'égalité de deux couples.
?
**Réponse:**
$A\times B=\{(a,b)\mid a\in A,\ b\in B\}$.
On a $(a,b)=(a',b')$ si et seulement si $a=a'$ et $b=b'$.
L'ordre compte : en général, $(a,b)\ne(b,a)$.

## 10. Équivalence logique
Quand deux propositions $P$ et $Q$ sont-elles logiquement équivalentes ?
?
**Réponse:**
Elles sont logiquement équivalentes si elles ont la même valeur de vérité dans tous les cas.
On note alors $P\Longleftrightarrow Q$.

## 11. Implication et contraposée
Quelle est la contraposée de $P\Rightarrow Q$, et quelle est sa valeur logique ?
?
**Réponse:**
La contraposée est $\neg Q\Rightarrow\neg P$.
Elle est toujours logiquement équivalente à $P\Rightarrow Q$.
En revanche, la réciproque $Q\Rightarrow P$ ne l'est pas nécessairement.

## 12. Négation d'une implication
Comment nier $P\Rightarrow Q$ ?
?
**Réponse:**
$\neg(P\Rightarrow Q)\Longleftrightarrow P\land\neg Q$.
Une implication est donc fausse exactement lorsque son hypothèse est vraie et sa conclusion fausse.

## 13. Implication et condition nécessaire ou suffisante
Comment interpréter $P\Rightarrow Q$ en termes de conditions ?
?
**Réponse:**
$P$ est une condition suffisante pour $Q$.
$Q$ est une condition nécessaire pour $P$.
Si $P\Longleftrightarrow Q$, chacune est nécessaire et suffisante pour l'autre.

## 14. Relation binaire
Qu'est-ce qu'une relation binaire $\mathcal R$ sur $E$ ?
?
**Réponse:**
C'est une propriété portant sur deux éléments de $E$.
Pour $x,y\in E$, on écrit $x\mathcal R y$ lorsque $x$ est en relation avec $y$.

## 15. Relation d'ordre
Quelles propriétés définissent une relation d'ordre sur $E$ ?
?
**Réponse:**
Elle est réflexive : $x\preccurlyeq x$.
Elle est antisymétrique : $x\preccurlyeq y$ et $y\preccurlyeq x$ impliquent $x=y$.
Elle est transitive : $x\preccurlyeq y$ et $y\preccurlyeq z$ impliquent $x\preccurlyeq z$.

## 16. Ordre total et éléments remarquables
Quelle différence entre ordre partiel et ordre total, et comment définir maximum et minimum ?
?
**Réponse:**
Un ordre est total si tous les éléments sont comparables.
$m\in A$ est un maximum de $A$ si $\forall x\in A,\ x\preccurlyeq m$.
$m\in A$ est un minimum de $A$ si $\forall x\in A,\ m\preccurlyeq x$.

## 17. Relation d'équivalence
Quelles propriétés définissent une relation d'équivalence ?
?
**Réponse:**
Elle est réflexive, symétrique et transitive.
La congruence modulo $n$ sur $\mathbb Z$ en est un exemple : $a\equiv b\ [n]$ si $n\mid(a-b)$.

## 18. Classe d'équivalence et partition
Que faut-il savoir sur les classes d'une relation d'équivalence ?
?
**Réponse:**
La classe de $x$ est $[x]=\{y\in E\mid y\sim x\}$.
Deux classes sont soit égales, soit disjointes.
L'ensemble des classes forme une partition de $E$.

## 19. Démonstration par disjonction de cas
Quand et comment utiliser une preuve par cas ?
?
**Réponse:**
Si $P_1\lor\cdots\lor P_n$ est vrai, on démontre la conclusion dans chacun des cas $P_i$.
La conclusion est alors vraie sans avoir besoin de savoir quel cas se produit.

## 20. Raisonnement par l'absurde
Quel est le principe d'une preuve par l'absurde ?
?
**Réponse:**
Pour prouver $P$, on suppose $\neg P$ et on en déduit une contradiction.
La contradiction doit être explicitement identifiée ; elle établit alors $P$.

## 21. Récurrence simple
Quelle structure doit avoir une démonstration par récurrence sur $n\in\mathbb N$ ?
?
**Réponse:**
On vérifie l'initialisation $P(n_0)$.
On suppose $P(n)$ vraie pour un entier $n\ge n_0$ et on démontre l'hérédité $P(n)\Rightarrow P(n+1)$.
On conclut $\forall n\ge n_0,\ P(n)$.

## 22. Analyse-synthèse
Comment organiser une preuve d'existence et d'unicité par analyse-synthèse ?
?
**Réponse:**
Dans l'analyse, on suppose l'objet cherché existant et on détermine nécessairement sa forme.
Dans la synthèse, on vérifie que le ou les candidats obtenus satisfont bien les conditions.
L'unicité résulte de l'analyse si elle ne laisse qu'un candidat.
