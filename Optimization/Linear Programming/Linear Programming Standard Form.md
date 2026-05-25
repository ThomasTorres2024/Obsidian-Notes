---
title: Linear Programming Standard Form
tags:
  - Optimization
draft: "False"
---
# Derivation from General [[Linear Programming]]

A standard objection function in [[Linear Programming]] is of the form: 

$$\text{ min } c^T x , Ax=b$$
Subject to the constraints that $b\geq 0, x\geq 0$ for $x,b \in \mathbb{R}^n$. 

We can consider subcases now of this problem where we want to use different constraints. 

1. 

If we are trying to solve for $\text{ max } c^Tx$, then we switch to using $\text{ min } -c^Tx$

2. 

If we are in the case where $Ax\leq b$ then we make use of "__slack variables__" which we can use to enforce equality. Component wise here, we would have that the above inequality gives: 

$$\sum_{i=1}^n a_{ki}x_{i} \leq b _{k} \implies \left(  \sum_{i=1}^n a_{ki}x_{i}  \right)+y_{k}=b_{k}$$
Where our chosen $y_k \in \mathbb{R}^+$. This gives the following form for our optimization problem if we apply this for each $k$ where $1 \leq k \leq n$. 

$$\begin{bmatrix}
A & I 
 \end{bmatrix} \cdot \begin{bmatrix}
x \\ y
\end{bmatrix} = Ax+y =b$$

3. 

Similarly for $Ax\geq b$ we can use __surplus variables__:

$$\sum_{i=1}^n a_{ki}x_{i} \leq b_{k } \implies  \left( \sum_{i=1}^n a_{ki}x_{i} \right) + y_{k} = b_{k} $$

Here each $y_k$ is a scalar where $y_k \in \mathbb{R}^-$.  Again the optimization problem here has the same form: 

$$\begin{bmatrix}
A & I 
 \end{bmatrix} \cdot \begin{bmatrix}
x \\ y
\end{bmatrix} = Ax+y =b$$

4. If $x_i$ is a free variable, one with no restrictions, then, we let $x_i=u-v$ for $u,v \geq 0$, or we let

$$x_{i} = \frac{1}{a_{ii}} \left( b_{i} - \sum_{k=1}^n a_{ki}x_{k} \right) $$

---
# Example 1.)

For instance here, let us consider the following optimization problem and focus on the variable $x_1$: 

$$\begin{cases}
\text{min } x_{1}+3x_{2}+4x_{3} & \text{ st} \\
x_{1}+2x_{2}+x_{3}=5 \\
2x_{1}+3x_{2}+x_{3}=6 \\
x_{2},x_{3} \geq 0
\end{cases}$$

(We have an underdetermined linear system, so necessarily we must have a free variable)

Then we can either set $x_1=u-v$ for some $u,v \geq 0$ or we re-arrange for $x_1$. We can easily do this: 

$$x_{1}=5-2x_{2}-x_{3}$$ 
And therefore our optimization problem becomes: 

$$\begin{cases}
\text{min } x_{2}+3x_{3}+5 & \text{ st} \\
x_{2}+x_{3}=4 \\
x_{2},x_{3} \geq 0
\end{cases}$$
---
# Example 2.) 

$$\begin{cases}
\text{max } x_{2}-x_{1} & \text{ st} \\ \\

3x_{1}-x_{2}=-5 \\
|x_{2}| \leq 2 \\
x_{1} \leq 0
\end{cases}$$

The max is equivalent to finding the min of $x_{1}-x_{2}$. 

$x_2$ has no restrictions and it is free, so let it be described by $x_{2}=u-v$ for $u,v \geq 0$.  

We have the condition now that:

$$|x_{2}|=|u-v| \leq 2 \implies u-v \leq 2 , v-u \leq 2 $$

Thus using slack variables $y_1,y_2 \geq 0$ then: 

$$u-v+y_{1}=2, v-u+y_{2}=2$$

since $x \leq 0$ then let $x=-w$ for $w\geq 0$. Now we can now obtain the following: 

$$\begin{cases}
\text{min } x_{1}-x_{2} & \text{ st} \\ \\

3w+v-u=5 \\
u-v+y_{1}=2 \\ 
v-u+y_{2}=2 \\
 \\
y_{1},y_{2} \geq 0
\end{cases}$$




