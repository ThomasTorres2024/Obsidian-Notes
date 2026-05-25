---
title: K-Linear Form
tags:
  - LinearAlgebra
draft: "False"
---
# K-Linear Form 
An extension of a [[Bilinear Form]] from $2$ arguments to $k$ many arguments. If $X$ is some vector space and $x\in X$, and we have $k$ vectors, $x_{1},x_{2},x_{3}, \cdots,x_{k} \in X$, and a $k$ form with scalars $\alpha_{1},\alpha_{2} \in \mathbb{F}$, then:

$$w(x_{1},x_{2},\cdots,x_{k})=\alpha_{1} w(x_{1},x_{2},\cdots,x_{k}) + \alpha_{2 }w(x_{1},x_{2},\cdots,x_{k})$$

We say that a [[Multilinear Form]] is a Symmetric Form if we have that for some [[Permutation]] of arguments $\pi$ then:

$$\pi w(x_{1},x_{2},\cdots,x_{k})=w(x_{\pi(1)},x_{\pi(2)},\cdots,_{\pi(k)})$$

We can say that a form is skew symmetric if we have that for [[Multilinear Form]] $w$ and an odd [[Permutation]] $\pi$ then:
$$\pi w = -w$$
We also have the property that any Alternating Form, that is a form where if any $x_{i}=x_{j}$ in the arguments of a form $w$ are equal, then $w=0$. Any Alternating Form is skew symmetric. 

Another alternative condition for skew symmetry is if given any permutation $\pi$, then:

$$\text{sgn}(\pi) w=w$$

---
# Theorem - Any Alternating Form is Skew Symmetric
We can take 2 forms where we fix the other arguments (I don't know why?) and then we have:

$$w(x_{i}+x_{j},x_{i}+x_{j})=0 = w(x_{i},x_{i})+w(x_{i},x_{j})+w(x_{j},x_{i})+w(x_{j},x_{j})=w(x_{i},x_{j})+w(x_{j},x_{i})$$
$$\iff w(x_{i},x_{j})=-w(x_{i},x_{j})$$
These properties imply each other (this also pops up in Grassman Algebras and is essentially the same property).

---
# Theorem - If $x_{1},x_{2},\cdots,x_{k}$ are a linearly dependent set of vectors and if $w$ is an alternating $k$ linear form then $w(x_{1},x_{2},\cdots,x_{k})=0$

Suppose $x_{h}$ is a vector that can be expressed a linear combination of the other vectors, then we can write:
$$x_{h}=\sum_{i=0}^h\alpha_{i}x_{i}:\alpha_{i} \in \mathbb{F}$$
Using the properties of linearity, $$w(x_{1},x_{2},\cdots,x_{k})=w\left(  x_{1},x_{2},\cdots,\sum_{i=0}^{k-1}\alpha_{i}x_{i},\cdots,x_{k} \right)= \sum_{i=1}^{k-1} \alpha_{i}w(x_{1},x_{2},\cdots,x_{i},\cdots,x_{k}) =0$$
Then since $w$ is alternating and has duplicate terms it is $0$. 

---
# Theorem - If $w$ is a non-zero alternating $n$ linear form and if $x_{1},x_{2},\cdots,x_{n}$ are linearly independent then $w(x_{1},x_{2},x_{3},\cdots,x_{n})\neq0$ 

$Proof.)$ Consider an arbitrary set of vectors $y_{1},y_{2},\cdots,y_{n}$ and we can express each $y$ in this set as a linear combination of vectors of $x_i$. We can then replace each vector in the following linear form and obtain the following:

$$w(y_{1},y_{2},y_{3},\cdots,y_{n}) \to \sum w(z_{1},z_{2},\cdots,z_{n})$$
If two of the $z$ vectors coincide then that particular $w(z_{1},z_{2},\cdots,z_{n})=0$. On the other hand since we have the case where each $z_{i}$ is distinct, then $w(z_{1},z_{2},z_{3},\cdots,z_{n})=\pi w(x_{1},x_{2},x_{3},\cdots,x_{n})$ for some permutation $\pi$, which follows from the definition of skew symmetry since $w$ is an alternating form. 

If $w$ were $0$ then we would have that:

$$w(x_{1},x_{2},x_{3},\cdots,x_{n})=0 \implies w(z_{1},z_{2},z_{3},\cdots,z_{n})=0 \implies w(y_{1},y_{2},\cdots,y_{n})=0 $$
Which would hold for any set of $y$ vectors and contradict the assumption that $w$ is not the $0$ form $(w\neq 0)$. 

---
# Theorem - Any $2$ alternating $n$-linear forms are linearly dependent 
Suppose that $w_1,w_2$ are $2$ alternating $n$ linear forms and that $\{x_{1},x_{2},\cdots,x_{n} \}$
is a basis. Given any $n$ vectors $\{y_{1},y_{2},\cdots,y_{n} \}$, each can be written as a linear combination of the $x$ vectors. 

Replace the vectors in $w_{1}(y_{1},y_{2},y_{3},\cdots,y_{n})$,$w_{2}(y_{1},y_{2},y_{3},\cdots,y_{n})$ with $x$ vectors and obtain the following:

$$w_{1}(z_{1},z_{2},z_{3},\cdots,z_{n}) \quad w_{2}(z_{1},z_{2},z_{3},\cdots,z_{n})$$
Since both $w_{1}$ and $w_2$ are scalars they are linearly independent and thus there exists scalars such that the following is true: 

$$\alpha_{1}w_{1}+\alpha_{2}w_{2}=0$$
From this we may obtain the fact that the linear functionals are independent since we know that $w_{1}\neq 0$ and $w_{2} \neq 0$ since the vectors plugged into them are linearly independent. 

