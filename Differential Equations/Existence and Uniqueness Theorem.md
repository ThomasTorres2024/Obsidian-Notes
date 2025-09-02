---

---
---
# Definition of the Existence and Uniqueness Theorem/Picard–Lindelöf Theorem
When trying to solve differential equations, we want to know if such a solution exists and if the solution to the equation is a unique one. If we trying to solve for an equation which does not exist then we clearly are wasting time and want to know when we we can solve such equations. We also want to know if we are able to solve an equation with more than one function. 

There is one such tool that allows us to determine if a differential equation has a solution and if it exists. 

---
# Definition of the Picard–Lindelöf Theorem 
Consider the function $y' = f(x,y)$ with the initial value of $y(x_{0})=y_{0}$. 

The theorem comes in two parts. We know that $y$ exists if $f$ is continuous near the point $(x_{0},y_{0})$ along 
Furthermore, if $\frac{\partial f}{\partial x}$ is continuous at $(x_{0},y_{0})$ then we can state that $y$ is unique.

---
# Proof of the Picard–Lindelöf Theorem 

The Picard–Lindelöf Theorem is the uniqueness part of this theorem, and assumes that a function satisfies $\dot x = v(x)$ and $x(0)=x_{0}$. 

The function $v : \mathbb{R}^n \rightarrow \mathbb{R}^n$ is locally Lipschitz contiunuous

---
# Other Forms of the Theorem

It must be noted that this is not an iff statement. If the function is not continuous and/or its derivative is also not continuous, then it could still be the case we have a unique function that satisfies the equation. 

The interval guaranteed by this theorem is rather small, so we should try and look to variants of the problem to narrow our search.

One of the reasons we choose to categorize differential equations by their form, ie ordinary, linear, first degree, second degree, and so on, allows us to go beyond the base theorem and specify more conditions for the interval these functions are defined on and their uniqueness. 