
## Minipage
- Using `minipage` for complex designs and float lefts and rights:
```latex
\begin{minipage}{0.1\textwidth}
    \begin{center}
        \includegraphics[width=1.5cm]{cea}
    \end{center}
\end{minipage}%
\begin{minipage}{0.9\textwidth}
        \textbf{Stage Développement logiciel scientifique (simulation radiations) - CEA} \hfill \small Saclay, Juin - Juillet 2023 \\
        \small Réécriture en Python d'un logiciel d'analyse sectorielle 3D pour le calcul des doses de radiations spatiales sur les satellites. Correction de bugs, amélioratgion des performance via une librairie C propre au projet. Développement d'un composant logiciel de modélisation 3D avec Three.js pour la visuallisation de la structure du satellite.
        \\ \underline{Compétences utilisés:} Python, Analyse sectorielle, Threejs, Git, \LaTeX, C, Matplotlib, Numpy
        \\[2pt]
\end{minipage}
```
Renders to:
![[latex_exemple_minipage.png]]

##