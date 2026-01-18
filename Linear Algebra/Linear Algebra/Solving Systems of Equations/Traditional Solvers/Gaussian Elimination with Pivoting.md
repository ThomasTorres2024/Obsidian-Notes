---
title: Gaussian Elimination with Pivoting
tags:
draft: "False"
---
# Gaussian Elimination with Pivoting
Pivoting is a modification of the [[Gaussian Elimination]] algorithm which makes [[Gaussian Elimination]] a numerically stable algorithm. 

Gaussian elimination takes $m$ many steps, that is $m$ many left multiplications by [[Elementary Matrix]]. At each step we work on the $k$th diagonal of matrix $A$, $A_{kk}$. This entry, $A_{kk}$ is the "pivot". We modify entries in the sub matrix hoping to annihilate all zeros underneath $A_{kk}$ by modifying $A_{k+1:m,k:m}$. 

There is no particular reason to choose $kk$ however for our pivot. We could choose some other pivot, $A_{ik}$ for $i$ where $k \leq i \leq m$.  $$\begin{bmatrix}
\times & \times & \times & \times & \times \\
 & \times & \times & \times & \times \\
 & \times & \times & \times & \times \\
 & x_{ik} & \times & \times & \times \\
 & \times & \times & \times & \times
\end{bmatrix}
\;\longrightarrow\;
\begin{bmatrix}
\times & \times & \times & \times & \times \\
      & 0 & \times & \times & \times \\
      & 0 & \times & \times & \times \\
 & x_{ik} & \times & \times & \times \\
      & 0 & \times & \times & \times
\end{bmatrix}.$$
We can also go for a different column, not necessarily the $k$th:
We can arbitrarily select any entry of $A_{k:m,k:m}$ to be the pivot, as long as this entry is $\neq 0$. For concerns of [[Numerical Stability]], we try to find a large element to ensure numerical stability. 

Making the choice of any random elimination at step $k$ results in a non-triangular matrix, however we want to retain the [[Upper Triangular Matrix]] during elimination. We handle our choice of moving a pivot into another position by using a [[Permutation Matrix]]. This change of rows and columns is known as "Pivoting". If we actually change the physical position of our matrices in memory is another question, as we may just change some pointers around to achieve the same effect. 

This algorithm is called "Complete Pivoting", since every index in the submatrix $A_{k:m,k:m}$ is considered a candidate. 

---
# Partial Pivoting 
The previous algorithm addressed is known as "Complete Pivoting", and has a [[Time Complexity]] of $O(m^3)$ since we look through $O((m-k)^2)$ many entries. A significantly cheaper algorithm is known as "partial pivoting", where we just consider less entries in $A_{k:m,k:m}$. Here we select the largest entry from the remaining columns instead of the whole matrix, which incurs a cost of $O(m-k)$ in total, which thus only results in a [[Time Complexity]] of $O(m^2)$ for the whole algorithm. 

---
# Pivoting as [[Matrix Multiplication]] 
Previously, we obtained an [[LU Factorization]] of $A$, it looked like:
$$A=\prod_{i=1}^{m-1}L_{i}^{-1} U $$
Here, if we make a permutation before each row operation, we would instead see the following formula, where each $P$ is a [[Permutation Matrix]]:
$$A=\left(\prod_{i=1}^{m-1}P_i^{-1}L_{i}^{-1} \right)U $$
---
# $PA=LU$ Factorization
The factorization we computed is not quite an $LU$ factorization of $A$, but it can be manipulated into being one. It turns out that we have computed an [[LU Factorization]] of $PA$. 

In our product for determining $U$, it turns out that we can actually reorder our matrix. Let us consider an example of $A$ being $3 \times 3$, so, our factorization would be:
$$L_3P_3L_2P_2L_1P_1A=U$$Let our $L'$ matrices that we obtain through some pivoting be:
$$L_3^{'}=L_3,L_2^{'}=P_3L_2P_3^{-1},L_1^{'}=P_3P_2L_1P_2^{-1}P_3^{-1}$$
Notice in the following that:
$$L'_3L'_2L'_1P_3P_2P_1=L_3P_3L_2P_2L_1P_1$$
Which notice that we can deal with the following factorization:
$$(L'_{m-1}L'_{m-2}\dots L'_1)(P_{m-1}\dots P_2 P_1)A=U$$
Which thus gives us the following factorization:
$$PA=LU$$
Any matrix $A$ that is square has a partial pivot LU decomposition. We do not actually permute $A$, and then perform partial pivoting on the resulting $PA$, as $P$ is unknown ahead of time. Instead, we follow the following algorithm for performing [[Gaussian Elimination]]:
![[Pasted image 20260118061605.png]]

---
# Complete Pivoting 
In complete pivoting, we change how we select our pivots for [[Numerical Stability]]. We permute the rows on the left, and the columns on the right of some matrix, obtaining some factorization similar to the above $PA=LU$ factorization:
$$PAQ=LU$$
Which we can then similarly work on. 