---
title: Rank 1 Perturbation
tags:
draft: "false"
---
# Rank 1 Perturbation 
A [[Rank 1 Perturbation]] is the result of taking a matrix $A \in \mathbb{F}^{n \times n}$, and for $u,v\in \mathbb{F}^{n}$ computing the following:
$$A-uv^H$$
If we begin from a simpler point, let $A=I$. We choose $u,v \neq 0$, such that $uv^H$ is a matrix of [[Rank]] 1. We can compute the inverse of this matrix, assuming that it exists as the following form:
$$(I-uv^H)^{-1}=I+\frac{uv^H}{1-v^Hu}$$
We can confirm that this hypothetical inverse is the actual inverse. Let us verify that this is an [[Inverse Matrix]]: 
$$(I-uv^H) (I-uv^H)^{-1}=(I-uv^H) \left[ I+\frac{uv^H}{1-v^Hu} \right]=(I-uv^H)+\frac{uv^H}{1-v^Hu}- \frac{uv^Huv^H}{1-v^Hu}$$
$$=I-\frac{(1-v^Hu)uv^H}{(1-v^Hu)}-\frac{uv^H(1-v^Hu)}{(1-v^Hu)}=I$$
Now we must show:
$$(I-uv^H)^{-1}(I-uv^H)=\left[ I+\frac{uv^H}{1-v^Hu} \right](I-uv^H)=\left[ I+\frac{uv^H}{1-v^Hu} \right]-uv^H- \frac{uv^Huv^H}{1-v^Hu}$$
Notice this is identical to what is already described above at some point during the simplification process, which entails that this expression to is $I$. Also notice that this matrix will only fail at being the inverse if $v^Hu=1$ 

We want to generalize this result to any $u,v \in \mathbb{F}^{n \times k}$, where $\text{rk}(u)=\text{rk}(v)=k$. The resulting product of these matrices $uv^H$ will be of rank $k$ as well. 

From this we obtain a [[Rank k Perturbation]] of a matrix.

We are interested in the inverse of the following matrix: 
$$(I_n-uv^H)^{-1}$$
From the [[Rank 1 Perturbation]] and [[Rank k Perturbation]], we will be able to obtain the [[Sherman-Morrison-Woodbury Formula]]. 

---
# Derivation of the Formula 
We are interested in the more general form of a [[Rank 1 Perturbation]] given by:
$$A-uv^H$$
Suppose that $Aw=b$ is solved for vector $u$. Now, we want to solve the following:
$$(A-uv^H)x=b$$
We want to be able to use $Aw=b$ in order to solve this new perturbed system without needing to go through all of the steps of [[Gaussian Elimination]]. 

We want to solve $Az=u$, and we hope that by solving $z$ we can obtain a solution for $x$. Here we can use  [[Gaussian Elimination]] 

The resulting expression for $x$ turns out to be(Strang doesn't derive this, idk how he got it but):
$$x=w+\frac{wv^Hz}{1-v^Hz}$$
---
# Uses
* 1.)  Perturbations can be used to solve [[system of equations]]. 
* 2.) For some $Ax=b$, we can add a new measurement to an existing system of equations in [[Least Squares]]. 

If $A \in \mathbb{R}^{m \times n}$ where $m \geq n$. Using the [[normal equation]]s for solving [[Least Squares]], then we express some new data matrix for our points. Here is our [[normal equation]]s expression: $$Ax=b \to A^TAx=A^Tb$$
Our new data point can be included as: $$B=\begin{bmatrix} A\\ v^T\end{bmatrix}x =\begin{bmatrix} b\\ \delta\end{bmatrix}$$
Our [[normal equation]]s now can be re-expressed with $B$ by:
$$B^TB\hat{x}=B^Tb$$
$$\begin{bmatrix} A^T& v\end{bmatrix} \begin{bmatrix} A\\ v^T\end{bmatrix} \hat{x}=B^Tb$$
$$(A^TA+vv^T)\hat{x}=B^Tb=A^Tb+v\delta$$
$$(A^TA+vv^T)\hat{x}=A^Tb+v\delta$$
Notice that this is a [[Rank 1 Perturbation]] of our given [[system of equations]]. We want to avoid doing additional computations, and just work with the perturbation and the new point, ideally we want to minimize new computations or re-computations of [[Least Squares]]. 

Speaking only in terms of theory, we can invert the above matrix by using the [[Rank 1 Perturbation]] formula that we just computed. This formulation here is known as [[Recursive Least Squares]].  