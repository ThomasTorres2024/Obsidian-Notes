---
title: Determinant
draft: "false"
tags:
---
# Determinant Definition
The [[Determinant]] is a map from a matrix, $$ \large \det(A) : \mathbb{C}^{n \times n} \mapsto \mathbb{C}$$
[[Determinant]]s are linear with respect to each row, are antisymmetric, and the volume of the $n$ basis vectors is $1$. It can be shown that there is one and only one function that satisfies this result. The [[Determinant]] of a matrix we can intuitively think of as the hypervolume of a parallelepiped. 

In the two by two case, for a 2x2 matrix we have that its determinant is:
$$\text{det}\left(\begin{bmatrix} a & b\\ c& d \end{bmatrix} \right)=ad-cb$$
We also use bars around a matrix to denote the [[Determinant]] of a matrix as an alternative notation. 

We can compute higher dimensional matrices by using the [[Cofactor Expansion]] by computing the sum of the determinant of correctly signed minor matrices. 

We can also use any row or column to iterate over in order to compute our determinant. Any even valued iteration in our expansion will have a negative sign in front of it. 

---
# Properties of the Determinant 
The properties of the determinant appear to come from fundamental Row Operations ([[Elementary Row Operations]]) that we can perform on matrices. They effect the determinant of the matrix in the following ways:

1. Column swaps correspond to introducing a negative sign to our determinant:
$$[\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]=-[\vec{a}_{2},\vec{a}_{1},\vec{a}_{3}]$$
2. If a column contains $c$, we can factor it out: $$[c\cdot\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]=c\cdot[\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]$$
3. Addition of columns does not change the determinant:
$$[\vec{a}_{1}+\vec{a}_{2},\vec{a}_{2},\vec{a}_{3}]=[\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]$$
#### (Proof) $\left|\text{det} \left(\begin{bmatrix} v_{1} & v_{2} \\ u_{1} & u_{2}  \end{bmatrix} \right) \right| = \text{Area of the Parallelogram Formed by } \vec{v},\vec{u}$:
We know that the magnitude of the [[Cross Product]] has an area equivalent to that of the parallelogram formed by vectors $\vec{v}$ and $\vec{u}$:
$$\| \vec{u} \times \vec{v} \| = \| \langle0,0,\hat{k}  \rangle \| = \left|\text{det} \left(\begin{bmatrix} v_{1} & v_{2} \\ u_{1} & u_{2}  \end{bmatrix} \right) \right|$$

---
# The [[Triple Product]]
The triple product is a scalar valued function for the given vectors, $\vec{x}$,$\vec{y}$,$\vec{z} \in \mathbb{R}^3$:
$$(\vec{x} \times \vec{y}) \cdot \vec{z} = z_{1} \left|\text{det} \left(\begin{bmatrix} x_{2} & y_{2} \\ x_{3} & y_{3}  \end{bmatrix} \right) \right| - z_{2} \left|\text{det} \left(\begin{bmatrix} x_{1} & y_{1} \\ x_{3} & y_{3}  \end{bmatrix} \right) \right| + z_{3} \left|\text{det} \left(\begin{bmatrix} x_{1} & y_{1} \\ x_{2} & y_{2}  \end{bmatrix} \right) \right| $$
$$=\text{det}\left( \begin{bmatrix} x_{1}&x_{2} & x_{3} \\ y_{1} & y_{2} & y_{3}\\ z_{1} & z_{2} & z_{3} \end{bmatrix} \right)$$
Geometrically, we are determining how much the vector $\vec{z}$ aligns with the vector which is orthogonal to both $\vec{x}$ and $\vec{y}$. We can also show that the absolute value of the [[Triple Product]] is the area of a [[parallelepiped]] (the three dimensional analog of a [[parallelogram]]).

![[volume_parallelepiped.png]]




We know that the area of the base is given by the area of the base multiplied by the height. We know that the base is a parallelogram formed by vectors $\vec{a}$ and $\vec{b}$ is the base, which we can find using the [[Cross Product]] which would be:
$$\| \vec{a} \times \vec{b} \| = \|\vec{a}\| \|\vec{b} \| \text{sin}(\theta)$$
The height is given by $\|c\| \text{cos}(\theta)$ which is equivalent to finding the angle between the normal of $\vec{a}$ and $\vec{b}$ and the vector $\vec{c}$. This yields that the area is given by:
$$\|\vec{a} \times \vec{b}\| \cdot \|c\| \text{cos}(\theta)=|(\vec{u}\times \vec{v})\cdot\vec{w}|$$
We use the [[Dot Product]] identity for the last step, and can successfully show the correspondence between the [[Triple Product]] and the [[parallelepiped]]. 

---
# Methods for Computing the [[Determinant]] of a Matrix:
### Cofactor Expansion: 
[[Cofactor Expansion]] is a method for computing the [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] of a matrix, $A \in \mathbb{R}^{n \times n}$. It is given using the following formula:
$$\sum_{i=1}^n (-1)^{i+1} \cdot a_{ij} \det(A_i)$$
Let $A_i$ be the [[Matrix of Minors]] which is the matrix found by deleting the corresponding row and column of our given $a_{ij}$ and then grouping the remaining indices into a new matrix. For example in the case of a $3 \times 3$ matrix, we can determine its [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] by choosing $j=1$ and doing:
$$\det\left( \begin{bmatrix} a_{11}&a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33} 
\end{bmatrix}\right) = a_{11}\begin{bmatrix} a_{22} & a_{23}\\ a_{32} & a_{33} \end{bmatrix} - a_{12}\begin{bmatrix} a_{11} & a_{13}\\ a_{31} & a_{33} \end{bmatrix} +  a_{13}\begin{bmatrix} a_{21} & a_{22}\\ a_{31} & a_{33} \end{bmatrix}$$
The formula for the [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] with [[Cofactor Expansion]] is recursive, meaning we calculate the determinant of a $3 \times 3$ using the formula of a $2\times 2$, and the formula for a $4 \times 4$ uses a $3 \times 3$, and the formula of an $n \times n$ uses an $(n-1) \times (n-1)$. 

---
### Leibnitz Formula:
The Leibnitz Formula is an alternative way of defining the [[Determinant]], and links the idea of the [[Determinant]] with [[Permutation]]s. Let $j$ denote the column-wise position from $1 \leq j \leq n$
$$\large \det(A)=  \sum_{(j_{1},j_{2},\dots,j_{n}) \in S_{n}} a_{j_{1}1}a_{{j_{2}}2}\dots a_{j_{n}n}\cdot \text{vol}(\vec{e_{j_{1}}}, \vec{e_{j_{2}}}, \dots , \vec{e_{j_{n}}})$$

---
### [[Eigen Value]] Definition
If we have the eigen values $\lambda_{1},\lambda_{2}, \dots, \lambda_{n}$ of a matrix, then we know that the [[Determinant]] of the matrix is:
$$\det(A)=\prod_{i=1}^{n}\lambda_{i}$$
---

# Hadamard's Inequality 
Hadamard's inequality relates the determinant of a Matrix using the [[norm]] of the column vectors of some $A$. Let $A \in \mathbb{C}^{m \times m}$, then it follows that:
$$\det(A) \leq \prod_{i=1}^m\|\vec{a_{j}} \|: \vec{a_{j}} \text{ is a column vector of } A$$
Geometrically, we can think of this as a bound to the area that the vectors in the columns of $A$ span. If $A$ is [[linearly dependent]] it is obvious that $\det(A)=0$, and equality may be achieved on the right hand side as well in this case if $A=0$. However, if the columns of $A$ are mutually [[orthogonal]] it follows that the inequality above is actually equality if and only if this condition is satisfied. 

### Proof 1.) Using [[QR Factorization]]:
If $A$ is rank deficient then the identity is trivially true due to the positive definiteness of norms:
$$|\det(A)|=0\leq \prod_{j=1}^m\|a_{j}\|_{2}$$

Now consider when $A$ is full rank $\implies A=QR$. 
$$|\det(A)|=|\det(QR)|=|\det(R)|=\left| \prod_{i=1}^m|r_{ii}|\right|$$
Notice that:
$$a_{j}=\sum_{i=1}^jr_{i}q_{j}$$
Since $q_{j}\perp q_{i}$ for $i \neq j\implies$ we can use the Pythagorean theorem to express the following:
$$\|a_{j}\|^2=\sum_{i=1}^j\|r_{ij}\cdot\vec{q}_{i}\|^2=\sum_{i=1}^j(r_{ij})^2 \implies r_{jj}^2 \leq \|a_{j}\|_{2}^2 \iff r_{jj} \leq \|a_{j}\|_{2}$$
$$\implies \prod_{i=1}^m r_{ii} \leq \prod_{i=1}^m\|a_{j}\|_{2} \iff \det(A) \leq\prod_{i=1}^m\|a_{j}\|_{2}  $$
$$\textcolor[RGB]{153, 115, 235}{\boxed{\therefore |\det(A)|\leq \prod_{j=1}^m\|a_{j}\|_{2}}}$$
