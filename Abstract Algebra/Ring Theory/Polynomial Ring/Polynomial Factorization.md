---
title: Polynomial Factorization
tags:
  - AbstractAlgebra
draft: "False"
---
### Definition). "Content"
The "Content" of a [[Polynomial]] for the polynomial $p(x)=\sum_{j=0}^n \alpha_{j}x^j$ is the greatest common divisor of the integers $\alpha_{n},\dots,\alpha_{0}$. 

### Definition). "Primitive Polynomial"
A primitive polynomial is an element of $\mathbb{Z}[x]$ with content $1$.  

### Gauss's Lemma 
Gauss's Lemma states that the product of two primitive polynomials is itself primitive. 

$Proof).$ 
Let $f(x),g(x)$ be polynomials that are primitive. BWOC assume $f(x)g(x)$ is not prime, thus we can assume that there is some prime $p$ such that $p$ is a factor of this polynomial. Now consider the following:
$$\begin{align}
\overline{f(x)} = f(x) \text{ mod}(p) \quad \quad   \overline{g(x)} = g(x) \text{ mod}(p) \\
 \overline{f(x)g(x)}= f(x)g(x) \text{ mod}(p)
\end{align}$$
Notice that $\overline{f(x)},\overline{g(x)},\overline{f(x)g(x)} \in \mathbb{Z}_{p}[x]$, which is an [[Integral Domain]] since $p$ is a prime. Then we have the following:
$$\overline{f(x)} \cdot \overline{g(x)} = \overline{f(x)g(x)} = 0 $$
Since we are over an integral domain then $f(x)=0 \lor g(x)=0$. This means that either one of $f,g$ has coefficients which are a multiple of $p$ and are thus composite which contradicts the fact $f,g$ are primitive $\therefore$ 

### Theorem). 
Reducibility over $\mathbb{Q} \implies$ reducibility over $\mathbb{Z}$. 

$Proof).$ 
Suppose that $f(x)=g(x)h(x)$ where $g(x),h(x) \in \mathbb{Q}[x]$.  Assume $f(x)$ is primitive (we can divide both $f(x),g(x)$ by the content of $f(x)$).

Let $a$ be the LCM of the denominators of the coefficients of $g(x)$ and $b$ be the LCM of the denominators of the coefficients of $h(x)$. 

Then:
$$abf(x)=ag(x) \cdot bh(x) $$
And thus we have that $ag(x),bh(x) \in \mathbb{Z}[x]$. Let $c_{1}$be the content of $ag(x)$ and let $c_{2}$ be the content of $bh(x)$. Then:
$$ag(x)=c_{1}g(x) \quad bh(x)=c_{2}h_{1}(x)$$ where both $g_{1}(x),h_{1}(x)$ are primitive and $abf(x)=c_{1}c_{2}g_{1}(x)h_{1}(x)$.Since $f(x)$ is primitive, then its content must be $ab$. Secondly, since the product of primitive polynomials is also primitive, then the content of $c_{1}c_{2}g_{1}(x)$ is thus $c_{1}c_{2}$. Therefore $ab=c_{1}c_{2}$ and $f(x)=g_{1}(x)h_{1}(x)$ for $g_{1}(x),h_{1}(x) \in \mathbb{Z}[x]$ 
and $\text{deg}(g_{1}(x))=\text{deg}(g(x))$ and $\text{deg}(h_{1}(x))=\text{deg}(h(x))$

We are able to cancel out the $ab$ and $c_{1}c_{2}$ and obtain our result over the integers, which concludes the proof. 

#### Example).
Let $f(x)=6x^2+x-2=\left( 3x-\frac{3}{2} \right)\left( 2x+\frac{4}{3} \right) =g(x)h(x)$. Then here we have that $a=2,b=3 \implies c_{1}=3,c_{2}=2$ and then $g_{1}(x)=2x-1$ and $h_{1}(x)=3x+2$. This finally gives us:
$$\begin{align}
2\cdot3 (6x^2 + x -2)=3\cdot 2(2x-1)(3x+2) \\
6x^2+x-2=(2x-1)(3x+2)
\end{align}$$

---
# Irreducibility Tests 
### Theorem).
Let $p$ be a [[Prime]] and suppose that $f(x) \in \mathbb{Z}[x]$ with $\text{deg}(f(x))\geq1$. Let $f(x)$ be the polynomial in $\mathbb{Z}_{p}[x]$ obtained by reducing all coefficients of $f(x) \text{ mod}(p)$. If $f(x)$ is irreducible over $\mathbb{Z}_{p}$ and $\text{deg}(f(x))=\text{deg}(\overline{f(x)})$, then $f(x)$ is irreducible over $\mathbb{Q}$. 

$Proof).$ 
From the above theorem, if $f(x)$ is reducible over $Q$ then $f(x)=g(x)h(x)$ with $g(x),h(x) \in \mathbb{Z}[x]$ s.t. $h,g$ have degrees less than that of $f$. 