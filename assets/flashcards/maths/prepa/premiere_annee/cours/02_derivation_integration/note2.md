# Intégration

## Définitions

**Intégrale :** Soient $a, b \in \mathbb{R}$ avec $a < b$. Soit $f : [a, b] \to \mathbb{R}$ une application continue. On note $$\int_a^b f(t) dt$$ (prononcer "intégrale de $a$ à $b$ de $f(t) dt$") l'aire comprise entre l'axe des abscisses (noté Ox) et le graphe de $f$, en comptant positivement les aires au dessus de l'axe Ox (donc lorsque $f(x) \geq 0$) et négativement les aires situées au dessous de l'axe Ox (lorsque $f(x) \leq 0$).

**Primitive :** Soit $I$ un intervalle de $\mathbb{R}$ et $f$ une application de $I$ dans $\mathbb{R}$ que l'on suppose continue. On dit que $F$ est une primitive de $f$ sur $I$ si et seulement si $F$ est dérivable et $F' = f$.

**Convention d'intégration :** Avec les notations et hypothèses précédentes, on convient que $$\int_a^b f(t) dt = -\int_b^a f(t) dt$$ et que $$\int_a^a f(t) dt = 0$$.

## Propriétés

### Propriétés de l'intégrale

Soit $I$ un intervalle inclus dans $\mathbb{R}$. Soient $f$ et $g$ deux applications continues de $I$ dans $\mathbb{R}$. Soient $a, b \in I$ (on peut avoir $a < b$, $b < a$ ou bien $a = b$).

- **Linéarité :** Pour tout $\alpha, \beta \in \mathbb{R}$,
$$\int_a^b (\alpha f + \beta g)(t) dt = \alpha \int_a^b f(t) dt + \beta \int_a^b g(t) dt$$

- **Relation de Chasles :** Pour tout $c \in I$,
$$\int_a^b f(t) dt = \int_a^c f(t) dt + \int_c^b f(t) dt$$

- **Positivité :** si $f \geq 0$, alors $$\int_a^b f(t) dt \geq 0$$

- **Croissance de l'intégrale :** si $f \leq g$, alors $$\int_a^b f(t) dt \leq \int_a^b g(t) dt$$

- **Inégalité triangulaire :**
$$\left|\int_a^b f(t) dt\right| \leq \int_a^b |f(t)| dt$$

### Théorème fondamental de l'analyse

Soit $I$ un intervalle de $\mathbb{R}$ et $f$ une application de $I$ dans $\mathbb{R}$ que l'on suppose continue. Soit $x_0 \in I$. Alors $x \mapsto \int_{x_0}^x f(t) dt$ est la unique primitive de $f$ qui s'annule en $x_0$.

**Corollaire :** Cela signifie que $$\frac{d}{dx}\left(\int_{x_0}^x f(t) dt\right) = f(x)$$.

### Corollaire sur les primitives

Soit $f$ une application continue d'un intervalle $I$ dans $\mathbb{R}$. Si $F$ est une primitive de $f$, alors pour tout $a, b \in I$,
$$\int_a^b f(t) dt = F(b) - F(a) = [F(t)]_a^b$$

**Notation :** L'écriture "$\int f(t) dt = F(t) + k, t \in I$" signifiera que $f$ est continue sur $I$ et que l'ensemble des primitives de $f$ est $\{F + k/k \in \mathbb{R}\}$.

### Propriété d'intégration d'une fonction positive

Soient $a, b \in \mathbb{R}$ avec $a < b$ et soit $f : [a, b] \to \mathbb{R}$ une application continue et positive, telle que $\int_a^b f(t) dt = 0$. Alors $f$ est identiquement nulle sur $[a, b]$.

## Remarques

- La notion d'aire utilisée est mal définie. C'est une définition intuitive et informelle. On construirera ultérieurement une théorie de l'intégration plus rigoureuse.
- L'opération de primitivation d'une fonction est l'opération réciproque de la dérivation.
- Une fonction ne possède pas une primitive unique, mais on peut dire que cette primitive est unique à une constante additive près.

## Calculs d'intégrales

### Changement de variables

**Théorème :** On suppose que $f$ est une application continue d'un intervalle $I$ dans $\mathbb{R}$, et que $\varphi$ est une application de classe $\mathcal{C}^1$ d'un intervalle $J$ dans $I$. Alors, pour tout $(\alpha, \beta) \in J^2$,
$$\int_\alpha^\beta f(\varphi(t))\varphi'(t) dt = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x) dx$$

Lorsque l'on remplace un membre de cette égalité par l'autre, on dit que l'on effectue le changement de variable $x = \varphi(t)$.

**Remarque :** Cette formule n'est pas à apprendre par cœur. Il faut savoir l'appliquer mécaniquement en menant mentalement le "raisonnement" suivant :
- Lorsque $t$ varie entre $\alpha$ et $\beta$, $x = \varphi(t)$ varie entre $\varphi(\alpha)$ et $\varphi(\beta)$, donc l'intégrale $\cdots dt$ devient $\cdots dx$.
- En outre, $dx = d(\varphi(t)) = \varphi'(t)dt$, donc $f(x)dx = f(\varphi(t))\varphi'(t)dt$.

### Intégration par parties

**Théorème :** Soient $u : I \to \mathbb{R}$ et $v : I \to \mathbb{R}$ deux applications de classe $\mathcal{C}^1$ sur $I$. Pour tout $(a, b) \in I^2$,
$$\int_a^b u(t)v'(t) dt = [u(t)v(t)]_a^b - \int_a^b u'(t)v(t) dt$$

**Formule alternative :** Soient $u : I \to \mathbb{R}$ et $v : I \to \mathbb{R}$ deux applications de classe $\mathcal{C}^1$ sur $I$. Alors,
$$\int u(t)v'(t) dt = u(t)v(t) - \int u'(t)v(t) dt, t \in I$$

### Symétries et périodicité

**Propriété :** Soit $a \in \mathbb{R}^*$ et soit $f$ une application continue sur $[-a, a]$.
- Si $f$ est paire, alors $$\int_{-a}^a f(t) dt = 2\int_0^a f(t) dt$$
- Et si $f$ est impaire, $\int_{-a}^a f(t) dt = 0$.

**Théorème de périodicité :** Soit $T \in \mathbb{R}^*$. On suppose que $f$ est une fonction continue et $T$-périodique définie sur $\mathbb{R}$. Alors, pour tout $t_0 \in \mathbb{R}$,
$$\int_t^{t+T} f(t') dt' = \int_0^T f(t') dt'$$

### Intégrale d'une fonction de classe C¹

**Corollaire :** Si $f$ est une application de classe $\mathcal{C}^1$ sur $[a, b]$,
$$\int_a^b f'(t) dt = f(b) - f(a)$$

## Fonctions particulières

### Logarithme et exponentielle

**Définition :** Pour tout $x > 0$, on pose $\ln(x) = \int_1^x \frac{dt}{t}$.

**Propriétés de $\ln$ :**
- Le domaine de définition de $\ln$ est égal à $\mathbb{R}^{*+}$
- Par construction, $\ln$ est dérivable sur $\mathbb{R}^{*+}$ et, pour tout $x \in \mathbb{R}^{*+}$, $$(\ln(x))' = \frac{1}{x}$$
- Ainsi, $\ln$ est strictement croissante et $\ln(1) = 0$
- Relation fonctionnelle : Pour tout $x, y \in \mathbb{R}^{*+}$, $\ln(xy) = \ln x + \ln y$
- Limites : $\ln(x) \to +\infty$ quand $x \to +\infty$, $\ln(x) \to -\infty$ quand $x \to 0^+$
- $\ln$ est un $\mathcal{C}^\infty$-diffeomorphisme de $\mathbb{R}^{*+}$ dans $\mathbb{R}$

**Définition :** La bijection réciproque de la bijection $\ln|_{\mathbb{R}^{*+}}$ est notée $\exp$.
$\exp$ est un $\mathcal{C}^\infty$ diffeomorphisme de $\mathbb{R}$ dans $\mathbb{R}^{*+}$. Pour tout $x \in \mathbb{R}^{*+}$, $\exp(\ln x) = x$ et, pour tout $x \in \mathbb{R}$, $\ln(\exp(x)) = x$.

**Propriétés de $\exp$ :**
- $\exp(1) = e$ (nombre de Neper, $e \approx 2,71828183 \pm 10^{-8}$)
- $$(\exp(x))' = \exp(x)$$
- Pour tout $x, y \in \mathbb{R}$, $\exp(x + y) = \exp(x)\exp(y)$
- Pour tout $n \in \mathbb{N}$, $\exp^{(n)} = e^n$ (par récurrence)
- Pour tout $n \in \mathbb{Z}$, $\exp(n) = e^n$
- En cohérence avec cette dernière propriété, on note le plus souvent pour tout $x \in \mathbb{R}$, $\exp(x) = e^x$

**Propriétés combinées de $\ln$ et $x \mapsto e^x$ :**

*Fonction logarithme :* Pour tout $x, y \in \mathbb{R}^{*+}$ et $n \in \mathbb{Z}$,
- $\ln(xy) = \ln x + \ln y$
- $\ln(1) = 0$ et $\ln(e) = 1$
- $\ln(\frac{1}{x}) = -\ln x$
- $\ln(\frac{x}{y}) = \ln x - \ln y$
- $\ln(x^n) = n\ln x$
- $\ln$ est définie sur $\mathbb{R}^{*+}$, elle est strictement croissante
- $\lim_{t \to 0} \ln(t) = -\infty$, $\lim_{t \to +\infty} \ln(t) = +\infty$
- $\lim_{t \to +\infty} \frac{\ln t}{t} = 0$

*Fonction exponentielle :* Pour tout $x, y \in \mathbb{R}$ et $n \in \mathbb{Z}$,
- $e^{x+y} = e^x e^y$
- $e^0 = 1$ et $e^1 = e$
- $e^x > 0$
- $e^{-x} = \frac{1}{e^x}$
- $e^{x-y} = \frac{e^x}{e^y}$
- $e^{nx} = (e^x)^n$
- $\exp$ est définie sur $\mathbb{R}$, elle est strictement croissante
- $\lim_{t \to -\infty} e^t = 0$, $\lim_{t \to +\infty} e^t = +\infty$

### Logarithmes et exponentielles en base $a$

**Définition :** Soit $a \in \mathbb{R}^{*+} \setminus \{1\}$. Le logarithme en base $a$ est l'application notée $\ln_a$ définie par :
$$\forall x \in \mathbb{R}^{*+}, \ln_a(x) = \frac{\ln x}{\ln a}$$

**Remarque :** Pour tout $x > 0$, $$(\ln_a(x))' = \frac{1}{x \ln a}$$

Le logarithme en base 10, souvent noté $\log$, est utilisé en chimie (pH) et en acoustique (dB). Le logarithme en base 2 est utilisé en informatique.

**Définition :** Soit $a \in \mathbb{R}^{*+}$. On définit par $a^n = e^{n\ln a}$ pour tout $n \in \mathbb{Z}$. On convient de noter, pour tout $x \in \mathbb{R}$, $$a^x = e^{x\ln a} = \exp_a(x)$$ : c'est la fonction "exponentielle en base $a$".

**Remarque :** Pour tout $x \in \mathbb{R}$, $$(a^x)' = (\ln a)a^x$$

**Propriété :** Soit $a \in \mathbb{R}^{*+} \setminus \{1\}$. Les fonctions $\ln_a$ et $x \mapsto a^x$ sont des bijections, réciproques l'une de l'autre :
$$\forall x \in \mathbb{R}, \ln_a(a^x) = x \quad \text{et} \quad \forall x \in \mathbb{R}^{*+}, a^{\ln_a x} = x$$

**Propriétés des fonctions $\ln_a$ et $x \mapsto a^x$ :**

*Fonction logarithme en base $a \in \mathbb{R}^{*+} \setminus \{1\}$ :* Pour tout $x, y \in \mathbb{R}^{*+}$ et $b \in \mathbb{R}$,
- $\ln_a(xy) = \ln_a x + \ln_a y$
- $\ln_a(1) = 0$ et $\ln_a(a) = 1$
- $\ln_a(\frac{1}{x}) = -\ln_a x$
- $\ln_a(\frac{x}{y}) = \ln_a x - \ln_a y$
- $\ln_a(x^b) = b\ln_a x$

*Fonction exponentielle en base $a$ :* Pour tout $x, y \in \mathbb{R}$,
- $a^{x+y} = a^x a^y$
- $a^0 = 1$ et $a^1 = a$
- $a^x > 0$
- $a^{-x} = \frac{1}{a^x}$
- $a^{x-y} = \frac{a^x}{a^y}$
- Pour tout $b \in \mathbb{R}$, $a^{bx} = (a^x)^b$
- Pour tout $b > 0$, $a^x b^x = (ab)^x$

### Fonctions puissance

**Définition :** Un monôme de degré $n \in \mathbb{N}$ est une application de la forme $x \mapsto ax^n$, où $a$ est un paramètre réel. Cette application est définie sur $\mathbb{R}$. Une fonction polynomiale est une somme finie de monômes.

**Définition :** Soit $\alpha \in \mathbb{R}$. La fonction puissance d'exposant $\alpha$ est l'application $x \mapsto x^\alpha = e^{\alpha\ln x}$. Elle est définie sur $\mathbb{R}^{*+}$. Lorsque $\alpha \in \mathbb{Z}$, cette application coïncide avec les applications précédentes sur $\mathbb{R}^{*+}$.

**Convention :** Pour tout $b \in \mathbb{R}^{*+}$, $0^b = 0$ et $0^0 = 1$. C'est cohérent avec le fait que, pour $b > 0$ fixé, $x^b \to 0$ et que $\frac{x}{x} \to 1$ lorsque $x \to 0$.

### Fonctions trigonométriques réciproques

**Fonction arcsin :** L'application $\sin : [-\frac{\pi}{2}, \frac{\pi}{2}] \to [-1, 1]$ est surjective, continue et strictement croissante. On note $\arcsin$ son application réciproque, de $[-1, 1]$ dans $[-\frac{\pi}{2}, \frac{\pi}{2}]$. Elle est continue, impaire et strictement croissante sur $[-1, 1]$.

Pour tout $t \in ]-\frac{\pi}{2}, \frac{\pi}{2}[$, $\sin'(t) = \cos(t) \neq 0$, et $\sin$ est $\mathcal{C}^\infty$, donc $\sin$ est un $\mathcal{C}^\infty$-diffeomorphisme de $]-\frac{\pi}{2}, \frac{\pi}{2}[$ sur $]-1, 1[$.

Pour tout $x \in ]-1, 1[$, $$(\arcsin)'(x) = \frac{1}{\sqrt{1-x^2}}$$
$\arcsin$ n'est pas dérivable en $1$ et $-1$. Sa restriction à $]-1, 1[$ est de classe $\mathcal{C}^\infty$.

**Fonction arccos :** L'application $\cos : [0, \pi] \to [-1, 1]$ est surjective, continue et strictement décroissante. On note $\arccos$ son application réciproque, de $[-1, 1]$ dans $[0, \pi]$. Elle est continue et strictement décroissante sur $[-1, 1]$.

Pour tout $t \in ]0, \pi[$, $\cos'(t) = -\sin(t) \neq 0$, et $\cos$ est $\mathcal{C}^\infty$, donc $\cos$ est un $\mathcal{C}^\infty$-diffeomorphisme de $]0, \pi[$ sur $]-1, 1[$, dont $\arccos$ est le $\mathcal{C}^\infty$ diffeomorphisme réciproque.

Pour tout $x \in ]-1, 1[$, $$(\arccos)'(x) = -\frac{1}{\sqrt{1-x^2}}$$
$\arccos$ n'est pas dérivable en $1$ et $-1$. Sa restriction à $]-1, 1[$ est de classe $\mathcal{C}^\infty$.

**Fonction arctan :** L'application $\tan : ]-\frac{\pi}{2}, \frac{\pi}{2}[ \to \mathbb{R}$ est surjective, continue et strictement croissante. On note $\arctan$ son application réciproque, de $\mathbb{R}$ dans $]-\frac{\pi}{2}, \frac{\pi}{2}[$. Elle est continue, impaire et strictement croissante sur $\mathbb{R}$.

Pour tout $t \in ]-\frac{\pi}{2}, \frac{\pi}{2}[$, $\tan'(t) = 1 + \tan^2 t \neq 0$, et $\tan$ est $\mathcal{C}^\infty$, donc $\tan$ est un $\mathcal{C}^\infty$-diffeomorphisme de $]-\frac{\pi}{2}, \frac{\pi}{2}[$ sur $\mathbb{R}$, dont $\arctan$ est le $\mathcal{C}^\infty$ diffeomorphisme réciproque.

Pour tout $x \in \mathbb{R}$, $$(\arctan)'(x) = \frac{1}{1+x^2}$$

**Fonctions trigonométriques hyperboliques :**
- **Cosinus hyperbolique :** $\forall x \in \mathbb{R}, \mathrm{ch}(x) = \frac{e^x + e^{-x}}{2}$
- **Sinus hyperbolique :** $\forall x \in \mathbb{R}, \mathrm{sh}(x) = \frac{e^x - e^{-x}}{2}$
- **Tangente hyperbolique :** $\forall x \in \mathbb{R}, \mathrm{th}(x) = \frac{\mathrm{sh}(x)}{\mathrm{ch}(x)} = \frac{e^{2x} - 1}{e^{2x} + 1}$

**Propriétés :** Les fonctions $\mathrm{sh}$, $\mathrm{ch}$ sont de classe $\mathcal{C}^\infty$ sur $\mathbb{R}$ et :
- $\mathrm{ch}' = \mathrm{sh}$
- $\mathrm{sh}' = \mathrm{ch}$
- $\forall x \in \mathbb{R}, \mathrm{th}'(x) = 1 - \mathrm{th}^2(x) = \frac{1}{\mathrm{ch}^2(x)}$

**Formule fondamentale :** $\forall x \in \mathbb{R}, \mathrm{ch}^2(x) - \mathrm{sh}^2(x) = 1$.

**Fonction argsh :** $\mathrm{sh}$ est un $\mathcal{C}^\infty$-diffeomorphisme de $\mathbb{R}$ dans $\mathbb{R}$, dont le diffeomorphisme réciproque est noté $\mathrm{argsh}$ ("argument sinus hyperbolique"). Ainsi $\mathrm{argsh}$ est une application $\mathcal{C}^\infty$, impaire, strictement croissante.
Pour tout $x \in \mathbb{R}$, $$(\mathrm{argsh})'(x) = \frac{1}{\sqrt{1+x^2}}$$

**Fonction argch :** L'application $\mathrm{ch}$ est une bijection continue strictement croissante de $\mathbb{R}^+$ dans $[1, +\infty[$. Son application réciproque est notée $\mathrm{argch}$. C'est une bijection continue strictement croissante de $[1, +\infty[$ dans $\mathbb{R}^+$.
$\mathrm{ch}$ est un $\mathcal{C}^\infty$-diffeomorphisme de $\mathbb{R}^{*+}$ dans $]1, +\infty[$, donc $\mathrm{argch}$ est $\mathcal{C}^\infty$ sur $]1, +\infty[$.
Pour tout $x \in ]1, +\infty[$, $$(\mathrm{argch})'(x) = \frac{1}{\sqrt{x^2-1}}$$

**Fonction argth :** $\mathrm{th}$ est un $\mathcal{C}^\infty$-diffeomorphisme de $\mathbb{R}$ dans $]-1, 1[$, dont le diffeomorphisme réciproque est noté $\mathrm{argth}$. Ainsi $\mathrm{argth}$ est une application $\mathcal{C}^\infty$, impaire, strictement croissante de $]-1, 1[$ dans $\mathbb{R}$.
Pour tout $x \in ]-1, 1[$, $$(\mathrm{argth})'(x) = \frac{1}{1-x^2}$$

## Théorèmes d'analyse

**Théorème de la limite monotone :** On pose $\overline{\mathbb{R}} = \mathbb{R} \cup \{+\infty, -\infty\}$. Soient $m, M \in \overline{\mathbb{R}}$ avec $m < M$. Notons $I = ]m, M[$. Soit $f$ une application de $I$ dans $\mathbb{R}$ que l'on suppose monotone. Alors la quantité $f(x)$ possède une limite dans $\overline{\mathbb{R}}$, lorsque $x$ tend vers $m$ (resp : $M$).

**Théorème de la bijection :** Soit $f$ une application définie sur un intervalle $I$ et à valeurs dans $\mathbb{R}$. On suppose que $f$ est continue sur $I$. Alors $f$ est une bijection de $I$ dans $f(I)$ si et seulement si $f$ est strictement monotone. Dans ce cas, $f(I)$ est un intervalle et l'application réciproque $f^{-1}$ est une application également continue, strictement monotone, de même sens de variation que $f$, allant de $f(I)$ dans $I$.

**Remarque :** Il est élémentaire de démontrer que, si $f$ est strictement monotone, alors $f$ est une bijection de $I$ dans $f(I)$ et que son application réciproque $f^{-1}$ est également monotone strictement, de même sens de variation que $f$. Les autres affirmations de cet énoncé sont moins immédiates.

**Définition :** Soit $f$ une application définie sur un intervalle $I$ et à valeurs dans un autre intervalle $J$ de $\mathbb{R}$. Soit $n \in \mathbb{N}^* \cup \{\infty\}$. On dit que $f$ est un $\mathcal{C}^n$-diffeomorphisme si et seulement si $f$ est une bijection de $I$ sur $J$ et si $f$ et $f^{-1}$ sont toutes deux de classe $\mathcal{C}^n$.

**Caractérisation d'un diffeomorphisme :** Soit $f$ une application définie sur un intervalle $I$ et à valeurs dans $\mathbb{R}$. Soit $n \in \mathbb{N}^* \cup \{\infty\}$. $f$ est un $\mathcal{C}^n$-diffeomorphisme de $I$ dans $f(I)$ si et seulement si $f$ est de classe $\mathcal{C}^n$ et si, pour tout $x \in I$, $f'(x) \neq 0$.

**Remarque :** C'est cohérent avec la formule : $(f^{-1})'(f(x)) = \frac{1}{f'(x)}$.
