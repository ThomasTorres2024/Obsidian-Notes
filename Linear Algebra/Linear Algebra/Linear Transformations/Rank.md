---
title: Rank of a Matrix
tags:
draft: "False"
---
# Rank Definition
We can think of the rank of a matrix as the [[Dimension]] of the [[Column Space]] and the [[Row Space]], which are always equivalent, and we just refer to this quantity as the rank:
$$\text{dim}(\text{col}(A))=\text{dim}(\text{row}(A))=r$$
A matrix which has a full rank has the maximum possible rank. For a matrix, $A \in \mathbb{F}^{m \times n}$, the matrix has rank:
$$r=\text{min}(m,n)$$
$A$ also has $n$ [[linearly independent]] columns. A [[full rank]] matrix is one which is [[injective]], meaning that for $x,y \in \mathbb{F}^n$, we have that:
$$A\vec{x} = A\vec{y} \Longleftrightarrow \vec{x} = \vec{y}$$
If $A$ has rank $r < \text{min}(m,n)$ it follows that there is a non-trivial zero given by $\vec{c}$ such that $A\vec{c}=\vec{0}$, meaning that for any $z \in Col(A)$, that we can obtain $z$ infinitely many ways using the non-trivial zero in the nullspace.   

---
### Rank [[Nullity]] Theorem:
Let $A$ be represented by the matrix where $A \in \mathbb{R}^{m \times n}$ By [[Rank]] [[Nullity]] theorem, the following is true:
$$\begin{align}
\text{dim}(\mathcal{N}(A))+\text{rank}(A)=n \\
\text{dim}(\mathcal{N}(A^T))+\text{rank}(A^T)=m \\
\text{rank}(A)=\text{rank}(A^T)
\end{align}$$
$Proof).$
For the [[Linear Transformation]] $A$ onto an $n$ [[Dimension]]al vector space $n$ denoted by $\mathcal{X}$, then immediately we can conclude that:
$$(1)\quad \text{dim}((A')^0)=\text{dim}(\mathcal{N}(A')) \implies \text{dim}(\mathcal{N}(A')) =n- \text{rank}(A) $$
For the [[Vector Space]] $\mathcal{X}=\{ \vec{x_{1}}, \vec{x_{2}},\ldots,\vec{x_{n}} \}$ be a basis such that the first $\nu$ vectors are a basis for $\mathcal{N}(A)$, then, for any $x=\sum_{i} \xi_{i}Ax_{i}$ we have that:
$$Ax=\sum_{i=1}^N \xi_{i}Ax_{i} = \sum_{i=\nu}^n \xi_{i}Ax_{i}$$
Therefore, we have that:
$$(2)  \quad \text{rank}(A) \leq n -  \text{dim}(\mathcal{N}(A))$$
This can be applied to $A'$ and thus:$$\text{rank}(A') \leq n -  \text{dim}(\mathcal{N}(A'))=\text{rank}(A)$$
By $(1),(2)$ we have that, replacing $A$ with $A'$
$$\begin{align}
\text{rank}(A) \leq n- \text{dim}(\mathcal{N}(A)) \\
\implies (3) \quad \text{rank}(A) \leq \text{rank}(A')
\end{align}$$
Thus we have:
$$(4) \quad \text{rank}(A)=\text{rank}(A')$$
By using $(1),(4)$ we obtain:
$$(5) \quad \text{dim}(\mathcal{N}(A'))=n - \text{dim}(\text{rank}(A'))$$
And then by substituting $A\to A'$ in $(5)$ we get:
$$(6) \quad  \text{dim}(\mathcal{N}(A))=n - \text{dim}(\text{rank}(A))$$
This concludes the proof. 

### Theorem).
If $A$ is a [[Linear Transformation]] on the $n$ dimensional vector space $V$, and if $H$ is any $h$ dimensional subspace of $V$, then $\text{dim}(AH) \geq h- \mathcal{N}(A)$

$Proof).$ 
Let $K$ be any subspace such that $V=H \oplus K$, if $\text{ dim}(K)=k \implies k=n-h$. When operating with $A$ we have that:
$$AV=AH+AK$$
We have that $AV=\text{dim}(\mathcal{R}(A))=n-\text{dim}(\mathcal{N}(A))$. Then notice that:
$$AV-AH=AK \implies \text{dim}(AK) \leq k =n-h = n - \text{dim}(\mathcal{N}(A))$$

# Rank Properties 
If $A,B$ are linear transformations on finite [[Dimension]]al vector spaces, then:
1. $\text{rk}(A+B)\leq\text{rk}(A)+\text{rk}(B)$
2. $\text{rk}(AB) \leq \text{min}(\{ \text{rk}(A),\text{rk}(B) \})$
$Proof).$ 
$$\begin{align}
(AB)x=A(Bx) \implies \mathcal{R}(AB) \subseteq \mathcal{R}(A) \\
\implies \text{rank}(AB) \leq \text{rank}(A)
\end{align}$$
This proves $(2)$. We can prove $(1)$ with the following, let both $A,B$ be defined on $V$, then:
$$\begin{align}
(A+B)(V)=AV+BV \implies \text{rank}(A+B) \leq \text{rank}(A) + \text{rank}(B)
\end{align} $$
 

For $A \in \mathbb{F}^{m \times n}$ where $\text{rk}(A)=n$ and $m \geq n$ and $B \in \mathbb{F}^{n \times d}$ then:
3. $\text{rk}(AB)=\text{rk}(B)$
4. $\text{rk}(AB)=\text{rk}(BA)=\text{rk}(A)$
$Proof).$ We can apply the result to $B'A'$, if $B$ is invertible then:
$$\begin{align}
\text{rank}(A)=\text{rank}(AB \cdot B^{-1})\leq \text{rank}(AB) \\
\text{rank}(A)=\text{rank}(B^{-1} \cdot BA)\leq \text{rank}(BA) 
\end{align} 

$$
In tandem with $(2)$ this gives $(4)$.
