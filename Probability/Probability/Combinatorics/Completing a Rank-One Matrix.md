---
title: Completing a Rank-One Matrix
tags:
draft: "false"
---
# Completing a Rank-One Matrix
Any matrix $A \in \mathbb{C}^{m \times m}$ where ([[Rank]]) $\text{rk}(A)=1$, we have that $A=uv^T$ for $u,v \in \mathbb{C}^m$. Every column of $A$ is a scalar multiple of one another. The following combinatorics problems asks, given non-zero entries in some positions of $A$, how can we determine that $A$ can be "completed" such that $A$ is rank 1? 

For instance consider the following matrix, where each "$*$" denotes a value which is non-zero that could be any value:

$$A=\begin{bmatrix} * & * & *\\
		* &  & \\
		* 
\end{bmatrix}$$
Is it possible for the remaining entries at $ij=22,23,32,$ and $33$ that we can construct an $A$ such that $\text{rk}(A)=1$? For this particular example it is possible. We know in a rank 1 matrix that each column is a scalar multiple of one of the other column vectors. Here, we fully know the leftmost column vector, and for the other two column vectors, we have some value. 

We can determine the ratio between the other two column vectors (since all values are non-zero) by simply taking the ratio between the known elements with the known vector, and then scaling the rest. For instance here we can calculate the following entries given:
$$A_{22}=\frac{A_{12}}{A_{11}}A_{21},A_{32}=\frac{A_{12}}{A_{11}}A_{31}$$
$$A_{23}=\frac{A_{13}}{A_{11}}A_{21},A_{33}=\frac{A_{13}}{A_{11}}A_{21}$$
This is a quite simple example, but it turns out that we can do this for other instances too, say for a $4 \times 4$ matrix. For a more complex $3\times 3$ example consider the following:
$$A=\begin{bmatrix} * & * & \\
		* &  & *\\
		& & * 
\end{bmatrix}$$
For this given matrix, we have enough information to find the ratio between $A_{21}$ and $A_{23}$. We also have the ratio between $A_{11}$ and $A_{12}$, so we can find the information for the other 2 columns given some values.  Since we know the other values in the other matrices, we have the ability to solve for the remaining four values. 

But for some matrix say this one:
$$A=\begin{bmatrix} * & * & \\
		* & * & \\
		& & * 
\end{bmatrix}$$
Since any $*$ is any non-zero value, it is possible that the $2\times 2$ matrix in the top left is non-zero which $\implies$ $\exists$ values of $*$ such that this [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] $\neq 0$. So, this would mean $\text{rk}(A) > 1 \neq 1$.    

We can find the precise condition for when some $A$ can recover a rank one matrix. It turns out that we need to interpret our entries of $A$ as a [[Bipartite Graph]].

For the position of some $* \in A$, we can interpret the row and the column of $*$ as an entry in the row portion of the vertices, and the column as an entry in the column portion. We can then draw an edge going from that row node to the corresponding column node. For instance take a look at the following matrix and its corresponding [[Bipartite Graph]]:

![[Pasted image 20260105144049.png]]
We can solve this matrix to be rank 1. It turns out that the condition of the [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] is only true in some cases, because there can be instances where there are no determinants which could result in a rank $>1$ matrix, but yet are still impossible to solve. It turns out that if a [[cycle]] occurs in our [[Bipartite Graph]] representation of the non-zero entries of our matrix, then it turns out that we cannot recover a rank 1 matrix guaranteed, since there are many non-zero entries.

For instance, here is an obvious example:
![[Pasted image 20260105144503.png]]
If we examine the top $2 \times 2$ section we could again obtain a $2 \times 2$ determinant $\neq 0$, but if we look at the corresponding rows and columns in the bipartite graph we see we get a cycle. Which means that we can freely choose the values here such that the values chosen can result in the columns being not scalar multiplies of one another $\implies \text{Rk}(A) \neq 1$.  At the least this is how I interpret it. Given this condition, I think that this is at least a decent interpretation?

Here is a more subtle example of a matrix failing for $4 \times 4$ and not falling to an obvious [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] issue:
![[Pasted image 20260105150916.png]]

Strang proposes a neat opening question at the end of the lecture, in the case of $A$ being of rank $n$, we do not really have a criteria to yet judge this and ensure what values of the matrix can be chosen and not chosen. 