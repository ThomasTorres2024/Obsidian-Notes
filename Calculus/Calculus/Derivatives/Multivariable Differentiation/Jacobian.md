---
title: Jacobian
tags:
draft: "False"
---
# Jacobian
The [[Jacobian]] is the matrix of[[Partial Derivative]]s of a function, $f: \mathbb{R}^n \mapsto \mathbb{R}^m$. 

For instance, if we consider $f=x^2+3xy$ then the [[Jacobian]] of $f$ is actually a special case and gives the [[Gradient]]: 
$$J_f=\langle 2x+3y,3x \rangle $$
One way that I like to remember the Jacobian is through the following outer product trick (I see notation like this often in vector calculus):
$$J_f=[f_1 , f_2 , \cdots f_m] \cdot \begin{bmatrix} \partial f/\partial x_1 \\\partial f/\partial x_2 \\ \dots \\ \partial f/\partial x_n   \end{bmatrix}$$
