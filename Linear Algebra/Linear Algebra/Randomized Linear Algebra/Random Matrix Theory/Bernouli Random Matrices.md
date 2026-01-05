---
title: Bernouli Distributed Random Matrices
tags:
draft:
---
# Bernouli Random Matrices 
We assume that for $M \in \mathbb{R}^{m \times n}$ that each $M_{ij}$ is distributed using a [[Bernouli Distribution]] with a mean of 0 and a variance of 1, which means $M_{ij} \in \{+1,-1 \}$, each has a probability of half of being chosen. 

One of the worthwhile things to understand for [[Bernouli Random Matrices]] is to understand the behavior of the [[Singular Value]]s of this class of matrices. 

One way we can begin to work with the upper bound for the [[Singular Value]]s is by considering the square of the [[Frobenius Norm]] of $M$. From this we obtain the [[Moment Method]]:

---
# [[Moment Method]]

Recall that:
$$\|A\|_{F}= \sqrt{ \sum_{i=1}^{m}\sum_{j=1}^{n} |a_{ij}|^{2 }} = \sqrt{\sum_{i=1}^{\min(m,n)}\sigma_{i}^{2  } }=\sqrt{ \text{Tr}(AA^H) } $$This allows us to establish the following bound:
$$\sigma_{1}^{2}\leq \text{Tr}(AA^{H)}= \sum \sigma_{i}^2$$
This method generally does a poor job at telling us information about the least singular value. For this we have the [[Epsilon Net Method]]. 

---
# [[Epsilon Net Method]] for Determining Behavior of the Smallest [[Singular Value]] 

We suppose that $\exists c \in \mathbb{R}$ such that the following is true with exponential probability:
$$\sigma_{i}(M) \leq c \sqrt{ n }$$
$$\mathbb{P}[\sigma_{1}(m) > c\sqrt{ n }] \leq \exp(-cn), c > 0$$
This result can be proved by using the supremum definition of the maximum singular value:
$$\mathbb{P}[\sigma_{1}(m) > c\sqrt{ n }] =\mathbb{P}\left[ \underset{\|x\|=1} \sup \|Mx\|  > c\sqrt{ n }\right]
=
\mathbb{P}\left[ \bigcup_{\|x\|=1} \|Mx\| > c\sqrt{n} \right]$$
One way Tao gives to go about this problem is by trying to sum over all such values for an upper bound, however we know that this is impossible as the region we are summing over is [[Uncountably Infinite]], so this sum is impossible. Our way of handling this is by constructing an epsilon net along the unit ball. 

We take some finite set of points along the unit ball such that each point is at least a distance of $\epsilon \geq 0$ at least away from one another and that all $x \in$ the epsilon set satisfies $\|x\|=1$. 

Let us denote $\Sigma$ to be a maximal $\epsilon$-net in $\{ \|x\|=1 \}$. All points in $\Sigma$ are $\epsilon$ apart from one another. The fact that the set is "maximal" means that no more points can be added to the set without destroying the epsilon spacing.  

We can find an exponential bound for the cardinality of the set $\Sigma$:
$$|\Sigma|\leq O(1/\epsilon)^n$$
Which is to say that the cardinality is less than that of some constant multiple of $1/\epsilon$ raised to some power. The set is still exponentially large, which is an improvement from being uncountably large. 

If we consider the set of balls centered at each point $x \in \Sigma$ of radius $\epsilon/2$, we can observe that these balls are bounded in the sphere of radius 2 since $1 + \epsilon < 2$ since $\epsilon < 1$. All of the balls of $r=\epsilon/2$ are disjoint. 

We can thus create a bound for the cardinality of $\Sigma$ using the following:
$$|\Sigma|\leq\frac{\text{vol}(B(0,2))}{\text{vol}(B(0,\epsilon/2))}$$
Which makes sense since it's the maximal number of balls that we could fit in the larger surrounding sphere embedded along $S_{2}$. We can actually bound our operator norm now using the following:
$$ \underset{\|x\|=1} \sup \|Mx\| \leq 2 \underset{x \in \Sigma} \sup \|Mx\|$$
We can prove this result. We know that for $\|x\| = 1, x \in S_{2}$ that there has to be a solution for $\|Mx\|$ since the set is "compact" and bounded. We do not know if $x \in \Sigma$ but we can say that $x$ is near $\Sigma$. 

We can say that $\exists y \in \Sigma, \text{ such that } \|y-x\| \leq \epsilon$. Therefore, by the [[Triangle Inequality]] we can write:
$$\|Mx\|_{2} \leq \|My\|_{2}+\|M(x-y)\|_{2}$$
We can further bound the inequality using the submultiplicative property of Matrix Norms:

$$\|My\|_{2}+\|M(x-y)\|_{2} \leq  \underset{y \in \Sigma} \sup \|My\| + \|M\|_{2} \cdot \|x - y\| $$
$$\leq \underset{y \in \Sigma} \sup \|My\| + \|M\|_{2}\epsilon \text{ (true via our assumption about near point y)}$$
If we assume that $\epsilon = \frac{1}{2} \implies$ our original problem can thus be re-written in the following form, meaning that we can bound an uncountable supremum with one which is countable:
$$\mathbb{P}\left[\sigma_{1}(m) > c\sqrt{ n }\right] \leq \mathbb{P}\left[\sup \|My\| \geq \frac{c}{2}\sqrt{n} \right]$$We can now use a [[Union Bound]] without being instantly dead out of the water:
$$=\mathbb{P}\left[\|Mx\|_{2} \geq \frac{c}{2} \sqrt{n} \right] $$
Since our matrix $M$ is a [[Bernouli Random Matrices]] we can say that its rows are independent and sample from the set $\{-1,1 \}$ (since it is Bernouli). $\|Mx\|$ can thus be re-written using [[Matrix Multiplication]] as:
$$= \mathbb{P}\left[ \left(\sum_{i=1}^n |x_{i} \cdot x|^2  \right)\geq \frac{c^2n}{4} \right]$$
Because each row $x_{i}$ is independent, we can somehow express it using a [[Moment Generating Function]] of an [[Exponential Distribution]], and therefore we obtain the result:
$$\boxed{}$$