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
Let $G$ be a [[Group]] and let $H \subseteq G : H \neq \emptyset$.  Then it follows that, if $H$ is a [[Subgroup]] of $G$ iff $ab^{-1} \in H, \forall a,b \in H$.   

#### Direction 1.) $\implies$ 
Since $H$ is a group, $b \in H \implies b^{-1} \in H$. Furthermore $ab^{-1} \in H$ since $H$ is closed under its own [[Binary Operation]].

#### Direction 2.) $\Longleftarrow$ 
Suppose $H$ satisfies $(\star)$ "$(ab^{-1} \in H, \forall a,b \in H)$". Let $H$ and $G$ share the same [[Binary Operation]]. Since the same operation is shared and $G$ is a group, it follows that $H$ is associative. 

We want to argue that $H$ contains an [[Identity Element]] as well. Since $H \neq \varnothing$
then $\exists x \in H$. Let $a=x,b=x$ then:
$$ab^{-1} \in H \iff xx^{-1} =e$$
So $H$ contains the [[Identity Element]]. Since we have $e$, we can show inverses now. Let $a=e$ and $b=x$. So:
$$ ab^{-1} \in H \iff  e \circ x^{-1} = x^{-1} \in H$$ So each element has its own inverse. If $x,y \in H$, then we need to show that $xy \in H$. Let $b^{-1} = y^{-1}$. Then by our assumption:
$$xy \in H$$
$$\therefore H \text{is a subgroup of G iff } ab^{-1} \in H, \forall a,b \in H$$
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