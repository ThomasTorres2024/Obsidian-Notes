---
title: Kernel
tags:
  - AbstractAlgebra
draft: "False"
---
# Definition: Kernel
The Kernel of a [[Homomorphism]] for $\phi: G \to \bar{G}$ is the set of all elements in $G$ such that the map results in the identity element of $\bar{G}$:
$$\text{ker }\phi = \{ x \in G : \phi(x)=e_{\bar{G}} \}$$
Kernels are also [[Normal Subgroup]]s of a Group Homomorphism. 

---
#  Theorem). Kernels are Ideals. 
Let $\phi$ be a ring homomorphism from  [[Ring]]s $R\to S$. Then:
$\text{ker}(\phi)=\{r \in R: \phi(r)=0 \}$ is an ideal of $R$. This result is trivial. Let $r \in R$ be arbitrary and $k \in \text{ker}(\phi)$ then consider the following:
$$\phi (kr)=\phi(0)\cdot \phi(r) = 0 = \phi(r)\cdot \phi(0) = \phi(rk)$$
# Theorem.) Ideals are Kernels
Every ideal of $R$ is the kernel of a [[Ring Homomorphism]] of $R$. Specifically, an ideal $A$ is the kernel of the mapping given by $r\mapsto r+A$ from $R \to \frac{R}{A}$. The above homomorphism is sometimes called the __natural homomorphism__. 

