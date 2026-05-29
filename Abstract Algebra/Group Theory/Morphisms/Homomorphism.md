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

For $8$, we can show that $\phi^{-1}(\bar{K}) \leq G$ using the one step subgroup test. 