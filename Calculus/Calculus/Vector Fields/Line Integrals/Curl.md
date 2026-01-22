---
title: Curl
tags:
draft: "false"
---
# Curl Intuition and Geometric Definition
The [[Curl]] of a [[Vector Field]] is the amount, thinking in terms of a physical intuition, fluid tends to rotate or swirl around it. Mathematically, we are summing up the measure of the tangents to the surface across all points along some surface $S$ in the [[Vector Field]]. 

Geometrically we can consider some region $D$ which contains point $p$. Let $n$ be a unit normal vector of $D$ in a plane with $p$. Then, we can provide a geometric definition of the curl with the following:
$$\text{curl } \vec{F}(P)\cdot \vec{n}=\lim_{D\to P} \frac{\int_{\partial D} F\cdot ds}{\text{area}(D)}$$
We essentially close in on some point $P$ as $D$ get progressively smaller. The portion of the [[Vector Field]] aligned with our surface $S$ will produce the rotational component. 

A nice result occurs if $F$ is in $2$ space. We have that the vector $\vec{n}=\langle 0,0,1\rangle$, which allows us to simplify our definition with the following:
$$\text{curl } \vec{F}(P)=\lim_{r \to 0^+} \frac{\int_{C_r} F\cdot ds}{\pi r^2}$$
Where we consider our region to be the circle of radius $r,C_r$ centered at $P$. Our [[Line Integral]] here sums up how much the tangent line is aligned with the [[Vector Field]]. The [[Curl]] is the measure of the circulation density as the limit of $r$ tends to $0$. 
# Curl Definition

The definition of [[Curl]] depends upon the dimension of the vector field. If we are operating over a 3d vector field, then our [[Curl]] will be of the form (where $\nabla$ here is the "[[Del]]" operator) for $\vec{F}=\langle P,Q,R \rangle$ we have the [[Cross Product]]:
$$\nabla \times \vec{F} = \text{curl}(\vec{F})= \det\left(\begin{bmatrix} \hat{i} & \hat{j} & \hat{k}\\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{bmatrix} \right)

$$

Since we can define a [[Vector Field]] $\vec{F}=N\hat{i}+M\hat{j}$, we can measure the rotational component of the vector field by a quantity called the "Curl":
$$\text{curl}(\vec{F})=N_{x}-M_{y}$$
If $\text{curl}(\vec{F})=0$ it follows that we have a [[Conservative Field]]. This follows since if $N_{x}=M_{y}$, then our vector field is conservative. This quantity is referred to as the "scalar curl".

If this test is passed and the vector field is defined everywhere, then our vector field is conservative. If our test fails, then our vector field is not conservative. If the test is passed but not defined everywhere, there is some ambiguity in our definition. 

For a velocity field, the curl measures the rotation part of motion. The curl measures twice the angular velocity of rotation component of a velocity field. 

The curl of a force field measures the torque exerted on an object in the field. 

The curl tells us how fast we are spinning at any given time up to a factor of two. The curl of the force field tells us how much fast our angular velocity will increase or decrease. 

---
# Properties 
#### Theorem 
For any $C^2$ function $f$, $\text{curl}(\nabla f) =0$. 
$$\therefore \nabla \times (\nabla f)=0$$
###### Proof
$$\begin{align}
\nabla \times \nabla f = \begin{bmatrix} \hat{i} & \hat{j} & \hat{k}\\
\frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\
\frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z}
\end{bmatrix}
\end{align}$$
Note that this matrix is clearly [[Linearly Independent]], so it clearly will have a resulting [[Determinant]] of 0. If we also just compute the [[Cross Product]] normally, the result will also be zero. 

---
# Identities
* $\text{curl}(F+G)=\text{curl}(F)+\text{curl}(G)$
* $\text{curl}(fF)=\nabla f \times F + f(\text{curl}F)$

---
# Examples 
#### 1.) Let $\vec{F}=\langle x^2y,z,xyz\rangle$ 
$$\nabla \times \vec{F} = \text{curl}(\vec{F})= \det\left(\begin{bmatrix} \hat{i} & \hat{j} & \hat{k}\\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x^2y & z & xyz \end{bmatrix} \right)$$
$$=\hat{i}(xz-1)-\hat{j}(yz)+\hat{k}(-x^2)$$
#### 2.) Let $\vec{F}=\langle x,xy,1\rangle$ 
$$\nabla \times \vec{F} = \text{curl}(\vec{F})= \det\left(\begin{bmatrix} \hat{i} & \hat{j} & \hat{k}\\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x & xy & 1 \end{bmatrix} \right)$$
$$=\hat{i}(0)-\hat{j}(0)+\hat{k}(y)+\hat{k}y$$
#### 3.) Let $\vec{F}=\left\langle \frac{-y}{x^2+y^2}, \frac{x}{x^2+y^2}\right\rangle$ 
$$\text{curl}(F)=P_x-Q_y=\frac{-2xy}{(x^2+y^2)^2}+\frac{2yx}{(x^2+y^2)^2}=0$$
$$\therefore \text{curl}(F)=0 \implies F \text{ is irrotational}$$
