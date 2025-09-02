---
title: Geometric Distribution
draft: "false"
tags:
---
# Definition and Introduction
The geometric distribution is given by $X$ ~$\text{Geom}(p)$, is composed of [[Independent]] [[Bernouli Trial]]s. Each trial has the same probability of success. The [[Geometric Distribution]] is the number of failures before the first success. We need to account for if we are counting the last failure or if we are ignoring it. 

Let $q=1-p$. We have a potentially infinite amount of trials for this distribution.  

Also note that, say if we have $\mathbb{P}[X=5]$, we would have exactly one circumstances where we get this count which is 5 failures, and then a success at last, which is given by the following string:
$$FFFFFT$$
Our probability for this occurring is the probability of a failure, $q$, to the power of the number of failures, multiplied by the [[probability]] of a success:

The [[Probability Mass Function]] for the [[Geometric Distribution]] is:
$$\mathbb{P}[X=k]=q^kp$$
We can easily verify that this is a valid [[Probability Mass Function]]:
$$\sum_{k=0}^\infty pq^k = p\sum_{k=0}^\infty q^k = \frac{p}{1-q}=1$$It is also fairly clear that each $\mathbb{P}[X=k] \geq 0$.

---
# [[Expected Value]] of [[Geometric Distribution]]:
We can first start by the definition of [[Expected Value]] of $X$ ~ $\text{Geom}(p)$:
$$\mathbb{E}[x]= \sum_{k=0}^\infty k \cdot q^kp= p\sum_{k=1}^\infty k \cdot q^k$$
Our $k$ is quite annoying, so we want to be able to remove it and somehow relate it back to the [[Geometric Series]]. Note that:
$$\sum_{k=0}^\infty q^k = \frac{1}{1-q}$$
If we take the derivative of both sides we obtain:
$$\sum_{k=0}^\infty kq^{k-1} = \frac{1}{(1-q)^2}$$
Both sides are just missing a $q$ on both sides to get our original result above, this will thus yield:
$$\sum_{k=0}^\infty kq^{k} = \frac{q}{(1-q)^2}=\frac{q}{p^2}$$
Substituting this back into our original expression, we would obtain:
$$\mathbb{E}[X]=\frac{q}{p}=\frac{1-p}{p}$$
If we consider the definition of the distribution with the number of trials needed until the first success we get:
$$\mathbb{E}[X]=\frac{1}{p}$$
We also have a more intuitive way of proving the [[Expected Value]] for the [[Geometric Distribution]]. Let $c = \mathbb{E}[x]$. Let us consider the example of a coin toss. We have two cases, either we fail, or succeed, this gives us:
$$c=0 \cdot p + (1+c)q$$
And then we arrange getting:
$$c=\frac{q}{p}$$
I'm not really sure what's going on with this one since it relies on some previous lectures I haven't seen, so it's a bit weird I think. 

---
# First Success Distribution
Let $X$ ~ $FS(p)$. This is basically a [[Geometric Distribution]], but we count the success instead of not counting it. Note that for $Y$ ~$\text{Geom}(p)$ that:
$$X=Y+1$$
If we want to convert between the two and determine the [[Expected Value]] of this result, all we would need to do is to take the expected value of both sides, which would give:
$$\mathbb{E}[X]=\mathbb{E}[Y]+1 =  \frac{q +p}{p} = \frac{1}{p} $$
This is a fairly intuitive result. If $p = 0.1$ then it would imply that we would need ten trials to get our result, which is exactly what the reciprocal of it here does. 