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
Notice that these are the properties of [[Homomorphism]]s generally. If this function is [[bijective]] then it follows that it is a [[Abstract Algebra/Ring Theory/Ring Theory Basics and Definitions/Ring Isomorphism]]. 

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

Since $a=\phi(1) \in \phi(\mathbb{Z}_{10})$, and since $|\phi(\mathbb{Z}_{10})|\bigg|10$ we have that by Lagrange's theorem, $|a|\bigg|10$, thus $|a|=10,5,2$, but again not $1$. 

Considering $|a|=10$ first, then we obtain that $a=2$, and we can observe that it is not idempotent: $$\begin{align}
2^2=4 \\
6^2=36=16 \mod(20) \\
14^2=196=16 \mod(20) \\
18^2=324=4 \mod(20)
\end{align}$$
Thus there are no idempotent elements for $|a|=10$. If we move onto $|a|=5$ then we have that, $a=4,8,12,16$. And then checking for idempotency:
$$\begin{align}
4^2=16 \\
8^2=64=4\mod(20) \\
12^2=144=4\mod(20) \\
16^2=256=16\mod(20)
\end{align}$$
Thus the mapping from $\mathbb{Z}_{10} \to \mathbb{Z}_{20}$ given by $\phi(x)=16x$ is a possible non-zero homomorphism which maintains all relevant properties. Lastly if $|a|=2$ then we only have the possibility of $a=10 \implies 10^2=100=0 \mod(20)$

For a homomorphism from $\mathbb{Z}_{20} \to \mathbb{Z}_{10}$, again $\phi(1)$ must also be an idempotent in $\mathbb{Z}_{10}$. By Lagrange's theorem, $|a| \bigg|10$, so $|a|=10,5,2$ and again it can't be $1$ since this would be the zero map. 

Since generators map to generators we must map to a function such that for $|a|=10$, $a\in U(10)$ which is to say that the candidates for this map are $1,3,7$ and $9$. We can check the following:

$$\begin{align}
1^2=1 \\
3^2=9 \\
7^2=49=9 \mod(10) \\
9^2=81 =1\mod(10)
\end{align}$$
Clearly $x \mapsto x$ is a well defined homomorphism from $\mathbb{Z}_{20} \to \mathbb{Z}_{10}$. 

For $|a|=5 \implies a=2,4,6,8$ and thus:
$$\begin{align}
2^2=4 \\
4^2=16=6 \mod(10) \\
6^2=36=6 \mod(10) \\
8^2=64=4\mod(10) 

\end{align}$$
It can be easily verified that $x \mapsto 6x \mod(10)$ is a homomorphism. from $\mathbb{Z}_{20} \to \mathbb{Z}_{10}$. 

If $|a|=2$ this gives that $a=5$ and $5^2=25=5\mod(10)$ thus $x \mapsto 5x \mod(10)$ is a valid ring homomorphism from $\mathbb{Z}_{20} \to \mathbb{Z}_{10}$. 

### Example 5.)
Determine all ring homomorphisms from $\mathbb{Z}_{12} \to \mathbb{Z}_{20}$. All group homomorphisms of this form are given by $x \mapsto ax$ where $a=0,15,10,20,5$ or $25$. By Lagrange's theorem, we must divide both $12$ and $30$ in $|\phi(1)|=|a|$. We can now check for idempotency:

$$\begin{align}
0^2=0 \\
15^2=225=15 \mod(30) \\
10^2=100=10\mod(30) \\
20^2=400=10\mod(30) \\
5^2=25 \\
25^2=625=25 \mod(30)
\end{align}$$
The each function given by $a=0,15,10,25$ is a homomorphism from $\mathbb{Z}_{12}\to \mathbb{Z}_{30}$.

### Example 6.) 
$R$ is a commutative ring with $\text{char}(R)=2$, then the mapping $a\to a^2$ is a homomorphism from $R\to R$. 

For addition:
$$\begin{align}
\phi(a+b)=(a+b)^2=(a+b)(a+b)= \\
a^2+ab+ba+b^2=a^2+2(ab)+b^2 =a^2+b^2=\phi(a)+\phi(b)
\end{align}$$
For multiplication:
$$\phi(ab)=(ab)^2=(ab)(ab)=a^2b^2 = \phi(a)\phi(b)$$

### Example 7.) 
$\mathbb{Z} \cong 2\mathbb{Z}$ as groups but not as rings. Not isomorphic since $\mathbb{Z}$ has a multiplicative identity but not $2\mathbb{Z}$. 

### Example 8.)
Test for divisibility by $9$. An integer $n$ with decimal representation $a_{k}a_{k-1}\cdots a_{1}a_{0}$ is divisible by $9 \iff$ $\sum_{i=0}^k a_{i}$ is divisible by $9$. Observe the following:
$$n=\sum_{i=0}^k a_{i}(10)^i$$
Denote the natural homomorphism from $\mathbb{Z}\to \mathbb{Z}_{9}$ via $\alpha$ then $9\bigg |n \iff$
$$\begin{align}
0=\alpha(n)=\alpha(a_{k})(\alpha(10))^k+\alpha(a_{k-1})
(\alpha(10))^{k-1} \cdots + \alpha(a_{0}) \\
 =\alpha\left( \sum_{i=0}^k a_{i} \right)
\end{align}
$$
This is equivalent to $a_k$ being divisible by $9$. 

### Example 9.) 
Theorem of Geronides. Observe that $2^3=8$ and $3^2=9$ are consecutive integers. Are they the only solution of the following equation for $m,n,x,y>1$ of the following form:

$$x^m-y^n=1 $$
It turns out that the answer is no. It can be shown that this expression is only valid when for $(m,n)=(3,2)$ given that $x=2,y=3$ or in other words:
$$2^m=3^n \pm {1}$$
This leaves $2$ possibilities to check, $2^m=3^n+1,2^m=3^n-1$. The trick to use here is modular arithmetic. 

#### Case 1.) $2^m=3^n+1$
Observe $\forall n \in \mathbb{N}$ we have that $3^n \mod(8)=1,3$ such that $2^n+1 \mod(8)=2,4$. 

If $m>2$, then $2^m \mod(8)=0$. Tus there are no solutions in this case. 

### Case 2.) $2^m=3^n-1$
Observe that $\forall n$
that $3^n \mod(16)=3,9,11$ or $1$ depending on the value of $n \mod(4)$. Thus, $3^n-1 \mod(16)=2,8,10$.$2^m \mod(16)=0$ for $m \geq4$, and rules out the cases for $n \mod(4)=1,2,3$. 

### Case 3.) $n \mod(4)=0$
Let $n=4k$ for $k>1$. Then:
$$\begin{align}
3^{4k} \mod(5)=(3^4)^k \mod(5) \\
=1^k \mod(5) \\
=1
\end{align}$$
So that $(3^{4k}-1) \mod(5)=0$. On the other hand $2^m \mod(5)=1,2,3,4$ and $2^m$ cannot be $0$. This contradiction completes the proof. 

---
# Theorem.) Properties of Ring Homomorphisms

Let $\phi$ be a ring homomorphism from a [[Ring]] $R\to S$. Let $A$ be a [[Subring]] of $R$ and let $B$ be an ideal of $S$.  

1. For any $r \in R, n \in \mathbb{N}$ $$\phi(nr)=n\phi(r),\phi(r^n)=(\phi(r))^n$$
2. $\phi(A)=\{ \phi(a) : a \in A \}$, gives that $\phi(A) \leq S$ 
3. If $A$ is an ideal and $\phi$ is onto $S$ then $\phi(A)$ is an ideal. 
4. $\phi^{-1}(B)=\{r \in R: \phi(r) \in B \}$ is an [[Ideal (Rings)]] of $R$. 
5. If $R$ is commutative then $\phi(R)$ is also commutative. 
6. If $R$ has unity $1$, $S \neq \{0\}$ then $\phi(1)$ is the unity of $S$ and units in $R$ map to units in $S$. 
7. $\phi$ is a ring isomorphism $\iff$ $\phi$ is onto and $\text{ker}(\phi)=\{r \in R: \phi(r)=0 \}=\{0\}$
8. If $\phi$ is an isomorphism from $R$ onto $S$, then $\phi^{-1}$ is an isomorphism from $S$ onto $R$ 

$Proof.$ 
Many of these identities are essentially the same as their group counterparts and are omitted. 

$3.$ Suppose $A$ is an ideal of $R$ and that $\phi$ is onto $S$. By $2$, we have that $\phi(A) \leq S$, we need to check all absorbing properties.

Let $b \in \phi(A)$ and $s \in S$ be arbitrary. By the definition of $b=\phi(a)$ for some $a \in A$, and since $\phi$ is onto, then $s=\phi(r)$ for some $r \in R$. Then:

$$\begin{align}
bs = \phi(a)\phi(r) \\
=\phi(ar)
\end{align}$$
Since $A$ is an ideal of $R$, then $ar \in A$, and thus $bs \in \phi(A)$ and similarly $sb \in \phi(A)$. This proves this result. 

$6.)$ Let $1$ be a unity of $R$. Suppose that $S\neq\{0\}$ and that $\phi$ is onto. To show that $\phi(1)$ is the multiplicative identity we need to show the following holds:
$$\phi(1)\cdot s=s=s\cdot \phi(1) \quad \forall s \in S$$
Let $s \in S$ be arbitrary since $\phi$ is onto, then $s=\phi(r)=\phi(r\cdot1)$. Thus:
$$\begin{align}
\phi(1)\cdot s = \phi(1) \cdot \phi(r) \\
=\phi(1\cdot r) \\
=\phi(r) \\
=s
\end{align}

$$
Similarly $s\cdot\phi(1)=s$. For the second part, of $6$ suppose that $u$ is a unit of $R$. Then $\exists v \in R$ such that $uv=vu=1$. Then:
$$\begin{align}
\phi(uv)=\phi(vu)=\phi(1) \\
=\phi(u)\phi(v)=\phi(v)\phi(u)=\phi(1)
\end{align}$$
Thus since $\phi(1)$ is the unity of $S$, we must have that $\phi(u)$ is a unit in $S$. This finishes this proof. 

$7.)$ Suppose that $\phi:R\to S$ is an isomorphism of rings. Then $\phi$ is automatically onto and if $r \in \text{ker}(\phi)  \implies \phi(r)=0=\phi(0)$ where $r=0$ thus $\phi$ is injective. 

Conversely suppose $\phi: R \to S$ is a ring homomorphism which is onto and for which $\text{ker}(\phi)=\{0 \}$. Since $\phi$ is already a [[Homomorphism]] and onto then all we need to do is check that $\phi$ is [[injective]]. Suppose the following:
$$\begin{align}
\phi(r_{1})=\phi(r_{2}) \\
\phi(r_{1}-r_{2})=0 \\
\implies r_{1}-r_{2} \in \text{ker}(\phi)
\end{align}$$
Since $\text{ker}(\phi)=\{0\}$ then $r_{1}-r_{2}=0$ so $r_{1} = r_{2}$ which concludes this result. 

The remaining proofs are trivial since they are similar to other proofs about Group homomorphisms. 