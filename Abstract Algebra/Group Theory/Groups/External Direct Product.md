---
title: External Direct Product
tags:
  - AbstractAlgebra
draft: "False"
---
# External Direct Product

We can generate a new [[Group]] by an operation called the [[External Direct Product]], by taking a set of groups, $G_i$ where we have $n$ many groups and $1 \leq i \leq n$. We define the external product, by using $\oplus$ as the following:

$$\bigoplus_{i=1}^nG_{i} = \{ (g_{1},g_{2}, \dots, g_{n}) : g_{i} \in G_{i}, 1 \leq i \leq n  \} $$

We can look at this as a [[Group]] by taking elements from each $i$th group. The [[Binary Operation]] here is doing the binary operation of each respective group with itself, for example:

$$(g_{1},g_{2},\dots, g_{n}) (g_{1}',g_{2}',\dots , g_{n}')=(g_{1}+_{G_{1}} g_{1}',g_{2} +_{G_{2}} g_{2}',\dots , g_{n} +_{G_{n}}  g_{n}')$$

If each $G_i$ is finite, then the [[Order]] of the external direct product of the groups is:

$$\left|\bigoplus_{i=1}^n G_{i} \right|= \prod_{i=1}^n |G_{i}|$$

Which is infinite in the case of some $|G_i|=\infty$. 

The idea here is quite similar to that of [[Isomorphic Vector Spaces]]. For instance, we can say that $\mathbb{R}^2 = \mathbb{R} \oplus \mathbb{R}$, which is to say that $\mathbb{R}^2 \cong \mathbb{R} \oplus \mathbb{R}$ (actual equality is the result of the Internal Direct Product).

---
### Example 1.)
$U(8) \oplus U(10)$ then:

$$\begin{align} U(8) \oplus U(10) =   \\ \\


\{ (1,1), (1,3), (1,7),(1,9), \\ 
(3,1),(3,3),(3,7),(3,9), \\
(5,1),(5,3),(5,7),(5,9), \\
(7,1),(7,3),(7,7),(7,9)  \}
\end{align} $$

---
### Example 2.)
$\mathbb{Z}_{2} \oplus \mathbb{Z}_{3}$ then:

$$\begin{align} \mathbb{Z}_{2} \oplus \mathbb{Z}_{3} =   \\ \\


\{  (0,0),(0,1),(0,2) \\
(1,0),(1,1),(1,2) \}
\end{align} $$
This is an Abelian group, notice that:
$$\mathbb{Z}_{2} \oplus \mathbb{Z}_{3  }=\langle (1,1) \rangle$$
And therefore:
$$\mathbb{Z}_{2} \oplus \mathbb{Z}_{3  } \cong \mathbb{Z}_{6}$$
---
# Example.) Classification of Groups of Order $4$ 
We can show that any group of order $4$ is either Isomorphic to $\mathbb{Z}_{4}$ or $\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$. These groups are not Isomorphic to one another $\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$ is not cyclic and $\mathbb{Z}_{4}$ is cyclic. 

The strategy for proving this result is to show that the [[Cayley Table]] of $G$ has either one of two valid forms. being the two aforementioned groups. 

By Lagrange's theorem, all elements of $G$ have order $1$ or order $2$. 


