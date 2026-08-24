#flashcards/VHDL/simulation_verification
## 1. Rôle d'un testbench
Quel est le rôle d'un testbench VHDL ?
?
**Réponse:**
Il instancie le DUT, génère des stimuli, observe les sorties et vérifie automatiquement le comportement attendu.
Il n'est pas synthétisé.

## 2. DUT
Que signifie DUT dans un testbench ?
?
**Réponse:**
DUT signifie Design Under Test.
C'est l'instance précise du bloc matériel dont on vérifie le comportement.

## 3. Horloge de simulation
Comment génère-t-on couramment une horloge de période `T` dans un testbench ?
?
**Réponse:**
Un processus alterne le signal d'horloge puis attend `T/2` entre deux basculements.
Le processus doit continuer aussi longtemps que le testbench en a besoin.

## 4. `assert`
Comment utiliser `assert` pour vérifier une sortie ?
?
**Réponse:**
Écrire une condition qui doit être vraie, par exemple `assert q_out = '1' report "unexpected output" severity error;`.
Si la condition est fausse, le simulateur rapporte le message et la sévérité.

## 5. Contrôle de fin de test
Comment signaler explicitement la fin d'un testbench ?
?
**Réponse:**
On peut écrire `assert false report "Test done" severity note;` puis `wait;`.
Le `wait` sans condition arrête ce processus et évite qu'il recommence.

## 6. Delta cycles
Pourquoi une sortie peut-elle ne pas être immédiatement visible après une affectation de signal ?
?
**Réponse:**
Les signaux sont mis à jour lors de cycles delta de simulation.
Attendre un delta ou un délai adapté avant de vérifier une valeur issue de plusieurs processus.

## 7. Vérification exhaustive ou dirigée
Quelle différence entre test exhaustif et test dirigé ?
?
**Réponse:**
Un test exhaustif couvre toutes les combinaisons possibles, pratique pour un petit bloc.
Un test dirigé choisit des scénarios représentatifs, limites et erreurs attendues pour un espace d'entrée trop grand.

## 8. Cas limites
Quels cas doivent systématiquement figurer dans un test de bloc numérique ?
?
**Réponse:**
Tester reset, valeurs minimales et maximales, transitions, dépassements éventuels, valeurs invalides et séquences consécutives.
Les cas limites révèlent plus de défauts que les cas moyens.

## 9. Golden model
Qu'est-ce qu'un golden model dans un testbench ?
?
**Réponse:**
C'est un modèle de référence, souvent plus simple ou algorithmique, qui calcule le résultat attendu.
Le testbench compare automatiquement le DUT à cette référence.

## 10. VCD et visualisation
À quoi sert un fichier VCD ?
?
**Réponse:**
Il enregistre l'évolution temporelle des signaux simulés.
On peut l'ouvrir dans GTKWave pour diagnostiquer séquences, latences, resets et violations de protocole.

## 11. Analyse, élaboration, exécution
Quelles sont les trois étapes typiques avec GHDL ?
?
**Réponse:**
L'analyse compile les unités VHDL avec `ghdl -a`.
L'élaboration prépare le top-level avec `ghdl -e`.
L'exécution simule ce top-level avec `ghdl -r`.

## 12. Test reproductible
Qu'est-ce qui rend un test de simulation reproductible ?
?
**Réponse:**
Des stimuli déterministes, des assertions automatiques, une commande documentée et un résultat indépendant de l'interface graphique.
Les waveforms servent au diagnostic, pas au seul oracle de validation.
