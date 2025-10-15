---
title: Givens Matrix
tags:
draft: "False"
---
# Given's Matrix
Given's matrix is a [[Unitary Matrices]], so for this instance it is particularly important to think of it in the context of being a rotation or reflection, which can introduce zeroes one at a time into a vector. For instance take the $2 \times 2$ case. Given a non-zero vector $[a_{1},a_{2}]^T$, we can force $a_{2}$ to $0$ while preserving the magnitude of the vector. This is the case since the givens is Hermitian and thus preserves the [[norm]] of a vector. Consider the following:
$$\begin{bmatrix} c & s\\ -s & c \end{bmatrix} \begin{bmatrix} a_{1}\\a_{2} \end{bmatrix}=\begin{bmatrix} \alpha\\0 \end{bmatrix}$$
If we expanded this it would be equivalent to writing:
$$\begin{bmatrix} a_{1}& a_{2}\\0&-a_{1}-a_{2}^2/a_{1} \end{bmatrix}\begin{bmatrix} c\\s \end{bmatrix}=\begin{bmatrix} \alpha \\ -\alpha a_{2}/a_{1} \end{bmatrix}$$
We can solve by [[back-substitution]] and then obtain:
$$s=\frac{\alpha a_{2}}{a_{1}^2+a_{2}^2}$$
$$c=\frac{\alpha a_{1}}{a_{1}^2+a_{2}^2}$$
Since the matrix is unitary it follows that $\det(G)=\pm1$, so $\det(G)=c^2+s^2=1$, thus we can express $s$ and $c$ respectively as:
$$s=\frac{ a_{2}}{\sqrt{a_{1}^2+a_{2}^2}}$$
$$c=\frac{ a_{1}}{\sqrt{a_{1}^2+a_{2}^2}}$$

---
## Example With $2 \times 2$ Matrix: 

- Let $\mathbf{a} = \begin{bmatrix} 4 \\ 3 \end{bmatrix}^T$

- To annihilate second entry we compute cosine and sine  
  $$
  c = \frac{a_1}{\sqrt{a_1^2 + a_2^2}} = \frac{4}{5} = 0.8 \quad \text{and} \quad 
  s = \frac{a_2}{\sqrt{a_1^2 + a_2^2}} = \frac{3}{5} = 0.6
  $$

- Rotation is then given by  
  $$
  G = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} = 
  \begin{bmatrix} 0.8 & 0.6 \\ -0.6 & 0.8 \end{bmatrix}
  $$

- To confirm that rotation works,  
  $$
  G\mathbf{a} = 
  \begin{bmatrix} 0.8 & 0.6 \\ -0.6 & 0.8 \end{bmatrix}
  \begin{bmatrix} 4 \\ 3 \end{bmatrix}
  = \begin{bmatrix} 5 \\ 0 \end{bmatrix}
  $$
---

# Generalizing Given's Beyond the $2 \times 2$ Case 
We can use given's to get zeros in a vector of arbitrary size. We need to be able to select one two distinct values from our vector, and construct our givens matrix. We can construct the given matrix that will case the value $a_{2}$ to go to $0$ and the $a_{1}$ to go to $\|a\|$ by  constructing a matrix of the following form:

$$\begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & c & 0 & s & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & -s & 0 & c & 0 \\
0 & 0 & 0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
a_1 \\
a_2 \\
a_3 \\
a_4 \\
a_5 \\
\end{bmatrix}
=
\begin{bmatrix}
a_1 \\
\alpha \\
a_3 \\
0 \\
a_5 \\
\end{bmatrix}$$
At the corresponding values of our indices, we replace the principal diagonal entries with $c$ and $s$ where the two cosine entries "intersect". Essentially, we are embedding the $2 \times 2$ in higher dimensional matrices each time, and then multiplying them by $a$ to obtain our scaled vector. 

---
# Applications to [[QR Factorization]]
We can use this property to obtain $R$ and $Q$ from a series of left multiplications of $A$ by different given matrices $Q_{ij}$ where each $i,j$ takes out an entry below the principal diagonal. This gives us $R$ at the very end after all of the multiplications. If we keep a record for what the $Q$s are, we can eventually take the product of them at the end and get $Q^T$, then we can take the transpose of this matrix to get $Q$ back, so in turn we can get a $QR$ factorization. 

Each [[Givens Matrix]] is orthogonal, so their product is another [[orthogonal matrix]] or [[Unitary Matrices]] in the context of complex numbers. 

This is particularly good in the case where we have a special matrix like maybe an [[Upper Hessenberg Matrix]], [[Lower Hessenberg Matrix]], [[Bidiagonal Matrix]], or some other matrix with a distinct structure which we can readily exploit instead of having to use [[Householder Transformation]]s which are more generalized and could be more costly in these instances. 

---
# Advantages and Disadvantages 
We do about 50% more work than the [[House Holder Reflectors]], needs more storage, and we only introduce one zero at a time instead of just doing a mass annihilation of a column with [[Householder Transformation]]s. We can overcome these disadvantages with a more complicated implementation however, and we can get some better performance if our matrix has a special sparser structure that we can tear down instead of having to do house holder on everything. 