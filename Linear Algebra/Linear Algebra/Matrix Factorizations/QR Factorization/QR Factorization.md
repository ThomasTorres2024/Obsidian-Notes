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
Notice in the [[Full QR]] factorization, we have that $\tilde{Q} \perp R(A)$, since the first $n$ vectors that comprise $\hat{Q}$ satisfy $\hat{Q} \equiv R(A)$. Notice that every vector in $x \in \hat{Q}$  and every vector $v \in \tilde{Q}$ satisfies $x^Tv=0$, to the two subspaces are orthogonal due to the properties of 

---
# Nested Subspace Property 
When we construct the QR factorization, we are constructing a basis by iteratively adding new vectors onto the basis that are linearly independent. We have a nice nested [[Vector Subspace]] property where if we add [[basis]] vectors $a_{1},a_{2},\cdots a_{n}$ it follows that:
$$\{a_{1} \} \subseteq \{a_{1},a_{2} \} \subseteq \{a_{1},a_{2},a_{3} \} \subseteq \cdots \subseteq \} \subseteq \{a_{1},a_{2}, a_{3}, \cdots a_{n} \}$$

---
# Existence and Uniqueness
### Theorem Every matrix $A \in \mathbb{C}^{m \times n}$ such that $m \geq n$ has a full [[QR Factorization]], and therefore a [[Reduced QR]] factorization
Every matrix $A \in \mathbb{C}^{m \times n}$ such that $m \geq n$ has a full [[QR Factorization]], and therefore a [[Reduced QR]] factorization. If $A$ is [[linearly independent]], the [[The Gram-Schmidt Process]] allows us to argue that it has a [[QR Factorization]]. [[The Gram-Schmidt Process]] only  fails when one of the column vectors of $A$ is linearly independent, resulting in one of the vectors $q$ becoming a zero vector, which removes the possibility for a proper QR factorization. If it is given that $A$ is linearly independent this is impossible. 

If $A$ is [[linearly dependent]], then in our QR factorization algorithm, one of our resulting vectors $v_{j}$ from the orthogonalization process is 0, so we begin orthogonalization again 
some arbitrary $q_{j}$ from $Q$ again.  

Full QR factorization is obviously not unique, since we can arbitrarily re-arrange the remaining vectors in $\tilde{Q}$ without affecting the resulting matrix $A$ from $A=[\hat{Q}|\tilde{Q}]R$ since all of the values from $\tilde{Q}$  are zeroed out. Another way in which the non-uniqueness of the [[QR Factorization]] can be observed by multiply some row $j$ in $R$ by $|z| \neq 0$ and column $j$ of $Q$ by $|z|^{-1}$ then we observe that we have a different QR factorization where $A=QR$, we have another QR factorization even for the reduced case. 

### Theorem Every matrix $A \in \mathbb{C}^{m \times n}$ such that $m \geq n$ has a full [[QR Factorization]] that is unique when $A$ is of full rank 
Because $A$ is of full rank, the diagonal entries from the matrix $R$ are guaranteed to be non-zero since each column vector in $A$ is linearly independent. It follows that we will get a full description using the QR factorization up to the point of the sign of each $q$ and the sign of each diagonal on $R$. Thus our QR factorization is fully described. If we fix each diagonal entry of $R$ to be zero, then we can obtain a unique QR factorization. Otherwise, we still have this difference to account for. 

---
# QR Factorization for Continuous Functions 
There is analogue for expanding complex functions that is an extension of that of vectors. Instead of considering $\mathbb{C}^m$ we choose $L^2[-1,1]$, which consists of a [[vector space]] of complex functions on the interval $[-1,1]$. 

The inner product of two functions $f,g\in L^2[-1,-1]$ then the [[inner product]] between these two functions is:
$$\langle f, g\rangle = \int_{-1}^1\overline{f(x)}g(x)dx$$
For example, we can consider the matrix consisting of monomials of $x^j$ where $1 \leq j \leq n:$ 
$$
A = \left[
\begin{array}{c|c|c|c|c}
\rule{0pt}{2.5ex}1 &
\rule{0pt}{2.5ex}x &
\rule{0pt}{2.5ex}x^2 &
\rule{0pt}{2.5ex}\cdots &
\rule{0pt}{2.5ex}x^{n-1}
\end{array}
\right]

$$
$$
A = QR =
\begin{bmatrix}
q_0(x) \mid q_1(x) \mid \cdots \mid q_{n-1}(x)
\end{bmatrix}
\begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n} \\
0      & r_{22} & \cdots & r_{2n} \\
\vdots & 0      & \ddots & \vdots \\
0      & \cdots & 0      & r_{nn}
\end{bmatrix}
$$

Then we can express $A$ using a QR factorization where each $q$ is a function from an orthonormal basis of functions on $L^2[-1,1]$, and  

We are able to construct an orthonormal basis of functions $q_{i}(x)$ that satisfy:
$$\int_{-1}^1\overline{q_{i}(x)}q_{j}(x)dx= \delta_{ij} =\begin{cases} 1 \text{ if i =j}\\0 \text{ if i} \neq j \end{cases}$$
$q_{j}$ is a polynomial of degree $j$. We can describe the [[vector space]] of polynomials using the Legendre polynomials, $P_{j}$ which have the basis given by: 
$$P_{0}(x)=1,P_{1}(x)=x,P_{2}(x)=\frac{3x^2-1}{2},P_{3}(x)=\frac{5x^3-3x}{2}$$
The [[Legendre Polynomials]] are a basis for the polynomials of degree $j$, but they are furthermore an [[orthogonal]] basis that spans the set of polynomials. 

---
# Applications 

We can use $QR$ factorization to compute [[Least Squares]] and to compute [[eigen values]].  QR factorization is especially useful for eigen value problems, [[Krylov Methods]], and many other methods. Having an orthonormal basis is significantly more desirable than having a potentially [[ill-conditioned]] matrix. 

#### Solving Ax=b with [[QR Factorization]]
[[QR Factorization]] can be used to solve the matrix equation $Ax=b$:
$$Ax=b \iff QRx=b \iff Rx=Q^Tb$$
And we can use [[back-substitution]] to solve for $x$ after solving the system $Rx$. We solve the following: 

1. Compute a [[QR Factorization]] of $A$, $A=QR$ 
2. Compute $y=Q^Hb$ 
3. Solve $Rx=y$ for $x$ 

