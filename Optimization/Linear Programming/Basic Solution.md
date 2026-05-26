---
title: Basic Solution
tags:
  - Optimization
draft: "False"
---
# Basic Solutions

We can define a Basic Solution via the following. Consider the [[Linear Programming Standard Form]]: 

$$\text{ min }c^Tx \quad :  Ax=b, x,b>0$$
And we have that, $c,x, \in \mathbb{R}^n$ and $b \in \mathbb{R}^m$. 

Let the [[Rank]] of $A$ be $m$ and let $m < n$. First, let us choose $m$ columns of $A$ which we are interested in (namely the [[Linearly Independent]] columns): 

$$A=[B \quad D]$$

Where $B \in \mathbb{R}^{m \times m}$ and $\text{rk}(B)=m$, and $D \in \mathbb{R}^{m \times (n-m)}$ 

The corresponding $x$ here is of the form $x=[x_B \quad x_D]^T$. Therefore, as $x$ is a solution to the matrix equation $Ax=b$ we would obtain: 

$$Ax=b \implies Bx_{b}+Dx+d=b$$

Here we have that $x_{B}=B^{-1}(b-Dx_{0})$. 

Notice that for $x$ that the following is a valid solution: 

$$x=[x_{B}\quad x_{D}] = [B^{-1}(b-Dx_{D}) \quad \vec{ 0} ] $$ is a solution of $Ax=b$. however, the __basic component__ here is the component which consists entirely of the linear combinations of the columns of $B$, and the columns of $D$ are scaled by $0$. 

The following is a basic solution:

$$x=[x_{B} \quad \vec{ 0} ]^T$$

---
# Feasible Solution 

A __feasible solution__ is a basic solution which the additional constraint that $x\geq 0$. 

If some of the values in $x_{B}$ are zeroes, then we would say that $x_B$ is __degenerated__ and the __basis solution is degenerated__. 

---
# Examples 

### Example.) 
Consider $Ax=b$: 

$$A=\begin{bmatrix}
\vec{a_{1}} & \vec{a_{2}} & \vec{a_{3}} & \vec{a_{4}}   
\end{bmatrix} = \begin{bmatrix}
1 & 1 & -1 & 4\\ 1  & -2 & -1 & 1  
\end{bmatrix}  $$

And we have that $\vec{b}= [8 \quad 2 ]^T.$  Furthermore we have that $\text{rk}(A)=2, B \in \mathbb{R}^{2 \times 2}$. 

In our solution, let $x_{3}=x_{4}=0$, leaving thus $x_1$ and $x_2$ to be solved for. This is one possible choice for linearly independent columns of $A$. 

$$
\left[
\begin{array}{cccc|c}
1 & 1 & -1 & 4 & 8\\ 1  & -2 & -1 & 1 & 2
\end{array}
\right]

\longrightarrow

\left[ \begin{array}{cc|c}
1 & 1 & 8 \\ 1 &  -2 & 2
\end{array} \right] \implies x_{2}=2,x_{1}=6 
$$

There are more possible choices of columns to select from than just the second. We cannot have the first and third since they would be linearly dependent (since $[-1 \quad -1]^T$ is a linear combination )

but we can have the first and last so here, $x_2=x_3=0$ and we look for $x_1$ and $x_4$:
$$
\left[
\begin{array}{cccc|c}
1 & 1 & -1 & 4 & 8\\ 1  & -2 & -1 & 1 & 2
\end{array}
\right]

\longrightarrow

\left[ \begin{array}{cc|c}
1 & 4 & 8 \\ 1 &  1 & 2
\end{array} \right] \implies x_{4}=2,x_{1}=0 
$$

This is a degenerated solution since some of the basic variables are $0$. 

Let $x_1=x_4=0$ then:
$$
\left[
\begin{array}{cccc|c}
1 & 1 & -1 & 4 & 8\\ 1  & -2 & -1 & 1 & 2
\end{array}
\right]

\longrightarrow

\left[ \begin{array}{cc|c}
1 & -1 & 8 \\ -2 &  -1 & 2
\end{array} \right] \implies x_{3}=-6,x_{2}=8 
$$

This solution is not feasible since $x_3=-6$. 

Let $x_1=x_3=0$ then:
$$
\left[
\begin{array}{cccc|c}
1 & 1 & -1 & 4 & 8\\ 1  & -2 & -1 & 1 & 2
\end{array}
\right]

\longrightarrow

\left[ \begin{array}{cc|c}
1 & -1 & 8 \\ -2 &  -1 & 2
\end{array} \right] \implies x_{3}=-6,x_{2}=8 
$$
