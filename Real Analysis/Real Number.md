---
title: Real Analysis
tags:
  - Real_Analysis
draft: "False"
---
# Real Numbers
Real analysiis studies concepts related to [[Real Number]]s. On one hand, we can begin with the [[Natural Number]]s, e.g. $1,2,3,\dots$ as undefined concepts and then construct from these the larger posiitive [[Rational Number]]s, negatives, and zero. From this we can construct the [[Irrational Number]]s like for instance $\sqrt{ 2 },\pi$.

The rational and irrational numbers constitute the reals. 

---
### Field Axioms of the Reals 
With the set $\mathbb{R}$ assume we have two [[Binary Operation]]s $+,\cdot$ addition and multiplication respectively wiith which we can form a [[Field]] such that the following are true:

1. $x+y=x+x \quad xy=yx$
2. $x+(y+z)=(x+y)+z \quad x(yz)=(xy)z$
3. $x(y+z)=xy+xz$

4. Given any two reals $x,y$ $\exists z \in \mathbb{R}$ such that $x+z=y$ where $z$ is denoted as $z=y-x$ and $x-x$ is denoted by $0$. 
5. If $x,y$ are two reals where $x\neq0$, then $\exists z \in \mathbb{R}$ where $xz=y$ where $z=\frac{y}{x}$

All laws of arithmetic can be derived from these expressions.

---
#### The Order Axioms 

We assume that there is a relation $\text{"<"}$ such that:

6. Exactly one of these holds for $x,y \in \mathbb{R}:x=y,x>y,y<x$

7. If $x<y$ then $\forall z \in \mathbb{R}$ we have $x+z<y+z$

8. If $x>0$ and $y>0$ then $xy>0$

9. If $x>y$ and $y>z$ then $x>z$ 

__Note__
A real number $x$ is positive if $x>0$ and negative if $x<0$. $\mathbb{R}^+$ is the set of all positive reals, and $\mathbb{R}^-$ is the set of all negatrive reals. 

From the order axioms have the typical rules of operating with inequalities. 


# Theorem 1.1 -
Given reals $a,b \in \mathbb{R}$ such that $a \leq b + \varepsilon$ $\forall \varepsilon >0$ then $a\leq b$. 

BWOC assume that $a>b$. Let $\varepsilon=\frac{a-b}{2}$, so $\varepsilon > 0$ 
$$a\leq b+\varepsilon = b + \frac{a-b}{2} = \frac{a+b}{2} < \frac{a+a}{2} =a$$
From which we get $a<a$ which is an obviouus contradiction. 
Then by axiom $6$ it must be the case that $a\leq b$.  

---
### Definition: Closed and Open Interval
A closed interval contains the endpoints of the interval, for example:
$$[a,b]=\{ x: a\leq x \leq b \}$$
An open interval does not, for example:
$$(a,b)=\{x:a<x<b\}$$
A single point is sometimes considered a "degenerate closed interval". 

---
# Integers 
The integers form a subset of $\mathbb{R}$ 