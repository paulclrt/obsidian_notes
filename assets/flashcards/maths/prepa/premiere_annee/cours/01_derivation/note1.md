# Dérivation

## Définitions

**Dérivée première :** Si $f$ est définie sur un intervalle $I$, on note $f'$ la dérivée de $f$. Pour tout $x \in I$, $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$.

**Deux fois dérivable :** $f$ est deux fois dérivable sur $I$ lorsque $f'$ est dérivable en tout point de $I$. La dérivée de la dérivée de $f$ est notée $f''$. On l'appelle la dérivée seconde de $f$.

**Dérivée n-ième :** Pour $n \in \mathbb{N}$, par récurrence, la dérivée n-ième de $f$ lorsqu'elle est définie est la dérivée $\frac{d^n}{dx^n}$ de la dérivée $(n-1)$-ième. On la note $f^{(n)}$ ou bien $x \mapsto f^{(n)}(x)$.

**De classe Cⁿ :** On dit que $f$ est de classe $\mathcal{C}^n$ sur $I$ lorsque $f$ est $n$ fois dérivable sur $I$ et que $f^{(n)}$ est continue.

**De classe C∞ :** On dit que $f$ est de classe $\mathcal{C}^\infty$ sur $I$ lorsque, pour tout $n \in \mathbb{N}$, $f$ est $\mathcal{C}^n$ sur $I$.

**Convention :** On convient que $f^{(0)} = f$, pour toute application $f$ de $\mathbb{R}$ dans $\mathbb{R}$.

## Propriétés

### Dérivées de fonctions usuelles

- $(x^n)' = nx^{n-1}$ pour $n \in \mathbb{Z}^*$
- $(\sin x)' = \cos x$
- $(\cos x)' = -\sin x$
- $(e^x)' = e^x$
- $(\ln x)' = \frac{1}{x}$ pour $x \in \mathbb{R}^{*+}$
- $(\arcsin x)' = \frac{1}{\sqrt{1-x^2}}$ pour $x \in ]-1, 1[$
- $(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$ pour $x \in ]-1, 1[$
- $(\arctan x)' = \frac{1}{1+x^2}$
- $(|x|)' = \frac{x}{|x|}$ pour $x \neq 0$

### Dérivation et opérations usuelles

Soient $f, g$ deux fonctions dérivables sur un intervalle $I$ et $\lambda \in \mathbb{R}$ :

- **Somme/Produit par une constante :** $(\lambda f)' = \lambda f'$
- **Somme :** $(f + g)' = f' + g'$
- **Produit :** $(fg)' = f'g + fg'$
- **Quotient :** $$(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$$ pour $g \neq 0$

### Formule de dérivation d'une fonction composée

Soit $u$ dérivable sur un intervalle $I$, $v$ dérivable sur l'image $u(I)$ :
$$(v \circ u)'(x) = v'(u(x)) \times u'(x)$$

### Dérivation d'une bijection réciproque

Soit $f$ une bijection de classe $\mathcal{C}^1$ définie sur un intervalle $I$. Soit $g = f^{-1}$ la fonction réciproque définie sur $f(I)$ :
$$(f^{-1})'(y) = \frac{1}{f'(x)}$$ où $y = f(x)$.

### Dérivation d'une fraction rationnelle

Soient $P, Q$ deux polynômes. Si $R = \frac{P}{Q}$ avec $Q \neq 0$, alors :
$$(\frac{P}{Q})' = \frac{P'Q - PQ'}{Q^2}$$

## Remarques

- On utilise une notion d'aire mal définie pour l'intégration. C'est une définition intuitive et informelle.
- La possession et la maîtrise d'une calculatrice graphique est un atout pour l'étude de fonctions.
- Les logarithmes ont été inventés par Neper (en 1614, mais pas sous forme intégrale : il faut attendre 1666 pour cela) afin de ramener le calcul d'un produit $xy$ à celui d'une somme : $\ln x + \ln y$. Cependant, pour terminer le calcul, il est nécessaire de connaître la bijection réciproque de la bijection $\ln$.

