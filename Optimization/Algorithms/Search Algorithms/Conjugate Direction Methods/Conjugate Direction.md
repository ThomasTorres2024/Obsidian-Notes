---
title: Conjugate Direction
tags:
  - Optimization
draft: "False"
---
# Conjugate Direction 
A set of vectors, $\vec{d}_{1},\vec{d}_{2},\dots,\vec{d}_{n}$ is said to be $Q$ conjugate for a symmetric [[Positive Definite Matrix]], $Q$, we have that:
$$d_{i}^TQd_{j} = 0 : i\neq j$$

---
# [[Conjugate Direction]]s are [[Linearly Independent]]
$Proof.$ Let $a_{i} \in \mathbb{R}$, and let $\vec{d}_{i} \in \mathbb{R}^n$ be a set of $Q$ conjugate vectors. Then:
$$\alpha_{0}d_{0}+\alpha_{1}d_{1}+\dots+\alpha_{n}d_{n} = 0 \iff \sum_{i=0}^n \alpha_{i}d_{i}=0$$
If we now consider left multiplication by $d_{j}^TQ$ we obtain that:
$$d_{j}^TQ\sum_{i=0}^n\alpha_{i}d_{i}=\sum_{i=0}^n \alpha_{i} (d_{j}^TQd_{i})=\alpha_{j}(d_{j}^TQd_{j}) =0$$
$$\iff a_{j} = \frac{0}{d_{j}^TQd_{j}}=0$$
And thus $\alpha_{j}=0$, which applies for each direction, and thus we have that the only solution for the null vector is if every $\alpha$ is 0. The last step is justified due to the definition of a positive definite Matrix. 

---
### Example 
Let:
$$Q=\begin{bmatrix}
3 & 0 & 1  \\
0 & 4 & 2 \\
1 & 2 & 3
\end{bmatrix}$$
And note that $Q=Q^T$ as well as $\det(Q_{1})>0,\det(Q_{2})>0,\det(Q)>0 \implies Q$ is symmetric positive definite. We can construct a set of $Q$ conjugate vectors with respect to $Q$ if we are able to take a set of linearly independent vectors and convert them to a set of $Q$ conjugate vectors. 

For instance here, consider the case when $d^{(0)}=[1,0,0]^T$ and we are trying to solve for $d^{(1)}$:
$$[1,0,0]Q \begin{bmatrix}
d_{1}^{(1)}\\d_{2}^{(2)}\\d_{3}^{(3)}
\end{bmatrix} = 3d_{1}^{(1)}+d_{3}^{(1)}$$
If we let $d_{1}^{(1)}=1$ and $d_{3}^{(1)}=-3$ and $d_{2}^{(2)}=0$, then we obtain that $d^{(1)}$ and $d^{(0)}$ are $Q$ conjugate vectors. 

For $d^{(2)}$ it must be the case that $d^{(2)}$ is $Q$ conjugate to both $d^{(1)}$ and $d^{(0)}$, and so we obtain the following system of equations to solve for the coefficients of $d^{(2)}$:
$$d^{(0)^T}Qd^{(2)}=3d_{1}^{(2)}+d_{3}^{(2)}$$
$$d^{(1)^T}Qd^{(2)}=-6d_{2}^{(2)}-8d_{3}^{(2)}$$
We can use elementary methods from Linear Algebra to solve this system of equations above. If we let $d^{(2)}=[1,4,-3]^T$, then it follows that $d^{(2)}$ is $Q$ conjugate to $d^{(1)}$ and $d^{(0)}$. 

This manner of obtaining $Q$ conjugate vectors can be systematized using [[The Gram-Schmidt Process]]. 

---
# $Q$ Conjugate Directions With the [[The Gram-Schmidt Process]] 
Given a set of [[Linearly Independent]] vectors, $p_{0},p_{1},\dots, p_{n}$, we can use [[The Gram-Schmidt Process]] in order to derive a set of $Q$ conjugate vectors by using the following algorithm. 
$$d_{0}=p_{0}$$
$$d_{k+1}=p_{k+1}-\sum_{i=0}^k \frac{p^{(k+1)^T}Qd^{(i)}}{d^{(i)^T}Qd^{(i)}}$$
