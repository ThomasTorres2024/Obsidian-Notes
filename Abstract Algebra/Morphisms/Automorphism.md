---
title: Autmorphism
tags:
  - AbstractAlgebra
draft: "False"
---
# Automorphism
An [[Automorphism]] is an [[Isomorphism]], $\phi$ that maps a [[Group]], $G$ to itself, which gives us:
$$\phi : G \mapsto G$$
Another way that we could say that is that $\phi$ is an [[Automorphism]] if it is both an [[Endomorphism]] and an [[Isomorphism]]. 

---
# Inner [[Automorphism]] 
The inner automorphism is defined by fixing some $a \in G$, such that we define the following bijective function:
$$\large \phi_{a}(x) = axa^{-1}$$
Which we call the "inner automorphism of $G$ induced by $a$". 

---

# Theorem.) $\text{aut}(G),\text{inn}(G)$ are [[Group]]s 

For a group $G$, let us denote the set of all [[Automorphism]]s of $G$ by $\text{aut}(G)$ and the set of all Inner Automorphisms by $\text{inn}(G)$.

It can be shown that both of these sets are actually [[Group]]s where the [[Binary Operation]] is function composition. 

# Motivating Example.) 
We are interested in finding all of the automorphisms of the group $\text{aut}(\mathbb{Z}_{10})$. We first want to assess what properties some $\alpha \in \text{aut}(\mathbb{Z}_{10})$ has.  

First, note that if $\alpha(1)$ is known, then for any other $k \in \mathbb{Z}_{10}$ then:
$$\large \alpha(k)=\alpha(k \cdot 1) = \sum_{i=1}^k \alpha(1)=k \cdot \alpha(1)$$
Therefore, any $\alpha(k)$ is completely determined by the value of $\alpha(1)$. We know that $|\alpha(1)|=10 \implies$ we must choose other elements from $\mathbb{Z}_{10}$ which also have the same order. 

In turn these must also be generators of this cyclic group, which in turn gives us the following choices:
$$\alpha_{1}, \alpha_{3}, \alpha_{9}, \alpha_{7}$$
We need to check that all of these outcomes are still [[Automorphism]]s of the group. 

The mapping given by $\alpha_{1}$ is the identity, so, we can confidently it is in the set of [[Automorphism]]s. We can further argue that the other sets are also [[Automorphism]]s. 

Consider $\alpha_{3}$. Since:
$$x\mod(10) = y \mod(10) \implies 3x \mod(10) = 3y \mod(10)$$
We have that $\alpha_{3}$ is "well-defined". Furthermore since $\alpha_{3}$ is a generator of $\mathbb{Z}_{10}$, it is onto (eventually we will exhaust every element in the set since it is a generator). And since $\mathbb{Z}_{10}$ is finite, $\alpha_{3}$ is $1$ to $1$. 

It is also the case that:
$$\large \alpha_{3}(a+b)=3(a+b)=3a+3b =\alpha_{3}(a)+\alpha_{3}(b)$$
Then we can say that $\alpha_{3}$ is an [[Automorphism]] $\implies \alpha_{3} \in \text{aut}(\mathbb{Z}_{10})$. 

By the same argument we can also say that $\alpha_{7},\alpha_{9} \in \text{aut}(\mathbb{Z}_{10})$. We can therefore conclusively write out the elements of this group:
$$\text{aut}(\mathbb{Z}_{10}) = \{ \alpha_{1},\alpha_{3},\alpha_{7},\alpha_{9} \}$$
We want to examine the structure of this [[Group]] as well. If we take $$\alpha_{3}^2=\alpha_{3}\alpha_{3}(1)=\alpha_{3}(3)=9=\alpha_{9}(1)$$
Similarly we also have that $\alpha_{3}^3=\alpha_{7}$ and $\alpha_{3}^4 = \alpha_{1}$ which gives us the result that $|\alpha_{3}|=4$ and that furthermore $\text{auto}(\mathbb{Z}_{10})$ cyclic group. 

We are also able to observe via Cayley Tables that $\text{aut}(\mathbb{Z}_{10}) \cong U(10)$:


| $U(10)$ | 1   | 3   | 7   | 9   |
| ------- | --- | --- | --- | --- |
| **1**   | 1   | 3   | 7   | 9   |
| **3**   | 3   | 9   | 1   | 7   |
| **7**   | 7   | 1   | 9   | 3   |
| **9**   | 3   | 7   | 3   | 1   |

| $\text{aut}(\mathbb{Z}_{10})$ | $\alpha_{1}$ | $\alpha_{3}$ | $\alpha_{7}$ | $\alpha_{9}$ |
| ----------------------------- | ------------ | ------------ | ------------ | ------------ |
| $\alpha_{1}$                  | $\alpha_{1}$ | $\alpha_{3}$ | $\alpha_{7}$ | $\alpha_{9}$ |
| $\alpha_{3}$                  | $\alpha_{3}$ | 9            | $\alpha_{1}$ | $\alpha_{7}$ |
| $\alpha_{7}$                  | $\alpha_{7}$ | $\alpha_{1}$ | $\alpha_{9}$ | $\alpha_{3}$ |
| $\alpha_{9}$                  | $\alpha_{9}$ | $\alpha_{7}$ | $\alpha_{3}$ | $\alpha_{1}$ |
Clearly then the two groups are isomorphic. 

---
# Theorem.) $\text{aut}(\mathbb{Z}_{n}) \cong U(n)$ where $n \in \mathbb{N}$.  
The [[Automorphism]]s $\alpha \in \text{aut}(\mathbb{Z}_{n})$ are determined by where $\alpha(1)$ maps to entirely. Furthermore, we also must have that $\alpha(1) \in  \text{aut}(\mathbb{Z}_{n})$. 

This allows us to write:
$$|\alpha(1)|=n=|1|$$
Now, let us consider the mapping from $T$ to $\text{aut}(\mathbb{Z}_{n})$ which is given by:
$$T(\alpha)=\alpha(1)$$
We want to show that our function $T$ is injective. Suppose that:
$$T(\alpha)=T(\beta) : \alpha(1)=\beta(1)$$
Let $k \in \mathbb{Z}_n$ then:
$$\alpha(k)=\alpha(k \cdot 1) = k \cdot \alpha(1)=k \cdot \beta(1) = \beta(k)$$
Which gives us that $\alpha = \beta$.  Thus $T$ is injective.

We want to show that $T$ is onto as well. Let $r \in U(n)$, and consider the mapping given by:
$$\alpha : \mathbb{Z}_{n} \to \mathbb{Z}_{n} : \alpha(s)=sr \mod(n)$$
For $s=1$, then $\alpha(1)=r$, and since $r \in U(n) \implies r$ is a generator of the group. Hence, $\alpha$ is clearly onto. 

We also have that:
$$\alpha(s+t)=\alpha(s)+\alpha(t) \mod(n)$$
Therefore, $\alpha$ is clearly an [[Automorphism]]. If we refer back to the mapping then we see now that: 
$$T(a)=\alpha(1)=r$$
And thus, $T$ is onto $U(n)$ since it hits every relatively prime number since each relatively prime number to $n$ is a generator of $\mathbb{Z}_{20}$. 

It can also be shown that $T$ is operation preserving. Let $a,b \in \text{aut}(\mathbb{Z}_{n})$. Then:

$$T(\alpha \beta)=(\alpha \beta)(1)= \alpha(\beta(1)) = \left(  \sum_{i=1}^{\beta_{1}}\alpha(1) \right)=\alpha(1) \beta(1)=T(\alpha)T(\beta)$$
Thus, $T$ is an [[Isomorphism]] between $\text{aut}(\mathbb{Z}_{n}) \mapsto \mathbb{Z}_{20}$. 



