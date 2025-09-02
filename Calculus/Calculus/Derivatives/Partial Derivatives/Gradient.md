---
title: The Gradient
tags: 
draft: "false"
---
# Definition of the Gradient
The gradient is a vector which consists of the partial derivative over each input variable. We can define the gradient for $f(x,y,z) : \mathbb{R}^3 \rightarrow \mathbb{R}$ as:
$$\nabla w= \langle f_{x},f_{y},f_{z} \rangle$$
# Motivation
Let us recall the definition of the differential of a function $f(x,y,z) : \mathbb{R}^3 \rightarrow \mathbb{R}$ is given by:
$$df=\dfrac{\partial f}{ \partial x}\cdot dx+\dfrac{\partial f}{ \partial y}\cdot dy+\dfrac{\partial f}{ \partial z}\cdot dz$$
We can consider its differential with respect to time:
$$\dfrac{df}{dt}=\dfrac{\partial f}{ \partial x}\cdot \dfrac{dx}{dt}+\dfrac{\partial f}{ \partial y}\cdot \dfrac{dy}{dt}+\dfrac{\partial f}{ \partial z}\cdot \dfrac{dz}{dt}$$
We can express this differential as a dot product between the gradient and the derivative of the  velocity vector given by $\vec{r}'(t)$:
$$\vec{r}(t)=\langle x(t),y(t),z(t) \rangle$$
$$\vec{r}'(t)=\langle x'(t),y'(t),z'(t) \rangle$$
# Properties of the Gradient 
##### Theorem: $\nabla w \perp \text{ level surface } \dfrac{d}{dt}\vec{r}(t)$
Let us consider a level curve, $w : \mathbb{R}^3 \rightarrow{R}$ given by $w(x,y,z) = c$ where $c$ is a constant value and $x=x(t),y=y(t),$ and $z=z(t)$.

The function $\vec{r}(t)=\langle x(t),y(t),z(t)  \rangle$ is a parametric curve which is along the level surface $w$. The derivative of this curve, $\dfrac{d}{dt}\vec{r}(t)$, gives the vectors tangent to this parametric curve.

Let us then take the derivative of the level curve with respect to time. From the previous lecture we obtain that $\dfrac{dw}{dt}$ is:
$$\dfrac{dw}{dt}=\dfrac{\partial f}{\partial x} \dfrac{dx}{dt}+\dfrac{\partial f}{\partial y} \dfrac{dz}{dt}+\dfrac{\partial f}{\partial z} \dfrac{dx}{dt}=0$$
Since $c$ is a constant function, its derivative is zero. And since the level curve is equal to a constant, its derivative must always be zero. 

Notice that we can express our in terms of a [[dot product]] between our function $\dfrac{d}{dt}\vec{r}(t)$ and $\nabla w$:
$$\dfrac{dw}{dt}=\nabla w \cdot \dfrac{dw}{dt}\vec{r}(t)=0$$
We should also note that since we have a dot product, we are establishing a fact also about the two vectors involved. We are essentially saying that the gradient vector is orthogonal to the tangent vector at a point.

$\dfrac{dw}{dt} \vec{r}(t)$ can be thought of as a set of tangent vectors corresponding to each point along the parametric curve on the level surface $w$. Notice that this result would hold for any such $\vec{r}(t)$, which in effect says that the gradient vector at any point is orthogonal to the tangent vector at any given point.

Notice that through a point, there are many different tangent vectors that pass through, not simply just a single vector. If we take the span of all of the points that pass through the point, we obtain a plane of vectors. 

Geometrically, the [[tangent plane]] and the gradient vector are orthogonal. We can actually obtain the equation for the [[normal vector]] to the tangent plane simply by taking the coefficients of the gradient vector. Using this information and knowing that the point we are evaluating our partial derivative at. 
#### Example 
Let us consider the following $w(x,y,z)$:
$$w(x,y,z)=x^2+y^2-z^2=4$$
Let us find the tangent plane through $(2,1,1)$.

One way to approach the problem is by using our knowledge that the gradient of $w$ at our point is the normal vector. 
$$\nabla w=\langle 2x,2y,-2z \rangle$$
Evaluated at our point we get:
$$\langle 4,2,-2 \rangle$$
Using the definition of the plane we can write that our tangent plane is equal to:
$$4(x-2)+2(y-2)-2(z-1)=0$$
An equivalent way to solve this problem is to begin with a tangent plane approximation, which involves use of the definition of the [[differential]]. We will start with the differential:
$$dw = 2xdx + 2ydy -2zdz$$
We can then write this as an approximation:
$$\Delta w \approx 4 \Delta x + 2\Delta y - 2 \Delta z$$
Since $w$ is constant it never fluctuates, so its delta is zero. We can then substitute in the deltas for the other values:
$$0=4(x-2)+2(y-1)-2(z-1)$$
---
# Further Intuition on the Gradient
An easy way to think of the orthogonal property between the gradient and any level curve/surface is to consider what the derivative of the line along the level curve/surface tells us and what the gradient tells us. The derivative of a parametric curve embedded on the surface tells us in what direction we need to move to stay along the curve. The gradient tells us how much we need to move to move away from the curve to the next level set.

The gradient is also always where the direction of steepest ascent is. The negative of the gradient points in the direction of steepest descent. We can think of this as the direction which is orthogonal to the tangent plane, the direction that takes us to the next level set.
