---
title: Conservative Vector Fields
tags: 
draft: "false"
---
# Conservative Vector Field Definition
A [[vector field]], $\vec{F}$ is conservative if it satisfies the following definition for a [[Line Integral]] over a path $\vec{r}$:
$$\int_{c}\vec{F}\cdot d\vec{r}=f(p_{1})-f(p_{0})$$
Which verbally means that the line integral between any path along a vector field is really equivalent to evaluating its [[Potential]] function on the endpoints of the curve. From this there are some following equivalent conditions to a vector field being conservative:

1. $\vec{F}$ is conservative
2. $\int_{c} \vec{F} \cdot d\vec{r}$ is path independent
3. $\int_{c}\vec{F}\cdot d\vec{r}=0$ for all closed curves $c$, we can think of this as two curves composing a single curve which in total must be a closed path
4. $\vec{F}$ is a [[Gradient Field]] 
5. $Mdx+Ndy=df$ is an exact differential equation, which is equivalent to being able to express our differential equation as the forms above as the differential 