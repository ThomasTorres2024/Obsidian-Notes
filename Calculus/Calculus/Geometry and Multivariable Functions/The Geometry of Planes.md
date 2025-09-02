---
title: The Geometry of Planes
tags: 
draft: "false"
---
# The Geometry of Planes 

For any two linearly independent vectors $\vec{v}_{1},\vec{v}_{2}, \in \mathbb{R}^3$ we can define a plane by determining the [[normal vector]] of the two vectors, which is obtained through a cross product: 

$$\vec{N}=\vec{v}_{1} \times \vec{v}_{2}$$

Another thing I found that works to compute $\vec{N}$ doesn't require using the cross product, but can be found by taking the orthogonal complement of $A \in \mathbb{R}^{3 \times 2}$ which is found by computing: 

$$\text{rref}(A^T)=\text{rref}
\left( \left[\begin{array}{ccc|c}
v_{11} & v_{12} & v_{13} & 0 \\
v_{21} & v_{22} & v_{23} &  0  \\
\end{array}\right] \right)$$

This seems to be analogous to computing the [[cross product]], it is less efficient in my personal belief but it works just fine. 

We know that $$\vec{N} \cdot \vec{v}_{1} = \vec{N} \cdot \vec{v}_{2} = \vec{0}$$

The normal vector is orthogonal to each so that is why we can seem to find the normal vector through the null space of $A^T$. 

The general form of a plane is given by:

$$ax+by+cz=d$$

Which we can compute using the normal and a second vector formed by a point on the plane $(p_{1},p_{2},p_{3})$ denoted by $P_{0}$, and any point in space $(x,y,z)$ where $\vec{w}=[x-p_{1},y-p_{2},z-p_{3}]^T$. 

We can obtain our plane equation by computing $\vec{N} \cdot \vec{w}$. 

Note also that the coefficients in our plane equation, $a,b$ and $c$ are the 3 coordinate positions, so: 

$$\vec{N}= \begin{bmatrix}a & b & c \end{bmatrix}^T$$

The value $d$ is the value of $z$ at $P_{0}$. 

---
# Determining if A Vector is Parallel or Perpendicular to a Plane 

Given the plane $ax+by+cz=d$ and vector $\vec{v}=\begin{bmatrix} v_{1} & v_{2} & v_{3} \end{bmatrix}$ we can determine the alignment by taking the normal from the plane equation, $\vec{N}=\begin{bmatrix}a & b & c \end{bmatrix}^T$, then we can consider the dot product:

$$\vec{N} \cdot \vec{v}$$
If: 
* $\vec{N} \cdot \vec{v} = 0$ the vector is either parallel to the plane or in the plane since it is perpendicular to the normal 
	* We can evaluate this by computing the plane equation on the vector, if it evaluates to the expected value of the plane, then we are in the plane, otherwise we are merely parallel  
* $\vec{N} \cdot \vec{v} = \pm 1$ then the vector is perpendicular to the plane since it is parallel to the normal 
* Else neither is true 

--- 
# Determining Intersections Between Planes 

The linear system provided in the matrix $A$ below can be visualized as the intersection of 3 planes. 

For example, consider the linear system expressed as an augmented matrix below that encapsulated $A\vec{x}=\vec{b}$:

$$A=\left[\begin{array}{ccc|c}
1 & 0 & 1 & 1 \\
1 & 1 & 0 &  2 \\
1 & 2 & 3 & 3
\end{array}\right]$$

If we take 2 planes then they intersect, we get a line where both conditions are met. 

If the third plane intersects, then the line will be intersected by a plane, and we will get a point. This will be enough to solve our linear system. 

We can express this in a way that is less heavy on linear algebra though its not necessary.

We can solve for the vector $\vec{x}$ by inverting $A$:

$$\vec{x}=A^{-1}\vec{b}$$It may be the case that none of the planes or only 2 planes intersect. 
In the case that all planes intersect in some way, our potential solutions to this system consist of a line, a plane, and a point. 

 Let us express this more formally using planes denoted by $P_{1},P_{2},P_{3}$.
 * If $P_{3}$ is not parallel to $P_{1} \cap P_{2}$, then $P_{1} \cap P_{2} \subseteq P_{3}$, then $\vec{x}$ has infinitely many solutions where any point in $P_{2} \cap P_{1}$ is a solution to the system , which could be a plane or a line 
* If $P_{3}$ is parallel to $P_{1} \cap P_{2}$ then $\not \exists \vec{x}$ that satisfies our system 

We can reconnect the ideas with the [[determinant]] and solving a linear system. We are guaranteed a linear solution if $A^{-1}$ exists, which means that the determinant of our system is non-zero. 

For the homogeneous case, we are guaranteed to have a solution. That is to say there is always a solution for: 

$$A\vec{x}=\vec{0}$$

If our planes have a z intercept of 0, then we are guaranteed to have a solution which is $\vec{x} =\vec{0}$. It may be the case that we have other solutions that are non-trivial that we can obtain by row reducing $A$ is $\text{dim}(\mathcal{N}(A))>0$. 

If $\exists A^{-1}$ then we are guaranteed to have $A\vec{x} = \vec{0} \Longleftrightarrow \vec{x} = \vec{0}$

If $P_{3}$ is coplanar with either $P_{1}$ or $P_{2}$ then $\vec{N}_{3}  \perp \vec{N}_{1} \times \vec{N}_{2}$

---
# General Cases for Solving Systems 

- If $\text{det}(A) \neq 0$ then $\exists! \vec{x}=A^{-1}\vec{b}$ 
- If $\text{det}(A) \neq 0$ then there is either infinitely many solutions or a single one 
