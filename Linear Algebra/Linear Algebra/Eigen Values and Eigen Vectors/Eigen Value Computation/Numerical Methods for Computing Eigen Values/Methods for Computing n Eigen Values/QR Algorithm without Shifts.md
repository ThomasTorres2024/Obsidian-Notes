---
title: QR Algorithm Without Shifts
tags:
draft: "False"
---
# Introduction
The QR algorithm without shifts makes use of the [[QR Factorization]] at each step to eventually give us the eigen values/vectors in 1 shot of a matrix, $A$, which satisfies (for the purpose of explanation here) $A=A^T$ and $A\in \mathbb{R}^{m \times m}$. We can describe the pure algorithm in the following:

The pure QR algorithm goes like the following. We begin with a matrix we want to iterate over, $A$, and perform the following operations, where we let each $A^{(k)}$ be the $k$th iterate of $A$.  
* $A^{(0)}$= A
* for $k=1,2,\cdots$
	* $Q^{(k)}R^{(k)}=A^{(k-1)}$ 
	* $A^{(k)}=R^{(k)}Q^{(k)}$ 
At each step, we are computing a [[QR Factorization]] of the $k$th iterate of $A$, and then we are computing a new $k$th iterate by performing a similarity transformation. Notice that the [[similarity transformation]] is obtained by doing: 
$$Q^{(k)}R^{(k)}=A^{(k)}$$
$$R^{(k)}=Q^{(k)^T} A^{(k)} \iff R^{(k)}Q^{(k)}=Q^{(k)^T} A^{(k)}Q^{(k)} = A^{(k+1)} $$
As such, we obtain a new iterate (I initially had some trouble understanding that this is not the $k$th power). Under certain conditions, our factorization of the $k$th iterate actually turns into a [[Schur's Triangularization]] of the matrix $A$, and if $A$ is [[Hermitian]], then the resulting matrix actually is of diagonal form. This [[similarity transformation]] here is the same transformation taken originally when we were trying to compute a factorization that had us instead use the [[Upper Hessenberg Matrix]] form of $A$ to properly obtain its eigen values and do a similarity transformation of it. 

---
# Connection to [[Simultaneous Iteration]]
[[Simultaneous Iteration]] is a simple algorithm that applied to several vectors, $V \in \mathbb{R}^{m \times n}$, where each $v_{i} \in V$ is [[linearly independent]]. From [[Power Iteration]], it is known that $A^kv_{1}^{(0)}$ is known to converge to $q_{1}$, which is to say the first eigenvector of $A$. We can make some additional assumptions and changes to our algorithm though, such that the following space converges to the [[Eigenspace]] of $A$, which is to say:
$$\left \langle A^{(k)}v_{1}^{(0)},\langle A^{(k)}v_{2}^{(0)}, \cdots, \langle A^{(k)}v_{n}^{(0)} \right \rangle \to \langle q_{1},q_{2},\cdots q_{n} \rangle  $$
For this part, we will define the initial matrix and $k$th iterate matrix $V$ by: 
$$V^{(0)}=\begin{bmatrix} v_{1}^{(0)} \cdots v_{n}^{(0)} \end{bmatrix}$$
and 
$$V^{(k)}= A^{k}V^{(0)}=\begin{bmatrix} v_{1}^{(k)} \cdots v_{n}^{(k)} \end{bmatrix}$$
Define an orthogonal basis for the column space of $V^{(k)}$, using [[Reduced QR]] factorization:
$$\hat{Q}^{(k)}\hat{R}^{(k)}=V^{(k)}$$
Here, we make the assumptions that the leading $1.) k+1$ eigen values are distinct, and also that the leading principal submatrices of $\hat{Q}^TV^{(0)}$ are nonsingular. It then follows that the columns of the matrix $\hat{Q}^{(k)}$ converge to the [[eigen vectors]] of $A$.  

The matrices, $V^{(k)}=A^kV^{(0)}$ are very [[ill-conditioned]], so at each step we need to orthonormalize instead of just at the very end. 
![[Pasted image 20251102153907.png]]
It is also the case that the column spaces of $\hat{Q}^{(k)}$ and $Z^{(k)}$ are both equal to the column space of $A^k\hat{Q}^{(0)}$, so it follows that the same convergence to the matrix of eigen vectors of $A$ occurs. 

Notice also that the [[Simultaneous Iteration]] algorithm is equivalent to the [[QR Algorithm without Shifts]], except one is done when $Q^{(0)}=I$.  