---
title: Triangle Inequality
tags:
  - LinearAlgebra
draft: "False"
---
# Triangle Inequality 
The [[Triangle Inequality]] we can think of as saying that the other two sides of a triangle are greater than or equal to the other side of a triangle. For vectors $x,y \in \mathcal{V}$ we formally express this using an arbitrary [[Norm]] by:
$$\large \|x +y \| \leq \|x\|+ \|y\|$$
Visually this is to say (reinforcing the intuition above)


```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}  

  
% Axes  
\draw[->] (-0.5,0) -- (4,0);  
\draw[->] (0,-0.5) -- (0,3);  
  
% Points  
\coordinate (O) at (0,0);  
\coordinate (X) at (2,1);  
\coordinate (Y) at (3.5,2);  
  
% Vectors  
\draw[->, thick, blue] (O) -- (X) node[midway, below left] {$x$};  
\draw[->, thick, red] (X) -- (Y) node[midway, above] {$y$};  
\draw[->, thick, purple] (O) -- (Y) node[midway, below right] {$x+y$};  
  
% Triangle edges  
\draw[dashed] (O) -- (Y);
 
  
\end{tikzpicture}
\end{document}
```
