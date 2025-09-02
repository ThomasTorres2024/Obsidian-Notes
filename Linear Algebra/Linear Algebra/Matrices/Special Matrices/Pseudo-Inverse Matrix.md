---
title: Pseudo-Inverse Matrix
tags: 
draft: "false"
---
# Definition and Overview
Only square matrices have inverse matrices. It turns out, that some rectangular matrices can also actually have inverses. We call these matrices by the names [[left inverse]] and [[right inverse]]. We are able to produce an inverse only when we multiply our matrix on the right side by our right inverse, or on the left by our left inverse. 

Let us consider $A \in \mathbb{R}^{m \times n}$. $A$ clearly cannot have an inverse, but there is a way that we should be able to multiply $A$ so that we can yield the identity matrix 

If we consider $A^TA$, we get a matrix which is $n \times n$, which should principally be invertible. If $A$ is full column rank, then $A^TA$ is full column rank, and since $A^TA$ is $n \times n$, it means that $A$ is invertible 

The pseudo inverse matrix exists if we have a matrix with [[linearly independent]] columns, meaning it has full rank. 

If we consider the short fat matrix given by $A \in  \mathbb{F}^{m \times n}$ where $n>m$, our matrix cannot be full rank since it has more columns than rows. So, our standard, $A^TA$ pseudo inverse matrix will not work out.

We can form a [[right inverse]] by the matrix given by $(AA^T)$. This matrix should be invertible if the matrix $A$ has a [[Rank]] of $m$. Thus, $AA^T$ is invertible:
$$(AA^T)(AA^T)^{-1}=I$$
Our right inverse is the matrix:
$$A^T(AA^T)^{-1}$$
Which we multiply by $A$ on the right side. Our main goal of a pseudo-inverse is being able to develop a matrix, $A^\dagger$ such that $A \cdot A^\dagger=I$ or $A^\dagger \cdot A = I$. 

---
# Right Inverses, Left Inverses, and Pseudo-Inverses 
The typical 2 sided inverse of a matrix satisfies the definition that:
$$AA^{-1}=A^{-1}A=I$$
Which has the necessary condition that for $A\in \mathbb{R}^{m \times n}$ that $m=r=n$, which is to say $A$ is just full rank. A left inverse is the case when $A$ has a full column rank, meaning $r=n$ for our matrix $A$.  However, it may be the case that we have more rows, and that these rows are not independent. The [[null space]] of $A$ for a rank of $n$ is clearly just $\{ \vec{0} \}$. This tells us that for some $\vec{b} \in \mathbb{R}^m$, that there is either 1 or 0 $\vec{x} \in \mathbb{R}^n$ such that:
$$A\vec{x}=\vec{b}$$
Which rules out the infinite number of possible solutions. Other solutions would be found by adding solutions from the null space into the mix, however this is not something we can do since $\text{Ker}(A)=\{ \vec{0} \}$.

It follows also that for $A^TA$, if $\text{rank}(A)=n$, it follows that $A^TA$ has a rank of $n$ as well, and $A^TA \in \mathbb{R}^{n \times n}$. This gives us a one sided [[left inverse]], which we denote by:
$$A^\dagger = (A^TA)^{-1}A^T$$
Which we can see that by multiplying by $A$ on the left clearly gives us the identity matrix. If we tried to put the pseudo inverse on the right it would fail. This is because $AA^T$ would be of size $\mathbb{R}^{m \times m}$ which is larger than $n$ and so it is not full rank, which implies it has some null space, so it cannot be inverted. 

We also have [[right inverse]]s for matrices $A$ where we have more columns than rows. If it is the case that we have a row rank of zero, that is to say $r=m$, then it follows that we can multiply our matrix by a pseudo inverse on the right to obtain the identity matrix:
$$A\cdot A^\dagger=I$$
From this we can see that if $A^\dagger = A^T(AA^T)^{-1}$ then we would obtain:
$$AA^\dagger = A(A^T(AA^T)^{-1})=I$$
If we consider the cases for both of these using the fundamental theorem of linear algebra, we would see that the column rank of $n$ case would result in a null space of $\vec{0}$, but a nullspace of $A^T$ that is full. Conversely for a matrix of row rank where the rank is $m$ then we get a nullspace that has many vectors, but a nullspace of $A^T$ with only the zero vector again. We are able to send back vectors in the column and row space respectively, but we cannot do anything with vectors that end up getting mapped to the zero vector.
![[Pasted image 20250619235624.png]]
Notice also that if we try and inverse the right side using a left inverse, and inverse the left side using a right inverse, we actually obtain the [[Projection Matrices]], which project onto the column space, and the row space. 

We can examine the third case where we do not have a full rank matrix in its columns or its rows, and it is rectangular. Our resulting matrix inverse could bring back vectors from the row space to the column space, and vice versa, but the components that are in the nullspace we could not bring back. 

Let us examine the linear transformation of the matrix, $A \in \mathbb{R}^{m \times n}$, with the vector $\vec{x} \in \text{Rowspace}(A)=\mathbb{R}^n$. The image of $\vec{x}$ under $A$ is given by $A\vec{x}$, which means that $A\vec{x} \in \text{Im}(A)$.  Our pseudo-inverse should principally return us from  our range back to our domain for this vector. That is, $A^\dagger A \vec{x} = \vec{x}$ 

But, if we have a vector from our nullspace, it gets mapped to the zero vector, which we cannot map back, as it always gets mapped back to the zero vector in another subspace. So, consequently, it is the nullspace of $A$ which causes it to not be invertible, and is where we get the fact that if $\text{Ker}(A)=\{ \vec{0} \}$, it follows that $A$ is fully invertible.  

Thus in the general case of a matrix, the best inverse that we can produce is a mapping between the row space and the column space. We know that both have a rank of $r$. Our pseudoinverse should therefore reverse the mapping on any vector from our column space to our vector space. 

Our pseudoinverse therefore performs the following map:
$$A^\dagger : \text{Im}(A) \rightarrow \text{Dom}(A)$$
Which is really equivalent to saying:
$$A^\dagger : \text{Col}(A) \rightarrow \text{Row}(A)$$
We need to be able to show for $\vec{x},\vec{y} \in \text{Row}(A)$  then $A\vec{x} \neq A\vec{y}$ given that $\vec{x} \neq \vec{y}$, which is to say that $A$ is injective.  We can prove this using a proof by contradiction:

Suppose that $\vec{x}\neq\vec{y}$ but $A\vec{x}=A\vec{y}$. It follows that, $A\vec{x}-A\vec{y}=\vec{0}$. So, $A(\vec{x}-\vec{y})=\vec{0}$. We can see that $\vec{x}-\vec{y}$ is in the null space, however we know that $\vec{x}$ and $\vec{y}$ are both in the row space, so it follows that $\vec{x}=\vec{y}=\vec{0}$, which gives us our contradiction. 

---
# Computing the Pseudo-Inverse
One way we can compute the psuedo inverse is via [[Single Value Decomposition]]. Via SVD we can express any $A$ as:
$$A=U\Sigma V^T$$
The hard part of inverting this is inverting our diagonal matrix sigma, which has $r$ many pivots. Our non-zero entries are simply their reciprocal. This in turn gives us our pseudo-inverse of $\Sigma$:
$$\Sigma = \begin{bmatrix} \sigma_{1}  & 0 & 0 & 0 & \cdots & 0\\
0 & \sigma_{2}   & 0 & 0 & \cdots &  0\\
0 & 0 & \sigma_{3}  & 0 & \cdots & 0 \\ \vdots  & \vdots & \vdots & \vdots & \ddots & 0\\ 0 & 0 & 0 & \sigma_{r} & \cdots & 0 \\ 0 & 0 & 0 & 0 & 0 & 0   \end{bmatrix}$$
Then it follows that we can express $\Sigma^\dagger$ as:
$$\Sigma^\dagger  = \begin{bmatrix} \dfrac{1}{\sigma_{1}}  & 0 & 0 & 0 & \cdots & 0\\
0 & \dfrac{1}{\sigma_{2}}   & 0 & 0 & \cdots &  0\\
0 & 0 & \dfrac{1}{\sigma_{3}}  & 0 & \cdots & 0 \\ \vdots  & \vdots & \vdots & \vdots & \ddots & 0\\ 0 & 0 & 0 & \dfrac{1}{\sigma_{r}} & \cdots & 0 \\ 0 & 0 & 0 & 0 & 0 & 0   \end{bmatrix}$$
 If we compute $\Sigma \Sigma^\dagger$ we would obtain:
$$\Sigma \Sigma^\dagger  = \begin{bmatrix} 1  & 0 & 0 & 0 & \cdots & 0\\
0 & 1   & 0 & 0 & \cdots &  0\\
0 & 0 & 1   & 0 & \cdots & 0 \\ \vdots  & \vdots & \vdots & \vdots & \ddots & 0\\ 0 & 0 & 0 & 1 & \cdots & 0 \\ 0 & 0 & 0 & 0 & 0 & 0   \end{bmatrix} \text{ which is in } \mathbb{R}^{m \times m} \text{ and a projection onto the column space} $$
Also note that if we compute $\Sigma \Sigma^\dagger$ we would obtain:
$$\Sigma^\dagger \Sigma  = \begin{bmatrix} 1  & 0 & 0 & 0 & \cdots & 0\\
0 & 1   & 0 & 0 & \cdots &  0\\
0 & 0 & 1   & 0 & \cdots & 0 \\ \vdots  & \vdots & \vdots & \vdots & \ddots & 0\\ 0 & 0 & 0 & 1 & \cdots & 0 \\ 0 & 0 & 0 & 0 & 0 & 0   \end{bmatrix} \text{ which is in } \mathbb{R}^{n \times n} \text{ and a projection onto the row space} $$
In general, we can express our pseudo inverse by the matrix $A^\dagger$ using SVD:
$$A^\dagger =  V \Sigma^{\dagger}U^T$$

---
# Personal Interpretation 
We know that for rectangular matrices that have a rank equivalent to the "small" dimension, in the case of a long full rank matrix its [[Rank]] is equal to its number of columns, and for the case with a wide matrix we have its rank being equal to its number of rows, we are guaranteed to have a corresponding left and right inverse. This idea comes from the fact that our matrices:
$$AA^T \text{ when } A\in \mathbb{R}^{m \times n}, m \geq n$$
$$A^TA \text{ when } A\in \mathbb{R}^{m \times n}, m \leq n$$
Are [[Invertible]]. Since these matrices are invertible for their respective cases we can express the following:
$$(AA^T)(AA^T)^{-1}=(AA^T)^{-1}(AA^T)=I_{m} \text{ when } A\in \mathbb{R}^{m \times n}, m \geq n$$
$$(A^TA)(A^TA)^{-1}=(A^TA)^{-1}(A^TA)=I_{n} \text{ when } A\in \mathbb{R}^{m \times n}, m \leq n$$
We want to denote our pseudoinverse by a single matrix and symbol, we don't want to have to multiply our original $A$ by two different matrices to get our result, and we want our pseudo-inverse to yield the identity. That is to say we want to express our inverse by computing $A\cdot A^\dagger$  or $A^\dagger \cdot A$. This doesn't work out for both definitions.  Our pseudo-inverse itself is not invertible, but we want to be able to multiply our $A$ by the pseudo inverse such that our resulting matrix is invertible. 

---
# Summary 
In total, when finding an inverse of a matrix we have four given cases. We have the case where $A$ is fully invertible, and can satisfy the condition that, $\exists A^{-1}$ such that:
$$AA^{-1}=A^{-1}A=I$$
There are a list of conditions linear algebra makes apparent are equivalent in the [[Invertible Matrix Theorem]] that give rise to such a matrix. 

We have the second case of left inverses, which occur for a full column rank matrix. Where multiplication on the left by $A^{\dagger}$ results in the identity. We only have the zero vector in the null space of $A$. 

We have the case of right inverses which occur for a full row rank matrix, where multiply on the right gives the identity. We only have the zero vector in the null space of $A^T$.

We have a rank not equal to the row count or column count. We have a non-trivial null space of $A$ and of $A^T$. 
