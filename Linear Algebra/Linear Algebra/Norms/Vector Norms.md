---
title: Vector Norms
tags: 
draft: "false"
---
# Norm Definitions

A norm is a mapping between a vector space, $\mathcal{V}$ to a field $\mathbb{F}$, where $\mathbb{F}$ is either the complex or real numbers. We should also note that [[Inner Product Spaces]] induce norms. 

A norm is a way to measure the size of a matrix, a tensor, a function, or some object. The norm should reflect aspects of our functions. We can examine some common  $p$  vector norms on the vector, $\vec{v}$. We denote a norm by double brackets:
$$ \text{Example notation for a norm: } \| \vec{v} \|$$
We denote the syntax for a general norm by:
$$\| \cdot \| : \mathcal{V} \rightarrow \mathbb{R}$$
A vector norm also must satisfy the following criteria for vectors $\vec{x},\vec{y} \in \mathcal{V}$
1. $\ | \vec{x} \| \geq 0$ $\forall \vec{x} \in \mathcal{V}$
2. $\| \vec{x} \| = 0 \Longleftrightarrow \vec{x}=\vec{0}_{v}$
3. $\| \alpha \cdot \vec{x}\|= |\alpha| \cdot \| \vec{x} \|$
4. $\|\vec{x} +\vec{y} \| \leq \| x || + \| y \|$ The triangle inequality is proved using the [[Cauchy-Schwarz Inequality]]

---
# Different Vector Norms

If $p=2$ we get the standard [[Euclidean Norm]]:
$$ \| \vec{v} \|_{2}= \sqrt{\sum_{i=1}^n v_{i}\cdot\bar{v_{i}}}   = \sqrt{v_{1}^2+v_{2}^2+\cdots+v_{n}^2}$$
If $p=1$ we get the [[Manhattan Distance]] or the "L1" norm. It is very important for signal processing:
$$\| \vec{v}\|_{1} = \sum_{i=1}^n |x_{i}|=|x_{1}|+|x_{2}|+\cdots+|x_{n}|$$
If $p=\infty$ we get the maximum of the absolute value of the component of our vector $\vec{v}$:
$$\| \vec{v} \|_{\infty}=\text{max}(|v_{i}|)$$
Generally we express our $p$ norms where $p>0$ and an integer as:
$$\| \vec{v} \|_{p}= \left( \sum_{i=1}^n |v_{i}|^p \right)^{\dfrac{1}{p}}$$
We also have the so called "0 norm", which is the number of nonzero components. This is a non-zero norm, since multiple vectors can map to $0$ that aren't the zero vector. 

#### Plots of $p$ Norms 
We can plot $p$ norms by considering the set of all vectors such that, $\|\vec{v}\|_{p}=1$. If we do this for the case where $p=2$, we get the resulting unit ball, since it's just the Euclidean distance everywhere. 
![[Pasted image 20250706000320.png]]
If we consider the $L1$ norm, we get a diamond. The unit ball, is a diamond constrained in our circle. For $p>2$ we get a figure that bounds our ball and that continues to swell outward. We end at a square which has side lengths of two when we get $p=\infty$. 

Also our degenerate case of a $p=0$ norm, we get a degenerate graph. 

---
#### The $S$ Norm
Let $S$ denote a symmetric positive definite matrix. We denote a norm with this matrix by $\| \vec{v} \|_{S}$.  For the given vector, we can express our norm using a quadratic form. Note that we also refer to this as the [[energy]] of our expression. 
$$ \| \vec{v} \|_{S}= \sqrt{\vec{v}^TS\vec{v}}$$
If  $S$ were the identity matrix, we would simply get the $L2$ norm. However, we are able to plug more things into our matrix this way. Take for instance when $S$ is:
$$S=\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$
We still get a valid norm. How do we visualize this norm? It turns out that if we compute out our expression, we would get the resulting quadratic form, and we could express the locus of all $\| \vec{v} \|_{S}=1$ for $\vec{v} \in \mathbb{R}^2$ by:
$$2v_{1}^2+3v_{2}^2=1$$
Which clearly is an ellipse if we graph out the resulting expression:
![[Pasted image 20250706001752.png]]

---
# Vector Norm Problems
One common problem is constrained optimization using norms. For instance, if we try and minimize, for some given matrix $A \in \mathbb{R}^{m \times n}$  and $\vec{b}\in\mathbb{R}^n$. 

For $L1$ the following optimization is known as [[Basis Pursuit]]:
$$\text{min}(\|\vec{x}||_{1}) \text{ such that: } A\vec{x}=\vec{b}$$
For $L2$ the following optimization is known as [[Ridge Regression]] which is similar to [[Least Squares]]
$$\text{min}(\|\vec{x}||_{2}) \text{ such that: } A\vec{x}=\vec{b}$$