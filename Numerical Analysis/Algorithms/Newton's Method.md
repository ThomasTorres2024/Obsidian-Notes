---
title: Newton's Method
tags:
  - Numerical_Analysis
draft: "False"
---
# Newton's Method 
Let us suppose that we have some [[continuous]] $f$ such that $f \in C^2[a,b]$ with initial guess $p_{0} \in [a,b]$ and $|p-p_{0}|$ is small, meaning that we are in the neighborhood of the value. 

Consider the first [[Taylor Series]] polynomial for $f(x)$ expanded about $p_{0}$ and evaluated at $x=p$. Our hope is that, we get the higher order terms to tend towards $0$:

$$0 = f(p_{0}) + (p-p_{0})f'(p_{0})+\frac{(p-p_{0})^2}{2}f''(\xi(p))$$

Newton's method is essentially if we take the second order term to be $0$, then we can rewrite it such that:

$$\begin{align} 
-pf'(p_{0}) = f(p_{0}) -p_{0}f'(p_{0}) \\
  p \approx p_{0} - \frac{f(p_{0})}{f'(p_{0})}=p_{1}
\end{align}$$
This is an iterative process. We can continue feeding $p_{n}$ into itself to get $p_{n+1}$:
$$p_{n}=p_{n-1} -\frac{f(p_{n-1})}{f'(p_{n-1})} \quad n \geq1$$Iteratively, Newton's method is creating a tangent line to the curve at each step given by $f(p_{0})+(x-p_{0})f'(p_{0})$ if we used $p_{0}$ as our starting point. 

We determine the point $p_1$ at which the tangent line equals $0$ that is to say find $x=p_{1}$ such that:
$$0=f(p_{0})+(x-p_{0})f'(p_{0})$$
And then we would run the algorithm on this new value. We would then continue with subsequent iterations. 

---
# Algorithm and Stopping Conditions

To find a solution $f(x)=0$ given an initial approximation $p_{0}$:

### Newton's Algorithm
1. Set $i=0$
2. While $i \leq N$, do steps $2.1-2.5$:
	2.1 If  $f'(p_{0}) = 0$ then step 5
	2.2 Set $p=p_{0}-\frac{f(p_{0})}{f'(p_{0})}$
    2.3 If $|p-p_{0}|<TOL$, then step $6$ 
    2.4 Set $i=i+1$
    2.5 Set $p_{0}=p$
3. Output a failure message for failing to converge
4. Output an appropriate fialure message and stop
5. Output $p$ 

![[Pasted image 20261006153555.png]]

### Stopping Criteria

The following can be used for stopping criteria:

* $|p_{n}-p_{n-1}|<\epsilon$
* $\frac{|p_{n}-p_{n-1}| }{|p_{n}|}<\epsilon \quad p_{n}\neq 0$
* $|f(p_{n})|<\epsilon$

---
# [[Fixed Point Iteration]]

It turns out under the hood, [[Newton's Method]] is actually a fixed point iteration or it can be expressed as such:

$$p_{n} = p_{n-1} - \frac{f(p_{n-1})}{f'(p_{n-1})} \quad n\geq 1 $$

This allows us to express the sequence of $p_{n}$ as:
$$p_{n}=g(p_{n-1})$$
Where evidently we just sub in the above expression using $n-1$.

---
# Example)

Consider the function $f(x)=\cos(x)-x=0$. We can approximate a root of $f$ using either a fixed point method or newton's method. For the setup we have:

$$p_{n} = p_{n-1} - \frac{\cos(x)-x}{-\sin(x)-1} $$
After doing $100$ iterations on this I obtained:

```
0: 0.7853981633974483
10: 0.7390851332151607
20: 0.7390851332151607
30: 0.7390851332151607
40: 0.7390851332151607
50: 0.7390851332151607
60: 0.7390851332151607
70: 0.7390851332151607
80: 0.7390851332151607
90: 0.7390851332151607
100: 0.7390851332151607
--------------------------------------------------
Final: 0.7390851332151607
```



---
# Theoretical Importance of choice of $p_{0}$

Recall that with a [[Taylor Series]] we only have a decent __local__ approximation. As we expand from our initial point, $(p_{0},f(p_{0}))$, our solution worsens. We hope that subsequent iterations of the algorithm will be able to correct it. 

We need to ensure that the quantity, $(p-p_{0})^2$ is _negligible_, meaning that it can be treated as approximately $0$. If this criterion is not satisfied, we will likely diverge.

If $p_{0}$ is far from the actual answer, we may be far away, and it may converge it may not, we do not know. 

### Convergence Theorem for Newton's Method

Let $f \in C^2[a,b]$. If $p \in (a,b)$ is such that $f(p)=0$ and $f'(p) \neq 0$. Then, $\exists \delta >0$ such that Newton's method generates a sequence $\{ p_{n}\}_{n=1}^\infty$ defined by:

$$p_{n}=p_{n-1} - \frac{f(n-1)}{f'(p_{n-1})}$$
Which converges to $p$ for any initial condition $p_{0} \in [p-\delta,p+\delta$. This doesn't tell us if the interval as this is just an existence proof. 

---
# Tradeoffs With Newton's Method

Newton's method is very powerful, but the condition of differentiability is a considerable weakness. $f'(x)$ is hard to compute in practice.

Newton's method is very quick in convergence, in fact it is $O(n^2)$, but the overall convergence is not guaranteed. 