---
title: Normalizer
tags:
  - AbstractAlgebra
draft: "False"
---
# Normalizer 
The set of elements in a [[Group]] $G$ which "vote" in favor of the normality of a [[Subgroup]] $H\leq G$, denoted by:
$$N_{G}(H)=\{ g \in G : gH=Hg \} = \{ gHg^{-1} = H \}$$
Is called the __Normalizer of $H$ in $G$__. We want to observe the structure of what a [[Normalizer]] is, we want to determine if it is a [[Subgroup]] or not. 

### Observation). 
If $g \in N_{G}(H) \implies gH \subseteq N_{G}(H)$

$Proof.)$
If $gH=Hg \implies gH=bH : \forall b \in gH$
Thus we have that $bH=gH=Hg=Hb$, which entails that a coset fully votes for $H$ when its left and right [[Coset]]s are equivalent. 

As a quick corollary, $|N_{g}(H)|$ is a multiple of $|H|$. 

$Proof.$ 
$N_g(H)$ is made up of whole left [[Coset]]s of $H$, and all left cosets are disjoint and are the same size. Thus, the size of the [[Normalizer]] must be a multiple of the size of $H$. 

We obtain that $N_{G}(H)=G \iff H \triangleleft G$ and that $N_{G}(H) = H$ if $H$ is as unnormal as possible which means that $H$ is the only coset where its left and right cosets are equivalent. 

# Theorem). [[Normalizer]]s are [[Subgroup]]s of $G$. 
For any $H < G \implies N_{G}(H) < G$. 

$Proof.)$ 
Recall that $N_{G}(H)=\{g \in G : gHg^{-1} = H \}$ is the set of elements that normalize $H$. We need to show that the group has an identity elements, inverses, and is closed under binary operations. Naturally, we have the identity given by $eHe^{-1}$:
$$eHe^{-1}=\{ ehe^{-1} : h \in H \}= H$$
Secondly to verify inverse elements we have that $g \in N_{G}(H)$ which means that $gHg^{-1}=H$. 

We want to show that $g^{-1} \in N_{G}(H)$ that is that: 
$$g^{-1}H(g^{-1})^{-1}=g^{-1}Hg=H$$
Which we can in the following:
$$g^{-1}Hg=g^{-1}(gHg^{-1})g=eHe=H$$
For closure consider the following. Let $g_{1},g_{2} \in N_{G}(H)$ which means that $g_{1}Hg_{1}^{-1}=H$ and that $g_{2}Hg_{2}^{-1}=H$. We want to show that $g_{1}g_{2} \in N_{G}(H)$:
$$(g_{1}g_{2})H(g_{1}g_{2})^{-1}=g_{1}(g_{2}Hg_{2}^{-1})g_{1}^{-1}=g_{1}Hg_{1}^{-1}=H$$
Thus $(g_{1}g_{2}) \in H$. 

$$\therefore N_{G}(H) \leq G$$
### Corollary 
Every subgroup is normal in its normalizer, which is to say that $H \triangleleft N_{G}(H)$ thus we have that:

This is a trivial statement since by definition $gH=Hg \quad \forall g \in N_{G}(H)$. 

---
# Examples).
We see that $H=\langle x, z \rangle \triangleleft A_{4}$, therefore $N_{A_{4}}(H)=A_{4}$. 

---
