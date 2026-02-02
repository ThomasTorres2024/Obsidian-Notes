---
title: The Divergence Theorem
tags: 
draft: "false"
---
# The Divergence Theorem
We refer to this result also as the Gauss-Green Theorem". This allows us to avoid calculation of [[Surface Integral]]s. This is also a 3D analog of [[Green's Theorem]] for [[Flux]]. 

If $S$ is a closed surface that encloses our surface $D$, and $\vec{n}$ is oriented outwards, and $\vec{F}$ is defined and differentiable everywhere in $D$, then we can actually express our closed surface integral as a triple integral:
$$\underset{ S \;}{ {\rlap{\mspace{1mu} \boldsymbol{\bigcirc}}{\rlap{\int}{\;\int}}} } \vec{F} \cdot d\vec{S}= \iiint_{D} \text{div}(\vec{F})\cdot dV $$
We need to note that our [[Divergence]] is different for 3 dimensions. We define our divergence for the vector field, $\vec{F}=P\hat{i}+Q\hat{j}+R\hat{k}$ as:
$$\text{div}(\vec{F})=P_{x}+Q_{y}+R_{z}$$
# 2D Divergence Theorem Proof:
2D Divergence Theorem Proof:
Let us consider $\vec{F}=\langle P,Q\rangle$, over a simple rectangular domain $D = [a,b] \times [c,d]$. 
```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[domain=0:4] % Set default domain
    % Draw grid and axes
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};


    % Plot f(x) = sin(x) (note the 'r' for radians)
    \draw[color=blue, domain=1:3] plot (\x,1) node[right] {$C_1$};
    \draw[color=blue, domain=1:3] plot (3,\x) node[above] {$C_2$};
    \draw[color=blue, domain=1:3] plot (\x,3) node[right] {$C_3$};
    \draw[color=blue, domain=0:2] plot (1,3-\x) node[right] {$C_4$};
    
	  

	\filldraw (1, 0) circle[radius=1.5pt];
	\node[below left] at (1, 0) {a};
	
		\filldraw (3, 0) circle[radius=1.5pt];
	\node[below left] at (3, 0) {b};

	  	\filldraw (0, 1) circle[radius=1.5pt];
	\node[below left] at (0, 1) {c};
	
		  	\filldraw (0, 3) circle[radius=1.5pt];
	\node[below left] at (0, 3) {d};



\end{tikzpicture}
\end{document}
```
We can decompose our region into 4 separate [[Line Integral]]s, such that (recall the definition of [[Flux]]):
$$\oint \vec{F}\cdot \textbf{n}ds=\sum_{i=1}^4 \int_{C_1}\vec{F}\cdot (\textbf{n}_i)ds=\int_{a}^b \vec{F}\cdot -\hat{j}ds+ \int_{c}^d \vec{F}\cdot \hat{i}ds+ \int_{b}^a \vec{F}\cdot \hat{j}ds+ \int_{d}^c \vec{F}\cdot -\hat{i}ds  $$
$$= \int_{b}^a -Q(t,c)dt+\int_{c}^dP(b,t)dt + \int_{a}^bQ(t,d)dt+\int_c^d-P(a,t)dt$$
$$=\int_{c}^d [P(b,t)-P(a-t)]dt+\int_a^b[Q(t,d)-Q(t,c)]dt$$
$$=\int_c^d \int_a^b \left(\frac{\partial P}{\partial x} \right)dxdy+\int_b^a \int_d^c \left(\frac{\partial Q}{\partial y}\right)dydx$$
$$= \int_c^d \int_a^b \left(\frac{\partial P}{\partial x} \right)dxdy+\int_c^d \int_a^b \left(\frac{\partial Q}{\partial y}\right)dydx$$
(Using [[Fubinni's Theorem]])
$$=\int_c^d \int_a^b \left(\frac{\partial P}{\partial x} +\frac{\partial Q}{\partial y}\right)dydx =\int_c^d\int_a^b \text{div}(\vec{F})$$
	$$\therefore \int_c^d\int_a^b \text{div}(\vec{F})= \oint \vec{F} \cdot \textbf{n}ds$$
Therefore, we can relate the [[Flux]] over a simple square closed region to that of the [[Divergence]] of the [[Vector Field]] over the bounds of that region. We can go much further to generalize this idea to other curves that are [[Simply Connected]] regions, consider the following diagram, let us consider:
$$D=\{(x,y) : a\leq x \leq b, g(x) \leq y \leq h(x) \}$$
```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[domain=0:4] % Set default domain
    % Draw grid and axes
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};


    % Plot f(x) = sin(x) (note the 'r' for radians)
    \draw[color=blue, domain=1:3] plot (\x,{sqrt(\x)}) node[right] {$C_1$};
    \draw[color=blue, domain=1.73205080757:3+0.225] plot (3,\x) node[right] {$C_2$};
    \draw[color=blue, domain=1:3] plot (\x,{sqrt(\x+2)+1} ) node[above] {$C_3$};
    \draw[color=blue, domain=0:1.73205080757] plot (1,\x+1) node[left] {$C_4$};


\end{tikzpicture}
\end{document}
```
For a more complicated region (this looks slightly linear here, this is meant to be an arbitrary region $D$), we can express the [[Flux]] of the region by iteratively taking slices of the region along different boundary conditions: 
$$\int_c^d \dots = \int_c^{g(x)} \dots + \int_{g(x)}^{h(x)} \dots + \int_{h(x)}^{d} \dots = \int_{g(x)}^{h(x)} \dots$$
(I can't really tell how we obtain this, it seems like we are partitioning this region into square bound regions and some that are non-square that 1 variable calculus handles)

If $c=g(x)$ and $d=h(x)$, then, the argument above, we can lastly express the following for any [[Simply Connected]] region:
$$\int_{\partial D} \vec{F}\cdot \textbf{n} ds=\iint_D\text{div}(\vec{F})dxdy$$
Furthermore, this idea can be extended to regions which are NOT [[Simply Connected]]. Let us consider the following (ignore the fact that it's circular, this not relevant, as long as it is punctured and has a hole, but otherwise is connected).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.2]

  % Outer and inner radii
  \def\R{3}
  \def\r{1.6}

  % Shaded annulus
  \fill[gray!30, even odd rule]
    (0,0) circle (\R)
    (0,0) circle (\r);

  % Outer and inner boundaries
  \draw (0,0) circle (\R);
  \draw (0,0) circle (\r);

  % Horizontal blue line
  \draw[blue, thick] (-\R,0) -- (\R,0);

  % Labels
  \node at (0, 2.2) {$D_1$};
  \node at (0,-2.2) {$D_2$};

\end{tikzpicture}
\end{document}
```
Then, we can express the [[Flux]] of this region by drawing a boundary across the curves. We know that the net change in [[Flux]] from this operation is $0$, so it is valid and we can compute this result. Now our single flux integral becomes 2 flux integrals:
$$\int_{\partial D} \vec{F}\cdot \textbf{n}ds=\int_{\partial D_1}\vec{F}\cdot \textbf{n}dS+\int_{\partial D_2}\vec{F}\cdot \textbf{n}dS$$
But notice by the above previously established fact, we can apply the divergence theorem again and obtain:
$$=\iint_{\partial D_1}\text{div}(\vec{F})dxdy+\iint_{\partial D_2}\text{div}(\vec{F})dxdy$$
Therefore we obtain for punctured regions that can be decomposed into a finite set of [[Simply Connected]] and for [[Simply Connected]] regions that:
$$ \oint\vec{F}\cdot \textbf{n}ds  =\sum_{i=1}^n \iint_{\partial D_i} \text{div}(\vec{F})\cdot \textbf{n}dS$$

#### Example 1.) Sphere
Consider the sphere of radius $a$ centered at the origin through the vector field $\vec{F}=z\hat{k}$ Green's theorem allows us to express our flux integral as:
$$\underset{ S \;}{ {\rlap{\mspace{1mu} \boldsymbol{\bigcirc}}{\rlap{\int}{\;\int}}} } z\hat{k} \cdot \hat{n} \cdot ds= \iiint_{D} \text{div}(z\hat{k})\cdot dV = \iint_{D}dV= \dfrac{4}{3} \pi a^3 $$
---
# Issues with Integration
Say if we have a volume region that is not vertically simple, we can cut it into regions which actually are vertically simple, and the flow in two different parts cancels out. 