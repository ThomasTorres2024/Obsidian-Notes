---
title: Fixed Point Iteration
tags:
  - Numerical_Analysis
draft: "False"
---
# Prime Objective 
Given a function $f(x)$ where $a\leq x \leq b$ we need to find values $p$ such that $f(p)=0$ (roots). 

Given some function $f(x)$, we can construct an auxiliary function $g(x)$ such that $p=g(p)$ whenever $f(p)=0$ (note that this construction is not unique).

The problem of finding $p$ such that $p=g(p)$ is known as the __fixed point problem__. 

---
# Fixed-Point Algorithm

To find a [[Fixed Point]] of $g$ in an interval $[a,b]$ given the equation $x=g(x)$ with an initial guess $p_{0} \in [a,b]$, we perform the following Algorithm:

1. $n=1$
2. $p_{n}=g(p_{n-1})$
3. If $|p_{n} - p_{n}-1| < \epsilon$, then go to $5$ 
4. $n\to n+1$; go to $2$ 
5. End of procedure. 

---
# Example Problem

Consider $x^2-x-1=0$ with $x= \frac{1+\sqrt{ 5 }}{2} \approx 1.618034$. We can convert the finding zeroes aspect of this problem to finding a fixed point. 

Let us try to get some $g(x)$ in the following:

$$\begin{align}
x^2-x-1=0 \\
\implies x^2 = x+1 \\
\implies x = \pm \sqrt{ x+1 }
\end{align}$$
So, we let $g(x)=\sqrt{ x+1 }$. After we run some iterations, we obtain the following (look under ```src``` for an implemention in Python). Here is the result after $20$ iterations:

```
0). 1.0
1). 1.4142135623730951
2). 1.5537739740300374
3). 1.5980531824786175
4). 1.6118477541252516
5). 1.616121206508117
6). 1.6174427985273905
7). 1.617851290609675
8). 1.6179775309347393
9). 1.6180165422314876
10). 1.6180285974702324
11). 1.618032322752
12). 1.6180334739281508
13). 1.618033829661219
14). 1.6180339395887897
15). 1.6180339735582778
16). 1.618033984055427
17). 1.6180339872992244
18). 1.618033988301613
19). 1.6180339886113682
```

Here is a visualization of the convergence of the function:

![[Pasted image 20261002125646.png]]

---
# Rate of Convergence
We require that $|g'(x)|\leq k <1$. Since:

$$g(x) = \sqrt{ x+1 } \quad g'(x) = \frac{1}{2\sqrt{ x+1 }} > 0 \quad \text{ for } x \geq0$$

Furthermore we have that $g'(x) = |\frac{1}{2\sqrt{ x+1 }}| < 1 : \forall x> -\frac{3}{4}$.  

Another way in which we can transpose $f(x)$ is in the following:

$$\begin{align}
x^2-x-1=0 \\
\implies x^2=x+1 \\
\implies x= 1+ \frac{1}{x}
\end{align}$$
And thus we get a second function we can use, $1+\frac{1}{x}$:
The corresponding output produced by this choice of function is:
```
0). 2.0
1). 1.5
2). 1.6666666666666665
3). 1.6
4). 1.625
5). 1.6153846153846154
6). 1.619047619047619
7). 1.6176470588235294
8). 1.6181818181818182
9). 1.6179775280898876
10). 1.6180555555555556
11). 1.6180257510729614
12). 1.6180371352785146
13). 1.6180327868852458
14). 1.618034447821682
15). 1.618033813400125
16). 1.6180340557275543
17). 1.6180339631667064
18). 1.6180339985218035
19). 1.618033985017358
```

![[Pasted image 20261002133431.png]]

We also observe that $g(x)$ satisfies the uniqueness criteria for a [[Fixed Point]], since:

$$g(x)=\frac{1}{x}+1 \implies g'(x)= -\frac{1}{x^2}<0 \quad \forall x$$
---
# Example). 

Consider the cubic function, $x^3+4x2-10=0$. It has a unique root of $x \approx 1.365230013$ along the interval.  

$$\begin{align}
x^3+4x^2-10=0 \\
\implies x^2 = \frac{1}{4}(10-x^3) \\
\implies \pm \frac{1}{2} (10-x^3)^{1/2}
\end{align}$$

(Interestingly the choice $x=\frac{10}{x^2}-4$) did NOT converge to $x\approx 1.365\dots$

There are $5$ possible transpositions to $x=g(x)$:

 
 1. $g_{1}(x)=x-x^3-4x^2+10$
 2. $g_{2}(x)= \sqrt{ \frac{10}{x}-4x }$
 3. $g_{3}(x)=\frac{1}{2}\sqrt{ 10-x^3 }$
 4. $g_{4}(x)= \sqrt{ \frac{10}{4+x} }$
 5. $g_{5}(x)=x-\frac{x^3+4x^2-10}{3x^2+8x}$

Here are their results:
![[Pasted image 20261002140707.png]]

We obtain that $g_{1}$ and $g_{2}$ fail to converge to their target value. $g_{3}$ converges, but slowly after $31$ iterations, $g_{4}$ converges after $12$ and $g_{5}$ after $5$. 

---
# Convergence of [[Fixed Point Iteration]] 

How can we find a fixed point problem that produces a sequence that reliably and rapidly converges to a solution given some root finding problem? 

We can use the following theorem to reject some functions, and furthermore some paths which we should pursue. 

### Convergence Result 

Let $g \in C[a,b]$ with $g(x) \in [a,b] : \forall x \in [a,b]$. Let $g'(x)$ exist on $(a,b)$ with:

$$|g'(x)|\leq k < 1 \quad \forall x \in [a,b]$$

If $p_{0}$ is any point in $[a,b]$ then the sequence defined by:
$$p_{n}=g(p_{n-1}) \quad n \geq1$$
Will converge to the unique fixed point $p$ in $[a,b]$. 

### Corollary to the Convergence Result
If $g$ satisfies the hypothesis of the theorem, then:

$$|p_{n}-p| < \frac{k^n}{1-k}|p_{1}-p_{0}|$$

---
### Example:

Consider $g(x)=3^{-x}$ on $\left[ \frac{1}{3},1 \right]$ starting with $p_{0}=\frac{1}{3}$. Determine a lower bound for the number of iterations $n$ required so that $|p_{n}-p|<10^{-5}$. 

We can just solve for the parameters of the problem. We can get these from $p_{1}=g(p_{0})=3^{-1/3}=0.6933612\dots$ and since $g'(x)=-3^{-x}\ln(3)$ we obtain the following bound:  

$$|g'(x)|\leq 3^{-1/3}\ln(3) \leq 0.7616362 \approx 0.762 = k$$

The rest quickly follows:

$$\begin{align}
|p_{n}-p| \leq \frac{k^n}{1-k}|p_{0}-p_{1}|  \\
\leq \frac{0.762^n}{1-0.762} \left| \frac{1}{3}-0.6933612 \right| \\
\leq 1.513 \times 0.762^n
\end{align}$$
And we require that:
$$1.513 \times 0.762^n < 10^{-5} \implies n > 43.88$$

---
# Footnote on Estimate Obtained 

Note that the estimate for the number of iterations is an upper bound. The number of true iterations needed is typically far less than the calculated amount. 

---
# Example 2

Return to example's equation and deal with an alternative form of $g(x)$ from $x^3+4x^2-10=0$ on the interval $[1,2]$ with $x \approx 1.365\dots$

Consider the representtion given by:
$$x=g_{1}(x)=x-x^3-4x^2+10$$
When we take $g'_{1}(x)$ it becomes apparent why this fails:

$$\begin{array}  \\
g_{1}'(x)=1-3x^2-8x & g_{1}'(1)=-10 & g'_{1}(2)=-27
\end{array}$$
Notice that there is no interval $[a,b]$ containing $p$ where also $|g'_{1}(x)|<1$. 

Also note that $g_{1}(1)=6$ and $g_{2}(2)=-12$ so $g(x) \not \in [1,2]$ for $x \in [1,2]$. 

Correspondingly, iterations explode rapidly:

![[Pasted image 20261002144446.png]]

Secondly we can also look at $x=g_{2}(x)$ where $g_{2}=\sqrt{ \frac{10}{x}-4x }$. This function fails for multiple reasons, for one $g'(1) \approx -2.86$ and $g'(p)=-3.43$, $g'(x)$ is not defined for $x>1.58$. 

It is important to note that iteration is not __well defined__ for $g_{2}$ since we run into a complex number quite early:

![[Pasted image 20261002145434.png]]

When we examine $g_{3}$ we see that we converge at an extremely slow rate:

$$g'_{3}(x) = -\frac{3x^2}{4 \sqrt{ 10 -x^3 }}<0 \quad \text{ for } x \in [1,2]$$
This entails that $g$ is strictly decreasing on $[1,2]$. But, $|g_{3}'(x)|>1$ for $x>1.71$ and $|g_{3}'(2)| \approx -2.12$. 