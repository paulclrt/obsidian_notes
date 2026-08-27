#flashcards/VHDL/hardware_engineering
## 1. Synthèse et implémentation
Quelle différence entre synthèse et implémentation sur FPGA ?
?
**Réponse:**
La synthèse transforme le RTL en une netlist logique optimisée.
L'implémentation place et route cette netlist dans les ressources physiques du FPGA avant génération du bitstream.
<!--SR:!2026-08-28,3,250-->

## 2. Contraintes temporelles
Pourquoi les contraintes d'horloge sont-elles indispensables ?
?
**Réponse:**
Elles indiquent à l'outil les périodes et relations d'horloges à respecter.
Sans elles, l'analyse temporelle ne peut pas prouver que le matériel fonctionnera à la fréquence visée.
<!--SR:!2026-08-28,2,210-->

## 3. Setup et hold
Que vérifient les contraintes de setup et de hold ?
?
**Réponse:**
Le setup vérifie que les données arrivent assez tôt avant le front d'horloge de capture.
Le hold vérifie qu'elles restent stables assez longtemps après ce front.
<!--SR:!2026-08-28,3,250-->

## 4. Clock enable
Pourquoi préférer un clock enable à une horloge fabriquée par logique ?
?
**Réponse:**
Un clock enable conserve une horloge propre et utilise les ressources d'horloge dédiées.
Fabriquer une horloge avec de la logique peut créer skew et glitches difficiles à analyser.
<!--SR:!2026-08-28,3,250-->

## 5. Domaines d'horloge
Qu'est-ce qu'un CDC ?
?
**Réponse:**
Un Clock Domain Crossing est le transfert d'information entre domaines d'horloge différents ou asynchrones.
Il doit être traité explicitement pour limiter le risque de métastabilité.
<!--SR:!2026-08-28,2,230-->

## 6. Synchroniseur simple bit
Quelle solution classique utilise-t-on pour un signal de contrôle sur un bit qui traverse un CDC ?
?
**Réponse:**
Utiliser généralement deux bascules en série dans le domaine receveur.
Cette méthode réduit le risque de métastabilité mais ne convient pas directement à un bus multi-bit.
<!--SR:!2026-08-29,3,250-->

## 7. Reset robuste
Quelle pratique rend la libération d'un reset asynchrone plus sûre ?
?
**Réponse:**
L'assertion peut être asynchrone, mais la désassertion est souvent synchronisée dans chaque domaine d'horloge.
Cela évite de libérer des bascules à des instants incohérents.
<!--SR:!2026-08-27,1,190-->

## 8. Signaux non initialisés
Pourquoi faut-il prendre `'U'` et `'X'` au sérieux en simulation ?
?
**Réponse:**
Ils révèlent souvent un registre non reseté, une entrée non pilotée ou plusieurs pilotes.
Les masquer trop tôt peut cacher un défaut réel du RTL ou du testbench.
<!--SR:!2026-08-28,3,250-->

## 9. Revue de RTL
Quels points vérifier lors d'une revue de module VHDL ?
?
**Réponse:**
Vérifier l'interface, les resets, les domaines d'horloge, les tailles et signes numériques, les valeurs par défaut, les cas limites et la synthétisabilité.
Vérifier aussi que les assertions et tests couvrent le comportement annoncé.
<!--SR:!2026-08-28,2,230-->

## 10. Warnings de synthèse
Comment traiter les avertissements de synthèse ou de timing ?
?
**Réponse:**
Les lire et les classer ; ne pas les ignorer par défaut.
Un latch, une troncature, une horloge non contrainte ou un chemin non analysé peut être un bug matériel.
<!--SR:!2026-08-28,3,250-->

## 11. Interface de streaming
Que faut-il garantir dans une interface de type `valid`/`ready` ?
?
**Réponse:**
Un transfert a lieu lorsque `valid` et `ready` sont tous deux actifs au même front.
La source maintient données et `valid` stables tant que le transfert n'a pas eu lieu.
<!--SR:!2026-08-28,2,210-->

## 12. Définition de terminé pour un bloc RTL
Quand peut-on considérer un bloc prêt à être livré à l'étape suivante ?
?
**Réponse:**
Son interface et son comportement sont spécifiés, le RTL est synthétisable, les tests et assertions passent, les contraintes sont définies et l'analyse temporelle est propre.
Les limitations connues doivent être documentées.
<!--SR:!2026-08-29,4,270-->
