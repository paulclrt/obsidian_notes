# Skill : format obligatoire des flashcards

## Portée

Cette consigne définit uniquement le format d'une carte destinée au logiciel de flashcards. Elle ne définit ni le contenu scientifique, ni le niveau, ni le style pédagogique.

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

## Contrôle final avant écriture

Vérifier systématiquement que :

- chaque carte a exactement un `?` puis un `**Réponse:**` dans cet ordre ;
- une ligne vide sépare chaque paire de cartes ;
- aucune ligne vide n'apparaît à l'intérieur d'une carte ;
- chaque expression LaTeX inline est écrite avec `$...$` ;
- les numéros de cartes sont séquentiels dans chaque fichier.
