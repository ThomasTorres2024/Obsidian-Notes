---
title:
---
 [[Chebyshev Polynomial]]s are [[Orthogonal]] [[Polynomial]]s on $(-1,1)$ with respect to the weight function $w(x)=(1-x^2)^{-1/2}$. These are actually [[Fourier Series]] except we substitute $x$ with $\cos(x)$, so for any [[Fourier Series]], the properties of a fourier series applies to 
 
 Here we define that:
$$\begin{align}
T_{n}(x) = \cos[n\arccos(x)] \quad \text{ for each } n\geq0 \\
T_{0}(x) = \cos(0 \cdot \arccos(x)) = 1  \\
T_{1}(x)=\cos[1 \cdot \arccos(x)]=x
\end{align}$$

Regardless of the $n$ value chosen we have that it and $w(x)$ are orthogonal, observe the following via properties of odd functions:
$$\int_{-1}^1 w(x)T_{1}(x) = \int_{-1}^1 \frac{x}{\sqrt{ 1-x^2 }}\text{d}x = 0 \text{ (odd func)} $$

We can obtain the $n$th [[Chebyshev Polynomial]] via the following:

$$\begin{align}
T_{n+1}=2xT_{n}(x)-T_{n-1}(x)
\end{align}$$
Due to this recurrence relation we know that despite the fact we use arctangents and complicated constructions these __ultimately are just polynomials__. 

We have $n$ simple zeroes in $[-1,1]$ at $\bar{x_{k}}=\cos\left( \frac{2k-1}{2n}\pi \right)$.

Here we have also that the absolute extrema are at $\bar{x_{k}'}=$ (TODO)

with $T_{n}(\bar{x_{k}'}) = (-1)^k$ for each $k=0,1,2,\dots, n$. The zeroes are well known, and we do not necessarily need the polynomial in order to find them. 

We can make the [[Chebyshev Polynomial]]s [[Monic Polynomial]]s by scaling them down  by $2^{n-1}$ which is the leading term of the polynomials:

$$\bar{T}_{0}(x)=1 \quad $$

When we use [[Chebyshev Polynomial]]s zeroes and interpolate through these endpoints we can overcome the [[Runge Phenomena]] that plagued standard interpolation with evenly spaced numbers. [[Chebyshev Polynomial]]s tend to cluster their roots towards the ends of the interval $[-1,1]$. 

What this means is __do not pick our points to be evenly spaced, pick zeroes of the [[Chebyshev Polynomial]]__ (we can pick which zeroes though). 

We are not always on the same interval, say if we have $[-5,5]$ and we want to make it work for the function we want to interpolate. We would just use $y=5x$ for the zeroes. 