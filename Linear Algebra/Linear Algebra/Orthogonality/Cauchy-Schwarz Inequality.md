---
title: Cauchy-Schwarz Inequality
tags:
  - LinearAlgebra
  - Functional_Analysis
draft: "False"
---
# Proof of the Cauchy-Schwarz Inequality 

The Cauchy-Schwarz identity states that for $\vec{x},\vec{y} \in \mathcal{V}$ where $\mathcal{V}$ is an inner product space, that: 

$$|\vec{x}\cdot \vec{y}| \leq \| \vec{x} \| \| \vec{y} \|$$

Let us begin by examining $\| \beta \vec{x} - \vec{y}] \|^2$ where $\beta \in \mathbb{R}$:

$$\| \beta \vec{x} - \vec{y}] \|^2=(\beta\vec{x}-\vec{y})^T(\beta\vec{x}-\vec{y})=\beta^2\vec{x}^T\vec{x}-\beta\vec{x}^T\vec{y}-\beta\vec{y}^T\vec{x}+\vec{y}^T\vec{y}$$
$$=\beta^2\|\vec{x}\|^2-2\beta<\vec{x},\vec{y}>+\| \vec{y} \|^2 \geq 0$$
We can think of this as a quadratic equation. Since $\vec{x}$ and $\vec{y}$ belong to an inner product space, $\| \beta \vec{x} - \vec{y }\| ^2 \geq 0$. We can treat the above identity as a quadratic equation which is greater than or equal to zero at all values of $\beta$. We can use the quadratic equation to solve for its roots. 

Since the parabola opens upward and is at least centered at zero, this means that its discriminant will result in a complex value, so it must contain a negative under the radical sign. That is to say: 

$$\sqrt{(-2<\vec{x},\vec{y}>)^2-4\|x\|^2|y|^2} \in \mathbb{C}$$
Which indicates that:

$$(-2<\vec{x},\vec{y}>)^2-4\|x\|^2|y|^2\leq 0$$
$$ \Longleftrightarrow 4<\vec{x},\vec{y}>^2 \leq 4\|x\|^2|y|^2\leq $$
$$\Longleftrightarrow |\vec{x} \cdot \vec{y}| \leq \|x\||y| $$
Which finally yields the Cauchy-Schwarz inequality. 

Intuitively, I think of this inequality as a corollary from the [[Cosine]] identity. Since we know that $\text{cos}(\theta)=\dfrac{|\vec{x} \cdot \vec{y}|}{\| \vec{x} \| \| \vec{y} \|}$, we know cosine is bound between $-1$ and $1$, and for most cases, unless the vectors are oriented in the same direction and thus linearly dependent, it is the case that the hypotenuse will be greater than the numerator, so our answer would tend to have an absolute value of less than one, which would imply that the denominator is larger. I tend to think of this identity as a concretization of this rather obvious fact, since the hypotenuse in a right triangle is always the largest side. 

---
### Alternative Proof of the Cauchy-Schwarz Identity Using [[Bessel's Inequality]]
We can also prove this result using this inequality. Given a finite orthonormal set, $X=\{x_{1},x_{2},\dots,x_{n} \}$ we can prove this result. 

$Proof).$ 
Let $y=0$ then it is trivial that $|\langle x,y \rangle| \leq ||x|| \cdot ||y||$. Now assume that $y\neq0$. It is trivially true that $\frac{y}{||y||}$ is an orthonormal set, a finite one so we can apply Bessel's Inequality:
$$\left|\left\langle  x, \frac{y}{||y||}  \right\rangle \right|^2 \leq ||x|| ^2 \iff |\langle x,y \rangle|^2 \leq ||x||^2 ||y||^2$$

---
# Relevance of the [[Cauchy-Schwarz Inequality]]
The [[Cauchy-Schwarz Inequality]] has important arithmetic, geometric, and analytic consequences, namely that in any [[Inner Product]] space we define a distance to be:
$$\delta(x,y)=||x-y||=\sqrt{ \langle x-y,x-y\rangle }$$
Any such distance function must obey the following properties to be called a metric. It should namely satisfy:

1. $\delta(x,y)=\delta(y,x)$ (Symmetry)
2. $\delta(x,y)\geq0;\delta(x,y)=0 \iff x=y$ (Positive Definiteness)
3. $\delta(x,y) \leq \delta(x,z) + \delta(z,y)$ (Triangle Inequality)
4. $\delta(x,y)=\delta(x+z,y+z)$ (Invariance Under Translations)

The properties $(i),(ii),(iv)$ are the result of the particular delta function chosen. The [[Triangle Inequality]] in $3$ is a well known property that comes directly from norms. This can be proven in the following:
$$\begin{align}
||x+y||^2 =\langle x+y,x+y \rangle = ||x||^2 + \langle x,y \rangle + \langle y,x \rangle + ||y||^2 \\
= ||x||^2 + \langle x,y \rangle + \overline{\langle x, y \rangle} + \|y\|^2  \\
= ||x||^2 + 2\text{Re}(\langle x,y \rangle) + ||y||^2 \\
=\|x\|^2 + 2 |\langle x, y \rangle| + \|y\|^2 \\
\leq \|x\|^2 + 2\|x\| \cdot \|y\| + \|y\|^2  \\
= (\|x\|+\|y\|)^2  
\end{align}$$
We can obtain this same result by replacing $x\to x-z$ and $y\to z-y$ from which we get:
$$\|x-y\| \leq \|x-z\| + \|z-y\|$$
Another consequence of the [[Cauchy-Schwarz Inequality]] is that in the Euclidean Space $\mathbb{R}^n$ the expression $\frac{\langle x,y \rangle}{\|x\| \cdot \|y\|}$ is equal to the angle between the vectors, and is tantamount to stating that the absolute value of the cosine of some angle is less than or equal to 1. 

In the unitary space $\mathbb{C}^n$, we have that the Schwarz inequality becomes the Cauchy inequality, namely that for any two sequences of complex numbers $(\eta_{1},\eta_{2},\dots,\eta_{n})$ and $(\xi_{1},\xi_{2},\dots,\xi_{n})$ we have:
$$\left|\sum_{i=1}^n \xi_{i} \overline{\eta_{i}}\right|^2 \leq \sum_{i=1}^n |\xi_{i}|^2 \cdot \sum_{i=1}^n |\eta_{i}|^2$$
In the space of [[Polynomial]]s, we have the following for the Schwarz Inequality:
$$\left|\int_{0}^1 x(t)\overline{y(t)} \text{ d}t \right|^2  \leq \left(\int_{0}^1 |x(t)|^2\text{ d}t \right)   \cdot \left(\int_{0}^1 |y(t)|^2\text{ d}t \right)  $$
Another consequence is that of [[Normed Space]]s , which live between general vector spaces and inner product vector spaces. Under [[Normed Space]]s, we have [[Norm]]s which entails lengths but nothing of angles. Generally inner product spaces are normed vector spaces, but the converse of this is false. 