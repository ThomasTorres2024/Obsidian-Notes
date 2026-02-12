---
title: Search Method
tags:
  - Optimization
draft: "False"
---
# Search Method
A [[Search Method]] in [[Optimization]] is a method that looks for the extrema of a function $f: \mathbb{R}^n \to \mathbb{R}$ by iterating upon the previous result until it converges to some region where the result approximately is. 

---
# 1-D Search Methods 
A sequence of real numbers is said to converge to some limit.
$$\{x_0, x_1, x_2 \dots , x_k \} \to \{x_k \}, \{x_k \}_{k=0}^\infty$$
If the sequence $\{x_k \}$ has a limit, denote it $x^*$, then the sequence $\{x_k\}$ is a convergent series. More formally, we say that $\forall \epsilon > 0, \exists k$that $\forall k > K$:
$$\|x_k -x^*\| < \epsilon$$
If the limit of the sequence exists, we say that it is unique. If the limit exists, then:
$$\lim_{k \to \infty} \|x_k -x_{k+1}\| =0$$
Also note that any [[Monotone Bounded Sequence]] converges. 