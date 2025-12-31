---
title: Schur's Triangularization
draft: "false"
tags:
---
# Schur's Triangularization Theorem 
Schur's Triangularization Theorem state that's any $A \in \mathbb{C}^{n \times n}$ can be written as the product of an [[orthogonal matrix]], $U \in \mathbb{C}^{n \times n}$ and [[upper triangular matrix]] $T_{A} \in \mathbb{C}^{n \times n}$:
$$A=UT_{A}U^H$$

It is possible for $T_{A}$ to be a [[diagonal matrix]], which implies that $A$ is then unitarily diagonalizable, but generally it is not.

This is a [[similarity transformation]] and we can derive various theorem about the [[determinant]] and the [[eigen values]] of $A$ from it. 
- - -
# Proof 

We can prove this result via induction. We will prove that any square $A$  can be expressed as $A=UT_{A}U^H$ where $A,U,T \in \mathbb{R}^{n \times n}$, $U$ is orthogonal, and $T_{A}$ is upper triangular. 

Consider the base case where $A \in \mathbb{R}^{1}$. Then consider $U$=1 and $T_{A}=A$ so we get the result that:

$$A=1 \cdot A \cdot 1^T = A$$
Since $U=1$ is orthogonal, $A$ is upper triangular, which implies that the base case of $n=1$ is true. 

For the inductive hypothesis, we assume that the result will hold for matrices of size $(n-1) \times (n-1)$.

Consider the [[characteristic polynomial]] of $A$ given by $P_{A}(\lambda).$ $P_{A}(\lambda)$ has $n$ roots, but allow us to consider the root $\lambda_{1}$ which is an eigen-value of $A$ with corresponding vector $\vec{v_{1}}$.

We can assume that $\| \vec{v_{1}} \| =1$ since, without loss of generality, any $\vec{v_{1}} \cdot c, c \in \mathbb{C}$ is still an eigen-vector. We know that $\dfrac{\vec{v_{1}} }{\| \vec{v_{1}}\|}$ is a unit vector. 

Using [[The Gram-Schmidt Process]] we can convert the [[Eigen Vectors]] of $A$ to be a set of [[orthonormal]] vectors. If we run out of eigen-vectors, we can consider their [[orthogonal complement]] and add them to the matrix. 

In total we have $n$ vectors that we will use to construct our orthogonal matrix, $V$.

Consider:
$$V =  \{ \vec{v_{1}} \vec{v_{2}} \dots \vec{v_{n}} \} = 
\left[
\begin{array}{c|c}
\vec{v_{1}} & V_{2} 
\end{array}
\right]
$$
where $V_{2} \in \mathbb{R}^{n\times(n-1)}$, which consists of all of the columns of $V$ except for the first vector $\vec{v_{1}}$. 

We will show that $U=V$ and that $T_{A}$ is an upper triangular matrix. Since we have established that $A=UT_{A}U^H$ we can see that $T_{A}=U^HAU$. We can more easily show this triangular result here. We will make the $U=V$ substitution below: 

$$U^HAU=\left[
\begin{array}{c|c}
\vec{v_{1}}^H\\ V_{2}^H 
\end{array}
\right]A\left[
\begin{array}{c|c}
\vec{v_{1}} & V_{2} 
\end{array}
\right]=\left[
\begin{array}{c|c}
\vec{v_{1}}^H\\ V_{2}^H 
\end{array}
\right]\left[
\begin{array}{c|c}
\vec{Av_{1}} & AV_{2} 
\end{array}
\right]=\left[
\begin{array}{c|c}
\vec{v_{1}}^HA\vec{v_{1}} & \vec{v_{1}}^HAV_{2} \\
\hline
V_{2}^HA\vec{v_{1}} & V_{2}^HAV_{2}
\end{array}
\right]$$

We know that $A \vec{v_{1}} = \lambda_{1} \vec{v_{1}}$ so $\vec{v_{1}}^H A \vec{v_{1}} = \lambda_{1}<\vec{v_{1}},\vec{v_{1}}> = \lambda_{1}$. 

Note also that since $V$ is an orthogonal matrix, by definition all $<\vec{v_{i}},\vec{v_{j}}>=0$ when $i \neq j$. So, $V_{2}^HA\vec{v_{1}}$ = 0.

Lastly notice that $V_{2}^HAV_{2}$ = $U_{2}T_{A_{2}}U^H$

$$\left[
\begin{array}{c|c}
\vec{v_{1}}^HA\vec{v_{1}} & \vec{v_{1}}^HAV_{2} \\
\hline
V_{2}^HA\vec{v_{1}} & V_{2}^HAV_{2}
\end{array}
\right]=\left[
\begin{array}{c|c}
\lambda_{1} & \vec{v_{1}}^HAV_{2} \\
\hline
0 & U_{2}T_{A_{2}}U^H
\end{array}
\right]$$


This matrix is nearly triangular, but notice that we can express it as a product of matrices which turns out to be of a triangular form: 

$$\left[
\begin{array}{c|c}
\lambda_{1} & \vec{v_{1}}^HAV_{2} \\
\hline
0 & U_{2}T_{A_{2}}U^H
\end{array}
\right]= \begin{bmatrix} 1 & 0\\0 & U_{2} \end{bmatrix} \left[
\begin{array}{c|c}
\lambda_{1} & \vec{v_{1}}^HAV_{2} \\
\hline
0 & T_{A_{2}}
\end{array}
\right] \begin{bmatrix} 1 & 0\\0 & U_{2}^H \end{bmatrix} $$

From this expression we can clearly see that the matrix in the center is an upper triangular matrix, and the matrices on the sides are both orthogonal. We see that the inductive hypothesis holds for $n$. In turn, we have obtained the result that $A$ can indeed be factored into a corresponding $UT_{A}U^H$

In turn, all entries of $T_{A}$ are the eigenvalues of $A$. 

---
# Important Corollaries 

For any $A \in \mathbb{C}^{n  \times n}$ we can obtain the following results: 

1. $\text{tr}(A)= \sum_{i=1}^n \lambda_{i}$
$$\text{tr}(A)=\text{tr}(U^HT_{A}U)=\text{tr}(U^HUT_{A})=\text{tr}(T_{A})=\sum_{i=1}^n \lambda_{i}$$



2. $\text{det}(A)= \prod_{i=1}^n \lambda_{i}$
$$\text{det}(A)= \text{det}(U^HT_{A}U)= \text{det}(U^H) \cdot \text{det}(T_{A}) \cdot \text{det}(U) = \text{det}(T_{A})= \prod_{i=1}^n \lambda_{i}$$

- - -
# 3. Cayley Hamilton Theorem

The proof for this corollary is more involved than the other two.

If $P_{A}(\lambda)$ is the characteristic polynomial of $A$, then $P_{A}(A)=0$. 

$$P_{A}(A)=P_{A}(UT_{A}U^H)= P_{A}(\lambda I_{n}-UT_{A}U^H) = P_{A}(\lambda U U^H-UT_{A}U^H)=P_{A}(U(\lambda I_{n}-T_{A})U^H)$$

$$= \prod _{i=1}^n U\left(\lambda I_{n}-T_{A}  \right)U^H= U \left( \prod _{i=1}^n \left(\lambda I_{n}-T_{A}  \right) \right)U^H =U P_{A}(T_{A})U^H$$

If we show that $P_{T_{A}}(T_{A})$ is 0, then it follows that $P_{A}(A)$ is 0 since $U(0_{n \times n}) U^H$ is 0. 

We can inductively argue that $P_{A}(T_{A}) = 0_{n \times n}$:

$$P_{T_{A}}(T_{A})=\begin{bmatrix} 0 & * & * & \dots & *
\\0 & * & * &\dots & * \\
0  & 0 & * & \dots   & *\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
0 & 0 & 0 & 0 & *\end{bmatrix} \cdot \begin{bmatrix} * & * & * & \dots & *
\\0 & 0 & * &\dots & * \\
0  & 0 & * & \dots   & *\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
0 & 0 & 0 & 0 & *\end{bmatrix} \cdot \begin{bmatrix} * & * & * & \dots & *
\\0 & * & * &\dots & * \\
0  & 0 & 0 & \dots   & *\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
0 & 0 & 0 & 0 & *\end{bmatrix}  \dots  \begin{bmatrix} 0 & * & * & \dots & *
\\0 & * & * &\dots & * \\
0  & 0 & * & \dots   & *\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
0 & 0 & 0 & 0 & *\end{bmatrix}$$

We can proceed with a formal proof of this statement using induction, however I will not go about this. Each zero column in the product of the above matrices will result in a new column of zeroes, which will eventually yield another zero matrix. Eventually, we would be able to see that $P_{T_{A}}(T_{A})=0_{n \times n}$

In conclusion it follows that $P_{T_{A}}(T_{A}) = 0_{n \times n}$, so $P_{A}(A)=U P_{T_{A}}(T_{A}) U^H = 0_{n \times n}$. In conclusion it follows that plugging a matrix into its own characteristic equation yields the zero matrix. 

This theorem allows us to express $A$ as a linear combination of powers of itself, for instance: 

$$A=a_{n}A^n+a_{n-1}A^{n-1}+\dots+a_{2}A^{2}+a_{1}A^1+a_{0}I_{n}$$
As an example consider: 

$$A=\begin{bmatrix}1 & 2\\ -2 & 1 \end{bmatrix}$$

$$P_{A}(\lambda)= (1-\lambda)^2+4=\lambda^2-2\lambda+5$$
Now we will compute $P_{A}(A):$
$$A^2 -2A+5I_{2}= \begin{bmatrix}-3 & 4\\-4 & -3 \end{bmatrix} -2\begin{bmatrix}1 & 2\\-2 & 1 \end{bmatrix} + 5\begin{bmatrix}1 & 0\\0 & 1 \end{bmatrix} = \begin{bmatrix}0 & 0\\0 & 0 \end{bmatrix}$$

We can also use the Caley Hamilton Theorem to compute the inverse of a matrix. In the above example consider: 

$$P_{A}(A)=A^2-2A+5I_{2}=0 \Longleftrightarrow I_{2}=\frac{1}{5} (-A^2+2A)=A \left(\frac{-1}{5}A+\frac{2}{5}I_{2} \right)$$

Since $I_{2}=A \left(\frac{-1}{5}A+\frac{2}{5}I_{2} \right) \Longleftrightarrow A^{-1} = \left(\frac{-1}{5}A+\frac{2}{5}I_{2} \right)$

Lastly, an important class of numerical methods for approximating eigen values and $\vec{x}$ in $A\vec{x}=\vec{b}$ come out of the Cayley-Hamilton theory. These methods are known are [[Krylov Methods]]. 