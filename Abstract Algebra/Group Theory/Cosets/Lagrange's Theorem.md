---
title: Lagrange's Theorem
tags:
  - AbstractAlgebra
draft: "False"
---
# Theorem.) [[Lagrange's Theorem]]
Lagrange's Theorem states that for a [[Finite Group]], $G$ and a [[Subgroup]] $H \leq G$, then $|H| \bigg| |G|$. 

Moreover, the number distinct left (also true for right) [[Coset]]s of the $H$ over $G$ is given by $\frac{|G|}{|H|}$. 

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
# Corollary 1.)  $\large [G:H]=\frac{|G|}{|H|}$
If $G$ is a finite group and $H \leq G$ then:
$$\large [G : H ] = \frac{|G|}{|H|} = r \quad (\text{ from above example})$$
# Corollary 2.)  $\large |a| \bigg| |G|$
In a [[Finite Group]], $G$ the order of each element $a \in G$ we have that the [[Order]] of $a$ divides the [[Order]] of $G$. 

##### Proof.) 
If $G$ is any group and $a \in G$, recall that from the properties of cyclic groups that $|a|=|\langle a \rangle|$. 

## Corollary 3.) Groups of Prime Order are Cyclic 

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
# Theorem .) Size of a Product Group

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

---
### Example.) 
Claim that a group of order $75$ has at most one subgroup of $25$. Suppose $|G|=75$. Let, $H,K \leq G$ and $|H|=|K|=25$. By the above theorem we know that $|H \cap K| \bigg| |H| \cdot |K|$. 

We also have that $|H \cap K|$ is an integer and must be less than or equal to $25$, so it either $1,5,$ or $25$.  $|H \cap K| =1 \implies |H| \cdot |K| > 75$ which is a contradiction since $|H| \cdot |K| > |G|$, similarly we get the same thing for $|H \cap K|=5$, we get $125>75$ and we only have a consistent result if $|H \cap K|=25$. 


---
# Theorem .) Classification of Groups of [[Order]] $2p$: 

Let $G$ be a group of order $2p$ where $p$ is a prime, so $p>2$. Then $G \cong \mathbb{Z}_{2p}$ OR $G \cong D_p$.  

$Proof.)$ If $G$ has an element of order $2p$ then $G$ is a [[Cyclic Group]] of order $2p$, and is therefore Isomorphic. We can then show that $G \cong D_p$ for the next case. 

Our goal is to be able to show that the [[Cayley Table]] of $G$ will resemble $D_p$ more and more until it is forced into being $D_p$, the [[Dihedral Group]] of $p$. It can be shown that $G$ must have an element of order $p$. 


By $7.1.2$, it must be the case that every element of $G$ must divide $2p=|G|$. Since $G$ has no elements of order $2p$, it means that $G$ has either an element of order $2$ or order $p$. 

If we suppose that there are no elements of order $p$, then every non identity element of $G$ is order $2$, which is to say that:


$$a^2 = e \iff a=a^{-1}  : \forall a \in G $$

Hence, if $a,b \in G$ then: 

$$ab=(ab)^{-1}=b^{-1}a^{-1}=ba$$

And thus $G$ is an Abelian group. Since $p \geq 2$, if $a,b \neq$ identity elements of $G$, then it follows that the set is a [[Subgroup]] of $G$:

$$\{e,a,b,ab \} < G $$

Since $p>2$ and $p$ is prime, so $p$ is odd, and thus it cannot be the case that $4 \not\bigg| \text{ }2p$
 which contradicts [[Lagrange's Theorem]], which entails that that $G$ must have an element of order $p$, which we denote by $a$. 

Since $a$ has order $p$ then $|\langle a \rangle|=p$, so there are elements in the group $G \textbackslash \langle a \rangle$.  Let $b \in G \textbackslash \langle a \rangle$. Thus, $|b|=2$ or $|b|=p$. 

By Lagrange's theorem, $\langle a \rangle \cap \langle b \rangle$ is a subgroup of $\langle a \rangle$ for $|\langle a \rangle | =p$. For $b \not \in \langle a \rangle$, then $\langle a \rangle \cap \langle b \rangle \neq \langle a \rangle$, and thus $|\langle a \rangle \cap \langle b \rangle|=1$. If $|b|=p$, then by $7.2$ we obtain that: 

$$|\langle a \rangle \cdot \langle b \rangle   =  \frac{ |\langle a \rangle| \cdot |\langle b \rangle |  }{ |\langle a \rangle \cap  \langle b \rangle | }=\frac{p^2}{1}=p^2 $$

But since $p>2$ then we have that $p^2 >2p$. It therefore must be the case that $|b|=2$. From this we are able to deduce that:

$$G=\langle a \rangle \cup \langle a \rangle b = \{ e,a,a^2, \cdots, a^{p-1}, b,ab, ab^2, \cdots, ab^{p-1} \}$$

From here we must show that the resulting group that we have obtained for $G$ has only possible [[Cayley Table]] for $G$, since $D_p$ is a group of order $2p$, then we would expect that $G \cong D_{p}$.  

If there are $2$ non-isomorphic finite groups of the same order then their multiplications are different. 

For $ab \not \in \langle a \rangle$, we have that $|ab|=2$ since we showed that any element in $G\textbackslash \langle a \rangle$ is $2$. Therefore we have that:

$$(ab) ^2 = e \iff bab=a^{-1}$$

Repeated multiplication of $a^{j}$ are of the form:

$$a^{-j} = ba^jb : j \in \mathbb{N}$$

There are $4$ types of products here: 

1. $a^i \circ a^j = a^{i+j}$

2. $a^i \circ (a^jb)=a^{i+j}b$

3. $(a^ib) \circ a^j=a^iba^jb^2=a^iba^j b\cdot b =a^ia^{-j}b=a^{i-j}b$

4. $(a^ib)(a^jb)=a^i(ba^jb)=a^ia^{-j}=a^{i-j}$

When $p>2$ is prime and $G$ doesn't have an element of order $2p$ then $G$ must have an element of order $2p$ then $G$ must have an element $a$ of order $p$ and an element $b$ of order $2$, and since $|G|=2p$, and $|a|=p,|b|=2$, which completely determines the table for $G$, and thus $G \cong D_{p}$ in this case. 

In either case we have that $G \cong D_{p}$ OR $G \cong \mathbb{Z}_{2p}$ for $|G|=2p$. 

---
