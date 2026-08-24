#flashcards/VHDL/rtl_design
## 1. RTL synthétisable
Qu'appelle-t-on RTL synthétisable ?
?
**Réponse:**
Le RTL décrit un matériel à registres et à logique combinatoire qu'un outil de synthèse peut transformer en portes, bascules, mémoire ou ressources FPGA.
Le code de testbench n'est pas nécessairement synthétisable.

## 2. Processus synchrone
Quel patron VHDL utiliser pour une logique cadencée par un front montant ?
?
**Réponse:**
Utiliser `process(clk)` puis `if rising_edge(clk) then`.
Les affectations à l'intérieur décrivent des registres déclenchés sur le front montant.

## 3. Reset synchrone et asynchrone
Quelle différence entre reset synchrone et asynchrone ?
?
**Réponse:**
Un reset synchrone est testé à l'intérieur de `if rising_edge(clk)`.
Un reset asynchrone est aussi dans la sensibilité et peut modifier l'état sans front d'horloge ; son usage dépend des contraintes de la cible.

## 4. Latch involontaire
Comment un latch est-il involontairement inféré dans un processus combinatoire ?
?
**Réponse:**
Lorsqu'un signal de sortie n'est pas affecté sur tous les chemins d'exécution.
Donner une valeur par défaut au début du processus ou couvrir tous les cas.

## 5. `if` et `case`
Quand préférer une instruction `case` à une chaîne de `if` ?
?
**Réponse:**
Utiliser `case` pour sélectionner explicitement un comportement selon les valeurs d'un même signal, notamment pour un état de FSM ou un opcode.
Prévoir un `when others` si toutes les valeurs ne sont pas couvertes.

## 6. Machine à états finis
Quelle structure rend une FSM facile à lire et à vérifier ?
?
**Réponse:**
Séparer un registre d'état synchrone et une logique combinatoire de prochain état et de sorties.
Définir un type énuméré pour les états et une valeur par défaut pour le prochain état.

## 7. Variables dans un processus séquentiel
Quelle règle mentale appliquer aux variables dans un processus cadencé ?
?
**Réponse:**
Elles servent au calcul intermédiaire immédiat pendant le front d'horloge.
Seules les affectations de signaux ou de ports conservent une valeur matérielle d'un cycle au suivant.

## 8. Génériques
À quoi sert un `generic` ?
?
**Réponse:**
Il paramètre une entité à l'élaboration, par exemple une largeur de bus, une profondeur de FIFO ou une fréquence d'horloge.
Il permet de réutiliser le même RTL sans le copier.

## 9. `generate`
Quand utiliser une instruction `generate` ?
?
**Réponse:**
Pour répéter ou conditionner structurellement du matériel à l'élaboration.
Elle est adaptée aux banques de registres, aux canaux identiques et aux options commandées par un générique.

## 10. Packages
Pourquoi placer types, constantes et fonctions dans un `package` ?
?
**Réponse:**
Un package centralise les déclarations partagées et évite les divergences entre modules.
Il rend les interfaces et les conventions de projet explicites et réutilisables.

## 11. Mémoire inférée
Quelles conditions favorisent l'inférence d'une RAM ou d'une ROM ?
?
**Réponse:**
Utiliser un tableau avec un style de lecture et d'écriture reconnu par l'outil de synthèse.
Suivre le guide de codage du fournisseur FPGA ou ASIC, car le comportement lecture-écriture dépend de la primitive ciblée.

## 12. Ne pas utiliser de délais dans le RTL
Pourquoi `after 10 ns` n'est-il pas approprié dans un RTL synthétisable ?
?
**Réponse:**
Le délai décrit un comportement de simulation, pas une temporisation matérielle portable.
En matériel synchrone, créer un compteur ou un enable cadencé.
