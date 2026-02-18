---
title: Gradient Search Method
tags:
  - Optimization
draft: "False"
---
# Gradient Search Method
Let us consider [[Multivariable Functions]] of the form $f : \mathbb{R}^n \to \mathbb{R}$. Recall the definitions of a [[Contour]], [[Gradient]]
$$\text{Level Set/Cntour} : \{ \vec{ x} \in \mathbb{R}^n, f(\vec{z})=k \}$$
$$\nabla f = \begin{bmatrix}
\frac{\partial f}{\partial x_{1}} & \frac{\partial}{\partial x_{2} } & \dots \frac{\partial}{\partial x_{n}} 
\end{bmatrix}^T$$
Also recall the following facts about the [[Contour]]s and [[Gradient]] over the [[feasible set]] $\Omega $
* $\vec{x}_{0} \in \Omega, \nabla f(\vec{x_{0}}) \perp \text{Level Surface}$
* $\nabla f(\vec{x_{0}})$ points in the direction of steepest increase of $f$
* The largest rate of change in all directions at $\vec{x_{0}}$ is given by $$\pm \| \nabla f(\vec{x_{0}}) \|$$
*  [[The Directional Derivative]] $$f_{\vec{d}}= \nabla f(\vec{x_{0}}) \vec{\cdot} d$$
If we are looking for [[Local Minima]] of $f$, then we want to move in the direction of: $-\nabla f(\vec{x_{0}})$, the negative gradient of $f$. 


---

Consider $\vec{A} \in \Omega$. We know the direction in which the [[Local Minima]] is positioned. 

Let us examine the one dimensional case:
$$\phi(\alpha)=f(\vec{A}-\alpha \vec{d})$$
We have the following function $\phi$:
$$\phi(\alpha \vec{d})$$
We are looking for the minimizer of $f(\alpha)$, which we denote by $\alpha^*$. 

Also note that:
$$\phi'(\alpha)= \nabla f(\vec{A}-\vec{\alpha} d) \cdot (-\vec{d})$$
And:
$$\phi'(\alpha)=0 \iff f(\vec{A}-\vec{\alpha} d) \cdot (-\vec{d}) = 0$$
Generally this is hard to obtain, so we are generally interested in using a linear approximation via a [[Taylor Series]] of $\phi'(\alpha)$:
$$\phi'(\alpha) \approx \phi'(0)+\phi''(0)\alpha$$
Generally, solving for $\alpha^*$ is a difficult thing to do. We can approximate it by doing the following:
$$\alpha^* = -\frac{\phi'(0)}{\phi''(0)}$$
It is generally easy to compute:
$$\phi'(0)= \nabla f(\vec{A})^T \vec{d}=\vec{d}^T\nabla(f(\vec{A}))$$
We can also approximate 
$$\phi''(\alpha) =\nabla^2 f(A-\vec{\alpha} d) \cdot -\vec{(d)} = \vec{d}^T\mathcal{H}_{A} \vec{d}$$Thus we obtain that:
$$\phi''(0)= \vec{d}^T $$














