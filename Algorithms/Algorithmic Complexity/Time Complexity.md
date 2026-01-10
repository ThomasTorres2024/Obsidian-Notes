---
title: Time Complexity
draft: "false"
tags:
---
# Time Complexity Overview
We are interested in applying mathematical tools to determine the rune time of algorithms because of many of the faults and costs of empirical analysis. 

Some introductory terms that are important here are algorithmic complexity, run time, computational cost, and the function $T(n)$, which expresses the number of operations in an an algorithm. This allows us to mathematically compare the run time of algorithms. This type of analysis is independent of all hardware and software. We are simply counting operations performed. 

---
# Big O Notation 

We can express T(n) to be a function which counts the number of steps. What we are interested in doing is to focus on the number of operations crucial to the problem that we are solving.  When expressing time complexity functions, we tend to ignore constant factors and lower order terms. For instance, we would not express some function T(n) = $5n^3 + 2n2 + 100$ this was, as n approaches infinity, we can write the expression as T(n) = $n^3$. This better characterizes the runtime of the algorithm. This is principally because $n^3$ is orders of magnitudes larger than the other parts of the function and is the reason it gets so much larger. 


The goal of big $O$ notation is to find functions which after some value $x_0$, have the property that for $f(x)$, $T(x)<f(x)$, which is to say that $T(x)$ is bounded above by this function.  Similarly, we can find a lower bound for our algorithm if after $x_0$, it is the case that $T(x) < h(x)$. If a function satisfies that after $x_0$ that $T(x) < f(x) \implies$ that our algorithm is of $O(f(x))$. if a function satisfies that after $x_0,$ that $T(x) > h(x) \implies$ the algorithm is of $\Omega(h(x))$. Furthermore, if we can find some functions after $x_0$ where the following condition is always true:
$$f(x) \leq T(x) \leq \delta f(x), \delta \in \mathbb{R} \implies \text{Our algorithm is of: } \theta(f(x))$$
Which is to say that our algorithm is just nestled between a function and some constant multiple of it. 

When considering run time of algorithms, the number of nested loops is not necessarily equal to the complexity function, we consider the total number of operations that occur.

For single loops computing the number of ops is generally iterations times operations. We must be careful to recognize ranges and loop sizes.

 For algorithmic analysis, runtime is not constant, but depends upon the input of the algorithm. We have a best case, worst case, and an average case though the average is very hard to find. Generally what we are interested in is the worst case scenario runtime. This is known as case analysis. 

We are not interested in constants, coefficients, or lower order terms when doing asymptotic analysis. Say if our algorithm is $3n^3+50n+24$, we can use the big theta function which removes constant and lower order terms giving us: $\theta$($n^3$). Say for $0.0001n^2 + 10^{10}n + 10^5$ = $\theta$($n^2$). $n^5 + 2^n -1$ = $\theta$($2^n$). 

