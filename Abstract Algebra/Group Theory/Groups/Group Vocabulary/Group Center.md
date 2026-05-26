---
title: Group Center
tags:
draft: "False"
---
# Group Center 
The [[Group Center]], for a [[Group]] $G$, is denoted by $Z(G)$ is the set where for $x \in G$, we define:
$$Z(G):=\{a \in G: ax=xa ,\forall x \in G \}$$
I like to think of this as being the Abelian part. 

#### Theorem 3.5 $Z(G) \leq G$ for any [[Group]] $G$. 
Clearly $e \in Z(G) \implies Z(G) \neq \varnothing$. 

Consider $a,b \in Z(G)$ and $x \in G$ as an arbitrary element. Then, by the definition of $Z(G)$:
$$(ab)x=a(bx)$$
But since $b \in Z(G) \implies bx=xb$ so:
$$=a(xb)=x(ab) \implies ab \in Z(G)$$
Suppose $a \in Z(G)$, then $ax=xa : \forall x \in G$. 

We want to show that $a^{-1}x=xa^{-1}$. But it is known that:
$$ax=xa$$
$$\iff x=a^{-1}xa$$
$$xa^{-1}=a^{-1}x$$
So $a^{-1} \in Z(G)$. 

Since $a^{-1} \in Z(G), ab \in Z(G)$ for $\forall a,b \in Z(G)$ then $Z(G$) is a [[Subgroup]] of the [[Group]] $G$. 

---
# Definition of Centralizer of $a$ in $G$ 
We want to consider all of the elements $a \in G$, denote this object by $C_a$, which is the set of all elements of $x \in G$ such that:
$$C(a)=\{ g\in G : ga=ag \}$$
We can then show that this is a [[Subgroup]]. If $G$ is a [[Group]] and $a \in G \implies C(a) \leq G$, then it can be shown that $G$ is a [[Subgroup]]. 

---
# Examples 
#### Example for the Dihedral Group of $n$ many elements:
$$Z(D_n)=\begin{cases} \{R_0,R_\pi \} & \text{ for n is even} \\
\{R_0\} & \text{ for n is odd}
\end{cases}$$
Note that every rotation commutes with every other rotation, which is how we obtain this center. We can check this for reflectors too. 

Let $R$ be a rotator in $D_n$ and $F$ be a reflector in $D_n$:
$$RF=(RF)^{-1}=F^{-1}R^{-1}=FR^{-1}$$
Which is to say it is its own inverse. Notice for $RF$ to commute then:
$$FR=RF=FR^{-1} \implies R=R^{-1}$$
Evidently, this is only true for a rotation of $\theta=\pi,\theta=0$. $R_\pi \in D_n$ iff $n$ is even however. So, we obtain the following $Z(D_n)$ from above. 