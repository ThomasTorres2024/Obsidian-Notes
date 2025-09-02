---
title: Var
tags: 
draft: "false"
---
# Variance 
The [[Variance]] measures how spread out our distribution is. We denote this by $Var(x)$. Intuitively, we would like to try and get the distance between every $x$ in our distribution and its mean, which we will denote here as $\mu$. We would thus want to calculate:
$$\mathbb{E}(X-\mu)=0$$
Notice that by the properties of [[Linearity]] that this results in a 0, so this isn't a good metric. We could try to impose an absolute value, but this isn't nice to work with due to the discontinuous point at $x=0$. We instead opt to square the amount:
$$Var(x)=\mathbb{E}(X-\mu)^2$$
There's a lot of geometry that goes underneath the hood using this squared metric. Since the [[Variance]] is a squared term, and its a bit more difficult to work with when we want to apply it, we typically take the square root of it to obtain the [[standard deviation]]:
$$\sigma = \sqrt{Var(x)}$$
For instance if we square the units, we want to bring them back to unsquared.  We can make our definition of variance nicer to work with. Consider the following:
$$Var(x)=\mathbb{E}(X-\mu)^2=\mathbb{E}(X^2-2X\mu+\mu^2) =  \mathbb{E}(X^2)+-2\mu\mathbb{E}(X)+\mu^2)=\mathbb{E}[X^2]-\mathbb{E}[X]^2$$

This formula is true for both [[Continuous Distributions]] and [[Discrete Distributions]].

---
# Properties 
Given [[Random Variables]] $X$, we can consider what happens to the [[Variance]] under scaling and addition transformations. 

Given constant $c$, it follows that the variance is unaffected by addition with it: $\mathbb{V}[X+c]=\mathbb{V}[X]$. 
Given constant $c$ a scaling transformation does the following:
$$\mathbb{V}[Xc]= \mathbb{E}[(Xc)^2]-\mathbb{E}[Xc]^2 = c^2(\mathbb{V}(x))= c^2  \mathbb{V}[X]$$It is important to note that this mean out variance still positive since $c$ may be negative but our [[Variance]] should always be a positive value. In a sense we have that the variance is [[positive definite]], as it is only zero when we have a constant probability function. 

We also have that the [[Variance]] is not linear. For example, let us consider $Var(X+X)=Var(2x)=4Var(x)$, which if it were linear would give $2Var(x)$ but it clearly does not. 