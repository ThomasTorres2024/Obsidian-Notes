---
title: Euler-Cauchy Equations
tags:
draft: "false"
---
# [[Euler-Cauchy Equations]]
Given a differential Equations of the form:
$$ax^2y'' +bxy' +cy  = 0$$
We can solve this [[Second Order Homogeneous Differential Equations]] by letting $y=x^n$. 

Observe that the derivative of a x raised to a constant power, n, is $y = x^n, y' = n\cdot x^n-1, y'' = n(n-1)\cdot x^n-2$. However, if each term were to be multiplied by its corresponding value, such as the second derivative multiplied by $x^2$ would result in $x^n$ again, and so on for other examples. 

Attempt the substitution $y = x^r$, $y' = rx^{r-1}, y'' = r(r-1)x^{r-2}$. Plug these values into the second order ODE:

$$ax^2(r(r-1)x^{r-2} + bx(rx^{r-1} cr^x) = 0)$$

Collecting terms $x^r$

$$x^r(ar(r+1) + br + c ) = 0$$
This is the characteristic equation for the Euler equation of the second order. This equation can also be written as, $$ar^2 + r(b-a) + c = 0$$We can then use the quadratic formula or some other method of factoring in order to solve for this equation.

---
# Repeated Roots
For situations with repeated roots, we must perform [[Reduction of Order]] on the equation that we found. 

We are trying to solve equations of the form, $y'' + p(x)y' + g(x)y = f(x)$, where f(x) $\neq$ 0. We want to use our knowledge of the homogeneous solution, which we can easily solve, to solve for the non-homogeneous solution. 
