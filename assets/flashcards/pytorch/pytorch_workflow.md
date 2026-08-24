#flashcards/machine_learning/pytorch/workflow
## 1. Train/Validation Split

Comment diviser des données en ensembles d'entraînement (80%) et validation (20%) ?
?
**Réponse:**
```python
training_split = int(len(x) * 0.8)
x_train, y_train = x[:training_split], y[:training_split]
x_val, y_val = x[training_split:], y[training_split:]
```
Utiliser le slicing après avoir calculé l'index de coupure.

## 2. Data Visualization

Comment visualiser les données d'entraînement, validation et les prédictions ?
?
**Réponse:**
```python
def plot_predictions(train_data, train_labels, test_data, test_labels, predictions=None):
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training")
    plt.scatter(test_data, test_labels, c="g", s=4, label="Validation")
    if predictions is not None:
        plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
    plt.legend(prop={"size": 14})
```
Bleu = train, Vert = validation, Rouge = prédictions.

## 3. Subclassing nn.Module

Comment créer un modèle personnalisé en PyTorch ?
?
**Réponse:**
```python
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1), requires_grad=True)
        self.bias = nn.Parameter(torch.randn(1), requires_grad=True)

    def forward(self, x):
        return self.weights * x + self.bias
```
1. Subclasser `nn.Module`
2. Définir paramètres dans `__init__` avec `nn.Parameter`
3. Implémenter `forward()`

## 4. Model Parameters

Comment accéder aux paramètres d'un modèle ?
?
**Réponse:**
- `model.parameters()` : itérateur sur tous les paramètres (pour optimizer)
- `model.state_dict()` : dict `{nom: tenseur}` avec noms et valeurs (pour sauvegarde/débogage)
- `list(model.parameters())` : liste des tenseurs paramètres

## 5. Inference Mode

Qu'est-ce que `torch.inference_mode()` et quand l'utiliser ?
?
**Réponse:**
Désactive le calcul de gradients et optimise pour l'inférence. Plus efficace que `torch.no_grad()`.
```python
model.eval()
with torch.inference_mode():
    preds = model(x_test)
```
Toujours utiliser avec `model.eval()` pour désactiver BatchNorm/Dropout.

## 6. Loss Functions by Problem Type

Quelle loss function choisir selon le type de problème ?
?
**Réponse:**
| Problème | Loss Function |
|---|---|
| Régression | `nn.L1Loss()` (MAE) ou `nn.MSELoss()` (MSE) |
| Classification binaire | `nn.BCEWithLogitsLoss()` (recommandé) ou `nn.BCELoss()` |
| Classification multi-classes | `nn.CrossEntropyLoss()` |

## 7. Optimizer Setup

Comment configurer un optimizer en PyTorch ?
?
**Réponse:**
```python
optimizer = torch.optim.SGD(params=model.parameters(), lr=0.01)
# ou
optimizer = torch.optim.Adam(params=model.parameters(), lr=0.001)
```
Passer `model.parameters()` et `lr` (learning rate). SGD = descente de gradient stochastique, Adam = adaptatif.

## 8. Training Loop Steps

Quelles sont les 5 étapes essentielles d'une boucle d'entraînement ?
?
**Réponse:**
```python
model.train()                    # 1. Mode entraînement
y_pred = model(x_train)          # 2. Forward pass
loss = loss_fn(y_pred, y_train)  # 3. Calcul loss
optimizer.zero_grad()            # 4. Reset gradients
loss.backward()                  # 5. Backpropagation
optimizer.step()                 # 6. Mise à jour poids
```
Puis évaluation : `model.eval()` + `torch.inference_mode()`.

## 9. train() vs eval()

Quelle est la différence entre `model.train()` et `model.eval()` ?
?
**Réponse:**
- `model.train()` : active mode entraînement → **BatchNorm** utilise stats du batch, **Dropout** actif
- `model.eval()` : active mode évaluation → BatchNorm utilise stats globales, Dropout désactivé
Toujours alterner : `train()` pendant entraînement, `eval()` pendant validation/test.

## 10. Save Model (state_dict)

Comment sauvegarder un modèle PyTorch ?
?
**Réponse:**
```python
from pathlib import Path
modelpath = Path("models")
modelpath.mkdir(parents=True, exist_ok=True)
torch.save(model.state_dict(), modelpath / "model.pth")
```
Sauvegarde **seulement** les paramètres (poids/biais), pas l'architecture. Le fichier `.pth` est un pickle.

## 11. Load Model

Comment charger un modèle sauvegardé ?
?
**Réponse:**
```python
# 1. Recréer EXACTEMENT la même classe de modèle
loaded_model = LinearRegressionModel()

# 2. Charger les poids
loaded_model.load_state_dict(torch.load("models/model.pth"))

# 3. Mode évaluation
loaded_model.eval()
```
La classe doit être identique (même architecture) à la sauvegarde.

## 12. Device Management (CPU/GPU)

Comment déplacer un modèle et les données sur GPU ?
?
**Réponse:**
```python
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
x = x.to(device)
y = y.to(device)

# Vérifier device
next(model.parameters()).device
```
Tous les tenseurs et le modèle doivent être sur le **même device**.

## 13. Backpropagation

Qu'est-ce que la backpropagation et comment la déclencher en PyTorch ?
?
**Réponse:**
Algorithme calculant gradients de la loss par rapport à chaque paramètre.
```python
loss.backward()  # Calcule gradients → stockés dans param.grad
```
L'optimizer utilise `param.grad` pour mettre à jour les poids.

## 14. Gradient Accumulation

Pourquoi doit-on reset les gradients à chaque epoch/batch ?
?
**Réponse:**
Sans `optimizer.zero_grad()`, les gradients s'**accumulent** (s'additionnent) d'un step à l'autre → corruption de l'entraînement.
```python
optimizer.zero_grad()  # Reset AVANT loss.backward()
loss.backward()
optimizer.step()
```

## 15. Learning Rate Effect

Quel est l'effet du learning rate trop élevé vs trop bas ?
?
**Réponse:**
- **Trop élevé** : le modèle diverge, loss explose, oscillations
- **Trop bas** : convergence très lente, bloqué dans minimum local
Valeurs courantes : `0.01`, `0.001`, `0.0001`. Tester avec learning rate finder.

## 16. Epoch Definition

Qu'est-ce qu'un epoch exactement ?
?
**Réponse:**
Un **epoch = une passe complète** sur tout l'ensemble d'entraînement.
100 epochs = le modèle voit chaque exemple 100 fois. 
Différent de "step" ou "iteration" = un batch.

## 17. Overfitting Detection

Comment détecter l'overfitting pendant l'entraînement ?
?
**Réponse:**
- Loss **training** diminue
- Loss **validation** augmente ou stagne
Solutions : early stopping, plus de données, dropout, weight decay, data augmentation, transfer learning.

## 18. Underfitting Detection

Qu'est-ce que l'underfitting et comment le résoudre ?
?
**Réponse:**
Loss **élevée** sur training ET validation. Le modèle n'apprend pas.
Solutions : plus de couches/neurones, entraîner plus longtemps, réduire régularisation, augmenter learning rate, transfer learning.

## 18. state_dict() Details

Que contient `model.state_dict()` et pourquoi est-ce important ?
?
**Réponse:**
Dictionnaire `{nom_paramètre: tenseur}` de **tous les paramètres entraînables** (poids, biais).
- C'est ce que `torch.save()` sérialise
- Permet transfert entre devices/architectures
- Utile pour débogage : inspecter valeurs précises

## 20. Complete Workflow Summary

Quelles sont les 6 étapes d'un workflow PyTorch complet ?
?
**Réponse:**
1. **Préparer données** : split, tenseurs, DataLoader
2. **Construire modèle** : subclass `nn.Module`, définir `forward`
3. **Entraîner** : boucle epochs + forward/loss/backward/step
4. **Évaluer** : `model.eval()` + `torch.inference_mode()`
5. **Sauvegarder** : `torch.save(model.state_dict(), path)`
6. **Charger/Utiliser** : recréer classe + `load_state_dict()`

## 21. BCEWithLogitsLoss vs BCELoss

Quelle est la différence entre `BCEWithLogitsLoss` et `BCELoss` ?
?
**Réponse:**
- `BCEWithLogitsLoss` : combine **Sigmoid + BCELoss** en une seule fonction (plus stable numériquement). Prend des **logits** (sorties brutes).
- `BCELoss` : attend des **probabilités** (déjà passées par Sigmoid).
**Recommandation** : toujours utiliser `BCEWithLogitsLoss` pour classification binaire.

## 22. CrossEntropyLoss Details

Que fait `nn.CrossEntropyLoss()` et qu'attend-il en entrée ?
?
**Réponse:**
Combine **LogSoftmax + NLLLoss**. Attend :
- **Input** : logits bruts (non-normalisés), shape `(batch, num_classes)`
- **Target** : indices de classe (entiers), shape `(batch,)` — **PAS one-hot**
Pas besoin de Softmax manuel avant.

## 23. Accuracy Calculation

Comment calculer l'accuracy en PyTorch ?
?
**Réponse:**
```python
def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item()
    return (correct / len(y_pred)) * 100

# Ou avec torchmetrics
from torchmetrics import Accuracy
accuracy = Accuracy(task="multiclass", num_classes=10)
acc = accuracy(y_pred, y_true)
```
Pour classification : `y_pred = logits.argmax(dim=1)`.

## 24. Training Loop with DataLoader

Comment écrire une boucle d'entraînement avec DataLoader (batches) ?
?
**Réponse:**
```python
for epoch in range(epochs):
    model.train()
    train_loss = 0
    for batch, (X, y) in enumerate(train_dataloader):
        X, y = X.to(device), y.to(device)
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
    train_loss /= len(train_dataloader)
```
Accumuler loss par batch, faire moyenne à la fin.

## 25. Evaluation Loop with DataLoader

Comment écrire une boucle d'évaluation avec DataLoader ?
?
**Réponse:**
```python
model.eval()
test_loss, test_acc = 0, 0
with torch.inference_mode():
    for X, y in test_dataloader:
        X, y = X.to(device), y.to(device)
        y_pred = model(X)
        test_loss += loss_fn(y_pred, y).item()
        test_acc += accuracy_fn(y, y_pred.argmax(dim=1))
test_loss /= len(test_dataloader)
test_acc /= len(test_dataloader)
```
Pas de `backward()`, pas de `optimizer.step()`, pas de `zero_grad()`.