---
title: Divergence
tags: 
draft: "false"
---
# Geometric Interpretation of the [[Divergence]]
The [[Divergence]] can be thought of using a physical intuition. We can think of it as the amount of fluid flowing out of some region. This gives rise to a geometric definition. Let $B_r$ be the ball with radius $r$ and let $P$ be the origin, for some vector field, $\vec{F}$:
$$\text{div} \vec{F}(P)= \lim_{r\to0^+} \frac{\large \iint_{\partial B_r}F\cdot dS}{\text{vol}(B_r)}$$
As $r \to 0^+$, the ball $B_r$ shrinks down to $P$. 

Intuitively I think this is a ratio between the total amount that the vector field is aligned with the cross product between the vector field and the vector orthogonal to the force. Intuitively we can think of this as the amount that is leaking out of the solid at this point. 

The [[Divergence]] at point $P$ is denoted by $\text{div} \vec{F}(P)$ which is the "flux density" at $P$. 

We can interpret [[Divergence]] as $\text{div}(F)>0 \implies$ fluid is leaking over some region. We can think of this as being a "source", where everything "diverges".

We can interpret that $\text{div}(F)<0 \implies$ fluid is compressing into the vector field over some region. This is a "sink", where everything "converges". 

If all of our points tend toward a single point, we can think of this kind of point as a "sink", where everything is convergent. 
##### Example 1.) Calculate divergence of $r(x,y,z)=\langle x,y,z \rangle$. Find $\text{div}(r)$ at the origin using the geometric definition.


# Divergence Definition

The formula for [[Divergence]] depends upon the dimension of the [[Vector Field]] in question.  Here we make use of the "del" operator, such that for $\nabla$ in $\mathbb{R}^3$, we have that:
$$\nabla = \left\langle \frac{\partial }{\partial x},\frac{\partial }{\partial y},\frac{\partial }{\partial z} \right\rangle $$

The divergence, with components of a [[Vector Field]], $\vec{F} :\mathbb{R}^2 \mapsto \mathbb{R}^2,$  $\vec{F}=\langle P, Q\rangle$, is given by:
$$\text{div}(\vec{F})=P_{x}+Q_{y}=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}$$
For a [[Vector Field]] $\vec{F}:\mathbb{R}^3 \mapsto \mathbb{R}^3$, $\vec{F}= \langle P,Q,R \rangle$, then the [[Divergence]] is defined by the following, which we represent symbolically by $\nabla \cdot \vec{F}$ indicating the [[Dot Product]]:
$$\text{div}(\vec{F})= \nabla \cdot \vec{F}= \frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z} $$

The divergence measures how much things are diverging in a vector field. We can interpret divergence of a vector field as how much our flow is expanding. 

If we have positive divergence, we see that a fluid is expanding within a region, and if we have a negative divergence, we see that fluid is entering a system. 

For this definition of [[Divergence]], we can think of these intuitively by the amount of fluid in a [[Vector Field]] which flows in a direction of one of the three fundamental basis vectors. 

For some 2 dimensional vector field, we have a flow along the $x$ and $y$ direction. For some 3 dimensional vector field, we have a flow along the $x,y,z$ direction. The formulas for both cases reflect this particular intuition. 

[[Divergence]] in the direction of $x^+$ corresponds to positive divergence in that term, and divergence in the opposite direction corresponds to negative divergence in that term. The same can be said for the other dimensions as well. 

---
# [[Divergence]] Properties:

#### Theorem 
For any $C^2$ [[Vector Field]] $F$, $\text{div}\text{ curl}(\vec{F}) =0$:
$$\nabla \cdot (\nabla \times f)=0$$

* $\text{div}(F+G)=\text{div}(F)+\text{div}(G)$
* $\text{div}(fF)=(\nabla f)\cdot F + f \text{div}(F)$
* $\text{div}{(F \times G)}=(\text{curl}(F)\cdot (G-F)\text{curl}(G))$

---
# Examples:
#### Example 1.) 
Let $\vec{F}=\langle x^2y,z,xyz \rangle$. We can compute its [[Divergence]] using the [[Divergence]] formula. 
$$\text{div}(\vec{F})= 2xy+xy =3xy$$
#### Example 2.) 
Let $\vec{F}=\langle x,xy,1 \rangle$. We can compute its [[Divergence]] using the [[Divergence]] formula. 
$$\text{div}(\vec{F})= 1+y+0=1+y$$

#### Example 3.) 
Let $\vec{F}=\langle xy,y^2-x^2 \rangle$. We can compute its [[Divergence]] using the [[Divergence]] formula. 
$$\text{div}(\vec{F})= y+2y=3y$$
#### Example 4.) Let $\vec{F}=\left\langle \frac{-y}{x^2+y^2}, \frac{x}{x^2+y^2}\right\rangle$ 
$$\text{div}(F)=P_x+Q_y=\frac{2xy}{(x^2+y^2)^2}+\frac{-2yx}{(x^2+y^2)^2}=0$$
$$\therefore \text{div}(F)=0 \implies F \text{ is divergence-free/incompressible}$$
