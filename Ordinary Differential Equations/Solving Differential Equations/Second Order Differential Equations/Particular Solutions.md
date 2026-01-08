---
title: Second Order Non-Homogeneous Differential Equations
tags:
draft: "false"
---
# Introduction to [[Particular Solutions]] of an [[Ordinary Differential Equation]]:
#### Theorem:
We can write y as: $$y = y_{p} + y_{1}c_{2} + y_{2}c_{2}$$ Which is actually just the sum of the homogeneous equation and the particular solution, $y_{p}$. 

We can prove this result by plugging in the general solution $y$ into the equation, $f(x)$. 

$$y'' + p(x)y + q(x)y = f(x)$$
Taking the difference between $y$ and the $Y$ which solves the homogeneous equation, we essentially remove the homogeneous solution, and we can then re-write the equation to show that the homogeneous solution summed to the particular is the general solution y. 

To solve these equations practically, we try to solve the homogeneous equation, and one particular solution of the non-homogeneous equation we are trying to solve. We can then write $y$, the solution to this DE, as the sum of the homogeneous and non-homogeneous equations. The only difficult part of this process is trying to solve for the particular solution.

---
# Finding [[Particular Solutions]] 
We have several methods for finding [[Particular Solutions]] to [[Second Order Differential Equation]]s:
* (Guessing and Checking) If we have only one particular solution, we can solve for all of the different y's. We find $y_{p}$ by observation, which is to say a glorified way of guessing and checking. 
* [[Variation of Parameters]] 
