---
title: Secant Method
tags:
  - Numerical_Analysis
draft: "False"
---
# Secant Method 

The [[Secant Method]] is derived from [[Newton's Method]]. We opt to use an approximation for the [[derivative]] of a function instead of a directly differentiable function. Using the derivative of a lot of functions in the real world is often costly and too complicated to compute. Therefore, using this method we approach a solution much easier.

$$f'(p_{n-1})= \lim_{ x \to p_{n-1}} \frac{f(x)-f(p_{n-1})}{x-p_{n-1}} $$

Since we use a secant line to approximate the derivative, we need to use two points, $p_{0},p_{1}$:

If $p_{n-2}$ and $p_{n-1}$ are close, then:
$$f'(p_{n-1}) \approx \frac{f(p_{n-2}) -f(p_{n-1})}{p_{n-2}-p_{n-1}}$$
We can use this approximation for $f'(p_{n-1})$ in Newton's formula to obtain:
$$p_{n}=p_{n-1} - \frac{f(p_{n-1} )(p_{n-1}-p_{n-2} ) }{f(p_{n-1}) - f(p_{n-2}) }$$

---
# The Secant Method Algorithm
### Procedure

* We begin $2$ initial approximations, $p_{0},p_{1}$. $p_{2}$ is the $x$ intercept of the line that joins $(p_{0},f(p_{0}))$ and $(p_{1},f(p_{1}))$.  
* Likewise, $p_{3}$ is the $x$ intercept of the line that joins $(p_{1},f(p_{1}))$ and $(p_{2},f(p_{2}))$.  
* We only need a single function evaluation per step after we have evaluated $p_{2}$.
* Newton's method requires both the evaluation of a function and its derivative at each step. 

### Algorithm Pseudocode

1. Set $i=2,q_{0}=f(p_{0}), q_{1}=f(p_{1})$
2. While $i\leq N_{0}$, do steps 3-6
	3. Set $p=p_{1}-\frac{q_{1}(p_{1}-p_{0})}{(q_{1}-q_{0})}$ (Compute $p_i$)
	4. If $|p-p_{1}| < TOL$ then output $p$, stop
	5. set $i=i+1$
	6. Set $p_{0}=p_{1}$ (update $p_{0},q_{0},p_{1},q_{1}$) and $q_{0}=q_{1};p_{1}=p;q_{1}=f(p)$. 
3. Output after execution within the loop ends if failed or converged

![[Pasted image 20261006130258.png]]

---
