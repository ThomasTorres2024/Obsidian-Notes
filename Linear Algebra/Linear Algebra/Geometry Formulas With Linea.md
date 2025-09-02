---
title: Etc Idk
draft: 
tags:
---

<h1 align="center">Point to Plane Distance Formula</h1>

Consider point $p \in \mathbb{R}^3$ where $p = (p_{x},p_{y},p_{z})$ and a plane, $X$ of the form $ax+by+zc=0$

We know the vector $\vec{d} =\begin{pmatrix} a & b & c \end{pmatrix}^T$ is orthogonal to all points along $X$.

We also know that $p$  intersects with some $\vec{d} \cdot \delta$ when we scale $\vec {d}$ enough

We also know that if we considered $p$ to be represented as a vector, $\vec{p} = \begin{pmatrix} p_{x} & p_{y} & p_{z} \end{pmatrix}^T$

We can make use of the Pythagorean Theorem to consider $\vec{p}$ the hypotenuse, and the vector $\vec{d} \cdot \delta$ orthogonal to plane $X$ as another side of the triangle, and the last vector parallel to $X$. 

Consider the angle between $\vec{d}$ and $\vec{p}$. Using the cosine inner product identity, we can write that 
$$\text{cos}(\theta)= \dfrac{ <\vec{p} ,\vec{d} \cdot \delta> }{\| \vec{d} \cdot \delta\| \| \vec{p} \|} = \dfrac{\| \vec{d} \cdot \delta \|}{\| p \|}$$

We can see that: 

$$\| \vec{d} \cdot \delta \|^2 = <\vec{p} ,\vec{d} \cdot \delta> \Longleftrightarrow  \  \delta =  \dfrac{<\vec{p} ,\vec{d}>  }{ \| d\|} = \dfrac{p_{x}a + p_{y}b+p_{z}c}{\sqrt{a^2+b^2+c^2}}$$

Note this is true iff our plane, $X$ passes through the origin, otherwise we would get some additional term, $h$ which indicates how far our plane is from the origin. 

Also we must make the numerator positive if $\delta$ measures distance and not merely the amount we are scaling $\vec{d}$ by, so our final result is thus:

$$\dfrac{|p_{x}a + p_{y}b+p_{z}c +h|}{\sqrt{a^2+b^2+c^2}}$$

- - -
