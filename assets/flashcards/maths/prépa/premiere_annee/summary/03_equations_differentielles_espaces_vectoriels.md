#flashcards/maths/prépa/premiere_annee/summary/equations_differentielles_espaces_vectoriels
## 1. Équation différentielle linéaire d'ordre $1$
Quelle est la solution générale de $y'+a(x)y=b(x)$ sur un intervalle $I$ ?
?
**Réponse:**
Si $A$ est une primitive de $a$, les solutions sont $y(x)=e^{-A(x)}\left(C+\int_{x_0}^x b(t)e^{A(t)}\,dt\right)$.
La solution générale est une solution particulière plus la solution générale de l'équation homogène.

## 2. Équation à variables séparables
Comment résoudre $y'=a(x)b(y)$ lorsque la séparation est licite ?
?
**Réponse:**
Sur un intervalle où $b(y)\ne0$, on écrit $\frac{y'}{b(y)}=a(x)$.
Après intégration, $\int\frac{dy}{b(y)}=\int a(x)\,dx+C$.
Il faut aussi chercher les solutions constantes vérifiant $b(y)=0$.

## 3. Équation linéaire d'ordre $2$ à coefficients constants
Comment déterminer les solutions de $y''+ay'+by=0$ ?
?
**Réponse:**
On résout l'équation caractéristique $r^2+ar+b=0$.
Deux racines réelles distinctes donnent $Ce^{r_1x}+De^{r_2x}$.
Une racine double $r$ donne $(C+Dx)e^{rx}$.
Des racines $\alpha\pm i\beta$ donnent $e^{\alpha x}(C\cos\beta x+D\sin\beta x)$.

## 4. Sous-espace vectoriel
Quel critère permet de reconnaître un sous-espace vectoriel $F$ de $E$ ?
?
**Réponse:**
$F$ est un sous-espace vectoriel si $F\ne\varnothing$ et si, pour tous $x,y\in F$ et tout $\lambda\in\mathbb K$, $x+y\in F$ et $\lambda x\in F$.
Équivalemment : $F\ne\varnothing$ et $\lambda x+\mu y\in F$ pour tous $x,y\in F$ et $\lambda,\mu\in\mathbb K$.

## 5. Famille libre et génératrice
Définir une famille libre et une famille génératrice de $E$.
?
**Réponse:**
$(x_i)_{i\in I}$ est libre si toute combinaison linéaire nulle est triviale.
Elle est génératrice si tout vecteur de $E$ est combinaison linéaire des $x_i$.
Une base est une famille à la fois libre et génératrice.

## 6. Dimension
Que faut-il savoir sur la dimension d'un espace vectoriel de dimension finie ?
?
**Réponse:**
Toutes ses bases ont le même cardinal, appelé dimension.
Une famille libre a au plus $\dim E$ vecteurs ; une famille génératrice en a au moins $\dim E$.
Une famille de $\dim E$ vecteurs est une base si et seulement si elle est libre, si et seulement si elle est génératrice.

## 7. Rang et théorème du rang
Définir le rang d'une application linéaire $u:E\to F$ et énoncer le théorème du rang.
?
**Réponse:**
$\operatorname{rg}(u)=\dim(\operatorname{Im}u)$.
Si $E$ est de dimension finie, $\dim E=\dim(\ker u)+\operatorname{rg}(u)$.

## 8. Projecteur et symétrie
Comment caractériser un projecteur et une symétrie vectoriels ?
?
**Réponse:**
$p$ est un projecteur si $p^2=p$.
$s$ est une symétrie si $s^2=\operatorname{id}$.
Pour une décomposition $E=F\oplus G$, le projecteur sur $F$ parallèlement à $G$ est $p(f+g)=f$, et la symétrie associée est $s(f+g)=f-g$.

## 9. Espaces affines
Comment caractériser un sous-espace affine $A$ de direction $F$ ?
?
**Réponse:**
Il existe un point $a\in A$ tel que $A=a+F=\{a+u\mid u\in F\}$.
Pour $x,y\in A$, le vecteur $\overrightarrow{xy}$ appartient à $F$.
