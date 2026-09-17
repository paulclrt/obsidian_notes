#flashcards/maths/prépa/premiere_annee/cours/12_calcul_asymptotique/12_relation_eq

## Définition 

Quand est-ce que qu'une relation d'équivalence ?
?
$f$ est équivalente à $g$ au voisinage de $a$ ssi:
$$
f(x) - g(x) = o(g)
$$
On écrit alors:
$$
f \sim_ {\substack{x\rightarrow a \\ a \in A}} g \iff f = g + o(g)
$$
BONUS: quelques explicaiton supplémentaires...
l'expression $f-g = o(g)$ est un peu confuse comme ça. En fait c'est bien plus claire si on réécrit la définition de la prépondérance. $\forall x \in V \cap A \quad \|f(x)\|_F \leq \epsilon \|g(x)\|_G$.
On voit alors mieux que
$$
\|f-g\| \leq \epsilon \|g\|
$$
Ce que l'on a vu est vrai ssi:
$$
\frac{\|f-g\|}{\|g\|} \longmapsto 0 \quad (when\ x\longmapsto a)
$$
(which is obvious because: fallait juste diviser par $\|g\|$ (donc g différent de 0 ofc) vu que par def $\epsilon$ est très petit)

## Relation d'équivaence pour fonction scalaires non nulles

Si f et g sont des fonctions scalaires non nulles. Comment dire quelles sont équivalentes ?
?
$$
\frac{f}g\longmapsto 1 \quad (when\ x\rightarrow a)
$$

## Relation d'équivalence lorsque f tend vers l en a

Soient F un espace vectoriel normé, $f ∈ F(A, F)$ et $l ∈ F$. 
Que ce passe-t-il ?
?
Si $f (x) → l$ et si $l \neq 0$, alors $f (x) ∼ l$.

## Stabilité et défault de stabilité de l'équivalence

Quand est-ce que l'équivalence est stable et instable ?
?
**réponse courte:**

| Stable                                   | Instable                            |
| ---------------------------------------- | ----------------------------------- |
| Multiplication par une fonction scalaire | Composition                         |
|                                          | Addition                            |
|                                          | puissance dépendante de la variable |

- L'équivalence est **stable par la multiplication par une applicaiton scalaire**:
$$
si\ \varphi \sim \psi \quad\ et\ \quad f \sim g \quad\quad alors \quad\quad \varphi.f \sim \psi.g
$$
- Mais elle **n'est pas stable par composition si $\varphi$ ou $\psi$ ne sont pas scalaires** --> exponentiel as ex.
Exemple pour l'instabilité:
si $f$ et $g$ sont à valeur réel:
$$
e^{f(x)} \sim e^{g(x)} \iff (f-g)(x) \rightarrow 0
$$
Ainsi, avec $f(t) = t^2+t$ et $g(t)=t^2$ au voisinage de $+\infty$: $f(t)\sim$g(t)$ mais $e^{f(t)} \nsim e^{g(t)}$ 
En règle général: 
$$
si\ f (x) ∼ g(x),\quad \varphi(f (x)) \nsim \varphi(g(x))
$$
L’´equivalence de fonctions au voisinage d’un point n’est pas stable par composition la gauche. (Mais elle l'est pas la droite --> c'est un changement de variable)
- Elle est aussi **instable par addition**:
$t^2 \sim t^2 + 2t$   et    $-t^2+1 \sim -t^2$    mais si l'on somme les deux: $1 \nsim 2t$ $\square$ 
 Le raisonnement “au voisinage de 0, $sin t ∼ t − \frac{t^3}{6} ∼ t + t^2$, donc sin t − t ∼ t2” n’est pas valable car il utilise la stabilit´e de l’addition, qui est fausse.

## Propriétées de l'équivalence

Citez les propriétées suivantes:
- équivalence des inverses
- Lien entre équivalence et norme
- Voisinage et signe des deux fonctions
- puissance/dérivé
- limite d'une fonction
?
- Si f et g ne s'anullent pas et $f \sim g$ 
- Si $f \sim g$, alors $‖f ‖ ∼ ‖g‖$
- Si $f \sim g$, alors f et g ont le mˆeme signe au voisinage de a au sens strict, c’est-aà-dire que $f (x)$ et $g(x)$ sont tous deux nuls, ou tous deux strictement positifs, ou tous deux strictement négatifs
- Si $f \sim g$ et si $g$ est strictement positive au voisinage de $a$, alors $f^\alpha (x) ∼ g^\alpha (x)$
- Si $f \sim g$ et si $g(x) \longmapsto l$ lorsque $x\rightarrow a\ and\ a \in A$, alors $f (x) \longmapsto l$ en a
BONUS:
Propriété. Soient F et G deux espaces vectoriels normés, f : A −→ F et g : A −→ G deux applications. La condition f = O(g) (respectivement f = o(g), f ∼ g) est vraie si et seulement si elle l’est en rempla¸cant f et g par des applications ´equivalentes
## Changement de variable pour l'équivalence

Expliquer le changeent de variable pour l'équivalence de fonction
?
Si $\phi(t) → a$ et $f (x) \sim g(x)$, alors $f \circ \phi(t) \sim g \circ  \phi(t)$


## Méthodes de calculs d'équivalents

TODO
?
TODO

