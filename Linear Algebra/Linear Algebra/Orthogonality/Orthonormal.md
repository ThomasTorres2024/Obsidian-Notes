---
title: Orthonormal
tags:
  - LinearAlgebra
draft: "False"
---
# Orthonormal 
We say that two vectors are [[Orthonormal]] if for $v_{i},v_{j} \in \mathcal{V}$ where $\mathcal{V}$ is a [[Vector Space]], the inner product between $v_{i},v_{j} = \delta_{ij}$ ([[Kronecker Delta]]). In English this means that every vector is mutually [[orthogonal]] and the [[Norm]] of each vector is 1. 

# Completeness
A finite orthonormal set is in an [[Inner Product]] Space is said to be "complete" if it is a maximal set, meaning that no more orthonormal vectors can be generated. 

### Bessel's inequality for a finite [[Vector Space]]
If $X=\{ x_{1},x_{2},\dots,x_{n} \}$ is a finite [[Orthonormal]] set in an [[Inner Product]] Space, and if $x$ is any vector and if $\alpha_{i}=\langle x,x_{i} \rangle$ then we have that:
$$\sum_{i} |\alpha_{i}|^2 \leq \|x\|^2$$
The vector $x'=x-\sum_{i} \alpha_{i}x_{i}$ is orthogonal to each $x_{j}$ and consequently is orthogonal to each vector in $X$. 

$Proof).$ 
For the first assertion:
$$\begin{align}
0 \leq \|x'\|^2 = \langle x', x' \rangle = \left\langle  x- \sum_{i=1}^n \alpha_{i}x_{i}, x-\sum_{j=1}^n \alpha_{j}x_{j}  \right\rangle  \\
= \langle x, x \rangle - \sum_{i=1}^n \alpha_{i} \langle x_{i},x \rangle - \sum_{j=1}^n \overline{\alpha_{j}} \langle x,x_{j} \rangle + \sum_{i=1}^n \sum_{j=1}^n \alpha_{i} \overline{\alpha_{j}}  \langle x_{i},x_{j} \rangle \\
= \|x\|^2 - \sum_{i}^n |\alpha_{i}|^2 -  \sum_{i}^n |\alpha_{i}|^2 + \sum_{i}^n |\alpha_{i}|^2 \\
= \|x\|^2 - \sum_{i} |\alpha_{i}|^2
\end{align}$$
For the second assertion:
$$\langle x', x_{j} \rangle = \langle x,x_{j} \rangle - \sum_{i} \alpha_{i} \langle x_{i}, x_{j} \rangle = \alpha_{j} - \alpha_{j} = 0$$
### Theorem 2). 
TFAE:
If $X$ is any finite orthonormal set in an inner product space $V$ the following six conditions on $X$ are equivalent:

1. The orthonormal set $X$ is complete
2. If $\langle x,x_{i} \rangle = 0$ for $i=1, \dots ,n$ then $x=0$. 
3. The subspace spanned by $X$ is the whole space $V$ 
4. If $x \in V \implies x = \sum_{i} \langle x, x_{i} \rangle x_{i}$
5. If $x,y \in V$ then ([[Parseval's Theorem]]): $$\langle x,y \rangle = \sum_{i} \langle x, x_{i} \rangle \langle x_{i},y \rangle$$
6. If $x \in V \implies$ $$\|x\|^2 = \sum_{i} |\langle x, x_{i} \rangle|^2$$
$Proof).$ 

$(1) \implies (2)$
If $\langle x,x_{i} \rangle = 0$ for all of $i$ and $x\neq0$, then we could adjoin $x$ to $X$ and get a larger set, however this would contradict the idea of completeness and we obtain a larger orthonormal set. 

$(2) \implies (3)$
If there is an $x$ that is not a linear combination of the $x_i$'s, then by the second part of theorem 1, $x'=x-\sum_{i} \langle x,x_{i} \rangle x_{i} \neq0$ and it is orthogonal to each $x_i$, which contradicts $2$ so it must be the case that every vector can be expressed as such a linear combination. 

$(3) \implies (4)$
If every $x$ has the form $x=\sum_{j} \alpha_{j} x_{j}$ then: $$\langle x,x_{i} \rangle = \sum_{j=1}^n \alpha_{j} \langle x_{j},x_{i} \rangle = \alpha_{i}$$
$(4) \implies (5)$
Let $a,b \in V$ then $a=\sum_{i=1}^n \alpha_{i}x_{i}$ and $b=\sum_{i=1}^n \beta x_{i}$ so that:
$$ \langle a,b \rangle = \left\langle  \sum_{i=1}^n \alpha_{i}x_{i},  \sum_{i=1}^n \beta x_{i}\right\rangle = \sum_{i} \alpha_{i} \sum_{j} \overline{\beta_{j}} \langle x_{i},x_{j} \rangle = \sum_{i=1}^n \alpha_{i} \overline{\beta_{i}} = \sum_{i=1}^n\ \langle a,x_{i} \rangle  \cdot \langle b,x_{i}\rangle    $$

$(5) \implies (6)$
Set $x=y$, we obtain then that:
$$\langle a, a \rangle = \|a\|^2 = \sum_{i=1} ^n |\langle a,x_{i} \rangle|^2$$
$(6) \implies (1)$
Assume that $X \subset Y$ where $Y$ is another orthonormal set. Then let $x_{0}$ be orthogonal to each $x_i$, then: 
$$\|x_{0}\|^2 = \sum_{i} |\langle x_{0}, x_{i} \rangle|^2 = 0 \implies x_{0}=0$$
Thus the circuit is complete, and the proof holds $\therefore$ 

--- 
# Complete [[Orthonormal]] Sets 
### Theorem). 
If $V$ is an $n$ dimensional [[Inner Product]] space, then there exists complete orthonormal sets in $V$ such that every complete orthonormal set in $V$ contains exactly $n$ elements. The orthogonal dimension of $V$ is the same as its linear dimension. 

$Proof).$
Orthonormal sets exist, if they do not contain $n$ many elements yet they can be enlarged such that they will contain $n$ vectors in $n$ or less steps. This set will span the whole space, and since it is linearly independent it must be a basis for $V$. The dimension of this resulting set is equivalent to $V$, therefore the statement is true. 

We also can prove this constructively using the [[The Gram-Schmidt Process]] instead of by performing this inductively. 
