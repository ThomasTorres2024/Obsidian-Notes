---
title: Second Order Homogeneous Differential Equations
tags:
draft: "false"
---
# Solutions to Homogeneous Second Order ODEs

[[Homogeneous Differential Equation]]s of the second order have the property that $y = y_{1}c_{1} + y_{2}c_{2} = 0$ and for any scalar multiple of the sum of the two separate linearly independent solutions, we get a new solution. This property is known as the "superposition" for homogeneous equations.  It is also worthwhile to note that the solutions to a [[Second Order Differential Equation]] of this form form a Vector Space ([[Vector Spaces and Vector Subspaces]].).

We can use the conditions of a vector subspace this to illustrate this solution. If $c_1=c_2=0 \implies y=0$ satisfies the condition. For $y_1,y_2 \in \mathcal{V}$ and $c_1,c_2 \in \mathbb{C}$ where $\mathcal{V}$ is the vector space of solutions to this [[Homogeneous Differential Equation]], we have that:
$$y_1c_1+y_2c_2=0+0\implies y_1c_1+y_2c_2\in \mathcal{V}$$
So since the scalar, additive, and 0 properties are satisfied, the [[Homogeneous Differential Equation]] of second order forms a [[Vector Subspace]] (I am aware these aren't the properties for a Vector Space, we have to satisfy all 8, this is just some quick vibe check for it, it obviously should).

In order to solve for the constants $c_{1}$ and  $c_{2}$  given $y = y_{1}\cdot c_{1} + y_{2} \cdot c_{2}$, two different values are needed of the expression, or related expression such as y'($x_{0}$), in order to find the values of these constants. Which is to say, we need some [[Initial Condition]] for our given DE.

#### Superposition of Second Order Differential Equation
If $y_{1}(x)$ and $y_{2}(x)$ solve the equation $y''+p(x)y'  + q(x)y = 0$ along the interval $I$, then the linear combination $$y_{1}\cdot c_{1} + y_{2}\cdot c_{2} =y $$
If $y_1$ and $y_2$ are [[Linearly Independent Functions]]. 

---
### [[Existence and Uniqueness Theorem]] for [[Second Order Homogeneous Differential Equations]]
The heart of differential equations is finding what function solves a differential equation, which in turn relates to more specific questions of if a differential equation has a solution, and if the  solution is unique. 

Unique solutions imply that only one function can solve a differential equation, whereas  some differential equations can be solved with more than one function. Taking a crucial fact from the study of [[Linear Equation]]s, all linear equations, whether a system of linear equations, one linear equation, or a linear differential equation, all have either 0, 1, or infinitely many solutions. 

This fact can be used to assert that the  equation $y''+p(x)y'' + q(x)y = f(x)$ has one function, $y$,  which solves the differential equation along the  closed interval x $\in (a,b)$ and for y $\in$ $(y_{0},y_{1})$, which satisfies the initial conditions y($x_{0}$) = $y_{0}$ and y'($x_{0}$) = $y_{1}$.

---
### Solution Set to Homogeneous Differential Equations

This theorem solves the uniqueness part of the problem. Given any specific solution given by y($x_{0}$) = $y_{0}$ and y'($x_{0}$) = $y'_{0}$, it can be shown that there exists a specific solution to the differential equation which is unique and specifies the values of $c_{1}$ and $c_{2}$ in $y = y_{1}c_{1} + y_{2}c_{2}$.

Since it is assumed that $y_{1}$ and $y_{2}$ are linearly independent functions, and that we can solve for 2 constants $c_{1}$ and $c_{2}$, we have arrived at a unique solution to the differential equation. From this the definition of the solution set to a homogeneous ODE follows as:

$$y = c_{1}y_{1} + c_{2}y_{2}$$

The textbook presents the reduction of order method in a light similar to that of solving the cubic equation, $x^3 -7x^2 +1$ where knowledge of one solution, $x = 1$, can provide us knowledge of other solutions after we factor out $(x-1)$, and obtain:
$$x^3-7x^2+1(x-1)(x^2+x-6)$$

Using theorem 3.4, provided that one solution to the differential equation is given as $y_{1}$, we can then manipulate the expression of the DE such that it will resemble a lower order differential equation and thereby become a trivial task to solve. We can make use of the equation, $y_{2}=v(x)y_{1}$ to accomplish this. $v(x)$ will be a non-constant function of x. If $v(x)$ is a constant, then this results in $y_{2}$ being a linearly dependent solution and therefore not the solution we are looking for. 
