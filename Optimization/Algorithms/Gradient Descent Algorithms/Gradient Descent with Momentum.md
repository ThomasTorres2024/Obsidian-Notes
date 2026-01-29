---
title: Gradient Descent with Momentum
draft: "false"
tags:
---
# Gradient Descent with Momentum Description
The aim of [[Gradient Descent with Momentum]] is to create a [[Optimization/Algorithms/Gradient Descent Algorithms/Gradient Descent]] method which remembers which directions we have previously moved in. Our formula for [[Gradient Descent with Momentum]] is described using a decay term. Our previous ratio of convergence is given is a modification in the form:
$$\left(\frac{1-b}{1+b}\right)^{2}\to \left(\frac{1-\sqrt{b}}{1+\sqrt{b}}\right)$$
Here, even if $b$ is small, it should be the case that
$$\left(\frac{1-b}{1+b}\right)^{2} > \left(\frac{1-\sqrt{b}}{1+\sqrt{b}}\right)$$
Which implies convergence happens much quicker. Our formula for the stochastic gradient formula is as follows:
$$\textcolor{Periwinkle}{\boxed{x_{k+1}=x_{k}-sz_{k},z_{k} =\nabla f_{k}+\beta z_{k-1}}}$$ Unlike in the original formulation, we have that $z_{k}=\nabla f_{k} + \beta z_{k-1}$, which is the gradient plus the previous direction that we moved in. It isn't just the [[Gradient]], it is a modification of it.  We can say that we have moved beyond a move of 2 steps of memory, to one of 3 steps. We can think of this like a second order differential equation that has a dampening term. We want to be able to express our equation here as a system of equations. Both of these are obtained by reordering the equations:
$$x_{k+1}=x_{k}-sz_{k}$$
$$z_{k+1}-\nabla f_{k+1}=\beta z_{k}$$
We are still using the same function as in the original [[Optimization/Algorithms/Gradient Descent Algorithms/Gradient Descent]] problem, so:
$$f(x)=\frac{1}{2}x^{T}Sx\implies \nabla f =Sx$$
We can re-write our [[Gradient Descent with Momentum]] equations to be:
$$x_{k+1}=x_{k}-sz_{k}$$$$z_{k+1}-Sx_{k+1}=\beta z_{k}$$
We can describe this as a matrix equation now:
$$x_{k+1}-x_{k}=-sz_{k}$$$$z_{k+1}-Sx_{k+1}=\beta z_{k}$$$$\begin{pmatrix}1 & 0\\ S & 1\end{pmatrix} \begin{pmatrix} x \\ z \end{pmatrix}_{k+1}=\begin{pmatrix}1 & -S\\ 0 & \beta \end{pmatrix} \begin{pmatrix}x\\z\end{pmatrix}_{k}$$
We can simplify this result using the [[Eigen Vectors]] of $S$, since $S$ is [[Symmetric Matrix]] by [[Spectral Theorem Definition and Proof]] we know that $S=X\Lambda X^{T}\implies Sq=\lambda q$ for a full set of [[Eigen Vectors]]. For this problem let:
$$x_{k}=c_{k}q$$
$$z_{k}=d_{k}q$$
Which is to say we assume that the $x$ and $z$ are scalar multiples of [[Eigen Vectors]] of $S$. We also have that:
$$Sx_{k}=c_{k}\lambda k=\nabla f_{k}$$

We can re-write our formula as:
$$\begin{pmatrix}1 & 0\\ -\lambda & 1\end{pmatrix} \begin{pmatrix} c_{k+1} \\ d_{k+1}\end{pmatrix}=\begin{pmatrix} 1 & -s\\0 & \beta\end{pmatrix} \begin{pmatrix} c_{k}\\d_{k} \end{pmatrix}$$
We can re-write our equation using the inverse of the left hand side matrix:
$$\begin{pmatrix} c_{k+1} \\ d_{k+1}\end{pmatrix}= \begin{pmatrix}1 & 0\\ \lambda & 1\end{pmatrix} \begin{pmatrix} 1 & -s\\0 & \beta\end{pmatrix} \begin{pmatrix} c_{k}\\d_{k} \end{pmatrix} \implies$$
$$\begin{pmatrix} c_{k+1} \\ d_{k+1}\end{pmatrix}= \begin{pmatrix}1 & -s\\ \lambda & \beta-\lambda s\end{pmatrix}\begin{pmatrix} c_{k}\\d_{k} \end{pmatrix}=R\begin{pmatrix} c_{k}\\d_{k} \end{pmatrix}$$
We want to choose an $s$ and a $\beta$ such that we make $R$ as "small as possible". We know that the [[eigen values]] of $S$ (which is also [[Positive Definite Matrix]]) lie between:
$$0<m \leq \lambda \leq M$$
The [[Condition Number]] of our matrix is given by:
$$\kappa =\frac{M}{m}$$
The larger, $\kappa$, the harder the problem is to solve. If it turns out that $\kappa=1 \implies S = \lambda \cdot I_{n}$ For instance, if:
$$\kappa = \frac{1}{b}\gg 1$$ Means that the problem will be a lot harder to solve if $b$ is very large. Performance of the algorithm is heavily based around this fact. We can start by determining the eigen values of the matrix, $R$. 

We want the eigen-values of $R$. Thus, we are looking to minimize the following:
$$\min(\max(\lambda_{1},\lambda_{2}))$$
It turns out that the quantities $S$ and $\beta$ that optimize our eigen values are:
$$S_{\text{optimized}}=\left( \frac{2}{\sqrt{\lambda_{Max}}+\sqrt{\lambda_{Min}+}} \right)^2$$
$$\beta_{\text{optimized}}=\left( \frac{\sqrt{\lambda_{Max}}-\sqrt{\lambda_{Min}+}}{\sqrt{\lambda_{Max}}+\sqrt{\lambda_{Min}+}} \right)^2$$
It turns out that these values actually optimize the $2 \times 2$ case. 