---
title: Ring Homomorphism
tags:
  - AbstractAlgebra
draft: "False"
---
# Ring Homomorphism Definition
A [[Ring Homomorphism]] $\phi$ from a [[Ring]] $R$ to a ring $S$ is a mapping that preserves the [[Binary Operation]]s for both multiplication and addition. That is to say:
$$\phi(a+b)=\phi(a)+\phi(b)$$
$$\phi(ab)=\phi(a)\phi(b)$$
Notice that these are the properties of [[Homomorphism]]s generally. If this function is [[bijective]] then it follows that it is a [[Ring Isomorphism]]. 

---
# Examples

### Example 1.)
For any $n \in \mathbb{N}$ the mapping $\mathbb{Z}\to \mathbb{Z}_{n}$ given $k\to k \mod(n)$ is a ring homomorphism from $\mathbb{Z}$ onto $\mathbb{Z}_{n}$. This is called the "natural homomorphism" from $\mathbb{Z}\to \mathbb{Z}_{n}$. 

For addition:
$$\begin{align}
\phi(a+b)=(a+b)\mod(n)=(nk_{1}+r_{1})+(nk_{2}+r_{2}) \mod(n)=(r_{1}+r_{2}) \mod(n) \\
=(r_{1})\mod(n) +(r_{2}) \mod(n)=(r_{1}+nk_{1})\mod(n) +(r_{2}+nk_{2}) \mod(n) \\
=(a)\mod(n)+(b)\mod(n) = \phi(a)+\phi(b)
\end{align}$$
For multiplication:
$$\begin{align}
\phi(a \cdot b)=(a\cdot b)\mod(n)=(nk_{1}+r_{1}) \cdot (nk_{2}+r_{2}) \mod(n)=(r_{1} \cdot r_{2}) \mod(n) \\
=(r_{1})\mod(n)  \cdot (r_{2}) \mod(n)=(r_{1}+nk_{1})\mod(n)  \cdot (r_{2}+nk_{2}) \mod(n) \\
=(a)\mod(n) \cdot (b)\mod(n) = \phi(a) \cdot \phi(b)
\end{align}$$
The map is trivially onto for addition by definition of modulus.

### Example 2.) 
The mapping $\phi:\mathbb{C}\to \mathbb{C}$ where $z \in \mathbb{C}, z\mapsto \bar{z}$. 

Let $a,b \in \mathbb{C}$ be arbitrary. 
$$\begin{align}
\phi(a+b)=\overline{a+b}=\overline{(a_{1}+a_{2}i)+(b_{1}+b_{2}i)} \\
=(a_{1}-a_{2}i)+(b_{1}-b_{2}i)=(a+b_{i})
-(a_{1}+b_{2})i \\
=(a_{1}-a_{2}i)+(b_{1}-b_{2}i)=\phi(a)+\phi(b)
\end{align}$$
$$\begin{align}
\phi(a b)=\overline{ab}=\overline{(a_{1}+a_{2}i)(b_{1}+b_{2}i)} \\
=(a_{1}-a_{2}i)(b_{1}-b_{2}i)=\phi(a)\phi(b)
\end{align}$$
Thus $\phi$ is a homomorphism. 

### Example 3.)
The mapping $p(x)\to p(1)$ is a ring homomorphism from $\mathbb{R}[x]$ onto $\mathbb{R}$. 

It can easily be shown to be a ring homomorphism. Let $p(x),q(x) \in \mathbb{R}[x]$. Then we can evaluate the following:

For addition:
$$\begin{align}
\phi(p(x)+q(x))=\phi((p+q)(x)) = (p+q)(1) \\
=p(1)+q(1)=\phi(p(x))+\phi(q(x))
\end{align}$$
For multiplication:
$$\phi(p(x)q(x))=\phi(pq(x))=pq(1)=p(1)\cdot q(1)= \phi(p(x))\phi(q(x))$$

It is trivially onto $\mathbb{R}$, let $p(x)=x$. 

### Example 4.)
Find all non-zero ring homomorphisms from $\mathbb{Z}_{10}\to \mathbb{Z}_{20}$ and then from $\mathbb{Z}_{20} \to \mathbb{Z}_{10}$. 

We can begin by considering homomorphisms from $\mathbb{Z}_{20}\to \mathbb{Z}_{10}$. By properties of homomorphisms, we require that $|\phi(\mathbb{Z}_{10})| \bigg|10$. 

Thus, $\phi(\mathbb{Z}_{10})$ must be of order $10,5,2$, and not $1$ since this would result in the zero homomorphism. 

If $\phi:R\to S$ is a ring homomorphism and $R$ has a multiplicative unity, then we must have that:
$$a=\phi(1)=\phi(1)\cdot \phi(1)=a^2 \implies a^2=a$$
Such an element here is called idempotent of $S$. 

In order to determine homomorphisms here we need to be able to find all idempotent elements of the form $a=\phi(1) \in \mathbb{Z}_{20}$. 

Since $a=\phi(1) \in \phi(\mathbb{Z}_{10})$