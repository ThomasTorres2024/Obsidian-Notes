---
title: Piecewise Continuous
tags:
  - Functional_Analysis
draft: "False"
---
# Piecewise Continuous Function
Let $I$ be an interval. We define the set of [[Piecewise Continuous]] functions to be of the form:
$$\large PC(I) = \{ f : I \to \mathbb{C} | f \text{ is piecewise continuous} \} $$
A piecewise continuous function is continuous on $I$ except for at finitely many points $\{ x_{k} \}$. We have that everywhere along $I$ has a one sided limit which either exists, or evaluates to $\pm \infty$:
$$\large f(x_{k}^-) = \lim_{ x \to x_{k}^- } f(x) \text{ and } f(x_{k}^+) = \lim_{ x \to x_{k}^+ } f(x)$$
For example the function $f(x)=\frac{1}{x}$ on $[-\pi,\pi]$ is [[Piecewise Continuous]]:

```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}  
% Grid  
\draw[very thin,color=gray] (-4,-4) grid (4,4);  
  
% Axes  
\draw[->] (-4,0) -- (4,0);  
\draw[->] (0,-4) -- (0,4);  
  
% f(x) = 1/x (split around 0!)  
\draw[red, thick, domain=-4:-0.25, samples=200]  
plot (\x,{1/\x});  
  
\draw[red, thick, domain=0.25:4, samples=200]  
plot (\x,{1/\x})  
node[right] {$f(x)=\frac{1}{x}$};  
  
\end{tikzpicture}
\end{document}
```
Also we have that the set of [[Continuous Function]] is a subset of the set of [[Piecewise Continuous]] functions:
$$C(I) \subset PC(I)$$
