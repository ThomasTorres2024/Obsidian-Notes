---
title: Transpose
tags:
draft: "False"
---
# Transpose
A Matrix [[Transpose]] is an operation which essentially flips the contents of a matrix over its diagonal. We can more formally describe this with the following. Let $A \in \mathbb{R}^{m \times n}$, then for $A^T \in \mathbb{R}^{m \times n}$. 

Each entry of $A$ is given by, $A^T_{ij}=A_{ji}$.  For concrete examples consider the following:
![[Pasted image 20260111084207.png]]

If a matrix satisfies $A^T=A$ then we say that $A$ is a [[Symmetric Matrix]].  

---
# [[Dual Spaces]] and the Matrix [[Transpose]]
We can actually obtain the [[Transpose]] of a Matrix by modifying a [[Linear Transformation]]. 

Recall that the [[Dual Spaces]] can be defined as a [[Linear Transformation]] which goes from some [[Vector Space]], $\mathcal{V}$ to a [[Field]] $\mathbb{F}$:
$$V^*=\mathcal{L}(\mathcal{V},\mathbb{F})$$
Let $T$ be the [[Linear Transformation]] between the vector spaces $\mathcal{V} \to \mathcal{W}$. The transpose of $T$ should be  an operation that maps not just in the opposite order from $\mathcal{W} \to \mathcal{V}$, but also by taking the dual of these vector spaces. Therefore, we can think of $T^T$ as the following map:
$$T^T:\mathcal{W}^* \to \mathcal{V}^*$$
If we consider some $g \in \mathcal{W}^*$. $g$ is a linear functional. If we consider $T^T(g)$ then, we obtain a new functional in $\mathcal{V}^*$. We can now formally define the [[Transpose]] of a Matrix given some $x \in \mathcal{V}$ 
$$T^T(g)(x)=g(T(x))$$
We have two ways of obtaining $g(T(x))$. We can either achieve this result in 1 composition or in 2:
![[Pasted image 20260111090947.png]]
We can either compose $T(x)$ with $g$ or, we can just do $T^T(g)(x)$ and obtain the same result. Our end goal here is to be able to construct some matrix $A$ associated with $T$, and then to show that the matrix of $T^T$ actually is $A^T$.  

For $T : \mathcal{V} \to \mathcal{W}$, let us express a [[basis]] for $\mathcal{V}$ and $\mathcal{W}$:
$$\beta=\{ v_1,v_2,\dots v_n \}$$
$$\gamma =\{ w_1,w_2,\dots w_m \}$$
Then we can express $T$ as the matrix:
$$A=[T]_{\beta}^\gamma$$
To constructor a matrix for $T^T$, we need a basis for $\mathcal{W}^*$ and $\mathcal{V^*}$:
$$\beta^* = \{f_1,f_2,\dots f_n \} \text{ is a basis of } \mathcal{V}^*$$
$$\gamma^* = \{g_1,g_2,\dots g_m \} \text{ is a basis of } \mathcal{W}^*$$
Then we can express $T^T$ as a matrix by:
$$[T^T]_{\gamma^*}^{\beta^*}=A^T$$
This result can be verified by computing each basis vector of $T^T$:
$$[T^T]_{\gamma^*}^{\beta^*}=[T^T(g_1),T^T(g_2), \dots T^T(g_m)]$$
$$T^T(g_j)=\sum_{i=1}^n T^T(g_j)$$
(I left this off here, I really do not understand what is going on)