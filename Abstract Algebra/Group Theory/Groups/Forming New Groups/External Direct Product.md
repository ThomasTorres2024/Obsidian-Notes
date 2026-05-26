---
title: External Direct Product
tags:
  - AbstractAlgebra
draft: "False"
---
# External Direct Product

We can generate a new [[Group]] by an operation called the [[External Direct Product]], by taking a set of groups, $G_i$ where we have $n$ many groups and $1 \leq i \leq n$. We define the external product, by using $\oplus$ as the following:

$$\bigoplus_{i=1}^nG_{i} = \{ (g_{1},g_{2}, \dots, g_{n}) : g_{i} \in G_{i}, 1 \leq i \leq n  \} $$

We can look at this as a [[Group]] by taking elements from each $i$th group. The [[Binary Operation]] here is doing the binary operation of each respective group with itself, for example:

$$(g_{1},g_{2},\dots, g_{n}) (g_{1}',g_{2}',\dots , g_{n}')=(g_{1}+_{G_{1}} g_{1}',g_{2} +_{G_{2}} g_{2}',\dots , g_{n} +_{G_{n}}  g_{n}')$$

If each $G_i$ is finite, then the [[Order]] of the external direct product of the groups is:

$$\left|\bigoplus_{i=1}^n G_{i} \right|= \prod_{i=1}^n |G_{i}|$$

Which is infinite in the case of some $|G_i|=\infty$. 

The idea here is quite similar to that of [[Isomorphic Vector Spaces]]. For instance, we can say that $\mathbb{R}^2 = \mathbb{R} \oplus \mathbb{R}$, which is to say that $\mathbb{R}^2 \cong \mathbb{R} \oplus \mathbb{R}$ (actual equality is the result of the Internal Direct Product).

---
### Example 1.)
$U(8) \oplus U(10)$ then:

$$\begin{align} U(8) \oplus U(10) =   \\ \\


\{ (1,1), (1,3), (1,7),(1,9), \\ 
(3,1),(3,3),(3,7),(3,9), \\
(5,1),(5,3),(5,7),(5,9), \\
(7,1),(7,3),(7,7),(7,9)  \}
\end{align} $$

---
### Example 2.)
$\mathbb{Z}_{2} \oplus \mathbb{Z}_{3}$ then:

$$\begin{align} \mathbb{Z}_{2} \oplus \mathbb{Z}_{3} =   \\ \\


\{  (0,0),(0,1),(0,2) \\
(1,0),(1,1),(1,2) \}
\end{align} $$
This is an Abelian group, notice that:
$$\mathbb{Z}_{2} \oplus \mathbb{Z}_{3  }=\langle (1,1) \rangle$$
And therefore:
$$\mathbb{Z}_{2} \oplus \mathbb{Z}_{3  } \cong \mathbb{Z}_{6}$$
---
# Example.) Classification of Groups of Order $4$ 
We can show that any group of order $4$ is either Isomorphic to $\mathbb{Z}_{4}$ or $\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$. These groups are not Isomorphic to one another $\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$ is not cyclic and $\mathbb{Z}_{4}$ is cyclic. 

The strategy for proving this result is to show that the [[Cayley Table]] of $G$ has either one of two valid forms. being the two aforementioned groups (this is similar to the proof that groups of order $2p$ for prime $p$ are either isomorphic to the dihedral group or are the cyclic group $2p$). 

Clearly if $G$ has an element of order $4$ then $\mathbb{Z}_4 \cong G$. Now we need to show the other case.   

By Lagrange's theorem, all elements of $G$ have order $1$ or order $2$. If $a,b$ are two non-identity elements of $G$. Only the identity element can have order $1$. 

Let $a,b$ be two non-identity elements of $G$. Since $a,b$ both have order $2$ then it follows that:

$$a=a^{-1}, b=b^{-1}$$

Since $a\neq b$ and $a=a^{-1},b=b^{-1}$ then $ab \neq e$. Thus we have that:

$$G=\{e,a,b,ab \}$$
And that $|ab|=2$, and thus every element has order $2$. Also note that $G$ is abelian since $ab=(ab)^{-1}=b^{-1}a^{-1}=ba$. And this is enough to determine the [[Cayley Table]] of $G$.  

---
# Properties of External Direct Products 

## Theorem (8.1) Order of an Element in a Direct Product 

The [[Order]] of an element in a [[External Direct Product]] of a finite number of groups is the LCM of the order of each component of the element. For instance the following element has the following order:

$$\large |(g_{1},g_{2},\dots, g_{n})|= \text{LCM}( |g_{1}|,|g_{2}|,\dots,|g_{n}| )$$
### $Proof.$ 
For each $1 \leq i \leq n$, let $e_i$ be the identity element of $G_i$. Let:

$$s= \text{LCM}( |g_{1}|,|g_{2}|,\dots,|g_{n}| ), t= |(g_{1},g_{2},\dots, g_{n})|$$

Since $s$ is a multiple of $|g_i|$ for each $i$ we know that:

$$\large (g_{1},g_{2},\dots,g_{n})^s = (g_{1}^s,g_{2}^s,\dots,g_{n}^s) =  (e_{1},e_{2},\dots,e_{n}) $$

On the other hand we also know that:

$$\large (g_{1},g_{2},\dots,g_{n})^t = (g_{1}^t,g_{2}^t,\dots,g_{n}^t) =  (e_{1},e_{2},\dots,e_{n}) $$

We also know that $|g_{i}| \bigg| t : \forall i$. Since by definition $t$ must be as small as possible, it must be the case that $t=s$. 

---
# Example 4.) 

All of the following groups have order $100$, but none are pairwise isomorphic:

$$\begin{align}
\mathbb{Z}_{100} \quad \mathbb{Z}_{25} \oplus \mathbb{Z}_{1} \oplus \mathbb{Z}_{2} \\ \\

\mathbb{Z}_{5} \oplus \mathbb{Z}_{5} \oplus \mathbb{Z}_{4} \\ \\

\mathbb{Z}_{5} \oplus \mathbb{Z}_{5} \oplus \mathbb{Z}_{2} \oplus \mathbb{Z}_{2} \\
 \\
D_{50} \quad D_{10} \oplus  \mathbb{Z}_{5} \quad D_{5} \oplus \mathbb{Z}_{5}  
\end{align}$$

We can begin by examining the following groups and examining which has the element of largest order in each:

1. $\mathbb{Z}_{100}$ max order $100$ 

2. $\mathbb{Z}_{25} \oplus \mathbb{Z}_{1} \oplus \mathbb{Z}_{2} \quad D_{50}$ max order $50$ 

3. $\mathbb{Z}_{5} \oplus \mathbb{Z}_{5} \oplus \mathbb{Z}_{4}$ max order $20$ 

4. $\mathbb{Z}_{5} \oplus \mathbb{Z}_{5} \oplus \mathbb{Z}_{2} \oplus \mathbb{Z}_{2} \quad D_{10} \oplus \mathbb{Z}_{5}$ max order $10$ 

5. $D_{5} \oplus D_{5}$ max order $5$

Since the maximum element in each of these categories is different then we know that of another category we just need to show that there is no Isomorphism between anything in each category. 

In $2.)$ we have that $\mathbb{Z}_{25} \oplus \mathbb{Z}_{1} \oplus \mathbb{Z}_{2}$ is an Abelian group and $D_{50}$ is __not__ Abelian.
In $4$ we also have that $\mathbb{Z}_{5} \oplus \mathbb{Z}_{5} \oplus \mathbb{Z}_{2}$ is Abelian and $D_{10} \oplus \mathbb{Z}_{5}$ is __not__ Abelian. 

It can also be shown that these two sets of groups are not isomorphic by counting the number of elements of order $10$ in each group. 

$\mathbb{Z}_{5} \oplus \mathbb{Z}_{5} \oplus \mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$ has $(5^2-1)(3^2-1)=48$ elements of order $10$, while $D_{10} \oplus \mathbb{Z}_{5}$ has $64$ elements of order $10$ 

---
# Example 5.) 

Let $m,n \in \mathbb{N}$ both be divisible by $5$. We want to find the number of elements of order $5$ in $\mathbb{Z}_{m} \oplus \mathbb{Z}_{n}$. We need to find the number of elements that satisfy:

$$5=|(a,b)| = \text{lcm}(|a|,|b|)$$

From this we obtain that either $|a|=1$ or $5$ and $|b|=1$ or $|b|=5$, but not $|a|=|b|=1$.  

By theorem $4.3$ we have that $\mathbb{Z}_{m}$ and $\mathbb{Z}_{n}$ each have exactly one subgroup of order $5$, namely:

$$\langle a^{m/5} \rangle, \langle b^{n/5} \rangle $$

We have $5$ different choices here for $a^{m/5}$ and $b^{n/5}$, namely $a^{m/5},a^{2m/5},a^{3m/5},a^{4m/5},\dots, a^{0}$ and $b^{m/5},b^{2m/5},b^{3m/5},b^{4m/5},\dots, b^{0}$. We thus have $5 \cdot 5$ many choices, and then the identity element which overlaps in each group and cannot be twice counted, and thus we get $25-1=24$ many possibilities. 

For $m,n \in \mathbb{N}$ are divisible by some prime number $p$, then we have that there are $p^2-1$ many elements of this order. 

---
### Example 6.) 

How many cyclic subgroups of order $10$ are in $\mathbb{Z}_{150} \oplus \mathbb{Z}_{50}$, which has $7500$ elements?

We can begin by counting the number of elements of order $10$. We have that:

$$10=|(a,b)|=\text{lcm}(|a|,|b|)$$

Which means that $a$ and $b$ must be a valid combination of $1,2,5,10$. The unique subgroup of $\mathbb{Z}_{150}$ of order $10$  is $\langle 15 \rangle$ and in $\mathbb{Z}_{50}$ is $\langle 5 \rangle$. 
.
Therefore, any such $(a,b) \in \langle 15 \rangle \oplus \langle 5 \rangle \cong \mathbb{Z}_{10} \oplus \mathbb{Z}_{10}$. We can thus find the number of elements of order $10$ in $\mathbb{Z}_{150} \oplus \mathbb{Z}_{50}$ by finding the number of elements in $\mathbb{Z}_{10} \oplus \mathbb{Z}_{10}$. 

From earlier, we know that $5^2-1$ there are $24$ elements of order $5$, and we have that there are $2^2-1=3$ many elements of order $2$, and of course only $1$ element of order $1$, which leaves $72$ elements of order $10$ from:

$$100-24-3-1=0$$

By theorem 4.4 we have that every cyclic subgroup of order $10$ has $\phi(10)=\phi(5)\phi(2)=4$ many elements of order $10$. Distinct cyclic subgroups cannot have common elements $\frac{72}{4}=18$ many cyclic subgroups of order $10$. 

---
### Example $7$.) 

Find the number of elements of order $2$ in $D_{4} \oplus \mathbb{Z}_{4}$:

$$|(a,b)| =2 \implies |a|=1 \text{ or } 2, |b|=1 \text{ or 2}$$

But not both. There are $6$ choices for $a$, counting the identity, we have $R_{\pi}$, the identity, (idk what the remaining $4$ are), and for $b$ we have $2$ and $0$ as our choices. 

Excluding the identity element we have:

$$6 \cdot 2 - 1 = 11$$

many choices for elements of order $2$. 

---
### Example 8.) 

For each divisor $r$ of $m$ and $s$ of $n$, the group $\mathbb{Z}_{m} \oplus \mathbb{Z}_{n}$, is isomorphic to some subgroup of $\mathbb{Z}_{r} \oplus \mathbb{Z}_{s}$. 

---

# Theorem 8.2) Criterion for $G \oplus H$ to be a [[Cyclic Group]]

Let $G$ and $H$ be finite cyclic groups. Then $G \oplus H$ is a cyclic group iff $|G|$ and $|H|$ are relatively prime. 

### $Proof.)$ 
$\implies$ Suppose $G \oplus H$ is cyclic. We want to show that $\text{gcd}(m,n)=1$. Denote $d=\text{gcd}(m,n)$, and let $(g,h)$ be a generator of $G \oplus M$. It follows that:

$$(g,h)^{mn/d} = ((g^m)^{n/d},(h^n)^{m/d})=(e_{G},e_{H})$$
We thus obtain that: $|(g,h)| \leq \frac{mn}{d}$. We have that $|(g,h)|=mn$ since $G \oplus H$ is cyclic and is generated by $(g,h)$. By Lagrange's theorem we know that: 
$$(g,h)^{|G \oplus  H|}=(g,h)^{mn}=e$$
Which gives $mn \leq \frac{mn}{d}$ and thus $d=1$ as desired. 

$\Longleftarrow$ Suppose that $\text{gcd}(m,n)=1$. Since $G,H$ are assumed to be cyclic we have that $G=\langle g \rangle, H = \langle h \rangle$ for some $g \in G, h \in H$. 

By theorem $8.1$ (the fact that the direct product of $2$ groups has an order equal to $\text{lcm}(m,n)$ for $|G| =m$ and $|H|=n$, then:
$$|(g,h)\text{lcm}(m,n)=mn \text{ (step follows from the fact the GCD is assumed 1)} =|G \oplus H|$$

Thus since we showed both directions the result follows that $|G \oplus H|$ is cyclic $\iff|G|,|H|$ are relatively prime. 

---
# Corollary 1.) Criterion for  $\bigoplus_{i=1}^n G_{i}$ to be cyclic. 
Repeated application of the above theorem results in the fact that $\bigoplus_{i=1}^n G_{i}$ is cyclic when each $|G_{i}|$ and $|G_{j}|$ are relatively prime. 

# Corollary 2.) Criterion for $Z_{n,n_{2},\cdots,n_{k}} \cong \bigoplus_{i=1}^k \mathbb{Z}_{n_{i}}$
The result holds true iff $\text{gcd}(n_{i},n_{j})=1$ for $i\neq j$. For example the following is true:

$$\mathbb{Z}_{2} \oplus \mathbb{Z}_{2} \oplus  \mathbb{Z}_{3} \oplus \mathbb{Z}_{5} \cong \mathbb{Z}_{2} \oplus  \mathbb{Z}_{6} \oplus \mathbb{Z}_{5} \cong \mathbb{Z}_{2} \oplus  \mathbb{Z}_{30} $$

This result isn't true for $\mathbb{Z}_{60}$ since $\mathbb{Z}_{60}$ is a cyclic group and none of the others are via the above theorem. 




