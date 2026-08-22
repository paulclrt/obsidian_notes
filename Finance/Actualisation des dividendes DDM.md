| **Critère**              | **DCF (Discounted Cash Flow)**                                                   | **Modèle d'actualisation des dividendes (DDM / Gordon Shapiro)**                                            |
| ------------------------ | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Flux actualisé**       | **Free Cash Flow** (capacité réelle de l'entreprise à générer du cash)           | **Dividendes versés** (cash effectivement distribué aux actionnaires)                                       |
| **Périmètre**            | Évalue l'ensemble de l'entreprise (actifs opérationnels)                         | Évalue uniquement la part perçue directement par l'actionnaire                                              |
| **Taux d'actualisation** | **WACC** (coût moyen pondéré du capital) pour le FCF to Firm                     | **$K_e$** (coût des capitaux propres / rendement exigé par l'actionnaire)                                   |
| **Cas d'usage idéal**    | Entreprises en croissance, cycliques ou qui réinvestissent massivement leur cash | Entreprises matures, stables, avec une politique de dividende prévisible (banques, assurances, utilitaires) |

Le **DDM** (_Dividend Discount Model_, ou modèle de Gordon-Shapiro dans sa version la plus connue) repose sur le principe que **le juste prix d'une action est égal à la somme actualisée de tous les dividendes futurs qu'elle versera à l'actionnaire**.

Contrairement au DCF qui évalue l'entreprise dans sa globalité via le WACC et la dette, le DDM calcule **directement la valeur par action pour l'investisseur** en utilisant son coût des capitaux propres ($K_e$).

### 1. La formule classique : Modèle de Gordon-Shapiro (Croissance constante)

Lorsque les dividendes augmentent à un taux régulier et prévisible à l'infini, la formule se simplifie en une série géométrique :
$$P_0 = \frac{D_1}{K_e - g}$$
- $P_0$ : Juste valeur intrinsèque de l'action aujourd'hui.
- $D_1$ : Dividende attendu pour l'année prochaine ($D_1 = D_0 \times (1 + g)$).
- $K_e$ : Taux de rendement exigé par l'actionnaire (calculé via le MEDAF / CAPM).
$$
K_e = R_f +\beta(R_m-R_f)
$$
avec $Rf$ le taux sans risque. $\beta$ le sensibilité de l'action aux mouvement du marché et $R_m-R_f$ la prime de risque du marché (rendement attendu par les investisseurs sinon ils vont se tourner vers les obligations etc sans risque). Autres explication sur [[WCAA et CPMM (Cout moyen pondere du capital)]]
- $g$ : Taux de croissance annuel perpétuel estimé du dividende (avec obligatoirement $K_e > g$).

Il y a un exercice de moi qui l'applique à Total (très mal appliqué mais on apprend doucement): [[me_learning_DDM_on_total.ods]]
### 2. Le DDM multi-périodes (2 phases de croissance)

En pratique, une entreprise peut connaître une phase de forte croissance de ses dividendes pendant quelques années avant de stabiliser sa distribution. On découpe alors le calcul en deux étapes :
1. **Phase 1 :** Actualisation des dividendes prévus sur les $n$ premières années.
2. **Phase 2 :** Valeur terminale calculée avec Gordon-Shapiro à partir de l'année $n+1$, puis actualisée au présent.

### 3. Exemple concret pas à pas (DDM à 2 phases)

Prenons le cas d'une grande entreprise de services aux collectivités (_Utilities_) :
- **Dernier dividende versé ($D_0$) :** 3,00 € par action
- **Phase 1 (Années 1 à 3) :** Croissance des dividendes à **6 % / an**
- **Phase 2 (Année 4 et au-delà) :** Croissance perpétuelle stabilisée ($g$) à **2,5 % / an**
- **Rendement exigé par l'actionnaire ($K_e$) :** **8,0 %**
#### Étape 1 : Projection et actualisation des dividendes (Années 1 à 3)

- **Année 1 :** $D_1 = 3{,}00 \times 1{,}06 = 3{,}18\text{ €} \longrightarrow \frac{3{,}18}{(1{,}08)^1} = \mathbf{2{,}94\text{ €}}$
- **Année 2 :** $D_2 = 3{,}18 \times 1{,}06 = 3{,}37\text{ €} \longrightarrow \frac{3{,}37}{(1{,}08)^2} = \mathbf{2{,}89\text{ €}}$
- **Année 3 :** $D_3 = 3{,}37 \times 1{,}06 = 3{,}57\text{ €} \longrightarrow \frac{3{,}57}{(1{,}08)^3} = \mathbf{2{,}83\text{ €}}$
**Somme des dividendes actualisés = 8,66 €**

#### Étape 2 : Calcul de la Valeur Terminale (au bout de la 3ᵉ année)

Le dividende de l'année 4 passe au régime de croissance perpétuelle ($g = 2{,}5\%$) :
$$D_4 = D_3 \times (1 + g) = 3{,}57 \times 1{,}025 = 3{,}66\text{ €}$$
Valeur du titre à l'année 3 :
$$P_3 = \frac{D_4}{K_e - g} = \frac{3{,}66}{0{,}08 - 0{,}025} = \frac{3{,}66}{0{,}055} = 66{,}55\text{ €}$$
Actualisation de cette valeur au présent :
$$\text{Valeur Terminale actualisée} = \frac{66{,}55}{(1{,}08)^3} = \mathbf{52{,}83\text{ €}}$$

#### Étape 3 : Juste prix de l'action
$$\text{Valeur intrinsèque} = 8{,}66\text{ €} + 52{,}83\text{ €} = \mathbf{61{,}49\text{ €}}$$
> **Lecture boursière :**
> - Si l'action cote **48 €** sur le marché : le titre offre une marge de sécurité d'environ 22 % $\rightarrow$ opportunité d'achat intéressante.
> - Si l'action cote **75 €** : le marché paie le flux de dividendes plus cher que son rendement théorique $\rightarrow$ surévaluation.

### Forces et limites du modèle
- **Points forts :** Très simple à mettre en œuvre, direct (pas besoin d'estimer la dette ni le WACC), parfaitement adapté aux valeurs de rendement.
- **Limites majeures :** Inutilisable pour les entreprises sans dividende (croissance, tech), très sensible au différentiel $(K_e - g)$, et ignore le cash conservé par l'entreprise pour ses réinvestissements.