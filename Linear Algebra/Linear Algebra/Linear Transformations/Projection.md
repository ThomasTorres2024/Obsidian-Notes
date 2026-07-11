---
title: Projection
tags:
  - LinearAlgebra
draft: "False"
---
# [[Projection]] Definition
A [[Projection]] $E$ is a [[Linear Transformation]] on a [[Vector Space]] $V$ such that $V=M \oplus N$ and thus $v \in V \implies v =x+y$ for $x \in M, y \in N$. Then we have for $E$, $Ev=x$. For the matrix representation of [[Projection]]s, see [[Projection Matrices]]. 

---
# Theorem). 
A linear transformation $E$ is a [[Projection]] if and only if it is idempotent. 

### Theorem).
For a projection $E$ on some $V= M \oplus N$ then $Ez=z \implies z \in M$ and $Ez=0 \implies z \in N$. 

### Theorem). 
A linear transformation $E$ is a [[Projection]] iff $I-E$ is a projection on $N$ along $M$.

$Proof).$
$\implies).$
If $E$ is a transformation then for $x\in M$ we have that:
$$(I-E)x=x-Ex=x-x=0$$
For $y \in N$ then:
$$(1-E)y=y-Ey=0$$
We can also show that $(I-E)^2=(I-E)$:
$$(I-E)^2 = (I-E)(I-E)=I^2-2E + E^2  = I-2E+E=I-E$$
$\Longleftarrow ).$
If $I-E$ is a projection on $N$ along $M$, then for $n \in N$:
$$(I-E)n = n \iff In-En = n \iff En=0$$
Then for $m \in M$:
$$(I-E)m=0 \iff Im=Em \iff m=Em$$
Secondly it can be shown that $(I-E)^2 = (I-E) \implies E^2=E$
$$\begin{align}
(I-E)^2 = (I-E) \iff I-2E+E^2 = I-E \\
\iff -2E+E^2=-E \iff E^2 = E 
\end{align}$$
Thus the result holds. 

---
# Theorem). Combination of [[Projection]]s 
We are interested in determining under what conditions a combination of [[Projection]]s is another [[Projection]]. The following provide some criteria for $E_{1},E_{2}$ as projectors. Then: