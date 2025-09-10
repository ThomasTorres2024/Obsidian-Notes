---
title: Plane
tags:
draft: "false"
---
#  Linear Forms to Consider in $\mathbb{R}^n$
In $\mathbb{R}^n$, the most interesting linear subsets for us to consider are forms which we can describe through one [[vector]] alone, that is lines, $\vec{x} \in \mathbb{R}^n$ and $n$ dimensional hyperplanes which have a Co-Dimension of $1$ (I think this correlates to a null-space of 1 if we consider a representation of the hyper-plane as the linear combination of $n-1$ [[Linearly Independent Vectors]]).

We have an infinite amount of subspaces with dimension $\mathbb{R}^{n-1},\mathbb{R}^{n-2},\cdots,\mathbb{R}^{1}$ and so on when we consider the linear subspaces of $\mathbb{R}^n$.

We can describe the orientation of a line with a single [[vector]] known as the [[Direction Vector]]. Likewise, we can describe planes with a single vector. In $\mathbb{R}^3$, this vector is the cross product which we embed in the general plane formula. 

The general plane formula is given by $\vec{n}=[a,b,c]^T$ and point $x=(x_{1},y_{1},z_{1})$ given to be on the plane, and another general point (these are variables) $(x,y,z)$. We form a second vector by taking points from the general point off of the fixed point: $[x-x_{1},y-y_{1},z-z_{1}]^T$. 

We know that $\vec{n}$ is orthogonal to this vector, so we can use the dot product to obtain:
$$\vec{n} \cdot [x-x_{1},y-y_{1},z-z_{1}]^T = a(x-x_{1})+b(y-y_{1})+z(z-z_{1})=0$$
More generally this can be re-written to:
$$ax+by+cz=d$$
---
# Point to Plane Distance Formula
Let $Q=(x_{1},y_{1},z_{1})$ be a point not on plane $\mathbb{P}$, and a point $M = (x_{0},y_{0},z_{0})$ is on the plane. Let the vector $\vec{QM}$ be the vector that runs through both $Q$ and $M$. The side length is the side which is orthogonal to plane $\mathbb{P}$, the vector $\vec{n}$. We can form a right triangle out of this, and then project the vector $\vec{QM}$ onto $\vec{n}$. 

We can find the constant $c$ from the [[vector projection]]:
$$c=\frac{\langle \vec{QM},\vec{n} \rangle}{\vec{n^T \vec{n}}}$$
The magnitude of that orthogonal projection is thus:
$$\frac{\langle \vec{QM},\vec{n} \rangle}{\| \vec{n} \|}=\frac{a(x_{1}-x_{0})+b(y_{1}-y_{0})+c(z_{1}-z_{0})}{\| \vec{n} \|}=\frac{ax_{1}+by_{1}+cz_{1}+d}{\sqrt{a^2+b^2+c^2}}$$
![[maxresdefault.jpg]]

