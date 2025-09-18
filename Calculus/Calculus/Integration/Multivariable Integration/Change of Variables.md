---
title: Change of Variables
tags: 
draft: "false"
---
# Change of Variables in Double Integrals
Consider the example of the area of an ellipse that has semiaxes $a$ and $b$. Our curve is given by:
$$\left(\dfrac{x}{a}\right)^2+\left(\dfrac{y}{b}\right)=1$$
We can find the area of this region by calculating the [[Double Integrals]] integral given by:
$$\int \int_{R} dx dy$$
where $R=\left(\dfrac{x}{a}\right)^2+\left(\dfrac{y}{b}\right)^2 < 1$. Doing this with cartesian coordinates would be tedious, and be unpleasant. We can make the substitutions $\dfrac{x}{a}=u$
 and $\dfrac{y}{b}=v$ in order to make this particular substitution to make conversion to polar much easier. Our new region in turn becomes $R=u^2+v^2$

We can solve this simply with 2 independent substitutions. 
$$\dfrac{x}{a}=u \rightarrow du \cdot a = dx$$
$$\dfrac{y}{b}=v \rightarrow dv \cdot b = dy$$
Which results in:$$ab\int\int_{u^2+v^2<1}dudv$$
 This gives the area of the unit disk which is given by $\pi ab$ since this is clearly the area of a unit circle. 

For more complex examples, we need to have a better way to account for our different bounds. Let us suppose that our $u=3x-2y$ and that our $v=x+y$.
We need to find relation between $dA=dxdy$ and $dA' = dudv$. 

We can think of our transformation from $x$ and $y$ to $v$ and $u$ to be a transformation that is locally linear. Since it is locally linear, we can think of it as preserving the properties of 2 parallel lines staying parallel. In turn we get the following diagram from our transformation:
![[Pasted image 20250627034648.png]]
The rate of change is the same everywhere, so the position we begin with for our coordinates does not actually modify the resulting 

We can examine where the transformation sends our basis vectors, and compute the [[Determinant]] of the transformation and see how much our area has been scaled by. We then need to divide our differential by the amount that the area is scaled by. 

Let us call our scaled matrix $A$, we would get that $\text{det}(A)=5$, so our integral would be:
$$\int \int _{R_{x,y}}\cdots dxdy = \int \int_{R_{u.v}} \cdots \dfrac{1}{5}dudv$$
---
# General Case   
For an integral described by our standard $x,y$ variables, we can change our variables to the two functions $u=u(x,y)$ and $v=v(x,y)$ to obtain a new coordinate system that is easier to work with; We can approximate the rates of change using the definition of the differentials for both $u$ and $v$:
$$\Delta u \approx u_{x} \Delta x + u_{y} \Delta y   $$
$$\Delta v \approx v_{x} \Delta x + v_{y} \Delta y   $$
We can express this in matrix form:
$$\begin{bmatrix} \Delta u \\ \Delta v  \end{bmatrix} \approx \begin{bmatrix} u_{x} & u_{y} \\ v_{x} & v_{y} \end{bmatrix} \cdot \begin{bmatrix} \Delta x \\ \Delta y \end{bmatrix}$$
The scaling factor of our transformation actually turns out to be the determinant of our matrix of partial derivatives:
$$ \text{scale factor} = \text{det} \left(\begin{bmatrix} u_{x} & u_{y} \\ v_{x} & v_{y} \end{bmatrix} \right)$$
Moving in the $x$ or $y$ directions with respect to our new coordinates can be determined by computing our matrix of partial derivatives multiplied by $\hat{i} \cdot \Delta x$ and $\hat{j} \cdot \Delta y$:
$$ \begin{bmatrix} u_{x} & u_{y} \\ v_{x} & v_{y} \end{bmatrix} \cdot \begin{bmatrix} \Delta x \\ 0 \end{bmatrix} = \begin{bmatrix} u_{x}\Delta x \\ v_{x}\Delta x \end{bmatrix}$$
$$ \begin{bmatrix} u_{x} & u_{y} \\ v_{x} & v_{y} \end{bmatrix} \cdot \begin{bmatrix} 0 \\ \Delta y \end{bmatrix} = \begin{bmatrix} u_{y}\Delta y \\ v_{y}\Delta y \end{bmatrix}$$
We call this matrix the $\textbf{"Jacobian"}$ ([[Jacobian]]).

---
# The Jacobian Matrix
We denote the matrix responsible for producing our scale factor via a determinant as $J$, the Jacobian Matrix:$$J= \dfrac{\partial(u,v)}{\partial(x,y)} = \left| \begin{bmatrix} u_{x} & u_{y} \\ v_{x} & v_{y} \end{bmatrix} \right|$$It is important to note that the strangeness of this notation should be ignore and not taken literally. It reminds us that this tells us the ratio of our scaled values to our unscaled values.

We can then derive a general expression for our scale factor, which is given by:
$$du\cdot dv = |J| dx \cdot dy = \left| \begin{bmatrix} u_{x} & u_{y} \\ v_{x} & v_{y} \end{bmatrix} \right| dx \cdot dy$$
We take the area because we may get a negative from our operation since we may be performing some kind of flip between our basis vectors so we need to take the absolute value to ensure that we only have the positive area. 

It turns out that [[Polar Coordinate Integration]] can be derived from this method. 
#### Example 1. Polar Coordinates 
Let us consider the Jacobian for a polar coordinate transformation given that $x=r\cdot\text{ cos}(\theta)$,$y=r\cdot\text{ sin}(\theta)$, and $x^2+y^2=r^2$.
$$|J|=\left| \begin{bmatrix} x_{r} & x_{\theta} \\ y_{r} & y_{\theta} \end{bmatrix} \right|=\left| \begin{bmatrix} \text{cos}(\theta) & -r \text{ sin}(\theta) \\ \text{sin}(\theta) & r\text{ cos}(\theta) \end{bmatrix} \right|$$
Then we can find $\text{det}(|J|)$]:
$$\text{det}(|J|)=r(\text{cos}^2(\theta)+\text{sin}^2(\theta))=r$$
In conclusion we obtain that $dx\cdot dy = r \cdot d\theta dr$ 

## Remark: 
Note that the following Jacobians are inverses of one another:
$$\dfrac{\partial (u,v)}{\partial (x,y)} \cdot \dfrac{\partial (x,y)}{\partial (u,v)}=1$$
The matrices are inverses of one another and bring us back to having a proper scale factor in both ratio. Generally, our scale factor is also not a constant, it is often a variable. 
#### Example 2. 
Consider:
$$\int_{0}^1 \int_{0}^1 x^2y \cdot dxdy$$
Let $u=x$ and $v=xy$. Compute the integral after using change of variables. We first need to compute the Jacobian:
$$\dfrac{\partial (u,v)}{\partial(x,y)}=\left|det\left( \begin{bmatrix} 1 & 0\\ y & x \end{bmatrix} \right)\right|=x$$
So it follows that $du \cdot dv = x \cdot dxdy$. We know $x>0$ so $|x|=x$ in this context. We need to express our integrand in terms of $u$ and $v$ as well:
$$x^2y\cdot dx dy=uv\cdot dudv \cdot \dfrac{1}{u}=v \cdot dudv$$
We have to compute new bounds for our integral as well. Our order of bounds could be either $du,dv$ or $dv,du$ we do not know yet. I won't include the bounds calculation here it's a bit tedious. 