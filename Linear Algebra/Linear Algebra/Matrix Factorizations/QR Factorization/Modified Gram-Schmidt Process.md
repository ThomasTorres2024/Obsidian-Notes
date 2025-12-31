---
title: Modified Gram-Schmidt Process
---
# Modified Gram-Schmidt Process
The modified [[The Gram-Schmidt Process]], is a process which takes of a set $n$ linearly independent vectors and finds and a basis which spans the same set such that the new basis is orthogonal. [[The Gram-Schmidt Process]] is [[numerically unstable]], so we have to make some changes to it in order for it to not break early on. 

[[The Gram-Schmidt Process]] uses rank 1 projectors at each iteration to force orthogonality, but the [[Modified Gram-Schmidt Process]] take $j-1$ projections of rank $m-1$. Note that $P_{\perp q}$ is the projector onto the null space of $q$.  

We can form the $j$th projector by taking of the first $j-1$ projectors and taking their product. Instead of continually projecting onto rank 1 subspaces, we compute the next $v_{j}$ by taking a product with new projector matrices.

---
# [[Projection Matrices]] and the [[Modified Gram-Schmidt Process]]
We can think of each $q_{i}$ column vector in the matrix $Q$ as a projection of a column vector of $A$ onto an [[Orthogonal Projector]]. 
$$q_{1}=\frac{P_{1}a_{1}}{\|P_{1}a_{1}\|},q_{2}=\frac{P_{2}a_{2}}{\|P_{2}a_{2}\|},\cdots, q_{n}=\frac{P_{n}a_{n}}{\|P_{n}a_{n}\|}$$
We denote the $j$th projection matrix, $P_{j} \in \mathbb{C}^{m \times m}$, as a projection of $\mathbb{C}^{m}$ onto the space orthogonal to the first $j-1$. vectors. When we carry out [[The Gram-Schmidt Process]], we are essentially trying to extract the component of $a_{j}$ which does not lie in the part spanned by the previous subspace $\langle q_{1},q_{2},\cdots,q_{j-1},\rangle$. We continue repeating this process until we have exhausted all column vectors of $A$. 

The $j$th projection matrix is of rank $m-(j-1)$. The last should be of dimension 1, since we only have 1 more dimension to span before fully describing all of $\mathbb{C}^m$. We begin with $I_{m}$ as our matrix, since we have described nothing so far, and extract the vector raw, which is line with how we just take the first vector and normalize it with respect to the normal process and its interpretation. 

We can represent $P_{j}$ explicitly by considering the first $j-1$ columns. We can construct a matrix with orthonormal columns, $\hat{Q}_{j-1} \in \mathbb{C}^{m \times (j-1)}$. We can obtain $P_{j-1}$ by first considering a projection onto the space:
$$\hat{Q}_{j-1}\hat{Q}_{j-1}^H$$
We can then determine an [[Orthogonal Projector]] to that space by:
$$P_{j}=I_{m}-\hat{Q}_{j-1}\hat{Q}_{j-1}^H$$
By the definition of $P_{j}$ we have that:
$$P_{j}=P_{\perp}q_{j-1}\cdots P_{\perp}q_{2}P_{\perp}q_{1}$$
$$v_{j}=P_{\perp}q_{j-1}\cdots P_{\perp}q_{2}P_{\perp}q_{1}a_{j}$$
---
# Computing Subsequent Projection Matrices
We can determine the projection matrices used to project the column vectors of $A$ down onto lower subspaces by considering the part of the column vector orthogonal to   the $j-1$th space spanned by the first $j-1$ vectors of $Q_{j-1}$. 

$$v_{j}^{(1) }=a_{j}$$
$$v_{j}^{(2) }=P_{\perp}q_{1}v_{j}^{(1)}=v_{j}^{(1)}-q_{1}q_{1}^Hv_{j}^{(1)}$$
$$v_{j}^{(3) }=P_{\perp}q_{2}v_{j}^{(2)}=v_{j}^{(2)}-q_{2}q_{2}^Hv_{j}^{(2)}$$
Thus for a general form of each $v_{j}$:
$$v_{j}=v_{j}^{j}=P_{\perp}q_{j-1}v_{j}^{(j-1)}=v_{j}^{(j-1)}-q_{j-1}q_{j-1}^Hv_{j}^{(j-1)}$$
This method is still [[numerically unstable]], but has a better [[Numerical Stability]] than [[The Gram-Schmidt Process]]. 

---
# [[Modified Gram-Schmidt Process]] Algorithm:

$\text{for } i=1 \text{ to } n$                                
$\text{\quad \quad} v_{1}=a_{1}$
$\text{for } i=1 \text{ to } n$
$\text{\quad \quad} r_{ii}=\|v_{i} \|$
$\text{\quad \quad} q_{i}=v_{i}/r_{ii}$
$\text{\quad \quad \quad for } j=i+1 \text{ to } n$
$\text{\quad \quad \quad \quad } r_{ij}=q_{i}^Hv_{j}$
$\text{\quad \quad \quad \quad } v_{j}=v_{j}-r_{ij}q_{i}$


# Practicality 
[[The Gram-Schmidt Process]] and [[Modified Gram-Schmidt Process]] are generally not used in the real world for normal [[orthogonal]]ization tasks, but for [[Krylov Methods]] we make use of these ideas. 
