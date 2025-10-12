---
title: Critical Points
tags:
draft: "false"
---
# Critical Points 
Critical points may be the [[local minima]] or [[local maxima]] of a continuous function, or alternatively saddle points or points which are degenerate in nature and cannot be classified so simply. Critical points occur in the multivariable case on $f : C \subseteq \mathbb{R}^n \to \mathbb{R}^m$ where $\nabla f = \vec{0}$, which is to say that at a critical point we can expect a [[tangent plane]] with a horizontal slope. We need to be able to classify the critical points as being maxima or minima by using the [[Hessian Matrix]], and then determining if the given [[Taylor Series]] of the function can be represented using a [[positive definite]] matrix or a [[negative definite]] matrix. 

A [[positive definite]] [[Hessian Matrix]] is positive definite if and only if $A$ satisfies that $A^H=A$ and that $\vec{x}^TA\vec{x}>0$ and is equal to zero only when $\vec{x}=\vec{0}$.  A negative definite matrix is less than 0 given its [[Quadratic Form]] and zero when $\vec{x}=\vec{0}$. 

### Case - Determinant is Non-Zero 
In practice all we need to do is be able to compute the [[Hessian Matrix]], and then look at its determinants. A [[positive definite]] [[Hessian Matrix]] satisfies the condition that its $n$ derivatives from the first to the $n$th all are greater than or equal to 0. The [[negative definite]] [[Hessian Matrix]] must satisfy the condition that all determinants from $1$ to $n$ vary between being negative, to positive, and then to negative. This is the case since all eigen values of the [[Hessian Matrix]] are negative, and in turn the sign will vary because the product of an even number of negative values is a positive number, and the product of an odd number of negative values is odd. The first case holds for the [[positive definite]] [[Hessian Matrix]] because each eigen value is greater than 0, which means that the determinant is always positive. 

### Case - Determinant is Zero
When the determinant of our [[Hessian Matrix]] is zero, then we encounter a degenerate case where our function has an infinite number of points that are negative. Take a look at [[Quadratic Form]]s that correspond to these hessian matrices. We have paraboloids that are extruded, it's like a rotated case of $x^2=z$ or $z=y^2$ in the 2d case. 
# Optimization Generally
If we are looking for [[global minima]] or [[global maxima]], then we need to be able to use contour diagrams and compute the critical points. 

If we have a constrained problem then we use [[Lagrange Multipliers]] to find the critical points. If we are only working on a boundary then we only need to worry about the points with [[Lagrange Multipliers]]. When we have points along an interior, then we need to compute critical points and determine that the points are within this region. 

