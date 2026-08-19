## La formule générale du WACC (Weighted Average Cost of Capital)
**CMPC** en français : Coût Moyen Pondéré du Capital)
Taux de rentabilité minimum exigé par l'ensemble des apporteurs de capitaux (actionnaires et créanciers) pour financer l'entreprise --> Combien les investisseur sont prêt à préter (taux d’intérêt en gros)

$$WACC = \left( \frac{E}{E + D} \times K_e \right) + \left( \frac{D}{E + D} \times K_d \times (1 - T) \right)$$

- $E$ : Valeur de marché des capitaux propres (_Market Cap_)
- $D$ : Valeur de marché de la dette financière nette
- $E + D$ : Valeur totale du capital de l'entreprise
- $K_e$ : Coût des capitaux propres (_Cost of Equity_)
- $K_d$ : Coût de la dette brute (_Cost of Debt_)
- $T$ : Taux d'impôt sur les sociétés (le terme $(1 - T)$ reflète le bouclier fiscal, car les intérêts de la dette sont déductibles d'impôt)

### Calculer le Coût des Capitaux Propres ($K_e$)
$$K_e = R_f + \beta \times ERP$$
- **$R_f$ (Taux sans risque) :** Rendement d'une obligation d'État à 10 ans (ex. _Bund_ allemand ou _US 10Y Treasury_, souvent entre 2,5 % et 4 %).
- **$\beta$ (Bêta de l'action) :** Mesure la volatilité du titre par rapport au marché :
    - $\beta = 1$ : Risque identique au marché.
    - $\beta > 1$ : Plus volatil/cyclique (ex. Tech, Luxe).
    - $\beta < 1$ : Moins volatil/défensif (ex. Santé, Utilitaires).
- **$ERP$ (Prime de risque du marché) :** Rendement supplémentaire exigé pour investir en actions plutôt qu'en obligations d'État (historiquement entre 4,5 % et 6 %).
### Calculer le Coût de la Dette ($K_d$)
Le coût de la dette est le taux d'intérêt moyen auquel l'entreprise emprunte :
$$K_d = \frac{\text{Charges d'intérêts annuelles}}{\text{Dette financière totale brute}}$$
_(Alternative plus précise pour les grandes entreprises cotées : le rendement à l'échéance / _Yield to Maturity_ de leurs obligations en circulation)._


### 3. Exemple concret pas à pas
Imaginons une entreprise avec les paramètres suivants :
- **Capitalisation boursière ($E$) :** 800 M€ (80 % du total)
- **Dette nette ($D$) :** 200 M€ (20 % du total) $\rightarrow$ Total $E + D = 1\,000\text{ M€}$
- **Taux sans risque ($R_f$) :** 3,0 %
- **Bêta ($\beta$) :** 1,2
- **Prime de risque de marché ($ERP$) :** 5,0 %
- **Coût de la dette ($K_d$) :** 4,5 %
- **Taux d'impôt ($T$) :** 25 %

#### Étape 1 : Coût des fonds propres ($K_e$)
$$K_e = 3{,}0\% + (1{,}2 \times 5{,}0\%) = 3{,}0\% + 6{,}0\% = \mathbf{9{,}0\%}$$
#### Étape 2 : Coût de la dette après impôt ($K_d \times (1 - T)$)
$$K_d \times (1 - 0{,}25) = 4{,}5\% \times 0{,}75 = \mathbf{3{,}375\%}$$
#### Étape 3 : Pondération finale du WACC
$$WACC = (0{,}80 \times 9{,}0\%) + (0{,}20 \times 3{,}375\%) = 7{,}20\% + 0{,}675\% = \mathbf{7{,}875\%}$$
Ce taux de **~7,9 %** est le taux d'actualisation à utiliser dans le modèle DCF.