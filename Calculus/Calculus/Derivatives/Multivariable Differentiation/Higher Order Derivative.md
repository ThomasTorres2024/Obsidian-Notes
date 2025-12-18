---
title: Higher Order Derivatives
---
# Higher Order [[Partial Derivative]]s
In the single variable case higher order derivatives are only taken with one value:
$$f(x),f'(x),f''(x),\cdots,f^n(x)$$
For the multivariable case we need to be attentive to the fact that we need to take the derivative with respect to each variable at each stage. In turn, we see a blowing up effect in terms of the number of derivatives, and a new rank $n$ tensor to represent the $n$th derivative. For instance, if we have $f(x,y):\mathbb{R}^2\to \mathbb{R}$, then the first order derivative is given by the gradient, a rank $1$ tensor taken with respect to each variable:
$$f'(x,y)=\nabla f =\left\langle \frac{\partial f}{\partial x},\frac{\partial f}{\partial y}   \right\rangle$$
If a function $f$ is $C^2$, then it follows that:
$$f_{xy}=f_{yx}$$
if a function is $C^3$ then it follows that:
$$f_{xyz}=f_{xzy}=f_{zyx}=f_{zxy}=f_{yxz}=f_{yzx}$$
Which is to say that the permutations of the orders of the derivatives are equal, so we can take the [[Partial Derivative]] with respect to $x$ fist, and then $y$, and then $z$, and then any other order would be equal. Generally for some $f$ that is $C^n$ it follows that its $n$th mixed partial derivatives taken in any order are equivalent. 