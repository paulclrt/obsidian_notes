#flashcards/maths/prépa/premiere_annee/summary/fonctions_trigonometrie
## 1. Image directe et image réciproque
Soit $(f:E\to F)$, $(A\subset E)$ et $(B\subset F)$. Comment définit-on $(f(A))$ et $(f^{-1}(B))$ ?
?
**Réponse:**
$f(A)=\{f(x)\mid x\in A\}$.
$f^{-1}(B)=\{x\in E\mid f(x)\in B\}$.
Attention : $f^{-1}(B)$ désigne toujours une image réciproque, même si $f$ n'est pas bijective.

## 2. Injectivité, surjectivité et bijectivité
Quels sont les critères de définition d'une application injective, surjective et bijective ?
?
**Réponse:**
$f:E\to F$ est injective si $f(x)=f(y)\Rightarrow x=y$.
Elle est surjective si $\forall y\in F,\ \exists x\in E,\ f(x)=y$.
Elle est bijective si elle est à la fois injective et surjective ; tout $y\in F$ possède alors un unique antécédent.
<!--SR:!2026-08-25,1,230-->

## 3. Réciproque d'une bijection
Quand une application $f:E\to F$ admet-elle une réciproque, et quelles identités la caractérisent ?
?
**Réponse:**
Elle admet une réciproque exactement lorsqu'elle est bijective.
Sa réciproque $f^{-1}:F\to E$ vérifie $f^{-1}\circ f=\operatorname{id}_E$ et $f\circ f^{-1}=\operatorname{id}_F$.
<!--SR:!2026-08-24,0,230-->

## 4. Parité et périodicité
Donner les définitions d'une fonction paire, impaire et $T$-périodique, ainsi que leur interprétation graphique.
?
**Réponse:**
$f$ est paire si $f(-x)=f(x)$ : son graphe est symétrique par rapport à l'axe des ordonnées.
$f$ est impaire si $f(-x)=-f(x)$ : son graphe est symétrique par rapport à l'origine.
$f$ est $T$-périodique si $f(x+T)=f(x)$ : son graphe est invariant par translation de vecteur $T\vec\imath$.

## 5. Fonctions trigonométriques usuelles
Quelles sont les parités et périodes fondamentales de $\cos$, $\sin$ et $\tan$ ?
?
**Réponse:**
$\cos$ est paire et $2\pi$-périodique.
$\sin$ est impaire et $2\pi$-périodique.
$\tan$ est impaire, définie sur $\mathbb R\setminus\{\frac\pi2+k\pi\mid k\in\mathbb Z\}$, et $\pi$-périodique.

## 6. Formules d'addition
Quelles sont les formules d'addition pour le cosinus et le sinus ?
?
**Réponse:**
$\cos(a+b)=\cos a\cos b-\sin a\sin b$.
$\sin(a+b)=\sin a\cos b+\cos a\sin b$.
En remplaçant $b$ par $-b$, on obtient les formules de soustraction.

## 7. Identité trigonométrique fondamentale
Quelle identité relie $\cos$ et $\sin$, et quelles conséquences immédiates donne-t-elle ?
?
**Réponse:**
$\cos^2x+\sin^2x=1$.
Donc $|\cos x|\leq1$ et $|\sin x|\leq1$.
Lorsque $\cos x\ne0$, $1+\tan^2x=\frac1{\cos^2x}$.

## 8. Dérivées des fonctions trigonométriques
Quelles sont les dérivées de $\cos$, $\sin$ et $\tan$ sur leurs domaines de définition ?
?
**Réponse:**
$(\cos x)'=-\sin x$.
$(\sin x)'=\cos x$.
$(\tan x)'=1+\tan^2x=\frac1{\cos^2x}$, là où $\tan$ est définie.
<!--SR:!2026-08-27,3,250-->
