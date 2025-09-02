---
title: Second Derivative Test
tags: 
draft: "false"
---
# Second Derivative Test 
How do we know if a critical point is a maximum or a minimum? If we have multiple points, we would typically have to compute the value of the function at the critical points, and can determine which is which. 

Let us consider the function $w : \mathbb{R^2} \rightarrow \mathbb{R}$

$$w(x,y)=ax^2+bxy+cy^2$$
In order to find the minimum point of this function, we can complete the square. If $a \neq 0$ then we can perform the following factorization: 
$$w=a \left(x^2+\frac{b}{a}xy+ \right)+c^2$$
$$=a \left( x + \dfrac{b}{2a}y \right)^2 + \left( c- \dfrac{b^2}{4a} \right)y^2$$
$$=\dfrac{1}{4a} \left[4a^2 \left( x + \dfrac{b}{2a}y \right)^2 + \left( 4ac- b^2 \right)y^2 \right]$$
We have expressed our function as the sum of two squares. Regardless of the values of $a,b,c$ the term $4a^2(x+\frac{b}{2a}y)^2$ will always be positive.  On the other hand the term $(4ac-b^2)y^2$ will vary in positivity or negativity due to to the values chosen for $a,b,c. y^2$ will always be positive, so instead we focus on the sign given by $4ac-b^2$. 

We can go through what happens to the signs of our $4ac-b^2$ term:

1. $4ac-b^2 < 0$ results in a difference of squares, which tantamount to the form $d\cdot(ex^2-fy^2)$ which is the equation of a hyperbola, which has a saddle point.

![[Pasted image 20250622025841.png]]

2. $4ac-b^2 = 0$ results in a degenerate graph where we end up ignoring one direction, and have a parabola opening in the positive $z$ direction and a set of critical points along a line 

![[Pasted image 20250622025753.png]]

3. $4ac-b^2 > 0$ results in a parabola and from here we have two different subcases.  The inside contents result in the sum of two squares, and will only be positive numbers. The thing that determines if we have a positive or a minimum is if our value of $a > 0$ or $a < 0$ since this flips the sign of our parabola.

	- if $a >0$ then our parabola opens upward in the positive $z$ direction, so our critical point is a [[local minima]]  
	- if $a<0$ then our parabola opens downward in the positive z direction, so our critical point is a [[local maxima]] 

---
# Elaboration on Discriminant for finding Minima and Maxima 

Reconsider our function $w=ax^2+bxy+cy^2$. We can rewrite it as the following:

$$w=ax^2+bxy+cy^2=y^2\left[ a\left(\dfrac{x}{y} \right)^2 + b\left(\dfrac{x}{y} \right) +c \right]$$
The $y^2$ term is always positive. We can use the quadratic formula to analyze the sign of the product by considering what values the quadratic expression evaluates to. We can think of it in terms of the quadratic formula, and then express then analyze when our parabola is constrained to open upward. 

Recall the discriminant of the quadratic equation:
$${b^2-4ac}$$
If the quadratic equation has any roots that are not zero, this means that the quadratic passes through the origin, which means its value is not strictly positive, and not strictly negative, meaning it is [[indefinite]]. 

This occurs when the roots are real, meaning that our discriminant is positive:
$$b^2-4ac>0$$

When the parabola has no non-zero roots, it follows that our parabola is centered at $(0,0)$, is above the origin strictly, or below the origin strictly. This implies that our parabola is negative or [[positive definite]]. This excludes the possibility of a saddle point. 

This occurs when the roots are complex, meaning that our [[discriminant]] is negative.
$$b^2-4ac<0$$
With all of this being said, we have a way to decide if a critical point of a quadratic function of the form $w=ax^2+bxy+cy^2$ is a saddle point, minima, or maxima. 

---
# General Case for Second Optimizing with Second Derivatives

In the general case of a function $f : \mathbb{R}^2 \rightarrow \mathbb{R}$, we will examine the second derivatives of $f$, and then examine our critical points. 

We will denote our second derivatives like this:
$$\dfrac{\partial^2f}{\partial x^2}=f_{xx}$$
$$\dfrac{\partial^2f}{\partial y^2}=f_{yy}$$
$$\dfrac{\partial^2f}{\partial x \partial y}=\dfrac{\partial^2f}{\partial y \partial x}=f_{xy}=f_{yx}$$
As an aside, we know via Clairaut's Theorem that for any continuous function, $f$, defined on a disk, $D$ which contains point $(a,b)$, then $f_{xy}$ and $f_{yx}$ are both continuous functions which are equal:
$$f_{xy}(a,b)=f_{yx}(a,b)$$
### The Second Derivative Test 
Given a critical point $(x_{0},y_{0})$ of $f$, let: $A=f_{xx}(x_{0},y_{0}),B=f_{x,y}(x_{0},y_{0}),B=f_{y}(x_{0},y_{0})$. 
- If $AC-B^2 > 0$ and $A < 0$ then $A$ is a $\textbf{local maximum}$
- If $AC-B^2 > 0$ and $A > 0$ then $A$ is a $\textbf{local minimum}$
- If $AC-B^2 < 0$ then our point is a saddle point
- If $AC-B^2 = 0$ then our point is conclusive

It turns out that this is equivalent to our original method for the quadratic case. Let us reconsider $w=ax^2+bxy+cy^2$ and compute its second partial derivatives:

$$w_{xx}=2a,A=2a$$
$$w_{xy}=b,B=b$$
$$w_{yy}=2c,C=2c$$
Let us compute $AC-B^2$
$$AC-B^2=4ac-b^2$$

It turns out that this is secretly the discriminant of the quadratic equation in disguise. Instead of writing $b^2-4ac$ we consider when it is negative. The condition where a quadratic equation has no roots is when $-AC+B^2<0$ which we flip by multiplying it by $-1$ which would give us our $AC-B^2>0$ rule. 

It turns out that we don't need to write out $4ac-b^2$ to fully do this and that we have arrived at our original expression again. Why is it that this idea extends beyond the quadratic? The reason is that we can approximate a quadratic function using a Taylor series. 

Let us consider the Taylor series consisting of first derivatives of our function:
$$\Delta f \approx f_{x}(x_{0})(x-x_{0})+f_{y}(y_{0})(y-y_{0}) = 0$$
This approximation is quite poor since we know that our first derivatives evaluate to zero at each of the points given above. We need to use more derivatives for a better approximation. Let us consider the Taylor approximation with second derivatives:
$$\Delta f \approx \frac{1}{2} f_{xx}(x-x_{0})^2+f_{xy}(x-y_{0})(y-y_{0})+f_{yy}(y-y_{0})^2 $$
$$=a(x-x_{0})^2+b(x-x_{0})(y-y_{0})+c(y-y_{0})^2$$
Our general case reduces to the quadratic case for approximating the minima. 

This is only a good approximation if our third degree derivatives and higher reduce to zero. Our approximation is a good one because the structure of the graph is highly determined by the quadratic terms, especially within the neighborhood of the critical point. 

In the degenerate case, what happens depends upon higher order derivatives of our Taylor approximation. This gives us the "inconclusive" case. If our discriminant is zero, then we are extremely unlucky. 

--- 
# Notes on the Hessian Matrix
We can express our test more succinctly using a symmetric matrix of partial derivatives, which is better known as the [[Hessian Matrix]], denoted by $\mathcal{H}$ for the case in $\mathbb{R}^2$ for the function $f : \mathbb{R}^2 \rightarrow \mathbb{R}$:

$$\mathcal{H}=\begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy}  \end{bmatrix}$$
Note that computing the trace and determinant of our matrix gives us the [[Laplacian]] and the [[Second Derivative Test]]. 

To determine if our matrix has a maxima/minima, a saddle point, or nothing we begin by considering $\text{det}(\mathcal{H})$.
$$\text{det}(\mathcal{H})=f_{xx}f_{yy}-f_{xy}^2$$
Notice that this gives us $AC-b^2$ which is what we previously used above, and fully captures the computation:

* $\text{det}(\mathcal{H})>0$ entails that we have a maxima or a minima, we need more info to categorize 
	- $\text{tr}(\mathcal{H})>0$ entails that we have a local minima since both eigen values are positive
	- $\text{tr}(\mathcal{H})<0$ entails that we have a local maxima since both eigen values are negative 
* $\text{det}(\mathcal{H}) < 0$ entails that we have a saddle point due to mixed signs 
* $\text{det}(\mathcal{H}) = 0$ entails that we need further information 

