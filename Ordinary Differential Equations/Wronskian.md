---
title: The Wronskian
tags:
draft: "false"
---

#  The Wronskian

Oftentimes determining linear independence between two functions is a trivial task, however it can be confirmed if two functions are linearly independent by computing the determinant of the [[Wronskian]] Matrix. If the determinant is zero for some, or all, values of x, then it can be said that the functions are linearly dependent.

$$\mathcal{W}(f(x),g(x))= 
\begin{bmatrix}
    f(x) & g(x)\\
    f(x)' & g(x)'\\
    \end{bmatrix}$$

$$\det(\mathcal{W}(f(x),g(x))) =  f(x)\cdot g'(x) - g(x) \cdot f'(x)$$

If $f(x)\cdot g'(x) - g(x) \cdot f'(x) = 0$ then $f$ and $g$ are [[Linearly Dependent]] If $f(x)\cdot g'(x) - g(x) \cdot f'(x) \neq 0$ the function can be said to be [[Linearly Independent Functions]].

The following statements regarding the [[Wronskian]] are true if one of these statements is true:
*  $g(x)$ and $f(x)$ are linearly independent solutions on an interval $(a,b)$
*  $\mathcal{W}(g(x),f(x)) \neq$ 0 $\forall x \in  (a,b)$
* $\mathcal{W}(g(x_{0}),f(x_{0}) \neq$ 0 for at least one $x_{0} \in  (a,b)$

