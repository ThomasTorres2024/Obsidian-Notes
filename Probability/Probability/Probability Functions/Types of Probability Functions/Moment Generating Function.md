---
title: Moment Generating Functions
tags:
draft: "false"
---
# Moment Generating Function (MGF)
An alternate way to define [[Probability Density Function]]s. A random variable, $X$ has MGF $M(t) = \mathbb{E}[e^{tx}]$ as a function of $t$, as long as our function is finite along $(-a,a)$ where $a>0$. The moment generating function of a [[Probability Density Function]] is essentially the [[Laplace Transform]] of a [[Probability Density Function]].  

$t$ is just a dummy variable. This is a well defined variable, since the function of a [[Random Variables]] is itself a [[Random Variables]]. 

Why is this called a "moment generating function"? Let us expand the [[Taylor Series]] of our [[Moment Generating Function]], and we know that the taylor expansion of $e$ has an infinite radius of convergence, so it is valid everywhere: 
$$\mathbb{E}[e^{tx}]=\mathbb{E}\left[ \sum_{n=0}^\infty \frac{x^n t^n}{n!} \right]$$
Applying [[Linearity]] of the [[Expected Value]] over an infinite number of values 
$$= \sum_{n=0}^\infty \frac{\mathbb{E}[x^n] t^n}{n!}$$
$\mathbb{E}[x^n] \text{ is known as the } n\text{th moment}$. The first moment is the [[mean]], the second moment is not the [[Variance]] but we need it in order to find the [[Variance]]. Higher [[moment]]s have more complicated but useful interpretations. We might not care about moments beyond the mean and the variance, so why are MGFs important?

---
# Relevance of the MGF 
1. It is sometimes important to know higher [[moment]]s. The $n$th moment, $\mathbb{E}[X^n]$ is the coefficient of $\frac{x^n}{n!}$ in the [[Taylor Series]] of $M(t)$. Another way to write this is that the $n$th derivative of $M$  evaluated at 0 is our derivative: $$M^{(n)}(0)=\mathbb{E}[x^n]$$
2. The MGF determines the distribution. If [[Random Variables]] $X$ and $Y$ have the same [[Moment Generating Function]], then it follows that $X$ and $Y$ have the same [[Cumulative Density Functions]]. 
3. The sums of [[Random Variables]] is greatly reduced, we do not need to compute [[Convolution]] Integrals. If $X$ has MGF $M_{x}$ and $Y$ has MGF $M_{y}$ and $X$ and $Y$ are independent, then $X+Y$ has MGF:$$ \mathbb{E}[e^{t(x+y)}]=\mathbb{E}[e^{tx}] \cdot \mathbb{E}[e^{ty}] = M_{x}(t) \cdot M_{y}(t)$$