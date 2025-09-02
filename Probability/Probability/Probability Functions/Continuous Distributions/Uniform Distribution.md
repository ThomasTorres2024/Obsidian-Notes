---
title: Uniform Distribution
---
The [[Uniform Distribution]] is a [[Continuous Distributions]] denoted by $Unif(a,b)$, where along the points $[a,b]$ we have that $\mathbb{P}[X=x]=\frac{1}{a-b}$ for $x \in [a,b]$. 
![[maxresdefault.jpg]]
We can define our [[Probability Density Function]] for the [[Uniform Distribution]] by:
$$
f(x) = \begin{cases}    \frac{1}{a-b} & \text{if } a \geq x  \geq b \\    0   & \text{else } \end{cases}
$$
The [[Cumulative Density Functions]] for this distribution is its integral:
$$
f(x) = \begin{cases}    \frac{x-b}{a-b} & \text{if } a\geq x  \geq b \\ 0 & \text{if } a<x\\    1   & \text{else } \end{cases}
$$
We can easily find the [[Expected Value]] and [[Variance]] using the formulas for each. 
The [[Expected Value]] is $\frac{a+b}{2}$, which is the midpoint of the uniform distribution. 
The [[Variance]] is $\frac{(b-a)^2}{12}$. 
