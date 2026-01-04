---
title: Robust Regression with the L1 Norm
tags:
draft: "false"
---
# Robust Regression with the L1 Norm 
Typically in the context of applied math, we deal with the [[Euclidean Norm]] almost exclusively. It turns out that both the L1 and L2 norms have their own merits. The L1 norm has gained significantly more interest recently, since it is used in statistics and also in regression type problems. The L2 norm has nice geometric aspects that we ignore when we choose the L1 norm and is computationally easier and easier to write out in code. 

In the typical [[Least Squares]], ignoring the $y$ intercept and assuming it is 0 to begin with, we have the following equation:
$$ax=b \iff a \begin{pmatrix} x_{1} & x_{2} & \dots &x_{n} \end{pmatrix}=\begin{pmatrix} b_{1} & b_{2} & \dots &b_{n} \end{pmatrix}$$
We are trying to find $a \in \mathbb{R}$ such that:
$$\min(\|ax-b \|_{2})$$
Typically, we try and minimize using the 2 norm. However, there is a huge problem here involving outliers. Minimizing the [[Euclidean Norm]] here would massively skew the distribution. There's a very simple solution, which can be handled by instead considering the $LP1$ norm instead of the $LP2$ norm:
$$\min(\|ax-b\|_{1})$$Instead of adding the errors of all of the squares, we are just adding the absolute values of the errors, which are not squared. 