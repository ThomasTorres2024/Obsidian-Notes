---
title: The Directional Derivative
---
# Directional Derivative Introduction
We have seen how to express the derivative of a multivariable function with respect to its $x$ and $y$ axes previously. There may be instances where we want to express the derivative of a function with respect to an arbitrary direction. 

It turns out that there is a way to do this that we can express using very nice and compact notation. Let us consider the unit vector $\vec{u}$, and the [[gradient]] $\nabla f = \langle f_{x},f_{y} \rangle$ to give us the case for a function in $\mathbb{R}^2 \rightarrow \mathbb{R}$, then our directional derivative is given by:
$$\nabla f \cdot \vec{u}=f_{x}\cdot\text{cos}(\theta)+f_{y} \cdot \text{sin}(\theta)$$
![[Pasted image 20250625033416.png]]
We can think of the directional derivative as a way to slice our surface in any direction and then to find its derivative along said direction since the intersection between the plane along that line and the surface forms a curve that we can take derivatives on. 
# Formal Definition
We can think of our directional derivative by thinking of the definition of the [[Partial Derivative]] of a function $f(x,y)$ with respect to either $x$ or $y$. Let us write the definition of the partial derivative for each bellow:
$$\dfrac{\partial f}{\partial x}(a,b) = \lim_{h \to 0} \dfrac{f(a+h,b)-f(a,b)}{h}$$
$$\dfrac{\partial f}{\partial y}(a,b) = \lim_{h \to 0} \dfrac{f(a,b+h)-f(a,b)}{h}$$
We can think of these as vector equations as well evaluated on the vector valued function $f(\vec{a})$, evaluated on the varying vector $\vec{a}$. We can re-write our functions as:
$$\dfrac{\partial f}{\partial x}(\vec{a}) = \lim_{h \to 0} \dfrac{f(\vec{a}+\hat{i}h)-f(\vec{a})}{h}$$
$$\dfrac{\partial f}{\partial y}(\vec{a}) = \lim_{h \to 0} \dfrac{f(\vec{a}+\hat{j}h)-f(\vec{a})}{h}$$
Which is essentially the same thing, all we do is just vary our amount in the direction of $\hat{i}$ or $\hat{j}$. We can generalize this notion to nudge any particular direction vector, $\vec{v}$ given by:
$$\nabla_{\vec{f}}f(\vec{a})= \lim_{h \to 0} \dfrac{f(\vec{a}+\vec{v})-f(\vec{a})}{h}$$
# Derivation
The directional derivative is a special case of the multivariable chain rule. Let us consider a unit vector with components $\vec{u}=[a,b]^T$. We can think of $\vec{u}$ as the derivative of the vector values function given by $\vec{r}(s)$:
$$\vec{r}(s) =
\begin{cases}
  x(s) = x_{0} +as\\
  y(s)=y_{0}+bs 
\end{cases}$$
Clearly $\dfrac{dr}{ds}\vec{r}(s)=\vec{u}=[a,b]^T$
If we were to consider the derivative of the level curve function $w(x,y,z) : \mathbb{R}^3 \rightarrow \mathbb{R}$ where $x=x(s),y=y(s),$ and $z=z(s)$, then we can simply derive the directional derivative formula using the [[Multivariable Chain Rule]]:
$$\dfrac{dw}{ds}=\nabla f \cdot \dfrac{d \vec{r}}{ds} = \nabla f \cdot \vec{u}$$
We can succinctly express the formula for the directional derivative as:
$$\dfrac{dw}{ds}|_{\vec{u}}=\nabla w \cdot \vec{u}$$

---
# Further Interpretation of the Directional Derivative
The gradient gives the change of a function's value with respect to all of its constituent components. It is a vector in space. 

We can think of the direction derivative as a [[vector projection]] of our gradient onto the unit vector $\vec{u}$. The directional derivative tells us how much the function changes with respect to a particular direction. 

We can apply some further results from vector algebra here. Recall the cosine identity for vectors $\vec{x}$ and $\vec{y}$:
$$|\vec{x}\cdot \vec{y}|=\| x\| \|y \| \cdot \text{cos}(\theta)$$
Then since we have a dot product here, we can equate our directional derivative with the cosine identity:
$$\dfrac{dw}{ds}= \nabla w \cdot \vec{u}=\| \nabla w \| \| \vec{u} \| \cdot \text{cos}(\theta)= \|\nabla w \|  \cdot \text{cos}(\theta)$$

This demonstrates how we are obtaining the derivative of $w$ in some specific direction $\vec{u}$. 

We can also consider at what points we are maximizing our function. If it turns out that both the gradient and the directional are parallel, then their dot product is zero, which implies that their cosine is one, which implies their angle is the same. 

Therefore, the vector which maximizes the increase of the rate of change of our function will be the directional vector of the gradient. We can express this by 

If we want to know the slope of the gradient, it is given by: 
$$|\nabla w|=\dfrac{dw}{ds}|_{\vec{u}=\text{dir}(\nabla w)}$$
This corresponds to the magnitude of the vector $\vec{w}$.

To find the lowest descent, all we do is consider $-\text{dir}(\nabla w)$ which would reverse the direction vector and result in a negative cosine since the angle is zero but the orientations are opposite. In turn.

We also get further confirmation that the tangent vector and the gradient are in opposite direction, since the tangent vector at some point is the vector which minimizes the angle which would result in zero. 