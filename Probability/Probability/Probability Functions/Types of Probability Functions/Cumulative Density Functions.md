---
title: Cumulative Density Functions
tags: 
draft: "false"
---
The Cumulative Density Function, $F(x)$ for a given [[Random Variables]] $X$, returns $\mathbb{P}(X\leq x)$.  The CDF is defined for both continuous and and discrete cases. 

As $x\to \infty$, it follows that the probability that $x$ occurs increases, and so the value of our CDF tends towards 1. Once it reaches one it remains there. Consider the example below:
![[CDF_normal_male.webp]]

In the continuous case, for a CDF defined along $[a,b]$, we define the CDF at $k \in [a,b]$ for the [[Probability Density Function]] f(x) is:
$$\mathbb{P}[X\leq x] = \int_{b}^{k} f(x)dx$$
Discrete CDFs will have jump discontinuities, and it increases as $x \to \infty$. Eventually we hit $1$, and we remain there forever. An example of a discrete CDF is the following:
![[unnamed.png]]
Discrete CDFs have jump discontinuities. If we want to recover the original [[Probability Mass Function]] all we have to do is measure the amount our probability changed from one probability to the next. If given the [[Probability Mass Function]] we can construct the CDF and vice-versa. 

For the discrete case, given the [[Probability Mass Function]] $g(x)$ along the interval of integers, $a,b$ we define our probability for $\mathbb{P}[X\leq k]$ for $k$ in between the interval $a,b$:
$$\mathbb{P}[X \leq x] = \sum_{i=a}^k \mathbb{P}[X=k]$$

---
# Properties of CDFs 
1. CDFs are increasing, that is as $x \to \infty$, $F(x)$ gets larger 
2. CDFs are right continuous. For any point, approaching its limit as we go from the right the limit works as we would expect it to (?)
3. As $F(x) \to 0$ as $x \to -\infty$, $F(x) \to 1$ as $x \to \infty$ 

If a function satisfies these 3 qualities, then it is a valid CDF. And a valid CDF must satisfy these 3 properties. 