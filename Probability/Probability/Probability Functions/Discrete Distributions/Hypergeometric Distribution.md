---
title: Hypergeometric Distribution
tags: 
draft: "false"
---
# Motivation and Definition
The [[Hypergeometric Distribution]] is a generalization of the [[Binomial Distribution]] where we consider randomly selecting $k$ objects from two groups, $A$ and $B$. Taking from one group affects the probability of choosing from the other group, so it follows that our two groups are not [[Independent]], as drawing from one affects the other. This is because we are [[Sampling Without Replacement]]

We define the [[Hypergeometric Distribution]] as the following given we have $a$ items from group $A$ and $b$ items from group $B$, when we are drawing $n$ total items and looking for $k$ items from group $A$ where $0 \leq k \leq n\leq a$ and $0 \leq k \leq n-k\leq b$:
$$P(X=k)=\dfrac{{a \choose k}{b\choose n-k}}{{a+b \choose n}}$$
If we have that $n$ is a small number but $a+b$ is quite large, say that $a+b$ is a billion and $n=10$, then it would follow that the [[Binomial Distribution]] would behave quite similarly to the [[Hypergeometric Distribution]] here in this instance. 

--- 
# Verification that the [[Hypergeometric Distribution]] is a valid [[Probability Mass Function]] 

In order to verify that the [[Hypergeometric Distribution]] is a [[Probability Mass Function]] we need to be able to show that given $X$ ~ $\text{Hypergeom}(a,b,n)$ that each $\mathbb{P}(X=k) \geq 0$ and that $\sum_{i=0}^k \mathbb{P}(X=k)=1$. 

Recall that $P(X=k)=\dfrac{{a \choose k}{b\choose n-k}}{{a+b \choose n}}$. Since our choice formulas always result in non-negative numbers, and multiplication of non-negative is closed over the integers and we are guaranteed a positive denominator, then it follows that each $\mathbb{P}(X=k)\geq 0$. 

Secondly, we need to show that:
$$\sum_{i=0}^k \mathbb{P}(X=k)=1$$
We can reuse the [[Vandermonde Identity]] that we used to show that the sum of two [[Binomial Distribution]] [[Random Variables]] is another [[Binomial Distribution]].  

Let us show this result:
$$\sum_{i=0}^k \mathbb{P}(X=k)= \sum_{i=0}^k \dfrac{{a \choose k}{b\choose n-k}}{{a+b \choose n}} = \dfrac{1}{{a+b \choose n}} \sum_{i=0}^k {a \choose k}{b\choose n-k} = \dfrac{{a+b \choose n}}{{a+b \choose n}} = 1$$
$\therefore$ In conclusion, the [[Hypergeometric Distribution]] is a valid [[Probability Mass Function]] since it satisfies the two criteria of one. 

---
# [[Expected Value]] 
#### Let $X$ ~ $\text{Hypgeom}(a,b,n)$. Let $x_{j}$ be a [[Bernouli Trial]] or indicator that the $j$th card is an ace. 

Let us consider a hand of $5$ cards, and let us find the expected value that we have an ace in our hand. We make use of [[Linearity]] in this example. 
$$\mathbb{E}(X)=\mathbb{E} \left(\sum_{i=1}^5 x_{i} \right)= \sum_{i=1}^5 \mathbb{E}(x_{i})$$
I'm not entirely sure why but due to symmetry we can condense this down to:
$$=5\mathbb{E}(x_{1})=5 \cdot \dfrac{1}{13}=\dfrac{5}{13}$$
Generally, the expected value of a [[Hypergeometric Distribution]] is about the same, so 