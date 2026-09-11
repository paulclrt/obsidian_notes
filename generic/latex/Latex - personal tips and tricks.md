
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

## Lists

Pour enlever la marge à gauche... ainsi que les espaces entre les items
```latex
 \begin{itemize}[noitemsep, leftmargin=5pt]
        \item Français: Natif
        \item Anglais: C1 \\ \quad (TOEIC 2024: 965)
        \item Espagnol: B1
        \item Russe: A1
\end{itemize}
```
![[list.png]]
Instead of:
![[list_no_format.png]]

## Ecrire un document en français et pas avoir tout qui foire

```latex
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
```

## Marges

```latex
\usepackage[hmargin=1cm, vmargin=1cm, a4paper]{geometry}      % Bonnes marges pour un CV


\usepackage[a4paper, total={6in, 8in}]{geometry}              % a document using A4-sized paper with a text area which shouldn't exceed 6 inches wide and 8 inches high
\usepackage[legalpaper, landscape, margin=2in]{geometry}      % legal paper size + landacpe and 2inch margin
```


The [`layout` package](https://ctan.org/pkg/layout?lang=en) provides a very convenient solution to _visualizing_ the document's current layout. It provides two commands: `layout` and `layout*` which draw a graphic representing the current layout. The starred version (`layout*`) recalculates the internal values used to draw the graphic.
It creates this:
![[layout.png|311]]
Adapted to your curent document settings.
Every element corresponds to a `geometry` package layout parameters

`textwidth` - Corresponds to element 8 in the graphic.
`textheight` - Element 7 in the graphic.
`total` - Depends on other parameters, by default defines the dimensions of the Body, but can be combined with the `includehead`, `includefoot`, `includeheadfoot` and `includemp` commands to change the dimensions of Header, the Body, the Footer and the Margin Notes altogether.
`left`, `lmargin`, `inner` - These three parameters change the length of the left margin. Elements 1 and 3 in the graphic, combined.
`right`, `rmargin`, `outer` - These three parameters change the length of the right margin. Elements 9 and 10 in the graphic, combined.
`top`, `tmargin` - These two parameters represent elements 2 and 6 in the graphic, combined.
`bottom`, `bmargin` - These two parameters set the distance from the bottom edge of the document to its baseline.
`headheight` - Height of the header
`headsep` - Separation between header (baseline) and text body. Element 6 in the graphic.
`footnotesep` - Separation between the bottom of text body (baseline) and the top of footnote text.
`footskip` - Distance separation between baseline of last line of text and baseline of footer.
`marginparwidth`, `marginpar` - Width of the margin notes. Element 10 in the graphic.


```latex
\usepackage{layout}


\layout*
\layout % either of these
```
## Page numbering

```latex
\pagenumbering{gobble} % pas de numéros de pages
```
- `arabic`: use Arabic numerals (1, 2, 3, ...)
- `alph`: use lowercase letters (a, b, c, ...)
- `Alph`: use uppercase letters (A, B, C, ...)
- `roman`: use lowercase roman numerals (i, ii, iii, ...)
- `Roman`: use uppercase roman numerals (I, II, III, ...)

Met ça où tu veux dans ton doc ça change le numérotage, passde arabic a roman puis de nouveau à arabic stv

## Images

```latex
\usepackage{graphicx}
\graphicspath{ {./images1/}{./images2/} }                    % set the lookup folders for images

\includegraphics[scale=1.5]{overleaf-logo}                   % scale the iamge size
\includegraphics[width=5cm, height=4cm]{overleaf-logo}       % set height, width
\includegraphics[width=\textwidth]{universe}                 % full page width
\includegraphics[scale=1.2, angle=45]{overleaf-logo}         % angles
``` 

Positionning:

 ```latex
\begin{figure}[h]
\includegraphics[width=8cm]{Plot}
\end{figure}
 ```

|Parameter|Position|
|---|---|
|h|Place the float _here_, i.e., _approximately_ at the same point it occurs in the source text (however, not _exactly_ at the spot)|
|t|Position at the _top_ of the page.|
|b|Position at the _bottom_ of the page.|
|p|Put on a special _page_ for floats only.|
|!|Override internal parameters LaTeX uses for determining "good" float positions.|
|H|Places the float at precisely the location in the LaTeX code. Requires the `float` package, though may cause problems occasionally. This is somewhat equivalent to h!.|
Wrapping text around figures:
```latex
\begin{wrapfigure}{r}{0.25\textwidth} %this figure will be at the right
    \centering
    \includegraphics[width=0.25\textwidth]{mesh}
\end{wrapfigure}

There are several ways to plot a function of two variables, 
depending on the information you are interested in. For 
instance, if you want to see the mesh of a function so it 
easier to see the derivative you can use a plot like the 
one on the left.

\begin{wrapfigure}{l}{0.25\textwidth}
    \centering
    \includegraphics[width=0.25\textwidth]{contour}
\end{wrapfigure}

On the other side, if you are only interested on
certain values you can use the contour plot, you 
can use the contour plot, you can use the contour 
plot, you can use the contour plot, you can use 
the contour plot, you can use the contour plot, 
you can use the contour plot, like the one on the left.
```
![[images_in_text.png|615]]

here are the available positions:

| r   | R   | right side of the text                                 |
| --- | --- | ------------------------------------------------------ |
| l   | L   | left side of the text                                  |
| i   | I   | inside edge–near the binding (in a _twoside_ document) |
| o   | O   | outside edge–far from the binding                      |

## figures

```latex
\begin{figure}[h]
\caption{Example of a parametric plot ($\sin (x), \cos(x), x$)}
\centering
\includegraphics[width=0.5\textwidth]{spiral}
\end{figure}
```
![[caption_above_figure.png|466]]

References:

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.25\textwidth]{mesh}
    \caption{a nice plot}
    \label{fig:mesh1}
\end{figure}

As you can see in the figure \ref{fig:mesh1}, the 
function grows near 0. Also, in the page \pageref{fig:mesh1} 
is the same example.
```
![[figures_refereences.png|683]]

`label{fig:mesh1}`
This will set a label for this figure. Since labels can be used in several types of elements within the document, it's a good practice to use a prefix, such as `fig:` in the example.

`\ref{fig:mesh1}`
This command will insert the number assigned to the figure. It's automatically generated and will be updated if insert some other figure before the referenced one.

`\pageref{fig:mesh1}`
This prints out the page number where the referenced image appears.

## List of figures

![[list_fo_figures.png]]

```latex
\listoffigures
```


## List of tables
```latex
\listoftables

% To change the names dispayed:
\renewcommand{\listfigurename}{List of plots}
\renewcommand{\listtablename}{Tables}
```
![[list_of_tables_renames.png]]

## Table of contents

```latex
\tableofcontents


... your text

\addcontentsline{toc}{section}{Unnumbered Section}
\section*{Unnumbered Section}


% to change the name of the table of content:
\renewcommand*\contentsname{Summary}
```
To manually add entries, for example when you want an unnumbered section, use the command `\addcontentsline`
![[renaming_toc.png]]



## Glossary

Seems overblown feature. More details here: https://www.overleaf.com/learn/latex/Glossaries


## Multi files latex projects

```
main.tex
sections/section2.tex
setions/introduction.tex
```

 ```latex
 \usepackage{subfiles}
 
 ...
 \subfile{sections/introduction}
 ...
 ```
Put this in thesubfiles:
```latex
\documentclass[../main.tex]{subfiles}
```

or for more details checkout teh `standalone` package: https://www.overleaf.com/learn/latex/Multi-file_LaTeX_projects

## Fonts
https://www.overleaf.com/learn/latex/Font_typefaces <-- list all fonts availbles

```latex
\usepackage[T1]{fontenc}
\usepackage{tgbonum}

% for specific sections
{\fontfamily{qcr}\selectfont
This text uses a different font typeface
}
```

![[fonts.png]]

## Footer notes

The `\footnote` command is the core LaTeX command for creating footnotes and takes two forms:
- `\footnote{_text for footnote_}`: This inserts an (automatically-generated) superscript number, called the footnote _marker_, into the document text and also creates the corresponding footnote at the bottom of the page, containing the corresponding footnote _marker_ and `_text for footnote_`.
- `\footnote[_number_]{_text for footnote_}`: This form of the command uses the optional value `_number_` to create the superscript footnote _marker_; it also inserts the corresponding footnote at the bottom of the page, containing the identifying footnote marker (`_number_`) and `_text for footnote_`.
![[footer_notes.png]]

Very nicly explained: https://fr.overleaf.com/learn/latex/Footnotes