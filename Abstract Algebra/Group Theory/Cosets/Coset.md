---
title: Coset
tags:
  - AbstractAlgebra
draft: "False"
---
# Coset 
We can define a [[Coset]] by considering a group, $G$ and a [[Subgroup]] $H \leq G$, and some $a,b \in G$ (it is possible that $a,b \not \in H$). Then we can define the following types of Cosets:
$$\begin{align}
\large \text{left coset: } aH=\{ah : h \in H   \}\\ \\
\large \text{right coset: } Ha=\{ha : h \in H   \} \\ \\
\large = aHa^{-1} \{ aha^{-1} : h \in H \}
\end{align} $$
We can think of [[Coset]]s as [[Equivalence Class]]es 

### Remark.) 
Cosets generally are not subgroups. It can be the case that $aH=bH$ even if $a \neq b$ (ex 1).  

---
# Lemma.) Properties of Cosets
Let $G$ be a [[Group]], $H \leq G$ and let $a,b \in G$ then the following are true:
1. $a \in aH$
2. $aH=H \iff a \in H$
3. $(ab)H=a(bH)$ and $H(ab)=(Ha)b$
4. $aH=bH \iff a \in bH$
5. $aH=bH$ or $aH \cap bH = \varnothing$
6. $aH=bH \iff a^{-1}b \in H$
7. $|aH|=|bH|$
8. $aH=Ha \iff H=aHa^{-1}$
9. $aH$ is a [[Subgroup]] of $G \iff a\in H$. 

### Proof.) 

#### 1.) Proof $a \in aH$
Since $H$ is a group, $e \in H$, and so $ae =a \in aH$. 

#### 2.) Proof $aH=H \iff a\in H$
 We want to show that $aH=H \iff a\in H$. If $aH =H$ then, we know that $a \in aH$ by $1$, so we also know that $a \in H$ since $aH=H$. 
 
 Conversely, let $a \in H$. Clearly, $aH \subseteq H$. Let $h \in H$. We know that $a^{-1}h \in H$ via closure. But also, $a^{-1}h \in aH \implies a(a^{-1}h) =h \in aH$, and thus $aH=H$  

#### 3.) Proof $(ab)H=a(bH)$
Follows directly from the associative property of elements of groups (we know all of these elements are associative since they come from $G$ which is  group as well):
$$(ab)h=a(bh) \text{ and } h(ab)= (ha)b$$

#### 4.) Proof $aH=bH \iff a,b \in H$
If $a \in H$ then $aH=H=bH$ trivially. If $aH=bH$ then 


---
# Examples:
### Example 1.) $G=S_{3}$, $H=\{(1),(1,3) \}$.
$$\large S_{3}=\{ \epsilon,(12),(13),(23),(123),(321) \}$$
The cosets of $G$ are:
$$1H=H, (13)H=H$$
$$(12)H= \{(12),(12)(13) \}=\{(12),(132) =(132)H\}$$
$$(23)H= \{(23),(23)(13) \}=\{(23),(123) =(123)H\}$$
### Example 2.) $\large H = \{0,3,6 \}$ in $\mathbb{Z}_{9}$ under $+ \mod(9)$:
All of the cosets of $H$ here are:
$$0+H=\{0,3,6 \}=3+H=6+H$$
$$1+H=\{1,4,7 \}=4+H=7+H$$
$$2+H=\{2,5,8 \}=5+H=8+H$$

