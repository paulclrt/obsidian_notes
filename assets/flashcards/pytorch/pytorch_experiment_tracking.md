#flashcards/machine_learning/pytorch/experiment_tracking
## 1. Why Experiment Tracking

Pourquoi faire du experiment tracking en ML ?
?
**Réponse:**
Entraîner 15 modèles avec hyperparams différents → impossible de comparer mentalement.
Tracking permet :
- Comparer loss/accuracy entre expériences
- Visualiser courbes d'apprentissage (TensorBoard)
- Reproduire meilleurs résultats
- Partager résultats équipe
- Décider quel modèle déployer

## 2. Experiment Tracking Tools

Quels sont les principaux outils de experiment tracking ?
?
**Réponse:**
| Outil | Setup | Pros | Cons | Coût |
|---|---|---|---|---|
| **Python dict/CSV/print** | Aucun | Simple, pur Python | Difficile à échelle | Gratuit |
| **TensorBoard** | `pip install tensorboard` | Intégré PyTorch, standard, scalable | UX basique | Gratuit |
| **Weights & Biases (W&B)** | `pip install wandb` + compte | UX excellente, public sharing, auto-log | Dépendance externe | Gratuit perso |
| **MLflow** | `pip install mlflow` | Open source, MLOps complet, remote server | Setup serveur plus complexe | Gratuit |

## 3. TensorBoard SummaryWriter

Comment utiliser `SummaryWriter` de PyTorch pour TensorBoard ?
?
**Réponse:**
```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(log_dir="runs/experiment_1")

for epoch in range(epochs):
    # ... training ...
    
    # Log scalaires (loss, accuracy)
    writer.add_scalars("Loss", {"train": train_loss, "test": test_loss}, epoch)
    writer.add_scalars("Accuracy", {"train": train_acc, "test": test_acc}, epoch)
    
    # Log graph du modèle (une fois)
    if epoch == 0:
        writer.add_graph(model, torch.randn(32, 3, 224, 224).to(device))

writer.close()
```
Lance TensorBoard : `tensorboard --logdir runs/`

## 4. add_scalars vs add_scalar

Quelle est la différence entre `add_scalar` et `add_scalars` ?
?
**Réponse:**
```python
# add_scalar : une seule courbe par tag
writer.add_scalar("Loss/train", train_loss, epoch)
writer.add_scalar("Loss/test", test_loss, epoch)

# add_scalars : multiple courbes sous MÊME tag (groupées dans TensorBoard)
writer.add_scalars("Loss", {"train": train_loss, "test": test_loss}, epoch)
writer.add_scalars("Accuracy", {"train": train_acc, "test": test_acc}, epoch)
```
`add_scalars` → onglet "Scalars" TensorBoard montre train/test superposés automatiquement.

## 5. add_graph for Model Architecture

Comment logger l'architecture du modèle dans TensorBoard ?
?
**Réponse:**
```python
# Une seule fois (début entraînement)
writer.add_graph(
    model=model,
    input_to_model=torch.randn(32, 3, 224, 224).to(device)  # exemple input
)
```
Affiche graphe computationnel dans onglet "Graphs" — utile pour vérifier shapes, connexions, paramètres.

## 6. Custom SummaryWriter Factory

Comment créer une factory pour organisers logs par expérience ?
?
**Réponse:**
```python
from datetime import datetime
import os
from torch.utils.tensorboard import SummaryWriter

def create_writer(experiment_name: str, model_name: str, extra: str = None):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    if extra:
        log_dir = os.path.join("runs", timestamp, experiment_name, model_name, extra)
    else:
        log_dir = os.path.join("runs", timestamp, experiment_name, model_name)
    print(f"[INFO] Created SummaryWriter, saving to: {log_dir}")
    return SummaryWriter(log_dir=log_dir)

# Usage
writer = create_writer("data_10_percent", "effnetb0", "5_epochs")
# Logs dans: runs/2026-08-24/data_10_percent/effnetb0/5_epochs/
```
Structure : `runs/YYYY-MM-DD/experiment_name/model_name/extra/`

## 7. Hyperparameters as Experiments

Quels hyperparamètres varier pour créer différentes expériences ?
?
**Réponse:**
Chaque combinaison = une expérience :
- **Epochs** : 5, 10, 50, 100
- **Architecture** : ResNet18, EfficientNet-B0, ViT-B/16, TinyVGG
- **Hidden units / layers** : [10, 10], [64, 32], [256, 128, 64]
- **Learning rate** : 1e-2, 1e-3, 1e-4, 1e-5
- **Batch size** : 16, 32, 64, 128
- **Data augmentation** : none, flip, flip+rotate, AutoAugment
- **Data amount** : 1%, 10%, 100%
- **Optimizer** : SGD, Adam, AdamW
- **Weight decay** : 0, 1e-4, 1e-2

## 8. Nested Experiment Loops

Comment structurer des boucles imbriquées pour tester multiples configs ?
?
**Réponse:**
```python
num_epochs_list = [5, 10]
models = ["effnetb0", "resnet18"]
dataloaders = {"10_percent": dl_10, "full": dl_full}

for data_name, dataloader in dataloaders.items():
    for epochs in num_epochs_list:
        for model_name in models:
            writer = create_writer(data_name, model_name, f"{epochs}_epochs")
            model = get_model(model_name)
            optimizer = get_optimizer(model)
            
            for epoch in range(epochs):
                train_loss, train_acc = train_step(...)
                test_loss, test_acc = test_step(...)
                
                writer.add_scalars("Loss", {"train": train_loss, "test": test_loss}, epoch)
                writer.add_scalars("Accuracy", {"train": train_acc, "test": test_acc}, epoch)
            
            writer.close()
            # Save model, log hyperparams...
```
Chaque combinaison a son propre `writer` → dossier séparé dans TensorBoard.

## 9. Logging Hyperparameters

Comment logger les hyperparamètres dans TensorBoard ?
?
**Réponse:**
```python
hparams = {
    "lr": 0.001,
    "batch_size": 32,
    "epochs": 10,
    "model": "effnetb0",
    "data": "pizza_steak_sushi_10percent"
}

# Métriques finales
metric_dict = {
    "hparam/accuracy": final_test_acc,
    "hparam/loss": final_test_loss
}

writer.add_hparams(hparams, metric_dict)
```
Onglet "HPARAMS" dans TensorBoard : tableau comparatif + graphiques parallèles.

## 10. Logging Images

Comment logger des images (prédictions, grad-CAM, etc.) dans TensorBoard ?
?
**Réponse:**
```python
# Log images de validation avec prédictions
model.eval()
with torch.inference_mode():
    X, y = next(iter(test_dataloader))
    X, y = X.to(device), y.to(device)
    preds = model(X).argmax(dim=1)
    
    # Grid d'images
    import torchvision
    grid = torchvision.utils.make_grid(X[:8].cpu(), nrow=4)
    writer.add_image("Predictions", grid, epoch)
    
    # Ou images individuelles
    for i in range(4):
        writer.add_image(f"Pred_{i}/True_{y[i]}/Pred_{preds[i]}", X[i].cpu(), epoch)
```
Onglet "Images" dans TensorBoard — utile pour inspection qualitative.

## 11. Logging Histograms

Comment logger la distribution des poids/gradients ?
?
**Réponse:**
```python
for name, param in model.named_parameters():
    writer.add_histogram(f"Weights/{name}", param, epoch)
    if param.grad is not None:
        writer.add_histogram(f"Gradients/{name}", param.grad, epoch)
```
Onglet "Distributions" / "Histograms" — détecter gradient explosion/vanishing, dead neurons.

## 12. Early Stopping with Tracking

Comment implémenter early stopping basé sur TensorBoard metrics ?
?
**Réponse:**
```python
best_test_loss = float('inf')
patience = 5
patience_counter = 0

for epoch in range(epochs):
    train_loss, train_acc = train_step(...)
    test_loss, test_acc = test_step(...)
    
    writer.add_scalars("Loss", {"train": train_loss, "test": test_loss}, epoch)
    writer.add_scalars("Accuracy", {"train": train_acc, "test": test_acc}, epoch)
    
    if test_loss < best_test_loss:
        best_test_loss = test_loss
        patience_counter = 0
        torch.save(model.state_dict(), "best_model.pth")
    else:
        patience_counter += 1
        if patience_counter >= patience:
            print(f"Early stopping at epoch {epoch}")
            break
```
Sauvegarde meilleur modèle, arrête si pas d'amélioration.

## 13. Comparing Experiments in TensorBoard

Comment comparer plusieurs expériences dans TensorBoard ?
?
**Réponse:**
1. Lancer : `tensorboard --logdir runs/`
2. Onglet **Scalars** : cocher/décocher runs dans sidebar gauche
3. Onglet **HPARAMS** : tableau comparatif hyperparams vs métriques
4. Filtrer par tag (Loss, Accuracy) ou run name
5. Télécharger CSV pour analyse externe
Runs organisés par dossier = faciles à sélectionner/désélectionner.

## 14. Experiment Naming Convention

Quelle convention de nommage pour les expériences ?
?
**Réponse:**
```
runs/
└── YYYY-MM-DD/
    ├── experiment_description/
    │   ├── model_name/
    │   │   ├── hyperparam_value/
    │   │   └── another_hyperparam/
    │   └── another_model/
    └── another_experiment/
```
Exemple : `runs/2026-08-24/pizza_steak_sushi_10pct/effnetb0/lr_1e-3_bs32/5_epochs/`
Lisible, filtrable, chronologique.

## 15. Reproducibility with Tracking

Comment assurer la reproductibilité avec experiment tracking ?
?
**Réponse:**
```python
def set_seed(seed=42):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)

# Logger seed + versions
hparams = {
    "seed": 42,
    "torch_version": torch.__version__,
    "cuda_version": torch.version.cuda,
    "python_version": sys.version
}
writer.add_hparams(hparams, {})
```
Tracker : seed, versions libs, git commit hash, data version.