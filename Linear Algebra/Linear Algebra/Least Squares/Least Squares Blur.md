---
title: Least Squares Blur
tags:
draft: "False"
---
# Introduction to Least Squares Blur
If we have a one dimensional signal, $u \in \mathbb{R}^{200}$, we are interested in seeing what happens if the signal is "blurred", and what we may be able to do to subsequently unblur it.

One way of blurring a vector is by considering the matrix, $T$ known as the Toeplitz matrix where each $T_{jk}=c \cdot \exp\left( -\frac{1}{10}(j-k)^2 \right)$ and $T$ is a symmetric matrix where $1 \leq j, k\leq 200$. 

We can get $v=Tu$, where $v$ is the blurred signal. We want to be able to take any arbitrary blurred signal $v$, and apply some operation to obtain $u$ on the vector $v$. 

We also have to deal with noise, $e$, which then results in the vector:
$$w=v+e$$
No longer do we have a blurred signal, we have a noisy blurred signal. The noise may be Gaussian. We can find $\hat{u}$ if we cannot find $u$ to solve the following system when we have noise and blur but still want something for $\hat{u}$:
$$T\hat{u}=w $$
So we can determine $\hat{u}$ via matlab backslash:
$$\hat{u}=T\text{ \\ } w$$
This restoration given is a [[Least Squares]] problem, and it fully minimizes $\|w-T\hat{u}\|_{2}$, but we run into some issues here. For one, we ignore the noise in $w$, and get possible rounding errors in computation. We in turn solve a system of equations with a wrong righthand side using the backslash operator.

$T$ has small singular values eventually, so $T$ is [[Ill-Conditioned]]. 

We can determine the influence of the error vector on $u$ by seeing that:
$$T\hat{u}=w=v+e$$
$$T\hat{u}-v=T\hat{u}-Tu=e$$
Notice that:
$$\hat{u}-u=T^{-1}e$$
So:
$$\|\hat{u}-u\|=\|T^{-1}e \|\leq \|T^{-1}\|\cdot \|e\|$$
We also have that $\|e\|=10^{-3} \|u\|$ so we obtain that $\|u\|^1.375$ 
We know that $\|T^{-1}\|=\frac{1}{\sigma_{200}}\cdot 10^{-3}\|u\|=3\cdot 10^7$. Basically the point of this is to say that the minimized solution can be completely useless and doesn't really help us out.

---
# Solving with [[Single Value Decomposition]]
Consider the SVD of $T$:
$$T=U\Sigma V^T, 1 \leq k \leq 200, T_{k}=U\Sigma_{k}V^T$$
We want to determine an approximation of the noise free signal $u$ by solving the least squares problem for some $k$ of:
$$\min_{x \in \mathbb{R}^{200}} \|T_{k}x-w\|^2=\min_{x \in \mathbb{R}^{200}} \|U\Sigma_{k}V^Tx-w\|^2=\min_{x \in \mathbb{R}^{200}} \|\Sigma_{k}y-\hat{w}\|^2$$
Where $\hat{w}=U^Tw$:
$$\min_{x \in \mathbb{R}^{200}} \|\Sigma_{k}x-w\|^2 = \min_{x \in \mathbb{R}^{200}}  \sum_{j=1}^k(\sigma_{j}y_{j}-\hat{w}_{j})^2+\sum_{j=k+1}^{200} \hat{w}_{j}^2$$
Where each $y_{j}=\frac{\hat{w}_{j}}{\sigma_{j}}, 1 \leq j \leq k$, and $x_{k}=Vy_{k}$. Each vector $x_{k}$ is an approximation of the undiluted signal $u$. 

---
# The [[L-Curve]]
The [[L-Curve]] is an important result in applied math. We plot the norm of the residual and the norm of x as a function of $k$ as $k$ goes from $1$ to $200$. 
![[Pasted image 20251015011907.png]]

We can find our optimal solution by looking at the graph of $\|x_{k}\|^2$ by $\|Tx_{k}-w\|^2$ for different values of $k$. 
![[Pasted image 20251015012238.png]]

Here we would select the black point because we have some kind of like inflection point, we don't gain anymore substantial change in the output compared to the initial part of the graph, and we can call it a good approximation for $x$. 