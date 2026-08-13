---
title: Irreducible Polynomial
tags:
  - AbstractAlgebra
draft: "False"
---
# Irreducible Polynomial 
Let $D$ be an [[Integral Domain]], a polynomial $f(x) \in D[x]$ s.t. $f(x)\neq0$ and $f(x)$ is not a unit is said to be an [[Irreducible Polynomial]] over $D$ if when $f(x)$ is expressed as a product $f(x)=g(x)h(x)$, then $g(x)$ or $h(x)$ is a [[Unit (Ring Theory)]] over $D[x]$. A non-zero nonunit element of $D[x]$ that is not irreducible over $D$ is called reducible. 

### Examples). 
* $f(x)=2x^2+4$ is irreducible over $\mathbb{Q}$, but it is over $\mathbb{Z}$ since $2(x^2+4)=f(x)$ where $2$ is not invertible and neither is $x^2+4$ so both are non-unit
* $f(x)=2x^2+4$ over $\mathbb{R}$, but reducible over $\mathbb{C}$. 
* $f(x)=x^2-2$ irred. over $\mathbb{Q}$ but not on $\mathbb{R}.$
* $f(x)=x^2+1$ is irreducible over $\mathbb{Z}_{3}$ but not over $\mathbb{Z}_{5}$. 
Generally determining if a polynomial is reducible over an [[Integral Domain]].  Some cases, however, make it easier. 

### Theorem). 
Let $F$ be a [[Field]], if $f(x) \in F[x]$ and $\text{deg}(f(x))=2,3$ then $f(x)$ is reducible over $F$ iff $f(x)$ has a zero in $F$. 

$Proof).$ 
Suppose $f(x)=g(x)h(x)$, where $g(x),h(x) \in F[x]$ and $\text{deg}(f(x)),\text{deg}(g(x)) \leq f(x)$ s.t. $\text{deg}(h(x))+\text{deg}(g(x))=\text{deg}(f(x))$. 

Since $f(x)$ is degree $2,3$ then at least one of $g(x),h(x)$ is degree 1. So, $g(x)=ax+b \implies -a^{-1}b$ is a zero of $g(x) \implies$ zero of $f(x)$ too. 

This theorem is particularly easy to check over finite fields, especially $\mathbb{Z}_{p}$. If for $a \in \mathbb{Z}_{p}$ we have that $f(a)=0$ for $a=0,1,\dots,p-1$ then we have that $a$ is a zero of $f$. 

Secondly, a polynomial may be reducible even if it has no zeroes and is above degree $3$, namely consider the example $x^4+2x^2+1=(x^2+1)^2$. This has no zeroes in $\mathbb{Q}$, but yet the above factorization holds. 