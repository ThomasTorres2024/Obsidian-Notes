---
title: Adjoint
tags:
  - LinearAlgebra
draft: "False"
---
# Adjoint Definition
The [[Adjoint]] of a [[Linear Transformation]] $A$, is $A'$, a linear transformation satisfying the following. For $x\in V$ and for some $y \in V'$ the [[Dual Space]] of $V$, $A'$ is the [[Linear Transformation]] on $A':V' \to V'$ such that:
$$[Ax,y]=[x,A'y]$$
It can be shown that this is a linear transformation. Consider $x,z \in V$ then where $\delta,\epsilon \in \mathbb{F}$ (the corresponding field for $V$):
$$\begin{align}
[A(\delta x+ \epsilon z),y]=[(x+z),A'y]= \delta[x,A'y]+\epsilon[z,A'y] \\
&& \blacksquare 
\end{align}$$
From this we obtain the following results about the Adjoint:
1. $0'=0$
2. $1'=1$
3. $(A+B)^{\prime}=A'+B'$
4. $(\alpha A)'=aA'$
5. $(AB)'=B'A'$ (Order Reversing)
6. $(A^{-1})'=(A')^{-1}$

Another important relation about the adjoint of any adjoint, namely that:
$$A'' \cong A \iff A''=A $$
We write equality of the adjoint of the adjoint as the original when in reality it is just an [[Abstract Algebra/Morphisms/Isomorphism|Isomorphism]] between the two objects. If we identify $V$ and $V''$ through the natural isomorphism, then we obtain the isomorphism between the two vector spaces. 

On another note, the correspondence between the linear transformation $A \to A'$ forms an 'anti-isomorphism', namely due to property $6$, operation reversing.

---
# Adjoints of Projections
### Theorem). 
If $E$ is the [[Projection]] on $M$ along $N$ then $E'$ is the projection on $N$ along $M$. 

$Proof$. 
To start it is known that $(E')^2=(E^2)'=E'$ and also that $V=M \oplus N \implies V'=M^0 \oplus N^0$, which leaves it to be shown that $\{y : E'y=0 \}=M^0, \{y:E'y=y \}=N^0$. 

1. If $y\in M^0, \forall x:$
$$\begin{align}
[x,E'y]=[Ex,y]=0 \quad (\text{ by def of anihillator}) \\
\implies M^0 \subseteq \{ y: E'y=0 \}
\end{align}$$
2. If $E'y=0, \forall x \in M$
$$\begin{align}
[x,y]=[Ex,y]=[x,E'y]=0 \\
\implies y\in M^0 \text{ (def anihillator again) } \\
M^0 \supseteq \{ y: E'y=0 \}
\end{align}$$
3. If $y \in N^0 \implies \forall x$
$$\begin{align}
[x,y]=[Ex,y]+[(1-E)x,y]=[Ex,y]=[x,E'y] \\
\implies E'y=y \implies N^0 \subseteq \{ y: E'y=y \}
\end{align}
$$
4. If $E'y=y, \forall x \in N$:
$$\begin{align}
[x,y]=[x,E'y]=[Ex,y]=0 \\
\implies y \in N^0 \implies N^0 \supseteq \{y: E'y=y \}
\end{align}$$
By $1-4$ the result follows $\blacksquare$. 

### Theorem).
If $M$ is an [[Invariant Subspace]] under $A \implies M^0$ is an invariant subspace under $A'$. If $A$ is reduced by $(M,N)$ then $A'$ is reduced by $(M^0,N^0)$. 

$Proof).$ 
The first part can be shown in the following. Given any three linear transformations $A,F,E$ then the following is always true given that $F=(1-E)$
$$FAF-FA=EAE-AE=0$$
Since $M$ is invariant then $EAE=AE \iff EAE-AE=0$
If we let $E$ be any projection on $M$, then we have that $F$ is also a projection. By taking adjoints then:
$$(FAF-FA)'=F'A'F-A'F' \iff F'A'F' = A'F'$$
Since $F'$ is a transformation, then the result holds that $A'$ is also invariant. 

Given that the first part is true the second part can be shown now. Since $A$ is reduced by $(M,N) \implies V=M \oplus N$. We know that $V'=M^0 \oplus N^0$ as a common result involving direct sums. Since $A$ is given to be invariant on the vector spaces $M$ and $N$,it can be show that both $M^0,N^0$ are invariant subspaces under $A'$ using the fact that $A$ is invariant:
$$\begin{align}
\forall x\in M, \forall y \in M^0 : 0=[Ax,y]=[x,A'y] \implies A'y \in M^0 \\
\forall x\in B, \forall y \in N^0 : 0=[Ax,y]=[x,A'y] \implies A'y \in N^0 \\
\end{align}$$

 But since $V'=M^0 \oplus N^0$, then we obtain that $A'$ is reduced by $(M^0,N^0)$ as desired $\blacksquare$
