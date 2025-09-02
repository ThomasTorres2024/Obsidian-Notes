---
title: The Divergence Theorem
tags: 
draft: "false"
---
# The Divergence Theorem
We refer to this result also as the Gauss-Green Theorem". This allows us to avoid calculation of [[Surface Integral]]s. This is also a 3D analog of [[Green's Theorem]] for [[Flux]]. 

If $S$ is a closed surface that encloses our surface $D$, and $\vec{n}$ is oriented outwards, and $\vec{F}$ is defined and differentiable everywhere in $D$, then we can actually express our closed surface integral as a triple integral:
$$\underset{ S \;}{ {\rlap{\mspace{1mu} \boldsymbol{\bigcirc}}{\rlap{\int}{\;\int}}} } \vec{F} \cdot d\vec{S}= \iiint_{D} \text{div}(\vec{F})\cdot dV $$
We need to note that our [[Divergence]] is different for 3 dimensions. We define our divergence for the vector field, $\vec{F}=P\hat{i}+Q\hat{j}+R\hat{k}$ as:
$$\text{div}(\vec{F})=P_{x}+Q_{y}+R_{z}$$
#### Example 1.) Sphere
Consider the sphere of radius $a$ centered at the origin through the vector field $\vec{F}=z\hat{k}$ Green's theorem allows us to express our flux integral as:
$$\underset{ S \;}{ {\rlap{\mspace{1mu} \boldsymbol{\bigcirc}}{\rlap{\int}{\;\int}}} } z\hat{k} \cdot \hat{n} \cdot ds= \iiint_{D} \text{div}(z\hat{k})\cdot dV = \iint_{D}dV= \dfrac{4}{3} \pi a^3 $$
---
# Issues with Integration
Say if we have a volume region that is not vertically simple, we can cut it into regions which actually are vertically simple, and the flow in two different parts cancels out. 