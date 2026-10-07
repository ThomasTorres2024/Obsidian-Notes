---
title: Bisection Method
tags:
  - Numerical_Analysis
draft: "False"
---
# Bisection Method
One of the most basic problems of numerical approximation is root finding. This process involves finding a root, naemly $x$ such that $f(x)=0$ for some given function $f$. This is a [[Binary Search]] method based on the [[Intermediate Value Theorem]].

This algorithm is _agnostic to the number of zeroes_, meaning that we can only find _one_. It does not fail if there are multiple. 

Suppose we have a [[continuous]] function $f$ on $[a,b]$ given that $f(a),f(b)$ are oppositely signed. 

---
# Algorithm 
To begin, set $a_{1}=a$ and $b_{1}=b$, let $p_{1}$ be the midpoint of $[a,b]$ that is:

$$p_{1}=a_{1}+\frac{b_{1}-a_{1}}{2} = \frac{a_{1} + b_{1}}{2}$$
We prefer to write the midpoint here in this manner so that we can get a [[Numerical Stability]] value for the midpoint. Now we proceed to the algorithm:

* $f(p_{1})=0$ We are done
* If $f(p_{1}) \neq0$ then $f(p_{1})$ has the smae sign as one of the two
	* If $a_{1},p_{1}$ have the same sign, set $a_{2}=p_{1}$ and $b_{2}=b_{1}$
	* Otherwise $a_{2}=a_{1},b_{2}=p_{1}$

Basically we just narrow ourselves down to a section that's smaller and smaller which encloses on a zero:

![[Pasted image 20260929125634.png]]

Let us translate this succinctly into an algorithm:

1. $a_{1}=a,b_{1}=b,p_{0}=a;$
2. $i=1;$
3. $p_{i}=\frac{1}{2} (a_{i} +b_{i);}$
4. If $|p_{i}-p_{i-1}|<\epsilon \implies \text{ terminate};$
5. If $f(p_{1})f(a_{i})>0$ then go to $6;$ If $f(p_{i})f(a_{i})<0,$ then go to $8$;
6. $a_{i+1}=p_{i},b_{i+1}=b_{i};$
7. $i=i+1;$ go to $3$;
8. $a_{i+1}=a_{i}; b_{i+}=p_{i};$
9. $i=i+1;$ go to $3;$ 
10. End of procedure 

We can also chooe other stopping procedures in step 4, we can use relative error provided that $P_{n}\neq {0}$:

$$\begin{align}
|P_{n} < P_{n-1}| < \epsilon \\
\frac{|P_{n} < P_{n-1}| }{|P_{n|}}< \epsilon \quad P_{n} \neq 0  \\
|f(P_{n})|<\epsilon
\end{align}  
$$

---
### Example). $f(x)=x^3+4x^2-10=0$

Show that $f(x)$ has a root on $[1,2]$ and use the bisection method to determine an aprpoximation to the root that is accurate to at least within $10^{-4}$, 

#### Solution. 
First we need to check that a $0$ value occurs. Check $f(1),f(2)$ are oppositely signed yielding $f(1)=-5,f(2)=14$ thus by IVT we have a root on $[1,2]$. 

For the first iteration of the bisection method we have $f(1.5)=2.3$, we set $a_{2}=1,b_{2}=1.5$, and then we continue iterating: 

$$\begin{array}{c|c|c|c|c|c|c}
\text{Iter} & a_n & b_n & p_n & f(a_n) & f(p_n) & \text{RelErr} \\ \hline
1  & 1.000000 & 2.000000 & 1.500000 & -5.000 & 2.375  & 0.33333 \\
2  & 1.000000 & 1.500000 & 1.250000 & -5.000 & -1.797 & 0.20000 \\
3  & 1.250000 & 1.500000 & 1.375000 & -1.797 & 0.162  & 0.09091 \\
4  & 1.250000 & 1.375000 & 1.312500 & -1.797 & -0.848 & 0.04762 \\
5  & 1.312500 & 1.375000 & 1.343750 & -0.848 & -0.351 & 0.02326 \\
6  & 1.343750 & 1.375000 & 1.359375 & -0.351 & -0.096 & 0.01149 \\
7  & 1.359375 & 1.375000 & 1.367188 & -0.096 & 0.032  & 0.00571 \\
8  & 1.359375 & 1.367188 & 1.363281 & -0.096 & -0.032 & 0.00287 \\
9  & 1.363281 & 1.367188 & 1.365234 & -0.032 & 0.000  & 0.00143 \\
10 & 1.363281 & 1.365234 & 1.364258 & -0.032 & -0.016 & 0.00072 \\
11 & 1.364258 & 1.365234 & 1.364746 & -0.016 & -0.008 & 0.00036 \\
12 & 1.364746 & 1.365234 & 1.364990 & -0.008 & -0.004 & 0.00018 \\
13 & 1.364990 & 1.365234 & 1.365112 & -0.004 & -0.002 & 0.00009
\end{array}$$
Notice that we eventually tend towards a $0$ as the iteration continues. We can approximate the stopping size by using the bounds of the interval, we know that $|b_{n}-a_{n}|\geq |p-p_{n}|$ and if it happens that $|b_{n}-a_{n}|$, we also have that:

$$\frac{|p-p_{n}|}{|p|} \leq \frac{|a_{n}-b_{n}|}{|a_{n}|}$$
Furthermore, we can determine the number of significant digits. Since for this problem we chose the upper bound epsilon to be $10^{-4}$, which helps us in this endeavor. 

---
# Theorem). 
Suppose that $f\in C[a,b]$ and the function evaluated at the endpoints is differently signed. The bisection method generates a sequence approximation the sequence where:
$$|P_{n}-P| \leq \frac{b-a}{2^n} \quad \text{ where } n \geq1 $$
The rate of convergence for this function is ggiven by:
$p_{n}=p+O\left( \frac{1}{2^n} \right)$

---
### Conservative Error Bound

It is important to realize that the amount of error we calculate is generally very _conservative_ meaning the actual amount of error (if we were to compute the exact) would be significantly smaller. Take the example for instance. 

![[Pasted image 20260929132510.png]]

---
### Example: Using the Error Bound

Using the same $f$ with accuracy $10^{-3}$, we will use logarithms to find an integer $N$ that satisfies the following:

$$|P_{n}- P| \leq 2^{-N}(b-a) = 2^{-N} < 10^{-3}$$
We can just use the logarithm function to solve for the number of iterations:

$$-N\log_{10}(2) < -3 \implies N > \frac{3}{\log_{10}(2)} \approx 9.96 $$
We would thus need $N=10$ many iteration to achieve $10^{-3}$ levels of accuracy. Again, this amount is generally just a conservative upper bound. 

---
# Tradeoffs

Bisection method has a lot of drawbacks. First, it can be very slow to converge in that $N$ may become quite large before $P-P_{N}$ becomes very small. We also may inadvertently discard intermediate approximations. 

However, the Bisection always converges to a solution, and can provide a good initial approximation for some kind of more efficient procedure. 

The bisection method has guaranteed convergence, but it is fairly slow at $O(n)$.