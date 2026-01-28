---
title: Optimization
tags:
  - Optimization
draft: "False"
---
# Theoretical Optimization Overview 
Optimization considers strategies for finding the [[Global Minima]], [[Global Maxima]], [[local minima]], and [[local maxima]] of functions $f$ of the form:
$$f: \mathbb{R}^n \to \mathbb{R}$$
The function we are trying to minimize or maximize is known as the "objective function". The sets of functions that restrict our domain, $g_1,g_2,\dots g_k$ are known as the "constraint set". 

A point within the constraint set (Domain) is a point in the [[feasible set]] of a function. A point that is outside of the constraint is not in the [[feasible set]]. 

---
# Different Forms of Optimization Problems 

Optimization problems of the form $f: \mathbb{R} \to \mathbb{R}$ only requires singular variable calculus, and the [[First Derivative Test]] can be used to find the [[local maxima]] and [[local minima]] of a function. If we are subject to some constraint set, we essentially check the local maxima and minima by computing $f'(x^*)=0$, and then determine the [[Concavity]] by computing $f''(x^*)$. 

Say we have a constraint set given by $D=[a,b]$, then we would as well check to see if the endpoints $f(a)$ or $f(b)$ are extrema as well. 

Optimization problems of the form $f : \mathbb{R}^n \to \mathbb{R}$ rely on techniques from multivariable calculus to find extrema, namely techniques like [[Lagrange Multipliers]] when we have a non-linear function with a non-linear constraint set. 

##### Non-Linear Multivariable Function, Non-Linear Constraint Set 
If we are given some general region rather than just a boundary to use, say for example the constraint set $x^2+y^2 \leq 3$, we need to check all of the points along the boundary. and the points within the boundary. We thus divide our problem into 2 sub-tasks:
$$\begin{cases} 
x ^2 + y^2=3  & \text{Use Lagrange Multipliers}\\
x^2 + y^2 < 3 & \text{ Test for Extrema with Hessian} 
\end{cases}$$
For the first part, $x^2+y^2=3$, we obtain the optimal solutions along the boundary using [[Lagrange Multipliers]], and for within the region we can simply use the [[Hessian Matrix]] and determine when the [[Gradient]], $\nabla f = \vec{0}$. 

Using a [[Lagrange Multipliers]], we compute when the gradients of the constraint set are parallel to that of the function, that is to say: $$\nabla f = \lambda_1 \nabla g_1,\nabla f = \lambda_2 \nabla g_2, \dots \nabla f = \lambda_k \nabla g_k$$
##### Non-Linear Multivariable Function, Linear Constraint Set 
When we are given some multivariable function $f$ with a linear constraint set, we can express the function in terms of a single variable and then convert it into a single variable calculus problem that is a lot easier to work with. 

Say for $f : \mathbb{R}^3 \to \mathbb{R}$, we are given a constraint set where $\alpha x + \beta y + \gamma = 0$, then we can simplify our $f(x,y) \to f(x)$ or to $f(y)$, and then  

---
# [[Linear Programming]] 
[[Linear Programming]] is a domain of [[Optimization]] where the objective function is linear, and all of the constraint functions are linear. Techniques for solving problems of this form consist of:
* [[Simplex]]




