---
title: Greens Theorem
tags: 
draft: "false"
---
# Definition of [[Green's Theorem]] 
Let us recall the definition of the [[Curl]] for a vector field in two dimensions, $\vec{F}=\langle M, N \rangle$:$$\text{curl}(\vec{F})=N_{x}-M_{y}$$ The [[Vector Field]] is said to be a [[Conservative Field]] if $\text{curl}(\vec{F})=0$. We can compute the [[Line Integral]] directly along a closed curve to determine this fact, or we can make use of "Green's Theorem". 

Green's theorem states that for a closed curve $c$ where $c$ goes counterclockwise, enclosing a region $R$, with a vector field $\vec{F}$ that is differentiable in $R$, then it follows that:
$$\oint_{c}\vec{F}\cdot d\vec{r}=\iint_{R} \text{curl}(\vec{F})dA= \iint_{R}(N_{x}-M_{y})dA$$
If it is the case that $c$ is clockwise, we would simply multiply our integral by $-1$

# Proof of [[Green's Theorem]]
We can make use of the previously proved The Divergence Theorem. In order to use the divergence theorem, we consider vector field 
 and the normal vector to the region . We can consider a rotation of 
 by 90 degrees, and then consider the tangent components of  (since we rotated by  degrees). Therefore, we will obtain:
$$\int_{\partial D} \vec{F} \cdot \textbf{ n } ds= \int_{\partial D} \langle -Q,P\rangle \cdot \mathbf{t }dS-\iint_D \text{div}(\langle -Q,P \rangle) dxdy=\iint_D [-Q_x +P_y ]dxdy$$$$=\iint_D \text{curl}(\vec{F})dxdy$$
---
# Applications
The area of a two dimensional region can be calculated using [[Green's Theorem]]. 
Consider the [[Vector Field]], $$\vec{A}=\langle -y, x \rangle$$
Over the closed region $D$. Then: 
$$\frac{1}{x}\int_{\partial D} \vec{A} \cdot \textbf{ t}dS= \frac{1}{2} \iint_D\text{curl}(\vec{A})= \frac{1}{2}\iint_D \left[\frac{\partial }{\partial x}(x)- \frac{\partial}{\partial y}(-y) \right]dxdy$$
$$= \frac{1}{2} \iint_D (1+1)dxdy=\frac{2}{2}\iint_Ddxdy= \text{Area}(D)$$
#### Example 1. 
Let $C$ be the circle of radius 1 centered at $(2,0)$ that is counterclockwise. Let us compute the line integral:
$$\oint_{c}ye^{-x}dx+\left(\dfrac{1}{2}x^2-e^{-x}\right)dy$$ If we were to directly approach the problem we would be using the bounds, $$x=2+\text{cos}(\theta),dx=-\text{sin}(\theta)d\theta$$$$y=\text{sin}(\theta),dx=\text{cos}(\theta)d\theta$$
Instead, we can just compute a double integral instead of a line integral. We will let $N=\left(\dfrac{1}{2}x^2-e^{-x}\right)$ and $M=ye^{-x}$. It follows that our resulting integral is:
$$\int \int_{R}(x+e^{-x}-e^{-x})dA=\int \int_{R}x\cdot dA$$
Instead of computing this raw, we can think of this as the $x$ position in the center of mass with a uniform density of 1. It follows that:
$$\int \int_{R}x \cdot dA=\text{Area}(R) \cdot \bar{x}$$
We know that $\bar{x}=2$ where the circle is centered, and $\text{Area}(R)=\pi$ since it is a circle, so our result is $2\pi$ in total. 

It is important to note that the vector field at the origin is not defined, which messes with 

---
# Special Case 
Let $\vec{F}$ be a vector field defined everywhere in the plane, if $\text{curl}(\vec{F})=0$ then $\vec{F}$ is a conservative field. Using green's theorem we see that for the vector field $\vec{F}$ it is true that:
$$\oint_{c} \vec{F} \cdot d\vec{r}= \int \int _{R}\text{curl}(\vec{F})dA=\int \int_{R}0\cdot dA=0$$
Let us try to apply Green's theorem with a vector field that was not defined at a point but has a curl of zero everywhere else. The curl everywhere along the field is zero, except when we go through the single  undefined point. We cannot apply Green's theorem to this vector field. The curl here is somehow infinite and not zero when going through that point. Since the region has a hole in it, we cannot integrate over it 

---
# Proof of Green's Theorem 
We want to prove that:
$$\oint_{c}Mdx+Ndy= \int \int_{R}(N_{x}-M_{y})dA$$
If it is the case that $N=0$ we get the special case for our vector field:$$\oint_{c}Mdx+Ndy= \oint_{c}Mdx= \int \int_{R}(-M_{y})dA$$If we prove this case, we can then prove that the case where $M=0$ is true, and then we can prove the case where it is true for both $M$ and $N$:
$$\oint_{c}Ndy=\int \int_{R}NdA$$
Now that we can examine only one component of the vector field, we can split $R$ into simpler regions that are easier to work with.  We can decompose $M$ into curves that enclose $R$. The curve $c_{1}$ encloses $R_{1}$ and $c_{2}$ encloses $R_{2}$. When we do a line integral over both of these regions, we introduce a new path on each of our closed curves of opposite orientation. 
![[Pasted image 20250629195239.png]]
When we add the line integrals together the new paths cancel, and we get our resulting region $R$. It turns out that we can cut our region $R$ into "vertically simple" regions. This means that for $x$ values where $a<b$ and $x<a<b$, then we have $f_{1}(x) < y <f_{2}(y)$, meaning we only intersect our region twice. 

Thus, if we take a look at one of the sub-regions of$R$ that is vertically simple, and $c$ is the boundary of $R$, where our region is bounded by $y=f_{2}(x)$ and $y=f_{1}(x)$, we get four curves in total. Two are constant functions that are vertical components, and two are functions expressed with respect to $f_{1}(x)$ and $f_{2}(x)$. The vertical components have a $dx=0$, so we are stuck with the components with respect to $f_{1}$ and $f_{2}$. Therefore we can write:
$$\int_{c_{1}} Mdx=\int_{a}^bM(x,f_{1}(x))dx-\int_{a}^b M(x,f_{2}(x))dx$$
We can take a look at the other expression as well. We can re-write it as:
$$\int \int_{r}-M_{y}dy=-\int_a^b \int_{f_{1}(x)}^{f_{2}(x)} \dfrac{\partial M}{\partial y}dyd=\int_{a}^b M(x,f_{1}(x))dx-\int_{a}^b M(x,f_{2}(x))dx$$Notice that when we evaluate this expression, it really is the same as our integral expression above. Since we have shown that our special case is true, we can analogously show that it is true for the component defined with $N$, sum both components, add them together, and we prove the general case. 

---
# Intuition Behind Green's Theorem
The way I like to think of the theorem is that we can calculate the curl over some region simply by dividing it into smaller and smaller pieces that eventually cancel each other out to the point that we end up just defining bounds for a double integral. 

We can think of our line integral as a measure of [[circulation density]] along a boundary which indicates the area of some inner region. This is like the integral operation, which related area to the bounds of the antiderivative function, and so we analogously can compute the net circulation density of a region just by computing its line integral. 

---
# Other Forms of Green's Theorem 
In addition to the green's theorem discussed above, we have computed a formula for the component of velocity or force that is parallel to the tangent line of a curve. This idea we can further extend to encompass the normal component as well when we are working with the [[Flux]] which elaborates more on the idea there. 

For a vector field, $\vec{F}=\langle P,Q\rangle$, the solution to a flux line integral can be solved by a corresponding double integral given in the following:
$$\oint_{c}\vec{F}\cdot\vec{n}\cdot ds=\oint_{c}-Qdx+Pdy=\int \int_{R}(P_{x}+Q_{y})dA$$
---
# Resolving Line Integrals with Green's Theorem With Discontinuities in a Vector Field
Let us recall [[Green's Theorem]] for tangents and for normal for a [[Vector Field]] $\vec{F}$ where $\vec{F}$ is differentiable everywhere and is defined everywhere. If we are given a counterclockwise closed curve, $c$, it follows that we can express [[Line Integral]]s involving these regions with the following:
$$\oint_{c}\vec{F}\cdot \vec{n}=\int \int_{R}\text{div}(\vec{F})\cdot dA$$
$$\oint_{c}\vec{F}\cdot d\vec{r}=\int \int_{R}\text{curl}(\vec{F})\cdot dA$$
If there is a single undefined point along the vector field, then our identity in our region $R$, our identity will not hold. Let us consider the vector field, $\vec{F}=\dfrac{-y\hat{i}+x\hat{j}}{x^2+y^2}$. Any region that encloses the origin will not have zero curl. But, everywhere else, the field has zero [[Curl]]. 

It turns out that we can still apply Green's theorem to find the curl along some regions. If our region $R$ loops around but does not contain the area with a hole, we can take a line integral with respect to the center region that contains the hole, and subtract it from our larger region. We can now apply Green's theorem. All we need to do is be careful and essentially just remove the problem areas by subtracting a curve. 

We can do a similar thing for calculation of [[Flux]] and [[Divergence]]. All we have to do is be careful that our inner curve is clockwise or counterclockwise. 

