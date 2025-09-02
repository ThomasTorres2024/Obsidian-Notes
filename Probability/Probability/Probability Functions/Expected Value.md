---
title: Expected Value
draft: "false"
tags:
---
# Expected Value
The terms [[average]], [[mean]], and [[Expected Value]] all refer to the same idea. This is a useful metric well tells us the the balance point of our [[Probability Mass Function]] or [[Probability Density Function]]. More loosely, it tells us what value we would expect to get if we performed an experiment on our function. 
#### Raw Averages 
For example, if we want to find the average of 1,2,3,4,5,6, we could simply just use a standard average formula:
$$\text{avg} = \dfrac{1}{6} \sum_{i=1}^6 i$$
Note also that an arithmetic sum allows us to compute this nicely in $O(1)$. Since we know that:
$$\sum_{i=1}^n i = \dfrac{n(n+1)}{2}$$
It follows that the average of this amount , over $n$ numbers, is:
$$ \dfrac{1}{n} \sum_{i=1}^n i = \dfrac{1}{n} \cdot \dfrac{n(n+1)}{2} =  \dfrac{n+1}{2}$$
#### Weighted Averages 
We also have weighted average, where we multiple numbers by constants in our average in order to skew our mean if needed. 

---
# Average of a Discrete [[Random Variables]] $X$
Our [[Expected Value]] of RV $X$ is essentially a weighted average. We define our expected value and denote it by $\mathbb{E}[X]$  by:
$$\mathbb{E}[X]= \sum_{i=1}^n i \cdot \mathbb{P}[X=i]$$We give a higher weight to values that are more likely, and a low weight to values that are less likely. That is the central idea of our summation here 

#### Example 1.) $X$ ~ $\text{Bern}(p)$:
$$\mathbb{E}[X]= \sum_{i=0}^1 i \cdot \mathbb{P}[X=i] = 0\cdot p+1\cdot p=p$$
A [[Bernouli Trial]] has an [[Expected Value]] of $p$. There's a bit more depth going on here. Let us examine indicator random variables, given by:
$$X= \begin{cases}
 1 & \text{if A occurs}  \\
  0 & \text{ else }\\
\end{cases}$$This gives the following result:
$$\mathbb{E}(X) = \mathbb{P}(A)$$We can think of this result as a bridge between [[Expected Value]]s and the [[probability]] of a value. We can think of all expected value problems as being reduced down to the probability of a given set of [[Bernouli Experiment]]s. 

---
# Linearity of Expected Values 
Given [[Random Variables]], $X,Y$, The expected value of $X+Y$ is:
$$\mathbb{E}[X+Y]=\mathbb{E}(X)+\mathbb{E}(Y)$$
This holds even if $X$ and $Y$ are [[Dependent Random Variables]]. Linearity of the sum of expected values allows us to also factor out a constant $c$ from our random variable:
$$\mathbb{E}[c \cdot X]=c \cdot \mathbb{E}(X)$$
We can use [[Linearity]] to prove the [[Expected Value]] of the [[Binomial Distribution]] as well. 

We can prove the property of [[Linearity]] of the [[Expected Value]] of $X+Y$. Let $T=X+Y$. 
$$\mathbb{E}[T]=\sum_{t}t\cdot\mathbb{P}[T=t]$$We want to be able to express our $\mathbb{P}[T=t]$ in terms of $X$ and $Y$. We can begin by imposing a constraint that:
$$\mathbb{P}[T=t]=\sum_{x}\mathbb{P}[T=t|X=x]\mathbb{P}[Y=x]$$
This definition has some serious pitfalls, and leaves us stuck. We can re-interpret this problem by reconsidering what the definition of [[Random Variables]] and the probability of an item. 

Let us remind ourselves that [[Random Variables]] can be defined as a function, $X$, that maps the [[Sample Space]], $\Omega$ to the reals:
$$X:\Omega \to \mathbb{R}$$
We can also reconsider our [[Expected Value]] equation, which we give for [[Random Variables]] $S$ as:
$$\mathbb{E}[S]=\sum_{s}s\cdot\mathbb{P}[S=s]$$
Let's give this problem a concrete interpretation. Let's say instead we are finding the average weight of a group of pebbles.

![[Pasted image 20250814001536.png]]
The typical expected value is a grouped sum, which takes each item in the group and sums them. We have another way of dealing with this problem, that allows us to find a mean of pebbles over each individual pebble. 

We can re-write our sum as:
$$\mathbb{E}[S]=\sum_{x}x\cdot\mathbb{P}[S=x]= \sum_{s}X(s) \mathbb{P}(\{ s \})$$
Which is really the same thing as an ungrouped sum and doing the pebbles individually for each stone $s$. We can use this definition to prove linearity of $T$:
$$\mathbb{E}[T]=\sum_{t}t\cdot\mathbb{P}[T=t]=\sum_{s}(X+Y)(s) \mathbb{P}[\{ s \}] $$
We can distribute our [[Random Variables]] so we get:
$$=\sum_{s}X(s) \mathbb{P}[\{ s \}]+\sum_{s}(Y(s) \mathbb{P}[\{ s \}] = \mathbb{E}[X]+\mathbb{E}[Y]$$
Similarly, we can also make the same argument for $c\cdot \mathbb{E}[cT]=c\mathbb{E}[X]+c\mathbb{E}[Y]$

Therefore, we have the linearity property. 

---
# LOTUS/Law of the Unconscious Statistician 
It follows that $\mathbb{E}[g(x)]= \int_{-\infty}^\infty g(x) f(x) dx$ in the [[Continuous Distributions]] case and $$\mathbb{E}[g(x)]= \sum_{i=1}g(i) \cdot  \mathbb{P}[X=i]$$
We can think of this in a sort of table sense. If we modify our $x$ somehow, we are not modifying the probabilities themselves but we are modifying the number associated with each probability. For instance consider the following:

![[Pasted image 20250823080450.png]]

We can see that each $X_{1}$ and $X_{2}$ has the same probability for each column, but they have different row entries at some values. Because the fact probability isn't changed, and just the associated value we can use [[LOTUS]]. 

#### Proof for [[LOTUS]] in Discrete Case 
We want to show that:
$$\mathbb{E}[g(x)] = \sum_{x} g(x) \mathbb{P}[X=x]$$
Recall that we can represent the expected sum in one of two ways, we can represent it as each $s$ in our Sample space using the ungrouped formula. 