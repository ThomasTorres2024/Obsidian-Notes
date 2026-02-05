---
title: Local Minima
tags:
  - Optimization
draft: "False"
---
# # Local Minima 
The [[Local Minima]] of a function, $f : \mathbb{R}^n \to \mathbb{R}$, tells us that over some region, $D$, we have that the [[Local Minima`]], $x^*$ satisfies that:
$$f(x^*) \leq f(x), \forall x \in D$$
Note that $x^*$ is not necessarily unique, as a function may have multiple local minima.  The way that we specify $D$ is by considering some bound, $\epsilon \in \mathbb{R}$, such that:
$$D=\{x \in \mathbb{R}^n : \|x^*-x\| \leq \epsilon \}$$
Which is to say all of the vectors are within a distance ([[norm]]) of $\epsilon$ from the local minimum. 

---
# First Order Necessary Conditions for $x^*$ to be a [[Local Minima]]
Let us consider some [[Multivariable Functions]] $f$ such that $f : \mathbb{R}^n \to \mathbb{R}$ where $f$ has the [[feasible set]] $\Omega, \Omega \subseteq \mathbb{R}^n$, and that $f$ is $C^1$. 

If $x^* \in \Omega$, then $x^*$ is a local min if for any direction $\vec{d}$  that is a [[Feasible Direction]] we have that [[The Directional Derivative]] in direction $\vec{d}$ satisfies:
$$d^T [\nabla f(x)]\geq 0$$
If $x^*$ is the local minimizer, then it follows for some neighborhood around $x^*$ that:
$$f(x^*+\alpha\vec{d})\geq f(x^*)$$
Let $\alpha$ satisfy $0 < \alpha < \alpha_0$. Now we can turn this expression into a secant line, and then determine its derivative:
$$\frac{f(x^*+\alpha \vec{d}) -f(x^*) }{\alpha}, \lim_{\alpha \to 0} \frac{f(x^*+\alpha \vec{d}) -f(x^*) }{\alpha} = d^T(\nabla f(x^*))\geq 0$$
### Corollary 
If $x^* \in \Omega$ is an interior point, and a local min, then $\nabla f(x^*)=\vec{0}$. Consider any [[Feasible Direction]] $d$, then $d^T(\nabla f(x^*)) \geq 0$. Since the point is an interior point, we can make use of any $d$ in any direction. Thus, for each identity vector, $d=e_i$, we have the following:
$$d^T(\nabla f(x^*))=\frac{\partial f}{\partial x_i} \geq 0 \text{ (by FONC})$$
However, we also know that $-d$ must also be a direction since $x^*$ is an interior point. So the following must also be true:$$-d^T(\nabla f(x^*))=-\frac{\partial f}{\partial x_i} \geq 0 \text{ (by FONC})$$
However $\implies \nabla f(x^*)=0$. and simply not just something greater than or equal to 0. 