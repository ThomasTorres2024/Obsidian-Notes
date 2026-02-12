---
title: Stoke's Theorem
tags:
  - Calculus
draft: "False"
---
# Stokes' Theorem
[[Stokes' Theorem]] can be thought of as a generalization of [[Green's Theorem]], where we take some oriented surface $S$, and stretch it out over $\mathbb{R}^3$. Intuitively, we should be able to apply [[Green's Theorem]] in some shape to the region, which is what we are hoping to show. [[Stokes' Theorem]] states that for $S$:
$$\int_{\partial S} \vec{F} \cdot ds = \iint_D (\nabla \times \vec{F}) \cdot dS =\iint_D \text{curl}(\vec{F}) \cdot \vec{dS}$$
Where $\vec{dS}$ is normal to the surface of $S$ and is thus a [[Flux Integral]]. Note that by the reduction of the line integral down to a double integral, we are relating the surface integral over some region to simple an integral around its boundary $\partial D$. 

# Proof of [[Stokes' Theorem]] 
The general structure of the proof of [[Stokes' Theorem]] is to use [[Green's Theorem]] to show that [[Stokes' Theorem]] holds. Begin by letting $\vec{F}=\langle F_1,F_2,F_3 \rangle$, then the [[Curl]] of this expression is given by:
$$\text{curl}(\vec{F}) = \left\langle \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z}, \frac{\partial F_1}{\partial z}  - \frac{\partial F_3}{\partial x}, \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right\rangle  $$
Let $S$ be the surface the surface we are integrating over in $\mathbb{R}^3$. Let $S$ have a parametrization given by $S(u,v)=\langle u,v, f(u,v) \rangle$. Denote $f(u,v)=z. We can determine $dS$ with the following then using the standard result:
$$dS=\langle -z_x,-z_y,1 \rangle $$
Now, using these two identities we can write: 
$$\iint_S \text{curl}(\vec{F}) \cdot dS= \iint_D \left[ \left(\frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z}\right)\left(- \frac{\partial z}{\partial x} \right) +\frac{\partial F_1}{\partial z}  - \frac{\partial F_3}{\partial x}, \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right]dA$$


















If we have that $\vec{F}$ is $C^1$. 
If the surface $S$ has no boundary, then the boundary set $\partial S$ and thus:
$$\iint \text{curl}(\vec{F}) \cdot \vec{dS}=\int_{\partial S =\varnothing} \vec{F} \cdot \vec{dS}=0$$

