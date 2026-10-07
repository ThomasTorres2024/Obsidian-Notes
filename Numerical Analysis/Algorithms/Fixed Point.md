---
title: Fixed Point
tags:
  - Numerical_Analysis
draft: "false"
---
# Definition Fixed Point

If $g$ is defined on $[a,b]$ and $g(p)=p$ for some $p \in [a,b]$, then the function $g$ is said to have the fixed point $p$ in $[a,b]$.  

Note that $g(x)$ has a fixed point in the interval $[a,b]$ when $g(x)$ intersects the line $y=x$. 

For instance, consider the example of $f(x)=x-\cos(x)=0$. If we write the equation of the form $x=\cos(x)$ and $g(x)=\cos(x)$ then we will obtin that there is a $0$ roughly around $(0.739,0.739)$. 

![[Pasted image 20261002122154.png]]

---
# Existence of a Fixed Point

If $g \in C[a,b]$ and $g(x) \in [a,b] : \forall x \in [a,b]$, then __the function $g$ has a fixed point in $[a,b]$. 

$Proof).$ 
If $g(a)=a$ or $g(b)=b$ existence is obvious, so we will suppose that these are not the case.

Then, it must be true that $g(a)>a$ and $g(b) < b$ (I don't like this step. This result seems true if we have that the bounds are equal by [[Rolle's Theorem]]. I think this comes from the bounds. It's a bit weird but I will assume it's that). Define $h(x)=g(x)-x$. $h$ is continuous on $[a,b]$ and moreover:
$$h(a)=g(a)-a > 0 \quad h(b)=g(b)-b < 0$$
Note by the [[Intermediate Value Theorem]] then that $\exists p \in [a,b]$ such that $g(p)-p=0 \implies g(p)=p$ means we have some fixed point $p$ of $g$. 

---

### Example). 

Consider the function $g(x)=3^{-x}$ on $0 \leq x \leq1$. $g(x)$ is continuous and since $g'(x)=-3^{-x} \log(3) <0$ on $[0,1]$ we obtain that $g(x)$ is strictly decreasing on $[0,1]$. This therefore entails that:

$$g(1)= \frac{1}{3} \leq g(x) \leq 1 = g(0) $$

Therefore $g(x) \in [0,1] : \forall x \in [0,1]$ and therefore by the prcedeing result, $g(x)$ has a fixed point in $[0,1]$. 

![[Pasted image 20261002123628.png]]

### Observation

On some interval $I=[a,b],g(x)$ may have many fixed points or also possibly none. In order to make sure that $g(x)$ has unique fixed points in $I$, we need to make an additional assumption that $g(x)$ does not vary too rapidly. 

Therefore we need to establish a uniqueness result. 

---
# Uniqueness of Fixed Point 

Let $g \in C[a,b]$ and $g(x) \in [a,b] : \forall x \in [a,b]$ . If $g'(x)$ exists on $(a,b)$ and $|g'(x)|\leq k <1$ , then $g$ has a unique fixed point $p$ in $[a,b]$. 