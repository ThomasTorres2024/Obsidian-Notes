---
title: Negative Binomial Distribution
tags: 
draft: "false"
---
# Definition
The [[Negative Binomial Distribution]] is a distribution that generalizes the [[Geometric Distribution]]. It has two parameters, $r$ and $p$. 

Intuitively, the distribution is composed of [[Independent]] [[Bernouli Trial]]s with probability $p$. We measure the number of failures before the $r$th success.  This gives us our distribution. 

Our [[Probability Mass Function]] can be obtained via a sequence. We can represent our results as a binary string, where each success is a 1, and every failure is a 0. For example we could have:
$$1000100101$$
Our $r$th success is the last item in our binary sequence is always a 1, since we terminate then. The other $n+r-1$ failures can be supported in any order. Our formula is pretty straight forward, it just comes directly out of the [[Binomial Theorem]]. 

Let $X$ ~ $\text{Binom}(r,p)$. Its PMF is given by:
$$\mathbb{P}[X=n]= {n+r-1\choose r-1} p^r (1-p)^n$$
This is essentially just the binomial theorem applied when we have $n+r-1$ many trials (it would not be $n+r$ since we always have that the end is 1 regardless of our operation). We also consider $p^r$ since we succeed $r$ times and we consider $(1-p)^n$ because we have $n$ failures. 

---
# [[Expected Value]] Calculation
Working with this function in its raw form is quite difficult. We can think of this function as the sum of $r$ $X$ random variables, where each $r$ corresponds to a success. We have $r$ many since we can interpret our result as waiting for the first $r$ successes. So we have that:
$$\mathbb{E}[X]=\mathbb{E}\left( \sum_{i=1}^r X_{i} \right)$$
Each $X_{i}$ is the number of failures between the $i$ and $i-1$th success. Each trial is [[Independent]], but moreover, we should recognize that each $X_{i}$ here is a [[Geometric Distr  ibution]]. 

Since we have $r$ many [[Geometric Distribution]]s, and we can recall that the [[Expected Value]] of said distribution is $\frac{1-p}{p}$, it follows that for a [[Negative Binomial Distribution]] that we would have an [[Expected Value]] of:
$$\mathbb{E}[X]=\frac{(1-p)r}{p}$$

---
# PMF Verification

We can prove that the [[Negative Binomial Distribution]] is a [[Probability Mass Function]] by verifying that it has a mass of 1 and non-negative probabilities. It should be very clear that our function has probability entries for $n$ that are non-negative since we can't get a negative anyway here. 

We can simplify