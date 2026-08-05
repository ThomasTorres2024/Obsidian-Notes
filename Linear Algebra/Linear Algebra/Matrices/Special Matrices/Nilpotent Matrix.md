---
title: Nilpotent Matrix
tags:
  - LinearAlgebra
draft: "False"
---
# Nilpotent Matrix 
A [[Linear Transformation]]/[[Matrix]] is Nilpotent if $\exists n \in \mathbb{N}$ such that for some $A$ onto $\mathcal{R}$ such that $A^n=0$. 

One result from this family of matrices is that for some $x\in \mathcal{R}$ such that $Ax\neq0 \implies \{ x,Ax,A^2x, \cdots,A^{n-1}x \}$ is a [[Linearly Independent]] set and that if $\mathcal{H}$ is the space spanned by these vectors then there exists a [[Vector Subspace]] $\mathcal{K}$ such that $\mathcal{R} = \mathcal{K} \oplus \mathcal{H}$ and that $(\mathcal{H},\mathcal{K})$ reduce $A$. 

#### Theorem).
$Proof).$ 
Let us begin with proving linear independence, we want to show that each of the following $\alpha_{i} = 0$ given the following $\sum_{i=1}^{n-1} \alpha_{i} A^ix = 0$. Denote $j$ as the first index such that $\alpha_{j} \neq0$ and permitting that $j=0$. Then we obtain the following: 
$$A^j x=\begin{align}
\sum_{i=j+1}^{n-1} \alpha_{i} A^ix = A^{j+1}\left( \sum_{i=j+1}^{n-1} \alpha_{i} A^{i-j-1}x \right)=A^{j+1}y
\end{align}$$
Then from the definition of $n$, 
$$A^{n-1}x=A^{n-j-1}A^j x = A^{n-j-1}A^{j+1}x=A^ny=0$$
It must therefore be the case that each $\alpha_{i}$ is 0 since this contradicts the choice of $x$, therefore the set is linearly independent. I'm not going to write down the remainder of this proof. 

---
#### Theorem). 
Here we have that 

$Proof.$ 