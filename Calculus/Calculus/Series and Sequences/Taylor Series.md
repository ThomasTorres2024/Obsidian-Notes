---
title: Taylor Series
tags:
draft: "false"
---
# Taylor Series in Single Variable Calculus
In single variable calculus, we can approximate a function using the [[Taylor Series]] using the first $k$ derivatives of our function and constructing a function of the following form for a given function $f$ which is at least $k$ times differentiable and analytic on $(a,b)$. Another thing to note is that an [[analytic function]] is one which can be represented by a [[Taylor Series]] expansion on some interval as $k\to\infty$, the approximation function will tend towards the actual function. 

Our general definition is of the form:
$$f(x)\approx f_{\text{approx}}= \sum_{n=0}^k \frac{f^n\cdot(x)^n}{n!} \text{ where } f^n \text{ represents the nth derivative of } f.$$
I like to think of this as an extension of the idea that the very essence of calculus is using linear approximations to get good approximations of an otherwise complicated object locally. We can then add on a second degree approximation in the form of quadratic, and so on to the $n$th degree for even better approximations, until having taken $n\to \infty$ many derivatives, we get $f$ if our error term:
$$ \lim_{n \to \infty }f-f_{approx}=0 \implies \lim_{k \to \infty} \sum_{n=0}^k \frac{f^n\cdot(x)^n}{n!}=f$$
---
# Multivariable Taylor Series 
