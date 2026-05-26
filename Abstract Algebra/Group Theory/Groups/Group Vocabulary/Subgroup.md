---
title: Subgroup
tags:
draft: "False"
---
# Subgroup
Let $H \subseteq G$ where $H,G$ are both [[Group]]s. If $H$ is a [[Group]] under the [[Binary Operation]] of $G$, then we can call $H$ a [[Subgroup]] of $G$. 

We denote a subgroup by $H \leq G$ or $H < G$ if we have a proper subset of $G$. 

There are two trivial subgroups. The group which consists exclusively of the [[Identity Element]], and the group where $H=G$, that is a [[Group]] is a subset of itself. 

#### (Theorem 3.1) Subgroup Test 
Let $G$ be a [[Group]] and let $H \subseteq G : H \neq \emptyset$.  Then it follows that, if $H$ is a [[Subgroup]] of $G$ iff $ab^{-1} \in H, \forall a,b \in H$.  Note, it is extremely important to demonstrate $H \neq \varnothing$ in addition to $ab^{-1} \in H$, so the non-emptiness of $H$ should not be ignored. 
#### Direction 1.) $\implies$ 
Since $H$ is a group, $b \in H \implies b^{-1} \in H$. Furthermore $ab^{-1} \in H$ since $H$ is closed under its own [[Binary Operation]].
#### Direction 2.) $\Longleftarrow$ 
Suppose $H$ satisfies the condition given by $(\star)$: $$(ab^{-1} \in H, \forall a,b \in H)$$ Let $H$ and $G$ share the same [[Binary Operation]]. Since the same operation is shared and $G$ is a group, it follows that $H$ is associative. 

We want to argue that $H$ contains an [[Identity Element]] as well. Since $H \neq \varnothing$
then $\exists x \in H$. Let $a=x,b=x$ then:
$$ab^{-1} \in H \iff xx^{-1} =e$$
So $H$ contains the [[Identity Element]]. Since we have $e$, we can show inverses now. Let $a=e$ and $b=x$. So:
$$ ab^{-1} \in H \iff  e \circ x^{-1} = x^{-1} \in H$$ So each element has its own inverse. If $x,y \in H$, then we need to show that $xy \in H$. Let $b^{-1} = y^{-1}$. Then by our assumption:
$$xy \in H$$
$$\therefore H \text{ is a subgroup of G iff } ab^{-1} \in H, \forall a,b \in H$$
#### (Theorem 3.2) Two-Step Subgroup Test 
Let $G$ be a [[Group]] and let $:H \neq \varnothing$ and $H \subseteq G$. 

Then, $H \leq G \iff$ to the following 2 conditions:
* $ab \in H, \forall a,b \in H$
* $a^{-1} \in H, \forall a \in H$. 

#### Direction 1.) $\implies$ 
We assume that $H \leq G$. By the definition of a group, $ab \in H$ and $a \in H \implies a^{-1} \in H$. 

#### Direction 2.) $\Longleftarrow$
We assume for $H \subseteq G, a,b \in H, a^{-1} \in H$. We also assume $ab \in H$. 
Let $b=a^{-1}$. Then for $ab=aa^{-1}=e \in H$, so $H$ contains the [[Identity Element]]. 
We know $H$ is associative since we inherit the [[Binary Operation]] from $G$. We assume that we have an inverse element so that is given. We also assume closure. Therefore, it follows that $H \leq G$ since the group axioms are satisfied:
$$\therefore H  \leq G$$
### Show that a subset $S$ of a [[Group]] is not a [[Subgroup]]
We can show that $S$ is not a subgroup of $G$ for $S \subseteq G$ if any of the follow conditions fails:
* [[Identity Element]] $e \not \in S$. 
* Find some $a \in S$ such that $a^{-1} \not \in S$
* Find $a,b \in S$ where $ab \not \in S$

### Theorem 3.3 Finite [[Subgroup]] Test 
Let $H \subseteq G$ s.t. $H \neq \varnothing$. We can prove that $H \leq G$ iff $H$ is closed under the operation of $G$. 

###### Proof
$1.) \implies$ 
Since $H \leq G$, by theorem 3.2, we showed that being a subgroup entails closure. So, since $H \leq G$ we know $H$ must be closed. 

$2.) \Longleftarrow$ 
We assume for any $a.b \in H$ that $ab \in H$ by this direction. We need to only show that $a \in H \implies a^{-1} \in H$. Since $H$ is assumed non-empty, let $a=e$. Then, we have that $a^{-1}=e$. 

If $a \neq e$, then for $a,a^2,a^3,\dots$ it must be the case that for some $n$ that $a^n=e$. This is a property of $H$ being a [[Finite Group]]. The sequence must repeat at some point. 

So:
$$a^i = a^j: i > j$$
Using cancellation:
$$a^{i-j}=e$$
We have that $a \neq e$ so $i-j >1$. 
So we have that:
$$aa^{i-j-1}=a^{i-j-1}a=e$$
So $a^{-1}=a^{i-j-1}$. By the uniqueness of inverses, $a$ has an inverse element.

Therefore since we have shown both directions, $H \leq G \iff H \text{ is closed}$

---
# Examples 
##### Example 1.) Let $G$ be an Abelian Group with the condition that $H=\{x \in G : x^2 = e \}$. 

Note that $H \neq \varnothing$ since $x=e$, $e^2=e$ satisfies the condition so $H$ is not null. We can apply the [[Subgroup]] test. 

Let us assume that $a^2 = e, b^2=e$. We want to show that $ab^{-1} \in H$ using the [[Subgroup]] test. Let us then express that:
$$(ab^{-1})^2=(ab^{-1})(ab^{-1})$$Then since $G$ is assumed Abelian:
$$=(a^2(b^2)^{-1})=(e\cdot e)=e \in H$$
Thus, $(ab^{-1})^2 \in H$. 

##### Example 2) Let $G$ be an Abelian Group with identity $e$ then $H=\{x^2|x \in G\}$ is a [[Subgroup]] of $G$. $H$ is the set of squares in $G$. 

Notice $e \in H$ since $e^2=e \in G$. We want to try and use the [[Subgroup]] test. Suppose that for $a,b \in G$ we have $a^2,b^2 \in H$:
$$a^2(b^2)^{-1}=a^2(b^{-1})^2=(ab^{-1})(ab^{-1})$$
This step is allowed because $G$ is assumed Abelian. Then:
$$=(ab^{-1})^2$$
Note that $ab^{-1} \in G$, so $(ab^{-1})^2 \in H$. 
$$\therefore H \leq G$$
##### Example 3) Let $G$ be an Abelian Group. 
Let $H=\{ x \in G : |x| \text{ is fininite } \}$.  It can be shown that $H \leq G$. 

Note that $H \neq \varnothing$ since the [[Identity Element]], $e \in H$ since $|e|=1$. Let $a,b \in H$. Let $|a|=m,|b|=n$. Now, let us consider $ab$ and if $|ab|$ is finite. 

Let us consider $(ab)^{mn}$:
$$(ab)^{mn}=a^{mn} \circ b^{mn}=(a^m)^n\circ (b^n)^m=e^n\circ e^m =e \in H$$
So, $|ab| \leq mn \implies |ab| \text{ is finite}$.  

Now to show that $a^{-1 }\in H$. Notice that:
$$(a^{-1})^m=(a^m)^{-1}=e^{-1}=e \implies |a^{-1}| \text{ is finite}$$
Since $ab\in H, a^{-1} \in H\implies H \text{ is a subgroup of } G$ 
##### Example 4) Let $G$ be an Abelian Group where $H,K$ are [[Subgroup]]s of $G$ 
Let $HK=\{  hk : h \in H, k \in K\}$, then $HK$ is a [[Subgroup]] of $G$. 
We have that $H \leq G$ and $K \leq G$, so the identity element $e \in G$, then $e \in H, e \in K$. 
We know that $HK \neq \varnothing$ since it contains $e=e\circ e$. 

We can use the two condition subtest. We want to show that $\forall a,b \in H$ that $ab \in H$. Secondly, we want to show that for $a \in H, \exists a^{-1} \in H$. 

Let $a,b \in HK$, Then, $a=a_Ha_K$ and $b=b_Hb_K$. Consider the product $ab$:
$$ab=(a_Ha_K)(b_Hb_K)$$
Since $G$ is abelian, then:
$$=(a_Hb_H)(a_Kb_K) \in HK$$
This satisfies condition 1 of the 2 part subgroup test. 

Now consider $a$ again. 
$$a=a_Ha_K$$
Since $HK$ consists of all products of elements in the subgroups $H$ and $K$. Since $a_H \in H \implies a_H^{-1}\in H$ and $a_K \in K \implies a_K^{-1} \in K$  

Therefore the product $a_H^{-1}a_K^{-1} \in HK$. But since $G$ is abelian, we know that the product $a_K^{-1}a_H^{-1} \in HK$. But notice that this is the inverse of $a$ (algebraically verifiable, very easy to do not texxing it here).

Therefore since the first and second conditions of the [[Subgroup]] test are verified, it follows that $HK$ is a subgroup of $G$. 

#### Example 5.) Consider $G= \mathbb{R}\textbackslash \{0\}$ under mult. 
$$H=\{x \in G: x=1 \lor x \not \in \mathbb{Q} \}$$
$$K=\{x \in G:x \geq 1 \}$$

$H$ is not a subgroup because it is not closed. $a=\sqrt{2} \in H$. Let $a=b$. $ab=4$. $ab \not \in H$, therefore the first criteria of the [[Subgroup]] test fails, so $H$ is not a subgroup of $G$. 

For $K$, consider $a=4 \in G$. Notice that $a^{-1}=1/4 \not \in G$. Thus $\exists a \in K$ such that $\not \exists a^{-1} \in K$. 

#### Example 6.) [[Abstract Algebra/Group Theory/Special Groups/Cyclic Group|Cyclic Group]] (Read More Here)


