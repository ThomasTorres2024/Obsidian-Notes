---
title: Stoke's Theorem
tags:
  - Calculus
draft: "False"
---
# Stokes' Theorem
[[Stokes' Theorem]] can be thought of as a generalization of [[Green's Theorem]], where we take some oriented surface $S$, and stretch it out over $\mathbb{R}^3$. Intuitively, we should be able to apply [[Green's Theorem]] in some shape to the region, which is what we are hoping to show. [[Stokes' Theorem]] states that for $S$:
$$\int_{\partial S} \vec{F} \cdot \vec{dS}=\iint \text{curl}(\vec{F}) \cdot \vec{dS}$$
If we have that $\vec{F}$ is $C^1$. 
If the surface $S$ has no boundary, then the boundary set $\partial S$ and thus:
$$\iint \text{curl}(\vec{F}) \cdot \vec{dS}=\int_{\partial S =\varnothing} \vec{F} \cdot \vec{dS}=0$$

