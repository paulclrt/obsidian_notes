#flashcards/machine_learning/pytorch/transfer_learning
## 1. What is Transfer Learning

Qu'est-ce que le transfer learning et pourquoi l'utiliser ?
?
**Réponse:**
Réutiliser un modèle pré-entraîné sur un gros dataset (ex: ImageNet) comme point de départ pour une nouvelle tâche.
- **Gain de temps** : features génériques (bords, textures) déjà apprises
- **Moins de données** : converge avec peu d'exemples
- **Meilleure performance** : surtout si données target limitées
Étude : transfer learning >> training from scratch en coût/temps (How to train your ViT? 2021).

## 2. Where to Find Pretrained Models

Où trouver des modèles pré-entraînés pour PyTorch ?
?
**Réponse:**
| Source | Modèles | Lien |
|---|---|---|
| **torchvision.models** | ResNet, VGG, EfficientNet, ViT, ConvNeXt | `torchvision.models` |
| **HuggingFace Hub** | Vision, NLP, Audio, Multimodal | huggingface.co/models |
| **timm (PyTorch Image Models)** | 500+ architectures SOTA | github.com/rwightman/pytorch-image-models |
| **Papers With Code** | Implémentations papers + benchmarks | paperswithcode.com |

## 3. Loading Pretrained Model (torchvision v0.13+)

Comment charger un modèle pré-entraîné avec les weights et transforms automatiques ?
?
**Réponse:**
```python
import torchvision

# 1. Charger weights (inclut métadonnées + transforms)
weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT

# 2. Transforms automatiques adaptées au modèle
auto_transforms = weights.transforms()
print(auto_transforms)  # Resize, CenterCrop, Normalize (ImageNet stats)

# 3. Créer modèle avec weights
model = torchvision.models.efficientnet_b0(weights=weights).to(device)
```
`weights.transforms()` retourne le `Compose` exact utilisé pour l'entraînement original.

## 4. Pretrained Model Structure (EfficientNet)

Quelles sont les 3 parties principales d'un modèle EfficientNet pré-entraîné ?
?
**Réponse:**
1. **`features`** : Backbone convolutionnel (extracteur de features) — apprend représentations visuelles génériques
2. **`avgpool`** : Global Average Pooling → vecteur de features (feature vector) 1D
3. **`classifier`** : Couche(s) finale(s) — mappe feature vector → logits classes (1000 pour ImageNet)

```python
model = torchvision.models.efficientnet_b0(weights=weights)
print(model.features)      # Conv blocks
print(model.avgpool)       # AdaptiveAvgPool2d
print(model.classifier)    # Sequential(Dropout, Linear(1280, 1000))
```

## 5. Freezing Feature Extractor

Comment geler (freeze) le feature extractor pour n'entraîner que le classifier ?
?
**Réponse:**
```python
model = torchvision.models.efficientnet_b0(weights=weights)

# Freeze tous les paramètres du backbone
for param in model.features.parameters():
    param.requires_grad = False

# Optionnel : freeze aussi avgpool
for param in model.avgpool.parameters():
    param.requires_grad = False

# Remplacer classifier pour nouvelle tâche
model.classifier = nn.Sequential(
    nn.Dropout(0.2),
    nn.Linear(1280, num_classes)  # 1280 = in_features EfficientNet-B0
).to(device)
```
`requires_grad=False` → pas de gradient → pas de mise à jour par optimizer.

## 6. Fine-tuning vs Feature Extraction

Quelle est la différence entre feature extraction et fine-tuning ?
?
**Réponse:**
| Approche | Backbone | Classifier | Quand utiliser |
|---|---|---|---|
| **Feature Extraction** | Gelé (frozen) | Entraîné | Petit dataset, tâche similaire |
| **Fine-tuning** | Dégelé (partiellement/totalement) | Entraîné | Dataset moyen/grand, tâche différente |

Fine-tuning : dégeler derniers blocs du backbone + classifier, LR plus bas (ex: 1e-4 vs 1e-3).

## 7. Replacing Classifier Head

Comment remplacer la tête de classification pour votre nombre de classes ?
?
**Réponse:**
```python
# 1. Trouver in_features du classifier original
in_features = model.classifier[-1].in_features  # 1280 pour EfficientNet-B0

# 2. Remplacer
model.classifier = nn.Sequential(
    nn.Dropout(p=0.2, inplace=True),
    nn.Linear(in_features, num_classes)
).to(device)
```
Adapter `in_features` selon l'architecture (ResNet50: 2048, ViT-B/16: 768, etc.).

## 8. Fine-tuning Last Layers Only

Comment fine-tuner seulement les dernières couches du backbone ?
?
**Réponse:**
```python
# Freeze tout d'abord
for param in model.parameters():
    param.requires_grad = False

# Dégeler derniers N blocs (ex: dernier bloc EfficientNet)
for param in model.features[-2:].parameters():  # derniers 2 blocs
    param.requires_grad = True

# Classifier toujours entraîné
for param in model.classifier.parameters():
    param.requires_grad = True

# Optimizer seulement sur paramètres requires_grad=True
optimizer = torch.optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=1e-4  # LR plus bas pour fine-tuning
)
```
`filter(lambda p: p.requires_grad, ...)` exclut paramètres gelés.

## 9. Learning Rates for Transfer Learning

Quels learning rates utiliser pour transfer learning ?
?
**Réponse:**
| Phase | LR typique | Raison |
|---|---|---|
| **Feature extraction** (classifier only) | 1e-3 à 1e-2 | Nouveaux paramètres, peuvent bouger vite |
| **Fine-tuning** (backbone + classifier) | 1e-5 à 1e-4 | Préserver features pré-entraînées, ajustements fins |
| **Différentiel** (discriminative LR) | Classifier: 1e-3, Backbone: 1e-5 | Groupes de paramètres séparés dans optimizer |

```python
optimizer = torch.optim.Adam([
    {"params": model.features.parameters(), "lr": 1e-5},
    {"params": model.classifier.parameters(), "lr": 1e-3}
])
```

## 10. Data Transforms for Pretrained Models

Pourquoi utiliser les transforms automatiques du modèle pré-entraîné ?
?
**Réponse:**
```python
weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT
transform = weights.transforms()
# Equivalent à :
# Compose([
#     Resize(256), CenterCrop(224), ToTensor(),
#     Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
# ])
```
Le modèle a été entraîné avec **ces exacts transforms** (resize, crop, normalization). Utiliser d'autres transforms dégrade performance.

## 11. Transfer Learning Training Loop

À quoi ressemble la boucle d'entraînement pour transfer learning ?
?
**Réponse:**
```python
# Même boucle standard, mais :
# - model déjà sur device
# - optimizer seulement sur params requires_grad=True
# - moins d'epochs (5-20 typique)
# - LR plus bas

for epoch in range(epochs):
    model.train()
    for X, y in train_dataloader:
        X, y = X.to(device), y.to(device)
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    # Evaluation...
```
Points clés : `model.eval()` + `inference_mode()` pour val, `train()` pour train (BatchNorm/Dropout dans classifier).

## 12. Popular Pretrained Architectures

Quelles sont les architectures pré-entraînées courantes dans torchvision ?
?
**Réponse:**
| Architecture | Variantes | Caractéristiques |
|---|---|---|
| **ResNet** | resnet18, resnet50, resnet152 | Residual connections, robuste |
| **EfficientNet** | efficientnet_b0 à b7 | Compound scaling, efficient |
| **Vision Transformer (ViT)** | vit_b_16, vit_b_32, vit_l_16 | Attention globale, SOTA |
| **ConvNeXt** | convnext_tiny, small, base, large | Modern CNN, compete avec ViT |
| **VGG** | vgg11, vgg16, vgg19 | Classique, beaucoup de paramètres |
| **MobileNet** | mobilenet_v2, v3_small, v3_large | Mobile, depthwise separable conv |

## 13. Checking Trainable Parameters

Comment vérifier quels paramètres sont entraînables (requires_grad=True) ?
?
**Réponse:**
```python
# Compter paramètres totaux vs entraînables
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Total: {total_params:,} | Trainable: {trainable_params:,} ({100*trainable_params/total_params:.1f}%)")

# Lister noms paramètres entraînables
for name, param in model.named_parameters():
    if param.requires_grad:
        print(f"  {name}: {param.shape}")
```
Vérifier que seul classifier (et blocs dégelés) sont entraînables.

## 14. Transfer Learning for Different Domains

Le transfer learning fonctionne-t-il cross-domain (ex: médical, satellite) ?
?
**Réponse:**
Oui, mais efficacité décroît avec distance domaine :
- **Proche** (photos naturelles → photos naturelles) : excellent
- **Moyen** (photos → dessins, art) : bon
- **Lointain** (photos → médical IRM, satellite, microscopie) : limité
Solutions domaine lointain : fine-tuning plus agressif, plus de données, adapter architecture, self-supervised pretraining sur domaine target.

## 15. Saving/Loading Fine-tuned Model

Comment sauvegarder/charger un modèle fine-tuné ?
?
**Réponse:**
```python
# Sauvegarder (state_dict suffit, architecture recréable)
torch.save(model.state_dict(), "effnet_b0_finetuned.pth")

# Charger
model = torchvision.models.efficientnet_b0(weights=None)  # Pas de weights !
model.classifier = nn.Sequential(nn.Dropout(0.2), nn.Linear(1280, num_classes))
model.load_state_dict(torch.load("effnet_b0_finetuned.pth"))
model.to(device).eval()
```
**Important** : recréer architecture IDENTIQUE (même classifier) avant `load_state_dict`.