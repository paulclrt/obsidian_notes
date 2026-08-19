# Skill: Formatage universel de questions/réponses pour flashcards

## Objectif

Formater des cartes de questions/réponses pour un logiciel de flashcards qui utilise les retours à la ligne comme délimiteurs.

Ce skill concerne uniquement le FORMAT.
Il ne définit ni le sujet, ni le niveau, ni le contenu scientifique, ni le style pédagogique.

Il doit être applicable à n'importe quel domaine : informatique, biologie, médecine, histoire, physique, etc.

## Format obligatoire d'une carte

Chaque carte doit suivre exactement cette structure :

## N. Titre de la carte

Question.
```text
contenu éventuel
```
?
**Réponse:**
Réponse.

Le `?` doit être placé sur sa propre ligne, immédiatement après la question et après tout éventuel bloc de code ou contenu associé à la question.

`**Réponse:**` doit être placé sur la ligne immédiatement suivante.

Il ne doit y avoir AUCUNE ligne vide entre :

la question et le `?`

le `?` et `**Réponse:**

`**Réponse:**` et le début de la réponse

les différentes lignes d'un même bloc de réponse

## Règle absolue sur les retours à la ligne

Deux retours à la ligne consécutifs sont interdits à l'intérieur d'une carte.

Interdit :

Question.

?

**Réponse:**

Réponse.

Correct :

Question.
?
**Réponse:**
Réponse.

Interdit :

Question.
```text
contenu
```

?

Correct :

Question.
```text
contenu
```
?
**Réponse:**
Réponse.

Il ne faut jamais créer de paragraphe vide dans une carte.

## Séparation entre les cartes

Les cartes doivent être séparées de manière compatible avec le logiciel.

Ne pa# Skill: Formatage universel de questions/réponses pour flashcards

## Objectif

Formater des cartes de questions/réponses pour un logiciel de flashcards qui utilise les retours à la ligne comme délimiteurs.

Ce skill concerne uniquement le FORMAT.
Il ne définit ni le sujet, ni le niveau, ni le contenu scientifique, ni le style pédagogique.

Il doit être applicable à n'importe quel domaine : informatique, biologie, médecine, histoire, physique, etc.

## Format obligatoire d'une carte

Chaque carte doit suivre exactement cette structure :

## N. Titre de la carte

Question.
```text
contenu éventuel
```
?
**Réponse:**
Réponse.

Le `?` doit être placé sur sa propre ligne, immédiatement après la question et après tout éventuel bloc de code ou contenu associé à la question.

`**Réponse:**` doit être placé sur la ligne immédiatement suivante.

Il ne doit y avoir AUCUNE ligne vide entre :

la question et le `?`

le `?` et `**Réponse:**

`**Réponse:**` et le début de la réponse

les différentes lignes d'un même bloc de réponse

## Règle absolue sur les retours à la ligne

Deux retours à la ligne consécutifs sont interdits à l'intérieur d'une carte.

Interdit :

Question.

?

**Réponse:**

Réponse.

Correct :

Question.
?
**Réponse:**
Réponse.

Interdit :

Question.
```text
contenu
```

?

Correct :

Question.
```text
contenu
```
?
**Réponse:**
Réponse.

Il ne faut jamais créer de paragraphe vide dans une carte.

## Séparation entre les cartes

Les cartes doivent être séparées de manière compatible avec le logiciel.

Ne pas ajouter de lignes vides supplémentaires entre les cartes.

Une carte peut commencer directement après la dernière ligne de la carte précédente :

Réponse de la carte précédente.
## 2. Titre suivant
Question suivante.
?
**Réponse:**
Réponse suivante.

## Titres

Utiliser :

## N. Titre

Le numéro doit être séquentiel si plusieurs cartes sont produites.

Le titre peut contenir du texte, du Markdown inline et des éléments spécifiques au sujet.

Le titre ne doit pas être séparé de la question par une ligne vide.

Correct :

## 1. Nom de la structure

Quelle est sa fonction ?
?
**Réponse:**
...

## Blocs de code

Si la question ou la réponse contient du code, utiliser un bloc Markdown :

```c
int x = 0;
```

Le langage peut être adapté au contenu :

```python
...
```

```text
...
```

etc.

Le bloc de code fait partie de la question ou de la réponse et ne doit pas introduire de ligne vide avant `?`.

Exemple correct :

## 1. Exemple

Que fait ce code ?
```c
int x = 1;
```
?
**Réponse:**
Il initialise `x` à 1.

## Contenu non-code

Le même format doit fonctionner pour des mathématiques, des réactions chimiques, des tableaux, des listes ou tout autre contenu.

Le principe reste toujours :

Question.
contenu éventuel
?
**Réponse:**
Réponse.

Le type de contenu ne change jamais la position du `?`.

## Réponses longues

Une réponse peut contenir plusieurs lignes, mais aucune ligne vide ne doit être utilisée pour créer des paragraphes.

Correct :

**Réponse:**
Première explication.
Deuxième explication.
Troisième explication.

Incorrect :

**Réponse:**
Première explication.

Deuxième explication.

## Listes

Éviter les lignes vides entre les éléments d'une liste.

Correct :

**Réponse:**
1. Premier élément
2. Deuxième élément
3. Troisième élément

## Règle sur le `?`

Le `?` est le séparateur entre la question et la réponse.

Il doit apparaître exactement une fois à cet emplacement.

Ne pas écrire :

Question ? 
**Réponse:**

Ne pas écrire :

Question
?

**Réponse:**

Écrire :

Question
?
**Réponse:**

Si la question contient déjà un point d'interrogation grammatical, conserver malgré tout le séparateur `?` sur une ligne distincte.

Exemple :

Pourquoi cette structure est-elle importante ?
?
**Réponse:**
...

## Règle sur `**Réponse:**`

Toujours utiliser exactement :

**Réponse:**

Ne pas utiliser :

Réponse :

**Answer:**

**Answer:** 

ou d'autres variantes.

`**Réponse:**` doit suivre immédiatement la ligne `?`.

## Pas de bloc de code global

Ne jamais entourer toute la carte ou toute la sortie dans un unique bloc de code.

Les blocs de code doivent uniquement servir aux exemples ou contenus qui nécessitent réellement un bloc monospace.

## Pas de métadonnées supplémentaires

Ne pas ajouter de marqueurs, identifiants, attributs HTML, IDs ou commentaires techniques aux blocs de code ou aux cartes.

## Principe de compatibilité

Le format doit rester volontairement simple.

La structure minimale fiable est :

## N. Titre
Question
?
**Réponse:**
Réponse

Toute sophistication de mise en page qui introduit des lignes vides doit être évitée.

## Vérification avant sortie

Avant de produire les cartes, vérifier systématiquement :

Chaque carte commence par `## N.`.

Chaque question est suivie par une ligne `?`.

La ligne `?` est immédiatement suivie par `**Réponse:**`.

Il n'existe aucun double retour à la ligne à l'intérieur d'une carte.

Aucune ligne vide ne sépare `**Réponse:**` du texte de réponse.

Aucune ligne vide ne sépare les lignes d'une réponse.

Les blocs de code ne contiennent pas de métadonnées artificielles.

Le format ne dépend d'aucun domaine particulier.

## Exemple générique

## 1. Exemple de question

Quelle est la fonction de cette structure ?
```text
Exemple
```
?
**Réponse:**
Cette structure permet de représenter l'information décrite dans la question.s ajouter de lignes vides supplémentaires entre les cartes.

Une carte peut commencer directement après la dernière ligne de la carte précédente :

Réponse de la carte précédente.
## 2. Titre suivant
Question suivante.
?
**Réponse:**
Réponse suivante.

## Titres

Utiliser :

## N. Titre

Le numéro doit être séquentiel si plusieurs cartes sont produites.

Le titre peut contenir du texte, du Markdown inline et des éléments spécifiques au sujet.

Le titre ne doit pas être séparé de la question par une ligne vide.

Correct :

## 1. Nom de la structure

Quelle est sa fonction ?
?
**Réponse:**
...

## Blocs de code

Si la question ou la réponse contient du code, utiliser un bloc Markdown :

```c
int x = 0;
```

Le langage peut être adapté au contenu :

```python
...
```

```text
...
```

etc.

Le bloc de code fait partie de la question ou de la réponse et ne doit pas introduire de ligne vide avant `?`.

Exemple correct :

## 1. Exemple

Que fait ce code ?
```c
int x = 1;
```
?
**Réponse:**
Il initialise `x` à 1.

## Contenu non-code

Le même format doit fonctionner pour des mathématiques, des réactions chimiques, des tableaux, des listes ou tout autre contenu.

Le principe reste toujours :

Question.
contenu éventuel
?
**Réponse:**
Réponse.

Le type de contenu ne change jamais la position du `?`.

## Réponses longues

Une réponse peut contenir plusieurs lignes, mais aucune ligne vide ne doit être utilisée pour créer des paragraphes.

Correct :

**Réponse:**
Première explication.
Deuxième explication.
Troisième explication.

Incorrect :

**Réponse:**
Première explication.

Deuxième explication.

## Listes

Éviter les lignes vides entre les éléments d'une liste.

Correct :

**Réponse:**
1. Premier élément
2. Deuxième élément
3. Troisième élément

## Règle sur le `?`

Le `?` est le séparateur entre la question et la réponse.

Il doit apparaître exactement une fois à cet emplacement.

Ne pas écrire :

Question ? 
**Réponse:**

Ne pas écrire :

Question
?

**Réponse:**

Écrire :

Question
?
**Réponse:**

Si la question contient déjà un point d'interrogation grammatical, conserver malgré tout le séparateur `?` sur une ligne distincte.

Exemple :

Pourquoi cette structure est-elle importante ?
?
**Réponse:**
...

## Règle sur `**Réponse:**`

Toujours utiliser exactement :

**Réponse:**

Ne pas utiliser :

Réponse :

**Answer:**

**Answer:** 

ou d'autres variantes.

`**Réponse:**` doit suivre immédiatement la ligne `?`.

## Pas de bloc de code global

Ne jamais entourer toute la carte ou toute la sortie dans un unique bloc de code.

Les blocs de code doivent uniquement servir aux exemples ou contenus qui nécessitent réellement un bloc monospace.

## Pas de métadonnées supplémentaires

Ne pas ajouter de marqueurs, identifiants, attributs HTML, IDs ou commentaires techniques aux blocs de code ou aux cartes.

## Principe de compatibilité

Le format doit rester volontairement simple.

La structure minimale fiable est :

## N. Titre
Question
?
**Réponse:**
Réponse

Toute sophistication de mise en page qui introduit des lignes vides doit être évitée.

## Vérification avant sortie

Avant de produire les cartes, vérifier systématiquement :

Chaque carte commence par `## N.`.

Chaque question est suivie par une ligne `?`.

La ligne `?` est immédiatement suivie par `**Réponse:**`.

Il n'existe aucun double retour à la ligne à l'intérieur d'une carte.

Aucune ligne vide ne sépare `**Réponse:**` du texte de réponse.

Aucune ligne vide ne sépare les lignes d'une réponse.

Les blocs de code ne contiennent pas de métadonnées artificielles.

Le format ne dépend d'aucun domaine particulier.

## Exemple générique

## 1. Exemple de question

Quelle est la fonction de cette structure ?
```text
Exemple
```
?
**Réponse:**
Cette structure permet de représenter l'information décrite dans la question.