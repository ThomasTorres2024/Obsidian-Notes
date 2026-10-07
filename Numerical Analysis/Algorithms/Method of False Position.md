---
title: Method of False Position
tags:
  - Numerical_Analysis
draft: "False"
---
# Method of False Position 

Similar to the [[Secant Method]] and [[Bisection]] method. Instead of cutting the interval in half, we run the secant method until we go out of bounds. 

We have a test which uses the bisection method to cut the interval if we go out of bound. This method is generally not recommended nowadays, but this is a demonstration of "bracketing". 

---
# Algorithm

1. Choose initial approximations $p_{0},p_{1}$ with $f(p_{0}) \cdot f(p_{1}) <0$. 
2. Approximation $p_{2}$ is chosen in the same manner as the secant method as the $x$ intercept of the line that joins $(p_{0},f(p_{0}))$ to $(p_{1},f(p_{1}))$. 
3. In order to determine the line to compute $p_3$, we need to consider $\text{sgn}(f(p_{2})) \cdot   \text{sgn}(f(p_{1}))$
	* If the quantity is negative, then we bracket a root, and choose $p_{3}$ as the $x$ int. joining the two lines
	* If not, we choose $p_3$ as the x-int of the line joining $(p_{0},f(p_{0}))$ and $(p_{2},f(p_{2}))$. We then interchange the indices of $p_0,p_1$,