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

