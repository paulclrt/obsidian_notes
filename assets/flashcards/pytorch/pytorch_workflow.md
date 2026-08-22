#flashcards/code/pytorch/workflow
## 1. Train/Validation Split

Comment divise-t-on les données en ensembles d'entraînement et de validation en PyTorch ?
?
**Réponse:**
Avec un ratio (souvent 80/20) : `training_split = int(len(x) * 0.8)` puis slicing : `x_train, y_train = x[:training_split], y[:training_split]` et `x_validation, y_validation = x[training_split:], y[training_split:]`.

---

## 2. Data Visualization

Comment visualise-t-on les données et les prédictions d'un modèle ?
?
**Réponse:**
Avec `matplotlib.pyplot.scatter()`. Trois scatter plots : training (bleu), validation (vert), prédictions du modèle (rouge). Utiliser `plt.legend()` pour identifier chaque série.

---

## 3. Subclassing nn.Module

Comment crée-t-on un modèle personnalisé en PyTorch ?
?
**Réponse:**
En subclassant `torch.nn.Module`, en définissant les couches (`nn.Parameter`) dans `__init__` et en implémentant la méthode `forward()` qui définit le calcul sur les données d'entrée.

---

## 4. Model Parameters

Comment accède-t-on aux paramètres d'un modèle ?
?
**Réponse:**
`model.parameters()` retourne un itérateur sur tous les paramètres. `model.state_dict()` retourne un dictionnaire avec les noms et valeurs des paramètres. Utile pour le débogage et la sauvegarde.

---

## 5. Inference Mode

Qu'est-ce que `torch.inference_mode()` et pourquoi l'utilise-t-on ?
?
**Réponse:**
Désactive le calcul de gradients et d'autres opérations inutiles pour les prédictions. Plus efficace que `torch.no_grad()`. Utiliser avec `with torch.inference_mode():` avant les prédictions.

---

## 6. Loss Function

À quoi sert une loss function et comment la choisit-on ?
?
**Réponse:**
Mesure l'erreur entre les prédictions et les vraies valeurs. Pour la régression : `nn.L1Loss()` (MAE) ou `nn.MSELoss()`. Pour la classification binaire : `nn.BCELoss()`. Pour la classification multi-classes : `nn.CrossEntropyLoss()`.

---

## 7. Optimizer

Quel est le rôle de l'optimizer et comment l'utilise-t-on ?
?
**Réponse:**
Met à jour les paramètres du modèle pour minimiser la loss. `torch.optim.SGD()` ou `torch.optim.Adam()`. Trois étapes : `optimizer.zero_grad()` (reset), `loss.backward()` (calcul gradients), `optimizer.step()` (mise à jour).

---

## 8. Training Loop

Quels sont les étapes essentielles d'une boucle d'entraînement ?
?
**Réponse:**
1. `model.train()` → mode entraînement
2. Forward pass → calculer prédictions et loss
3. `optimizer.zero_grad()` → reset gradients
4. `loss.backward()` → backpropagation
5. `optimizer.step()` → mise à jour des poids
6. `model.eval()` + `torch.inference_mode()` → évaluation

---

## 9. train() vs eval()

Quelle est la différence entre `model.train()` et `model.eval()` ?
?
**Réponse:**
`model.train()` active le mode entraînement (BatchNorm, Dropout actifs). `model.eval()` active le mode évaluation (comportement différent pour ces couches). Toujours alterner entre les deux.

---

## 10. Save Model

Comment sauvegarde-t-on un modèle en PyTorch ?
?
**Réponse:**
`torch.save(model.state_dict(), "model.pth")` sauvegarde uniquement les paramètres. Utiliser `pathlib.Path` pour créer le répertoire. Ne sauvegarde PAS la classe du modèle.

---

## 11. Load Model

Comment charge-t-on un modèle sauvegardé ?
?
**Réponse:**
1. Recréer la même classe de modèle
2. `model.load_state_dict(torch.load("model.pth"))`
3. `model.eval()` pour passer en mode évaluation
Important : la classe du modèle doit être identique à celle utilisée à la sauvegarde.

---

## 12. Device (CPU/GPU)

Comment déplace-t-on un modèle sur GPU ?
?
**Réponse:**
`device = "cuda" if torch.cuda.is_available() else "cpu"` puis `model.to(device)`. Vérifier avec `next(model.parameters()).device`. Déplacer aussi les données : `x = x.to(device)`.

---

## 13. Backpropagation

Qu'est-ce que la backpropagation et comment fonctionne-t-elle en PyTorch ?
?
**Réponse:**
Algorithme qui calcule les gradients de la loss par rapport à chaque paramètre. En PyTorch : `loss.backward()` calcule les gradients stockés dans `param.grad`. L'optimizer utilise ces gradients pour mettre à jour les poids.

---

## 14. Gradients

Que sont les gradients et pourquoi doivent-ils être reset à chaque epoch ?
?
**Réponse:**
Les gradients indiquent la direction et l'amplitude de la mise à jour des paramètres. Sans `optimizer.zero_grad()`, les gradients s'accumulent d'un epoch à l'autre, ce qui corrompt l'entraînement.

---

## 15. Learning Rate

Quel est le rôle du learning rate et que se passe-t-il s'il est trop élevé ou trop bas ?
?
**Réponse:**
Contrôle la taille des pas de mise à jour. Trop élevé : le modèle diverge. Trop bas : convergence très lente ou blocage dans un minimum local. Valeurs courantes : 0.01, 0.001, 0.0001.

---

## 16. Epochs

Un epoch représente quoi exactement dans l'entraînement ?
?
**Réponse:**
Un epoch = une passe complète sur l'ensemble d'entraînement. 100 epochs signifie que le modèle voit chaque exemple 100 fois. Le nombre d'epochs dépend du dataset et de la convergence.

---

## 17. Overfitting

Comment détecte-t-on un overfitting lors de l'entraînement ?
?
**Réponse:**
La loss de training diminue tandis que la loss de validation augmente ou stagne. Solution : arrêter tôt (early stopping), augmenter les données, ajouter de la régularisation (dropout, weight decay).

---

## 18. Underfitting

Qu'est-ce que l'underfitting et comment le résoudre ?
?
**Réponse:**
Le modèle n'arrive pas à apprendre (loss élevée sur train et validation). Solutions : augmenter la complexité du modèle (plus de couches/neurones), entraîner plus longtemps, réduire la régularisation.

---

## 19. state_dict()

Qu'est-ce que `model.state_dict()` et pourquoi est-ce important ?
?
**Réponse:**
Dictionnaire contenant tous les paramètres entraînables du modèle (poids, biais). Utile pour la sauvegarde, le débogage, et le transfert entre appareils. C'est ce qui est sauvegardé avec `torch.save()`.

---

## 20. Full Workflow Summary

Quels sont les 6 étapes d'un workflow PyTorch complet ?
?
**Réponse:**
1. Préparer les données (split, tensors)
2. Construire le modèle (subclass nn.Module)
3. Entraîner (boucle avec forward/backward)
4. Évaluer (inference mode)
5. Sauvegarder (state_dict)
6. Charger et utiliser (load_state_dict)

---