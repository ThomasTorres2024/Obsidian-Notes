---
title: Projection Matrices
draft: "false"
tags:
---
# Projection Matrices Definition 

Orthogonal projections concern themselves with taking vectors that exist in higher dimensional spaces and then bringing them down and constraining them to lower dimensional spaces. 

We can describe this more succinctly through a matrix equation where $P$ represents the projection matrix, and $x$ is an arbitrary vector in space. The follow properties hold:

$$P^2x=Px$$
Geometrically, we can think of the projected vector $Px$ being perfectly inline with the projection space, and thus further projections onto said space will result in the same vector since it has already been projected. 

It also is the case that $P$ is idempotent, which is to say that:

$$P^n=P$$
Meaning the application of $P$ any number of times is the same as applying it once. 

Since we are losing at least one dimension by projecting onto a lower space, it follows that:

$$\text{rank}(P)<n$$
Lastly, the Projection matrix is a symmetric one:

$$P^T=P$$
Since $P$ is orthogonal and a projection matrix, it follows that it is symmetric. 

---
# Orthogonal Projections are Symmetric 

Consider vectors $\vec{u}$ and $\vec{v}$. We can consider their orthogonal projects onto another given by: 

$$P\vec{u} \cdot \vec{v} = <\hat{u},\vec{v}>$$

$$\vec{u} \cdot P\vec{v} = <\vec{u},\hat{v}>$$
These constitute a projection of $\vec{u}$ onto $\vec{v}$ and a projection of $\vec{v}$ onto $\vec{u}$ respectively. If we consider a mutual projection onto another given by: 

$$P\vec{u} \cdot P\vec{v} = <\hat{u},\hat{v}>$$

We can prove that all three of these identities are actually equivalent. We must take into consideration that we can express each vector as a sum of two vectors that consist of a component that is parallel and orthogonal to each respective subspace:

$$\vec{u}=P\vec{u}+\vec{u}_{\perp}$$
$$\vec{v}=P\vec{v}+\vec{v}_{\perp}$$

In the dot products all we do is make the according and substitutions, and we can algebraically verify this property: 

$$<P\vec{u},\vec{v}>=(P\vec{u})^T\vec{v}=\vec{u}^TP^T(\vec{v})=\vec{u}^TP^T(P\vec{v}+\vec{v}_{\perp})=\vec{u}^TP^TP\vec{v}+\vec{u}^TP^T\vec{v}_{\perp}=$$
$$\vec{u}^TP^TP\vec{v}+\vec{u}^TP^T\vec{v}_{\perp}=\vec{u}^TPP\vec{v}+\vec{u}^TP\vec{v}_{\perp}=\vec{u}^TP\vec{v}$$
And secondly:

$$<\vec{u},P\vec{v}>=\vec{u}^TP\vec{v}=(P\vec{u}+\vec{u}_{\perp})^TP\vec{v}=(\vec{u}^TP+\vec{u}_{\perp}^T)P\vec{v}=\vec{u}^TPP\vec{v}+(P\vec{u}_{\perp})^T\vec{v}=\vec{u}^TP\vec{v}$$
Lastly: 

$$<P\vec{u},P\vec{v}>=\vec{u}^TP^TP\vec{v}=\vec{u}^TP\vec{v}$$

In conclusion, all three of these projections have the same value with respect to the real inner product. 

---

# Projection Matrices and Eigen Values 

Projection matrices will be of lower rank than full rank and are responsible for reducing a dimension. Since projection matrices are not full rank, it implies that $0$ is an eigen value of $P$, since there is a null space that is nontrivial.

Since we are preserving the parallel component another eigen value is $1$. Thus the only eigen values of our projection matrix is $0$ and $1$. 