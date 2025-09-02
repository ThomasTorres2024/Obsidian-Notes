---
title: Bernouli Experiment
tags: 
draft: "false"
---

# [[Expected Value]] of $\text{Bern}(p)$
#### Let $X$ ~ $\text{Bern}(p)$:
$$\mathbb{E}[X]= \sum_{i=0}^1 i \cdot \mathbb{P}[X=i] = 0\cdot p+1\cdot p=p$$
A [[Bernouli Trial]] has an [[Expected Value]] of $p$. There's a bit more depth going on here. Let us examine indicator random variables, given by:
$$X= \begin{cases}
 1 & \text{if A occurs}  \\
  0 & \text{ else }\\
\end{cases}$$This gives the following result:
$$\mathbb{E}(X) = \mathbb{P}(A)$$We can think of this result as a bridge between [[Expected Value]]s and the [[probability]] of a value. We can think of all expected value problems as being reduced down to the probability of a given set of [[Bernouli Experiment]]s. 
