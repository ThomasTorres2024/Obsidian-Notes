---
title: Isomorphism
tags:
  - AbstractAlgebra
draft: "False"
---
# Isomorphism 
An [[Isomorphism]] is a bijective function which maps between two [[Group]]s, $G_1$ and $G_2$ denoted by $\phi$ with the special property that for, $a,b$ that:
$$\phi(ab)=\phi(a) \phi(b)$$
Which is equivalent to saying that the [[Binary Operation]] of $G_1$ on the group elements and then taking the isomorphism of that result is equivalent to applying the isomorphism to $a,b$ separately and then applying the [[Binary Operation]] of $G_{2}$. 

If groups $G_{1}$ and $G_{2}$ are isomorphic, we denote this via:
$$G_{1} \equiv G_{2}$$
Since $\phi$ is bijective, it also must clearly be the case that $|G_{1}|=|G_{2}|$ 

---
# Properties of Isomorphisms $\textcolor{red}{(Theorem)}$ 
Suppose that $\phi$ is an isomorphism from a group $G_{1} \mapsto G_{2}$, then:

1. $\phi$ maps the identity of $G_{1}, e_{G_{1}}$ to the identity of $G_{2}$, $e_{G_{2}}$. 

2. For every integer $n$ and every group element $a \in  G_{1}$, $\phi(a^n)=(\phi(a))^n$

3. For any elements $a,b \in G_{1}$ $ab$ commute iff $\phi(a)\phi(b)$

4. $G_{1} = \langle a \rangle \iff G_{2} = \langle \phi(a) \rangle$

5. $|a|=|\phi(a)| : \forall a \in G_{1}$

6. For a fixed integer $k$ and a fixed group element $b \in G_{1}$, the equation $x^k =b$ has as many solutions in $G_{1}$ as $y^k = \phi(b)$ in $G_{2}$

7. If $G_{1}$ is finite then $G_{1},G_{2}$ have exactly the same number of elements of every order.


### Proof 1, $\phi(e_{G_{1}})=e_{G_{2}}$
$$\phi(e_{G_{1}})=\phi(e_{G_{1}} \cdot e_{G_{1}})= \phi(e_{G_{1}}) \phi(e_{G_{1}}) \iff \phi(e_{G_{1}}) \cdot \phi(e_{G_{1}}) = \phi(e_{G_{1}})$$
$$ \phi(e_{G_{1}}) \phi(e_{G_{1}}) \phi(e_{G_{1}})^{-1} = \phi(e_{G_{1}}) \cdot \phi(e_{G_{1}})^{-1} \iff \phi(e_{G_{1}}) = e_{G_{2}}$$
### Proof 2, $\phi(a^n)=(\phi(a))^n$
We can prove this inductively. First assume $n\geq 0$. The base case for $n=0$ is trivial. Secondly, for the inductive hypothesis assume the following holds:
$$\phi(a^{n-1})=\phi(a)^{n-1}$$
Now let us consider $\phi(a^n)$:
$$\phi(a^n)=\phi(a \cdot a^{n-1})=\phi(a) \cdot \phi(a^{n-1})=\phi(a)^1 \cdot \phi(a)^{n-1}=\phi(a)^n $$
Therefore, via induction:
$$\phi(a^n)=(\phi(a))^n$$
holds for $n \in \mathbb{N}$. For $n \in \mathbb{Z}$ I think the result generalizes, since if $n <0$ then we can write the expression above as:
$$\phi((a^{-1})^n)=\phi(a^{-1})^n$$
Which should clearly hold since $a^{-1}$ is an arbitrary element in $G_{1}$.
$$$$
### Proof 3, $ab$ and $ba$ commute $\iff \phi(a)$ and $\phi(b)$ commute
#### 1.) $\implies$
Assume $ab=ba$. Then:
$$\phi(a) \phi(b) =\phi(ab)=\phi(ba)=\phi(b) \phi(a)$$
#### 2.) $\Longleftarrow$
Assume $\phi(a)\phi(b)=\phi(b)\phi(a)$ then:
$$\phi(a)\phi(b) =\phi(ab) = \phi(b)\phi(a) = \phi(ba) \iff \phi(ab)= \phi(ba) \iff ab=ba$$
Since $\implies, \Longleftarrow$, then  $ab$ and $ba$ commute $\iff \phi(a)$ and $\phi(b)$ commute.

#### Proof 4.) $G_{1} = \langle a \rangle \iff G_{2} = \langle \phi(a) \rangle$

#### 1.) $\implies$
Let $G_{1} = \langle a \rangle$. 
By closure of groups it follows that:
$$\large \langle \phi(a) \rangle \subseteq G_{2}  $$
Consider any $b \in G_{1} \implies b=a^k: k \in \mathbb{Z}$. Then for $\phi (b) \in G_{2}$
$$\large \phi(b)=\phi(a^k)=[\phi(a)]^k \implies G_{2} \subseteq \langle \phi(a) \rangle \implies G_{2} = \langle \phi(a) \rangle $$

#### 2.) $\Longleftarrow$ 
Let $G_{2} = \langle \phi(a) \rangle$:
By closure it follows that:
$$\langle a \rangle \subseteq G_{1}$$
Consider $b \in G_{2}$, then $b=\phi(a)^k=\phi(a^k)$. Then,
$$\phi^{-1}[\phi(a^k)] \in G_{1}$$
Furthermore, $G_{1} \subseteq \langle a \rangle \implies G_{1} =\langle a \rangle$.

Since $\implies, \Longleftarrow$ it follows that $G_{1} = \langle a \rangle \iff G_{2} = \langle \phi(a) \rangle$. 

### Proof 5.) $\large |a|= |\phi(a)| : a \in G_{1}$ 
Let $|a|=n : n \in \mathbb{N}$ Then:
$$|a| = n \implies a^k = e_{G_{1}} \iff \phi(a^n) = \phi(e_{G_{1}}) = \phi(a)^n = e_{G_{2}}$$
So $|\phi(a)| \leq n$. Consider the order of $|\phi(a)|$ and let it be denoted by $k$: 

Thus:
$$\large \phi(a)^k = e_{G_{2}} \iff \phi(a^k) =e_{G_{2}} \iff a^k = e_{G_{1}}$$
And thus $k=n$ so it must also be the case that $|\phi(a)|=n$. 

### Proof 6.) $x^k=b$ and $y^k = \phi(b)$ have the same number of solutions.
Let $x^k=b$ for $b \in G_1$ have $k$ many solutions in $G_1$. Then:
$$x^k=b \iff \phi(x^k) = \phi(b) \iff \phi(x)^k = \phi(b)$$
If we denote $\phi(x)=y$ then:
$$y^k=\phi(b)$$
as desired. 

### Proof 7.) If $G_{1}$ and $G_{2}$ are finite then both groups have the same number of elements of each order 
By $5.$ it should be clear that for each $a \in G_1$ where each $a$ has order $n$, it follows that the item mapped to has the same order. Thus there is the same number of elements of each order in both groups. 

# Properties of Isomorphisms Acting on [[Group]]s $(\textcolor{red}{Theorem})$ 

Suppose that $\phi$ is an isomorphism from a group $G_1$ to a group $G_{2}$, then:
1. $\phi^{-1}$ is an isomorphism from $G_{2} \mapsto G_{1}$
2. $G_{1}$ is Abelian $\iff$ $G_2$ is [[Abelian Group]]
3. $G_{1}$ is cyclic $\iff G_{2}$ is [[Cyclic Group]] 
4. If $K_{1} \leq G_{1}$, then $\phi(K_{1}) = \{ \phi(k) : k \in K_{1} \}$
5. If $K_{2} \leq G_{2}$, then $\phi^{-1}(K_{2})$ is a [[Subgroup]] of $G_{1}$
6. For the [[Group Center]], we have that: $\phi(Z(G_{1})) = Z_(G_{2})$

### 1. $\phi^{-1} : G_{2} \mapsto G_{1}$ is an Isomorphism 
##### $\textcolor{red}{Proof.)}:$ 
Since $\phi$ is a bijection, then clearly $\phi^{-1}$ is a bijective function. 
Let $a,b \in G_{1}$ and let $c=\phi(a),d=\phi(b)$, then:
$$\phi(ab)=\phi(a)\phi(b)=cd$$
$$\phi^{-1}(ab)=cd=\phi^{-1}(a)\phi^{-1}(b)$$
Notice that now we have satisfied the homomorphic part and the bijective part, so thus $\phi^{-1}$ is an [[Isomorphism]]. 

### 4.)  If $K_{1} \leq G_{1}$, then $\phi(K_{1}) = \{ \phi(k) : k \in K_{1} \}$
$\textcolor{red}{Proof.)}$ 
It can be shown that $K_{1}$ is a subgroup of $G_1$ using the two element subgroup test. 


---
# Tests for Isomorphism: 
If any of the following conditions are satisfied, it is the case that, $G_1$ and $G_2$
$$G_1 \not \cong G_{2}: $$
1. $|G_{1} | = |G_{2}|$
2. Show either $G_1$ or $G_{2}$ is cyclic, but the other is not. 
3. Show either one is abelian but the other is not 
4. Show that the largest order of any element in $G_1$ is not the same as the largest order of any element in $G_2$ 
5. Show that the number of elements of some specific order in $G_1$ is not the same as the number of elements of that order in $G_{2}$
# Definition.) [[Automorphism]] 
An [[Automorphism]] is an [[Isomorphism]], given by $\phi : G \mapsto G$. 

---
# Cayley's Theorem
Every [[Group]] is isomorphic to a group of [[Permutation]]s. Let $G$ be a group, and let $T_{g}(x)=gx : x \in G$ be a map from $G$ to $\widetilde{G}$.  

Clearly, $T_{g}$ is a permutation of $G$ It can be argued that $T_{g}(x)$ is onto, due to properties of closure by groups we should be able to argue that $T_{g}(x)$ is still a group, and also that $T_{g}(x)$ is injective. 

Now let us define the group of all of the permutations by:
$$\large \widetilde{G}= \{ T _{g} : g \in G \}$$
Thus $\widetilde{G}$ is a [[Group]] under function composition. It can be shown that This is a group easily. It is well known that the composition of functions is associative so that is satisfied. It is also closed for $g,h \in G$:
$$T_{g}(T_{h}(x)) = T_{g}(hx)=ghx=T_{gh}(x) \implies \text{closure under comp}$$
Clearly, $T_e$ is the identity mapping and $T_{g^-1}$ is the inverse of $T_{g}$. So, $\widetilde{G}$ is a group. Now we can define the [[Isomorphism]] between the groups, $\phi : G \mapsto \widetilde{G}$: 

For $g \in G$, let $\phi(g) = T_{g}$. It can be shown that it is bijective:
$$\phi(g)=\phi(h) \iff T_{g}(x) =T_{h}(x) \iff gx = hx \iff g = h$$
Thus $\phi$ is injective. It is also clearly onto since for $g \in G$, we have $T_g \in \widetilde{G}$. It can also be shown to preserve the operation:
$$\phi(gh)=T_{gh}(x)=T_{g}T_{h}=\phi(g)\phi (h)$$
Thus, $\phi$ is bijective and operation preserving, so it is an isomorphism:
$$\therefore G \cong \widetilde{G} $$ Also note that the group we just constructed is known as the "left regular representation of $G$". 

---
# Examples 


### Ex 1.)
Given, $G_{1}=(\mathbb{R},+)$ and $G_{2}=((0,\infty),\cdot )$ we can construct the following 















