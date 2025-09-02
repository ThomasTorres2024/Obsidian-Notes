---
title: Surface Integrals
tags: 
draft: "false"
---
# Computing Surface Integrals For Flux in $\mathbb{R}^3$
When we are computing the given [[Flux]] of a [[Vector Field]] in $\mathbb{R}^3$, we consider how much the normal of a surface, $S$, aligns with the vector field at that point. We denote our normal vector $\vec{n}$ and we denote our area element by $dS$. 

It turns out that we can express $\vec{n} \cdot dS$ as $\langle -f_{x},-f_{y},1 \rangle \cdot dx \cdot dy$. We can derive this expression along a surface using the following geometry. 

We will consider a small slice of the $xy$ plane, starting at some point $(x,y)$. We then consider some small step away from this point $\Delta x$ and another $\Delta y$. 

We can observe on the graph that these two points get mapped to two vectors along our surface $S$, giving the vectors $\vec{u}$ and $\vec{v}$. We have previously established that the magnitude of the [[cross product]] gives us the area spanned by a parallelogram constructed out of these two vectors. 

It turns out that the cross product also gives us the [[normal vector]] to the surface at that point, but just scaled up by some amount:
$$\vec{u} \times \vec{v} = \Delta S \cdot \vec{n}$$

In turn, this will give us our area element for the surface. 
![[Pasted image 20250703000303.png]]
We need to be able to express our vectors $\vec{u}$ and $\vec{v}$ so that we can perform a cross product on them. We can find our vector formulas by subtracting their elements pointwise, that is to say:
$$\vec{u}=\langle \Delta x + x-x,y - y, f(x+\Delta x,y)-f(x,y) \rangle \approx \langle \Delta x, 0,\Delta x \cdot f_{x} \rangle$$
$$\vec{v}=\langle  x -x,\Delta y + y - y, f(x,y+\Delta y)-f(x,y) \rangle \approx \langle 0, \Delta y, \Delta y \cdot f_{y} \rangle$$The last step we write as linear approximations since we can write the delta of our function as approximately the [[Differentials]] of our function. 

Lastly, note that for each vector we can factor out the deltas, so we can simplify our cross product nicely:
$$\vec{u} \times \vec{v} = \langle 1,0,f_{x} \rangle \times \langle 0,1,f_{y} \rangle\cdot \Delta x \cdot \Delta y =$$
$$=\text{det}\left(\begin{bmatrix} \hat{i} & \hat{j}& \hat{k}\\1 & 0 & f_{x}\\ 0 & 1 & f_{y} \end{bmatrix} \right)\cdot \Delta x \cdot \Delta y= \langle -f_{x},-f{y},1 \rangle $$
Therefore we obtain the result that:$$\vec{u} \times \vec{v} = \pm \langle -f_{x},-f_{y},1 \rangle dx dy$$Which allows us to orient our normals upward or downward with respect to how we orient our surface. 

---
#### Example Flux Calculation 
Let us consider the vector field $\vec{F}=z\hat{k}$ of the paraboloid $z=x^2+y^2$ above the unit disk. Let us find the flux of this field through the surface.
$$\text{flux}(\vec{F},z)=\int \int_{S}\vec{F}\cdot \vec{n} \cdot dS= \int \int \langle 0,0,z \rangle \cdot \langle -f_{x},-f_{y},1 \rangle dx \cdot dy   $$
$$= \int \int_{S} \langle 0,0,z \rangle \cdot \langle -2x,-2y,1 \rangle dx \cdot dy  = \int \int_{S}z \cdot dx dy$$
Note that the function we are differentiating this to get our normal must be the surface, because we want to obtain the normals of of source to find Flux. Also, since $z$ is related to $x$ and $y$, we can rewrite our integral again:
$$\int \int_{S}(x^2+y^2)dx\cdot dy$$
We can convert this to polar to make it nicer, since $r^2=x^2+y^2$ and $dxdy = dr\cdot d\theta \cdot r$ we can easily make a substitution and we can see that:
$$= \int_{0}^{2\pi} \int_{0}^1 r^3 drd\theta = 2\pi$$
---
# Computing a Surface Integral by Parametrization
We can compute a surface integral by parametrization. Say we have a surface given by $\vec{r}=\langle x,y,z \rangle$ where $x=x(u,v),y=y(u,v),z=z(u,v)$. Principally, we should be able to express our surface in terms of $u,v$ so that we end up with a double integral. and have an easy computation. 

Generally, we want to be able to express $\vec{n} \cdot dS$ in terms of our variables $u$, and $v$:
$$\vec{n} \cdot dS = ? \cdot dudv$$

It turns out that we can use our idea from the cartesian coordinates above, where we computed the cross product for some $dx$ and $d$y nudges at the point $x,y$. We have essentially the same idea here for $u$ and $v$. 

We also need to introduce some new notation. Note the following:
$$\dfrac{\partial \vec{r}}{\partial u} \Delta u = \left\langle \dfrac{\partial x }{\partial u} \cdot \Delta u, \cdots \right\rangle$$
The two sides of our parallelogram can be found when we choose to examine $u$ and vary it by $\Delta u$ and keep $v$ constant and vice versa. In turn the two sides of our parallelogram are:
$$\dfrac{\partial \vec{r}}{\partial u} \cdot \Delta u \text{ and } \dfrac{\partial \vec{r}}{\partial v} \cdot \Delta v$$
We know that computing the cross product of these two vectors gives the normal vector that we need to compute Flux, and also gives us the size of the parallelogram spanned by the two vectors when we consider the normals's magnitude. 

So, we can write:
$$\vec{n} \Delta s = \left( \dfrac{\partial \vec{r}}{\partial u} \Delta u\right) \times \left( \dfrac{\partial \vec{r}}{\partial v} \Delta v\right)=\left( \dfrac{\partial \vec{r}}{\partial u} \right) \times \left( \dfrac{\partial \vec{r}}{\partial v} \right)\Delta u\Delta v$$
$$= \pm \left( \dfrac{\partial \vec{r}}{\partial u}  \times \dfrac{\partial \vec{r}}{\partial v} \right)\Delta u\Delta v $$
As we allow our deltas to go to infinity it ends up giving:
$$\vec{n}dS=\pm \left( \dfrac{\partial \vec{r}}{\partial u}  \times \dfrac{\partial \vec{r}}{\partial v} \right)du\cdot dv $$
---
# Further Examples That Illustrate Geometric Intuition About $\vec{n}\cdot dS$
#### Example 1.) Plane 
Let us consider a plane $S$ in $\mathbb{R}^3$. 
![[Pasted image 20250703010539.png]]
We can find a relation between $dA$, the projection of our plane $S$ onto the standard $xy$ plane by considering the projection of $\Delta S$ onto $\Delta A$. Recall the [[vector projection]] formula:
$$\Delta A =\Delta S \cdot \text{cos}(\alpha)$$
It turns out that we can express our $\alpha$ as the vector between two normal vectors, the plane's normal vector, and the vertical direction, $\hat{k}$:
$$\text{cos}(\alpha) = \dfrac{\vec{N}\cdot\hat{k}}{\| N \| \cdot \| k\|}=\dfrac{\vec{N}\cdot\hat{k}}{\| N \|} $$
Using substitution we can clearly see that:
$$\Delta S = \Delta A \dfrac{1}{\text{cos}(\alpha)}= \Delta A \dfrac{\| N \|}{\vec{N}\cdot \hat{k}}$$
Multiply both sides by a unit normal vector, $\vec{n}$, that comes from our plane:
$$ \vec{n} \Delta S  = \Delta A \cdot \vec{n}  \dfrac{\| N \|}{\vec{N}\cdot \hat{k}} = \pm \dfrac{\vec{N}}{\vec{N}\cdot \hat{k}} \Delta A = \pm \dfrac{\vec{N}}{\vec{N}\cdot \hat{k}} dx \cdot dy  $$
If we wanted to project onto something other than $x$ and $y$, we could've just as easily chosen $y$ and $z$ or something else, the argument is similar. 

#### Example 2.) Level Surface and the Gradient 
Let us consider $S$, and the function $g(x,y,z)=z-f(x,y)=0$. We know that the [[Gradient]] of a level curve is normal to its tangent and surface, so we get that our normal vector, $\vec{n}$ can be expressed as: 
$$\vec{N}=\nabla g(x,y,z)=\langle -f_{x},-f_{y} ,1\rangle$$
I'm not really sure why we do this, I asked chat gpt about this and the math checks out but we divide the left side by $\vec{N} \cdot \hat{k}$, it's one so it does nothing but we get this result:
$$\dfrac{\vec{N}}{\vec{N}\cdot \hat{k}}dx dy = \langle -f_{x},-f_{y},1 \rangle dxdy$$This is a more general result as we don't need to solve for $z$. 