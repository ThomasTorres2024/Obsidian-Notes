---
title: Lagrange's Theorem
tags:
  - AbstractAlgebra
draft: "False"
---
# Theorem.) [[Lagrange's Theorem]]
Lagrange's Theorem states that for a [[Finite Group]], $G$ and a [[Subgroup]] $H \leq G$, then $|H| \bigg| |G|$. 

Moreover, the number distinct left (also true for right) [[Coset]]s of the $H$ over $G$ is given by $\frac{||G||}{||H||}$. 

### Proof.) 
Let the distinct cosets of $H$ in $G$ be:
$$a_{1}H,a_{2}H,\dots, a_{r}H$$
Where there are $r \in \mathbb{N}$ many distinct cosets. By $5$ of the lemma for cosets, it follows that each of the distinct cosets are disjoint. 

Furthermore, we know that:
$$\bigcup_{i=1}^r a_{i}H = G$$
If this were not the case then, $\exists a \in G \textbackslash (\bigcup_{i=1}^r a_{i}H )$. Since we supposed that $a_{i}H: 1 \leq i \leq  r$ are all of the distinct cosets of our set, and that by $5$ of the lemma again all of the cosets are disjoint, this contradicts the fact that these are __all__ of the distinct cosets of $H$ in $G$. 

Therefore it is valid to say that:
$$\bigcup_{i=1}^r a_{i}H = G$$
Furthermore we have that:
$$|G| = |a_{1}H|+|a_{2}H|+\dots + |a_{r}H| = \sum_{i=1}^r |a_{i}H|$$
For lemma $7$ we also have that for $a_i=e$:
$$|a_{i}H|=|eH|=|H|$$
Since the size of each [[Coset]] is equivalent it follows that every [[Coset]] has size $|H|$. We finally obtain that:
$$|G|=r|H|$$
Which concludes the proof that $|H| \bigg |G|$ and that there are $r$ many [[Coset]]s of $H$ over $G$

---
# Corollary .)  $\large [G:H]=\frac{|G|}{|H|}$
If $G$ is a finite group and $H \leq G$ then:
$$\large [G : H ] = \frac{|G|}{|H|} = r \quad (\text{ from above example})$$
# Corollary .)  $\large |a| \bigg| |G|$
In a [[Finite Group]], $G$ the order of each element $a \in G$ we have that the [[Order]] of $a$ divides the [[Order]] of $G$. 

##### Proof.) 
If $G$ is any group and $a \in G$, recall that from the properties of cyclic groups that $|a|=|\langle a \rangle|$. 

### Corollary.) Groups of Prime Order are Cyclic 

Every group of prime order is isomorphic ([[Isomorphism]]) to $\mathbb{Z}_{p}$ and is also an [[Abelian Group]] by extension. 

##### Proof.) 
Suppose that $G$ has prime order $p$, thus $|G| > 1$. Let $a \in G$ such that $a \neq e$ (since we have excluded the trivial group now). 

Then by the previous corollary we have that $|\langle a \rangle| \bigg| p$ and $|\langle a \rangle|>1$.  Since $p$ has no divisors then $|\langle a \rangle | = |G|$ and so $G$ is cyclic of order $p$ and we have that:
$$G \cong \mathbb{Z}_{p}$$

## Corollary 4.) $\large a^{|G|}=e$
By corollary $2$ we have that:
$$|a| \bigg| |G| \implies |G| =|a| k : k \in \mathbb{N}$$
Therefore:
$$a^{|G|}=a^{|a|k}=(a^{|a|})^k=e^k=e$$

## Corollary 5.) [[Fermat's Little Theorem]]
For every integer $a$ and prime number $p$ we have that:
$$a^p = a \mod(p)$$
##### Proof.) By the [[Division Algorithm]]:
$$a=pm+r : 0 \leq r < p$$
Therefore, $a=r \mod(p)$. It is thus equivalent to prove that $r^p=r \mod(p)$. If $r=0$ the result is trivially true, so now we can assume that $1 \leq r \leq p-1$ which is to say that $r \in U(p)= \{1,2,\cdots,p-1  \}$. 

By the preceding corollary we know that (since $p$ is chosen prime then we know that $|U(p)|=p-1$ also true via [[Euler's Totient Function]] )
$$r^{|U(p)|}= r^{p-1}=1\mod(p)$$
And thus:
$$r^p=r \mod(p)$$Which concludes the proof. 

---
# Examples.)

#### Example 1.) 
Let $A_4$ be the alternating group, which has order $12$. We can show that $A_{4}$ has no subgroups of order $6$. 

We have that $A_4$ has $8$ elements of order $3$:

$$\begin{align}
(123),(243),(142),(134) \\
(132),(143),(234),(124)
\end{align} $$

Suppose that $H < A_4:|H|=6$. Now, let $a \in A_{4}$ and $|a|=3$. By [[Lagrange's Theorem]], it follows that there are $2$ distinct cosets here. If we choose $a \not \in H$ then it follows by $5$ of lemma $7.1$ that $aH \neq H$, so we can write that: 
$$A_{4} = H \cup aH$$

We have either that $a^2 \in H$ or $a^2 \in aH$ (I think this step is justified by the cosets being disjoint and needing to contain all of the elements in both sets). Since $|a|=3$, notice that: 

$$(a^2)^2 = a^4 = a^3 \cdot a = e \cdot 
a = a \implies a \in H$$
However, this is impossible since we assumed that $a \not \in H$. 

Now consider if $a^2 \in aH$, then, for some $\ h \in H$, $a^2=ah$, and thus: we have that $h=a$, however this would entail that $h \in H \implies a \in H$, which is a contradiction. 

It must be the case then that $a \in H$. Furthermore, notice that we have listed $8$ elements in the [[Coset]] where $|a|=3$ and since we have shown that any arbitrary $a \in H$, we therefore obtain that all $8$ elements of order $3$ must be in $H$ and by the Pigeon hole principle we run out of slots and therefore obtain the fact that there can be no subgroup of order $6$ of $A_{4}$. 

---

### Corollary 7.1.6: $$[G:K]=[G:H] \cdot [H:K]$$
If $G$ is a [[Finite Group]] and $H \leq G$, and $K \leq H$ then we obtain that: 


$$[G:K] = \frac{|G|}{|K|} = \frac{|G|}{|H|} \cdot \frac{|H|}{|K|}$$
Which completes the proof for this corollary. 

---
# Theorem 7.2 

Given the [[Subgroup]]s, $H \leq G$ and $K \leq G$ then for the following group:

$$HK=\{ hk: h \in H, k \in K \}$$

Then it is true that:

$$|HK| = \frac{|H||K|}{|H \cap K|}$$

Note, that it is not necessarily the case that $HK \leq G$. There are maximum of $|H| \cdot |K|$ many elements in $HK$, however we need to handle the overlap. 

We want to find the degree of repetition. We we may have that:

$$hk=h'k' : h \neq h' \text{ both in } H, k \neq k' \text{ both in } K$$
Note that, for every $t \in H \cap K$, in every product $hk$ we have that:

$$hk=(ht)(t^{-1}k)$$
Thus, there are at least $|H \cap K|$ many repetitions, since each element and its inverse is contained within this set. 

On the other hand, 
$$hk=h'k' \implies h^{-1}h^1 = k'(k)^{-1} \in H \cap K$$
We know this element is in the intersection since both of its elements are from $H$ and from $K$, yet they are equivalent. But notice that this is actually $t$:

$$t=h^{-1}h'=k(k')^{-1}$$

And we obtain that: 

$$h'=ht, k'=t^{-1}k$$

Thus, for ever element in $H \cap K$, there is another way to express the element $hk$. QED $|HK|= \frac{|H||K|}{|H \cap K|}$










