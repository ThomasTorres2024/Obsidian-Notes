---
title: Interpolation
tags:
  - Numerical_Analysis
draft: "False"
---
# Interpolation 

---
# Weirstrass Approximation Theorem
Suppose that $f$ is defined and continuous on $[a,b]$ for $\epsilon>0$, then $\exists$ [[Polynomial]] $P(x)$ with the property that:

$$|f(x) -P(x)| < \epsilon \quad x  \in [a,b]$$

With this we can get very good approximations of very complicated functions as [[Polynomial]]s.

### Benefits:
* [[derivative]]s are easy
* [[integrals]] are also easy

---
# Interpolating with [[Taylor Series]]

* Agree entirely with a function __only at a specific point__. But accuracy is just concentrated around a single point. 
* A good interpolation polynomial needs to provide a relatively accurate approximation over __an entire interval__, and Taylor Series generally do not do this.
* As the degree $n$ of a [[Taylor Series]] increases, our general accuracy tends to increase
* Example, $e^x$ works excellently but this cannot be used as a general example. 

If we consider $f(x)=\frac{1}{x},f'(x)=-x^{-2},f''(x)=2x^{-3}$ and generally $f^{(k)}(x)=(-1)^kk!x^{x-k-1}$

Which can be used to express a Taylor polynomial:
$$P_{n}(x)= \sum_{k=0}^n \frac{f^{(k)}(1)}{k!}(x-1)^k= \sum_{k=0}^n (-1)^k (x-1)^k$$
If we wanted to approximate $f(3)=\frac{1}{3}$ by $P_{n}(x)$ for increasing values of $n$ we obtain failing values as $n\to \infty$ 

$$
\begin{matrix}
n & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
P_n(3) & 1 & -1 & 3 & -5 & 11 & -21 & 43 & -85
\end{matrix}
$$

(Generall in NA, we use [[Taylor Series]] for methods, but for general practical approximation, we do not use it. It is __only good near the expansion point__). 

---
# Interpolation

Instead we use __Interpolation__, or namely "[[Lagrange Polynomial]]"s. 

Given the following points $x_0,x_1$ we can write the following approximation:
$$L_{0}(x)= \frac{x-x_{1}}{x_{0}-x_{1}} \quad L_{1}(x)= \frac{x-x_{0}}{x_{1}-x_{0}}$$

$$P(x) = L_{0}(x)f(x_{0})+L_{1}(x)f(x_{1}) = \frac{x-x_{1}}{x_{0}-x_{1}}f(x_{0}) + \frac{x-x_{0}}{x_{1}-x_{0}}f(x_{1})$$

This is the [[Lagrange Polynomial]] in the __linear case__. Furthermore, notice that:

$$\begin{cases}
L_{0}(x_{0}) = 1f(x_{0}) = f(x_{0}) \\
L_{0}(x_{1}) = \frac{0}{x_{0}-x_{1}}f(x_{0}) = 0 \\
\\ 
 L_{1}(x_{0}) = 0 \\
L_{1}(x_{1}) = 1 
\end{cases}$$
This entails that: 
$$\begin{align}
P(x_{0})=1 \cdot f(x_{0}) + 0 \cdot f(x_{1}) = f(x_{0}) = y_{0} \\
P(x_{1})= 0 \cdot f(x_{0})+1\cdot f(x_{1}) = f(x_{1})= y_{1}
\end{align}$$

$P$ is thus a polynomial of degree at most $1$ which passes through $(x_{0},y_{0})$ and $(x_{1},y_{1})$. 

---
# Example).
Determine the linear lagrange interpolating polynomial that passes through $(2,4)$ and $(5,1)$. Let $x_{1}=2,x_{0}=5$
$$\begin{align}
L_{0}(x_{0})= \frac{x-x_{1}}{x_{0}-x_{1}} = \frac{x-2}{5-2} = \frac{x-2}{3}  \\
L_{0}(x_{1})= \frac{x-x_{0}}{x_{1}-x_{0}} = \frac{x-5}{-3} \\
 \\

\end{align}$$
And we can thus obtain $P(x)$ for a linear approximation:

$$P(x)  = L_{0}(x)f(x_{0}) + L_{1}(x)f(x_{1}) = \frac{x-2}{3}(1) + \frac{x-5}{-3}(4)  $$
![[Pasted image 20261013143238.png]]

---
# Degree $n$ construction

To generalize the concept of linear interpolation, we can consider the construction of an $n$th degree polynomial through $n+1$ points:

$$(x_{0,f(x_{0})}  ),\dots,(x_{n+1},f(x_{n+1}))$$
For each $k=0,1,\dots,n$
 we construct a function s.t. $L_{n,k}(x_{i})=0$ for each $i \neq k$ and $L_{n,k}(x_{k})=1$. 

So, the numerator is thus:
$$\begin{align}
(x-x_{0})(x-x_{1})\dots(x-x_{k-1})(x-x_{k+1})\dots(x-x_{n})
\end{align}$$
And likewise the denominator is the same as the numerator but we replace $x$ with $x_{k}$ for each value, which get us the condition $L_{n,k}(x_{k})=1$.

Thus we obtain the following:
$$L_{n,k}(x) = \frac{(x-x_{0}) \dots(x-x_{k-1})(x-x_{k+1})\dots(x-x_{n}) }{(x_{k}-x_{0})\dots(x_{k}-x_{k-1})(x_{k}-x_{k+1}\dots(x_{k}-x_{n})} $$

![[Pasted image 20261013161730.png]]

We can then define our polynomial as:
$$\begin{align}
P(x) = f(x_{0})L_{n,0}(x)+ \dots + f(x_{n})L_{n,n}(x) \\
= \sum_{k=0}^n f(x_{k})L_{{n,k}}(x)
\end{align}$$
Where $L_{n,k}$ is:
$$\begin{align}
L_{n,k}(x) = \frac{(x-x_{0})(x-x_{1})\dots(x-x_{k-1})(x-x_{k+1})\dots(x-x_{n})}{(x_{k}-x_{0})(x_{k}-x_{1})\dots(x_{k}-x_{k-1})(x_{k}-x_{k+1})\dots(x_{k}-x_{n})} \\
= \prod_{i=0,i\neq k}^n \frac{x-x_{i}}{(x_{k}-x_{i})}
\end{align}$$
We can abbreviate this to $L_{k}(x)$ if there is no confusion about the degree of the polynomial, $n$. 

---
# Example ). 2nd Degree [[Lagrange Polynomial]] 

Let $f(x) = \frac{1}{x}$. Use $x_{0}=2,x_{1}=2.75,x_{2}=4$ to determine the second lagrange polynomial interpolating for $f(x)=\frac{1}{x}$. 

Use the polynomial to approximate $f(3)=\frac{1}{3}$. 
 

