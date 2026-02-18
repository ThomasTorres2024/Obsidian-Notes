---
title: Taylor Series
tags:
draft: "false"
---
# Taylor Series in Single Variable Calculus
In single variable calculus, we can approximate a function using the [[Taylor Series]] using the first $k$ derivatives of our function and constructing a function of the following form for a given function $f$ which is at least $k$ times differentiable and analytic on $(a,b)$. Another thing to note is that an [[analytic function]] is one which can be represented by a [[Taylor Series]] expansion on some interval as $k\to\infty$, the approximation function will tend towards the actual function. 

Our general definition is of the form:
$$f(x)\approx f_{\text{approx}}= \sum_{n=0}^k \frac{f^n\cdot(x)^n}{n!} \text{ where } f^n \text{ represents the nth derivative of } f.$$
I like to think of this as an extension of the idea that the very essence of calculus is using linear approximations to get good approximations of an otherwise complicated object locally. We can then add on a second degree approximation in the form of quadratic, and so on to the $n$th degree for even better approximations, until having taken $n\to \infty$ many derivatives, we get $f$ if our error term:
$$ \lim_{n \to \infty }f-f_{approx}=0 \implies \lim_{k \to \infty} \sum_{n=0}^k \frac{f^n\cdot(x)^n}{n!}=f$$
Another thing to note, the Taylor series expansion of a function is unique. Any way that we may obtain the Taylor series results in the same expression. Due to this fact, we can add, multiply, differentiate, or integrate them as we please. 

---
# Multivariable Taylor Series 
The notion of approximating functions using increasingly higher terms is true here. We use a [[tangent plane]] for a first degree [[Taylor Series]]. Another particularly relevant approximation is one using a [[Quadratic Form]], which is a second order approximation and again the highest term is second degree. 

If we look at the case of a two dimensional function, $f(x,y) : C \subseteq \mathbb{R}^2 \to \mathbb{R}$,  we must take account of the fact we have a multivariable function, and can write it as such around the point $(a,b)$:
$$f(x,y)\approx f_{1}= f(a,b)+f_{x}(a,b)(x-a)+f_{y}(a,b)(y-b)$$
Which is the first order taylor series and linear approximation of $f$. We can take the second degree term by using the formula:
$$f(x,y)\approx f_{1}+\frac{f_{xx}(a,b)(x-a)^2}{2!}+\frac{f_{yy}(a,b)(y-b)^2}{2!}+f_{xy}(a,b)(x-a)(y-b)$$
Which has clear analogues to the single variable case. There are more general ways to express these functions for functions of the type $g : U\subseteq \mathbb{R}^n \to \mathbb{R}^m$.  They are in the course notes, I don't feel like retyping them atm. 

#### Computing Multivariable Taylor Series
We can use some tricks like [[polar coordinates]], addition and subtraction of other taylor series since they are uniquely defined, and as well the [[Geometric Series]] since the following is true for $-1 < x < 1$:
$$\frac{1}{1-x}=\sum_{k=0}^\infty x^{k}=1+x+x^2+x^3+\cdots$$
# Using Vector Notation and [[Matrix Derivative]]s 
We can further generalize the idea for functions of the form $f : \mathbb{R}^n \to \mathbb{R}$. Then, we can define the [[Taylor Series]] of first and second order with the following for $\vec{A} \in \mathbb{R}^n$:
$$T_{1}(\vec{x},A)=f(\vec{x},\vec{A})+[\nabla f(\vec{A})]^T (\vec{x}-\vec{A})$$
$$T_{2}(\vec{x},A)=f(\vec{x},\vec{A})+[\nabla f(\vec{A})]^T (\vec{x}-\vec{A}) + \frac{1}{2}(\vec{x}-\vec{A})^T \mathcal{H}_{A} (\vec{x}-\vec{A})$$
Where $\mathcal{H}_{A}$ denotes the [[Hessian Matrix]] of $f$. Notice that here we include the [[Quadratic Form]] of the [[Hessian Matrix]] and the [[Vector Derivative]]. 

