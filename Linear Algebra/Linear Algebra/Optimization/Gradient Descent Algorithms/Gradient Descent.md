---
title: Gradient Descent
tags:
draft: "False"
---
# Gradient  and Convexity Review
Gradient Descent is a method used to obtain the local minimum of a function by continually iterating in the direction of the lowest descent. 

For some function $f(x,y)$ the [[Gradient]], $\nabla f = \langle f_{x},f_{y} \rangle$. The [[Hessian]] is given by:
$$\mathcal{H}= \nabla^2f =\begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$$
The standard interpretation of the gradient asks us which direction of steepest descent out of the function. If we take the minus of it we get the same line, but in the direction of least descent. If we go perpendicular to both, we stay along the function along a tangent line. 

Here is a basic linear example:
![[Pasted image 20260102204320.png]]
Another point to consider is the connection between the [[Hessian]] and the [[Convexity]] of a function. The [[Hessian]] test determines if a function is [[p[ositive definite]], [[negative definite]], or neither.

We can obtain convexity from a function being either convex, or strictly convex. If a function is convex, then $H$ is [[positive semidefinite]], if the function is strictly convex then $H$ is [[Positive Definite Matrix]]. 

Let us consider some example functions and apply notions of convexity:
$$f(x)=\frac{1}{2}x^TSx-a^Tx-b$$
This function is convex when $H=S$ since 

We can determine the [[Gradient]] of this function with the following. If we consider what happens in the $1\times 1$ case for $x$ we would be differentiating the following:
$$=\frac{1}{2}Sx^2-a^Tx-b$$
$$\nabla f = Sx-a$$
The same logic extends to when $x \in \mathbb{R}^n$. Much with the same logic, it would follow that:
$$\nabla^2f=S=H$$
If we want to determine the minimum value of $f$ it would be when $\nabla f = \vec{0}$. If $\exists S^{-1} \implies$ $x=S^{-1}a$, which clearly results in a minimum. This also happens to be the argmin of $f$. We can determine the actual minimum value at this point:
$$f(S^{-1}a)=\frac{1}{2}(a^TS^{-T})SS^{-1}a-a^TS^{-1}a-b$$
$$=\frac{1}{2}a^TS^{-{1}}a-a^TS^{-1}a-b=-\frac{1}{2}a^TS^{-1}a-b$$
This is thus the minimum value, also we only obtain this answer because it is assumed that $S=S^{T}$. 

The following is an interesting example of a convex function for $X \in \mathbb{R}^{n \times n}$: 
$$f(x)=-\log(\det(X))$$
We can determine the values of the derivative as being the entries of the inverse matrix, or at least related to it. Let us use the definition of the [[Determinant]] using [[Cofactor Expansion]]:
$$\det(X)=\sum_{i=1}^n x_{i1}\cdot (-1)^{i+1} \cdot \det(C_{i1})$$
$$-\frac{\partial \log(\det(X))}{\partial x_{ij}}=\frac{-\pm\det(C_{i1})}{\det(X)}$$
# Gradient Descent Overview
The formula for gradient descent is as follows:
$$x_{k+1}=x_{k}-S_{k}\nabla f(x_{k})$$
The only parameter for this operation is the learning rate. Let us assume $S_{k}$ is a constant. If $S_{k}$ is too large, we overshoot and do not converge to a minimum. If $S_{k}$ is too small, we take too long, and do not converge in an adequate amount of time. One way we can try and work with $S_{k}$ is through either an [[Exact Line Search]] or by choosing some initial value and checking to see if it is a good value or not. 

The [[Exact Line Search]] method tells us to choose $S_{k}$ to make $f(x_{k+1})$ a minimum on the search direction. The search direction is given by the gradient at $x_{k}$. If $f$ is convex, initially moving along the negative gradient would move us down. Once we begin to move up, then we have met some kind of minima, and we would stop. [[Exact Line Search]]s can be extremely slow for small condition numbers. 

When we do an exact line search, we are interested in seeing how much our little steps reduce the function, which again involves the reduction number. 

Another method is [[Backtracking]]. We begin with a fixed $S$ again, we consider the full step, half of it, a quarter of it, and so on, and check to see which portion is tending upwards, and which portion is still tending downwards. We are interested at the point at which we go from downwards to upwards, as this is a minima. 

# Gradient Descent Example

We can determine the convergence of the [[Gradient Descent]] algorithm by considering the smallest and largest [[eigen value]]s when a matrix is a [[Symmetric Matrix]]. If the matrix were not symmetric, the maximum [[singular value]] over the minimum singular value would be used:
$$\text{Symmetric Matrix: } \frac{\lambda_{\text{max}}}{\lambda_{\text{min}}}$$
$$\text{Not Symmetric Matrix: } \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}}$$
Let us consider the pure quadratic given by:
$$f(x)=\frac{1}{2}x^TSx=\frac{1}{2}(x^2+by^2)$$
Where:
$$S=\begin{bmatrix} 1 & 0 \\ 0 & b\end{bmatrix}$$
The function here strictly is a bowl. The local minimum clearly is the center at $(0,0)$. This is a useful example since the entire thing can be visualized and improved upon since it is a basic example. This would also be the argmin of $f$. 

Let us write out the [[Gradient Descent]] for this function:
$$\begin{pmatrix} x\\ y \end{pmatrix}_{k+1}=\begin{pmatrix} x\\y \end{pmatrix}_{k}-S_{k}\begin{pmatrix}2bx\\2by\end{pmatrix}_{k}$$
