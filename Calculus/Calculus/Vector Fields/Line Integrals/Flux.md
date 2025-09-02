---
title: Flux
tags: 
draft: "false"
---
# Flux Definition
The big idea behind Flux is to measure the net inflow and outflow of a fluid from a region. 

The Flux is a [[line integral]]. Say we have a plane curve, $c$, over a vector field, $\vec{F}$, then it follows that our flux of $\vec{F}$ across $c$ is:$$\int_{c}\vec{F}\cdot\vec{n}\cdot ds$$The vector $\vec{n}$ is a normal unit vector to the tangent of our curve $c$. Everywhere along our integral, $\vec{n}$ is $90^{\circ}$ clockwise from our curve. At every point, we are computing the dot product between the [[Vector Field]] and the unit normal vector. 

If we break our $c$ into small pieces of $\Delta s$, then we obtain our flux by considering what happens when each $\Delta s$ gets arbitrarily small:
$$\text{flux}(\vec{F},c,\vec{r})= \lim_{\Delta s \rightarrow 9}\left(\sum \vec{F}\cdot\vec{n}\cdot\Delta s \right)$$
Notice that our calculation for [[Work]] is the line integral for the curve given by $\vec{r}$ as:
$$W=\int_{c}\vec{F}\cdot\vec{T}\cdot ds$$
Where for each tangent vector on the curve $c$ we compute how aligned it is with the vector field $\vec{F}$ via the dot product, and then multiply it with the size of the arclength, $ds$ at each step. At each step we are performing a [[vector projection]] of the vector field at each point onto our curve, and summing these components for every point on $c$. 

The Flux calculation is essentially the same thing, the only difference is that we project onto the component of the force field that is orthogonal to our tangent vector in the curve. 

---
# Physical Interpretation  
Let $\vec{F}$ be a velocity field. It follows that the Flux measures how much fluid passes through a curve $c$ per unit time. Why does this make sense? Let us consider the example where our $\vec{F}$ translates everything to the right. 

![[Pasted image 20250629222726.png]]
We can think of this as a very zoomed in portion of our vector field and curve $c$. If we move our curve to the right in the vector field, we end up drawing a parallelogram, and this will hold for any such vector field: 
![[Pasted image 20250629223314.png]]
The amount of fluid that passes through this section is given by the parallelogram that is drawn out by extending the segment of our curve through a vector in $\vec{F}$. If our unit time is quite small, like a couple milliseconds, then this is a perfectly good approximation. 

We calculate our net inflow and outflow by considering how much fluid comes in through our direction $\vec{n}$ and how much goes out by considering how much goes out through $-\vec{n}$. What flows across $c$ left to right is counted positively. What flows right-to-left is counted negatively. 

---
#### Example. 
Let us consider the case where $c$ is a circle of radius $a$ at the origin and is counterclockwise. Our vector field is given by $\vec{F} =x\hat{i}+y\hat{j}$. By convention, we would be counting the amount of net outflow from the circle via our normal vector:
![[Pasted image 20250629224401.png]]
We know that a tangent vector for our curve $c$ would be given by $\langle -y,x \rangle$ which would have a corresponding normal vector of $\langle x,y \rangle$. Since each  vector in our vector field has the same description as the normal vector, it follows that:
$$\vec{F} \parallel \vec{n}$$
Since both vectors are completely aligned in the same direction, it follows that their dot product is:
$$\vec{F}\cdot\vec{n}= \|\vec{F} \| \| \vec{n} \| =\| \vec{F} \|=a$$
It follows that our flux at a point would be $a$. We can now calculate our flux via  line integral:
$$\int_{c} \vec{F} \cdot \vec{n} \text{ }ds = \int_{c}a\cdot ds=a\cdot \text{length}(c)=2\pi a \cdot a = 2\pi a^2$$
#### Example 2. 
If we consider the vector field given by $\vec{F}=-y\hat{i}+x\hat{j}$, and consider the circle of radius  $a$ as our curve $c$, we would see that there is no net outflow, since at each point, the tangent vector of $c$ would be parallel to $\vec{F}$, so our orthogonal component would always be zero. In turn, our Flux would also be zero. 

![[Pasted image 20250629225553.png]]

---
# Calculation Using Components
If we do not have a valid geometric interpretation that we can use, we need a general way to express and work with our integrals. Recall that in our computation of [[Line Integral]]s we could express the derivative of an arbitrary curve, $r$, over our vector field $\vec{F}$, by:
$$d\vec{r}=\vec{T}\cdot ds =\langle dx,dy \rangle$$
We can think of $\vec{n}$ in a similar way. Our $\vec{n}$ is simply $\vec{T}$ rotated $90^{\circ}$ counter clockwise. We know that the orthogonal vector here would be:
$$\vec{n}\cdot ds=\langle -dy,dx \rangle$$
If we rotated it clockwise for some reason we would get:
$$\vec{n}\cdot ds=\langle dy,-dx \rangle$$
All we need to do to obtain these vectors is just multiply our vector of differentials by a rotation matrix of $-\dfrac{\pi}{2}$ or $\dfrac{\pi}{2}$. This allows us to re-write our expression for Flux for the given vector field $\vec{F}=\langle P,Q\rangle$ as:
$$\int_{c}\vec{F}\cdot\vec{n}\cdot ds=\int_{c}\langle P,Q\rangle\cdot \langle dy,-dx \rangle= \int_{c}-Qdx+Pdy$$
---
# Flux Along a Closed Curve 
If $c$ is a closed curve and $\vec{F}$ is a vector field, it follows that we should have a way to evaluate our linear integral in terms of a double integral, as [[Green's Theorem]] allows us to evaluate the line integral without having to do any kind of parametrization of $y$. 

Green's theorem for Flux essentially works the same way. If $c$ is a counterclockwise curve that is closed, and $\vec{F} = \langle P, Q\rangle$ is defined and differentiable in $R$, then we can express our line integral in terms of the [[Divergence]]:
$$\oint_{c}\vec{F}\cdot\vec{n}\cdot ds= \int \int_{R} \text{div}(\vec{F})\cdot dA$$

This is simply Green's theorem in normal form. The other Green's theorem is Green's theorem for tangent form. We want to show that the following is true:
$$\oint_{c}\vec{F}\cdot\vec{n}\cdot ds=\oint_{c}-Qdx+Pdy=\int \int_{R}(P_{x}+Q_{y})dA$$
The first step of this is true by definition of the gradient and the dot product. Let us try and write this in terms of the tangent form of Green's Theorem that we have previously seen. Let $M=-Q$ and $N=P$.
$$\oint_{c}-Qdx+Pdy=\oint_{c}Mdx+Ndy$$
By Green's Theorem it follows that:
$$\oint_{c}Mdx+Ndy=\int \int_{R}(N_{x}-M_{y})dA$$
We can substitute our values back into the expression and obtain:
$$\int \int_{R}(P_{x}+Q_{y})dA$$
It turns out this is the result we were trying to find. In conclusion we have shown that Green's Theorem for normals is true. 

---
#### Example of Green's Theorem
Let $\vec{F}=x\hat{i}+y\hat{j}$ over a curve, $c$, which is a circle of radius $a$ at the origin. First, we must compute $\text{div}(\vec{F})$:
$$\text{div}(\vec{F})=\dfrac{\partial}{\partial x}(x)+\dfrac{\partial}{\partial y}(y)=1+1=2$$
Using Green's theorem we can express our line integral as:
$$\oint_{c} \vec{F}\cdot \vec{n} \cdot ds= \int \int_{R}2da$$
We can factor out 2, and then recognize that we are finding the area of a circle, which has radius $a$, which in total yields $2\pi a^2$ for our flux. 

---
# Flux in 3d 
The Flux in higher dimensions needs to be measured through a surface, and no longer just a line as in $\mathbb{R}^2$. We need to use a surface integral. 

Our interpretation of Flux in 3d is simply the amount of matter that flows through a surface over a region $S$ per unit time. 

Our surface consists of three variables, but in total it only really occupies something that is two dimensional, so we can end up expressing it in terms of two variables, and then performing a [[Double Integrals]] with respect to said field. 

In the 2d case, we considered the normals to a curve. In the 3d case, will consider all of the normals to our plane:![[Pasted image 20250701023948.png]]
We have 2 choices for where our normal goes. We can choose normals $\vec{n}$ that are oriented upward, and normals that are oriented downward. When we choose clockwise or counterclockwise in $\mathbb{R}^2$, we already had ideas of orientation, we didn't need to define them. 

Here, we need to orient the surfaces ourselves, and define them in our own way. There is no concrete definition that is as stable as in the case of $\mathbb{R}^2$. 

Let $\vec{F}$ be our vector field, $S$ be a surface on our vector field, and $\vec{n}$ be a normal vector on it. 

We can consider our flux integral to be:
$$\int \int_{S} \vec{F} \cdot \vec{n} dS$$
By this we mean going through every point on the surface and consider the projection of our force onto the orthogonal component. If our vector field is tangent to the surface, our flux is zero. 

As a bit of a note, sometimes we write $\vec{n} \cdot dS$ as $d\vec{S}$, which often can simplify our computations. 
#### Example 1.  
Lets consider the flux of $\vec{F}=\langle x,y,z \rangle$ through a sphere of radius $a$ centered at the origin. Our sphere looks something like this, which has normals everywhere along the curve:
![[Pasted image 20250701024940.png]]
Our normal vectors are parallel to the vectors of the gradient field. We can obtain our $\vec{n}$ by writing it and the gradient vector as:
$$\vec{n}=\dfrac{1}{a}\langle x,y,z \rangle$$
We can simplify the inner part of our flux integral since we know that:
$$\vec{F}\cdot \vec{n} = \sqrt{x^2+y^2+z^2} = a $$
So we rewrite our Flux integral as:
$$\int \int_{S} \vec{F} \cdot \vec{n} \cdot dS=a \int \int_{S}  dS$$
We know that $\int \int_{S} dS$ gives the area of a sphere, meaning our total answer is $4 \pi a^3$. 

#### Example 2. 
Let us consider $\vec{F}=\langle 0,0,z \rangle$, with a sphere of radius $a$ centered at the origin. We still have $\vec{n}=\dfrac{\langle x,y,z \rangle}{a}$. When we compute our dot product between $\vec{F}$ and $\vec{n}$ we obtain:
$$\vec{F}\cdot \vec{n}= \dfrac{z^2}{a}$$
So, our resulting integral is:
$$\int \int_{S} \vec{F} \cdot \vec{n} \cdot dS= \dfrac{1}{a} \int \int_{S} z^2\cdot  dS$$
We can use spherical coordinates to solve our answer, that is we need to express $ds$ as a product of $d \theta \cdot d \phi$ and the additional integrating factor. Notice that in [[Spherical Coordinates]] derivation of the surface area of a slice on the circle, we already obtained our $dS$ equivalent:
$$ds=d \theta d \phi \cdot a^2 \cdot \text{sin}(\theta)$$
We also know that $z=\text{cos}(\theta) \cdot a$ if we take a slice of the sphere surface and consider it in the plane, we would see that this is how we get our $z$. We thus have an integral we know how to compute:
$$\dfrac{1}{a} \int \int_{S} z^2\cdot  dS= \int \int_{S} a^3\cdot \text{ cos}^2(\phi)\text{ sin}(\phi)  d\phi \cdot d\theta  $$
We can find our bounds easily for a sphere and lastly get:
$$\int_{0}^{2 \pi} \int_{0}^{\pi} a^3\cdot \text{ cos}^3(\phi)\text{ sin}(\phi)  d\phi \cdot d\theta  $$

---
# Alternative Derivation for flux calculation in $\mathbb{R}^2$
Let us consider a vector field in $\mathbb{R}^2$, $\vec{F}$, over the closed curve $c$ given by $\vec{r}(t)$. Our integral is given by:
$$\text{flux}(\vec{F},c)\oint_{c}\vec{F}\cdot \vec{n}_{r'(t)}(t)ds$$
We want to be able to express $\vec{n}(t)$ in terms of the components of $\vec{r}'(t)$ . We can see that $\vec{r}'(t)$ can be expressed as:
$$\vec{r}'(t)=x'(t)\hat{i}+y'(t)\hat{j}$$
We can also see that $\vec{n}(t)=-y'(t)\hat{i}+x(t)\hat{j}$ simply by inspection, since the dot product between the two results in zero, meaning they are orthogonal and $\vec{n}(t)$ is a normal vector. 

We can also do this via the determinant method and [[cross product]]. We know that $\hat{k}$ is orthogonal to $\vec{r}'(t)$ since $\hat{k}$ is in the third dimension sticking upward and our other vectors are flat. We can compute the determinant between $\vec{r}'(t)$ and $\hat{k}$ which gives us:
$$\text{det}\left(\begin{bmatrix} \hat{i} & \hat{j} & \hat{k} \\ x'(t) & y'(t) & 0
\\ 0 & 0 & 1 \end{bmatrix} \right)=\hat{i}y'(t)-\hat{j}x'(t)$$
Which would give us the following vector for $\vec{n}(t)=\begin{bmatrix}y'(t)& -x'(t) \end{bmatrix}^T$. We can express out resulting flux integral as:  
$$\text{flux}(\vec{F},c)\oint_{c}\vec{F}\cdot (\begin{bmatrix}y'(t)& -x'(t) \end{bmatrix}^T)ds=\oint_{c}M(x,y)y'(t)ds+\oint_{c}-N(x,y)x'(t)ds$$