---
title: Homomorphism
tags:
  - AbstractAlgebra
draft: "False"
---
# Homomorphism
A [[Morphism]] between two [[Group]]s, $\phi : A \to B$ such that for $a,b \in A$ is a special type of [[Function]] which satisfies the following condition:
$$\phi(a \circ_{A} b)=\phi(a) \circ_{B} \phi(b)$$
Which is to say that the binary operation on $A$ of $a,b$ and then applying $\phi$ is equivalent to applying $\phi$ to $a,b$ first respectively over $A$, and then applying the binary operation of $B$ over the resulting elements. 

---
# Definition : [[Group]] Homomorphism
A homomorphism $\phi : G \to \bar{G}$ is a mapping from $G \to \bar{G}$ which preserves the following operation:
$$\phi(ab)=\phi(a)\phi(b) \quad \forall a,b \in G$$

---
# Definition: Kernel
The Kernel of a [[Homomorphism]] for $\phi: G \to \bar{G}$ is the set of all elements in $G$ such that the map results in the identity element of $\bar{G}$:
$$\text{ker }\phi = \{ x \in G : \phi(x)=e_{\bar{G}} \}$$
---
### Example 1.)
Any [[Isomorphism]] between $2$ groups is automatically a homomorphism. 

### Example 2.) $\mathbb{R}^* = \mathbb{R} \textbackslash\{0 \}$ with multiplication
Then:
$$\det : GL(n,\mathbb{R}) \to \mathbb{R}^*$$
Is a homomorphism. 

### Example 3.) $\phi : \mathbb{R}^* \to \mathbb{R}^* \quad x \mapsto |x|$ 
Is a homomorphism with the kernel $\text{ker }\phi =\{-1,1\}$.

### Example 3.5) 
Any vector space is an Abelian group with the addition of operation of vectors. If $V,W$ are Vector spaces with zero vectors $0_{v}$ and $0_{W}$ then any [[Linear Transformation]] $f: V \to W$ is a [[Homomorphism]] with the associated kernel:
$$\text{ ker }f = \{ v \in V : f(v)=0_{W}\}$$

### Example 4 $\mathbb{R}[x]$ polynomials in $x$ with real coefficients with addition of polynomials 
The derivative mapping is a homomorphism (particularly an endomorphism) from $\mathbb{R}[x] \to \mathbb{R}[x]$ given by $f\mapsto f'$. 

### Example 5.) $\phi: \mathbb{Z} \to \mathbb{Z}_{n}$
Then $\phi(m)=m \text{ mod }n$ is a homomorphism. 

### Example 8.) $\phi(x)=x^2$ 
is not a homomorphism from $\mathbb{R} \to \mathbb{R}$ over addition:
$$\phi(1+1)=\phi(2)=4 \quad \phi(1)+\phi(1)=2$$

---
# Properties of Homomorphism 

### Definition [[Image (Abstract Algebra)]]
The image of a [[Homomorphism]] from a group $G$ to a group $\bar{G}$ is the range of $\phi$, the set of the following form, denoted via $\text{Im }\phi$ and $\phi(G)$:
$$\text{Im }\phi = \phi(G)=\{ \phi(g) : g \in G \}$$
# Theorem .) Properties of Homomorphisms 
Let $G,\bar{G}$ be group with [[Identity Element]]s $e_{G}$ and $e_{\bar{G}}$ respectively and let $\phi: G \to \bar{G}$ be a [[Homomorphism]] between the groups. Then: the following are true:

1. $\phi(e_{G})=e_{\bar{G}}$
2. $\phi(g^n)=(\phi(g))^n$
3. $\text{Im }\phi \leq \bar{ G}$
4. If $g \in G$ has finite order then $\phi(g) \bigg| |g|$ and if $|G|$ is finite then $|\phi(g)|$ divides both $|g|$ and $|\phi(G)|$. 
5. $\phi(a)=\phi(b) \iff a\text{Ker }\phi =b\text{Ker }\phi$
6. If $g \in G$ and $\phi(g)=g'$ then: $$\phi^{-1}(g')=\{x \in G: \phi(x)=g' \} = g \text{Ker } \phi $$
$Proof.)$
Proofs for $1,2$ are identical to proofs for [[Isomorphism]] theorem of the same properties. 

For $2.5$ note that for $a,b \in G$
$$\phi(a)(\phi(b))^{-1} = \phi(a) (\phi(b^{-1}))=\phi(ab^{-1}) \in \phi(G)$$
Thus by the 1 step subgroup test it follows that $\text{Im}(G) \leq \bar{G}$. 

For $3$ using $1,2$ we have that if $g^n=e_{G}$ then $e_{\bar{G}} = \phi(e_{G})=\phi(g^n)=\phi(g)^n$. Thus we have that $|\phi(g)| \bigg| n$. 

If $G$ is finite then so is $\phi(G)$, and we also have that by Lagrange's theorem that $|\phi(g)| \bigg| |\phi(G)|$ as well. 

For $4$, by $1$ $e_{G} \in \text{ker }\phi$ so that $\text{ker }\phi \neq \emptyset$. By the sub group test we have that $\text{ker }\phi \leq G$ given that we can show for $a,b \in \text{ker } \phi$ that $ab^{-1} \in \text{ker }\phi$:
$$\phi(ab^{-1})= \phi(a)\phi(b^{-1}) = e_{\bar{G}} \cdot (e_{\bar{G}})^{-1}=e_{\bar{G}}$$
Thus $ab^{-1} \in \text{ker }\phi$ so $\text{ker }\phi \leq G$. 

For $5$ assume that for $a,b \in G$ that $\phi(a)=\phi(b)$. Then we have that:
$$e_{\bar{G}}=(\phi(b))^{-1} \phi(a)=\phi(b^{-1}a)$$
So then we have that $b^{-1}a \in \text{ker }\phi$. By properties of cosets we then obtain that:
$$b \text{Ker }\phi=a \text{Ker }\phi$$This argument is reversible, and thus $5$ is true. 

To prove $6$ we need to show that $\phi^{-1}(g') \subseteq g\text{Ker }\phi$ and that $g \text{ Ker}\phi \subseteq \phi^{-1}(g')$. 

For the first inclusion let $x \in \phi^{-1}(g')$, then $\phi(x)=g'$, and furthermore $\phi(g)=\phi(x)$. By $5$ we have that $g \text{ Ker }\phi =x \text{Ker }\phi$ and thus $x \in g \text{Ker }\phi$. 

For the other direction suppose that $k \in \text{ker }\phi$. Then we have that:
$$\phi(gk)=\phi(g) \cdot \phi(k)=g' \implies gk \in \phi^{-1}(g')$$
This shows both directions.

This proves every result in the theorem. 

---
# Theorem .) Properties of Subgroups Under Homomorphism 
Let $\phi$ be a [[Homomorphism]] from a group $G$ to a group $\bar{G}$ and let $H$ be a subgroup of $G$. Then: 

1. $\phi(H)=\{ \phi(h) : h \in H \} \quad \phi(H) \leq \bar{G}$
2. If $H$ is cyclic then $\phi(H)$ is also cyclic
3. If $H$ is abelian then $\phi(H)$ is also Abelian. 
4. If $H \triangleleft G$ then $\phi(H) \triangleleft \phi(G)$.
5. If $|\text{ker }\phi|=n$ then $\phi$ is an $n-1$ mapping from $G$ onto $\phi(G)$. 
6. If $H$ is finite then $|\phi(H)|$ divides $|H|$
7. $\phi(Z(G))$ is a subgroup of $Z(\phi(G))$
8. If $\bar{K} \leq \bar{G}$ then $\phi^{-1}(\bar{ k})=\{ k \in G : \phi(k) \in \bar{ K} \}$ is a subgroup of $G$. 
9. If $\bar{K}$ is a [[Normal Subgroup]] of $G$ then $\phi^{-1}(\bar{K})=\{ k \in G : \phi(k) \in \bar{ K} \}$
10. If $\phi$ is onto and $\text{ker } \phi =\{e \}$  then $\phi$ is an [[Isomorphism]] from $G\to \bar{ G}$. 

$Proof.)$
The proofs for $1,2,3$ are the same as their isomorphism counterparts. 

For $4$, let $\phi(h) \in \phi(H), \phi(g) \in \phi(G)$. Then:
$$\phi(g) \phi(h) \phi(g)^{-1}=\phi(ghg^{-1}) \in \phi(H)$$
Therefore we have that $\phi(H) \triangleleft \phi(G)$ since we have that $ghg^{-1} \in H$ since we assume that $G \triangleleft H$. 

For $5$, we have that from $6$ of the above theorem, and the fact that all cosets of $\text{ker }\phi=\phi^{-1}(x)$ have the same number of elements, which is $n$. 

For $6$, let $\phi_{H}$ denote $\phi|_{H}$, the restriction of $\phi$ to $H$. Then, $\phi_{H}$ is a homomorphism from $H$ onto $\phi(H)$. 

Suppose that $|\text{ker }\phi|=t$. By $t$ then $\phi_{H}$ is $5$ to $1$, so that $|\phi(H)|t=|H|$. And thus $|\phi(H)|$ divides $|H|$ as required. 

For $7$ if $\phi(z) \in \phi(Z(G))$ and $\phi(g) \in \phi(G)$ then we have that: 
$$\phi(z)\phi(g)=\phi(zg)=\phi(gz)=\phi(g)\phi(z)$$
Thus $\phi(z) \in Z(\phi(G))$. 

For $8$, we can show that $\phi^{-1}(\bar{K}) \leq G$ using the one step subgroup test. We have that $e_{g} \in \phi^{-1}(\bar{K})$ via properties of homomorphisms, thus $\phi^{-1}(\bar{K})\neq \emptyset$. 

Let $k_{1},k_2 \in \phi^{-1}(\bar{K})$. Then by the definition of $\phi^{-1}(\bar{K})$ we have that $\phi(k_{1}),\phi(k_{2}) \in \bar{K}$, thus $\phi(k_{2})^{-1} \in \bar{K}$ and thus:"

$$\phi(k_{1}k_{2}^{-1})=\phi(k_{1}) \phi(k_{2})^{-1}$$
We thus obtain that $k_{1},k_{2} \in \phi^{-1}(\bar{K})$ as desired. 

In $9$ we make use of the normality test. Let $x \in G$ be arbitrary. Then, every element $x\phi^{-1}(\bar{K})x^{-1}$ has the form $xkx^{-1}$ where $\phi(k) \in \bar{K}$.

Since $\bar{K} \triangleleft \bar{G}$ we have that $\phi(xkx^{-1}) =\phi(x) \phi(k) \phi(x^{-1}) \in \bar{K}$ so that by def $xkx^{-1} \in \phi^{-1}(\bar{K})$. 

$10$ follows from $5.$ 

---
### Corollary [[Kernel (Abstract Algebra)]]s are Normal
Let $\phi$ be a group homomorphism from $\phi: G \to \bar{G}$, then $\text{ker } \phi \triangleleft G$. 

The proof follows from $9$ of the above theorem. Since $\{e_{G}\} \triangleleft \bar{G}$ and $\text{ker }\phi=\phi^{-1}(\{ e_{\bar{G}} \})$. 

---
# Examples

### Example $9 \quad \mathbb{C}^* = \mathbb{C}\textbackslash\{ 0\}$ with multiplication of complex numbers
Consider $\phi: \mathbb{C}^* \to \mathbb{C}^*$ given by $\phi(z)=z^4$. Then since $\phi(zw)=(zw)^4=z^4w^4$ we have that $\phi$ is a homomorphism. We obtain the following:
$$\text{ker }\phi=\{ z : z^4=1 \} = \{1,i,-1,-i \}$$
Then by using theorem $4.2$ we know that this mapping is $4$ to $1$. We can use this to find all elements that map to $2$ under $\phi$. 

Clearly, $\phi(\sqrt[4]{2 })=2$. Then, via $6$ of 10.1, the set of all elements which map to $2$ under $\phi$ is given in the following coset:
$$\sqrt[4]{ 2 } \text{ ker }\phi = \{\sqrt[4]{ 2 }, \sqrt[4]{ 2 }i, -\sqrt[4]{ 2 },- \sqrt[4]{2  }i \}$$

### Example Define $\phi: \mathbb{Z}_{12} \to \mathbb{Z}_{12}$ by $\phi(x)=3x \text{ (mod 12)}$ 

Clearly $\phi$ is a homomorphism. It can be shown that $\text{ker }\phi=\{ 0,4,8\}$ by using $5$ of the second set of properties of homomorphisms and observe that this is a $3$ to $1$ mapping. 

Since $\phi(2)=6$ by $6$ of theorem $10.1$ we have that $\phi^{-1}(6)=2+\text{ker }\phi =\{2,6,10 \}$. Furthermore, $\langle 2 \rangle$ is a cyclic group, and $\phi(\langle 2 \rangle)=\{0.6\}$ must also be cyclic. 

Furthermore, $|2|=6$ and $|\phi(2)|=|6|=2$. So we have that $|\phi(2)|$ divides $|2|$. 

If we let $\bar{K}=\{0,6\}$, then $\phi^{-1}(\bar{K})=\{0,2,4,6,8,10\}$.

### Example 11.) Find all homomorphisms from $\mathbb{Z}_{12} \to \mathbb{Z}_{30}$. 
By $2$ of theorem $10.1$, any such homomorphism is specified by the map of the image $\phi(1)$. Thus for $\phi(1)=a$ we have that $\phi(x)=xa$ for any $x \in \mathbb{Z}_{12}$. 

By Lagrange's theorem and $3$ of the first theorem, $|a|$ must divide $30$ and it must divide $12$. This necessitates that $|a|=1,2,3,6$. We have the total possibilities for this mapping now as $a=0,15,10,20,5,25$. 

Each of these give a different operation preserving function from $\mathbb{Z}_{12} \to \mathbb{Z}_{30}$. 

### Ex 12.) Sign Function $\text{sgn} : Sn \to\{ -1,1\}$
$$Sn(\sigma)= \begin{cases}
1 & \sigma \text{ is even } \\
-1 & \sigma \text{ is odd}
\end{cases}$$

---
# The First Isomorphism Theorem for [[Group]]s 
Let $\phi$ be a [[Group]] homomorphism from $G \to \bar{G}$. Then the following mapping is an [[Isomorphism]] from $\frac{G}{\text{ker }\phi} \to \phi(G)$ given by:
$$g\text{Ker }\phi \to \phi(g)$$

$Proof.)$ Use $\psi$ to denote the correspondence $g\text{Ker }\to \phi(g)$, and we also have that $\psi$ is both a well defined and injective correspondence. Surjectivity here is also trivial. 

The last thing to check is that the result is observation preserving. Consider the following:
$$\psi(x \text{ ker }\phi \cdot y \text{ ker }\phi)=\psi(xy \text{ ker }\phi)=\phi(x)\phi(y)$$
$$=\psi(x \text{ ker }\phi)\psi(y \text{ ker }\phi)$$

### Corollary.) If $\phi$ is a homomorphism from a finite group $G$ to a finite group $\bar{G}$, then:

$\frac{|G|}{|\text{ker }\phi|} = |\phi(G)|$
Trivially follows from Lagrange. Since $\frac{G}{\text{ker }\phi}$ is the factor group it must have as many elements as [[Coset]]s. 

### Corollary $2$
If $\phi$ is a homomorphism from a finite group $G\to \bar{G}$, then $|\phi(G)|$ divides $|G|$ and $|\bar{G}|$ if $|\bar{G}|<\infty$ and divides $|G|$ if $|G| =\infty$. 

$Proof.)$
$|\phi(G)|$ divides $|G|$ via corollary $1$. Secondly, since $\phi(G) \leq \bar{G}$ via [[Lagrange's Theorem]] we have that $|\phi(G)| \bigg| |\bar{G}|$. In the case where $|\bar{G} = \infty|$, this is trivial. 

--- 
# Commutative Diagrams 
The first isomorphism theorem for groups can be understood in terms of a commutative diagram. 

![[Pasted image 20260602084131.png]]

Here we let $\phi:G \to \phi(G)$ and $\gamma: G \to \frac{G}{\text{ker }\phi}$ where $g \mapsto g\text{ ker }\phi$. This is known as the natural quotient map. Lastly, let $\psi: \frac{G}{\text{ker } \phi } \to \phi(G)$ and $g\text{ker }\phi \mapsto \phi(g)$. 

Notice that $\phi$ is the mapping used in the first isomorphism theorem. Furthermore, note that for $g \in G$ that:

$$\psi(\gamma(g))=\psi( g \text{ker }\phi)=\phi(g)$$
Which is to say that $\phi=\psi \circ \gamma$. 

---
### Example 14.) 
Recall the homomorphism from example $5$ from $\mathbb{Z} \to \mathbb{Z}_{n}$ given by $m\to m \mod(n)$. By the above theorem we then have that, since $\text{ker }\phi = \langle n \rangle = n\mathbb{Z}$ that:

$$\frac{\mathbb{Z}}{n\mathbb{Z}} \cong \mathbb{Z}_{n}$$
Where the isomorphism is given by $m+n\mathbb{Z} \to m \mod(n)$. 

### Example 15.) $\phi: GL(n,\mathbb{R}) \to \mathbb{R}^*$ 
Consider $\phi$ where $A \in GL(n,\mathbb{R}), A\mapsto \det(A)$. 

Then, $\phi$ is a homomorphism whose kernel is $SL(n,\mathbb{R})$. By the above theorem we obtain that: 

$$\frac{GL(n,\mathbb{R})}{SL(n,\mathbb{R})} \cong \mathbb{R}^*$$
### Example 16.) 
Let $G$ be an Abelian group, and recall that $G^k = \{ x^k : x \in G \}$ and $G^{(k)}=\{ x \in G: x^k=e \}$ are both subgroups of $G$. 

If we define a homomorphism $\phi: G \to G^k$ given by $\phi(x)=x^k, x\in G$, then clearly by the first isomorphism theorem for groups:

$$\frac{G}{G^{(k)}} \cong G^k$$
### Example 17.) N/C Theorem 
Let $G$ be a group and $H \leq G$. Define the normalizer of $H$ in $G$ as the following: 
$$N(H) = \{x \in G: xHx^{-1} =H \} $$
And the centralizer of $H$ in $G$ as:
$$C(H) = \{ x \in G:xhx^{-1} = h, \forall h \in H \}$$
Both $N(H),C(H)$ are subgroups of $G$. 

Consider the mapping from $N(A) \to \text{Aut}(H)$ given by $g \mapsto \phi_{g}$. Recall that an inner automorphism $\phi_{g}(h)=ghg^{-1},h \in H$. 

This can easily be verified to be a homomorphism. The kernel of this transformation is given by $$\{ g :\phi_{g} =e \} = \{g : ghg^{-1} =h, \forall h \in H \}=C(H)$$
Thus by the first isomorphism theorem we know that: 
$$\frac{N(H)}{C(H)} \cong S : S \leq \text{Aut}(H) $$

---
# Theorem.) Normal Subgroups are Kernels 
Every normal subgroup of a group $G$ is a kernel of a homomorphism of $G$. In particular any such homomorphism is the kernel of the mapping $g\to gN$ from $G\to \frac{G}{N}$.

$Proof.)$
Define $\gamma:G \to \frac{G}{N}$ by $\gamma(g)=gN$ where $\gamma$ is the natural homomorphism from $G\to \frac{G}{N}$. 

Then we have that:
$$\gamma(xy)=(xy)N=xNyN = \gamma(x) \gamma(y)$$
This equality holds since $N \triangleleft G$, thus we have that $\gamma$ is a homomorphism. Moreover, $g \in \text{ker }\gamma \iff gN=\gamma(g)=N$ which is true $\iff g \in N$. 

Thus $N$ is a kernel of some homomorphism of $G$. Therefore we have shown the desired result.


