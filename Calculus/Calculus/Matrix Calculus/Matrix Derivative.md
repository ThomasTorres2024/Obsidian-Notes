---
title: Matrix Derivative
tags:
  - Calculus
draft: "False"
---
# Matrix [[derivative]]
Consider $A \in \mathbb{R}^{m \times n}$ with $\vec{ x} \in \mathbb{R}^n$, then:
$$\vec{A}x \in \mathbb{R}^m : (m \times n )(n \times 1) = (m \times 1)$$
We have that:
$$ \frac{d}{dx} A \vec{x} = A$$
##### Proof.) 
We will do a proof for lower dimensions for the sake of ease. 

Consider $A \in \mathbb{R}^{2 \times 2}$:
$$A = \begin{bmatrix}
a & b \\ c & d
\end{bmatrix}, \vec{x}=[x_{1},x_{2}]^T$$
Then:
$$\frac{d}{dx} (A \vec{x}) :A \vec{x}= \begin{bmatrix}
a & b \\ c & d 
\end{bmatrix} \cdot \begin{bmatrix}
x_{1} \\ x_{2}
\end{bmatrix} = \begin{bmatrix}
y_{1} \\ y_{2}
\end{bmatrix} = \begin{bmatrix}
ax_{1}+bx_{2}\\ cx_{1}+dx_{2}
\end{bmatrix}$$
$$\frac{d}{dx} (\vec{A}x)=\nabla \left( \begin{bmatrix}
ax_{1} + bx_{2}\\cx_{1} +dx_{2}
\end{bmatrix}  \right) = \begin{bmatrix}
\frac{ \partial y_{1}}{\partial x_{1}} & \frac{ \partial y_{1}}{\partial x_{2}} \\ \frac{ \partial y_{2}}{\partial x_{1}} & \frac{ \partial y_{2}}{\partial x_{2}}
\end{bmatrix} = \begin{bmatrix}
a & b \\ c & d 
\end{bmatrix}=A$$
Notice that this should make sense. When we differentiate the gradient of a vector, we end up with a matrix as in the hessian, as we need to differentiate each component with respect to each variable and we get a resulting $n \times n$ matrix. 

I think the same idea takes place here. 
