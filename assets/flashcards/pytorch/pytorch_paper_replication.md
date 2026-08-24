#flashcards/machine_learning/pytorch/paper_replication
## 1. Why Replicate Papers

Pourquoi répliquer des papers de recherche en ML ?
?
**Réponse:**
- **Apprentissage actif** : comprendre en implémentant (pas juste lire)
- **Validation** : vérifier que résultats sont reproductibles
- **Adaptation** : adapter SOTA à son propre problème/données
- **Skill building** : architectures modernes, techniques avancées
- **Portfolio** : démontrer compétences techniques
- **Bibliothèques nées de réplication** : HuggingFace, timm, fast.ai

## 2. Key Resources for Finding Papers

Quelles sont les meilleures ressources pour trouver papers + code ?
?
**Réponse:**
| Ressource | Description |
|---|---|
| **arXiv** | arxiv.org — prépublications gratuites (ML: cs.LG, cs.CV, stat.ML) |
| **Papers With Code** | paperswithcode.com — papers + code + benchmarks + SOTA tables |
| **AK Twitter** | @_akhaliq — highlights quotidiens avec démos |
| **HuggingFace Papers** | huggingface.co/papers — papers tendances quotidiens |
| **GitHub Trending** | github.com/trending — implémentations populaires |
| **Conference proceedings** | CVPR, NeurIPS, ICML, ICLR — papers peer-reviewed |

## 3. Paper Reading Strategy

Comment lire efficacement un paper ML pour l'implémenter ?
?
**Réponse:**
1. **Abstract + Figures** : comprendre le problème, méthode, résultats clés
2. **Architecture diagram** : visualiser le modèle (souvent Figure 1 ou 2)
3. **Methods section** : détails architecture, loss, training, hyperparams
4. **Experiments** : datasets, baselines, ablation studies
5. **Appendix / Supplementary** : hyperparams complets, détails implémentation
6. **Code officiel** : GitHub link (souvent dans paper ou PapersWithCode)
7. **Répliquer** : commencer minimal, valider chaque composant

## 4. Vision Transformer (ViT) Architecture

Quels sont les composants clés du Vision Transformer (ViT) ?
?
**Réponse:**
Paper: "An Image is Worth 16x16 Words" (Dosovitskiy et al., 2020)
```
Input Image (224x224)
    ↓
Patch Embedding (16x16 patches → 196 tokens + cls token)
    ↓
Positional Embedding (appris)
    ↓
Transformer Encoder × L layers
    ├── Multi-Head Self-Attention
    ├── LayerNorm + Residual
    ├── MLP (GELU)
    └── LayerNorm + Residual
    ↓
MLP Head (LayerNorm + Linear) → Classes
```
- **Patch size** : 16x16 (ViT-B/16) ou 32x32 (ViT-B/32)
- **Hidden dim** : 768 (Base), 1024 (Large), 1280 (Huge)
- **Heads** : 12 (Base), 16 (Large)

## 5. Implementing Patch Embedding

Comment implémenter le patch embedding de ViT ?
?
**Réponse:**
```python
class PatchEmbedding(nn.Module):
    def __init__(self, in_channels=3, patch_size=16, embed_dim=768):
        super().__init__()
        self.patch_size = patch_size
        # Conv2d avec kernel=patch_size, stride=patch_size = non-overlapping patches
        self.proj = nn.Conv2d(in_channels, embed_dim, kernel_size=patch_size, stride=patch_size)
    
    def forward(self, x):
        # x: (B, C, H, W) → (B, embed_dim, H/patch, W/patch)
        x = self.proj(x)
        # Flatten spatial: (B, embed_dim, N_patches) → (B, N_patches, embed_dim)
        x = x.flatten(2).transpose(1, 2)
        return x  # (B, 196, 768) pour 224x224, patch=16
```
`Conv2d` avec `stride=kernel_size` = extraction patches non-overlapping efficacement.

## 6. Class Token and Positional Embedding

Comment ajouter class token et positional embedding ?
?
**Réponse:**
```python
class ViT(nn.Module):
    def __init__(self, ..., num_patches=196, embed_dim=768):
        super().__init__()
        self.patch_embed = PatchEmbedding(...)
        
        # Class token (appris)
        self.cls_token = nn.Parameter(torch.randn(1, 1, embed_dim))
        
        # Positional embedding (appris)
        self.pos_embed = nn.Parameter(torch.randn(1, num_patches + 1, embed_dim))
        
        self.dropout = nn.Dropout(0.1)
    
    def forward(self, x):
        B = x.shape[0]
        x = self.patch_embed(x)              # (B, 196, 768)
        cls_tokens = self.cls_token.expand(B, -1, -1)  # (B, 1, 768)
        x = torch.cat([cls_tokens, x], dim=1)            # (B, 197, 768)
        x = x + self.pos_embed                                   # Add pos embed
        x = self.dropout(x)
        return x
```
Class token = représentation globale image (utilisé pour classification).

## 7. Transformer Encoder Block

À quoi ressemble un bloc Transformer Encoder pour ViT ?
?
**Réponse:**
```python
class TransformerEncoderBlock(nn.Module):
    def __init__(self, embed_dim=768, num_heads=12, mlp_ratio=4.0, dropout=0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(embed_dim)
        self.attn = nn.MultiheadAttention(embed_dim, num_heads, dropout=dropout, batch_first=True)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, int(embed_dim * mlp_ratio)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(int(embed_dim * mlp_ratio), embed_dim),
            nn.Dropout(dropout)
        )
    
    def forward(self, x):
        # Attention + Residual
        x_norm = self.norm1(x)
        attn_out, _ = self.attn(x_norm, x_norm, x_norm)
        x = x + attn_out
        
        # MLP + Residual
        x = x + self.mlp(self.norm2(x))
        return x
```
Pre-LayerNorm (norm avant attention/MLP) — plus stable que Post-LN.

## 8. MLP Head for Classification

Comment faire la tête de classification ViT ?
?
**Réponse:**
```python
class ViT(nn.Module):
    def __init__(self, ..., num_classes=1000, embed_dim=768):
        # ... patch_embed, cls_token, pos_embed, encoder blocks ...
        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, num_classes)
    
    def forward(self, x):
        # ... patch embed + cls + pos + encoder blocks ...
        x = self.norm(x)
        cls_token_final = x[:, 0]  # (B, embed_dim) - premier token = cls
        logits = self.head(cls_token_final)
        return logits
```
Utilise **seulement le class token** final (pas moyenne pooling comme CNN).

## 9. ViT Hyperparameters by Variant

Quels sont les hyperparams standards pour variantes ViT ?
?
**Réponse:**
| Variant | Layers | Hidden | Heads | MLP Ratio | Params |
|---|---|---|---|---|---|
| **ViT-Ti/16** | 12 | 192 | 3 | 4 | 5.7M |
| **ViT-S/16** | 12 | 384 | 6 | 4 | 22M |
| **ViT-B/16** | 12 | 768 | 12 | 4 | 86M |
| **ViT-L/16** | 24 | 1024 | 16 | 4 | 307M |
| **ViT-H/14** | 32 | 1280 | 16 | 4 | 632M |

Suffix /16 = patch 16x16, /14 = patch 14x14, /32 = patch 32x32.

## 10. Training ViT (Key Differences from CNN)

Quelles sont les différences clés d'entraînement ViT vs CNN ?
?
**Réponse:**
| Aspect | CNN | ViT |
|---|---|---|
| **Data Augmentation** | Standard (flip, crop) | **Stronger** : RandAugment, Mixup, CutMix, Random Erasing |
| **Optimizer** | SGD + momentum | **AdamW** (weight decay decoupled) |
| **LR Schedule** | Step / Cosine | **Cosine decay + Warmup** (10k steps) |
| **Weight Decay** | 1e-4 | **0.05 - 0.3** (plus fort) |
| **Batch Size** | 256-1024 | **Grande** (4096+ pour JFT-300M) |
| **Epochs** | 90-300 | **300-1000** (plus long) |
| **Regularization** | Dropout, BN | **DropPath (Stochastic Depth)**, LayerScale |

## 11. DropPath (Stochastic Depth)

Qu'est-ce que DropPath et comment l'implémenter ?
?
**Réponse:**
DropPath = supprime aléatoirement des **branches résiduelles** entières pendant l'entraînement.
```python
def drop_path(x, drop_prob=0.1, training=True):
    if drop_prob == 0. or not training:
        return x
    keep_prob = 1 - drop_prob
    shape = (x.shape[0],) + (1,) * (x.ndim - 1)
    random_tensor = keep_prob + torch.rand(shape, dtype=x.dtype, device=x.device)
    random_tensor.floor_()  # binarize
    return x.div(keep_prob) * random_tensor

class TransformerEncoderBlock(nn.Module):
    def __init__(self, ..., drop_path=0.1):
        # ...
        self.drop_path = drop_path
    
    def forward(self, x):
        x = x + drop_path(self.attn(self.norm1(x)), self.drop_path, self.training)
        x = x + drop_path(self.mlp(self.norm2(x)), self.drop_path, self.training)
        return x
```
Augmente drop_path progressivement par couche (ex: 0 → 0.1 → 0.2).

## 12. Using timm Library

Comment utiliser `timm` pour charger ViT pré-entraîné ?
?
**Réponse:**
```python
import timm

# Lister modèles disponibles
print(timm.list_models("*vit*"))

# Charger ViT-B/16 pré-entraîné ImageNet-1k
model = timm.create_model("vit_base_patch16_224", pretrained=True, num_classes=1000)

# Pour fine-tuning sur custom classes
model = timm.create_model("vit_base_patch16_224", pretrained=True, num_classes=10)

# Transforms automatiques
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=True)
```
`timm` = 500+ modèles, pré-entraînés, configs, transforms, tout intégré.

## 13. Replicating Paper Results Checklist

Checklist pour valider une réplication ?
?
**Réponse:**
- [ ] **Architecture** : nombre couches, dimensions, heads, patch size identiques
- [ ] **Hyperparams** : LR, schedule, weight decay, batch size, epochs, warmup
- [ ] **Data** : même dataset, mêmes splits, mêmes augmentations
- [ ] **Initialization** : mêmes seeds, même pretrained weights (si applicable)
- [ ] **Compute** : même hardware (ou scaling rules ajustées)
- [ ] **Metrics** : même protocole éval (top-1, top-5, throughput)
- [ ] **Logs** : courbes loss/acc matchent paper (forme, valeurs)
- [ ] **Ablations** : composants clés testés individuellement

## 14. Common Replication Pitfalls

Quels sont les pièges fréquents en réplication ?
?
**Réponse:**
| Piège | Solution |
|---|---|
| **Différente augmentation** | Utiliser transforms exacts du paper (souvent dans appendix/code) |
| **Mauvais LR schedule** | Vérifier warmup steps, cosine vs step, epochs totaux |
| **Weight decay mal appliqué** | AdamW ≠ Adam + weight_decay (decoupled) |
| **Batch size différent** | Scaling LR linéaire : `lr_new = lr_orig * (bs_new / bs_orig)` |
| **Seed non fixée** | Fixer tous seeds + `cudnn.deterministic=True` |
| **Prétraining vs from-scratch** | Paper souvent pré-entraîné JFT-300M puis fine-tune ImageNet |
| **Métriques différentes** | Top-1 vs Top-5, single-crop vs multi-crop eval |

## 15. From Replication to Application

Comment adapter un paper répliqué à son propre problème ?
?
**Réponse:**
1. **Répliquer d'abord** : valider sur benchmark original (ImageNet, CIFAR)
2. **Transfer learning** : charger weights pré-entraînés, remplacer head
3. **Adapter data** : même preprocessing, augmentation adaptée domaine
4. **Ajuster hyperparams** : LR plus bas, moins d'epochs, early stopping
5. **Monitor** : TensorBoard + validation metrics
6. **Itérer** : ablation sur composants (augmentation, head, freeze strategy)

## 16. Paper Replication Workflow

Workflow recommandé pour répliquer un paper ?
?
**Réponse:**
```
1. Trouver paper + code officiel (PapersWithCode, GitHub, arXiv)
2. Lire paper : architecture, hyperparams, données, résultats
3. Créer squelette minimal (modèle + data + train loop)
4. Implémenter composants un par un (patch embed → encoder → head)
5. Tester chaque composant isolément (shapes, forward/backward)
6. Entraîner sur petit subset (overfit 1 batch → sanity check)
7. Entraîner complet, comparer courbes/logs au paper
8. Debug si écart : vérifier hyperparams, augmentations, seeds
9. Documenter : config, résultats, différences, lessons learned
10. Adapter à propre problème (fine-tune, nouveaux data)
```