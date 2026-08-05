---
title: Rank 1 Matrix
tags:
  - LinearAlgebra
draft: "False"
---
# Rank 1 Matrix
A [[Rank 1 Matrix]] is a [[Matrix]] of [[Rank]] $1$. 

### Theorem - Form of a [[Rank 1 Matrix]]
If a [[Linear Transformation]] $A$ on a finite dimensional vector space $V$ is such that $\text{rank}(A)\leq1$ then, the elements of the matrix $A$ have the form $a_{ij}=\beta_{i} \gamma_{j}$ in every coordinate system. 

Conversely, if $A$ has this form then it entails that $\text{rank}(A) \leq 1$. 

$Proof)$.
The case for $\rho(A)=0 \implies A=0$ is trivial. Consider now when $\rho(A)=1$. Then we know that $\mathcal{R}(A)$ is one dimensional, so this space has a basis such that every vector in it is a scalar multiple of its basis vectors. 

Therefore:
$$Ax=y_{0}x_{0}$$
Let $\mathcal{X}=\{ \vec{x_{1}},\vec{x_{2}},\ldots,\vec{x_{n}} \}$ be a basis for the space, and let $[A]$ now denote the corresponding matrix for the linear transformation $A$ with the follow property:
$$Ax_{j}= \sum_{i} \alpha_{ij} x_{i} $$
Given a dual basis for $\mathcal{X}'=\{y_{1},y_{2},\cdots,y_{n} \}$ then we have that:
$$a_{ij}=[Ax_{j},y_{i}]$$
We can then express:
$$\alpha_{ij}=[y_{0}(x_{j})x_{0},y_{i}]=y_{0}(x_{j})[x_{0},y_{i}]=[x_{0},y_{i}][x_{j},y_{0}]$$And we can take that $\beta_{i}=[x_{0},y_{I}]$ and $\gamma_{j}=[x_{j},y_{0}]$.
Conversely, if we suppose that for $\alpha_{ij}$ of $A$ that $\alpha_{ij}=\beta_{i}\gamma_{j}$.

We can find a linear functional $\gamma_{j}=[x_{j},y_{0}]$ and a vector $x_{0}$ via:
$$x_{0}=\sum_{k}\beta_{k}x_{k}$$
Then the linear transformation $\tilde{A}$ defined by $\tilde{A}x=y_{0}(x)x_{0}$ is a rank one matrix, and its coordinate matrix is given by:
$$\tilde{\alpha_{ij}}=[\tilde{A}x_{j},y_{i}]$$
Where $\mathcal{X}'=\{y_{1},y_{2},\cdots,y_{n} \}$ is the dual basis of $\mathcal{X}$. Hence:
$$\tilde{\alpha_{ij}}=[y_{0}(x_{j})x_{0},y_{i}]=[x_{0},y_{i}][x_{j},y_{0}]=\beta_{i} \gamma_{j}$$
Which entails that $\tilde{A}=A$, which concludes the proof. 

### Theorem). 
If $A$ is a linear tf of rank $\rho$ on a finite dimensional vector space $V$, then $A$ can be written as the sum of $\rho$ transformations of rank 1. 

$Proof).$ 
Since $AV=\mathcal{R}(A)$ has dimension $\rho$, then we can find $\rho$ vectors $x_{1},\cdots,x_{\rho}$ such that these form a basis for $\mathcal{R}(A)$, then for every $x$ in $V$ that:
$$Ax=\sum_{i=1}^\rho \xi_{i} x_{i}$$
Each $\xi_{i}$ depends on $y_{i}(x)$ which is a linear functional. For each $i$ we define the following linear transformation $A_{i}$ such that:
$$A_{i}x=y_{i}(x)x_{i}$$
Correspondingly each $A_{i}$ has rank $1$ and and we have that: 
$$A=\sum_{i=1}^\rho A_{i}$$
### Theorem).
Corresponding any linear transformation $A$ on a finite dimensional vector space $V$ there is an invertible linear transformation $P$ for which $PA$ is a [[Projection]]. 

