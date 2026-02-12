---
title: Curl Field
tags:
  - Calculus
draft: "False"
---
# Curl Field 
A [[Curl Field]] is a [[Vector Field]] that is the result of taking the [[Curl]] of another [[Vector Field]], mathematically, for a given [[Vector Field]] $\vec{F}$ we have that, iff $\vec{F}$ is a curl field that for vector field $\vec{G}$: 
$$\vec{F}= \nabla \times G = \text{curl}(G) $$
We can determine if $\vec{F}$ is a curl field by determining if $\text{div}(\vec{F})=0$. This result follows from a common fact about [[Divergence]]: 
$$\nabla \cdot (\nabla \times G )= (\nabla \times \nabla ) \cdot G$$
And becomes the matrix during the computation of curl formed by $\nabla \times \nabla$ is linearly independent, then we have that its curl is zero, and therefore the del operator with $G$ is also zero. 

We would like to be able to say that $G$ is a curl field iff  $\text{Div}(F)=0$ is, but we add on the caveat that $F$ is $C_1$ meaning that is defined for all of $x,y,z$. 