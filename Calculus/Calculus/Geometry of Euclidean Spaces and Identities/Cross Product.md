---
title: Cross Product
tags:
draft: "false"
---
# Definition and Introduction
The cross product is an operation between two vectors from $\mathbb{R}^3$, $\vec{x},\vec{y}$, that returns a vector which is orthogonal to $\vec{x}$ and $\vec{y}$. We define the cross product algebraically and geometrically, much like the [[Dot Product]]. 

We denote the cross product by $\vec{x} \times \vec{y}$. We can more formally state that $\vec{x} \perp (\vec{x}\times \vec{y})$ and  $\vec{y} \perp (\vec{x}\times \vec{y})$. 

The algebraic definition of the cross product follows from the definition of the [[Determinant]] using co-factor expansion as follows:
$$\vec{x} \times \vec{v}= \text{det}\left( \begin{bmatrix} \hat{i} & \hat{j} & \hat{k}\\ x_{1} & x_{2} & x_{3} \\ y_{1} & y_{2} & y_{3]} \end{bmatrix} \right)=\hat{i}\cdot \text{det}\left(\begin{bmatrix} x_{2} & x_{3}\\ y_{2}& y_{3} \end{bmatrix} \right)-\hat{j}\cdot \text{det}\left(\begin{bmatrix} x_{1} & x_{3}\\ y_{1}& y_{3} \end{bmatrix} \right) +\hat{k}\cdot \text{det}\left(\begin{bmatrix} x_{1} & x_{2}\\ y_{1}& y_{2} \end{bmatrix} \right) $$
Which we can expand out to get the following vector:
$$\vec{x} \times \vec{v} =\langle x_{2}y_{3}-x_{3}y_{2},-x_{1}y_{3}+x_{3}y_{1},x_{1}y_{2}-x_{2}y_{1} \rangle$$
---
# Properties of the Cross Product

The cross product has the following properties:
* $\vec{x} \times \vec{y} = -(\vec{y} \times \vec{x})$. The cross product is [[anti-symmetric]]. The cross product does not commute. By changing the order in which we do a cross product, we are changing if the vector points up or down with respect to the line we are constrained along if we think of it as the span of our newly generated vector. We can verify this property by computing the determinant of our matrix, or by realizing that this is actually equivalent to a row swap in our determinant, which introduces a negative sign. 
* If $\vec{x}=\vec{y}=\vec{v}$ then $\vec{x} \times \vec{y} = \vec{v} \times \vec{v} = \vec{0}$. Intuitively this is because the only vector which is orthogonal to itself is the zero vector. Algebraically, and using the above property, this is because the only vector that is equal to its own negative must be the zero vector. 
* $\vec{x}\times(\vec{y}+\vec{w})=\vec{x}\times \vec{y} + \vec{x} \times \vec{w}$. Meaning that the cross product is distributive.   

---
# Geometric Definition of the Cross Product 
Again the cross product is orthogonal to both vectors $\vec{x}$ and $\vec{y}$. Furthermore the magnitude of the cross product is actually equal to the parallelogram formed by $\vec{x}$ and $\vec{y}$ using the addition rule. That is to say that:
$$\| \vec{u} \times \vec{v} \| = \|\vec{u}\| \| \vec{v}\| \text{sin}(\theta)$$
We can use this definition to simplify calculation of the magnitude of $\|\vec{u} \times \vec{v}\|$:
$$\|\vec{u} \times \vec{v}\|^2=(\|\vec{u}\| \|\vec{v} \| \text{sin}(\theta))^2=(\|u\|\|v\|)^2(1-\text{cos}(\theta)^2)=\|\vec{u}\|^2\|\vec{v}\|^2-\frac{\|\vec{u}\|^2\|\vec{v}\|^2 \langle \vec{u},\vec{v} \rangle)^2}{\|\vec{u}\|^2\|\vec{v}\|^2=\|\vec{u}\|^2\|\vec{v}\|}$$
$$\|\vec{v} \times \vec{u}\|^2=\|\vec{u}\|^2\|\vec{v}\|^2-\langle\vec{v},\vec{u}\rangle^2$$
If we use the [[Dot Product]] to determine that $\vec{u} \perp \vec{v}$, we can see that the dot product term goes to 0, and the resulting expression of our vectors would be:
$$\|\vec{v} \times \vec{u}\| = \|u\|^2\|v\|^2$$
