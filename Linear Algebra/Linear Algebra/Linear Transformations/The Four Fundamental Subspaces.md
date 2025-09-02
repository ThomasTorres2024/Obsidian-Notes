---
title: The Four Fundamental Subspaces
tags: 
draft: "false"
---
# The Four Fundamental Subspaces 

For a given linear transformation $A : \mathbb{R}^m \rightarrow \mathbb{R}^n$, we can say that $A$  has the associated subspaces that are defined by:
$$\mathcal{R}(A) = \{ \vec{x} \in \mathbb{R}^m : A\vec{x}=\vec{w}, \forall \vec{w}\in \mathbb{R}^n \}=\{A\vec{x}:\vec{x}\in\mathbb{R}^n\}$$
$$\mathcal{N}(A) = \{ \vec{x} \in \mathbb{R}^m : A\vec{x}=\vec{0}\}$$
$$\mathcal{R}(A^T) = \{ \vec{x} \in \mathbb{R}^n : A^T\vec{x}=\vec{w}, \forall \vec{w}\in \mathbb{R}^m \}=\{A^T\vec{x}:\vec{x}\in\mathbb{R}^m\}$$$$\mathcal{N}(A^T) = \{ \vec{x} \in \mathbb{R}^n : A\vec{x}=\vec{0}\}$$
We can apply some of the rules of [[orthogonal complements]] to relate these [[subspaces]] to one another:
$$\mathcal{R}(A)^\perp=\mathcal{N}(A^T)$$
$$\mathcal{R}(A^T)^\perp=\mathcal{N}(A)$$
We can also apply the rules of direct sums involving orthogonal spaces which directly follows:
$$\mathcal{R}(A)\oplus \mathcal{N}(A^T)=\mathbb{R}^n$$
$$\mathcal{R}(A^T)\oplus \mathcal{N}(A)=\mathbb{R}^m$$
Lastly we have the rank nullity theorem: 
$$\text{dim}(\mathcal{R}(A))\oplus \text{dim}(\mathcal{N}(A^T))=\text{dim}(\mathbb{R}^n)=n$$
$$\text{dim}(\mathcal{R}(A^T))\oplus \text{dim}(\mathcal{N}(A))=\text{dim}(\mathbb{R}^m)=m$$

Taking a step back to digest what these results mean, two subspaces are [[orthogonal]] if any vectors from each respective subspace is orthogonal to one another. When say that for the matrix $A$, that its range $\mathcal{R}(A)$ is orthogonal to $\mathcal{N}(A^T)$, then we are saying that for any $\vec{x} \in \mathcal{R}(A)$ and $\vec{y}\in \mathcal{N}(A^T)$ then it follows that: 
$$\vec{x}^T\vec{y}=0$$
This is also true for $\mathcal{R}(A^T)$ and $\mathcal{N}(A)$ as well. 

The dimension of the range of $\mathcal{R}(A)$ and $\mathcal{R}(A^T)$ is equivalent. The rank nullity theorem tells us that the rank of a matrix plus the number of columns in the null space is equivalent to the total number of columns in our matrix. Likewise, it also tells us that the rank plus the number of rows in the null space of $A^T$ is equal to the total number of columns, $m$. 

---
### 1.) Proof that $\mathcal{R}(A)^\perp=\mathcal{N}(A^T)$. 

Let us consider some $\vec{x} \in \mathbb{R}^n$ and some $\vec{y} \in \mathcal{R}(A)^\perp$ it follows that:

$$(A\vec{x})^T\vec{y}=\vec{x}^TA^T\vec{y}=0$$
$$\Longleftrightarrow A^T\vec{y}=0$$
$$\Longleftrightarrow A^T\vec{y} \in \mathcal{N}(A)^T$$
Notice that for $A^T\vec{y}$ that $\vec{y} \in \mathcal{N}(A^T)$. So, it follows that all vectors that are orthogonal to vectors in $\mathcal{R}(A)$ are in $\mathcal{N}(A^T)$ 

### 2.) Proof that $\mathcal{R}(A^T)^\perp=\mathcal{N}(A)$

Let us consider some $\vec{x} \in \mathbb{R}^m$ and some $\vec{y} \in \mathcal{R}(A^T)^\perp$ it follows that:

$$(A^T\vec{x})^T\cdot\vec{y}=\vec{x}^TA\vec{y}=0$$
$$\Longleftrightarrow A\vec{y}=0$$
$$\Longleftrightarrow A\vec{y} \in \mathcal{N}(A)$$
Likewise, $\mathcal{R}(A^T)^\perp=\mathcal{N}(A)$. 

We can conclude that the perp operator essentially just takes the transpose of the matrix on the inside of the range or null space, and swaps range to nullspace, and nullspace to range. 

---
# Visualizing the Four Fundamental Subspaces 

The way we tend to group the four fundamental subspaces is as such: 

![[Pasted image 20250619235624.png]]

In this diagram, we show that the null space of $A$ is orthogonal to the row space of $A$, and that under $A^T$ the row space is mapped to the column space.

We depict our range of the columns of $A$ and null space of $A^T$. 

--- 
# [[Invertible Matrix]] Theorem 

An invertible matrix has the following properties for the matrix $A \in \mathbb{R}^{n \times n}$. If the row and column counts for $A$ are not equal, then $A$ cannot be invertible. If they do match and any one of the following conditions are satisfied, then all of the other conditions are also true. 

1. $A$ is nonsingular/invertible, $\exists A^{-1}, A A^{-1}=A^{-1}  A = I_{n}$
2. $A$ is row equivalent to $I_{n}$, that is $\text{rref}(A)=I_{n}$
3. $\text{det}(A)\neq0$
4. $\text{rank}(A)=n$
5. $A\vec{x}=\vec{0} \Longleftrightarrow \vec{x}=\vec{0}$
6. $A\vec{x}=\vec{b}$ has a unique solution for any $\vec{b}\in \mathbb{R}^n$
7. $A$ has $n$ linearly independent columns 
8. $A$ has linearly independent rows 
9. $\mathcal{N}(A)=\{ \vec{0} \}$
10. $\mathcal{R}(A)=\mathbb{R}^n$

From here we can try and diagnose if there is a solution for our $\vec{b}$ in $\mathcal{R}(A)$. We have to go through the possibilities that there is no solution, infinitely many solutions, or only one unique solution:

![[Pasted image 20250620003405.png]]



