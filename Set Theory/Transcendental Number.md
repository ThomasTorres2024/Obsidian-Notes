---
title: Transcendental Numbers
draft: "False"
tags:
  - Set_Theory
---
 # Definition of [[Transcendental Number]] 
A number is defined as being Algebraic if it is the root of:
$$\sum_{i=0}^n a_{i}^i x^i: a_{i} \in \mathbb{Z}$$
For instance, $x+2=0 \implies -2 \in \mathbb{A},x^2+1=0 \implies i \in \mathbb{A}$.  A transcendental number is not Algebraic, meaning that it cannot be written as the root of a polynomial of the above form. 

We define the set of transcendental numbers, $\mathbb{T}$, as such:
$$\mathbb{T}=\mathbb{R} \textbackslash \{ x \in \mathbb{C}  : \exists P \in \mathbb{Q}[X],P \neq 0, P(x)=0  \} $$
Thus we have that: 
$$x \not \in \mathbb{A} \iff x \in \mathbb{T} $$

The Lindemann-Weirstrass Theorem guarantees that for $\alpha \not \in \mathbb{T}$, which is to say that:
$$e^1,e^2,\cdots,e^\sqrt{ 2 },e^\sqrt{ 3 } \in \mathbb{T}$$

This allows to prove that $\pi$ is a transcendental number BWOC.

$Proof.)$
Assume that $\pi \in \mathbb{A}$. Since $i \in \mathbb{A}$, then $\pi i \in \mathbb{A}$ since $\mathbb{A}$ is a [[Field]]. But, by [[Euler's Identity]] we have that:
$$e^{i\pi}=-1 \in \mathbb{T}$$
Which should be true via the Lindemann-Weirstrass Theorem, but this is a contradiction since clearly $-1 \in \mathbb{A}$, $\therefore \pi \in \mathbb{T}$. 

---
# Gelfond-Schneider Theorem 
If $a \in \mathbb{A}$ and $a \neq 0, a \neq 1$ and $b \in \mathbb{A}\textbackslash \mathbb{Q}$, then, $a^b \in \mathbb{T}$