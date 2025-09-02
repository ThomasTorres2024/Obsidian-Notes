---
title: Simplifying Line Integrals
tags: 
draft: "false"
---
# Introduction 
Some line integrals can be tedious to compute due to the various paths that we need to account for during our calculation. 
# The Fundamental Theorem of Calculus for Line Integrals
The calculation of work is a subset of a larger theorem known as the fundamental theorem of calculus for line integrals.

The gradient of a function is actually a [[Vector Field]] that is known as the [[Gradient Field]], denoted by the  [[Gradient]] of $f$, $\vec{F}=\nabla f$ It is the derivative of a multivariable function. $f(x,y)$ which is known as the [[Potential]], which is like the electric of gravitational potential. 

We can simplify the evaluation of a line integral of the form: 
$$\int_{c} \vec{F}\cdot d\vec{r}$$
The theorem relates the gradient of a function to its potential. It gives the following if and only if $f$ is the potential and $\nabla f$ is the gradient:
$$\int_{c} \nabla f \cdot d\vec{r}=f(p_{1})-f(p_{0})$$
This statement becomes quite obvious when we consider some alternate definitions of the line integral for work:
$$\int_{c}\nabla f \cdot d\vec{r}=\int_{c}f_{x}dx+f_{y}dy=\int_{c}df=f(p_{1})-f(p_{0})$$
A more formal way to prove this can be done by expressing the following as:
$$x=x(t),dx=x'(t)dt$$
$$y=y(t),dy=y'(t)dt$$
$$\int_{c}\nabla f \cdot d\vec{r}=\int_{c}\left(f_{x}\dfrac{dx}{dt}+f_{y}\dfrac{dy}{dt}\right)dt=\int_{t_{0}}^{t_{1}}\dfrac{df}{dt}=f(p_{1})-f(p_{0})$$
This  theorem ONLY works if $\vec{F}$ is the gradient of a function. Some of the consequences of this is that any path that we choose between two endpoints along our gradient results in the same quantity. We call this quality "[[Path Independence]]". 

We can summarize this nicely for curves $c_{1}$ and $c_{2}$ that have the same endpoints as:
$$\int_{c_{1}}\nabla f \cdot d\vec{r}=\int_{c_{2}}\nabla f \cdot d\vec{r}$$
This can be proved by the fundamental theorem, since each integral is evaluated at the endpoints, which is the same for each 

![[Pasted image 20250628051147.png]]
Another consequence is that our Gradient field is a [[Conservative Field]], meaning that our energy would be preserved if we had a closed curve. 
If we make an orbit around some trajectory, we would expect to have a zero. We can formalize this by saying for the closed curve, $c$ it follows that:
$$\int_{c} \vec{F}\cdot d\vec{r}=0$$
Which comes from the fundamental theorem of line integrals, which means that our endpoint and starting point are the same for our integral, which must result in a zero. A cool consequence of this is if we are working with a conservative vector field, like gravity or electricity, we get no change in force, so in turn we get no perpetual motion. 

If a vector field is conservative, then a closed loop on it must be zero, and if it is non-zero then the vector field is not zero. In a conservative energy field no energy can be extracted for free. Energy is conserved. 

Note that we denote closed loop bounds by the following integral:
$$\oint_{c}\vec{F}\cdot d\vec{r}$$
---
# Equivalent Properties for Conservative Vector Fields
1. $\vec{F}$ is conservative
2. $\int_{c} \vec{F} \cdot d\vec{r}$ is path independent
3. $\int_{c}\vec{F}\cdot d\vec{r}=0$ for all closed curves $c$, we can think of this as two curves composing a single curve which in total must be a closed path
4. $\vec{F}$ is a gradient field 
5. $Mdx+Ndy=df$ is an exact differential equation, which is equivalent to being able to express our differential equation as the forms above as the differential 

---
# Proof 
Let us consider a vector field $\vec{F}=\nabla f$, and a smooth curve over the vector field, $\vec{r}(t)$ through points $\vec{r}(a)=A$ and $\vec{r}(b)=B$. We can show that the following holds when $\vec{F}=\nabla f$:
$$\int_{C}\vec{F}\cdot d\vec{r}=f(B)-f(A)$$
Through a chain of equalities we are able to transform our original integral:
$$\int_{C}\vec{F}\cdot d\vec{r}= \int_{C}\vec{F}(\vec{r}(t))\frac{d\vec{r}}{dt}dt=\int_{a}^b \frac{d}{dt}f(\vec{r}(t))dt=f(\vec{r}(b))-f(\vec{r}(b))$$
$$=f(A)-f(B)$$
Which gives our desired result. We can further show that if a vector field is conservative, that $\nabla f = \vec{F}$, and make this a much stronger statement. 
