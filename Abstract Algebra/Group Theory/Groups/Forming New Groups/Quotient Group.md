---
title: Quotient Group
tags:
  - AbstractAlgebra
draft: "False"
---
# Quotient Group
A [[Quotient Group]] is constructed from taking a group $G$ and a [[Normal Subgroup]] of $G$, namely $H$, and then considering the sum of [[Coset]]s of $H$ over $G$. 

Also $\left|\frac{G}{H} \right|=[G:H]$ via [[Lagrange's Theorem]] since this is the total number of cosets of $H$ over $G$. 
# Theorem .) Quotient Groups 
Let $G$ be a group and let $H$ be  normal subgroup of $G$. Then the following is a group under the following operation: 

$$\begin{align}
\frac{G}{H}= \{aH :  a \in G \} \\
(aH)(bH)=abH
\end{align}$$
$Proof.)$ Since we are working with cosets and thereby [[Equivalence Class]]es we need to check that the group operation is well defined and not dependent on the choice of representation. 

We would like to be able to show that:
$$aH=a'H,bH=b'H \iff abH=a'b'H$$

By the definition of coset we have that $a'=ah_{1},b'=bh_{2}$ for some $h_{1},h_{2} \in H$. Then, it follows that:
$$\begin{align}
a'b'H=ah_{1}bh_{2}H \\
=ah_{1}bH \\
=ah_{1}Hb  \\ 
=aHb \\
=abH
\end{align}$$
The last and third equalities come from the fact that $H \triangleleft G$. 

We inherit associativity from $G$. We also have that $eH$ is the identity coset of $\frac{G}{H}:$
$$(aH)(eH)=aeH=aH$$
$$(eH)(aH)=eaH=aH$$
And $a^{-1}H$ is the inverse of each $aH \in \frac{G}{H}$ since the following holds: 
$$(a^{-1}H)(aH)=a^{-1}aH = eH \in H$$
$$(aH)(a^{-1}H)=aa^{-1}H=eH \in H$$
$\therefore \frac{G}{H}$ is a group under the defined operation. 

### Remark .) Converse of [[Quotient Group]]
The converse of the above theorem is true, namely that if $aHbH=abH$ defines a group operation of left cosets of $H$ in $G$ then $H \triangleleft G$. 

### Remark .) Quotient Group with Right Cosets 
Using right cosets would also work, and furthermore we would get a group that is isomorphic to the one we obtained using left cosets. 

---
### Example 1.) 
For $4 \mathbb{Z}$ we know that the following are distinct cosets in $\mathbb{Z}$:
$$\begin{align}
0 + 4\mathbb{Z} = \{ \cdots, -4,0,4,8, \cdots \} \\
1 + 4\mathbb{Z} = \{ \cdots, -3,1,5,9, \cdots \} \\
2 + 4\mathbb{Z} = \{ \cdots, -2,2,6,10, \cdots \} \\
3 + 4\mathbb{Z} = \{ \cdots, -1,3,7,11, \cdots \}
\end{align}$$
We claim that the above cosets of $4\mathbb{Z}$ over $\mathbb{Z}$ are distinct. Let $k \in \mathbb{Z}$. By the division algorithm we have that: 
$$k=4q+r \quad 0 \leq r < 4$$
So that:
$$k+4\mathbb{Z}=(4q+r)+4\mathbb{Z}=r+4\mathbb{Z}$$
And since $0\leq r < 3$, this coset is thus one of the $4$ cosets listed above. Furthermore, since $\mathbb{Z}$ is an Abelian group then it trivially follows that $4\mathbb{Z} \triangleleft \mathbb{Z}$. 

We thus obtain the following [[Quotient Group]] and here is its respective Cayley Table:

| $+$             | $3+4\mathbb{Z}$ | $0+4\mathbb{Z}$ | $1+4\mathbb{Z}$ | $2+4\mathbb{Z}$ |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| $0+4\mathbb{Z}$ | $3+4\mathbb{Z}$ | $0+4\mathbb{Z}$ | $1+4\mathbb{Z}$ | $2+4\mathbb{Z}$ |
| $1+4\mathbb{Z}$ | $0+4\mathbb{Z}$ | $1+4\mathbb{Z}$ | $2+4\mathbb{Z}$ | $3+4\mathbb{Z}$ |
| $2+4\mathbb{Z}$ | $1+4\mathbb{Z}$ | $2+4\mathbb{Z}$ | $3+4\mathbb{Z}$ | $0+4\mathbb{Z}$ |
| $3+4\mathbb{Z}$ | $2+4\mathbb{Z}$ | $3+4\mathbb{Z}$ | $0+4\mathbb{Z}$ | $1+4\mathbb{Z}$ |
From this we obtain that $4+4\mathbb{Z} \to k$ is an isomorphism from $\frac{\mathbb{Z}}{4\mathbb{Z}} \to \mathbb{Z}_{4}$. Generally it is the case that $\frac{\mathbb{Z}}{n\mathbb{Z}} \cong \mathbb{Z}_{n}$ for any $n$. 

### Example 11.)  $G=\mathbb{Z}_{18},H=\langle 6 \rangle = \{0,6,12 \}$. 
Since $G$ is Abelian then $H \leq G \implies H$ is Abelian and thus normal. We also obtain that: 

$$\frac{G}{H}=\{0+H,1+H,2+H,3+H,4+H,5+H \}$$
For example if we consider the group operation we can obtain: 
$$\begin{align}
(4+H)+(5+H)=(5+4)+H \\
=9+H \\
=3+6+H \\
=3+(6+H) \\
=3+H
\end{align}$$
Also recall that via Lagrange's theorem that 

---
# Corollary 1.) $|G/H|$
If $G$ is a finite group and $H \triangleleft G$ then:
$$|G/H|=[G:H]=\frac{|G|}{|H|}$$
$Proof.$ $|G/H|$ is the number of distinct cosets of $H$ in $G$ which is the definition of $[G:H]$. By [[Lagrange's Theorem]] this is equivalent to $\frac{|G|}{|H|}$. 

### Corollary 2.) $|G/K|=|G/H|\cdot |H/K|$
Suppose $G$ is a finite group and $H,K$ are normal subgroups of $G$ with $H \triangleleft  G$ and $K \triangleleft H$ then:
$$|G/K|=|G/H|\cdot |H/K|$$
This is obvious from Lagrange if we apply it to $[G:K]$, and then to $[G:H]$, and then to $[H:K]$. 

---
# Theorem .) Applications of Quotient Groups $\frac{G}{Z(G)}$
Let $G$ be a group and let $Z(G)$ be the [[Group Center]] of $G$ such that $Z(G) \triangleleft G$. If the only [[Coset]] of $\frac{G}{Z(G)}$ is the identity coset $G$ it follows that $G=Z(G)$. Showing that this result is true would be enough to prove the result. 

If $\frac{G}{Z(G)}$ is cyclic then $G$ is an [[Abelian Group]]. 

$Proof.$ 
If $G$ is [[Abelian Group]] then $Z(G)=G$. 
If the only [[Coset]] of $\frac{G}{Z(G)}$ is the identity coset $G$ it follows that $G=Z(G)$. Showing that this result is true would be enough to prove the result. 

We can begin. By properties of $Z(G)$ (that it is a center) $Z(G) \triangleleft G$ and thus $\frac{G}{Z(G)}$ automatically is a valid group under addition of cosets. Furthermore since $\frac{G}{Z(G)}$ is assumed cyclic we can write that for some $g \in G$ that $\langle g Z(G)\rangle=\frac{G}{Z(G)}$

Let the element $a \in G$ and then let $i \in \mathbb{Z}$ such that: 

$$aZ(G)=(gZ(G))^i=g^iZ(G)$$
This equality follows from the fact that $aZ(G) \in \frac{G}{Z(G)}$ and since $\frac{G}{Z(G)}$ is cyclic we know that it can be expressed in that fashion. 

Therefore we obtain the following if we notice now that $a=g^i$:
$$a\cdot g=(g^iz)(g)=g^{i+1}z$$
$$g\cdot a=g(g^{i}z)=g^{i+1}z$$
And thus we obtain that $ag=ga$. Since $a \in G$ was chosen arbitrarily, it follows that $g\in Z(G)$. Therefore we have that $gZ(G)=Z(G)$ (follows via properties of cosets). Thus we have that:
$$\frac{G}{Z(G)}=\langle g Z(G) \rangle = Z(G)$$
$\therefore$ Since we have showed that $\frac{G}{Z(G)}$ is only the identity coset, $Z(G)$ it follows that $G=Z(G)$ and therefore $G$ must be an [[Abelian Group]]. 

It is important to note that this theorem works for any $H$ which is a [[Cyclic Group]], and $H \leq Z(G)$, then $G$ is an [[Abelian Group]]. 

Furthermore, we often tend to use the contrapositive of the above statement, namely that if $G$ is not an [[Abelian Group]] then $\frac{G}{Z(G)}$ is not a [[Cyclic Group]]

---
# Example 15.) 
Suppose $G,H$ are groups where $H \triangleleft G$ and that $\bar{K}=\{H,a_{1}H,a_{2}H,a_{3}H \}$ is a subgroup of $\frac{G}{H}$ of order $4$. 

Then:
$$K = H \cup a_{1}H \cup a_{2}H \cup a_{3}H$$
Gives that $K$ is a [[Subgroup]] of $G$ of order $4|H|$. 

To see this, let $a_{0}=e$ and:
$$a_{i},a_{j} \in \{ a_{0},a_{1},a_{2},a_{3} \}$$
Thus for any $a_{i}h_{i},a_{j}h_{j} \in K$ we have that: 
$$(a_{i}h_{i})(a_{j}h_{j}) \in (a_{i}H)(a_{j}H)=a_{k}H$$
For $0 \leq k \leq 3$ so that $K$ is closed under multiplication. We can also show that $K$ is closed under inverses. Let $a_{i},h_{i} \in K$, then since $\bar{K}$ is a group, $\exists j, 0 \leq j \leq 3$ and $h \in H$ such that:
$$(a_{i}h_{i})(a_{j}h_{j})=h \iff a_{i}Ha_{j}H=H$$

Since we have that $H \triangleleft G$ then $\exists h'$ such that $a_{i}h_{i}=h'a_{i}$, which gives:
$$h'a_{i}a_{j}h_{j} = h$$

Then we have by cancellation:
$$a_{i}a_{j}=(h')^{-1}h(h_{j})^{-1}=h'' \in H$$
And thus we have that:
$$a_{i}^{-1}h'' = a_{j} \iff a_{i}^{-1}=a_{j}(h'')^{-1} \in K$$
Thus we have that the group is closed under inverses, and we know that $H$ is also closed under multiplication then we obtain that: 
$$(a_{i}h_{i})^{-1}=h_{i}^{-1}a_{i}^{-1} \in K$$
Thus by the $2$ step subgroup test then we have that $K\leq G$ and also we have that $e \in K \implies K !=\emptyset$. 

### Example $16$.) Suppose $G$ is a finite group for which there is a factor group $\frac{G}{H}$ which has an element $aH$ of order $n$ 
__Claim__ $G$ also has an element of order $n$. In order to see this, let $|a|=k$, so $a^k=e$. Then in $\frac{G}{H}$ we have that:

$$(aH)^k=a^kH=H$$
We thus know that $|aH|\leq k \implies |aH|=k=mn$ for $m \in \mathbb{N}$.

Then we have that: 
$$(a^m)^n = a^k =e$$
By definition of $k$ as $|a|$ in $G$, $n$ is as small as possible so that $|a^m|=n$. This concludes the proof since:
$$(a^mH)^n=a^{mn}H=H$$
And $n$ is minimal. 

---
# Theorem ). For group $G$ then $\frac{G}{Z(G)} \cong \text{Inn}(G)$
For any group $G$ then $\frac{G}{Z(G)} \cong \text{ Inn}(G)$ the group of Inner [[Automorphism]]s of $G$. 

$Proof.)$ Consider the correspondence from $\frac{G}{Z(G)} \to \text{ Inn}(G)$ which is given by:
$$T:gZ(G) \to \phi_{g}$$
Where each $\phi_{g}=\phi_{g}(x)=gxg^{-1}$, an inner automorphism. First it can be shown that $T$ is well defined.

If $gZ(G)=hZ(G)$ then we need to show that $\phi_{g}=\phi_{h}$. 

If $gZ(G)=hZ(g)$ then $h^{-1}g \in Z(G)$ via properties of cosets. By the definition of $Z(G)$ as the set of elements of $G$ which commute with every element of $G$, if $x \in G$ then: 
$$\begin{align}
(h^{-1}g)x=x(h^{-1}g) \\
gx=hxh^{-1}g \\
gxg^{-1}=hxh^{-1} \\
\iff \phi_{g}(x)=\phi_{h}(x)
\end{align}$$
We thus obtain that the cosets are well defined. Furthermore the argument is reversible giving injectivity. Secondly, we can show subjectivity but this is pretty obvious for $\phi_{g}$ since clearly $g \in G$ works. 

Thus there is a $1-1$ correspondence between both groups. Now it needs to be shown that it is Homomorphic. 

$$\phi(gx)=\phi_{gh}=xghx^{-1}=xgx^{-1} \cdot xhx^{-1} = \phi(g)\phi(h)$$
$$\therefore \frac{G}{Z(G)} \cong \text{Inn}(G)$$
---
### Example 17.)
Recall that $|Z(D_{4})|=2$, namely that $Z(G)=\{R_{0},R_{\pi} \}$.Then:
$$|D_{6}/Z(D_{6})|=\frac{12}{2}=6$$
By the theorem classifying groups of order $2p$ then we know that $\text{Inn}(D_{6})$ is isomorphic to either $D_{3}$ or to $\mathbb{Z}_{6}$. But, if $\text{Inn}(D_{6})$ were cyclic then by properties of isomorphism $\frac{D_{6}}{Z(D_{6})}$ would also be a cyclic group since it would be isomorphic to $\mathbb{Z}_{6}$. 

But, this would make $D_{6}$ Abelian but it is clearly not, thus $\text{Inn}(D_{6})\cong D_{3}$. 

---
# Theorem .) Cauchy's Theorem for Abelian Groups 
Let $G$ be a finite Abelian group and let $p$ be a prime which divides the order of $G$. Then $G$ contains an element of order $p$. 

$Proof.)$ Result is trivial for $|G|=1$ and $|G|=2$. Suppose that $|G|>2$ and assume the result is true for every finite Abelian group with less elements than $G$ for the induction hypothesis. 

First observe that $G$ has elements of prime order. If $x\in G$ and $x\neq e$ and $|x|=m$ and $q$ is a prime which divides $m$ such that $m=qn$ for some $n \in \mathbb{N}$. Then it follows that:
$$x^{m}=(x^n)^q \implies |x^n|=q$$
If $q=p$ then we re done, so assume that $q\neq p$ now. Since $G$ is Abelian and every subgroup of $G$ is an Abelian and therefore normal group, the following [[Quotient Group]] ca be constructed of the form $\bar{G}=\frac{G}{\langle x \rangle }$. 

Then $\bar{G}$ is Abelian and $p\bigg||\bar{G}|$ since $|\bar{G}| = \frac{|G|}{q}$ and $q \neq p$.  By the inductive hypothesis $\bar{G}$ contains an element of order $p$ and by example $16$ $G$ also contains an element of order $p$. 


