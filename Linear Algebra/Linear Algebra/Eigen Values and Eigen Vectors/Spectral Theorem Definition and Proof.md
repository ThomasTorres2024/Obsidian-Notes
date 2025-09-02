---
title: Spectral Theorem Definition and Proof
draft: 
tags:
---
- - -
# Spectral Theorem Definition 

Note that I included a proof for this under special matrices as well, and the proof is different. 

The spectral theorem states that for all Hermitian Matrices where $A \in \mathbb{R}^{n \times n}$:

1.  $A$  has real [[eigen value]]s
2.  [[Eigen Vectors]] corresponding to distinct eigen values in $A$ are [[orthogonal]]
3.  $A$ is orthogonally diagonalizable

- - - 
<h3 align="center">Proof that Eigen Values are Real for Symmetric Matrix A</h3>

Given that $\lambda$ is an eigen value of $A$ and that $\vec{v}$ is a corresponding eigen vector $\lambda$ , we want to show that $\lambda = \overline{\lambda}$, that $\lambda \not \in \mathbb{C}$.  Suppose that $\lambda \in \mathbb{C}$.

Begin with the original identity, and apply the [[Transpose]] operator. Then right multiply everything by $\overline{\vec{v}}$
$$A \vec{v} = \lambda \vec{v}$$
$$\Longleftrightarrow (A\vec{v})^T = (\lambda \vec{v})^T$$
$$\Longleftrightarrow \vec{v}^TA^T = \overline{\lambda} \vec{v}^T$$
$$\Longleftrightarrow \vec{v}^TA = \lambda \vec{v}^T $$
$$\Longleftrightarrow v^TA \overline{v} = \lambda v^T \overline{v} $$

We will consider what happens when we apply the conjugate of both sides of $A \vec{v} = \lambda \vec{v}$, which in turn results in $A \overline{{v}} = \overline{\lambda v}$. A remains $A$ as we know $A \in \mathbb{R}^{n \times n}$ and its conjugate is simply itself.

Substituting:
$$ v^TA \overline{v} = v^T \overline{\lambda v} = \overline{\lambda} v^T \overline{v} $$
Note that $\vec{v} \neq \vec{0}$ since $\vec{v}$ is an eigen vector, and eigen vectors are by definition non-zero.
Notice that both $(1)$ and $(2)$ are equivalent so we can write that: 
$$\lambda v^T \overline{v} = \overline{\lambda} v^T \overline{v} \Longleftrightarrow \lambda<v,v> = \overline{\lambda}<v,v> \Longleftrightarrow \lambda = \overline{\lambda} $$
Since $\lambda = \overline{\lambda}$ it follows that $\lambda \in \mathbb{R}$

### Alternative Proof that Eigen Vectors of a [[Hermitian]] Matrix are Real 

Consider the eigen value $\lambda$ with the associated eigen-vector $\vec{x}$ of the Hermitian matrix  $A\in \mathbb{C}^{n \times n}$. 

It follows that: 

$$\lambda \|\vec{x} \|^2=\lambda \vec{x}^H\vec{x}=\vec{x}^H\lambda\vec{x}=\vec{x}^HA\vec{x}=\vec{x}^HA^H\vec{x}=(A\vec{x})^H\vec{x}=\bar{\lambda}\vec{x}^H\vec{x}=\bar{\lambda}\| \vec{x} \|^2$$

Since $\lambda = \bar{\lambda}$ it follows that $\lambda \in \mathbb{R}$

---
# Proof Of Spectral Theorem for Hermitian Matrices

Consider the Hermitian matrix $A$. By Schur's Triangularization, it follows that: 

$$A=UDU^T=A^H=UD^HU^T$$
$$D=D^H$$

Where $U,D \in \mathbb{R}^{n \times n}$, and $U$ is orthogonal and $D$ is an [[upper triangular matrix]]. 

Since $D=D^H$, it follows that $D$ is both upper triangular and lower triangular, so in actuality $D$ is diagonal. Furthermore, since $D=D^H \implies D_{ii}= \bar{D_{ii}}^H$, which is to say that each entry of the diagonal matrix must be real. 

Since each diagonal entry is an eigen-value, this means the eigen values of $D$ are necessarily real. 

Lastly we can show that eigen vectors are orthogonal easily. Consider $\vec{x},\vec{y} \in R^{n}$ that are both distinct eigen-vectors with eigen values $\lambda,\mu$ respectively such that $\lambda \neq \mu$. It follows then that:
$$A\vec{x}=\lambda \vec{x}$$
$$\vec{x}^HA^H=\lambda\vec{x}^H$$
$$\vec{x}^HA \vec{y}=\lambda\vec{x}^H\vec{y}$$
$$\mu \vec{x}^H\vec{y}=\lambda\vec{x}^H\vec{y}$$
$$\mu \vec{x}^H\vec{y}-\lambda\vec{x}^H\vec{y}=0$$
$$(\mu-\lambda)\vec{x}^H\vec{y}=0$$
$$\vec{x}^H\vec{y}=<\vec{x},\vec{y}>=0$$
In conclusion, the inner product between any eigen vectors corresponding to distinct eigen values is 0, thus the two vectors are orthogonal.

$\therefore$ for any [[Hermitian matrix]] $A$, it follows its eigen values are real, it is [[unitarily diagonalizable]], and has orthogonal eigen vectors corresponding to distinct eigen values.
  - - - 
# Proof that the eigen vectors of A form a basis of $\mathbb{R}^n$

For symmetric matrices $A$, $\exists$ an orthogonal matrix $R$ such that $R^{-1}AR$ is [[diagonal]]. 
Let $\lambda \in \mathbb{R}$ and is an eigen value of $A$ with corresponding eigen vector $\vec{v}_{1}$. Consider $\vec{v}_{1}$ which is normalized. 

We wish to extend $\vec{v}_{1}$ to be extended to a basis of $\mathbb{R}^n$ which will make use of $\{ v_{1}, u_{2}, u_{3}, \dots , u_{n}  \}$ where we have a basis consisting of eigen values corresponding to each eigen value that are not normalized denoted by $u_{k}$. We will then run the Gram-Schmidt process on this basis to force orthonormality.

The matrix, $P = [ v_{1},v_{2}, \dots , v_{n} ]$ is the matrix obtained by running  [[The Gram-Schmidt Process]]  on the above [[basis]].  Note that $P$ is an ort[[orhogonal matrix]], so we know that $P^T = P^{-1}$ and that as well $PP^T = P^TP=I_{n \times n}$.

Note the similarity transformation $B = P^T A = P$. We want to argue that $B$ is a symmetric matrix. 
We can determine this easily by considering $B^T$:
$$B = P^T A P \Longleftrightarrow B^T = P^TA^TP \Longleftrightarrow B^T = P^TA P$$
  Since $B=B^T$ it is symmetric.

We can further show that $B$ must be a diagonal matrix. Consider multiplying it by $e_{k}$
 where $k \in \mathbb{N}$. $e_{k}$ is the $k$th identity vector.

$$Be_{k}=P^TAP{e_{k}}=P^TAv_{k}= \lambda_{k} P^Tv_{k} = \lambda_{k} e_{k}$$
Note, the reason we can do the last step comes from thinking of multiplication of $v_{k}$ by the rows of $P$, which results in $0$ at all indices other than 1 due to properties of the inner product. 

Thus, since each column of $B$ consists of $e_{k} \cdot \lambda_{k}$ it follows that $B$ is a [[diagonal matrix]] consisting of the eigen values of each eigen vector.

We can prove this inductively using this line of argument but I will not put it here. 

- - -

# Real Spectral Theorem 

The Real Spectral Theorem states that if $A \in \mathbb{R}^{n \times n}$ and $A=A^T \Longleftrightarrow$  $A=UDU^T$ where $U,D \in \mathbb{R}^{n \times n}$ and $U$ is orthogonal and $D$ is diagonal. 

To put it in plain English,  the normal matrix $A$ has a real unitary diagonalization if and only if $A=A^T$ and $A \in \mathbb{R}^{n \times n}$.

## Case 1: $U,D \in \mathbb{R}^{n \times n}\implies A\in \mathbb{R}^{n \times n} \text{ and } A^T=A$

$$A=UDU^T = (UDU^T)^T=A^T$$

Since all entries of $U$ and $D$ are real, and it follows that addition and multiplication are closed over the reals, it follows that each entry of $A$ must also be real. Therefore, it must be the case that $A=A^T$ and $A \in \mathbb{R}^{n \times n}$.

## Case 1: $U,D \in \mathbb{R}^{n \times n}\Leftarrow A\in \mathbb{R}^{n \times n} \text{ and } A^T=A$

We already know that since $A^T=A$ that $D\in \mathbb{R}^{n \times n}$, since $D$ consists of the eigen values of $A$ and each eigen value of a Hermitian matrix is real. 

We must lastly argue that $U$ is real.  To do this, let us assume that for eigen value $\lambda \in \mathbb{R}$ with associated eigen vector $\vec{x} \in \mathbb{C}^n$, that we can construct our orthogonal matrix using only real eigen vectors. 

Notice that if we set up the eigen-vector identity for $A$ that the complex conjugate of $\vec{x}$ is also an eigen-vector of $A$. Since $A$ consists of real entries and $\lambda$ is also real, we can ignore the conjugate operator there.

$$A\vec{x}=\lambda \vec{x} \Longleftrightarrow \bar{A\vec{x}} = \lambda \bar{\vec{x}} \Longleftrightarrow A\bar{\vec{x}} = \lambda \bar{\vec{x}}$$

Note also that $\vec{x} + \bar{\vec{x}} \in \mathbb{R}^n$. This is because the entries of each consist of each index of the new vector consists of the form $a+bi + a - bi$, which clearly removes each complex component. 

We can also observe that this vector will be an eigen vector: 

$$A(\vec{x}+\bar{\vec{x}})=A\vec{x}+A\bar{\vec{x}}=\lambda\vec{x}+\lambda\bar{\vec{x}}=\lambda(\vec{x} +\bar{\vec{x}})$$
Since every eigen vector of $A$ can be expressed using only real values, it follows that we can construct some $U$ using only real eigen vectors. In conclusion, $\exists U \in \mathbb{R}^{n \times n}$.

In conclusion, $A^T=A$ and $A \in \mathbb{R}^{n \times n} \implies$ $U,D \in \mathbb{R}^{n \times n}$




