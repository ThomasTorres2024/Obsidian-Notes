---
title: Characteristic (Ring Theory)
tags:
  - AbstractAlgebra
draft: "False"
---
# Characteristic ([[Ring]]) 
Note that for any $a+bi \in \mathbb{Z}_{3}[i]$ that $3(a+bi)=3a+3bi=0$ since we are working with mod $3$. 

In the subring $\{ 0,3,6,9\} \subseteq \mathbb{Z}_{12}$ we have that $4x=0$ for any $x$ in the subring. 

---
# Definition.) __Characteristic of a ring $R$__ 
The characteristic of a ring $R$ is the least positive integer $n \in \mathbb{N}$ such that $nx=0, \forall x \in R$. If no such integer $n$ exists, then we say that $R$ has characteristic $0$. We denote the characteristic of $R$ by $\text{char}(R)$. 

For instance, $\text{char}(\mathbb{Z})=0$ and $\text{char}(\mathbb{Z}_{n})=n$. 

---
# Theorem.) Characteristic of a Ring with Unity 
Let $R$ be a ring with unity $1$. If $1$ has infinite order under addition, then $\text{char}(R)=0$, if the [[Order]] of $1$ is $n$ under addition, then the characteristic of $R$ is $n$. 

$Proof.)$
If $1$ has infinite order, there is no positive integer $n$ such that $n\cdot1=0$, which results in $\text{char}(R)=0$. 

Suppose now that $1$ has order $n$ under $1$ and that $n\cdot1=0$ and $n$ is minimal. Then, for any $x \in R$ we have that: 
$$n \cdot x = n\cdot (1 \cdot x) = (n \cdot 1) \cdot x = 0 \cdot x = 0$$
This would not work for any smaller $n$ and relies on minimality, which gives the desired result. 

---
