---
title: The Gram-Schmidt Process
tags: 
draft: "false"
---
# The Gram-Schmidt Process

The goal of the Gram-Schmidt process it convert a full column basis, $P = \{ \vec{p}_{1},\vec{p}_{2}, \cdots, \vec{p}_{n}  \}$, into a basis $Q = \{ \vec{q}_{1},\vec{q}_{2}, \cdots, \vec{q}_{n}  \}$ where each $\vec{q}_{i}$ is mutually [[orthogonal]] and has a magnitude of one. 

That is to say: 

$$ \vec{q}_{i} \cdot \vec{q}_{j} = \begin{cases} 1 & \text{if } i =j \\ 0 & \text{if } i \neq j \end{cases}$$

In this process, we start by getting an orthogonal vector $\vec{q}_{1}$ obtained by normalizing any vector in $P$. Then we iteratively go through each other vector in $P$ and define it by orthogonally projecting the other vectors in our orthogonal set onto the current vector we have selected. We then normalize this vector and add it to our new orthogonal set. We repeat this process until there are $n$ many vectors in $Q$. 

We define each $\vec{q}_{i}$ in $Q$ by the following: 

$$\vec{q}_{1}=\dfrac{\vec{p}_{1}}{\| \vec{p}_{1} \|}$$
$$\vec{q}_{i} = \dfrac{\vec{p}_{i} - \sum_{j=1}^{i-1} \vec{p}_{i}- \dfrac{<\vec{p}_{i},\vec{q_{j}}>}{<\vec{q}_{j},\vec{q}_{j}>} \vec{q}_{j}}{v_{i}}$$

Where each $v_{i} = \| \vec{p}_{i} - \sum_{j=1}^{i-1} \vec{p}_{i}- \dfrac{<\vec{p}_{i},\vec{q_{j}}>}{<\vec{q}_{j},\vec{q}_{j}>} \vec{q}_{j} \|$

For example:

$$\vec{q}_{1}=\dfrac{\vec{p}_{1}}{\| \vec{p}_{1} \|}$$
$$\vec{q}_{2}= \vec{p}_{2}- \dfrac{<\vec{q}_{1},\vec{p}_{2}>}{\| \vec{q}_{1} \|}$$
$$\vec{q}_{3}= \vec{p}_{3}- \dfrac{<\vec{q}_{1},\vec{p}_{3}>}{\| \vec{q}_{1} \|} - \dfrac{<\vec{q}_{2},\vec{p}_{3}>}{\| \vec{q}_{2} \|} $$

After we have chosen our first $\vec{p}_{i}$ from $P$ and have successfully normalized it, we then look for the next vector in $P$ and project it onto $\vec{p}_{1}$, then we orthogonalize the result, and keep adding so forth and so on. 

Intuitively, we can think of this as taking off the component of each vector which is parallel to the existing vector until we end up only with the orthogonal part, since we can break apart any vector into a [[linear combination]] of the vectors orthogonal to that vector and parallel to that part. 

In turn, we are just extracting the orthogonal part at each iteration of this process. 

---
# Proof that $\text{span}\{\mathcal{Q} \}$ = $\text{span}\{\mathcal{P}\}$

Let $P = \{\vec{p}_{1},\vec{p}_{2},\dots,\vec{p}_{n}\}$. Let $M =\{\vec{m}_{1},\vec{m}_{2},\dots,\vec{m}_{n} \}$ where each $\vec{m}_{i}=\vec{p}_{i} \cdot \alpha_{i}$ given that $\alpha_{i} \neq 0$.

Let us consider some $\vec{p} \in \text{span}(P) = \sum_{i=1}^n \beta_{i} \vec{p}_{i} = \beta_{1}\vec{p}_{1} + \beta_{2}\vec{p}_{2} + \cdots + \beta_{n}\vec{p}_{n}$, which shows a linear combination of elements from $P$.  

Let us also consider some $\vec{m} \in \text{span}(M) = \sum_{i=1}^n \delta_{i} \vec{m}_{i} = \delta{1}\vec{m}_{1} + \delta{2}\vec{p}_{2} + \cdots + \delta{n}\vec{p}_{n}$, 

We can show that $\text{span}(M) \subseteq \text{span}(P)$. We could represent any $\vec{p} \in \text{span}(P)$ by dividing each $\vec{m}_{i}$ by their corresponding constant that they scale $\vec{p}_{i}$ by, $\alpha_{1}$ and putting in the numerator $\beta_{i}$ which in turn would generate the arbitrary $\vec{p}$:

$$\sum_{i=1}^n \vec{m}_{i} \cdot \dfrac{\beta_{i}}{\alpha_{i}} = \sum_{i=1}^n \vec{p}_{i} \alpha_{i} \cdot \dfrac{\beta_{i}}{\alpha_{i}}=\sum_{i=1}^n \beta_{i} \vec{p}_{i}=\text{span}(P)$$
Likewise, we can show that $\text{span}(P) \subseteq \text{span}(M)$ if we choose that for each $\beta_{i}$ that we scale each $\vec{p}_{i}$ by to be $\alpha_{i} \cdot \delta_{i}$ :

$$\sum_{i=1}^n \beta_{i} \vec{p}_{i}=\sum_{i=1}^n \delta_{i} \cdot \alpha{i} \cdot \vec{p}_{i}=\sum_{i=1}^n \delta_{i} \cdot \vec{m}_{i}=\vec{m}$$

Since $\text{span}(P) \subseteq \text{span}(M) \wedge \text{span}(M) \subseteq \text{span}(P)$, it follows that $\text{span}(P) = \text{span}(M)$.
(I know there's an easier way to show it with this, but I opted to not use it, I'll probably use this later, somehow)

To prove that $Q$ and $P$ have equivalent span, we would be able to express each $\vec{q}_{i}$ that occurs and eventually break it into the constituent vectors from $P$, and then factor each vector out and this would be sufficient to show that any linear combination of vectors from $Q$ is in $\text{span}\{ P \}$. 

$$\vec{q} \in \text{span}\{\mathcal{Q} \}, \vec{q}= \sum_{i=1}^n \vec{q}_{i} \alpha_{1}=\sum_{i=1}^n \alpha_{1} \left(\vec{p}_{i} - \sum_{j=1}^{i-1} \vec{p}_{j} \dfrac{<\vec{q}_{j},\vec{p}_{i}>}{<\vec{q}_{j},\vec{q}_{j}>} \right)$$
$$=\sum_{i=1}^n \left (\alpha_{i} \vec{p}_{i} - \sum_{j=1}^{i-1} \vec{p}_{j} \beta_{ij} \right)$$
$$=\alpha_{1}\vec{p}_{1}+(\alpha_{2}+\beta_{21})\vec{p}_{2}+(\alpha_{3}+\beta_{31}+\beta_{32})\vec{p}_{3}+ \cdots + (\alpha_{2}+\beta_{n1}+\beta_{n2}+\cdots+\beta_{nn})\vec{p}_{n}$$
Which indicates that $\vec{q} \in \text{span}\{ \mathcal{P} \}$, so $\text{span}\{ \mathcal{Q} \} \subseteq \text{span}\{\mathcal{P} \}$.

To show that $\mathcal{P}$ spans $\mathcal{Q}$, let us consider $\vec{p} \in P$ where $\vec{p} = \sum_{i=1}^n \vec{p}_{i}\gamma_{i}$ 

Given that each $\vec{q}_{i}=\dfrac{p_{i}-\sum_{j=1}^n \vec{q}_{j} \dfrac{<\vec{q}_{j},\vec{p}_{i}>}{<\vec{q}_{j},\vec{q}_{j}>} }{\|v_{i}\|}$, each $p_{i}$ can be expressed by simply re-arranging the variables to the following: 

$$\vec{p}_{i}=\|v_{i} \|\vec{q}_{i}+\sum_{j=1}^n \vec{q}_{j} \dfrac{<\vec{q}_{j},\vec{p}_{i}>}{<\vec{q}_{j},\vec{q}_{j}>}$$
Thus we can express our $\alpha_{i} \cdot \vec{p}_{i}$ using the above expression, I will change the coefficients since they are being multiplied by $\alpha_{i}$ for the sake of standardization and to make this a lot easier on myself to:$$\gamma_{i} \cdot \vec{p}_{i}= \delta_{i} \vec{q}_{i}+\sum_{j=1}^n \vec{q}_{j}\cdot\beta_{ij}$$Likewise we can express $$\vec{p}=\gamma_{1}\vec{p}_{1}+\gamma_{2}\vec{p}_{2}+\cdots+\gamma_{n}\vec{p}_{n}$$
$$= \delta_{1}\vec{q}_{1}+(\delta_{2} \vec{q}_{2}+\sum_{j=1}^1 \vec{q}_{j}\cdot\beta_{2j})+(\delta_{3} \vec{q}_{3}+\sum_{j=1}^2 \vec{q}_{j}\cdot\beta_{3j})+\cdots+(\delta_{n} \vec{q}_{n}+\sum_{j=1}^{n-1}\vec{q}_{j}\cdot\beta_{nj})$$
$$(\delta_{1})\vec{q}_{1}+(\delta_{2}+\beta_{21})\vec{q}_{2}+(\delta_{3}+\beta_{31}+\beta_{32})\vec{q}_{3}\cdots+(\delta_{n}+\beta_{n1}+\beta_{n2}+\cdots+\beta_{n3})\vec{q}_{n} \in \text{span}\{\mathcal{Q} \}$$

Therefore, $\text{span}\{ \mathcal{P} \} \subseteq \text{span}\{ \mathcal{Q} \}$. Since we have shown that both $\text{span}\{ \mathcal{P} \} \subseteq \text{span}\{ \mathcal{Q} \}$ and $\text{span}\{ \mathcal{Q} \} \subseteq \text{span}\{ \mathcal{P} \}$, it follows that $\text{span}\{ \mathcal{P} \} = \text{span}\{ \mathcal{Q} \}$.

---
# Connection to [[Unitary Matrices]]

If we have $n$ many vectors each of which belong to $\mathbb{R}^n$ in our $\mathcal{Q}$, then it turns out we can put all of our vectors into a matrix, which turns out to be a unitary matrix since each all of its columns are mutually orthogonal, and each vector is [[orthonormal]]:

$$A=\{\vec{q}_{1},\vec{q}_{2},\cdots,\vec{q}_{n} \}$$
If we consider the product of $A\cdot A^T$ we obtain: 
$$AA^T= \begin{bmatrix}\vec{q}_{1} &\vec{q}_{2} & \cdots & \vec{q}_{n} \end{bmatrix} \cdot \begin{bmatrix}\vec{q}_{1}^T \\ \vec{q}_{2}^T \\ \vdots \\ \vec{q}_{n}^T \end{bmatrix}= \begin{bmatrix} \sum_{i=1}^n \vec{q}_{i}\cdot \vec{q}_{1}^T& \sum_{i=1}^n \vec{q}_{i}\cdot \vec{q}_{2}^T& \cdots & \sum_{i=1}^n \vec{q}_{i}\cdot \vec{q}_{n}^T&  \end{bmatrix} $$
Each corresponding $\sum_{i=1}^n \vec{q}_{i} \cdot \vec{q}_{j}^T = \vec{e}_{j}$ since the vectors are mutually orthogonal and equal to the identity vector $\vec{e}_{j}$ when $i=j$. In turn, we get the identity matrix. We can make an equivalent argument for $A^TA$ using outer products, however I will not do this. In turn, we would observe that:

$$A^TA=AA^T=I_{n}$$
Thus, $A$ is a unitary matrix. 

---
# A Brief Note on $A=QR$ [[QR Factorization]]

The Gram-Schmidt process allows us to express a linearly independent basis $\mathcal{P}$ represented by the matrix $P \in \mathbb{R}^{m \times n}$ where $m \geq n$ as a product of an orthogonal set obtained through the Gram-Schmidt process, and an [[upper triangular matrix]] with positive diagonal entries that comes from constants that reverse the Gram-Schmidt process. 

I have elaborated on this in the matrix factorization section, so I will only briefly provide the $QR$ factorization in its full and reduced forms. 

The reduced $QR$ decomposition is expressed as, $\hat{Q} \in \mathbb{R}^{m \times n}, \hat{R} \in \mathbb{R}^{n \times n}$:

$$A=\hat{Q}\hat{R} =  \begin{bmatrix}\vec{q}_{1} &\vec{q}_{2}  & \cdots & \vec{q}_{n} \end{bmatrix}   \begin{bmatrix} \|v_{1} \| & <\vec{v}_{1},\vec{v}_{2}> & <\vec{v}_{1},\vec{v}_{3}> & \cdots & <\vec{v}_{1},\vec{v}_{n}>   \\ 0 & \|v_{2} \| & <\vec{v}_{2},\vec{v_{3}}>&   \cdots & <\vec{v}_{2},\vec{v_{n}}> \\ 0 & 0 & \|v_{3} \|&   \cdots & <\vec{v}_{2},\vec{v_{n}}> \\    \vdots  & \vdots  & \vdots  & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & \| v_{n} \|  \end{bmatrix}$$

We can construct our full $QR$ factorization in the following; 
$$A=QR, \text{ where, } Q=[\hat{Q}|\tilde{Q}] \text{ and } R =  \begin{bmatrix} \hat{R} \\ 0_{(m-n) \times m}\end{bmatrix}$$
Our matrix $Q \in \mathbb{R}^{m \times m}$ and $R \in \mathbb{R}^{m \times n}$.  We obtain our matrix $Q$ by taking $\hat{Q}$ from above and performing an orthogonal complement on it so that we obtain a fully orthogonal matrix. We can do this because we are able to extend any basis such that it completes $\mathbb{R}^{m}$, and this is precisely what we are doing here. We have to be able to delete these new values, so we do this by padding our new $R$ matrix with additional zeroes, which also makes multiplication conformable. 

-- -
# Nested Subspace Property 

During the Gram-Schmidt process, at each iteration we are finding an equivalent basis for the subspace spanned by the first $k$ vectors from $\mathcal{P}$. To clarify this point consider the following:

$$\text{span}\{ \vec{q}_{1} \}=\text{span}\{\vec{p}_{1} \}$$
$$\text{span}\{ \vec{q}_{1},\vec{q}_{2} \}=\text{span}\{\vec{p}_{1},\vec{q}_{2} \}$$
$$\text{span}\{ \vec{q}_{1},\vec{q}_{2},\cdots,\vec{q}_{k} \}=\text{span}\{\vec{p}_{1},\vec{q}_{2}, \cdots, \vec{p}_{k} \}$$
Each basis here gives an orthonormal basis for the first $k$ vectors from $P$. 

---
# [[The Gram-Schmidt Process]] and [[Projection Matrices]]
We can think of each $q_{i}$ column vector in the matrix $Q$ as a projection of a column vector of $A$ onto an [[Orthogonal Projector]]. 
$$q_{1}=\frac{P_{1}a_{1}}{\|P_{1}a_{1}\|},q_{2}=\frac{P_{2}a_{2}}{\|P_{2}a_{2}\|},\cdots, q_{n}=\frac{P_{n}a_{n}}{\|P_{n}a_{n}\|}$$
We can think of the classical Gram-Schmidt Process as a projection onto rank one subspaces of each $q_{i}$ continually. We can sidestep the repeated work with a more numerically stable algorithm known as the [[Modified Gram-Schmidt Process]], which essentially projects onto the subspace orthogonal to the previous $j-1$ spanned vectors, and sets this to our next $q_{j}$ after normalization. 

---
# Further Results 

The orthonormal basis we obtain from the Gram-Schmidt process is not unique. All we have to do is change the order of the vectors we cycle through, and this is enough to change our resulting matrix many times over. 

QR factorization is useful in [[Least Squares]], and allows us to derive an expression to calculate our best fit curves. 

---
# Gram-Schmidt and [[Numerical Stability]]
It is well known that [[The Gram-Schmidt Process]] is numerically unstable, because as we continue computing we lose the property of [[orthogonal]]ity. We can somehow stabilize this using an augmented system of equations. 

We obtain, $R$ and $Q^Hb$ with $Q^Hb$ being implicit. We can then backsolve for $x$ in $Rx=Q^Hb$ using an augmented system. Somehow this is stable? Doesn't really explain it?