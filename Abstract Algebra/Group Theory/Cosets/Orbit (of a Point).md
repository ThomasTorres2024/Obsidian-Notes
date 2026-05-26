---
title: Orbit (of a Point)
tags:
  - AbstractAlgebra
draft: "False"
---
# Orbit (of a Point)

Let $G$ be a [[Permutation Group]] of a set $S$. For each $i \in S$, we have that:

$$\text{orb}_{G}(i)=\{ \phi(i) : \phi \in G \}$$

Which is to say all of the elements that every [[Permutation]] $\phi$, maps elements from $i$ to other elements in $S$. The set $\text{orb}_{G}(i) \subseteq S$, is called the __orbit of $i$ under $G$__. 

The number of elements in $|\text{orb}_{G}(i)|$ is used to denote the number of elements in the set $\text{orb}_{G}(i)$. 

---
# Example.)

Let $G < S_8$:

$$G=\begin{align} \{ (1),(132)(465)(78),(132)(465), \\
(123)(456),(123)(456)(78),(78)
\}

\end{align}$$

We then have that: 


$$\begin{align}
\text{orb}_{G}(1) = \{  1,3,2\} \quad   \text{stab}_{G}(1) = \{ (1),(78)  \}\\
\text{orb}_{G}(2) = \{  2,1,3\} \quad  \text{stab}_{G}(2) = \{ (1),(78)  \}\\
\text{orb}_{G}(4) = \{  4,6,5\} \quad \text{stab}_{G}(4) = \{ (1),(78)  \}\\ \\

\text{orb}_{G}(7) = \{  7,8\} \quad \quad \text{stab}_{G}(7) = \{ (1),(132)(465),(123)(456)  \}
\end{align}$$

---
# Example.) 
Consider the Dihedral group $D_4$:

$$D_{4} = \left\{  R_{0},R_{\frac{\pi}{2}} ,R_{\pi}, ,R_{\frac{3\pi}{2}}, R_{0}F, R_{\frac{\pi}{2}}F, R_{\pi}F, R_{\frac{3\pi}{2}}F    \right\}$$

The orbit of a point $p$ under $D_4$, where $p$ is one of the axes, consists of a rotation of $p$ onto different axes, this its orbit is:

$$\text{stab}_{{D_{4}}}(p)=\{R_{0},F \}$$

---
# Theorem ). Orbit-Stabilizer Theorem 

([[Stabilizer of a Point]])

Notice that in both of the examples we see that:

$$|G| = |\text{orb}_{G}(i)| \cdot |\text{ stab}_{G}(i)|$$

Equivalently we can also say that the index ([[Lagrange's Theorem]]) of the orbit of $i$ is:

$$|\text{orb}_{G}(i)| = \frac{|G|}{|\text{stab}_{G}(i)|}$$
### $Proof.)$ 
By [[Lagrange's Theorem]], for $i \in S$ we have that: 

$$[G : \text{stab}_{G}(i)]=\frac{|G|}{|\text{stab}_{G}(i)| }$$ We want to define a correspondence $T$ from left [[Coset]]s of $\text{stab}_{G}(i)$ to elements of $\text{orb}_{G}(i)$ via the following function:

$$T: \phi \text{ stab}_{G(i)} \to \phi(i)$$

We must show all of the following things. We need to show that $T$ is well-defined, $T$ is injective, and that $T$ is surjective. 

1. $T$ is well defined. We want to show that if $\alpha \text{ stab}_{G}(i) = \beta \text{ stab}_{G}(i) \implies \alpha(i)=\beta(i)$. 

$$\begin{align}
\alpha \text{ stab}_{G}(i)   =  & \text{ } \beta \text{ stab}_{G}(i)  \\
 \Updownarrow  \\
  \alpha \beta^{-1} \in \text{ stab}_{G}(i)     \\ \\
(\alpha^{-1}\beta) \in \text{stab }_{G}(i) \\
\Updownarrow  \\  
\alpha(i) = \beta(i) \\

\end{align}$$

2. $T$ is injective 

if $\alpha(i)=\beta(i) \implies \alpha \text{stab}_{G}(i)= \beta \text{stab}_{G}(i)$. Using the above argument, we can reverse the direction and obtain this result, meaning that $T$ is injective. 

3. $T$ is surjective 

Let $j \in \text{orb}_{G}(i)$, then by definition: 

$$j=\alpha(i) : \alpha \in G \text{ for some } \alpha$$

And then we have that: 

$$T(\alpha \text{ stab}_{G}(i))=\alpha(i)=j$$

And thus $T$ is onto. 

By $1,2,3$ there is a correspondence between the left cosets of $\text{stab}_{G(i)}$ and the elements of $\text{orb}_{G(i)}$, and therefore we obtain that:

$$\therefore |\text{orb}_{G}(i)| = \frac{|G|}{|\text{stab}_{G}(i)|}$$

