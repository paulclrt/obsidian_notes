#flashcards/maths/prépa/premiere_annee/cours/12_calcul_asymptotique/12_preponderance_domination


## Notion de domination


Définir la notion de domination
?
Soit:
$$
f:A\longmapsto F \quad \quad and \quad \quad g:A\longmapsto G
$$
On dit que $f$ est prédominée par $g$ au voisinage de $a$ ssi:
$$
\exists V \in \mathcal{V}(a)\quad \exists C \in \mathbb{R}_+^* \quad \forall x \in V\cap A
$$
$$
\|f(x)\|_F \leq C\|g(x)\|_G
$$
On note cela
$$
f(x) = \mathbf{O}_{\substack{x\to a \\ x \in A}} (g(x)) \quad ou \quad f = \mathbf{O}(g)
$$
Et on dit que *"f est dominée par g en a"*

## Propriétés de la domination


Citez les propriétés de la domination pour:
- La composition
- La somme
- Le produit
- La puissance/dérivé ?
?
Composition:     $\mathbf{O}(\mathbf{O}(f)) = \mathbf{O}(f)$
Addition:          $\mathbf{O}(f) + \mathbf{O}(f) = \mathbf{O}(f)$
Produit:            $\mathbf{O}(\varphi) . \mathbf{O}(f) =  \mathbf{O}(\varphi . f)$    avec           $\varphi : A \longmapsto \mathbb{K}$    (fonction scalaire)
Puissance:         $\mathbf{O}(f)^\alpha = \mathbf{O}(f^\alpha)$


## Domination et limite vers 0


Que ce passe-t-il si: $F$ et $G$ deux espaces vectoriel normés
$$
f : A \longmapsto F \quad g:A\longmapsto G
$$
deux applications avec: $f(x) = \mathbf{O}(g(x))$ et $g(x)\rightarrow_{\substack{x\rightarrow a \\ a \in A}} 0$    ?
?
$$
f(x)\rightarrow 0
$$
quand $x\rightarrow a$ et $a \in A$

## Domination et borne pour $\mathbf{O}$


Quand est-ce que $f = \mathbf{O}(g)$ ?
?
Si et seulement si:
$$
x \longmapsto \frac{\|f(x)\|}{\|g(x)\|} \quad est\ bornée\ au\ voisinage\ de\ a
$$


## Notion de prépondérance


Définir la notion de domination
?
Soit:
$$
f:A\longmapsto F \quad \quad and \quad \quad g:A\longmapsto G
$$
On dit que $f$ est négligeable devant $g$ au voisinage de $a$ ssi:
$$
\forall \epsilon \in \mathbb{R}_+^* \quad \exists V \in \mathcal{V}(a) \quad \forall x \in V\cap A
$$
$$
\|f(x)\|_F \leq \epsilon\|g(x)\|_G
$$
On note cela
$$
f(x) = o(g(x)) \quad ou \quad f = o(g)
$$
Et on dit que *"f est négligeable devant g en a"*

## Propriétés de la prépondérance


Rappeler les propriétés suivantes pour la prépondérance:
- relation avec $\mathbf{O}$
- composition avec $o$ et $\mathbf{O}$
- composition avec $o$
- somme avec $o$
- produit avec une fonction scalaire
- puissance/dérivé ?
?
Relation avec $\mathbf{O}$:                         $o(f) = \mathbf{O}(f)$    (valable que dans un sens)
Composition avec $o$ et $\mathbf{O}$:              $o(\mathbf{O}(f)) = o(f)$ et $\mathbf{O}(o(f)) = o(f)$
composition avec $o$:                      $o(o(f)) = o(f)$
Somme avec $o$:                            $o(f) + o(f) = o(f)$
Produit avec une fonction scalaire:  $o(f) + o(\varphi) = o(\varphi . f)$ et $\mathbf{O}(\varphi).o(f) = o(\varphi . f)$
Puissance/dérivé:                         $o(f)^\alpha = o(f^\alpha)$

## Prépondérance et $o(1)$


Quand est-ce que:
$f = o(1)$
?
$f(x)\longmapsto 0$ pour $x \rightarrow a$


## Egaité de prépondérance


Que dire sur l'égalité et la prépondérance ?
?
Elle n'est plus symétrique:
$f = o(h)$ et $g = o(h)$ ne veut pas dire que $f = g$
<!--SR:!2026-09-21,4,270-->

## Domination et borne pour prépondérance


Quand est-ce que $f = o(g)$ ?
?
Si et seulement si:
$$
\frac{\|f(x)\|}{\|g(x)\|} \longmapsto 0
$$

## Théorème des croissances comparées


Donner le théorème des croissances comparées pour $ln^\alpha(n)$, $n^\beta$, $a^n$, $n!$ avec $\alpha,\beta,\gamma \in \mathbb{R}_+^*$ et $a > 1$ :
?
1. Les suites $\ln^\alpha(n)$, $n^\beta$, $a^n$ et $n!$ tendent vers $+\infty$ et chacune est négligeable devant les suivantes.
2. Au voisinage de $+\infty$, les fonctions $\ln^\alpha x$, $x^\beta$ et $e^{\gamma x}$ tendent vers $+\infty$ et chacune est négligeable devant les suivantes.
3. Au voisinage de $0^+$, $\vert{}\ln x\vert{}^\alpha = o\left(\frac{1}{x^\beta}\right)$.
4. Au voisinage de $-\infty$, $e^{\gamma x} = o\left(\frac{1}{\vert{}x\vert{}^\beta}\right)$.


