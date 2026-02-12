---
title: Conservative Vector Fields
tags: 
draft: "false"
---
# Conservative Vector Field Definition
A [[vector field]], $\vec{F}$ is conservative if it satisfies the following definition for a [[Line Integral]] over a path $\vec{r}$:
$$\int_{c}\vec{F}\cdot d\vec{r}=f(p_{1})-f(p_{0})$$
Which verbally means that the line integral between any path along a vector field is really equivalent to evaluating its [[Potential]] function on the endpoints of the curve. From this, TFAE:

1. $\vec{F}$ is a conservative vector field 
2. $\int_{c}\vec{F}\cdot d\vec{r}=0$ for all simple closed curves $c$, we can think of this as two curves composing a single curve which in total must be a closed path
3. $\int_{c} \vec{F} \cdot d\vec{r}$ is path independent, that is for closed curved $S_1$ and $S_2$ between points $a$ and $b$, we have that: $$\int_{S_1} \vec{F} \cdot dS= \int_{S_2} \vec{F} \cdot dS$$
4. $\vec{F}$ is a [[Gradient Field]], meaning $\exists$ a non-unique $f(x,y,z)$ s.t. $\vec{F} = \nabla f$. 
5. $$\text{curl}(\vec{F})=0$$
6. $Mdx+Ndy=df$ is an [[Exact Differential Equation]] which is equivalent to being able to express our differential equation as the forms above as the differential 

# Proof: 
We will show that $2 \implies 3 \implies 4 \implies 2$ .
#### Pf.) $2 \implies 3$. 
Given any oriented closed curve $C$, we assume that:
$$\oint_C \vec{F} \cdot dS=0$$


```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.2]


% Points a and b
\filldraw (0,0) circle (2pt) node[below left] {$a$};
\filldraw (3,0) circle (2pt) node[below right] {$b$};

% Curve S1: a to b (wide upper arc)
\draw[thick, blue, ->]
  (0,0)
  to[out=40, in=140]
  (3,0)
  node[midway, above] {$S_1$};

% Curve S2: b to a (tighter, skewed lower path)
\draw[thick, red, dashed, ->]
  (3,0)
  to[out=-160, in=-20]
  (0,0)
  node[midway, below] {$S_2$};

\end{tikzpicture}
\end{document}
```

Let $C=S_1+S_2$, such that $S_2$ is a negative orientation, between the two points $a$ and $b$. Since $S_2$ is then a parametrization running from $b$ to $a$:  then:
$$\oint_C \vec{F} \cdot dS \implies \int_{S_1} \vec{F} \cdot dS - \int_{S_2} \vec{F} \cdot dS = 0 \iff \therefore \int_{S_1} \vec{F} \cdot dS =  \int_{S_2} \vec{F} \cdot dS $$
#### Pf.) $3 \implies 4$ 
I don't have the proof for this yet it's non trivial and hard to express 
#### Pf.) $4 \implies 5$ 
Recall the identity that $\nabla \times (\nabla f) =0 \iff \nabla \times \vec{F} =0, \text{ }  \therefore \text{curl}(\vec{F})=0$. 
#### Pf.) $5 \implies 2$ 
We can show that $\text{curl}(\vec{F})=0 \implies$ circulation around $C =0$. If $C$ is a simple closed curve, then:
$$\oint_C \vec{F} \cdot dS= \iint_S \text{curl}(\vec{F} ) \cdot ds = \iint_S 0 \cdot dS = 0$$
Therefore, the circulation around the given curve is $0$ via [[Stokes' Theorem]]. 

---
# True condition for $\oint_C \vec{F} \cdot dS=0$ given that $F =\nabla f$. 
The theorem is nearly true, however it must be the case that $F$ is defined everywhere, or that it is "undefined at a finite number of points." The true condition is more topological. If it possible to shrink closed curve $C$ such that the point it is shrunken onto is a part of where $F$ is defined, that entails that the line integral evaluates to zero. We are allowed to shrink, expand, and to translate it freely. However, we cannot cut it out or have it bypass some region where it is undefined. 