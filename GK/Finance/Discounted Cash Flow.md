
**DCF: Discounted Cash Flow**
1. Projeter les flux de trésorerie disponibles ([[FCF (Free cash flow)]]) sur 5 à 10 ans.
2. Actualiser ces flux au présent en utilisant un taux d'actualisation (WACC), qui intègre le coût du capital et le risque.
3. Additionner la valeur terminale pour obtenir la valeur intrinsèque par action.

> **Marge de sécurité** (généralement 20 % à 30 % de décote par rapport à votre estimation de la valeur intrinsèque) avant d'envisager un investissement.


### Exemple : Valorisation par DCF (_Discounted Cash Flow_)
Prenons une entreprise hypothétique **Alpha Corp** avec les données de départ suivantes :
- **Free Cash Flow initial ($FCF_0$) :** 100 M€
- **Horizon de projection explicite :** 5 ans
- **Croissance estimée des FCF (Années 1 à 5) :** 8 % par an
- **Taux d'actualisation ($WACC$) :** 9 % (coût moyen pondéré du capital) ---> Voir [[WCAA et CPMM (Cout moyen pondere du capital)]]
- **Taux de croissance perpétuelle ($g$) :** 2,5 % (croissance à long terme de l'économie)
- **Dette nette :** 150 M€
- **Nombre d'actions :** 50 millions d'actions

#### Étape 1 : Projection et actualisation des FCF sur 5 ans

Formule du flux actualisé : $\text{FCF actualisé} = \frac{FCF_t}{(1 + WACC)^t}$
- **Année 1 :** $100 \times 1{,}08 = 108{,}0\text{ M€} \longrightarrow \frac{108{,}0}{(1{,}09)^1} = \mathbf{99{,}08\text{ M€}}$
- **Année 2 :** $108 \times 1{,}08 = 116{,}6\text{ M€} \longrightarrow \frac{116{,}6}{(1{,}09)^2} = \mathbf{98{,}17\text{ M€}}$
- **Année 3 :** $116{,}6 \times 1{,}08 = 126{,}0\text{ M€} \longrightarrow \frac{126{,}0}{(1{,}09)^3} = \mathbf{97{,}27\text{ M€}}$
- **Année 4 :** $126{,}0 \times 1{,}08 = 136{,}0\text{ M€} \longrightarrow \frac{136{,}0}{(1{,}09)^4} = \mathbf{96{,}38\text{ M€}}$
- **Année 5 :** $136{,}0 \times 1{,}08 = 146{,}9\text{ M€} \longrightarrow \frac{146{,}9}{(1{,}09)^5} = \mathbf{95{,}50\text{ M€}}$
**Somme des FCF actualisés (Années 1 à 5) = 486,40 M€**

#### Étape 2 : Calcul de la Valeur Terminale (TV)
La valeur terminale représente la valeur de tous les flux au-delà de la 5ᵉ année :
$$\text{Valeur Terminale à l'année 5} = \frac{FCF_5 \times (1 + g)}{WACC - g} = \frac{146{,}9 \times 1{,}025}{0{,}09 - 0{,}025} = \frac{150{,}57}{0{,}065} = 2\,316{,}50\text{ M€}$$

Actualisation de la Valeur Terminale au présent :
$$\text{TV actualisée} = \frac{2\,316{,}50}{(1{,}09)^5} = \mathbf{1\,505{,}55\text{ M€}}$$
#### Étape 3 : Du bilan à la juste valeur par action
1. **Valeur d'Entreprise ($EV$) :** $486{,}40 + 1\,505{,}55 = \mathbf{1\,991{,}95\text{ M€}}$
2. **Valeur des Capitaux Propres (_Equity Value_) :** $EV - \text{Dette Nette} = 1\,991{,}95 - 150 = \mathbf{1\,841{,}95\text{ M€}}$
3. **Valeur intrinsèque par action :** $\frac{1\,841{,}95\text{ M€}}{50\text{ M d'actions}} = \mathbf{36{,}84\text{ €}}$

> **Décision d'investissement :**
> - Si l'action cote actuellement **26 €** : elle présente une décote de ~30 % $\rightarrow$ **Marge de sécurité respectée (Achat envisageable)**.
> - Si l'action cote **45 €** : le titre intègre des attentes supérieures au scénario retenu $\rightarrow$ **Surévaluation**.