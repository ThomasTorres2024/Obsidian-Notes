---
title: Gauss's Law
tags:
  - Calculus
  - Electromagnestism
draft: "False"
---
# Gauss's Law
Consider the [[Solid Angle Vector Field]], $\mathbb{A}$:
$$\mathbb{A}= \frac{1}{x^2+y^2} \langle x,y\rangle$$
And let us consider the "Decent" region (such that we can apply the 2d [[Divergence]] Theorem, basically [[Simply Connected]] or punctured and separable into [[Simply Connected]] regions) defined by $D$. 

Suppose that $(0,0) \not \in D$ (this is a trouble spot for the [[Solid Angle Vector Field]]) then we can consider its [[Divergence]]:
$$\text{div}(\mathbb{A})= \frac{-1}{(x^2+y^2)^2} ((x^2+y^2)-2x^2) + (x^2+y^2)-2y^2)=0 $$
Therefore for this case we obtain that:
$$\int_{\partial D}\mathbb{A} \cdot \mathbf{n}dS= \iint_D \text{div}(\mathbb{A})dV_2=\iint_D0\cdot dV_2=0$$
For the second case, consider that $(0,0) \in D$. We can create some boundary condition for $\epsilon >0$ such that there is a ball around $(0,0)$ where the [[Solid Angle Vector Field]] is poorly defined. The circle surrounds the origin and is enveloped in $D$. 

Let us redefine $D$ to be an annular region:
$$D_n=\{D \textbackslash \{x,y \} \in \mathbb{R}^2, x^2+y^2 \leq \epsilon \}$$

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
Now the region can be evaluated with the following:
$$\int_{\partial D_n} \mathbb{A}\cdot \textbf{n}dS=\int_{\partial D} \mathbb{A}\cdot \mathbf{n}dS+\int_{x^2+y^2\leq \epsilon} \mathbb{A}\cdot \mathbf{n}dS=0$$
Notice that the [[Flux]] over $D_n$ should evaluate to $0$ by the above argument, since $(0,0) \not \in D_n$. Therefore we obtain that:
$$\int_{\partial D} \mathbb{A}\cdot \mathbf{n}dS=-\int_{x^2+y^2\leq \epsilon} \mathbb{A}\cdot \mathbf{n}dS=0$$
Since we are evaluating over a circular region, we have that $\mathbf{n}=\frac{\vec{r}}{r}$, the [[Position Vector Field]]. So:
$$\int_{x^2+y^2\leq \epsilon} \mathbb{A}\cdot \mathbf{n}dS= \int_0^{2\pi} \frac{1}{x^2+y^2} \langle x,y \rangle \cdot \vec{r}   dt=  \int_{0}^{2\pi}\frac{x^2+y^2}{x^2+y^2}dt=\int_{0}^{2\pi}dt=2\pi$$
Notice that our choice is independent of the size of $\epsilon$ as long as $B_\epsilon$ is contained within $D$. 

Thereby [[Gauss's Law]] states that:
$$\begin{cases}
\text{ if } (0,0) \in D : \large \iint_D \normalsize \text{div}(\mathbb{A})=2\pi \\
\text{ if } (0,0) \not \in D : \large \iint_D \normalsize \text{div}(\mathbb{A})=0
\end{cases}$$
In words, for a closed region $C$ in $\mathbb{R}^2$, if $C$ contains $(0,0)$, because the [[Solid Angle Vector Field]] is poorly defined at the origin, we get $2\pi$ as our answer by the circle insertion trick. If $(0,0) \not \in C$, then we get 0 (this can be computed via the [[The Divergence Theorem]]). 

