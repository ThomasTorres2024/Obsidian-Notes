---
title: Divergence
tags: 
draft: "false"
---
# Geometric Interpretation of the [[Divergence]]
The [[Divergence]] can be thought of using a physical intuition. We can think of it as the amount of fluid flowing out of some region. This gives rise to a geometric definition. Let $B_r$ be the ball with radius $r$ and let $P$ be the origin, for some vector field, $\vec{F}$:
$$\text{div} \vec{F}(P)= \lim_{r\to0^+} \frac{\large \iint_{\partial B_r}F\cdot dS}{\text{vol}(B_r)}$$
As $r \to 0^+$, the ball $B_r$ shrinks down to $P$. 

Intuitively I think this is a ratio between the total amount that the vector field is aligned with the cross product between the vector field and the vector orthogonal to the force. Intuitively we can think of this as the amount that is leaking out of the solid at this point. 

The [[Divergence]] at point $P$ is denoted by $\text{div} \vec{F}(P)$ which is the "flux density" at $P$. 

We can interpret [[Divergence]] as $\text{div}(F)>0 \implies$ fluid is leaking over some region. We can think of this as being a "source", where everything "diverges".

We can interpret that $\text{div}(F)<0 \implies$ fluid is compressing into the vector field over some region. This is a "sink", where everything "converges". 

If all of our points tend toward a single point, we can think of this kind of point as a "sink", where everything is convergent. 
##### Example 1.) Calculate divergence of $r(x,y,z)=\langle x,y,z \rangle$. Find $\text{div}(r)$ at the origin using the geometric definition.


# Divergence Definition

The formula for [[Divergence]] depends upon the dimension of the [[Vector Field]] in question.  Here we make use of the "del" operator, such that for $\nabla$ in $\mathbb{R}^3$, we have that:
$$\nabla = \left\langle \frac{\partial }{\partial x},\frac{\partial }{\partial y},\frac{\partial }{\partial z} \right\rangle $$

The divergence, with components of a [[Vector Field]], $\vec{F} :\mathbb{R}^2 \mapsto \mathbb{R}^2,$  $\vec{F}=\langle P, Q\rangle$, is given by:
$$\text{div}(\vec{F})=P_{x}+Q_{y}=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}$$
For a [[Vector Field]] $\vec{F}:\mathbb{R}^3 \mapsto \mathbb{R}^3$, $\vec{F}= \langle P,Q,R \rangle$, then the [[Divergence]] is defined by the following, which we represent symbolically by $\nabla \cdot \vec{F}$ indicating the [[Dot Product]]:
$$\text{div}(\vec{F})= \nabla \cdot \vec{F}= \frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z} $$

The divergence measures how much things are diverging in a vector field. We can interpret divergence of a vector field as how much our flow is expanding. 

If we have positive divergence, we see that a fluid is expanding within a region, and if we have a negative divergence, we see that fluid is entering a system. 

For this definition of [[Divergence]], we can think of these intuitively by the amount of fluid in a [[Vector Field]] which flows in a direction of one of the three fundamental basis vectors. 

For some 2 dimensional vector field, we have a flow along the $x$ and $y$ direction. For some 3 dimensional vector field, we have a flow along the $x,y,z$ direction. The formulas for both cases reflect this particular intuition. 

[[Divergence]] in the direction of $x^+$ corresponds to positive divergence in that term, and divergence in the opposite direction corresponds to negative divergence in that term. The same can be said for the other dimensions as well. 

---
# [[Divergence]] Properties:

#### Theorem 
For any $C^2$ [[Vector Field]] $F$, $\text{div}\text{ curl}(\vec{F}) =0$:
$$\nabla \cdot (\nabla \times f)=0$$
We can prove this by computing the expression using the definition of the [[Cross Product]]:
$$\begin{align}
\nabla \cdot \nabla f = \begin{bmatrix} \hat{i} & \hat{j} & \hat{k}\\
\frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\
P & Q & R
\end{bmatrix}
\end{align}=\nabla \cdot (\hat{i} (R_y-Q_z) -\hat{j}(R_x-P_z) +\hat{k}(Q_x-P_y) $$
$$=R_{yx}-Q_{zx}-R_{xy}+P_{zy}+Q_{xz}-P_{yz} = 0$$
Due to equality of mixed [[Partial Derivative]]s, it follows that the above expression is 0:$$ \therefore \nabla \cdot (\nabla \times f)=0$$

* $\text{div}(F+G)=\text{div}(F)+\text{div}(G)$
* $\text{div}(fF)=(\nabla f)\cdot F + f \text{div}(F)$
* $\text{div}{(F \times G)}=(\text{curl}(F)\cdot (G-F)\text{curl}(G))$

---
# 2D Divergence Theorem Proof:
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

---
# Examples for Calculation of Divergence:
#### Example 1.) 
Let $\vec{F}=\langle x^2y,z,xyz \rangle$. We can compute its [[Divergence]] using the [[Divergence]] formula. 
$$\text{div}(\vec{F})= 2xy+xy =3xy$$
#### Example 2.) 
Let $\vec{F}=\langle x,xy,1 \rangle$. We can compute its [[Divergence]] using the [[Divergence]] formula. 
$$\text{div}(\vec{F})= 1+y+0=1+y$$

#### Example 3.) 
Let $\vec{F}=\langle xy,y^2-x^2 \rangle$. We can compute its [[Divergence]] using the [[Divergence]] formula. 
$$\text{div}(\vec{F})= y+2y=3y$$
#### Example 4.) Let $\vec{F}=\left\langle \frac{-y}{x^2+y^2}, \frac{x}{x^2+y^2}\right\rangle$ 
$$\text{div}(F)=P_x+Q_y=\frac{2xy}{(x^2+y^2)^2}+\frac{-2yx}{(x^2+y^2)^2}=0$$
$$\therefore \text{div}(F)=0 \implies F \text{ is divergence-free/incompressible}$$
# Examples for 2D [[Divergence]] Theorem:
#### Example 1.) 
$$\vec{F}=\langle 2xy, -y^2 \rangle $$
$$\text{div}(\vec{F})=2x-2y=0$$
Let the region be described by the ellipse given by $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$. Then via the 2d divergence theorem:
$$\int_c\vec{F}\cdot \textbf{n}dS=\iint \text{div}(\vec{F})dV_2=\iint0\cdot dV_2=0$$
