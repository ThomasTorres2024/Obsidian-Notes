---
title: Distance Matrices
tags:
draft: "false"
---
# Distance Matrices
We are given a set of point in $\mathbb{R}^d$, where $d$ is not known. We are given a matrix $D$, where we know the [[Euclidean Norm]] between $x_{i}$ and $x_j$. We want to find every $x$ that satisfies this condition. For one, we know that our problem is invariant to shift translations, and to rotations. We can simplify the problem and remove the translation invariance by centering the origin of our coordinates there. 

Given some matrix $D$, we want to find the $X$ matrix which consists of the positions for each point in space. 

Let us denote the distance between some $x_{i}$ and $x_j$ by $d_{ij}:$
$$d_{ij}=\|x_i-x_j\|^2=(x_i,x_i)-2(x_i,x_j)+(x_j,x_j)$$