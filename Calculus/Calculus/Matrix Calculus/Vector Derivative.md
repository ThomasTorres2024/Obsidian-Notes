---
title: Vector Derivative
draft: "False"
tags:
  - Calculus
  - VectorCalculus
---
# Vector Derivative 
Let $x,b \in \mathbb{R}^n$. Furthermore, let $b$ be a constant vector. Then:
$$\vec{ b}^T \vec{ x} = \vec{ x}^T \vec{b}$$
And the [[derivative]] is given by:
$$\frac{d}{dx} (\vec{b}^\vec{T} x)= \frac{d}{dx}(\vec{x}^Tb)=\vec{b}$$
This should make sense since obtain the following [[Multivariable Functions]] from:
$$\vec{b}^T \vec{x} = \sum_{i=1}^n b_{i}x_{i}$$
And thus:
$$\nabla (\vec{b}^T \vec{x}) = \langle b_{1},b_{2}, \dots, b_{n} \rangle  \iff \nabla(\vec{b}^T \vec{x})_{i}=b_{i}$$
