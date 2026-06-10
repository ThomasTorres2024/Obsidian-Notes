---
title: Maximal Ideal
tags:
  - AbstractAlgebra
draft: "False"
---
# Maximal Ideal
# Prime Ideal 
A [[Maximal Ideal]] is an [[Ideal (Rings)]] of a commutative [[Ring]] $R$ is a proper ideal of $R$ such that whenever $B$ is an ideal of $R$ and $A \subseteq B \subseteq R$ then $B=A$ or $B=R$. 

The only ideal which properly contain a maximal ideal that can properly contain a maximal ideal is $R$ itself. 

---
### Example 1.)
The lattice of ideals of $\mathbb{Z}_{36}$, where $\langle 2 \rangle$ and $\langle 3 \rangle$ are maximal ideals. Arrows here denote inclusion. 

![[name.png]]
### Example 2.)
The ideal $\langle x^2+1\rangle$ is maximal in $\mathbb{R}[x]$. Suppose $A$ is an ideal of $\mathbb{R}[x]$, which properly contains $\langle x^2+1\rangle$. 

__Claim 1.)__ 
We claim that $\exists$ a non-zero real number $c$ which belongs to $A$. Let $f(x)\in A$ but $f(x)\not \in \langle x^2+1\rangle$. 

Then by the polynomial division algorithm we obtain:
$$f(x)=q(x)(x^2+1)+r(x)$$
Where $q(x),r(x)$ are polynomials where $r(x)\neq0$ and $0\leq \text{deg}(r(x))\leq1$.

Then, $r(x)=ax+b$ where $a,b$ are both not $0$. Then:

$$\begin{align}
ax+b=r(x)
=f(x)-q(x)(x^2+1)\in A\end{align}$$
Thus, $ax^2-b^2=(ax+b)(ax-b)\in A$ via absorbing properties, and $a^2(x^2+1)\in \langle x^2+1 \rangle \subseteq A$. 

Hence, $0\neq a^2+b^2 = (a^2x^2+a^2)-(a^2x^2-b^2) \in A$. And thus claim $1$ follows with $c=a^2+b^2$

__Claim 2.__
$A=\mathbb{R}[x]$. In this case, we would be done. Since $c\neq0 \in A$, and $A$ is an ideal, then $\frac{1}{c} \cdot c = 1 \in A$. 

If $p(x)$ is any polynomial in $\mathbb{R}[x]$, and since $1\in A$ then $p(x) \cdot 1 \in A$, thus $A=\mathbb{R}[x]$. 

---
# Corollary.) Maximal Ideals are Prime
Let $R$ be a commutative ring with unity and let $A$ be a proper ideal of $R$. Then, if $A$ is a [[Maximal Ideal]] then it must also be a [[Prime Ideal]]. 

We can use the result for [[Quotient Group]]s which states that if $\frac{R}{A}$ where $A$ is a proper ideal of $R$ forms a [[Field]] iff $A$ is a maximal ideal.  Secondly, we know that every field is an integral domain, and that $\frac{R}{A}$ is an integral domain $\iff A$ is prime. 

The result holds that $A$ is both prime and maximal. 