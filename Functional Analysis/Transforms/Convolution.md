---
title: Convolution
tags:
draft: "False"
---
# Convolution Overview 


---
# Acyclic [[Convolution]]

The discrete version of [[Convolution]] for 2 given vectors $c,d \in \mathbb{F}^n$ is given as follows:
$$(c \times d)_{k}=\sum_{i,j : i+j=k} c_{j}d_{j}=\sum_{i=1} c_{i}d_{k-i}$$
The general rule for this is that the indices of $i$ and $j$ should add to $k$, which we can reduce to a single variable by the expression on the right. We can extend this to continuous functions by considering the continuous functions $f(x),g(x)$ and convolving them:
$$f(x) * g(x) = (f * g)(x)$$
The discrete cases asks us for $k$, however the continuous case asks us for when both $f$ and $g$ are at $x$. The analog for the continuous cause is to use integration instead of summation:
$$(f*g)(t)=\int_{-\infty}^\infty f(x)g(t-x)dx$$
Here, there is a correspondence with the discrete variant, namely $x$ corresponds to $i$, and $t$ corresponds to $j$. $t$ is the amount of shift that we are applying to our functions. We may want to apply [[Cyclic Convolution]] if $f$ and $g$ are both periodic functions, say if $f$ and $g$ are sinusoidal. 

---
# Cyclic [[Convolution]]
If we have some [[Group]], $G$ and some $x,y \in G$, and we want $x * y \in G$ as well, we consider [[Cyclic Convolution]]. In the discrete case, we modify our formulas to remain cyclic by doing the following:
$$(c \times d)_{k}=\sum_{i+j=k \text{ mod}(n)} c_{j}d_{j}=\sum_{i=1}^{n-1} c_{i}d_{k-i}$$
---
# Correspondence to [[Toeplitz Matrix]] and [[Circulant Matrices]]
To describe [[Convolution]], we can use a [[Toeplitz Matrix]], and to describe  [[Cyclic Convolution]] we use a [[Circulant Matrices]] (which are [[Toeplitz Matrix]], but have the property of being cyclic and forming their own [[Group]]). 

---
# Applications
[[Convolution]] is used extensively in signal processing and in [[Convolutional Neural Networks]] for image processing. [[Convolution]] also connects to the [[Fourier Transform]] of a function. 