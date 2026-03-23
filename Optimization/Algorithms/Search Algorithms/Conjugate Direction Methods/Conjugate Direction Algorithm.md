---
title: Conjugate Direction Algorithm
tags:
  - Optimization
draft: "False"
---
# [[Conjugate Direction Algorithm]] 
The [[Conjugate Direction Algorithm]] can be used to determine the local extrema of a [[Quadratic Form]] in $n$ many steps. We can think of this family of methods as being a cross between Newton's Method and Gradient Descent. 

Objective functions for this method are of the form:
$$f(x)=\frac{1}{2}x^TQx-x^Tb$$
Where $Q$ is a [[Positive Definite Matrix]] and symmetric, $x \in \mathbb{R}^n$. Since $Q$ has this form, if we consider its gradient:
$$Qx=b$$
Then we could solve for $x$ by taking an inverse (which is generally a really poor idea especially for large data) and obtain that:
$$x=Q^{-1}b$$
---
### Basic Conjugate Direction Algorithm: 
Given a starting point $x^{(0)}$, and $Q$ conjugate directions, $d^{(0)},d^{(1)},\dots,d^{(n-1)}$ we then have that: 
$$g^{(k)}=\nabla f(x^{(k)})=Qx^{(k)}-b$$
$$\alpha_{k}=-\frac{g^{(k)T}d^{(k)}}{d^{(k)^T}Qd^{(k)}}$$
$$x^{(k+1)}=x^{(k)}+\alpha_{k}d^{(k)}$$----
### Theorem 
For any starting point, $x^{(0)}$, the basic conjugate direction algorithm converges to the unique $x^{*}$ (the solution to $Qx=b$) in $n$ many steps, which is to say that $x^{(n)}=x^*$. 

$\textcolor{red}{Proof.)}$ Consider $$


