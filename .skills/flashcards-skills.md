# Skill : format et contenu des flashcards

## Portée

Cette consigne définit le format d'une carte destinée au logiciel de flashcards, ainsi que la méthode de sélection du contenu (niveau, équilibre, style). Elle ne remplace jamais la demande de l'utilisateur, qui prime sur tout le reste.

## Structure exacte d'une carte

Chaque carte doit respecter exactement le modèle suivant :

```markdown
## N. Titre de la carte
Question, sur une ou plusieurs lignes.
?
**Réponse:**
Réponse, sur une ou plusieurs lignes.
```

Règles impératives :

- Le titre est toujours une ligne de la forme `## N. Titre`, avec un numéro séquentiel dans le fichier.
- Le `?` est seul sur sa ligne, immédiatement après la dernière ligne de la question.
- `**Réponse:**` est seul sur la ligne immédiatement après le `?`.
- La réponse commence sur la ligne immédiatement après `**Réponse:**`.
- Il n'y a jamais de ligne vide à l'intérieur d'une carte : ni avant le `?`, ni avant ou après `**Réponse:**`, ni entre deux lignes de réponse.

Le libellé de réponse suit la langue du jeu de cartes : `**Réponse:**` en français, `**Answer:**` en anglais. Le format structurel (question, `?`, libellé, réponse) reste identique.

## Séparation obligatoire entre les cartes

Une et une seule ligne vide sépare deux cartes.

```markdown
Réponse de la carte précédente.

## 2. Titre de la carte suivante
Question suivante.
?
**Réponse:**
Réponse suivante.
```

Cette ligne vide fait partie du séparateur entre cartes ; elle ne doit jamais être placée à l'intérieur d'une carte.

## Mathématiques et LaTeX

Toute expression mathématique inline doit être encadrée par des signes dollar : `$...$`.

Correct :

```markdown
Si $f:E\to F$ est bijective, alors $f^{-1}$ existe.
```

Incorrect :

```markdown
Si \(f:E\to F\) est bijective, alors \(f^{-1}\) existe.
```

Ne pas employer `\(` ni `\)` pour les expressions inline. Les symboles, variables et formules mathématiques doivent être placés dans `$...$`, sans parenthèses inutiles à l'intérieur des dollars.

## Contenu sur plusieurs lignes et blocs de code

Une question ou une réponse peut contenir plusieurs lignes, une liste ou un bloc de code. Ces lignes restent dans la même carte et ne doivent pas être séparées par une ligne vide.

````markdown
## 1. Exemple de code
Que fait ce code ?
```python
x = 1
```
?
**Réponse:**
Il affecte la valeur $1$ à `x`.
```
````

## Les deux niveaux de cartes

Chaque jeu de cartes s'appuie sur une note de cours et contient deux niveaux de cartes, équilibrés entre eux.

### Niveau 1 — notions atomiques / fondamentales

- Une seule notion par carte : définition, syntaxe, règle, sémantique clé, piège.
- Le « vocabulaire et la grammaire » du sujet, ce qui doit être su par cœur.
- Questions de reconnaissance : « qu'est-ce que… », « quelle est la différence entre… », « que fait ce code… ».
- Ne jamais ré-expliquer ce que tout le monde sait déjà (ex. « qu'est-ce qu'une variable »), sauf si la notion a un aspect non trivial (ex. l'immutabilité par défaut en Rust).
- Privilégier les concepts profonds et les règles qui se comprennent mal si on ne les a pas en tête.

### Niveau 2 — cas d'usage avancés / prêts à coder

- Une carte combine plusieurs notions, comme dans un vrai exemple du quotidien.
- La question est une petite tâche concrète : « écris… », « étant donné X, produis Y… », « implémente… », « esquisse… ».
- La réponse est du code complet et exécutable, ou une procédure précise et vérifiable.
- Objectif : rendre quelqu'un capable de committer du code réel, pas seulement de réciter.
- Exemples utiles : lire un fichier en gérant les erreurs, remplir un `CMakeLists.txt` complet avec tests, mocker une interface dans un test, compter des fréquences, paralléliser avec des threads.

### Équilibre

- Pas « beaucoup de niveau 1 et quelques niveau 2 » : l'équilibre est recherché.
- Assez de niveau 2 pour être opérationnel (prêt à coder), assez de niveau 1 pour posséder les notions profondes.
- Pas de niveau 1 qui ré-explique l'évident, pas de niveau 2 purement exotique sans usage réel.
- La qualité prime : pas de volume artificiel.

## Contrôle final avant écriture

Vérifier systématiquement que :

- chaque carte a exactement un `?` puis un `**Réponse:**` (ou `**Answer:**`) dans cet ordre ;
- une ligne vide sépare chaque paire de cartes ;
- aucune ligne vide n'apparaît à l'intérieur d'une carte ;
- chaque expression LaTeX inline est écrite avec `$...$` ;
- les numéros de cartes sont séquentiels dans chaque fichier ;
- le mélange niveau 1 / niveau 2 est équilibré et fidèle à la note source.
