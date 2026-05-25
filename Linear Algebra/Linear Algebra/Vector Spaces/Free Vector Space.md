---
title: Free Vector Space
tags:
  - LinearAlgebra
draft: "False"
---
# Free Vector Space
A [[Free Vector Space]] is a [[Vector Space]] given any set $S$ over the field $\mathbb{F}$ on $S$ is the set of all finite formal sums of elements of $S$ with coefficients in $\mathbb{F}$. For some set $S$ we define the free vector space on $S$ to be $V(S)$. 

---
# Theorem $V(S)$ Forms a [[Vector Space]]
Let $S$ be any set and $V(S)$ denotes the [[Free Vector Space]].

The [[Identity Element]] here is the "empty sum", not adding anything together. 
$$v= \sum_{i=1}^n a_{i}v_{i} : a_{i} \in \mathbb{F}, v_{i} \in S$$
$$\implies 0+v =v+0=v$$
We can also define addition here where $v,w$ have the following definitions:
$$v= \sum_{i=1}^n a_{i}v_{i} : a_{i} \in \mathbb{F}, v_{i} \in S \quad w= \sum_{i=1}^m b_{i}w_{i} : b_{i} \in \mathbb{F}, w_{i} \in S$$
Component wise, we cannot simplify unless $v_{i} \neq w_{i}:$
$$v+w: a_{i}v_{i} +b_{i} w_{i} = (a_{i}+b_{i})v_{i} \quad \text{(if }v_{i}=w_{i}  )$$

The other $7$ properties easily follow from this definition of addition. 

---
# Examples

### 1.  $S=\emptyset \quad v \in V(\emptyset)$:
$$v = \sum_{i=1}^n \alpha_{i} v_{i} : a_{i} \in \mathbb{F}, v_{i} \in \emptyset=0$$
Notice that this is empty set set $V(\emptyset)=\{0 \}$.  

### 2.  $S=\{x\} \quad v \in V(S)$:
$$v = ax : a \in \mathbb{F}$$
Notice that this if $\mathbb{F}=\mathbb{R}$ then we have that $V(S) \cong \mathbb{R}$ which we can denote as the product between $\mathbb{R}$ and $x$. $\mathbb{R}x$ thus:

$$V(S) \cong \mathbb{R} \cong \mathbb{R}x$$

### 3.  $S=\{x_{1},x_{2},\cdots,x_{n} \} \quad v \in V(S)$:
$$v = \sum_{i=1}^n \alpha_{i} x_{i} : a_{i} \in \mathbb{F}, x_{i} \in S$$

### 4.  $S=\{1,x,x^{2},\cdots,x^{n} \} \quad v \in V(S)$:
$$v = \sum_{i=0}^n \alpha_{i} x^i : a_{i} \in \mathbb{R}, x_{i} \in S$$
Also notice that if $n=\infty$ that:
$$V(S)=\mathbb{R}[x]=\mathbb{P}$$
### 5.) $S=\mathbb{R}$, $v \in V(S)$ 
$$v = \sum_{i=1}^n \alpha_{i} v_{i} : a_{i} \in \mathbb{R}, v_{i} \in \mathbb{R}$$
Notice also that $\alpha_{i} \cdot v_{i}$ uses __formal sums__. Some examples of elements in $V(S)$ are:

Where $2,3$ are linearly independent vectors in $V(S)$. 
$$3(2)+5(3)$$
Here $(7)$ and $(-1)$ are thought of as linearly independent vectors and it cannot be simplified. 
$$(7)+7(-1)$$ A more comprehensible way of defining vectors in this set is in the following:
$$v = \sum_{i=1}^n \alpha_{i} v_{x_{i}} : a_{i} \in \mathbb{R}, v_{x_{i}} \in \mathbb{R}$$
Rewriting the above vectors in this notation gives:
$$3v_{2}+5v_{3} \quad v_{7}+7v_{-1}$$