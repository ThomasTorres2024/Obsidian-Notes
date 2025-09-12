---
title: Multivariable Limit
tags:
draft: "false"
---
# Multivariable Limit Definition
The [[Multivariable Limit]] is an extension of the notion of a [[Limit]] to functions that have more than one variable. Working with multivariable functions is complex since in the one dimensional case we only have one axis to worry about, which means that we only have one possible path to evaluate our derivatives and integrals along.

In the multivariable case we have to consider an infinite number of paths that go through the point we want to find the limit at, $(a,b)$. Let $F: U \subseteq  \mathbb{R}^n \to \mathbb{R}^m$. Then, all of the following paths in the graphic below would be valid paths we need to consider. The limit must be satisfied along all of these definitions. 

![[Pasted image 20250912132205.png]]
For practical computations of these things we need to be able to ensure that we can use a delta epsilon proof through inequalities, because we obviously cannot compute each and every path with goes through this point, and we can also use conversion to other coordinate systems in order to facilitate the transformation of a multivariable limit into a one dimensional or simpler one. 

We also need to be able to generalize the [[Epsilon-Delta Limit]] from the single variable case into the multivariable one. Before, we considered a small interval $\delta > 0$ around $x$, which would give us the closed interval $(x-\delta,x+\delta)$. Now we have to account for the fact that the point lives in $\mathbb{R}^n$, accordingly we have to change how we think of this problem using vectors. 

We want to consider all paths through the point, so let us consider some small $n$-Sphere that runs through the point. We will denote this set centered around our point, $\vec{a}$, by $U \subseteq \mathbb{R}^n$.  All points in this ball have a distance $\delta > 0$ away from its origin. Translating this to a vector equation we can express that:
$${0<\|\vec{x}- \vec{a} \| < \delta}$$
Similarly, we must re-write our limit and epsilon conditions. Let $\epsilon > 0$. We should similarly be able to constrain the set of all outputs within the sphere to an $m$-Sphere. The limit would now be a vector given by $\vec{l}$. For any $\vec{x} \in U$, we need to express the idea that $0<|f(x)-\mathcal{L}|<\epsilon$ in higher dimensions. We can take the [[Euclidean Norm]] again of our expression to force it to be a scalar, and we can get the following condition:
$$0 <\| f\vec{x}-\vec{l} \| < \epsilon$$
We should now be able to give a full concrete and completely rigorous definition for the [[Epsilon-Delta Limit]] of a Multivariable function:
$$\vec{x}\in U, \forall \delta >0, \exists \epsilon | \text{ }0 <\|\vec{x}-\vec{a}\| < \delta \implies 0 < \|f(\vec{x})-\vec{l}\| < \epsilon  $$
