---
title: Ill-Conditioned
tags:
draft: "False"
---
# Ill-Conditioned 
An [[Ill-Conditioned]] problem or algorithm in numerical analysis is a problem or algorithm where a small perturbation in the input results in a significant change in the output. We can gain insight into the [[Conditioning]] of a problem or algorithm by considering its [[Condition Number]]. 

Examples of Ill-Conditioned problems include solving the roots of a polynomial equation, which are almost always [[Ill-Conditioned]]. 

Another example of an [[Ill-Conditioned]] problem is the computation of [[eigen value]]s of a non symmetric matrix. For instance take the following two matrices:
$$\begin{bmatrix} 1 & 1000\\ 0 & 1  \end{bmatrix} \implies \Lambda=\{ 1,1 \}$$$$\begin{bmatrix} 1 & 1000\\ 0.001 & 1  \end{bmatrix} \implies \Lambda=\{ 0,2 \}$$
However, the computation of the [[eigen value]]s of a [[Symmetric Matrix]] is [[Well-Conditioned]]. 