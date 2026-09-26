#flashcards/maths/prépa/premiere_annee/summary/analyse_calcul_differentiel_integration
## 1. Équivalents
Que signifie $f\sim g$ au voisinage de $a$ ?
?
**Réponse:**
$f\sim g$ signifie que $\frac{f(x)}{g(x)}\to1$ lorsque $x\to a$.
Cette relation permet de comparer les limites et les comportements dominants.

## 2. Développements limités usuels
Quels DL à l'ordre $2$ faut-il connaître au voisinage de $0$ ?
?
**Réponse:**
$e^x=1+x+\frac{x^2}{2}+o(x^2)$.
$\sin x=x+o(x^2)$ et $\cos x=1-\frac{x^2}{2}+o(x^2)$.
$\ln(1+x)=x-\frac{x^2}{2}+o(x^2)$ et $(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}2x^2+o(x^2)$.
<!--SR:!2026-08-27,1,230-->

## 3. Formule de Taylor-Young
Énoncer la formule de Taylor-Young à l'ordre $n$ en $a$.
?
**Réponse:**
Si $f$ est $n$ fois dérivable au voisinage de $a$, alors $f(a+h)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}h^k+o(h^n)$ lorsque $h\to0$.
<!--SR:!2026-08-26,0,230-->

## 4. Dérivée et approximation affine
Quelle approximation donne la dérivabilité de $f$ en $a$ ?
?
**Réponse:**
$f$ est dérivable en $a$ si $f(a+h)=f(a)+f'(a)h+o(h)$.
La droite d'équation $y=f(a)+f'(a)(x-a)$ est la tangente au graphe en $a$.
<!--SR:!2026-08-29,3,250-->

## 5. Théorème des accroissements finis
Énoncer le TAF.
?
**Réponse:**
Si $f$ est continue sur $[a,b]$ et dérivable sur $]a,b[$, il existe $c\in]a,b[$ tel que $f(b)-f(a)=f'(c)(b-a)$.
<!--SR:!2026-08-26,0,230-->

## 6. Convexité
Quel critère différentiel caractérise la convexité d'une fonction deux fois dérivable ?
?
**Réponse:**
Sur un intervalle, $f$ est convexe si et seulement si $f'$ est croissante, et si $f$ est deux fois dérivable, si et seulement si $f''\ge0$.
Le graphe d'une fonction convexe est au-dessus de ses tangentes.

## 7. Intégration par parties
Quelle est la formule d'intégration par parties ?
?
**Réponse:**
Si $u$ et $v$ sont de classe $\mathcal C^1$ sur $[a,b]$, alors $\int_a^b u(x)v'(x)\,dx=[u(x)v(x)]_a^b-\int_a^b u'(x)v(x)\,dx$.
<!--SR:!2026-08-30,4,270-->

## 8. Changement de variable
Quelle est la formule de changement de variable dans une intégrale ?
?
**Réponse:**
Si $\varphi$ est de classe $\mathcal C^1$ et envoie $[\alpha,\beta]$ dans $[a,b]$, alors $\int_\alpha^\beta f(\varphi(t))\varphi'(t)\,dt=\int_{\varphi(\alpha)}^{\varphi(\beta)}f(x)\,dx$.
<!--SR:!2026-08-27,1,230-->

## 9. Théorème fondamental de l'analyse
Quelle est la dérivée de $F(x)=\int_a^x f(t)\,dt$ lorsque $f$ est continue ?
?
**Réponse:**
$F$ est dérivable et $F'(x)=f(x)$.
Ainsi, les primitives de $f$ diffèrent d'une constante.
<!--SR:!2026-08-30,4,270-->

## 10. Fractions rationnelles
Quelle est la forme générale de la décomposition en éléments simples sur $\mathbb C$ ?
?
**Réponse:**
Après division euclidienne, une fraction rationnelle se décompose en somme de termes $\frac{a_k}{(X-\alpha)^k}$, où $\alpha$ parcourt les racines du dénominateur.
Sur $\mathbb R$, les facteurs quadratiques irréductibles donnent aussi des numérateurs affines.
<!--SR:!2026-08-26,0,230-->

## 11. Polynômes : racines et multiplicité
Comment caractériser une racine $\alpha$ de multiplicité $m$ d'un polynôme $P$ ?
?
**Réponse:**
$\alpha$ est racine de multiplicité $m$ si $P(X)=(X-\alpha)^mQ(X)$ avec $Q(\alpha)\ne0$.
Équivalemment, $P(\alpha)=\cdots=P^{(m-1)}(\alpha)=0$ et $P^{(m)}(\alpha)\ne0$.
<!--SR:!2026-08-26,0,230-->

## 12. Théorème de d'Alembert-Gauss
Quel théorème fondamental concerne les racines des polynômes complexes ?
?
**Réponse:**
Tout polynôme non constant à coefficients complexes admet une racine complexe.
Un polynôme de degré $n$ sur $\mathbb C$ possède exactement $n$ racines comptées avec multiplicité.
<!--SR:!2026-08-26,0,230-->
