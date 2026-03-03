---
title: Square Integrable
tags:
  - Functional_Analysis
draft: "False"
---
# Square Integrable Function
Let $I$ be an interval. We define the set of [[Square Integrable]] functions to be of the form:
$$\large L^2(I) = \left\{  f : I \to \mathbb{C} | \int_{I} |f(x)|^2dx < \infty  \right\} \text{ (f is square integrable on } \text{)}$$
$L$ here denotes the [[Lebesgue Integral]], and $f$ is Lebesgue measurable. $L^2(\mathbb{R})$ is the set of all [[Square Integrable]] functions over $\mathbb{R}$. 

We also have that $L^2(\mathbb{R})$ is a [[Hilbert Space]]. For $f,g \in L^2(\mathbb{R})$ we  use the following [[Inner Product]]
$$\large \langle f, g \rangle = \int_{-\infty}^\infty f(x) \overline{g(x)} dx$$
The induced $L^2$ norm is thereby:
$$\large \langle f, f \rangle = \sqrt{ \langle f, f \rangle } = \sqrt{ \int_{-\infty}^\infty f(x) \overline{g(x)} dx }$$
If the interval $I$ here is finite then it follows (this is not generally the case for an infinitely sizes interval) that:
$$\large \{ f: I \to \mathbb{C} | f \text{ is bounded} \} \subset L^2(I) \subset L^1(I)$$Where $L^1(I)$ here is the set of all [[Absolutely Integrable]] functions. 
