---
title: Normal Subgroup
tags:
  - AbstractAlgebra
draft: "False"
---
# Normal Subgroup Definition
A [[Subgroup]] $H$ of a group $G$ is called a normal subgroup of $G$ if, for the cosets of $H$ over $G$ we have that $aH=Ha \quad \forall a \in G$. We denote that a set is a normal subgroup via the following:
$$H \triangleleft G$$
We can think of this as a weak form of commutativity through another equivalent definition:
$$ah=h'a : \quad  a\in G \quad h,h' \in H$$
It is not generally the case that $h'=h$. 

---
# Normal Subgroup Test 
A subgroup $H\leq G$ is normal in $G \iff xHx^{-1} \subseteq H \quad \forall x \in G$. 

$Proof.)$
If $H \triangleleft G$ then $\forall x \in G, h\in H$ then $\exists h' \in H$ such that $xh=h'x$. This condition then gives that $xhx^{-1}=h' \in H$ and thus that the [[Coset]] $xHx^{-1} \subseteq H$. 

Conversely if $xHx^{-1} \subseteq H \quad \forall x \in G$ and $a\in G$ then if $x=a$ we get that:
$$aHa^{-1} \subseteq H \implies aH\subseteq Ha \text{ (obtained from right mult of a)}$$
On the other hand if let $x=a^{-1}$ then we obtain:
$$a^{-1}Ha \subseteq H \implies Ha \subseteq aH$$
And thus we obtain by both directions for this case that $ah=Ha$ and thus by the definition of a [[Normal Subgroup]] we obtain that $H \triangleleft G$. 

---
### Example 1.) 
For an [[Abelian Group]] $G$, and some [[Subgroup]] $H$ of $G$ we know that $H$ must be an [[Abelian Group]] and therefore must be normal since any $ah=ha$ for $a \in G, h \in H$. 

### Example 2.) If $G$ is a group and we consider the [[Group Center]] $Z(G)=\{  a\in G : ab=ba \quad \forall b \in G\}$
Since $Z(G)$ commutes with every element in $G$ it is trivially a [[Normal Subgroup]] of $G$. 

### Example 3.) If $n \geq_{1} \implies A_{n} \triangleleft S_{n}$. 
We can apply the normal subgroup test. If we consider some $\sigma \in A_{n}$ and $\tau\in S_{n}$ then $\tau \sigma \tau^{-1}$ must be even and thus $\tau \sigma \tau^{-1} \in A_{n} \implies \tau A_{n} \tau^{-1} \subseteq A_{n} \quad \forall \tau \in S_{n}$. 

### Example 4.) Every subgroup of $D_{n}$ (the dihedral group) consisting only of rotations is a normal subgroup of $D_{n}$ 
Here we can let $R_{n}$ be the subgroup of $D_n$ consisting only of rotations. Let $r_{\theta} \in R_{n}$ and let $x \in D_{n}$. If $x \in R_{n}$ the result is trivial. If $x \notin R_{n}$ then $x$ must be a reflection denoted by $f$. Recall that for dihedral groups the following property holds:
$$fr_{\theta}=r_{-\theta}f$$
Which entails that:
$$fr_{\theta}f^{-1}=r_{-\theta} \in R_{n}$$
Thus $R_{n} \triangleleft D_{n}$. 

### Example 5.) Suppose that $H \triangleleft G$ and $K \leq G$
Then the group $HK=\{hk : h \in H,k \in K \}$ is a subgroup of $G$. 

Clearly the identity element is in $HK \implies HK \neq \emptyset$. Furthermore note that $H \subseteq HK$ since $e \in K$. Consider $a=h_{1}k_{1}$ and $b=h_{2}k_{2}$ which are both members of $HK$. Now consider the following:

$$ab^{-1}=h_{1}k_{1}(h_{2}k_{2})^{-1}=h_{1}k_{1}k_{2}^{-1}h_{2}^{-1}=h_{1}(k_{1}k_{2}^{-1})h_{2}^{-1}=h_{1}h'(k_{1}k_{2}^{-1}) \in HK$$
The last equality comes from the fact that $H \triangleleft G$. Also we have that $h_{1}h' \in H$ and $(k_{1}k_{2})^{-1}\in K$ and thus by the $1$ step subgroup test it follows that $HK \leq G$.

### Example 6.) In $D_{8}$ let $H=\left\{ R_{0},R_{\frac{\pi}{2}},R_{\pi},R_{\frac{3\pi}{2}}  \right\}$ and $K=\{R_{0},F \}$
By example $4$ we know that $H \triangleleft D_{8}$ and by example $5$ we have that $HK \leq D_{8}$. 

The following group is non-Abelian and isomorphic to $D_{4}$:
$$HK=\left\{  R_{0},R_{\frac{\pi}{2}},R_{\frac{3\pi}{2}},R_{\pi},F,R_{\frac{\pi}{2}}F,R_{\pi}F,R_{\frac{3\pi}{2}}F  \right\}$$

### Example 7.) If $G$ has a unique subgroup $H$ of some specific order, then $H \triangleleft G$. 

If $G$ has a unique subgroup $H$ of some specific order, then $H \triangleleft G$. Consider the inner automorphism for the fixed element $g$ and $x \in H$ then $\phi_{g} : \phi_{g}(x) = gxg^{-1}$ is a mapping from $H\to gHg^{-1}$ where $|gHg^{-1}|=|H|$. 

Clearly $gHg^{-1} \leq G \implies gHg^{-1}=H$ and trivially by the normal subgroup test we have that $H \triangleleft G$. 

### Example 7.5) If $G$ is a group with either infinite or finite and even order and $H \leq G$ with $[G:H]=2$ then $H \triangleleft G$. 

Recall that $[G:H]$ is the number of left/right cosets of $H$ in $G$. So, $H$ has $2$ distinct left cosets in $G$. One of these cosets must be the identity coset $eH=H$. 

Now consider some $g \in G$ where $g$ is arbitrary. Then, $gH$ is either $H$ or the other coset of $H$ in $G$. 

If $gH=H \implies g\cdot e=g \in H$ so that $Hg=H$ and thus $gH=H=Hg$ would make it a normal group.

On the other hand if $gH \neq H$ then $ge \not\in H$ and thus $g \not\in H$ and thus $Hg \neq H$. 

Since $G$ has $2$ left cosets one of which is $H$ and $2$ right cosets one of which is also $H$, this forces that $gH=Hg$, and thus we obtain that $H \triangleleft G$. 

### Example $8$ $SL(2,\mathbb{R}) \triangleleft GL(2,\mathbb{R})$
Consider some $x \in SL(2,\mathbb{R})$ and $y \in GL(2,\mathbb{R})$ then:

$$\det(xyx^{-1})=\det(x)\cdot \frac{1}{ \det (x)} \cdot \det(y)=1 \implies xyx^{-1} \in SL(2,\mathbb{R})$$

Thus normality is obtained via the normal subgroup test. 

### Example 9.) $H=\{(1),(12)(34),(13)(24),(14)(23) \}$
$H \triangleleft A_{4}$ by example $7$ since it is the only subgroup of $A_4$ of order $4$ since the other elements of $A_4$ all have order $3$. 

On the other hand, 
$$K=\{ (1),(123),(132) \}$$
is not a normal subgroup of $A_4$ since for the element $((12)(34)) \in A_{4}$ we can see that: 
$$(12)(34)(123)((12)(34))^{-1} = (12)(34)(123)(34)(12)=(142) \notin K$$
