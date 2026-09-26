#flashcards/maths/prépa/premiere_annee/cours/13_polynomes/algebre_arithmetique
## 1. Degré d'un polynôme
Comment définit-on le degré de $P\in\mathbb K[X]$ ?
?
**Réponse:**
Pour $P\ne0$, $\deg P$ est le plus grand indice de son coefficient non nul.
Par convention, $\deg0=-\infty$.

## 2. Degré d'une somme et d'un produit
Quelles relations de degré faut-il connaître dans $\mathbb K[X]$ ?
?
**Réponse:**
$\deg(P+Q)\le\max(\deg P,\deg Q)$, avec égalité si les degrés sont distincts.
Si $P,Q\ne0$, $\deg(PQ)=\deg P+\deg Q$.

## 3. Division euclidienne
Énoncer le théorème de la division euclidienne dans $\mathbb K[X]$.
?
**Réponse:**
Pour $A\in\mathbb K[X]$ et $B\ne0$, il existe un unique couple $(Q,R)$ tel que $A=BQ+R$ et $\deg R<\deg B$.

## 4. Divisibilité
Que signifie $P\mid Q$ dans $\mathbb K[X]$ ?
?
**Réponse:**
Cela signifie qu'il existe $A\in\mathbb K[X]$ tel que $Q=PA$.
Si $P\mid Q$ et $Q\mid P$, alors $P$ et $Q$ sont associés.

## 5. PGCD et Bézout
Quel lien entre $\gcd(P,Q)$ et les combinaisons linéaires de $P,Q$ ?
?
**Réponse:**
Le PGCD unitaire $D$ vérifie $D=UP+VQ$ pour certains $U,V\in\mathbb K[X]$.
Ainsi, $P$ et $Q$ sont premiers entre eux si et seulement s'il existe $U,V$ tels que $UP+VQ=1$.

## 6. Lemme de Gauss polynômial
Énoncer le lemme de Gauss dans $\mathbb K[X]$.
?
**Réponse:**
Si $P\mid QR$ et $\gcd(P,Q)=1$, alors $P\mid R$.

## 7. Dérivation formelle
Comment définit-on la dérivée de $P(X)=\sum_{k=0}^na_kX^k$ ?
?
**Réponse:**
$P'(X)=\sum_{k=1}^nka_kX^{k-1}$.
Elle vérifie $(P+Q)'=P'+Q'$ et $(PQ)'=P'Q+PQ'$.

## 8. Composition
Quelle relation de degré vérifie la composition $P\circ Q$ ?
?
**Réponse:**
Si $P$ et $Q$ sont non constants, $\deg(P\circ Q)=\deg P\,\deg Q$.
La composition est associative mais n'est pas commutative en général.
