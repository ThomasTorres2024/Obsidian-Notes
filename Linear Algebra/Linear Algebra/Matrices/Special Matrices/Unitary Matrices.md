---
title: Unitary Matrices
draft: "false"
tags:
---
# Definition
Unitary Matrices are matrices whose inverse is the conjugate transpose. That is to say for $A \in \mathbb{R}^{n \times n}$:

$$AA^H=A^HA=I_{n}$$
By definition, [[Unitary Matrices]] are also [[Normal Matrices]]. Unitary matrices also preserve the Euclidean product. Let us consider $x,y \in \mathbb{R}^n$. It follows that:
$$(A\vec{x})^H(A\vec{y})=\vec{x}^HA^HA\vec{y}=\vec{x}^H\vec{y}=\langle \vec{x}, \vec{y} \rangle$$
$$Q\vec{x}=\lambda \vec{x}$$
$$(Qx)^HQ\vec{x}=(Qx)^H(\lambda \vec{x})$$
$$\bar{\lambda}\vec{x}^H\vec{x}$$
---
# Isometries 

For any given [[Matrix]] $U$ such that $U^HU=UU^H=I_{n}$ the following statements are equivalent:
1. $U^HU=I$
2. $\langle Ux,Uy\rangle=\langle x,y\rangle$
3. $\|Ux\|^2=\|x\|^2 \forall x$

$Proof).$ 
$(1) \implies (2)$
$$U^HU=I \iff x^HU^HUy=x^Hy \iff \langle Ux, Uy \rangle = \langle x,y\rangle$$
$(2)\implies(3)$
Let $y=x$. 
$(3)\implies(1)$
$$\|Ux\|^2 = \|x\|^2 \iff \langle Ux, Ux \rangle = \langle x, x\rangle \iff x^HU^HUx=x^Hx \iff U^HU=I $$

It is important to note that, between two [[Inner Product]] spaces, [[Unitary Matrices]] are Isometries (Isometry) since they preserve [[Norm]]s following a linear transformation. 