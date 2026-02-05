---
title: Boundary Orientation
tags:
  - Calculus
draft: "False"
---
# Boundary Orientation 
We say that the parametrization of a region ([[Parametrized Surfaces]]) has a positive [[Boundary Orientation]] if the interior of the region is always on the left of the boundary, if we were to picture an ant traversing it. Furthermore, we would say that a parametrization has a negative [[Boundary Orientation]] if the boundary was to the right. 

Consider the following region $D$.
```tikz 
\usepackage{tikz}
\begin{document}


\begin{tikzpicture}[scale=1.2]

% Axes
\draw[->] (-3,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-3) -- (0,3) node[above] {$y$};

% Region D (outer boundary)
\fill[gray!30]
  (-2,0)
  .. controls (-2,1.6) and (-0.5,1.8) .. (1.5,1.2)
  .. controls (3,0.8) and (3,0.2) .. (3,0)
  .. controls (3,-0.2) and (3,-0.8) .. (1.5,-1.2)
  .. controls (-0.5,-1.8) and (-2,-1.6) .. (-2,0)
  -- cycle;

% Inner circular hole
\fill[white] (-1,0) circle (0.9);
\draw (-1,0) circle (0.9);

% Label
\node at (2,1.4) {$D$};

\end{tikzpicture}



\end{document}
```
For the outer region, that is the region that does not enclose the circular part, we can see that a counter clockwise orientation would be a positive [[Boundary Orientation]], since the interior would always be to the left of something traversing the edge. Furthermore, we can see that in order for the inner circle to have a positive [[Boundary Orientation]], it must have a counter clockwise parametrization in order for the region to always be to the left of the direction of how the curve is traversed. 

Generally, for a [[Simply Connected]] region all we need for a positive [[Boundary Orientation]] is a counterclockwise orientation. For a puncture region, all we need is the outer curve to have a counterclockwise orientation, and the inner one around 

The same is essentially true if we extend the idea from regions to surfaces. 


