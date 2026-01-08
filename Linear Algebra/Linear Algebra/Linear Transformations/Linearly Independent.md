---
title: Linearly Independent
tags:
draft: "false"
---
# Linear Independence Intuition

A linearly independent matrix is a matrix which when reduced to [[Reduced Row Echelon Form]] can describe the values of other rows in terms of an independent value chosen for any of the other rows of the matrix. This in turn changes the dimensionality of the output space. For instance, if a 2x2 matrix is linearly dependent, this means that it really only has one free variable, despite the fact it is composed of two, one of the values within it is expressed with relationship to the other, this in turn constrains the output space of the linear transformation of the matrix to a line in this instance. If in three dimensions there were only 2 free variables, this would give a plane, which is analogous to $\mathbb{R}^2$ having a linearly independent matrix, since it outputs values to the entirety of $\mathbb{R}^2$ with two independent  variables. If instead the matrix were to have three independent variables this would imply that it would have an output space of $\mathbb{R}^3$.

# Linear Dependence/Independence Formal Definition
The formal definition of linear dependence makes use of the definition of the formula for a linear system/matrix's [[span]] with a specific restriction:
$$a_{1}x_{1}+a_{2}x_{2}+a_{3}x_{3}+....a_{n}x_{n}=0$$
Where $a_{1},a_{2},...a_{n}$ are scalars such that at least one $a_{k}$ in the scalars is not equal to zero and $x_{1},x_{2},...x_{n}$ are vectors. If there is some combination of vectors to get back to zero that isn't simply the trivial solution where every scalar is a negative, this means that there are multiple ways to express the same vector using information within the same set. This is a more formal definition of linear dependence. Taking the inverse of this argument gives us the definition of linear independence, which is if no scalars other than the trivial solution satisfy the above expression then the matrix/system is [[Linearly Independent]]. 

# Connection to [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]]s and Invertible Matrices ([[Inverse Matrix]]) 
A linearly independent matrix is one which has an [[Inverse Matrix]] and a [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] $\neq 0$. This is because a linearly independent matrix is a linear transformation which is one to one, meaning that every vector in the output space corresponds to only one value in the input space which was transformed to obtain the output value. Intuitively, a system which is linearly dependent, say for example in $\mathbb{R}^2$ is essentially just a line. We cannot inverse this line since information is lost condensing all of the space in $\mathbb{R}^2$ onto this line which has an output space of $\mathbb{R}$. Correspondingly the determinant of any system which is linearly independent is non-zero, meaning that we can take an inverse on that matrix, and that furthermore that it has n eigen values. 

Inversely for a matrix which is linearly dependent, it has a row of zeroes, making it have a determinant of zero meaning it cannot be inverted as already stated, and also has a less than n eigen values. Since the product of eigen values is equivalent to the determinant, we use this fact to obtain that a linearly dependent matrix which has an eigen value of zero is not invertible. 

# Linear Independence and [[Rank]]

The rank is the number of pivots a matrix has after it is row reduced. If for some $A \in \mathbb{R}^{m \times n},$ we have that $\text{rk}(A) = \min(m,n) \implies$ $A$ is [[Linearly Independent]]. Otherwise, $A$ is [[Linearly Dependent]]. 
