---
title: Error Analysis for Iterative Algorithms
tags:
  - Numerical_Analysis
---
# Error Analysis for Iterative Algorithms

How do we determine the rate of convergence of a method?

---
# Definition - __Order of Convergence__

Suppose $\{ p_{n} \}_{n=0}^\infty$ is a sequence that converges to $p$ with $p_{n} \neq p, \forall n$. If positive constants $\lambda, \alpha$ exist that satisfy:

$$\lim_{ n \to \infty } \frac{|p_{n+1}-p|}{|p_{n}-p|^\alpha}  = \lambda $$
Then $\{ p_{n}\}_{n=0}^\infty$ __converges to $p$ of order $\alpha$ with asymptotic error constant $\lambda$.__  

---
# Theorem - Linear Convergence 
Let $g \in C[a,b]$ such that $g(x) \in [a,b], \forall x \in [a,b]$. Suppose in addition that $g'$ is [[continuous]] on $(a,b)$ and a positive constant $k<1$ exists s.t. 
$$|g'(x)| \leq k \quad \forall x \in (a,b)$$
If $g'(p) \neq0$, then for any number $p_{0} \neq p$ in $[a,b]$ the sequence:

$$p_{n}=g(p_{n-1}) \quad n \geq 1$$
Converges only __linearly__ to the unique fixed point $p$ in $[a,b]$. 

---
# Theorem - Quadratic Convergence 

Let $p$ be a solution of the equation $x=g(x)$. Suppose that $g'(p)=0$ and $g''$ is continuous with $|g''(x)| < M$ on an open interval $I$ containing $p$. Then, $\exists \delta >0$ such that for $p_{0} \in [p- \delta, p+ \delta]$, the sequence defined by $p_{n}=g(p_{n-1})$ when $n\geq1$, converges at __at least quadratically to $p$__. Moreover, for sufficiently large values of $n$:

$$|p_{n+1}-p| < \frac{M}{2} |p_{n}-p|^2 $$