---
title: Group Action
tags:
  - AbstractAlgebra
draft: "False"
---
# Group Action Definition and Motivation).
A (left) [[Group Action]] of a [[Group]] $G$ on a [[Set]] $X$ is a map of the following form:
$$G \times X \to X \quad (g,x) \mapsto g\cdot x$$
Such that the following criteria are satisfied:
* $e\cdot x = x \quad \forall  x \in x$
* $(g_{1}g_{2})\cdot x = g_{1} \cdot(g_{2} \cdot x) \quad \forall g_{1},g_{2} \in G, x \in X$

---
### Definition). $G$ Equivalence 
Let $X$ be a $G$ set, and let $x,y \in X$. We say that $x$ is G equivalent to $y$ and write $x \sim Gy$ if $\exists g \in G$ such that $y=gx$. 
### Definition). Orbit 
The orbit of an element $x \in X$ is given by $O_x$:
$$O_{x} = \{y : y =g\cdot x , g \in G \}=[x]$$
We want to show that $G$ Equivalence is an [[Equivalence Relation]]. Here, the orbits should partition the set $X$. 

$$\begin{align} 
\text{ Reflexivity} \\

x \sim x \quad x=e\cdot x \\ \\
 
\text{ Symmetry}  \\

x \sim y \implies g \in G, y=g\cdot x \\
g^{-1}y=x \implies y \sim x \\\\
  
\text{ Transitivity}  \\

x \sim y, y \sim z \implies \exists g,h \in G  \\
y=g\cdot x, z=h\cdot y \implies  \\
z=h\cdot y=h(g\cdot x)
\end{align}$$
$\therefore O_{x}$ is an[[Equivalence Relation]].

---
## Definitions
Above is the __fixed point set of $g \in G$__ and the definition below is the __stabilizer subgroup of $x \in X$__. 
$$\begin{align}
X_{g} = \{x \in X : g\cdot x = x \} \\
G_{x}=\{ g\in G: g\cdot x =x \}
\end{align}$$
The second can trivially be shown to be a group. 

---
# Theorem). 
If $G$ acts on $X$ and both are finite, then:
$$|O_{x}|=[G:G_{x}]$$
$Proof.)$ 
We want to define a bijection $\phi$ which is map of the following form:
$$\phi : O_{x} \to \frac{G}{G_{x}} = L_{G_{x}}$$
Where $L_{G_{x}}$ denotes the set of left cosets. Let $y \in O_{x}$, thus $y=g\cdot x$ for some $g \in G$. We will set $\phi(y)=gG_{x}$. To begin we need to check that the mapping is well defined. 

Suppose that $\phi(y)=gG_{x}$ and that $\phi(y)=hG_{x}$:
$$\begin{align}
y=g\cdot x \quad y = h\cdot x \\
\implies (h^{-1}g)\cdot x = x  \\
\implies gG_{x}=hG_{x}
\end{align}$$
Thus the mapping is well defined. Secondly, we need to show that $\phi$ is an injective map, let us begin with the assumption:
$$\phi(y_{1})=\phi(y_{2})$$
Which entails that $\exists g_{1},g_{2} \in G$ such that:
$$y_{1}=g_{1}x \quad y_{2}=g_{2}x$$
Which gives:
$$\begin{align}
g_{1}G_{x}=g_{2}G_{x} \\
\implies g_{2}^{-1}g_{1} \in G_{x} \\
\implies (g_{2}^{-1}g_{1})x=x \\
\implies g_{1}x=g_{2}x  \\
\implies y_{1}=y_{2}
\end{align}$$
For the surjective portion, suppose that $gG_{x} \in L_{G_{x}}$. Let $y=g\cdot x \implies \phi(y)=gG_{x}$. Thus $\phi$ is injective, and then $|O_{x}|= \left|\frac{G}{G_{x}} \right|$. A result of this fact is the [[Class Equation]]. 

---
### Theorem). 
The [[Class Equation]] for [[Group Action]]s has the following form. For some [[Set]] $X$ and some group $G$ acting on said set in the perspective of [[Group Action]]s we have that:
$$|X|= \left| X_{g} \right| + \sum_{i=1}^n |O_{x_{i}}| : x_{i} \text{ forms distinct orbits that are non-single}$$
Recall that $|O_{x_{i}}|=[G:G_{x_{i}}]$.  

[[Equivalence Class]]es partition a set, and orbits form an equivalence class.  If $x \in X_{G} \implies O_{x}=\{x\}$. This can be extended to apply to [[Group]]s, which is the [[Class Equation]]. 

We need to consider all group actions. if $X=G$ can be shown to be a group action. First we have left multiplication where $g\cdot x = g \cdot x$ which is trivial. Secondly, we have right multiplication where:
$$g\cdot x = x\cdot g^{-1}$$
Then:
$$(gh)\cdot x = x \cdot (gh)^{-1}=xh^{-1}g^{-1}=g(xh^{-1})=g(h\cdot x)$$
Lastly we have conjugation, namely that:
$$g\cdot x = gxg^{-1}$$
With which we can express:
$$\begin{align}
(gh)\cdot x = (gh)x(gh)^{-1}=(gh)x(h^{-1}g^{-1}) \\
g(hxh^{-1})=g(h\cdot x)
\end{align}$$
If a [[Group]] acts on itself via conjugation, then the orbit, $O_{x}$ is actually the [[Conjugacy Class]] of $x$. 

---
## Corollary ([[Class Equation]])
If $G$ acts on $G$ and we are considering the [[Group Action]] of conjugation, we obtain the [[Class Equation]]. $O_x$ here considers [[Conjugacy Class]]es, and $G_{x}$ is the [[Centralizer]] [[Subgroup]] of some element $x$. Then we have that:
$$\large |G| = |Z(G)| + \sum_{g \in G \cap (Z(G))^c} [G:C_{G}(g)]$$
