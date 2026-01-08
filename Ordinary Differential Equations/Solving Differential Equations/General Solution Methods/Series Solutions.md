---
title: Solving Differential Equations with Power Series
tags:
draft: "false"
---
# Solving [[Ordinary Differential Equation]] with Series

We begin with the definition of a power series, which has the definition 
$$\sum_{i=0}^n a_{i}x^i =a_{0} + a_{1}(x-x_{0}) + a_{2}(x-x_{0}^2) + ... a_{n}(x-x_{0})^n$$

We can represent this more succinctly as a sum, also all values of $a_{n}$ are constants, and $x_{0}$ is a constant as well.

$$ \sum_{n=0}^{\infty} a_{n}(x-x_{0})^n$$

For any given power series,  we have various ways of determining if the series [[Converges (Series)]] or [[Diverges (Series)]]. 

We can begin to talk about the interval of convergence, which means the point, $x_{0}$ + r and $x_{0}$ -r, where for ($x_{0}-r,x_{0}+r$) represents the interval upon which the sum is defined and has a value. 

We can derive the radius of convergence from the [[Ratio Test]]. 

The ratio test states the following:
$$\lim_{n\to\infty} \left|\frac{a_{n+1}}{a_{n}} \right|= L$$

Based on the value L, we can conclude the following about the series:
$L < 1$ means that series converge, $L = 1$ is inconclusive, and $L>1$ means the series diverges.



# Applying Series to Differential Equations

### [[Taylor Series]]
Taylor series are given by the formula:
$$f(x) = f(x_{0}) + f(x_{0})'(x-x_{0}) + \frac{f(x_{0})''(x-_x{0})^2}{2!}+ ... + \frac{f(x_{0})''(x-_x{0})^n}{n!}$$

We can take a derivative of a power series by taking a derivative term by term of the function, and it will behave and converge within its respective radiance of convergence as a normal combination of functions would. The same notion applies to differentiation. 

We can allow y to be equal to a series representation of a function, for instance allow x to be equal to the general power series equation, and then take a derivative of it, yielding:

$$y =a_{0} + a_{1}(x-x_{0}) + a_{2}(x-x_{0})^2 + ... a_{n}(x-x_{0})^n$$
$$y' =0+ a_{1} + 2a_{2}(x-x_{0}) + ... na_{n}(x-x_{0})^n-1$$
$$y'' = 2a_{2} + 2\cdot3a_{3}(x-x_{0}) + 3\cdot 4a_{2}(x-x_{0})^2 + ... (n)(n-1)a_{n}(x-x_{0})^n$$

From this, we plug these terms into a differential equation, collect like terms and then solve for coefficients. 

We can derive some information just from the definition of a power series, such as $y(x_{0})$ which causes many cancellations in the numerator, equal to $a_{0}$. Similarly, $y(x_{0})'=a_{1}$.

When solving these sum formulas, finding the first couple of sums is often adequate since the first few powers tend to dominate and provide  a good local approximation.

# Power Series Solution to Differential Equations}

For some differential equations where the series it not centered at zero, then we must apply the general formula:
$$y=a_{0}+a_{1}(x-x_{0})+a_{2}(x-x_{0})^2 + a_{3}(x-x_{3]})...$$

We must re-write the center of the original differential equation, if there is an x term where we offset the x to be in the following example:
$$y'' -xy = 0$$
$$y'' -(x+2)y + 2y = 0$$