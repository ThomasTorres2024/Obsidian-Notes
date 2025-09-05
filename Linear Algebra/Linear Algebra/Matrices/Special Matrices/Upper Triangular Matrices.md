---
title: Upper Triangular Matrix
tags:
draft: "False"
---
# Definition
Upper triangular matrices are [[matrices]] in $A \in \mathbb{R}^{n \times m}$ where each $a_{ij} =0$ when $i>j$. Typically, [[Upper Triangular Matrices]] are square matrices in the wild. 

#### Facts about Upper Triangular Matrices 
The only matrices which are [[Upper Triangular Matrices]] and [[Lower Triangular Matrices]] are [[diagonal matrix]] (diagonal matrices). 

#### The [[Inverse Matrix]] of an Upper Triangular Matrix is an Upper Triangular Matrix 
Using a proof by contradiction, we can show that for the [[non singular]] Upper Triangular Matrix $A \in \mathbb{C}^{m \times m}$ that its inverse must necessarily be another Upper Triangular Matrix. Since $A$ is invertible, $A$ must have $m$ non-zero entries along its diagonal, otherwise it would have a determinant of zero and thereby not be invertible. Let the inverse matrix of $A$ be the matrix $Z$. 

Let us recall $(1.8)$, which states that for the inverse matrix, $Z$, that the $j$th identity vector can be expressed as
$$\vec{e}_{j} = \sum_{i=1}^m z_{ij}\cdot\vec{a}_{i}$$
Let us incorrectly assume that $Z$ is not an upper triangular matrix, meaning that for some $q>p$ that $z_{qp}\neq 0$. Observe that when we get to $i=q$ in our sum, that there are no values to cancel the value at our index. The value at the index in the new vector is no longer zero because $A$ is a full rank matrix, and instead is $z_{ij}a_{qq}$ which we know is non-zero since it comes from the diagonal. 


