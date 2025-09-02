---
title: Eigen Values and Vectors 
draft: 
tags:
---
---
### Right Eigen Values and Eigen Vectors
$\vec{x} \in \mathbb{C}^n$ is an eigen vector if $\vec{x} \neq \vec{0}$ and for $C \in \mathbb{R}^{n \times n}$,  $\exists \lambda \in \mathbb{C}$ such that:
$$A\vec{x}= \lambda \vec{x}$$
The scalar $\lambda$ is an eigen-value, and the non-zero vector $\vec{x}$ is thus an eigen vector. 
These are sometimes called "right-eigen values" and "right eigen-vectors". 
 - - -
### Left Eigen Values and Eigen Vectors
We also have left eigen values and eigen vectors that we can obtain through the following considering $\vec{y} \in \mathbb{C}^n$ where $\vec{y} \neq \vec{0}$ and $\mu \in \mathbb{C}$
$$y^HA = \mu y^H$$
- - -
An eigen pair consists of a pair of $\lambda$ and $\vec{x}$ such that $A\vec{x}=\lambda \vec{x}$ and is given by $(\lambda, \vec{x})$

The spectrum of $A$ is the set of all eigenpairs of $A$

We can find the eigen vectors of $A$ by finding the values of $\lambda$ which satisfy the following chain of equivalent expressions: 
$$A\vec{x}=\lambda \vec{x}$$
$$ \Longleftrightarrow A\vec{x} - \lambda \vec{x}= 0$$
$$ \Longleftrightarrow (A - \lambda I_{n \times n})\vec{x}= 0$$
$$ \Longleftrightarrow \text{det}(A - \lambda I_{n \times n})= 0$$
The eigen values of $A$ are thus the values for which $A - \lambda I_{n \times n}$ is a singular matrix.

We can find the ${\color{red} \text{characteristic polynomial}}$ of $A$ by computing the polynomial: $$p_{A}(\lambda) = \text{det}(A - \lambda I_{n \times n})=0$$ 
