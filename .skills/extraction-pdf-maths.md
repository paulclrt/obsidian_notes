# Skill: Extraction de contenu PDF pour notes mathématiques

## Description
Skill spécialisé pour extraire systématiquement les notations, définitions, propriétés et remarques à partir de documents PDF académiques (mathématiques, prépa MPSI/MP), en excluant démonstrations et exemples.

## Utilisation
```
/app:extraction_pdf_maths(path_pdfs="chemin/pdf1.pdf chemin/pdf2", format="md", sortie_racine=true)
```

## Workflow d'extraction

### 1. Conversion PDF → texte
- Outils prioritaires : `pdftotext`, `python pdfplumber/pypdf`, `PyMuPDF`
- Vérification de la qualité du texte extrait
- Gestion des encodages (UTF-8 par défaut, fallback sur latin-1)

### 2. Identification des éléments à extraire
**Priorité absolue :**
- Définitions (`Définition.` / « On dit que... » / « Soit... alors... »)
- Propriétés (`Propriété` / Théorèmes avec énoncés complets)
- Notations (`Notation` / « On note... » / conventions)
- Remarques (`Remarque` / « Attention » / « Important »)

**À exclure :**
- Démonstrations (`Démonstration`, « En effet », preuves détaillées)
- Exemples concrets avec calculs spécifiques
- Exercices et problèmes à résoudre
- Représentations graphiques (sauf si notées en texte)
- Numérotation de pages / en-têtes / pieds de page

### 3. Structure du markdown de sortie

**Format type pour chaque section :**
```markdown
# [Nom du chapitre]

## Définitions
- **Terme :** [Énoncé complet avec notation LaTeX]

## Propriétés
- **[Libellé] :** [Propriété complète avec conditions]
  - *Hypothèses :* [conditions nécessaires]
  - *Formulation :* $$[formules en LaTeX]$$

## Remarques
- [Remarque pratique/historique/contexte]
```

**Conventions LaTeX pour Obsidian :**
- Équations linéaires : `$inline$`
- Blocs d'équations : `$$block$$`
- Indices grecs : `\alpha`, `\beta`, `\dots`
- Limites : `\lim_{x \to a}`
- Fractions : `\frac{numérateur}{dénominateur}`
- Racines carrées : `\sqrt{expression}`

### 4. Templates par type de contenu

#### Définitions de fonctions
```markdown
**Définition :** [Nom] est l'application notée [symbole] définie sur [domaine] par :
$$[formule principale]$$
*Propriétés immédiates :*
- [Liste des propriétés essentielles]
```

#### Propriétés de dérivées/intégrales
```markdown
**Propriété :** Pour tout $x$ dans [domaine], avec hypothèses :
$$[dérivée/formule] = [expression]$$
*Conditions :* [préciser le domaine et hypothèses]
```

#### Théorèmes majeurs
```markdown
**Théorème de [nom] :** [Énoncé complet]
- *Hypothèses :* [liste numérotée des conditions]
- *Conclusion :* $$[conclusion avec formules]$$
- *Remarque :* [interprétation ou application]
```

### 5. Post-traitement obligatoire

**Vérifications :**
- [ ] Tous les symboles mathématiques correctement codés en LaTeX
- [ ] Pas de démonstrations incluses
- [ ] Domaines de définition précis pour chaque formule
- [ ] Consistance des notations (f vs f(x), dx vs dt, etc.)
- [ ] Séparation claire entre sections Définitions/Propriétés/Remarques

**Optimisation Obsidian :**
- Utilisation de blocs code pour formules complexes si nécessaire
- Emplacement logique dans la hiérarchie de cours
- Liens croisés suggérés (ex: `[[ln]]`, `[[dérivation]]`)

### 6. Exemples de traitement réussi

**Cas : Dérivées d'ordre supérieur**
- Extraits : Définition de f^(n), classe C^n, formule de dérivée sin/cos n-ième
- Exclu : Preuve par récurrence complète, calculs spécifiques de f(n)(x) pour fonctions particulières

**Cas : Intégration par parties**
- Extraits : Formule générale, exemples de primitives usuelles (ln, arctan)
- Exclu : Calculs détaillés d'intégrales spécifiques, justifications géométriques

### 7. Limitations connues et workarounds

**Limitations :**
- PDF scannés/non texturables → nécessite OCR préalable
- Mathématiques en images → transcription manuelle nécessaire
- Formules complexes avec plusieurs lignes → peut nécessiter reformatage

**Workarounds recommandés :**
- Utiliser `pdfplumber` pour une meilleure extraction LaTeX-native
- Pré-traitement avec `pdftotext -layout` pour préserver la mise en forme
- Vérification visuelle obligatoire des formules critiques

### 8. Bonnes pratiques documentées

✅ Toujours spécifier le domaine de définition après chaque formule
✅ Utiliser « On convient que » pour les conventions explicites
✅ Garder les liens entre définitions et propriétés (ex: f'' défini ⇒ f C²)
✅ Ne pas simplifier excessivement les formules (garder leur forme d'origine)
❌ Jamais inclure les démonstrations même partiellement
❌ Éviter les exemples avec calculs numériques spécifiques

### 9. Métriques de qualité

**Checklist post-extraction :**
- Nombre de définitions extraites : ≥ [target]
- Nombre de propriétés extraites : ≥ [target]
- Ratio formules LaTeX valides : > 95%
- Absence de démonstrations : 100%
- Cohérence des notations : vérifiée

### 10. Intégration dans le workflow académique

**Cas d'usage typique :**
1. Lecture rapide du cours PDF en entier
2. Extraction ciblée uniquement des définitions/propriétés
3. Génération de fiches mémo pour révisions
4. Création de flashcards à partir des remarques importantes
5. Construction automatique d'arbres de connaissances en Obsidian

**Gain de temps estimé :** ~60-70% du temps de lecture initiale pour les cours densifiés

## Méta-info
- **Créé :** 2026-09-26
- **Dernière mise à jour :** 2026-09-26
- **Domaines couverts :** Analyse, dérivation, intégration, fonctions usuelles
- **Niveau :** MPSI/MP prépa française (niveau Licence 1/Maths)
