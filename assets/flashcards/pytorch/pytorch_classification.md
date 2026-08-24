#flashcards/machine_learning/pytorch/classification
## 1. Binary vs Multiclass Output Shape

Quelle est la différence de shape de sortie entre classification binaire et multi-classes ?
?
**Réponse:**
- **Binaire** : `out_features=1` (un seul logit → probabilité classe 1)
- **Multi-classes** : `out_features=N` (N logits, un par classe)
Exemple : 3 classes (pizza, steak, sushi) → sortie shape `(batch, 3)`

## 2. Binary Classification Output Activation

Quelle fonction d'activation utiliser en sortie pour classification binaire ?
?
**Réponse:**
**Sigmoid** : `torch.sigmoid(logits)` → probabilité en [0, 1].
```python
y_pred_probs = torch.sigmoid(model(x).squeeze())
y_pred_labels = torch.round(y_pred_probs)  # 0 ou 1
```
Avec `BCEWithLogitsLoss`, le sigmoid est intégré dans la loss (ne pas l'appliquer manuellement).
<!--SR:!2026-08-27,3,250-->

## 3. Multiclass Classification Output Activation

Quelle fonction d'activation utiliser en sortie pour classification multi-classes ?
?
**Réponse:**
**Softmax** : `torch.softmax(logits, dim=1)` → probabilités sommant à 1.
```python
y_pred_probs = torch.softmax(model(x), dim=1)
y_pred_labels = y_pred_probs.argmax(dim=1)  # indice classe max
```
Avec `CrossEntropyLoss`, le softmax est intégré (ne pas l'appliquer manuellement).

## 4. Hidden Layer Activation

Quelle activation utiliser dans les couches cachées et pourquoi ?
?
**Réponse:**
**ReLU** (`nn.ReLU()`) : `max(0, x)`. 
- Introduit de la **non-linéarité** (sinon le réseau reste linéaire)
- Évite le problème de gradient vanishing vs sigmoid/tanh
- Simple, rapide, fonctionne bien en pratique
Alternatives : LeakyReLU, GELU, SiLU (Swish).

## 5. BCEWithLogitsLoss Usage

Comment utiliser `nn.BCEWithLogitsLoss` pour classification binaire ?
?
**Réponse:**
```python
loss_fn = nn.BCEWithLogitsLoss()
model = BinaryClassifier()  # sortie: 1 logit
y_pred_logits = model(x_train).squeeze()  # shape (batch,)
loss = loss_fn(y_pred_logits, y_train.float())  # target doit être float
```
- Prend des **logits** (pas de sigmoid manuel)
- Target doit être `float` (0.0 ou 1.0)
- Plus stable numériquement que `BCELoss` + sigmoid séparé

## 6. CrossEntropyLoss Usage

Comment utiliser `nn.CrossEntropyLoss` pour classification multi-classes ?
?
**Réponse:**
```python
loss_fn = nn.CrossEntropyLoss()
model = MultiClassClassifier()  # sortie: N logits
y_pred_logits = model(x_train)  # shape (batch, num_classes)
loss = loss_fn(y_pred_logits, y_train)  # target: indices entiers (LongTensor)
```
- Prend des **logits** (pas de softmax manuel)
- Target = **indices de classe** (entiers 0,1,2...), PAS one-hot
- Combine LogSoftmax + NLLLoss

## 7. Binary Classification Model Architecture

À quoi ressemble un modèle pour classification binaire ?
?
**Réponse:**
```python
class BinaryClassifier(nn.Module):
    def __init__(self, input_features):
        super().__init__()
        self.layer_1 = nn.Linear(input_features, 10)
        self.layer_2 = nn.Linear(10, 10)
        self.layer_3 = nn.Linear(10, 1)  # 1 sortie
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer_1(x))
        x = self.relu(self.layer_2(x))
        x = self.layer_3(x)  # pas d'activation ici (logits)
        return x
```
Sortie = 1 neurone → logit unique. Utiliser avec `BCEWithLogitsLoss`.

## 8. Multiclass Classification Model Architecture

À quoi ressemble un modèle pour classification multi-classes ?
?
**Réponse:**
```python
class MultiClassClassifier(nn.Module):
    def __init__(self, input_features, num_classes):
        super().__init__()
        self.layer_1 = nn.Linear(input_features, 10)
        self.layer_2 = nn.Linear(10, 10)
        self.layer_3 = nn.Linear(10, num_classes)  # N sorties
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer_1(x))
        x = self.relu(self.layer_2(x))
        x = self.layer_3(x)  # logits bruts
        return x
```
Sortie = `num_classes` neurones. Utiliser avec `CrossEntropyLoss`.

## 9. From Logits to Predictions (Binary)

Comment passer des logits aux prédictions de classe en binaire ?
?
**Réponse:**
```python
logits = model(x).squeeze()           # shape (batch,)
probs = torch.sigmoid(logits)         # probabilités [0,1]
preds = torch.round(probs)            # 0 ou 1 (classe)
# Ou en une ligne :
preds = torch.round(torch.sigmoid(model(x).squeeze()))
```
Seuil implicite à 0.5.

## 10. From Logits to Predictions (Multiclass)

Comment passer des logits aux prédictions de classe en multi-classes ?
?
**Réponse:**
```python
logits = model(x)                     # shape (batch, num_classes)
probs = torch.softmax(logits, dim=1)  # probabilités
preds = probs.argmax(dim=1)           # indices classes prédites
# Ou direct :
preds = logits.argmax(dim=1)          # argmax sur logits = argmax sur probs
```
`argmax(dim=1)` prend l'indice du max par échantillon (dim=0 = batch).

## 11. Accuracy Function for Binary

Comment calculer l'accuracy pour classification binaire ?
?
**Réponse:**
```python
def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item()
    return (correct / len(y_pred)) * 100

# Usage:
y_pred_logits = model(x_test).squeeze()
y_pred_probs = torch.sigmoid(y_pred_logits)
y_pred_labels = torch.round(y_pred_probs)
acc = accuracy_fn(y_test, y_pred_labels)
```
`y_true` et `y_pred` doivent avoir même shape et type.
<!--SR:!2026-08-27,3,250-->

## 12. Accuracy with torchmetrics

Comment utiliser `torchmetrics.Accuracy` pour la classification ?
?
**Réponse:**
```python
from torchmetrics import Accuracy

# Binaire
acc_fn = Accuracy(task="binary")
acc = acc_fn(preds, target)

# Multi-classes
acc_fn = Accuracy(task="multiclass", num_classes=10)
acc = acc_fn(preds, target)

# preds: logits OU probabilités (torchmetrics gère les deux)
# target: indices entiers
```
Plus robuste, gère automatiquement logits/probs selon config.

## 13. Confusion Matrix

Comment créer une matrice de confusion en PyTorch ?
?
**Réponse:**
```python
from torchmetrics import ConfusionMatrix

confmat = ConfusionMatrix(task="multiclass", num_classes=3)
conf_matrix = confmat(preds, target)
print(conf_matrix)
```
Rows = vraies classes, Cols = classes prédites. Diagonale = prédictions correctes.

## 14. Model Improvement Techniques

Quelles sont les 7 techniques pour améliorer un modèle qui ne performe pas ?
?
**Réponse:**
1. **Plus de couches** (réseau plus profond)
2. **Plus d'unités cachées** (réseau plus large)
3. **Plus d'epochs** (entraîner plus longtemps)
4. **Changer activation** (ex: ReLU → GELU)
5. **Changer learning rate** (trop haut/trop bas)
6. **Changer loss function** (adaptée au problème)
7. **Transfer learning** (modèle pré-entraîné)

## 15. Classification Decision Boundary Visualization

Comment visualiser la frontière de décision d'un classificateur 2D ?
?
**Réponse:**
```python
from helper_functions import plot_decision_boundary
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plot_decision_boundary(model, X_train, y_train)
plt.title("Train")
plt.subplot(1, 2, 2)
plot_decision_boundary(model, X_test, y_test)
plt.title("Test")
```
Nécessite données 2D (2 features) pour visualisation 2D.

## 16. Precision, Recall, F1

Quelles sont les définitions de Precision, Recall et F1-score ?
?
**Réponse:**
- **Precision** : TP / (TP + FP) — sur prédictions positives, combien sont vraies ?
- **Recall** : TP / (TP + FN) — sur vraies positives, combien détectées ?
- **F1-score** : 2 * (P * R) / (P + R) — moyenne harmonique
```python
from torchmetrics import Precision, Recall, F1Score
precision = Precision(task="binary")(preds, target)
recall = Recall(task="binary")(preds, target)
f1 = F1Score(task="binary")(preds, target)
```

## 17. Classification Report

Comment obtenir un rapport de classification complet (sklearn) ?
?
**Réponse:**
```python
from sklearn.metrics import classification_report

y_true = y_test.cpu().numpy()
y_pred = preds.cpu().numpy()
print(classification_report(y_true, y_pred))
```
Affiche precision, recall, f1, support par classe + macro/micro/weighted averages.
<!--SR:!2026-08-27,3,250-->

## 18. Non-linear Data Requires Non-linear Model

Pourquoi un modèle linéaire échoue sur des données non-linéaires (ex: cercles) ?
?
**Réponse:**
Un modèle linéaire (sans activation non-linéaire) ne peut créer que des frontières de décision **linéaires** (droites/hyperplans).
Données "cercles" (make_circles) nécessitent frontière **circulaire** → impossible sans non-linéarité (ReLU, etc.).
Ajouter `nn.ReLU()` entre couches linéaires permet d'apprendre des patterns non-linéaires.

## 19. Squeeze in Classification

Pourquoi utiliser `.squeeze()` dans la boucle d'entraînement binaire ?
?
**Réponse:**
`nn.Linear(..., 1)` sort shape `(batch, 1)`. `BCEWithLogitsLoss` attend `(batch,)`.
```python
y_pred = model(x_train).squeeze()  # (batch, 1) → (batch,)
loss = loss_fn(y_pred, y_train)
```
Retire la dimension de taille 1. Attention : ne pas utiliser si batch_size=1 (retirait la dim batch).

## 20. Target Type for Loss Functions

Quels types de target (y) attendre pour chaque loss ?
?
**Réponse:**
| Loss | Target dtype | Target format |
|---|---|---|
| `BCEWithLogitsLoss` | `float32` | 0.0 ou 1.0 (ou probabilités) |
| `CrossEntropyLoss` | `int64` (LongTensor) | Indices de classe : 0, 1, 2... |
| `MSELoss` / `L1Loss` | `float32` | Valeurs continues (régression) |
Erreur fréquente : passer `float` à `CrossEntropyLoss` → RuntimeError.
<!--SR:!2026-08-27,3,250-->