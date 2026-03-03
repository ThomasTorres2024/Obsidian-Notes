---
title: Pythagorean Theorem
tags:
  - Geometry
draft:
aliases:
---
# Pythagorean Theorem 
##### Proof for Linear Algebra 
$n=1$ is trivially true, so we have a base case. Assume the Pythagorean identity holds for $n-1$. 
$$ \large \left\| \sum_{i=1}^n \vec{x_{i}} \right\|^2 = \left( \sum_{i=1}^n \vec{x_{i}} \right)^T \cdot \left( \sum_{i=1}^n \vec{x_{i}} \right) = \left( \sum_{i=1}^{n-1}  \vec{x_{i}} + \vec{x}_{n} \right)^T \cdot \left( \sum_{i=1}^{n-1} \vec{x_{i}} + \vec{x}_{n} \right)     $$
$$ \large =\left\| \sum_{i=1}^{n-1} \vec{x_{i}} \right\|^2 + \| \vec{x_{n}}\|^2 + 2\left \langle \left( \sum_{i=1}^n \vec{x_{i}} \right),\vec{x_{n}} \right\rangle= \sum_{i=1}^{n-1} \| \vec{x_{i}}\|^2+\|\vec{x_{n}}\|^2=\sum_{i=1}^n \| \vec{x_{i}}\|^2$$
Therefore, the [[Pythagorean Theorem]] holds in any general finite dimension vector space. 