---
title: Reduction of Order
tags:
draft: "false"
---
# Reduction of Order

Provided that one solution is known, a second solution can be found by performing the reduction of order method. Let $y_{1}(x)$ be a solution to a [[Second Order Differential Equation]].  

We can define $y_{2} = y_{1}\cdot v(x)$ where v(x) is simply a non-scalar function, such that $y_{1}$ and $y_{2}$ will be [[Linearly Independent Functions]]. The value for $y_{2}$ can be found by taking the first and second derivatives of the function in this form and then substituting it into the differential equation. Ideally, the equation will yield a differential equation which is easily solvable involving $v(x)$ and its derivatives, which can then be used to solve for the value of $v(x)$ and thereby $y_{2}$.

This can also be done using a formula given that the differential equation we are trying to solve is $y'' + p(x)y' + q(x)y = 0$:

$$y_{2}(x) = y_{1}(x) \int \frac{e^- \left(\int P(x)dx \right)}{(y_{1}(x))^2} \,dx$$
