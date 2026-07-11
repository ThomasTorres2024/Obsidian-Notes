---
draft: "False"
title: Polynomial Division Algorithm
tags:
  - AbstractAlgebra
  - RingTheory
---
# Polynomial Division Algorithm
The [[Polynomial Division Algorithm]] states that for all $f(x),g(x) \in k[x]$ where $k$ is a [[Field]] and $k[x]$ is a [[Polynomial Ring]], that there is a unique $q(x),r(x)$ such that:

$$f(x)=q(x)g(x)+r(x)$$

Where the degrees of $r(x)$ and $g(x)$ satisfy:
$$0\leq \text{deg}(r(x))<\text{deg}(g(x))$$

### Corollary 1). The Remainder Theorem
Let $F$ be a [[Field]] and $a \in F,f(x) \in F[x]$. Then, $f(a)$ is the remainder of the division of $f(x)$ by $x-a$. 

$Proof.)$ 
Applying the division algorithm, we get $q(x)=\frac{f(x)}{x-a}$ and $r(x)$ such that $\text{deg}(r(x))<\text{deg}(x-a)$. Thus, $\text{deg}(r(x))=0$ so it is some constant in $F$, we obtain: 

$$\begin{align}
q(x)(x-a)+r(x)=f(x)  \\
\implies q(a)(a-a)+r(a)=f(a) \\
\implies r(a)=f(a)
\end{align}$$
Since $r(a)$ is constant then $r(a)=f(a)=r(x) \quad \forall x \in F$. 
### Corollary 2). Factor Theorem
Let $F$ be a [[Field]], $a \in F, f(x)\in F[x]$ then $a$ is a zero of $f(x) \iff (x-a)$ is a factor of $x-a$. 

$1.) \implies$
Here we assume that $a$ is a $0$ of $f$, which means that $f(a)=0$. 

We can consider the division algorithm of $f(x)$ here dividing by $x-a$, we then obtain that: 
$$f(x)=q(x)(x-a)+r(x)$$
Such that $\text{deg}(r(x))<1=\text{ deg}(x-a)$. So $r(x)$ is constant. Applying the above remainder theorem we get that $f(a)=r(a)=0 \implies r(x)=0 \quad \forall x$ which entails that $r(x)=0$. 

Therefore, $x-a$ factors $f(x)$.

$2.) \Longleftarrow$
Here we assume that $(x-a)$ is a factor of $f(x)$ which is to say that $\exists g(x) \in F[x]$ such that $g(x)(x-a)=f(x)$.

Then, if $x=a \implies f(a) \implies a$ is a $0$ of $f$. 