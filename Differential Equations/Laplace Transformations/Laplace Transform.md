---
title: Laplace Transform
draft: "false"
tags:
---
# Intuition
The end goal of the [[Laplace Transform]]s is being able to express a function as an equivalent sum of exponential functions given some $s_{i} \in \mathbb{C}$, where we have some $f(t) : \mathbb{R} \to \mathbb{R}$. We should be able to express:
$$f(t)=\sum_{i=1}^{k}c_{i}e^{s_{i}t}: c_{i}\in \mathbb{C}$$
For the sake of Differential Equations we are hoping to express a differential equation as an algebraic equation, and solve the algebraic equation, and then apply an [[Inverse Laplace Transform]] such that the differential equation is solved in the end:
![[Pasted image 20251221220112.png]]

For instance consider the function $\cos(t)$ which is clearly defined over the reals. We know that through [[Euler's Identity]] that $\cos(t)$ can be expressed using complex exponentials:
$$\cos(t)=\frac{1}{2}(e^{it}+e^{-it})$$

The Laplace transform itself defines some function $F(s)$ corresponding to $f(t)$ such that: $s \mapsto F(s)$. We use the term "[[Transform]]" as a mapping which  constructs a new function $F(s)$ with respect to $s$ for each value of $s$ chosen. If we were to visualize the output, there would be a [[pole]] corresponding to each $s_{i}$ somehow. 

We describe the [[Laplace Transform]] as the following:
$$F(s)=\int_{0}^\infty f(t)e^{-st}dt$$

Our goal is to be able to find these poles and find each $s_{i}$ such that we can express an equivalent version of $f(t)$ with respect the the $s$ space. The integral of this function should be able to detect which points along $S$ cause the function to jump significantly. Here is an example of some function in the $S$ plane using its poles:
![[Pasted image 20251221215016.png]]

---
# Complex Integration
To begin it's important to address the difficulties and changes of integrating in a complex setting compared to a real one. Instead of considering the more general integral given by
$$F(s)=\int_{0}^\infty f(t)e^{-st}dt$$
We instead consider the much simpler integral given by:
$$\int_{0}^\infty e^{-st}dt$$
Our intuition for this operation over the reals is simply the area underneath the curve. If we let $s=1$, then our area is 1. If $s$ large, then the area continues to decrease and heads to $\frac{1}{s}$ overall. But if $s \to 0$ then the area quickly tends towards infinity. We can try to generalize the notion of the integral to the complex plane 

Another way we can consider integration is by examining integration over a unit interval. We can think of it as a center of mass over the unit, and thus the average area over that length since we are only considering an area of 1, we only need to divide the integral by 1. We can then consider the total integral define from $0$ to $\infty$ as being the sum of the average unit areas. This notion of integration can be extended to the complex much easier than the other operation of area under a curve.

We can shift this idea over to the complex numbers now. Consider each unit interval along the integral, and then the average  of these values. We obtain a vector from each resulting unit length integral, and then then the sum of these vectors should ideally converge to some stable position, which constitutes another interpretation for complex integration within the context of the [[Laplace Transform]]. 

![[Pasted image 20251221231214.png]]

We can then consider the final position of the resulting vector $v=\langle x,y \rangle$, and then plot the magnitude of this vector in the $S$ plane, giving us $\|v\|$ for some $s=a+bi$. For the pet example considered in the video of the function $e^{-st}$, we have that  We will notice along the complex plane that there is a massive for $s=0$ since the integral completely diverges here:
$$\int_{0}^{\infty}e^{-0\cdot t}dt=\int_{0}^\infty dt \implies  \therefore  \text{integral diverges}$$We also have a direction described implicitly by $v$, so it follows that we can describe the angle using color.
![[Pasted image 20251221232059.png]]

It turns out also that if there is no real component for $s$, then the 

### Resolving Domain Issues 
If we consider the portion of the domain where $Re(s) < 0$ it follows that the Laplace transform without [[Analytic Continuation]] will necessarily diverge for all $Re(s)<0$. We will be able to resolve this using this technique. 

Notice that the integral $$\int_{0}^\infty e^{-st}dt=\frac{1}{s}$$
