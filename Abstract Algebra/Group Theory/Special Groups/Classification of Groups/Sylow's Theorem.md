---
title: Sylow Theorem
tags:
  - AbstractAlgebra
draft: "False"
---
 # Sylow's Theorems
Sylow's theorems are sort of the converse of [[Lagrange's Theorem]], which if we recall tells us that for some [[Subgroup]] $H$ of a [[Group]] $G$ we have that $H \leq G \implies \frac{|G|}{|H|} \in \mathbb{N}$. We cannot generally say that just because $|H| \bigg| |G|$ that there is some subgroup of size $|H|$, but [[Sylow's Theorem]] allows us to get close to this. 

Sylow Theorems apply to any finite group, not specific types of groups like cyclic, dihedral, or something else of that sort. 

---
# The First Sylow Theorem 

__Theorem__
Given a [[Group]] $G$, such that: $|G|=n=p^e \cdot m$ where $p$ is a prime number, and $e \in \mathbb{N}$ is the largest natural number such that $\text{gcd}(p,m)=1$ then $\exists H, H \leq G$ and $|H|=p^e$. 

__Definition__
This type of [[Subgroup]] is known as a Sylow $p-$subgroup. 

#### Example
Consider $G=S_{4}$ the symmetric group of $4$ elements, such that $|G|=4! =24$. By [[Sylow's Theorem]] we have that $|S_{4}|$ has some subgroup of order $8=2^3$. 

#### Example
Consider $G=D_{5}$ the Dihedral group of $10$ elements, such that $|G|=10=5\cdot 2$. By [[Sylow's Theorem]] we have that $G$ has a subgroup of order $2$ and order $5$ which reflects the $5$ rotations, and the $2$ reflections. Namely, $\langle \rho_{2\pi/5} \rangle$ has order $5$ and $\langle \text{reflection} \rangle$ has order $2$. 

---
### Corollary 
If $p$ divides $|G|$, $\exists x \in G$ such that $|x|=p$. 

For example if $|G|=14$, then it must be the case that $G$ has an element of order $7$ since $7$ divides $14$. 

$Proof.)$
Using Sylow $I$, we know that $H \leq G$ such that $|H|=p^e$ where $e \geq 1$. Pick some $y \in H$, then: 
$$\langle y \rangle = C_{p^f}$$
some cyclic group with order divide $p^e$. Taking:
$$x=y^{p^{k-1}}$$
Provides an element of order $p$. 

---
# The Second [[Sylow's Theorem]] 
The second [[Sylow's Theorem]] allows us to specify what subgroups which the first [[Sylow's Theorem]] groups look like. This theorem consists of $2$ parts:

1. Given $H \leq G$ where $H$ is a Sylow $p-$subgroup, any other Sylow $p-$subgroup is conjugate to $H$, namely, that $\exists g$ such that $H'=gHg^{-1}$. 

2. Given any subgroup $K \leq G$ such that $|K|=p^d$ for any Sylow subgroup $H$, $\exists g \in G$ such that $gKg^{-1} \leq H$.

Conjugating a Sylow subgroup results in another Sylow subgroup since it will have the same size. The theorem states that all Sylow subgroups arise in this way. The second part states that $|K|=p^d$, meaning that any prime power of a subgroup is a group. We can conjugate any $K$ and make it "land" in $H$. 