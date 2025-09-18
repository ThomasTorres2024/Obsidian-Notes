---
title: Vectors
tags:
draft: "false"
---
# Vector Definition
We are interested in being able to define notions of distance in $\mathbb{R}^2$ and $\mathbb{R}^3$. 

We describe points in $\mathbb{R}^n$ by $(x_{1},x_{2},\cdots,x_{n}$) and vectors by bracket notation, $\langle x_{1},x_{2},\cdots x_{n} \rangle$, boldface, or arrow notation. If we know the initial and terminal points, $P$ and $Q$, we can use, $\vec{PQ}$. 

A vector centered at the origin is known as the [[position vector]]. We are only going to use [[position vectors]]. The origin point is always at the origin. The terminal point is always the same as the coordinates of the vector in such a vector. 

Sometimes we use position notation as a point, and sometimes we use vector notation depending upon whichever is more useful to us at an instant. 

Fundamentally, a vector is an element of a [[Vector Spaces]]. This notion abstracts the general idea of displacement vectors in space for objects to things that live in vector spaces, meaning that they satisfy closure of vector addition and closure under scalar multiplication. 

In a typical linear algebra class we study metric vector spaces. Most of the time we are interested in [[Displacement Vectors]] in the context of Calculus. 

#### ([[Vector Spaces]] Definition)
We support 2 operations with vector spaces, [[vector addition]] and [[scalar multiplication]]. In vector addition for $\vec{x},\vec{y} \in \mathcal{V}$, we add components of $\vec{x}$ and $\vec{y}$ component wise. We do something similar for scalar multiplication, but we just scale the elements of a single vector by a scalar from a corresponding field.                 

---
# Standard Basis for $\mathbb{R}^n$
In the case of $\mathbb{R}^2$, we have a standard basis of $[\hat{i},\hat{j}]$ and for $\mathbb{R}^3$ we have $\hat{i},\hat{j},\hat{k}$. 

Any element $\vec{v} \in V$ is a linear combination of elements from that space, so it follows that we can break down any item from a vector space into how much we scale the elements in the [[basis]] of our [[Vector Spaces]]. 

--- 
# Parallelogram Rule for Addition and Triangle Rule 
When adding vectors, $\vec{a},\vec{b}$ tip to tail we end up forming a parallelogram in the non-degenerate case, e.g. where the [[Determinant]] $\neq 0$. If we halve the diagram and do not add on all sides, we get a triangle, where the longest length is $\vec{b}+\vec{a}$:

![[Pasted image 20250905090655.png]]

Since $\text{det}(A)=$ the area of the rectangle spanned by the two vectors, by doing $\frac{1}{2}\text{det}(A)$ we obtain the area of the triangle involved. There is also a nice connection between this idea and the [[Cross Product]] and its respective identities. 