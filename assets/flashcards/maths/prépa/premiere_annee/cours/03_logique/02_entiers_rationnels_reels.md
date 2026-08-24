#flashcards/maths/prépa/premiere_annee/cours/03_logique/entiers_rationnels_reels
## 1. Division euclidienne dans $\mathbb Z$
Énoncer le théorème de la division euclidienne.
?
**Réponse:**
Pour $a\in\mathbb Z$ et $b\in\mathbb Z^*$, il existe un unique couple $(q,r)\in\mathbb Z\times\mathbb N$ tel que $a=bq+r$ et $0\le r<|b|$.

## 2. Divisibilité
Que signifie $a\mid b$ dans $\mathbb Z$, et quelles propriétés immédiates faut-il connaître ?
?
**Réponse:**
$a\mid b$ signifie qu'il existe $k\in\mathbb Z$ tel que $b=ak$.
Si $a\mid b$ et $a\mid c$, alors $a\mid(ub+vc)$ pour tous $u,v\in\mathbb Z$.

## 3. PGCD et identité de Bézout
Quel lien entre le PGCD de $a,b\in\mathbb Z$ et les combinaisons linéaires de $a,b$ ?
?
**Réponse:**
Il existe $u,v\in\mathbb Z$ tels que $au+bv=\gcd(a,b)$.
Les diviseurs communs de $a$ et $b$ sont exactement les diviseurs de $\gcd(a,b)$.

## 4. Lemme de Gauss
Énoncer le lemme de Gauss.
?
**Réponse:**
Si $a\mid bc$ et $\gcd(a,b)=1$, alors $a\mid c$.
En particulier, si $p$ est premier et $p\mid bc$, alors $p\mid b$ ou $p\mid c$.

## 5. Décomposition en facteurs premiers
Quel théorème décrit la décomposition des entiers naturels non nuls ?
?
**Réponse:**
Tout entier $n\ge2$ s'écrit de manière unique, à l'ordre des facteurs près, $n=\prod_{p\in\mathcal P}p^{\nu_p(n)}$, avec un nombre fini d'exposants non nuls.

## 6. Congruence
Comment définit-on $a\equiv b\ [n]$ et quelles opérations la conservent ?
?
**Réponse:**
$a\equiv b\ [n]$ signifie $n\mid(a-b)$.
On peut additionner, soustraire et multiplier des congruences de même modulo.
Si $a\equiv b\ [n]$, alors $P(a)\equiv P(b)\ [n]$ pour tout $P\in\mathbb Z[X]$.

## 7. Nombres rationnels
Comment caractériser un rationnel et quand deux écritures fractionnaires représentent-elles le même rationnel ?
?
**Réponse:**
$x\in\mathbb Q$ si $x=\frac pq$ avec $p\in\mathbb Z$ et $q\in\mathbb Z^*$.
$\frac pq=\frac{p'}{q'}$ si et seulement si $pq'=p'q$.

## 8. Borne supérieure
Définir $s=\sup A$ pour une partie non vide majorée $A\subset\mathbb R$.
?
**Réponse:**
$s$ est un majorant de $A$ et tout majorant $M$ de $A$ vérifie $s\le M$.
Équivalemment, $\forall\varepsilon>0$, il existe $a\in A$ tel que $s-\varepsilon<a\le s$.

## 9. Complétude de $\mathbb R$
Quel axiome distingue fondamentalement $\mathbb R$ de $\mathbb Q$ ?
?
**Réponse:**
Toute partie non vide de $\mathbb R$ majorée possède une borne supérieure dans $\mathbb R$.
Cette propriété de complétude est fausse dans $\mathbb Q$.

## 10. Valeur absolue
Quelles inégalités sur la valeur absolue faut-il connaître ?
?
**Réponse:**
$|x|\le r$ équivaut à $-r\le x\le r$ pour $r\ge0$.
$|x+y|\le|x|+|y|$.
$\big||x|-|y|\big|\le|x-y|$.

## 11. Partie entière
Comment caractériser la partie entière $\lfloor x\rfloor$ ?
?
**Réponse:**
$\lfloor x\rfloor$ est l'unique entier $n$ tel que $n\le x<n+1$.
Elle vérifie $x-1<\lfloor x\rfloor\le x$.
