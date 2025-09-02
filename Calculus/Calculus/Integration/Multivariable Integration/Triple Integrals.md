---
title: Triple Integrals
tags: 
draft: "false"
---
# Triple Integrals
If we have a function of three variables, $f(x,y,z)$, and a solid region in space, $R$, then we can take the integral over this region with our function over $R$:
$$\int \int \int_{R} f\cdot dV$$
Where our $dv$ is our volume element. It depends upon what system of coordinates we are using. If it is the case that we are using Cartesian coordinates, then we will have $dv=dx\cdot dy \cdot dz$:$$\int \int \int_{R} f\cdot dx\cdot dy \cdot dz$$
We can calculate volume in a region  by describing a region $R$ and then just having a function $f(x,y,z)=1$, which makes our problem analogous to [[Double Integrals]] in that we are merely computing volume. 

#### Example 1. 
We have the region between the two paraboloids, $z=x^2+y^2$ and $z=4-x^2-y^2$ where we want to find the volume of this region:
$$\int \int \int_{R}1\cdot dV$$
![[Pasted image 20250630141526.png]]
We know that our surface will be constrained to have a circular region if we allow $x^2+y^2=4-x^2-y^2$. We can write our integral as the following:
$$\int \int \int_{x^2+y^2}^{4-x^2-y^2} dz \cdot dy \cdot dx$$
We do our bounds with respect to $x$ because [[Fubinni's Theorem]] allows this and to simplify our calculations. We need to narrow down our middle and outermost bounds by considering what happens in the $x,y$ plane, which happens to just be a disc. When we solve for our region we get that:
$$x^2+y^2 < 2 \implies \text{ disk of radius } \sqrt{2}$$
We can set up the middle bounds for our integral since we have described the disc, and in turn we get:$$\int_{\sqrt{2}}^{\sqrt{2}} \int_{-\sqrt{2-x^2}}^{\sqrt{2-x^2}} \int_{x^2+y^2}^{4-x^2-y^2} dz \cdot dy \cdot dx$$
We could also use [[Polar Coordinate Integration]] to simplify our calculation. After we calculate the $z$ bounds, we would get:$$\int_{\sqrt{2}}^{\sqrt{2}} \int_{-\sqrt{2-x^2}}^{\sqrt{2-x^2}} \int_{x^2+y^2}^{4-x^2-y^2} dz \cdot dy \cdot dx=\int_{\sqrt{2}}^{\sqrt{2}} \int_{-\sqrt{2-x^2}}^{\sqrt{2-x^2}} (4-2x^2-2y^2) dz \cdot dy \cdot dx$$We can now swap to polar coordinates. If we were to use our polar coordinates from the start we would get the following integral:
$$\int \int \int_{r^2}^{4-r^2}dz\cdot r \cdot d\theta$$
These are known as [[Cylindrical Coordinates]] more formally. Our volume element in cylindrical coordinates is $dx\cdot dy \cdot dz = r\cdot dr\cdot d\theta \cdot dz$. This comes out of polar coordinates.

---
# Applications

#### 1. Calculating Mass 
We can compute mass, since density, $\delta$, $\delta = \dfrac{\Delta M}{\Delta V}$, so $dm =\delta dV$. In total we can compute mass by the triple integral for a region in $\mathbb{R}^3$ as:
$$\int \int \int_{R} \delta \cdot dV$$
#### 2. Calculating Average Volume
$$\bar{f}=\dfrac{1}{\text{vol}(R)}\int \int \int_{R}f\cdot dV$$
We can also do a weighted average with density:$$\bar{f}=\dfrac{1}{\text{mass}(R)}\int \int \int_{R}f\cdot \delta \cdot dV$$
#### 3. Center of Mass: $(\bar{x},\bar{y},\bar{z})$
$$\bar{x}=\int \int \int_{R} x \delta\cdot dV$$
$$\bar{y}=\int \int \int_{R} y \delta\cdot dV$$
$$\bar{z}=\int \int \int_{R} z \delta\cdot dV$$
#### 4. Axis of Rotation:
$$\int \int \int_{R} \text{(dist to axis)}^2\cdot\delta \cdot dV$$
We can calculate our moment of inertia above the $x,y,z$ axes by:
$$I_{z}=\int \int \int_{R}r^2 \delta \cdot dV=\int \int \int_{R}(x^2+y^2) \delta \cdot dV$$
$$I_{x}=\int \int \int_{R}(y^2+z^2) \delta \cdot dV$$
$$I_{y}=\int \int \int_{R}(x^2+z^2) \delta \cdot dV$$