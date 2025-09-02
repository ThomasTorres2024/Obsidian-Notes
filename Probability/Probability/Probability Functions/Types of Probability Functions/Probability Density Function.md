---
title: Probability Density Function
tags: 
draft: "false"
---
# PDF Definition
A [[Random Variables]] $X$ has a [[Probability Density Function]] $f(x)$ if $$\mathbb{P}(a \leq x \leq b) = \int_{a}^b f(x)dx$$
Notice that if we let $a=b$ then, we have that the probability of a specific point is zero since we integrating to the same bound. 

A [[Probability Density Function]] should have $f(X) \geq 0$ and that $\int_{-\infty}^\infty f(x)dx = 1$, meaning every probability is one, and the total probability of our function is 1. 

We can approximate that we have a probability of $x$ along $[x-\frac{\epsilon}{2},x+\frac{\epsilon}{2}]$ using the PDF given some $\epsilon > 0$ that we can write our probability as:
$$f_{x}(x)\cdot \epsilon$$

---
# CDF Relation to PDF
The CDF is defined as $F(X)=\mathbb{P}[X=x]$, but notice that we define probabilities via integrals, so we get that:
$$F(X)=\mathbb{P}[X=x] = \int_{-\infty}^x f_x(x)dx$$
Intuitively, we are finding the area to the left of $x$ along our curve. We can also find the PDF given the CDF, assuming that we have a continuous random variable $X$. Assuming that the cdf, $F(x)$ is differentiable everywhere, we can determine our [[Probability Density Function]] via:
$$f_{x}(x) = \frac{d}{dx}F(x)$$
This is true via the [[Fundamental Theorem of Calculus]]. Also note that $\mathbb{P}[a \leq x \leq b] = \mathbb{P}[a < x < b]$ are equivalent since we have a continuous distribution, but in the discrete case these would generally be different. 

---
# Expected Value 
The [[Expected Value]] of a PDF is given by an integral instead of a sum:
$$\mathbb{E}[X]= \int_{\infty}^\infty x f_{x}(x) dx$$
---
# Variance 
The [[Variance]] measures how spread out our distribution is 