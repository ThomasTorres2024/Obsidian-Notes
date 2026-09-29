---
title: Convergence in Numerical Analysis
tags:
  - Numerical_Analysis
draft: "False"
---
# Convergence 
We are interested in determining the [[Numerical Stability]] of an algorithm and the [[Convergence (Numerical Analysis)]] of iterative processes. 

---
### Definition) Linear/Exponential Error
Suppose that $E_0>0$ denotes an error introduced at ome stage in the calculations, and $E_n$ represemts the magnitude of the error after $n$ subsequent operations. 

* If $E_{n} \approx C_{n}E_{0}$, where $C$ is a constant independent of $n$, then the growth is said to be linear 
* If $E_{n} \approx C^nE_{0}$ for some $C>1$, then the growth is called exponential 

---

### Definition) Rate of Convergence
Suppose that $\{ \beta_{n} \}_{{n=1}}^\infty$ is a sequence which converges to $0$ and $\{ \alpha_{n} \}_{n=1}^\infty$ converges to number $\alpha$. If $\exists k >0$ such that:
$$|\alpha _{n  }- \alpha| \leq K |\beta_{n}| \quad \text{for large }n $$
Then we say that $\alpha_{n}$ converges to $\alpha$ with a rate or order of convergence, $O(\beta_{n})$.  