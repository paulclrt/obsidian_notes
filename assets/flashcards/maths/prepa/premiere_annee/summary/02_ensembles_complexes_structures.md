#flashcards/maths/prépa/premiere_annee/summary/ensembles_complexes_structures
## 1. Quantificateurs
Comment nie-t-on une proposition de la forme $\forall x\in E,\ P(x)$ ou $\exists x\in E,\ P(x)$ ?
?
**Réponse:**
$\neg(\forall x\in E,\ P(x))\Longleftrightarrow\exists x\in E,\ \neg P(x)$.
$\neg(\exists x\in E,\ P(x))\Longleftrightarrow\forall x\in E,\ \neg P(x)$.

## 2. Union, intersection et complémentaire
Quelles sont les définitions de $A\cup B$, $A\cap B$ et du complémentaire de $A$ dans $E$ ?
?
**Réponse:**
$A\cup B=\{x\mid x\in A\text{ ou }x\in B\}$.
$A\cap B=\{x\mid x\in A\text{ et }x\in B\}$.
$E\setminus A=\{x\in E\mid x\notin A\}$.

## 3. Relation d'équivalence
Quelles propriétés définissent une relation d'équivalence sur $E$ ?
?
**Réponse:**
Elle est réflexive : $x\sim x$.
Elle est symétrique : $x\sim y\Rightarrow y\sim x$.
Elle est transitive : $x\sim y$ et $y\sim z\Rightarrow x\sim z$.

## 4. Classes d'équivalence
Que faut-il savoir sur les classes d'équivalence d'une relation d'équivalence ?
?
**Réponse:**
La classe de $x$ est $\operatorname{cl}(x)=\{y\in E\mid y\sim x\}$.
Deux classes sont soit égales, soit disjointes.
Les classes d'équivalence forment une partition de $E$.

## 5. Borne supérieure
Définir $\sup A$ pour une partie non vide majorée $A\subset\mathbb R$.
?
**Réponse:**
$s=\sup A$ si $s$ est un majorant de $A$ et si tout réel strictement inférieur à $s$ n'est pas un majorant de $A$.
Équivalemment : $\forall\varepsilon>0$, il existe $a\in A$ tel que $s-\varepsilon<a\le s$.

## 6. Module et conjugaison
Quelles identités fondamentales relient un complexe $z$, son conjugué et son module ?
?
**Réponse:**
Si $z=a+ib$, alors $\overline z=a-ib$ et $|z|=\sqrt{a^2+b^2}$.
$z\overline z=|z|^2$.
$|zw|=|z||w|$ et, si $w\ne0$, $\left|\frac zw\right|=\frac{|z|}{|w|}$.

## 7. Forme exponentielle
Comment s'écrit un complexe non nul en forme exponentielle ?
?
**Réponse:**
Tout $z\ne0$ s'écrit $z=|z|e^{i\theta}$, où $\theta$ est un argument de $z$.
Les arguments de $z$ sont égaux modulo $2\pi$.
La formule d'Euler est $e^{i\theta}=\cos\theta+i\sin\theta$.

## 8. Formule de Moivre et racines $n$-ièmes
Que donne la formule de Moivre et comment obtenir les racines $n$-ièmes de $z\ne0$ ?
?
**Réponse:**
$(re^{i\theta})^n=r^ne^{in\theta}$.
Les racines $n$-ièmes de $re^{i\theta}$ sont $r^{1/n}e^{i(\theta+2k\pi)/n}$ pour $k=0,\ldots,n-1$.

## 9. Groupe et sous-groupe
Quelles conditions permettent de reconnaître un sous-groupe $H$ d'un groupe $G$ ?
?
**Réponse:**
$H$ est un sous-groupe de $G$ si $H\ne\varnothing$ et $\forall x,y\in H,\ xy^{-1}\in H$.
Dans ce cas, la loi et l'inverse sont ceux de $G$.

## 10. Anneau intègre et corps
Quelle est la différence entre anneau, anneau intègre et corps ?
?
**Réponse:**
Un anneau possède une addition et une multiplication distributive.
Il est intègre s'il est non nul, commutatif, unitaire et sans diviseur de zéro.
Un corps est un anneau commutatif unitaire où tout élément non nul est inversible.
