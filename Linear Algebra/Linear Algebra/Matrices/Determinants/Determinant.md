---
title: Determinant
draft: "false"
tags:
---
# Determinant Definition

In the two by two case, for a 2x2 matrix we have that its determinant is:
$$\text{det}\left(\begin{bmatrix} a & b\\ c& d \end{bmatrix} \right)=ad-cb$$
We also use bars around a matrix to denote the determinant around a matrix, and in the context of the MTH 437 course is not absolute value. 

We can compute higher dimensional matrices by using the cofactor expansion by computing the sum of the determinant of correctly signed minor matrices. 

We can also use any row or column to iterate over in order to compute our determinant. Any even valued iteration in our expansion will have a negative sign in front of it. 

---
# Properties of the Determinant 
The properties of the determinant appear to come from fundamental Row Operations that we can perform on matrices. They effect the determinant of the matrix in the following ways:
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
