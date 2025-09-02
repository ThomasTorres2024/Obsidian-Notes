---
title: Least Squares
tags: 
draft: "false"
---
# Least Squares Introduction

We can use least squares to find the best first curve through a set of points. We can find polynomial curves, different linear planes, and as well functions like like $e^x$ through a set of points assuming that we apply the correct transformations to the data involved. 

In total, we have a method for approximating the curve that minimizes the squared error between a set of observed points, $P=\{(t_{1},y_{1}),(t_{2},y_{2}),\cdots, (t_{n},y_{n}), \}$. We would set up our least squares problem by finding the squared modulus of each point. 

Assuming that we are looking for a linear function that minimizes the distances between our best line, we would be looking for a function $y=t \alpha + \beta$ Our goal would be to find the parameters that minimize the following sum: 

$$\sum_{i=1}^n |t_{i}\alpha+\beta - y_{i}|^2=\sum_{i=1}^n \epsilon_{i}^2$$

We also define the error to be given at each point by $\epsilon_{i}=|t_{i}\alpha+\beta - y_{i}|$ which allows us to write our formula very nicely. 

Since we are trying to minimize many points for several variables, we can reformulate our problem through the lens of a matrix vector product. 

We will have a matrix consisting of our entries in time which would be scaled by $\alpha$ and a column of $1$ where our values of $\beta$ would go. We are multiplying this matrix by the vector consisting of the variables we are looking to solve for, namely $\begin{bmatrix} \alpha & \beta \end{bmatrix}^T$. We then subtract the vector which consists of all entries of observed points, and take the norm of the difference of the two vectors. This is equivalent to find the sum of each $\epsilon_{i}^2$:

$$ \left\|\begin{bmatrix} t_{1} &1 \\ t_{2} & 1\\ t_{3} & 1 \\ \vdots & \vdots \\ t_{n} & 1 \end{bmatrix} \cdot \begin{bmatrix} \alpha \\ \beta \end{bmatrix}  -\begin{bmatrix} y_{1} \\ y_{2} \\ y_{3}  \\ \vdots \\ y_{n}  \end{bmatrix}\right\|^2=\|A\vec{x}-\vec{b} \|^2 = \| \vec{\epsilon} \|^2=\vec{\epsilon}^T\vec{\epsilon}$$

We can express our data matrix as $A$, our vector we are trying to solve for as $\vec{x}$, and the vector of results as $\vec{b}$, and at least we have a succinct and nice way to write our problem for least squares in terms of linear algebra.

We call the error vector $\vec{\epsilon}=A\vec{x}-\vec{b}$.

For general least square problems, $A \in \mathbb{R}^{m \times n}$, where $m \geq n$, and $A$ is a full column [[Rank]] matrix. This is a reasonable assumption since we have a lot of row entries with few columns. It is therefore unlikely that a column will be a linear combination of another, though it is still possible and needs to be accounted for. Our least squares derivation here will take this into account. 

In total, the least squares problem is essentially a minimization of the squared norm of $\vec{e}$. 

---

# Solution via Full QR Decomposition 

Since $A \in \mathbb{R}^{m \times n}$ where $m \geq n$ and $\text{rank}(A)=r$, $A$ has a [[QR Factorization]]. We can use the full $QR$ decomposition here. This allows us to express $A=QR$ where $Q \in \mathbb{R}^{m \times m}$ and is [[orthogonal matrix]], and $R \in \mathbb{R}^{m \times n}$ is an "[[upper triangular]]" block matrix:

$$R=[\hat{R}^T|0_{m \times (m-n)}]^T$$

Where $\hat{R} \in \mathbb{R}^{n \times n}$ is a [[non singular]] upper triangular matrix with $n$ positive diagonal entries. 

Our answer to least squares here relies on the fact that the [[norm]] of a vector multiplied by an orthogonal matrix is the norm of the vector itself. To illustrate this fact, consider $\vec{b} \in \mathbb{R}^{m \times m}$. 

$$\| Q \vec{b} \|^2=(Q\vec{b})^T(Q\vec{b}) =\vec{b}^TQ^T \cdot Q\vec{b}=\vec{b}^T\vec{b}=\| \vec{b} \|^2$$
$$\|Q\vec{b} \|^2 = \| \vec{b} \|^2 \Longleftrightarrow \|Q\vec{b} \| = \| \vec{b} \|$$

We also know that $Q^T$ is another orthogonal matrix. In our formulation of the least squares problem, we are trying to minimize the squared norm of the error vector. Since multiplication of this vector by an orthogonal matrix will not change the norm of $\epsilon$, an equivalent problem would be to find $\vec{\epsilon}$ that minimizes  $\|Q^T\vec{\epsilon}\|$

$$\| \vec{\epsilon} \|^2=\|Q^T \vec{\epsilon} \|^2=\|Q^T(A\vec{x}-\vec{b}) \|^2=\|Q^T(QR\vec{x}-\vec{b}) \|^2=\|R\vec{x}-Q^T\vec{b} \|^2$$

For the sake of convenience let $\vec{c} = Q^T\vec{b}$. We will also take advantage of the fact that $R$ is a block matrix and split it up accordingly. We also need to divide $\vec{c}$ such that $\vec{c}=[\hat{c}^T|\hat{d}^T]^T$ where $\hat{c} \in \mathbb{R}^{n}$ and $\hat{d} \in \mathbb{R}^{m-n}$. 

$$=\|R\vec{x}-\vec{c} \|^2= \left\|\dfrac{\hat{R}\vec{x}-\hat{c}}{0_{(m-n)\times n}\vec{x}-\hat{d}} \right\|^2=\left\|\dfrac{\hat{R}\vec{x}-\vec{c}}{\hat{d}} \right\|^2=\|\hat{R}\vec{x}-\hat{c} \|^2+\| \hat{d}\|^2$$
Since $\| \hat{d} \|^2$ is a constant, we can ignore it, and just focus on minimizing $\| \hat{R}\vec{x}-\hat{c} \|^2$, since it does not depend on the constant. The best possible guess that we could give for the curve would have the error term of $\|\hat{d}\|^2$ as well. 

However, recall that $\hat{c} \in \mathbb{R}^n$ and that also $\hat{R}\in \mathbb{R}^{n \times n}$ and has a full column rank since it has $n$ many pivots. Thus, the $\vec{x}$ we have been looking for is the solution to$\hat{R}\vec{x}=\hat{c}$ which is:

$$\vec{x}=\hat{R}^{-1}\hat{c}$$

---

# Solution via Normal Equations 

Recall that for any $A \in \mathbb{R}^{m \times n}$ where $m \geq n$ and the columns of $A$ are [[linearly independent]], that: $$\mathbb{R}^m = \mathcal{R}(A) \oplus \mathcal{N}(A^T)$$ Any vector $\vec{b} \in \mathbb{R}^m$ can be uniquely expressed as a [[linear combination]] of a vector from $\mathcal{R}(A)$ and $\mathcal{N}(A^T)$. Therefore, we can express $$\vec{b} = \vec{b}_{\mathcal{R}} + \vec{b}_{\mathcal{N}}$$
Therefore, by minimizing our error vector's squared norm, we can re-write it as the following: 

$$\vec{\epsilon}=A\vec{x}-\vec{b} = A\vec{x}-\vec{b}_{\mathcal{R}}-\vec{b}_{\mathcal{N}}$$
Since $\vec{b}_{\mathcal{R}} \in \mathcal{R}(A)$, we can find an $\vec{x}$ that is equivalent to $\vec{b}_{\mathcal{R}}$. If we were to do so this would leave the quantity $-\vec{b}_{\mathcal{N}}$. This is the best we could do when minimizing the square of the error:

$$\| \vec{\epsilon} \| ^2= \| A\vec{x}-\vec{b} \|^2 = \| A\vec{x}-\vec{b}_{\mathcal{R}}-\vec{b}_{\mathcal{N}}\|^2=\| -\vec{b}_{\mathcal{N}}  \|^2$$

We can multiply both sides of $A\vec{x}-\vec{b}=-\vec{b}_{\mathcal{N}}$ by $A^T$ to obtain a so called [[normal equation]]. Since $\vec{b}_{\mathcal{N}} \in \mathcal{N}(A^T)$, it follows that $A^T \cdot \vec{b}_{\mathcal{N}} = \vec{0}$:

$$A\vec{x}-\vec{b}=-\vec{b}_{\mathcal{N}}$$
$$A^T(A\vec{x}-\vec{b})=-A^T(\vec{b}_{\mathcal{N}})$$
$$A^T(A\vec{x}-\vec{b})=\vec{0}$$
$$A^TA\vec{x}-A^T\vec{b}=\vec{0}$$
$$A^TA\vec{x}=A^T\vec{b}$$
The last step is our resulting normal equation. Note that $A^TA \in \mathbb{R}^{n \times n}$ and that it is symmetric. We can show that it is invertible by showing that $\text{ker}(A^TA)=\text{ker}(A)=\{ \vec{0} \}$. 

We can see that $\mathcal{N}(A) \subseteq \mathcal{N}(A^TA)$ by observing that for $\vec{x} \in \mathcal{N}(A)$:

$$A\vec{x}=\vec{0}$$
$$A^T\cdot A\vec{x} = \vec{0}$$
Which implies $x\in \mathcal{N}(A^TA)$. 

Similarly, we can see that $\mathcal{N}(A) \supseteq \mathcal{N}(A^TA)$ by considering the following for $x \in \mathcal{N}(A^TA)$:
$$A^TA\vec{x}=\vec{0}$$
$$\vec{x}^T\cdot A^TA\vec{x}=\vec{x}^T \cdot \vec{0}$$
$$ = \|A\vec{x} \|^2 = 0$$
Which only occurs when $\vec{x}=0$ since $\mathcal{N}(A)=\{ \vec{0} \}$. So, $\vec{x} \in \mathcal{N}(A^TA) \implies \vec{x} \in \mathcal{N}(A)$.

It follows that $\mathcal{N}(A^TA)=\mathcal{N}(A)=\{ 0 \}$. Since the kernel consists only of the zero vector, we are guaranteed to have an invertible matrix, $A^TA$. We can directly solve for $\vec{x}$ in our normal equation.
$$\vec{x}=(A^TA)^{-1}A\vec{b}$$
This is also known as the [[Moore-Penrose Pseudo Inverse]], as it is able to invert items from the range back to their domain, but not items in the null space. 

---
# Curve Fitting for Higher Degree Polynomials 

For polynomials higher than degree $1$, we include the powers of $t$ from 1 to the power of the polynomial. For example, if we were to minimize the degree for a degree 3 polynomial we would need to solve for the four variables below: 

$$ \left\|\begin{bmatrix} t_{1}^3 & t_{1}^2 & t_{1} &1 \\ t_{2}^3 & t_{2}^2 & t_{2} & 1\\ t_{3}^3 & t_{3}^2 & t_{3} & 1 \\ \vdots & \vdots & \vdots & \vdots \\ t_{n}^3 & t_{n}^2 & t_{n} & 1 \end{bmatrix} \cdot \begin{bmatrix} \alpha_{3} \\ \alpha_{2} \\\alpha_{1} \\ \beta \end{bmatrix}  -\begin{bmatrix} y_{1} \\ y_{2} \\ y_{3}  \\ \vdots \\ y_{n}  \end{bmatrix}\right\|^2=\|A\vec{x}-\vec{b} \|^2 = \| \vec{\epsilon} \|^2=\vec{\epsilon}^T\vec{\epsilon}$$
$$p_{3}(t)=\alpha_{3}t^3+a_{2}t^{2}+\alpha_{1}t+\beta$$

In the case of an $n$ degree polynomial, we have

$$ \left\|\begin{bmatrix} t_{1}^n & \cdots & t_{1}^3 & t_{1}^2 & t_{1} &1 \\ t_{2}^n & \cdots & t_{2}^3 &  t_{2}^2 & t_{2} & 1\\ t_{3}^n & \cdots & t_{3}^3 & t_{3}^2 & t_{3} & 1 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ t_{n}^n & \cdots &t_{n}^3 & t_{n}^2 & t_{n} & 1 \end{bmatrix} \cdot \begin{bmatrix} \alpha_{3} \\ \alpha_{2} \\\alpha_{1} \\ \beta \end{bmatrix}  -\begin{bmatrix} y_{1} \\ y_{2} \\ y_{3}  \\ \vdots \\ y_{n}  \end{bmatrix}\right\|^2=\|A\vec{x}-\vec{b} \|^2 = \| \vec{\epsilon} \|^2=\vec{\epsilon}^T\vec{\epsilon}$$
$$p_{n}(t)=\alpha_{n}t^n+a_{n-1}t^{n-1}+\cdots+\alpha_{2}t^2+\alpha_{1}t+\beta$$