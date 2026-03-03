---
title: Absolutely Integrable
tags:
  - Functional_Analysis
draft: "False"
---
# Absolutely Integrable Function
Let $I$ be an interval. We define the set of [[Absolutely Integrable]] functions to be of the form:
$$\large L^1(I) = \left\{  f : I \to \mathbb{C} | \int_{I} |f(x)|dx < \infty  \right\} \text{ (f is absolutely integrable on } \text{)}$$
$L$ here denotes the [[Lebesgue Integral]], and $f$ is Lebesgue measurable. $L^1(\mathbb{R})$ is the set of all [[Absolutely Integrable]] functions over $\mathbb{R}$. 

It is also the case that $L^1(\mathbb{R})$ is a [[Vector Space]] over $\mathbb{C}$ of $\mathcal{F}(\mathbb{R}, \mathbb{C})$. Furthermore, it is a [[Normed Space]], which uses the [[Manhattan Distance]] (L1) [[Norm]] of the following form:
$$\large \|f\|_{1} = \int_{-\infty}^\infty |f(x)|dx$$

A piecewise continuous function is continuous on $I$ except for at finitely many points $\{ x_{k} \}$. We have that everywhere along $I$ has a one sided limit which either exists, or evaluates to $\pm \infty$:
$$\large f(x_{k}^-) = \lim_{ x \to x_{k}^- } f(x) \text{ and } f(x_{k}^+) = \lim_{ x \to x_{k}^+ } f(x)$$
