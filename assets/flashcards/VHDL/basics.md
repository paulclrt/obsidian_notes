#flashcards/VHDL/basics
## 1. Deux unités de conception
Quels sont les rôles respectifs d'une `entity` et d'une `architecture` en VHDL ?
?
**Réponse:**
L'`entity` définit l'interface : génériques et ports du bloc.
L'`architecture` décrit son implémentation ou son comportement.
<!--SR:!2026-08-28,4,270-->

## 2. Directions de ports
Que signifient les modes `in`, `out`, `inout` et `buffer` d'un port ?
?
**Réponse:**
`in` est lu par le bloc ; `out` est produit par le bloc.
`inout` permet lecture et écriture avec plusieurs pilotes possibles.
`buffer` est un port de sortie relisible en interne, mais un signal interne est aujourd'hui généralement préférable.
<!--SR:!2026-08-27,3,250-->

## 3. Bibliothèques minimales
Pourquoi écrit-on souvent `library ieee; use ieee.std_logic_1164.all;` ?
?
**Réponse:**
La bibliothèque `ieee` fournit les paquets standards.
`std_logic_1164` définit notamment `std_logic`, `std_logic_vector` et les opérateurs logiques associés.
<!--SR:!2026-08-27,3,250-->

## 4. `std_logic` plutôt que `bit`
Pourquoi `std_logic` est-il généralement préférable à `bit` ?
?
**Réponse:**
`bit` ne peut valoir que `'0'` ou `'1'`.
`std_logic` modélise aussi l'inconnu, la haute impédance et les conflits de pilotes, ce qui rend la simulation plus réaliste.
<!--SR:!2026-08-29,3,230-->

## 5. Valeurs importantes de `std_logic`
Que représentent au moins `'0'`, `'1'`, `'U'`, `'X'` et `'Z'` ?
?
**Réponse:**
`'0'` et `'1'` sont les niveaux logiques connus.
`'U'` est non initialisé, `'X'` est indéterminé ou en conflit, et `'Z'` représente la haute impédance.
<!--SR:!2026-08-27,3,250-->

## 6. Signaux et variables
Quelle différence essentielle entre un `signal` et une `variable` ?
?
**Réponse:**
Une affectation de signal avec `<=` est planifiée pour une mise à jour ultérieure.
Une affectation de variable avec `:=` prend effet immédiatement dans le processus qui la contient.
<!--SR:!2026-08-29,3,230-->

## 7. Affectation concurrente
Comment écrire une porte OU combinatoire sans processus ?
?
**Réponse:**
Une affectation concurrente suffit : `q <= a or b;`.
Elle est évaluée chaque fois que `a` ou `b` change.
<!--SR:!2026-08-28,4,270-->

## 8. Processus combinatoire
Comment écrire correctement un processus combinatoire ?
?
**Réponse:**
Utiliser `process(all)` en VHDL-2008, ou mettre toutes les lectures dans la liste de sensibilité.
Attribuer une valeur à chaque sortie sur tous les chemins afin d'éviter d'inférer un latch.
<!--SR:!2026-08-27,1,190-->

## 9. Instructions séquentielles et concurrentes
Où peut-on employer `if`, `case` et `wait` ?
?
**Réponse:**
`if` et `case` sont des instructions séquentielles, donc s'emploient dans un processus.
`wait` est destiné surtout aux testbenches ; il n'est pas synthétisable dans le RTL courant.
<!--SR:!2026-08-27,3,250-->

## 10. `numeric_std`
Quel paquet faut-il utiliser pour les calculs sur vecteurs, et quels types fournit-il ?
?
**Réponse:**
Utiliser `ieee.numeric_std.all`.
Il fournit `unsigned` et `signed`, ainsi que les conversions `to_unsigned`, `to_signed`, `unsigned` et `signed`.
<!--SR:!2026-08-27,1,210-->

## 11. Conversions numériques
Comment convertir un entier naturel `n` sur huit bits et relire un `unsigned` `u` comme entier ?
?
**Réponse:**
Écrire `to_unsigned(n, 8)` pour obtenir un `unsigned(7 downto 0)`.
Écrire `to_integer(u)` pour obtenir sa valeur entière.
<!--SR:!2026-08-27,1,210-->

## 12. Largeur et sens d'un vecteur
Que signifie `unsigned(7 downto 0)` ?
?
**Réponse:**
Le vecteur possède huit bits, indexés de `7` à `0`.
Avec cette convention, l'indice `7` est le bit de poids fort et `0` le bit de poids faible.
<!--SR:!2026-08-27,3,250-->

## 13. Association de ports
Comment relier proprement les ports d'une instance ?
?
**Réponse:**
Préférer l'association nommée, par exemple `a => a_in, b => b_in, q => q_out`.
Elle est plus lisible et ne dépend pas de l'ordre de déclaration des ports.
<!--SR:!2026-08-28,2,210-->

## 14. Entité correcte à simuler
Après analyse et élaboration d'un testbench dont l'entité est `tb_orgate`, quelle entité faut-il exécuter avec GHDL ?
?
**Réponse:**
Il faut exécuter `tb_orgate`, par exemple `ghdl -r tb_orgate --vcd=waveform.vcd`.
L'entité exécutée est le testbench, pas le composant testé.
<!--SR:!2026-08-29,3,250-->
