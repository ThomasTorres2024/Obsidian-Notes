---
title: QR Factorization
tags: 
draft: "false"
---
# Definition and Motivation 

The $QR$ factorization allows us to express any matrix with full column rank as a product of an [[orthogonal matrix]] multiplied by an [[upper triangular matrix]]. The big general formula for this is $A=QR$, where I will out the specifics for now to later define the two variants of $QR$ factorizations to just quickly express the core idea of what this factorization does.

Our incentive for this factorization is rooted in the fact that we have an upper triangular matrix and an orthogonal matrix are nice to work with. Say if we are trying to solve $A\vec{x} = \vec{b}$ we could do: 
$$A\vec{x}=\vec{b}=QR\vec{x}$$$$R\vec{x}=Q^T\vec{b}$$
It turns out this is a nice system to work with for solving. We can find the inverse of $Q$ very quickly, of course assume that it is square, because $Q$'s inverse is just its transpose. Performing a matrix vector computation is also quick, so $Q^T\vec{b}$ can be solved easily. $\vec{x}$ can thus easily be solved by just row reducing, which is a nice matrix to work since it is upper triangular. 

Also, in this square case where both $Q$ and $R$ are full rank and square and thereby [[Invertible Matrix]], we get the following result:

$$| \text{det}(A)|=|\text{det}(QR)|=|\text{det}(Q)\cdot\text{det}(R)|=|\text{det}(R)|=|\prod_{i=1}^nR_{ii}|$$
This works out since $Q$ is a unitary matrix and has a determinant of plus or minus one, which has a magnitude of one. This simplifies our expression, and leaves us with the product of the diagonal entries. 

---
# Reduced QR Factorization and Relationship to the Gram-Schmidt Process 

For $A,\hat{Q} \in \mathbb{R}^{m \times n}$ for $m \geq n$, and $\hat{R} \in \mathbb{R}^{n \times n}$, we can express $A$ as the following matrix product in what is called "reduced QR factorization":

$$A=\hat{Q}\hat{R}$$ where

$$A=\hat{Q}\hat{R} =  \begin{bmatrix}\vec{q}_{1} &\vec{q}_{2}  & \cdots & \vec{q}_{n} \end{bmatrix}   \begin{bmatrix} \|v_{1} \| & <\vec{v}_{1},\vec{v}_{2}> & <\vec{v}_{1},\vec{v}_{3}> & \cdots & <\vec{v}_{1},\vec{v}_{n}>   \\ 0 & \|v_{2} \| & <\vec{v}_{2},\vec{v_{3}}>&   \cdots & <\vec{v}_{2},\vec{v_{n}}> \\ 0 & 0 & \|v_{3} \|&   \cdots & <\vec{v}_{2},\vec{v_{n}}> \\    \vdots  & \vdots  & \vdots  & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & \| v_{n} \|  \end{bmatrix}$$

[[The Gram-Schmidt Process]] tells us that we can find an [[orthonormal]] [[basis]] which [[span]]s the same space as $A$. That is to say, $\text{span}\{ \mathcal{A}\}=\text{span}\{ \mathcal{Q}\}$ where $\mathcal{Q}=\{\vec{q}_{1},\vec{q}_{2},\cdot,\vec{q}_{n} \}$ and $\mathcal{A}=\{\vec{a}_{1},\vec{a}_{2},\cdots,\vec{a}_{n} \}$. 

Each $\vec{q}_{i}=\dfrac{\vec{v}_{i} }{\|\vec{v}_{i}\|}$, where $\vec{v}_{i} = \vec{a}_{i} - \sum_{j=1}^{i-1} \alpha_{k} \cdot \vec{q}_{j}$. We already know how to obtain our $Q$, simply using the Gram-Schmidt process. If we are to write out some of these we can see how we obtain our $R$:

For example:

$$\vec{q}_{1}=\dfrac{\vec{a}_{1}}{\| \vec{a}_{1} \|}$$
$$\vec{q}_{2}= \vec{a}_{2}- \dfrac{<\vec{q}_{1},\vec{a}_{2}>}{\| \vec{q}_{1} \|}$$
$$\vec{q}_{3}= \vec{a}_{3}- \dfrac{<\vec{q}_{1},\vec{a}_{3}>}{\| \vec{q}_{1} \|} - \dfrac{<\vec{q}_{2},\vec{a}_{3}>}{\| \vec{q}_{2} \|} $$

When we compute the matrix vector product $QR$, we are undoing the Gram-Schmidt process at each step. We multiply each $\vec{q}$ by each component that was deducted from the corresponding $\vec{a}_{i}$. Then, we scale $q_{i}$ by everything we divided it by, and all of the positive parallel components we removed are combined with the negative parallel components in return just resulting in $\vec{a}_{i}$. It's a bit hard for me to articulate this and the process I'm describing, to best grasp it, you should just compute it yourself. Basically, at each step, we are just reversing the transformations we made. We do this by doing the calculations in reverse order. 

Our matrix $R$ is [[invertible]]. It has $n$ [[pivots]], and is upper triangular. Each pivot is positive, since each pivot is the norm of a non-zero vector. In turn, $R$ is a really nice matrix that we can work with, that we can use to solve least squares problems in the future. 

This is enough background to rationalize our $A=\hat{Q}\hat{R}$ factorization. 

---
# Full QR Factorization 

We also have the full $QR$ factorization, which expresses $A=QR$. 

We can construct our full $QR$ factorization in the following; 
$$A=QR, \text{ where, } Q=[\hat{Q}|\tilde{Q}] \text{ and } R =  \begin{bmatrix} \hat{R} \\ 0_{(m-n) \times m}\end{bmatrix}$$
$\hat{Q} \in \mathbb{R}^{m \times n}$ and $\tilde{Q} \in \mathbb{R}^{m \times (m-n)}$. We can find the remaining columns to complete this matrix by determining the [[orthogonal complement]] of $\hat{Q}$. In order to balance out the additional vectors, we pad our $\hat{R}$ with $m-n$ additional rows of zeroes in order to delete the additional vectors in $Q$. So, $R \in \mathbb{R}^{m\times n}$, and can be thought of as an "upper triangular matrix", but not in the typical sense. 

It is more preferable to have an invertible $Q$ than a $R$ for some situations, so we can provide this factorization. $Q$ is an orthogonal matrix since it consists of columns that are mutually orthogonal and each column is normal, so it has orthonormal columns. 

Just to demonstrate that $A=QR$, we can show this by: 

$$QR= [\hat{Q}|\tilde{Q}] \begin{bmatrix} \hat{R} \\ 0_{(m-n) \times m}\end{bmatrix}=\hat{Q}\hat{R}+\tilde{Q}\cdot0_{(m-n)\times m}=\hat{Q}\hat{R}=A$$
---
# Applications 

We can use $QR$ factorization to compute [[Least Squares]] and to compute [[eigen values]]. 