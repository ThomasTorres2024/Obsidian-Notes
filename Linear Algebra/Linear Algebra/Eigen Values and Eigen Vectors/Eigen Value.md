---
title: Eigen Values and Vectors 
draft: 
tags:
---
# [[Eigen Value]] Definition:
An [[Eigen Value]] is some $\lambda \in \mathbb{C}$ such that for the [[characteristic polynomial]] of a matrix $A \in \mathbb{C}^{n \times n}$, denoted by $p_A(x)$, the equation satisfies that: $$p_A(\lambda)=0$$ Furthermore an eigen-value satisfies the following equation with $v \in \mathbb{C}^n:v\neq \vec{0}$:
$$Av=\lambda v$$
We also call these "Right Eigen Values" and they 

### Right Eigen Values and Eigen Vectors
$\vec{x} \in \mathbb{C}^n$ is an eigen vector if $\vec{x} \neq \vec{0}$ and for $C \in \mathbb{R}^{n \times n}$,  $\exists \lambda \in \mathbb{C}$ such that:
$$A\vec{x}= \lambda \vec{x}$$
The scalar $\lambda$ is an eigen-value, and the non-zero vector $\vec{x}$ is thus an eigen vector. 
These are sometimes called "right-eigen values" and "right eigen-vectors". 
 - - -
### Left Eigen Values and [[Eigen Vector]]s
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

We can find the [[characteristic polynomial]] of $A$ by computing the polynomial: $$p_{A}(\lambda) = \text{det}(A - \lambda I_{n \times n})=0$$ 

The number of times $\lambda$ appears as a root of the [[Characteristic Polynomial]] is the algebraic multiplicity of $\lambda$, whereas the [[Dimension]] of the [[Eigenspace]] associated with an [[Eigen Value]] is the [[Geometric Multiplicity]] of an [[Eigen Value]]. 