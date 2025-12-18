---
title: Parametrized Surfaces
draft: "false"
tags:
---
# Parametrizing Surfaces

Parametrized surfaces can be defined in the following manner. Let $D$ be a domain in $\mathbb{R}^2$. If $X: D \to \mathbb{R}^2$ is continuous, then $S=X(D)$ is a parametrization of the surface. It follows also that if $X$ can be differentiated, then $S$ also can be so, so $X$ is $C^1 \iff S$ is $C^1$ [[Continuity Class]].  

# Common Surface Parametrizations

##### Graph Parametrization
The most common parametrization for a function is a function's graph. Given some $z=f(x,y)$, we can express the parametrization of this function by $X(x,y)=(x,y,f(x,y))$. 
##### Surfaces of Revolution ([[Solids of Revolution]])
A surface of revolution takes a curve, $z=g(y)$, and rotates it around some given axis. If the curve is revolved around an axis, we obtain that for $z=g(y)$, that $X(r,\theta) = (r\cos(\theta), r\sin(\theta), g(r))$.  

# Examples 

#### Cylinder
Find the parametrization for a cylinder: $x^2+y^2=1$. We can use [[polar coordinates]] and observe that for $x=\cos(\theta)$ and $y=\sin(\theta)$ that we can already obtain a way to express the base of the cylinder. To describe any position along the cylinder's height, we can leave $z$ as is. The resulting parametrization is given by:
$$X(\theta,z)=\langle \cos(\theta),\sin(\theta),z \rangle$$
#### Unit Sphere 
The unit sphere is given by $x^2+y^2+z^2=1$. We can find a parametrization of it by considering the [[Spherical Coordinates]]. Let $x=\cos(\theta)\sin(\phi), y=\sin(\theta)\sin(\phi).$ It follows that:
$$-x^2 - y^2+1=z^2 \iff -\cos(\theta)^2\sin(\phi)^2-\sin(\theta)^2\sin(\phi)^2+1=z^2$$
$$\iff 1-\sin(\phi)^2=z^2 \iff z=\cos(\phi)$$
Therefore, a resulting parametrization is:
$$X(\theta, \phi) = \langle \cos(\theta)\sin(\phi),\sin(\theta)\sin(\phi), \cos(\phi) \rangle$$

### Right 45 Degree Cone 
The cone is given by $z=\sqrt{x^2+y^2}$. One parametrization we can give is by using the graph parametrization, such that $X(x,y)=\langle x,y, \sqrt{x^2+y^2} \rangle$. 

---
# Tangency of Parametrizations 
If $X(u,v)$ is a surface in $\mathbb{R}^3$, and it is differentiable at $(u_{0},v_{0})$, then $X_{u}$ and $X_{v}$ are tangent to the surface at $(u_{0},v_{0})$. We should recall that the [[Gradient]] is orthogonal to a [[tangent plane]]. Therefore, it follows that $X_{u}$ and $X_{v}$ are tangent to the surface at $(u_{0},v_{0})$. 

If $X_{u}$ and $X_{v}$ are [[Linearly Independent Vectors]], it follows that $\vec{N}=X_{u} \times X_{v}$ is a normal vector of the tangent plane at $(u_{0},v_{0})$. 

We can compute the [[tangent plane]] using the following formula:
$$\vec{N}\cdot \langle x-x_{0},y-y_{0},z-z_{0} \rangle =0$$
Which is to say all points orthogonal to the normal vector, which is a plane. 

#### (Proof Sketch) Let $f : \mathbb{R}^2 \to \mathbb{R}$ be differentiable. The tangent plane to $z=f(x,y)$ at $(x_{0},y_{0},z_{0})$ is given by:
$$z=z_{0}+f_{x}(x_{0},y_{0})(x-x_{0})+f_{y}(x_{0},y_{0})(y-y_{0})$$
Due to the above theorem, we know that $f_{x} \perp P, f_{y} \perp P$. Given that the gradients are linearly independent, the cross product is the normal vector the plane. Using the formula above for the dot product with parametrizations, we obtain the plane formula above.

---
# Surface Qualities 
1. A surface is regular at point $(u_{0},v_{0})$ if $N = X_{u} \times X_{v} \neq 0$ at $(u_{0},v_{0})$. 
2. A surface is regular if it is regular at all points Any differentiable function must be regular since, $N=\langle -f_{x},-f_{y},1 \rangle$ which can never be 0. 


