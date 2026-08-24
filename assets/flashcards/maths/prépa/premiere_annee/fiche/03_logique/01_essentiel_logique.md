#flashcards/maths/prépa/premiere_annee/fiche/03_logique/essentiel_logique
## 1. Les quatre négations à savoir écrire
Donner les négations de $\forall x\in E,\ P(x)$, $\exists x\in E,\ P(x)$, $x\le y$ et $x=y$.
?
**Réponse:**
$\neg(\forall x\in E,\ P(x))\Longleftrightarrow\exists x\in E,\ \neg P(x)$.
$\neg(\exists x\in E,\ P(x))\Longleftrightarrow\forall x\in E,\ \neg P(x)$.
$\neg(x\le y)\Longleftrightarrow x>y$ et $\neg(x=y)\Longleftrightarrow x\ne y$.

## 2. Égalité et inclusion d'ensembles
Comment prouver $A=B$ et comment prouver $A\subset B$ ?
?
**Réponse:**
Pour $A=B$, prouver $\forall x,\ x\in A\Longleftrightarrow x\in B$, souvent par double inclusion.
Pour $A\subset B$, partir d'un élément arbitraire $x\in A$ et montrer $x\in B$.

## 3. De Morgan : ensembles et propositions
Énoncer les deux lois de De Morgan pour les ensembles et pour les propositions.
?
**Réponse:**
$(A\cup B)^c=A^c\cap B^c$ et $(A\cap B)^c=A^c\cup B^c$.
$\neg(P\lor Q)\Longleftrightarrow\neg P\land\neg Q$ et $\neg(P\land Q)\Longleftrightarrow\neg P\lor\neg Q$.

## 4. Implication
Quelles transformations logiques de $P\Rightarrow Q$ faut-il connaître ?
?
**Réponse:**
$P\Rightarrow Q\Longleftrightarrow\neg Q\Rightarrow\neg P$.
$\neg(P\Rightarrow Q)\Longleftrightarrow P\land\neg Q$.
Ne pas confondre la contraposée avec la réciproque $Q\Rightarrow P$.

## 5. Interpréter une équivalence
Comment rédiger une preuve de $P\Longleftrightarrow Q$ ?
?
**Réponse:**
Prouver séparément $P\Rightarrow Q$ puis $Q\Rightarrow P$.
Une équivalence ne s'obtient jamais en prouvant une seule implication.

## 6. Unicité
Comment prouver « il existe un unique $x$ vérifiant $P(x)$ » ?
?
**Réponse:**
Prouver d'abord l'existence d'au moins un tel $x$.
Puis, si $x$ et $y$ vérifient $P$, démontrer $x=y$.

## 7. Relation d'ordre ou d'équivalence
Comment distinguer rapidement une relation d'ordre d'une relation d'équivalence ?
?
**Réponse:**
Une relation d'ordre est réflexive, antisymétrique et transitive.
Une relation d'équivalence est réflexive, symétrique et transitive.
La différence cruciale est donc antisymétrie contre symétrie.

## 8. Minimum, maximum, minorant et majorant
Quelle différence entre maximum et majorant d'une partie $A$ d'un ensemble ordonné ?
?
**Réponse:**
Un majorant $M$ vérifie $\forall x\in A,\ x\le M$ mais peut ne pas appartenir à $A$.
Un maximum est un majorant qui appartient à $A$.
Les définitions de minorant et minimum sont analogues.

## 9. Produit cartésien
Comment prouver l'égalité de deux produits cartésiens ou l'appartenance à l'un d'eux ?
?
**Réponse:**
Traduire $(x,y)\in A\times B$ par $x\in A$ et $y\in B$.
Pour l'égalité de deux produits, raisonner sur un couple arbitraire et ses deux coordonnées.

## 10. Référence pour une récurrence
Quel piège faut-il éviter dans une preuve par récurrence ?
?
**Réponse:**
L'hérédité doit partir d'un entier arbitraire $n$ pour lequel l'hypothèse de récurrence est explicitement supposée.
Il faut aussi vérifier une initialisation compatible avec l'énoncé.

## 11. Choisir une méthode de preuve
Quelle méthode privilégier selon la forme de l'énoncé ?
?
**Réponse:**
Pour une implication : preuve directe ou contraposée.
Pour une égalité d'ensembles : double inclusion.
Pour une existence et unicité : analyse-synthèse ou existence puis unicité.
Pour une assertion indexée par $n$ : récurrence.

## 12. Erreurs de logique fréquentes
Quelles erreurs faut-il éviter avec les quantificateurs et les implications ?
?
**Réponse:**
Ne pas inverser l'ordre de $\forall$ et $\exists$ : ils ne commutent pas en général.
Ne pas démontrer la réciproque à la place de l'implication demandée.
Ne pas conclure une existence à partir d'un calcul qui ne vérifie pas le candidat.
