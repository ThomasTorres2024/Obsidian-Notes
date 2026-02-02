---
title: Local Minima
tags:
  - Optimization
draft: "False"
---
# # Local Minima 
The [[Local Minima]] of a function, $f : \mathbb{R}^n \to \mathbb{R}$, tells us that over some region, $D$, we have that the [[Local Minima`]], $x^*$ satisfies that:
$$f(x^*) \leq f(x), \forall x \in D$$
Note that $x^*$ is not necessarily unique, as a function may have multiple local minima.  The way that we specify $D$ is by considering some bound, $\epsilon \in \mathbb{R}$, such that:
$$D=\{x \in \mathbb{R}^n : \|x^*-x\| \leq \epsilon \}$$
Which is to say all of the vectors are within a distance ([[norm]]) of $\epsilon$ from the local minimum. 