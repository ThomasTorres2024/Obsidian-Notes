---
title: Orthogonal Complements
tags: 
draft: "false"
---

# Definition of Orthogonal Complement 

For a given set $S=\{\vec{v}_{1},\vec{v}_{2},\cdots,\vec{v}_{k} \} \subseteq \mathbb{R}^n$ we can define the orthogonal complement of $S^\perp$ by:

$$S^{\perp}=\{ \vec{x} \in \mathbb{R}^{n}: \vec{v}^T\vec{x}=0, \forall \vec{v} \in S \}$$
That is to say, that the set of vectors in $S^\perp$ is [[orthogonal]] to all vectors in $S$. When computing $S^{\perp}$ we end up computing the basis for $\mathcal{N}(S^T)$.

For example, considering the two [[linearly independent]] vectors in $V=\{\vec{w}_{1},\vec{w}_{2} \} \subseteq \mathbb{R}^3$.

We can write that:

$$V=\begin{bmatrix} w_{11} & w_{12} \\ w_{21} & w_{22} \\ w_{31} & w_{32}  \end{bmatrix}$$

We want our $\vec{x}$ to be orthogonal to both $\vec{w}_{1}$ and $\vec{w}_{2}$. We measure orthogonality via the [[inner product]] or [[Dot Product]]. We would thereby generate the following [[system of equations]]: 

$$\vec{w}_{1}^T\vec{x}=0$$
$$\vec{w}_{2}^T\vec{x}=0$$
Which can be expressed more usefully in the following:

$$w_{11}x_{1}+w_{21}x_{2}+w_{31}x_{3}=0$$
$$w_{12}x_{1}+w_{22}x_{2}+w_{32}x_{3}=0$$
Notice that we can express this as a matrix vector product by realizing that we have multiplied $V^T$ by the $\vec{x}$ to obtain: 

$$V^T\vec{x}=\vec{0}$$
This would be the equivalent of expressing a basis for $\mathcal{N}(V^T)$, which happens to be orthogonal to the range of $V$. 

--- 
# Orthogonal Complement Properties 

For the subspace $S$ of $\mathbb{R}^n$ and an orthogonal complement of $S$, $S^\perp$ , the following statements are:

1. $S^\perp$ is a subspace of $\mathbb{R}^n$
2. $S \oplus S^\perp = \mathbb{R}^n$
3. $(S^\perp)^\perp=S$ 

#### 1.) Proof that $S^\perp$ is a [[subspace]] of $\mathbb{R}^n$
We can observe that $S^\perp$ is a subspace through the definition of a subspace. $\vec{x}=0$ is in $S^{\perp}$, so it is not empty. We can also see that $S^\perp$ is closed under vector addition. Consider $\vec{z},\vec{w} \in S^\perp$ and $\vec{s} \in S$. By the definition of $S^\perp$, it follows that 

Consider the sum of the vectors is $\vec{z}+\vec{w}$. We can verify that the sum of the vectors is orthogonal to all vectors in $S$. 

$$\vec{s}^T(\vec{z}+\vec{w})=\vec{s}^T\vec{z}+\vec{s}^T\vec{w}=\vec{0}+\vec{0}=\vec{0}$$
This is the case since $\vec{z},\vec{w}$ are both orthogonal to all of $\vec{s} \in S$. So $\vec{z}+\vec{w} \in S^\perp$.

We can also verify by a similar argument that for $\alpha \in \mathbb{F}$ that $\alpha \cdot \vec{z} \in S^\perp$:

$$\vec{s}^T\cdot \alpha\vec{z}=\alpha(\vec{s}^T\vec{z})=\alpha \cdot \vec{0}=\vec{0}$$
In conclusion, $\alpha \cdot \vec{z} \in S^\perp$. 

Lastly we know that $S^\perp$ is non-empty, since $\vec{0} \in S^\perp$ for all sets of $S$. 

Since $S^\perp$ is closed under vector addition, closed under scalar multiplication, and non-empty, then  $S^\perp$ is a vector subspace.  

#### 2.) Proof that $S \oplus S^\perp = \mathbb{R}^n$
Let $S=\{\vec{s}_{1},\vec{s}_{2},\cdots,\vec{s}_{k}\}$ and $\vec{x} \in \mathbb{R}^n$. Let us consider $\vec{y}$ given by:

$$\vec{y}=\sum_{i=1}^k (\vec{s}_{i}^T\vec{x})\cdot\vec{s}_{i}$$
Let us also consider the vector $\vec{z}=\vec{x}-\vec{Y}$. We can show that $\vec{z} \in S^\perp$. For $\vec{s}_{i} \in S$, consider $\vec{z}^T\vec{s_{i}}$:

$$\vec{z}^T\vec{s_{i}}=(\vec{x}-\vec{y})^T\vec{s_{i}}=\vec{x}^T\vec{s_{i}}-\vec{y}^T\vec{s_{i}}=\vec{x}^T\vec{s_{i}}- \left( \sum_{j=1}^k (\vec{s}_{j}^T\vec{x})\cdot\vec{s}_{j} \right)^T\vec{s}_{i}$$
$$=\vec{x}^T\vec{s_{i}}- \left( \sum_{j=1}^k (\vec{s}_{j}^T\vec{x})\cdot\vec{s}_{j}^T\vec{s}_{i} \right)=\vec{x}^T\vec{s}_{i}-\vec{x}^T\vec{s}_{i}=0$$
In conclusion $\vec{z} \in S^\perp$ since it is orthogonal to all vectors in $S$. Note that because:

$$\vec{z}=\vec{x}-\vec{y} \Longleftrightarrow \vec{z}+\vec{y}=\vec{x} $$
We can also confirm that $S \cap S^\perp = \{ \vec{0} \}$. Any vector in this set must be orthogonal to all vectors in $S$, and all vectors in $S^\perp$ simultaneously, and the only vector that does this is $\vec{x}=0$. 

This tells us that any $\vec{x}\in\mathbb{R}^n$ can be expressed as a vector from $\vec{y} \in S$ and $\vec{z} \in S^\perp$. In conclusion, it follows that $S \oplus S^\perp = \mathbb{R}^n$. 

