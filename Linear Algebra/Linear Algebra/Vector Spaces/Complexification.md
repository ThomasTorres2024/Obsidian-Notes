---
title: Complexification
tags:
  - LinearAlgebra
draft: "False"
---
# Complexification 
Let $V$ be a [[Vector Space]] over the [[Real Numbers]]. We can construct a vector space such that $V^+=V \oplus Vi$ where $Vi$ is analogous to changing its corresponding [[Field]] to the [[Complex Numbers]]. 

Let addition over $V^+$ for $\langle x,y \rangle \in V^+$ and $x,y \in V$. Define the sum of these elements by:
$$\langle x_{1},y_{1} \rangle + \langle x_{2},y_{2} \rangle = \langle x_{1}+x_{2},y_{1}+y_{2} \rangle$$
And for some $(\alpha+i \beta)$ let multiplication by this scalar be given by:
$$(a+ib)\langle x,y\rangle =\langle \alpha x- \beta y, \beta x+\alpha y \rangle$$
Think of the second argument as being analogous to a complex vector. If $y=0$ then the subspace $\langle x,0 \rangle \cong V$ and likewise for $x=0,\langle 0,y\rangle \cong Vi$. We do this via the following:
$$\langle x,y \rangle = \langle x,0 \rangle + i \langle y,0 \rangle $$
Given the identity that $i\langle y,0 \rangle = \langle 0,y \rangle.$ Thus $\forall z\in V^+, z=x+iy$ for $x,y \in V$. Furthermore it should be clear that $V \cap Vi = \langle 0, 0\rangle$ thus $V^+=V\oplus Vi$. 

If $\{x_{1},x_{2},\dots,x_{n}\}$ is a [[Linearly Independent]] set of vectors in $V$ it is also [[Linearly Independent]] in $V^+$. Let $\alpha_{1},\alpha_{2},\cdots,\alpha_{n},\beta_{1},\beta_{2},\dots,\beta_{n}$ such that:
$$\sum_{j}(\alpha_{j}+\beta_{j}i)x_{j}=0 \iff \sum_{j} \alpha_{j}x_{j} + \sum_{j} \beta_{j}ix_{j}=0 $$
Then the real and complex parts must be 0 respectively, so the real part is 0 since the $x$ vectors are a linearly independent set, same argument applies for the betas. Secondly, if $x's$ are a basis for $V$  $\text{dim}(V^+)=\text{dim}(V)$

We can extend a [[Linear Transformation]] $A$ on $V$ to a linear transformation $A^+$ on $V^+$, namely:
$$A^+(x+iy)=Ax+iAy$$
An adequate [[Inner Product]] on this vector space can be given by:
$$\langle x_{1}+iy_{i},x_{2}+iy_{2} \rangle= \langle x_{1},x_2 \rangle + \langle y_{1},y_{2} \rangle - i(\langle x_{1},y_{2}\rangle - \langle y_{1},x_{2} \rangle)  $$
And then for any $x,y \in V$ then:
$$\|x+iy\|^2=\|x\|^2+\|y\|^2$$
Furthermore, $A^+$ preserves all algebraic properties. For instance:
$$\begin{align}
B=\alpha A \implies B^+ = \alpha A^+ \\
C=A+B \implies C^+=A^++B^+ \\
C=AB \implies C^+=A^+B^+
\end{align}$$
If $V$ is an inner product space, and if $B=A'$ then $B^+=(A^+)'$. 

We can also attend to [[Eigen Value]]s and [[Eigen Vector]]s, on $A$. Let $A:V \to V$ be a linear map, let $x+iy$ be an eigen vector on $A^+$ with the eigen value $\alpha+i \beta$ for $x,y \in V$ and $\alpha,\beta \in \mathbb{R}$. Then:
$$Ax=\alpha x - \beta y$$
$$Ay=\beta x- \alpha y$$
We have that the subspace of $V$ spanned by $x,y$ is invariant under $A$. Furthermore, any real eigen value of $A$ is also an eigen value of $A^+$. This follows from $Ax=\alpha x,Ay=\alpha y$. 

The main point of [[Complexification]] is that, given some real basis in $V$, it is also a complex basis in $V^+$. It is not merely the case that real matrices are a subset of complex matrices, but rather that they behave identically. 