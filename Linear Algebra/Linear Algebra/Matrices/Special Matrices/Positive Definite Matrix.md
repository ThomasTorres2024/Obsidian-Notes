---
title: Positive Definite Matrices
draft: "false"
tags:
---
# Definition of Positive Definite Matrix

A Positive Definite matrix, $A$ is defined as $A \in \mathbb{C}^{n \times n}$  and $A^H=A$, where $x^HAx>0$ except for $x=0$ which yields $x^HAx = 0$.

Some equivalent conditions for $A$ being positive definite are:

1. $A$ has a Cholesky factorization
2. $A$ has an LDV factorization where each $D_{ii}>0$
3. All principal submatrices of $A$ are positive definite
4. All eigen values of $A$ are positive 

---
# Properties 0

### $AA^T$ and $A^TA$ are SPD 
For any matrix $A \in \mathbb{R}^{n \times m}$ the matrix $A^TA$ and $AA^T$ are both positive definite matrices. Suffice to say, this class of matrices is commonly used and extremely important.  We make use of this when deriving the SVD of any matrix $A$.

$$x^TA^TAx=(Ax)^T(Ax)= \|A\vec{x} \|_{2}^2 \geq 0$$

Which is to say that the inner product of $A\vec{x}$ with itself is guaranteed to be greater than or equal to zero.  
### Sum of SPD matrices is SPD 
Consider $A$ and $B$ which are SPD:

$$x^T(A+B)x=x^TAx + x^TBx>0$$

Since $x^T(A+B)x >0$ then $A+B$ is also SPD.
#### Inverse of SPD matrix is SPD
We also know that for a SPD matrix $A$ that $A^{-1}$ is another SPD matrix. For any eigen value $\lambda \in \wedge(A)$it follows that $A\vec{x}=\lambda\vec{x}$. But since we know that $A^{-1}\vec{x}=\frac{1}{\lambda}\vec{x}$, we can conclude that $A^{-1}$ must be another symmetric positive definite matrix since every $\lambda > 0$ for a SPD matrix, so $\frac{1}{\lambda} > 0$, which indicates that $A^{-1}$ must also be SPD. 

### Tr($A$) $>0$ and Det($A$)>0

Since all $\lambda \in \wedge(A) >0$, it follows that:

$$\text{det}(A)=\prod_{i=1}^{n}\lambda_{i}>0$$
$$\text{det}(A)=\sum_{i=1}^{n}\lambda_{i}>0$$

---
# Proof That if $A^T=A$ and $A$ has an LU Decomposition then $A$ is SPD iff $A$ has all positive eigen values 

Let $A \in \mathbb{R}^{n \times n}$ and $A$ has an LU decomposition. 

## Case 1 $(\implies) \text{ all eigen values of } A \text{ are positive } \implies \text{ A is SPD}$

Since we assume that $A$ has all positive eigen values and is symmetric, we know that $\exists U,D \in \mathbb{R}^{n \times n}$ where $U$ is orthogonal and $D$ is diagonal such that we can express $A$ as: 

$$A=UDU^T=UD^TU^T=A^T$$

Due to spectral theorem, we know that the vectors which form $U = [u_{1},u_{2},\dots u_{n}]$ for $\mathbb{R}^n$, therefore any arbitrary $\vec{x} \in \mathbb{R}^n$ can be expressed as a linear combination of vectors from basis $U$:

$$\vec{x}= \sum_{i=1}^n \alpha_{i}\vec{u_{i}} \text{ where each } \alpha_{i} \in \mathbb{R}$$
Thus we can re-express $x^TAx$ as:

$$\vec{x}^TA\vec{x}= \left(\sum_{i=1}^n \alpha_{i}\vec{u_{i}} \right)^T \cdot A \cdot \left(\sum_{i=1}^n \alpha_{i}\vec{u_{i}}\right)$$
$$=\left(\sum_{i=1}^n \alpha_{i}\vec{u_{i}}^T \right) \cdot \left(\sum_{i=1}^n \alpha_{i}A\vec{u_{i}}\right)$$
$$=\left(\sum_{i=1}^n \alpha_{i}\vec{u_{i}}^T \right) \cdot \left(\sum_{i=1}^n \alpha_{i}\lambda\vec{u_{i}}\right)$$
$$=\sum_{j=1}^n\left(\sum_{i=1}^n \alpha_{j}\alpha_{i}\vec{u_{j}}^Tu_{i} \right)$$

For all values where $i\neq j$, since every vector in $U$ is mutually orthogonal it follows that the only term that survives is when $i=j$ which yields:

$$\vec{x}^TA\vec{x}= \sum_{i=1}^n \alpha_{i}^2\lambda \|u_{i} \|^2$$
In conclusion each term of this sum is guaranteed to be non-negative. It is ONLY zero when each $\alpha_{i}=0$ which is to say $\vec{x}=\vec{0}$.

In conclusion, $\vec{x}^TA\vec{x} > 0$ and $\vec{x}^TA\vec{x} = 0 \Longleftrightarrow \vec{x} =0$

## Case 2 $(\Longleftarrow)$ $A \text{ is SPD } \text{ all eigen values of } A \text{ are positive}$

Since $A$ is SPD, it follows that: 

$$A=A^T$$
$$x^TAx \geq 0, \forall \vec{x} \in \mathbb{R}^n$$
Using spectral theorem, we can re-write $A=UDU^T$ where $D$ is an $n \times n$ diagonal matrix and $U$ is an $n \times n$ orthogonal matrix. It follows that: 

$$A=UDU^T=UD^TU^T=A^T$$

Since we know that $x^TAx\geq0$ consider the $i$th identity vector given by $x=Ue_{i}$

$$e_{i}^TAe_{i}=e_{i}^TU^T(UDU^T)Ue_{i}=e_{i}^TDe_{i}=\lambda e_{i}^Te_{i}=\lambda$$
Since $x^TAx \geq 0$ and we know that $\lambda \neq 0$ it follows that $\lambda \geq 0$. 

---
