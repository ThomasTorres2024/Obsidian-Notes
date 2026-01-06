---
title: Convolution Matrix
tags:
draft: "false"
---
# Toeplitz Matrix/Convolution Matrix 
A [[Toeplitz Matrix]] is a special type of matrix where each diagonal entry consists of a single value, for instance the following are [[Toeplitz Matrix]]:
$$A=\begin{bmatrix} 1 & 2 & 3\\
4 & 1 & 2 \\
5 & 4 & 1
\end{bmatrix}, A=I_{n}$$
There are some modifications of [[Toeplitz Matrix]] like [[Circulant Matrices]] which are [[Toeplitz Matrix]] with the condition of being cyclic. These matrices are used for the operation of [[Convolution]] (acylic Convolution), and are used to speed up operations in [[Convolutional Neural Networks]]. 
