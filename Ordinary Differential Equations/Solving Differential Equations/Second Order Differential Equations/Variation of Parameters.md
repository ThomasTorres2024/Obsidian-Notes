---
title: Variation of Parameters
draft: "false"
tags:
---
# Variation of Parameters Overview 
Another method for solving non-homogeneous equations of the form: 
$$y'' + p(x)y + q(x)y = f(x)$$
Notice that the DE is obviously not homogeneous.

This method is useful for solving equations whose nth derivative does not result in a closed set of members, but instead keeps continuing, Example :$y'' - 5y' -6y = \frac{1}{\cos(x)}=\sec(x)$ which results in $\sec(x)'= \sec(x)\tan(x)$, and other functions which do not have cyclic derivatives, making the [[Method of Undetermined Coefficients]] useless here. 

For the general homogeneous equation, we would solve the equation s a homogeneous equation, and then substitute the valeus of $v_{1}(x)$ and $v_{2}(x)$ into the homogeneous solution, $y_{1}v_{1}(x) + y_{2}v_{2}(x)$. We then take derives of the expression, and get:

$$y_{p}' = v_{1}'y_{1}' + v_{2}y_{2} + v_{1}y_{1}' + v_{1}y_{1}' + v_{2}y_{2}'$$

We then forcefully set $v_{1}'y_{1}' + v_{2}y_{2}$ to be equal to zero, and then take a second derivative. 

$$ y_{p}'' = v_{1}'y_{1}' +  v_{1}'y_{1}'' + v_{2}'y_{2}' + v_{2}y_{2}'' +v_{1}y_{1}' + v_{2}y_{2}'$$

Taking these terms and substituting them into the general homogeneous equation and simplifying yields,

$$v_{1}(y_{1}'' + p(x)y_{1}' + q(x)y_{1}) + v_{2}(y_{2}'' + p(x)y_{2}' + q(x)y_{2}) + v_{1}'y_{1}' + v_{2}'y_{2}'= f(x) $$

We know that both $v_{1}$ and $v_{2}$ and the terms that they multiply together are both the homogeneous solutions, and thus reduces the equation nicely to:
$$v_{1}'y_{1}' + v_{2}'y_{2}' = f(x)$$

If we find the functions for $v_{1}$ and $v_{2}$ respectively, we can find the result for $y_{p}$. We do this by a system of equations:
$$v_{1}'y_{1} + v_{2}'y_{2} = 0$$
$$v_{1}'y_{1}' + v_{2}'y_{2}' = 0$$
We can use [[Cramer's Rule]] to solve this following system of equations, given the [[Wronskian]] $\mathcal{W}$:
$$v_{1}' = y = \frac{	\begin{bmatrix}
0 & y_{1}\\
f & y_{2}'
\end{bmatrix}}{\det(\mathcal{W})} $$
$$v_{2}' = y = \frac{	\begin{bmatrix}
y_{1} & 0\\
y_{1}' & f'
\end{bmatrix}}{\det(\mathcal{W})} $$
Therefore we obtain the following solutions for $v_1',v_2'$:
$$v_{2}' = \frac{y_{1}f}{\det(\mathcal{W})} , v_{1}' = \frac{-fy_{2}}{\det(\mathcal{W})}$$
We then integrate both sides and obtain the functions for $v_{1}$ and $v_{2}$.
