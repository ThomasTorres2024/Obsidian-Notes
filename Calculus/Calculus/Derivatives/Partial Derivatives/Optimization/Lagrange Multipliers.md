---
title: Lagrange Multipliers
tags: 
draft: "false"
---
# Lagrange Multiplier Introduction
When we want to minimize a function of several variables, $f$, we have so far looked at [[local minima]] and [[local maxima]] where there are no constraints on our region of optimization and where the variables $x,y,$ and $z$ are not independent. 

In the general case, we can allow our $f(x,y,z)=c$, which imposes a constraint on our variable. If the equation turns out to be nice, we will be able to solve for $c$. However, it is not the case that this function will always be nice and simple to solve. 

It is also the case that most [[critical point]]s tend to not satisfy the constraint of being equal to c.

Lagrange multipliers allow us to constrain the region we are searching over to find optimal solutions. 

# Key Intuition of Lagrange Multipliers
We can examine the Lagrange multiplier as a extension of the single variable case for constrained optimization. When working with a curve in single variable calculus, we would normally check for critical points and the endpoints of an interval, and evaluate all points to ensure that they were within our constraints or satisfied what we were searching for. 

In the multivariable case, we also need to check around the boundary of our function to check for  a local minima or local maxima, compared to the single variable case where we only check for the endpoints. 

My personal intuition on the matter is that we have two types of points that may satisfy optimization around a region. One is a critical point, which represents the maximum accumulation of change that a function has, and another is a point that lies on the boundary, which may give the most amount of change that occurred for a function. 

Let us constrain ourselves to the single variable case to make visualizing this easier so we can then justify the multivariable case:
![[Pasted image 20250626031131.png]]

Our function may come to a peak or a divot at a critical point, or it may continue to grow beyond that along an interval. If we think of a function like $x^2-3$, I think it's easier to see this. The critical point is not enough, it can still grow in directions without any bounds. We need to be able to check the edges where this may occur.

I believe that the analog of this is essentially the same in higher dimensions, its just that we have to apply the same idea to every plane that we can form by slicing through our region, which involves us using the Lagrange Multiplier to consider the entire set of such points. 

![[Pasted image 20250626031442.png]]
The red points here consist of the region we need to check around.

One way we could handle this is by turning the boundary curve as a parametric curve as a function of a single variable $t$, and then finding its maximum/minimum in the single variable case.

For our Lagrange multiplier to work out, we need a way to describe the boundary region. We need to consider the region we are optimizing over, which we define with respect to our independent variables. Let us retain ourselves to the case in $\mathbb{R}^2$, where we work with a function $f(x,y)$  we are trying to optimize over a region given by $g(x,y)=k$ where $k$ is a constant. 

The function $g$ is a level curve where its height has been constrained to $k$. Since $g$ is a level curve, and we have previously established that $\nabla g$ is orthogonal to a corresponding point on the level curve, the gradient is perpendicular to all points along our level curve. 

The level curve $g$ is a level curve, so it comes from a larger function overall where we are simply considering a slice at height $k$. The total function that gives our $g$ in the background is something we don't need to consider, but it is best to still note it is there behind the scenes, and is also the thing generating our gradient. 

If we examine the actual boundary surface, we can quickly observe that the point which gives us our local maximum or minimum is the point which has a derivative of zero along our surface, which means that our point is lying flat.

![[Pasted image 20250626033402.png]]
Since the slope of the boundary curve is zero at this point, which means that the boundary curve is flat at this point, which indicates that the boundary point here is the same point that would lie along a level surface. We know that the gradient at this point will be orthogonal to point along the boundary here.

Remember that $g$ is a level curve, and thus $\nabla g \perp$ to all points along $g$. So, at the critical point, it follows that both $\nabla g$ and $\nabla f$ are orthogonal to the tangent line at the point. Which therefore means that $\nabla g$ and $\nabla f$ have the same orientation. 
# Example:
We must find the point closest to the origin on the hyperbola $xy=3$.
We can solve this traditionally by using the distance formula, and then considering minimizing squared distance:
$$d^2=\left(\sqrt{x^2+\dfrac{9}{x^2}}\right)^2=x^2+\dfrac{9}{x^2}$$
We can then take the derivative of this function and look for when it is zero:
$$2x-18x^{-3}=0$$
$$x^4=9 \Longleftrightarrow x = \pm \sqrt{3}$$
Thus the point $\left(\pm \sqrt{3}, \pm \sqrt{3}\right)$ is the point that minimizes our function using the traditional method. 

---
# Example with Lagrange Multipliers 

We can now use our method of Lagrange multipliers to solve this problem. 

In this instance the point that minimizes our distance is the smallest circle that still passes through a set of points along the hyperbola. The circles eventually get so small they do not appear on the graph and shrink. We have other points near these points as well, but they do not minimize the distance fully:

![[Pasted image 20250625183623.png]]
In this instance, our level curves are formed by $f(x,y)=c$ where $f$ is the squared Euclidean distance:
$$f(x,y)=\sqrt{x^2+y^2}$$
We vary the value of $f$ and continually plot new curves at each level. Our $f$ level curve, and our hyperbola curve $g$ should be tangent to one another in our minimized solution. Since $f$ and $g$ are tangent at the point of intersection, it follows that their tangent lines are both aligned, which means that the normals of each tangent are also aligned. 

Since we previously established that the [[gradient]] is orthogonal to the level surface, the normal vector here is given simply by the gradient of our two functions. We know that the gradients are oriented in the same direction, however, their size is not necessarily the same. 

Therefore, $\nabla f \parallel \nabla g$. Since both are parallel, we can express one as a constant multiple of the other:
$$\nabla f \cdot \lambda = \nabla g$$
Which is equivalent to saying that our gradients are proportional to one another. 

Our original problem was a min max problem involving two variables with $x,y$, with the constraint of $f(x,y)=c$. We are able to express these as a series of equations:
$$f(x) =
\begin{cases}
  g_{x}= \lambda f_{x}\\
  g_{y}= \lambda f_{y}\\
  xy=3
\end{cases}
$$
Which is equivalent to saying:
$$f(x) =
\begin{cases}
  2x= \lambda y\\
  2y= \lambda x\\
  xy=3
\end{cases}
$$
Notice that we can arrange the top two equations into a system of equations involving a matrix:
$$\begin{bmatrix} 2x & - \lambda y \\ \lambda x & -2y \end{bmatrix} =  \begin{bmatrix} 2 & - \lambda  \\ \lambda  & -2 \end{bmatrix} \cdot \begin{bmatrix} x \\ y \end{bmatrix}$$
We then get a homogeneous equation:
$$\begin{bmatrix} 2 & - \lambda  \\ \lambda  & -2 \end{bmatrix} \cdot \begin{bmatrix} x \\ y \end{bmatrix}=\begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
The trivial solution $x=y=0$ satisfies this system, however if we try it on the third constraint, $xy=3$ it fails. So, we need to keep looking for solutions. Note that if the determinant of our matrix is zero, we have infinitely many solutions for zero, which perhaps could be useful to us:
$$\text{det}\left( \begin{bmatrix} 2 & - \lambda  \\ \lambda  & -2 \end{bmatrix}\right)=-4+\lambda^2=0 $$
So it follows that:
$$\lambda=\pm2$$
This would tell us that $2y=2x$ if we substitute $\lambda=2$ back into our matrix equations above. This gives that $x=y$. We can then substitute this into our equation $xy=3$ to obtain $x^2=3$ which gives that our point must be at:
$$(\sqrt{3},\sqrt{3}) \text{ or } (-\sqrt{3},-\sqrt{3})$$
If we let $\lambda =-2$ we get that $x=-y$, and then $-x^2=3$ which is clearly unsolvable. Therefore, we only get 2 such points that minimize our distance from the origin.  

The method does not tell us if our solution(s) are a minimum, or a maximum. We cannot use the second derivative test either. We are not interested in defining second derivative directional derivatives either. In this case, we know that at infinity we maximize, but the 2 solutions we get here are the minimums. 

We have good reason to believe these are minimums, so it follows that we can use these. 

