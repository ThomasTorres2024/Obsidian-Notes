---
title: Spectral Theorem Definition and Proof
draft: 
tags:
---
- - -
# Spectral Theorem Definition 

Note that I included a proof for this under special matrices as well, and the proof is different. 

The spectral theorem states that for all Hermitian Matrices where $A \in \mathbb{R}^{n \times n}$:

1.  $A$  has real [[Eigen Value]]s
2.  [[Eigen Vector]]s corresponding to distinct eigen values in $A$ are [[orthogonal]]
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

$\therefore$ for any [[Hermitian]] matrix $A$, it follows its eigen values are real, it is unitarily [[diagonalizeable]], and has orthogonal eigen vectors corresponding to distinct eigen values.
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

---
# Projections and [[Spectral Theorem]]

### Theorem).
For any Self-[[Adjoint]] [[Linear Transformation]], $A$, on a finite dimensional inner product space, there corresponds, $\alpha_{1},\alpha_{2},\alpha_{3},\dots ,\alpha_{r}$ with [[Projection]]s $E_{1},E_{2},\dots,E_{n}$such that they are all orthogonal and non-zero, then the following is true:

1. $\alpha_{j}$are pairwise distinct
2. the $E_{j}$ are pairwise orthogonal and non-zero
3. $\sum_{j}E_{j}=1$
4. $\sum_{j}\alpha_{j}E_{j}=A$

$Proof).$
Let $\alpha_{1},\dots,\alpha_{r}$ be the [[Eigen Value]]s of $A$ and let $E_j$ be the perpendicular projection on the subspace consisting of all solutions of $Ax=\alpha_{j} x$. This ensures condition $(1)$ clearly. This entails that each $x$ is an eigen vector corresponding to the eigen value $\alpha_{j}$, furthermore by spectral theorem these must be orthogonal thereby each projector is also mutually orthogonal. 

Now we can see that if $E=\sum_{j}E_{j}$ then $E$ must be another perpendicular projection. Notice that $\text{dim}(E)=\text{dim}\left( \sum_{j} E_{j} \right)=$ the dimension of the entire space which entails $(3)$ namely that $E=\sum_{j}E_{j}=I$. 

In order to prove $(4)$, consider any vector $x$, and then write $x_j=E_{j}x$. It then follows that:
$$Ax_{j}= \alpha x_{j}$$
This comes from the definition of each $E_{j}$ as being the set of all vectors fulfilling the above.
$$\begin{align}
Ax=A(Ix)=A\left( \sum_{j}E_{j}x \right) = \sum_{j}Ax_{j} =  \\
\sum_{j}\alpha_{j} x_{j} = \sum_{j} \alpha_{j} E_{j} x
\end{align}$$
And thus we have that $A=\sum_{j}\alpha_{j}E_{j}$ This concludes $(4)$ and thereby the proof.

The expression of $A=\sum_{j} \alpha_{j} E_{j}$ is known as the 'spectral form' of $A$. Now we shall prove its uniqueness.
### Theorem 2). 
If $\sum_{j=1}^r\alpha_{j}E_{j}$ is the spectral form of a self adjoint linear tf on a finite dimensional inner product space, then the $\alpha's$ are all distinct eigen values of $A$. 

Moreover, for $1\leq k\leq r$, then there there exist polynomials $p_{k}$ with real coefficients such that $p_{k}(\alpha_{j})=0$ whenever $j \neq k$ and that $p_{k}(a_{k})=1$ for every such polynomial $p_{k}(A)=E_{k}$. 

$Proof$).
Each $E_{j}\neq0$ and thus has some $x$ such that $E_{j}x=x$ and $E_{i}x=0 \forall i\neq j$, thus we have:
$$Ax=\sum_{j=1}^n( \alpha_{j} E_{j}x )=\alpha_{j}x \implies \alpha_{j} \text{ is eig of }A$$
Conversely let $\lambda$ be an eig of $A$, then for any $Ax=\lambda x$ for $x\neq0$, denote $x_{j}=E_{j}x$,and then:
$$Ax=\lambda x = \lambda \sum_{j}x_{j}$$
And thus:
$$Ax=A\left( \sum_{j} x_{j} \right)=\sum_{j} \alpha_{j} x_{j}$$
And then we have that:
$$\sum_{j} (\lambda - \alpha_{j})x_{j}=0 \implies \lambda -\alpha_{j} = 0$$
We know that the set formed is linearly independent between the $x$'s since they are orthogonal. And thus $\lambda$ is equal to one of the $\alpha_{j}'s$. 
### Theorem).
If $\sum_{i=1}^r \alpha_{j}E_{j}=A$ for $A=A^H$, then a necessary and sufficient condition such that $AB=BA$ is that $B$ commutes with each $E_{j}$. 

$Proof).$ 
The sufficiency of the condition is trivial, since it can clearly be algebraically verified that the result holds. Secondly. we can check the necessity condition. Let $A,B$ commute with one another. (I don't understand this), then from commutation we get that $B$ commutes with each polynomial in $A$, and therefore $B$ commutes with $E_j$. 

As a point to make, we can generalize the spectral definition easily to the case with infinite dimensional vector spaces, and it beats out standard notation sometimes. 

