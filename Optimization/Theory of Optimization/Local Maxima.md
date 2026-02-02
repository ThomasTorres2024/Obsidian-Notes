---
title: Local Maxima
tags:
draft: "False"
---
# Local Maxima 
The [[Local Maxima]] of a function, $f : \mathbb{R}^n \to \mathbb{R}$, tells us that over some region, $D$, we have that the [[Local Maxima]], $x^*$ satisfies that:
$$f(x^*) \geq f(x), \forall x \in D$$
Note that $x^*$ is not necessarily unique, as a function may have multiple local maxima. The way that we specify $D$ is by considering some bound, $\epsilon \in \mathbb{R}$, such that:
$$D=\{x \in \mathbb{R}^n : \|x^*-x\| \leq \epsilon \}$$
Which is to say all of the vectors are within a distance ([[norm]]) of $\epsilon$ from the local minimum. 