---
title: Analytic Function
tags:
draft: "False"
---
# Definition
An [[Analytic Function]] is a function, $f(z) : \mathbb{C} \to \mathbb{C}$ such that on an open set, $U$, $\exists f'(z),$ for each $z \in U$. Meaning, that we can differentiate at every point along $U$. 

Some definitions also include [[Goursat's Theorem]], which states that if $\exists f'(z)$ then $f'(z)$ is [[continuous]]. 

We also have the notion of being analytic at a point, $z_{0} \in \mathbb{C}$, which is to say we are analytic on an open disc centered at $z_{0}$. 

---
# Test to Determine if a Function is Analytic or Not 
If we decompose a complex function into two real valued functions, $u,v$ where $\mathbb{R}^2 \to \mathbb{R}$ , then we can write:
$$f(z)=u(x,y)+v(x,y)\cdot i=u+vi$$
There are two necessary and sufficient conditions for such a function to be an analytic function that we must satisfy. The first condition are the [[Cauchy Riemann Equations]] and the 

* [[Cauchy Riemann Equations]] two differential equations of a function that must be true: $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} $$
* Continuity of First Partials of $u$ and $v$ on $U$ 

#### (Proof) [[Cauchy Riemann Equations]] and Continuity of First Partials $\implies f(z)$ is analytic 

If $f(z)$ is analytic, then $$f'(z_{0}) = \lim_{z \to z_{0}} \frac{f(z)-f(z_{0})}{z-z_{0}}$$
Writing $z \to z_{0}$ is equivalent to writing $(x,y) \to (x_{0},y_{0})$, therefore we can write that:
$$f'(z_{0}) = \lim_{x,y \to x_{0},y_{0}} \frac{u(x,y)+iv(x,y)-(u(x_{0},y_{0})-iv(x_{0},y_{0}))}{(x+iy)-(x_{0}+iy_{0})}$$
$$= \lim_{x,y \to x_{0},y_{0}} \frac{(u(x,y)-u(x_{0},y_{0}))+i(v(x,y)-iv(x_{0},y_{0}))}{(x-x_{0})+i(y-y_{0})}$$