---
title: Integral Domain
tags:
  - AbstractAlgebra
draft: "False"
---
# Integral Domain
We can think of [[Integral Domain]]s as [[Ring]]s which are more like $\mathbb{Z}$ than general rings. That is to say that these rings as being commutative, having multiplicative identities, and cancellation laws. 

---
# Definition [[Integral Domain]]
An [[Integral Domain]] is a commutative [[Ring]] with an [[Identity Element]] and no [[Zero Divisor]]s. Thus, if $R$ is an integral domain, then $ab=0 \implies a=0 \lor b=0$ or both. 

---
# Examples 
### Example 1.) $\mathbb{Z}$ is an Integral Domain 
Trivial, properties of this Ring are already discussed above. 

### Example 2.) Gaussian Integers 
The Gaussian Integers are defined by:
$$\mathbb{Z}[i]=\{ a+bi : a,b \in \mathbb{Z}, i^2=-1 \}$$
Is another integral domain. This comes from the fact that $\mathbb{Z}$ itself is an [[Integral Domain]].  

### Example 3.)
The [[Polynomial Ring]] $\mathbb{Z}[x]$ is an [[Integral Domain]]. 

### Example 4.) 
The ring $\mathbb{Z}[\sqrt{ 2 }]=\{ a+b \sqrt{ 2 } : a,b \in \mathbb{Z} \}$. 

### Example 5.) 
$\mathbb{Z}_{p}$ is an integral domain if $p$ is a prime number. 

### Example 6.)
$\mathbb{Z}_{n}$ is __not__ an integral domain if $n$ isn't prime. For example if $n=4$ then $4^2=16=0$. 

### Example 7.)
$\mathbb{Z}^{2 \times 2}$ is __not__ an integral domain. Consider the family of nilpotent matrices for instance. There are numerous counter examples in the wild. 

### Example 8.)
$\mathbb{Z} \oplus \mathbb{Z}$ is not an integral domain. Consider $(1,0) \cdot(0,1)=(0,0)$. Therefore not an integral domain. 

---
# Theorem.) Cancellation Under Integral Domains
Integral domains are nice to work with since they permit cancellation of non-zero elements under multiplication. If $a,b \in \mathbb{R}$ and if $a\neq_{0}$ and $ab=ac$ then we have that $b=c$. 

$Proof.)$ 
Starting with $ab=ac$ we get that:
$$\begin{align}
ab-ac=0 \\
a(b-c)=0
\end{align}$$
Since $a\neq 0$ then it must be the case that $b-c=0 \implies b=c$. 

---
# Fields 
Every [[Field]] is an [[Integral Domain]]. Every non-zero element in a field is a unit. 

If $F$ is a field and $a,b \in F$ with $a\neq 0$ and $ab=0$, then by left multiplication we can obtain that: 
$$\begin{align}
ab=0 \\
\iff a^{-1}ab=a^{-1}0 \\
\iff b=0
\end{align}$$
Hence a field has no zero divisors, is commutative, and has an identity element, therefore every field is an [[Integral Domain]]. 

---
# Theorem). Finite Integral Domains are Fields 
A finite integral domain is a field. 
$Proof.)$ Let $D$ be a finite integral domain with identity $1$, and let $a\neq 0, a \in D$. It needs to be shown that $a$ is a unit. 

Consider the set $aD=\{ ab: b \in D  \}$. This is a subset of $D$ and also gives that $ab=ac \implies b=c$, and thus $aD$ has as many elements as $D$ since there is such a correspondence. 

Using the fact that $D$ is finite, since $D$ is finite we know that $aD=d$ and thus $\exists b \in D$ such that $ab=1$, and thus we conclude with our desired result. 

---
## Corollary). $\mathbb{Z}_{p}$ is a field 
For every prime $p$, $\mathbb{Z}_{p}$, the ring of integers modulo $p$ is a field. 

$Proof.)$ 
By the above theorem, since $\mathbb{Z}_{p}$ is known to be commutative with respect to multiplication and addition, and that it has the identity element $1$, then all we need to show is that it has no [[Zero Divisor]]s. 

Suppose that $a,b \in \mathbb{Z}_{p}$ and $ab=0$, then $ab=pk$ for some $k \in \mathbb{Z}$. By Euclid's lemma, then either $p \bigg|a$ or $p\bigg|b$. Thus in $\mathbb{Z}_{p}$ either $a=0$ or $b=0$ which entails that there are no $0$ divisors over $\mathbb{Z}_{p}$, and that it thus is a field. 

---
#  Theorem.) Characteristic of an [[Integral Domain]]
The characteristic of an integral domain is either $0$ or prime. 

$Proof.)$
By the above proof, it suffices to show that if the multiplicative identity of $1$ has finite order, then it must be prime. 

Suppose that $1$ has order $n$ and that $n=st$ where $1\leq s,t\leq n$, then:
$$\begin{align}
0 = n \cdot 1=(st) \cdot1 = (st) \cdot 1 \cdot 1 \\
= s \cdot 1 \cdot t\cdot 1 \\
= (s \cdot 1 )(t \cdot 1)
\end{align}$$
Since $R$ is an [[Integral Domain]] then either $s\cdot1 = 0$ or $t\cdot1=0$. Since $n$ is the smallest positive integer with $n\cdot1=1$, then either $s=n$ or $t=n$ is prime as desired. 
