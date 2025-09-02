---
title: Line Integrals
tags: 
draft: "false"
---
# Line Integrals of Vector Fields 
We can think of a line integral at first in the context of physics. Let us consider a [[Vector Field]] given by $\vec{F}$ and a displacement vector given by $\vec{r}$. When considering work we consider:
$$\text{Work=Force} \cdot \text{Displacement}=\vec{F}\cdot \Delta \vec{r}$$
This operation gives us the work, which tells us how much energy an operation needs to perform this operation. We consider $\Delta r$ to be a small nudge along our curve function over a region that is given by $\vec{r}$. 

In most cases we want to consider the total energy over the entire curve of $\vec{r}$ which we can consider by summing up the projections onto the curve for every point on the curve. 

We can call the trajectory that we are moving along, $c=c(x,y)$, and the force at that point given by  This requires integrating the dot product of the velocity function, $d\vec{r}$ vector function and the curve and the between $$w=\int_{c} \vec{F}\cdot d\vec{r}=\lim_{\Delta r_{i}\rightarrow 0} \sum_{i=1}^\infty\ \vec{F}\cdot \Delta \vec{r}_{i}$$Notice that this is equivalent to writing:
$$=\lim_{\Delta r_{i}\rightarrow 0} \sum_{i=1}^\infty\ \vec{F}\cdot \dfrac{\Delta \vec{r}_{i}}{\Delta t} \cdot \Delta t = \int_{t_{1}}^{t_{2}}\vec{F}\cdot\dfrac{d\vec{r}}{dt}dt$$
We can actually compute our expression with respect to time using our initial and end time as boundaries. Our vector field, $\vec{F}$ depends on $x,y$ before it depends on $t$, so we need to be able to express it in terms of each. 

Another way that we can think of our problem is thinking of the dot product of $\vec{F} = \langle M,N \rangle$ and $d\vec{r}=\langle dx,dy \rangle$. We can thus rewrite $\vec{F}\cdot d\vec{r}$:

$$\vec{F}\cdot d\vec{r}=Mdx+Ndy$$
$$\int_{c} \vec{F}\cdot d\vec{r}= \int_{c} Mdx+Ndy$$
Using our curve $c$, we only have 1 parameter that remains, and we can express our variables $x$ and $y$ in terms of this single parameter, which collapses this integral into a single variable integral, which can be easily computed. 

Another way that we can think of our line integral is through a geometric lens. We can consider $d\vec{r}$ to be a unit tangent vector, $\vec{T}$ that is scaled by some amount, $ds$, the arclength:
$$d\vec{r}=\langle dx,dy  \rangle = \vec{T}\cdot ds$$
Which would also give us:
$$\dfrac{d\vec{r}}{dt}= \left\langle \dfrac{dx}{dt}, \dfrac{dy}{dt} \right\rangle = \vec{T}\cdot \dfrac{ds}{dt}$$
We can rewrite our line integral formula as:
$$\int_{c}\vec{F}\cdot\vec{T}\cdot ds$$
In turn we get three equivalent ways to handle our line integral:
$$\int_{c} \vec{F}\cdot d\vec{r}= \int_{c} Mdx+Ndy=\int_{c}\vec{F}\cdot\vec{T}\cdot ds$$

---
#### Example 1.)
Let us consider the following vector field given by $\vec{F}$: $$\vec{F}=-y\hat{i}+x\hat{j}$$
Let us consider the curve, $c$, given by $x=t$ and $y=t^2$. 
$$\int_{c}\vec{F}\cdot d\vec{r}=\int_{0}^1\vec{F}\cdot \dfrac{d\vec{r}}{dt}dt= \int_{0}^1 \langle -y,x \rangle \cdot\langle 1,2t \rangle  dt$$
$$=\int_{0}^1(-y+2tx)dt=\int_{0}^1(-t^2+2t^2)dt=\int_{0}^1(t^2)dt=\dfrac{1}{3}$$
We can do this by the first method to obtain the following integral:
$$\int_{c} Mdx+Ndy=\int_{c} -y\cdot dx+x \cdot dy$$
We have two equations that relate $x$ and $y$, $x=t$ and $y=t^2$ so we can find their derivatives and substitute them in:$$\int_{c} (-t^2+2t^2)dt=\int_{0}^1 (t^2)dt=\dfrac{1}{3}$$

---
# Alternative Computation for Line Integrals
It may not be the case that we always are going to use or think of our line integral problem through a vector lens. Sometimes we may want to think of it in terms of scalar functions. 

Let us consider the function, $f(x,y)$ where $x=g(t),y=h(t)$, over the curve $C$. Our line integral will take the form:
$$\int_{c} f(x,y)ds= \lim_{n \to \infty} \sum_{k=1}^n f(x_{k},y_{k})\Delta s_{k}$$
This computation asks us, over some given curve $c$, that intersects with some surface, what is the total are along the curve? Consult the following image to clarify this fact:
![[Line-integral.png]]
When we compute integrals with respect to standard bounds, we don't need to think of the size of the increments on our curve changing. Along the curve for a line integral, this is something that we must consider. The increment along our curve is given by $\Delta s_{k}$, and the height is given by $f(x_{k},y_{k})$.

We can use the Pythagorean theorem to express our $\Delta s_{k}$, which is given by:
$$\Delta s_{k} = \sqrt{(\Delta x_{k})^2 + (\Delta y_{k})^2}$$
If we are interested in computing the arclength of a line integral, we can use the standard Pythagorean approximation at each segment along our curve:
$$\text{arclength }f \approx \sum_{i=1}^n f(x_{i},y_{i}) \sqrt{(\Delta x_{k})^2 + (\Delta y_{k})^2}$$
Which we can write our deltas in terms of $\Delta t$, which gives us the resulting expression:
$$\text{arclength }f \approx \sum_{i=1}^n f(x_{i},y_{i}) \sqrt{ \left(\dfrac{\Delta x_{k}}{\Delta t} \right)^2 + \left(\dfrac{\Delta y_{k}}{\Delta t} \right)^2} \cdot \Delta t$$
As $\lim_{x \to \infty}$  we see that:
$$\text{arclength}(f)= \int_{a}^b f(g(t),h(t)) \cdot \sqrt{g'(t)^2+h'(t)^2}dt$$
Since our curve $f$ can be parametrized. 

We can generalize this idea to 3 dimensions as well if $f$ is a function from $\mathbb{R} \rightarrow \mathbb{R}^3$, then we can write our line integral as:
$$\int_{a}^b f(g(t),h(t),k(t)) \sqrt{g'(t)^2+h'(t)^2+k'(t)^2}dt$$
---
# Line Integrals with Respect to X or Y
If for some reason we are only interested in computing what happens to our line integral with respect to $x$ or with respect to $y$, there are ways we can compute this. For the case where we are performing the integral using a dot product, we let the component of the vector field which corresponds to the x direction or y direction get zeroed out. 

We can think of this as projecting our function onto the $xz$ plane when we zero out $y$ or projecting it onto the $yz$ plane when we zero out $x$. 

This yields the following formulas:
$$\text{proj}_{xz}= \int_{a}^b f(g(t),h(t))g'(t)$$
$$\text{proj}_{yz}= \int_{a}^b f(g(t),h(t))h'(t)$$
For the [[Vector Field]] formulas given that the field $\vec{F} = M(x,y)\hat{i}+N(x,y)\hat{j}$ for the function $\vec{f}(t)=g(t)\hat{i}+h(t)\hat{j}$ we can express it as:
$$\text{proj}_{x}= \int_{c} g(t)\cdot M(x,y)\hat{i}$$
$$\text{proj}_{y}= \int_{c} h(t)\cdot N(x,y)\hat{j}$$
Also note that we can decompose any line integral as a sum of both projections:
$$\int_{C}\vec{F} \cdot \hat{T} ds= \int_{C} M(x,y)g(t)dt  + \int_{C} N(x,y)h(t)dt =\int_{c}Mdx+\int_{C}Ndy$$Let us consider the curve $C$ which is the parabola $y=x^2$ from $(1,1)$ to $(2,4)$. 