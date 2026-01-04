---
title: Linear Programming
---
# Overview of Linear Programming
Linear programming is the optimization of a linear cost function generally given by:
$$\min c^Tx=\sum\limits_{i=1}^{n}c_{i}x_{i}$$
With the constraint set given by:
$$Ax=b : A\in \mathbb{R}^{m \times n}, m < n$$
(Note that we are interested in these particular constraints, since we already have answers for other shapes of $A$ especially if $A$ has an [[Inverse Matrix]])

And the constraint that $x \geq 0$ which means $x_{i } \geq 0$ in $x$.  Due to these constraints, we have restricted ourselves to the first octant. 

For instance consider the following objective function with the constraint set:
$$\min x_{1}+2x_{2}+5x_{3}$$
$$x_{1}+x_{2}+x_{3}=3$$
Our resulting "feasible set" is a plane bounded by the $xy$ plane, $xz$ plane, and the $yz$ plane. Our resulting figure is some truncated plane:

![[Pasted image 20260103054954.png]]

Given a linear function, which our objective function is, the constraints are at the borders of the function with the boundary. They must result at the intersection with the different planes. For large values of $m$ and $n$, it turns out that there an exponential amount of corners to check, which makes the run time of the algorithm extremely high. 

There are 2 approaches to solving this problem, either using the [[Simplex Algorithm]] or the [[Karmarkar Algorithm]]. 

# 1.) Simplex Algorithm 
We begin at a corner, and then we move to the next corner, and continue to move until we have reached some minimum. This is similar to [[Gradient Descent]] but only on corner points. 

# 2.) Karmarkar Algorithm 
The idea is to travel within the [[feasible set]], instead of along the exterior. Essentially we apply [[Gradient Descent]] on the entire instead of the outside. 

Both of these algorithms still have not entirely beaten the other, and both have their own respective use cases. 

# [[Dual LP]]
Instead of solving the exact [[Linear Programming]] problem, we can opt to solve the [[Dual LP]], which is essentially the inverse of the problem. The set of constraints that we have becomes the function we are trying to optimize over, and the set of functions we are trying to optimize become the constraints. Furthermore, we are go from looking from a max to a minimum, and vice versa. 

In some way, this is the equivalent problem here as the original, and by solving one of the problems we are able to solve both. The [[Dual LP]] problem for our original [[Linear Programming]] problem would have the form of the following for [[Weak Duality]]
$$\max b^{T}y \text{ for } y_{1},y_{2},\cdots y_{m}$$
With the constraint set for any $x$
$$A^{Ty}\leq c, b^{T}y \leq c^Tx $$
We can prove the identity that: $b^{T}y \leq c^Tx$:
$$b^Ty=x^TA^Ty$$
But note that $A^{T}y\leq c \implies x^TA^{T}y\leq x^Tc=c^Tx$, and thus we get our constraint. 