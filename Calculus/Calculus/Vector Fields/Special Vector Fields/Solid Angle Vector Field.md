---
title: Solid Angle Vector Field
tags:
  - Calculus
draft: "False"
---
# The [[Solid Angle Vector Field]]
We define the [[Solid Angle Vector Field]] ([[Vector Field]]) for $\mathbb{R}^2$ by:
$$\mathbb{A}= \frac{1}{x^2+y^2} \langle x,y\rangle$$
We can define it for $\mathbb{R}^n$ by:
$$r=\sqrt{\sum_{i=1}^n x_i^2} $$
And use the [[Position Vector Field]], $\vec{r}$. Then the [[Solid Angle Vector Field]] is defined by:
$$\mathbb{A} : \mathbb{R}^n \to \mathbb{R}^n , \mathbb{A}= \frac{\vec{r}}{r^n}$$
If we consider the [[Flux]] of some surface $S$ in $\mathbb{A}$, we would obtain the angle that it spans. 

---
# Relationship Between the [[Solid Angle Vector Field]] and the [[Angle Element Vector Field]] in $\mathbb{R}^2$
In $\mathbb{R}^2$, both of these vector fields can be used to measure how far some curve extends. It is also the case that both of these vector fields will return the same angle in this special case. Recall the definition of the [[Angle Element Vector Field]]: 
$$\mathbb{a}(x,y)=\frac{1}{x^2+y^2}\langle -y,x \rangle $$
Notice that $\mathbb{a}$ is just a rotation of the [[Solid Angle Vector Field]] by $\frac{\pi}{2}$ radians. Similarly, we also rotate the surface, and since rotation will preserve the total angle stretched, we maintain the same difference in angle. 


