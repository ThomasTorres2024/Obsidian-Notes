---
title: Projection Matrices
draft: "false"
tags:
---
# Projection Matrices Definition 

Orthogonal projections concern themselves with taking vectors that exist in higher dimensional spaces and then bringing them down and constraining them to lower dimensional spaces. Another way we can think of the idea of projection is by using the physical intuition of shining light onto an object and observing its shadow, in some sense its form is being into a lower dimensional space. Projection matrices in essence perform the same operation, except with additional constraints of linearity that we would find within a matrix. 

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

Our projected vector, $P\vec{v}$ and the vector $\vec{v}$ has a difference in the [[Nullspace]] of the projection matrix $P$. Consider the product $P(P\vec{v}-\vec{v})=P^2\vec{v}-P\vec{v}=P\vec{v}-P\vec{v}=\vec{0}$, and thus $P\vec{v}-\vec{v} \in Nul(P)$. 

---
# Types of Projectors 
The projections we will speak of most are [[Orthogonal Projections]], which ensure that the difference vector between the projection of a vector and the original is orthogonal to the space it is being projected onto, which is also to say that it is a member of $N(P^T) \iff N(P)$. There are also [[Oblique Projectors]] which do not enforce this condition. 


#### Complementary Projectors 
We call this class of Projectors [[Complementary Projectors]] because of their relation to [[Complementary Subspaces]].

If $P$ is a projector, then the matrix $I-P$ is another projection matrix because it is also idempotent. It satisfies the condition that $(I-P)^2=I-P$:
$$(I-P)^2=I-2P+^2=I-P$$
We can argue that this space actually projects into the [[Nullspace]] of $P$. Notice that if $P\vec{v}=\vec{0}$, that for $(I-P)\vec{v}=\vec{v}$, so we can see that $nul(P) \subseteq \text{span}({I-P}$).  Moreover, for any $\vec{x} \in \mathbb{R^n}$, it follows that:
$$(I-P)\vec{x}=\vec{x}-P\vec{x} \in \text{Nul}(P)$$
Which means $(I-P) \subseteq \text{Nul}(P)$, so since both [[vector space]]s are subsets of one another it follows that they are equivalent. We can also argue that the vector spaces are also complimentary. We can express their bases as a direct sum of one another:
$$(I-P)=I-P$$ and we can also see that:
$$\text{rng}(P)=\text{nul}(P) = \{ 0 \}$$
We can thus say that this project separates $\mathbb{C}^m$ into two different spaces.

###### (Theorem) Two separate subspaces have a projector from one space to the other  
We say that $\exists P_{R},P_{N}$ such that both are projectors that project onto their corresponding spaces
$$P_{R}=\text{Range}(P) : P_{N}= \text{Nul}(P)$$
Another equivalent condition for [[Complementary Subspaces]] is that we can express any vector in both spaces as the sum of a vector from one and a vector from the other, which is to say (more formally):
$$\vec{v_{1}} \in S_{1},\vec{v_{2}} \in S_{2} \text{ and } S_{1} \oplus S_{2}=\mathbb{C}^m \text{ and } S_{1} \cap S_{2} = \{ \vec{0} \}$$
Then it follows that:
$$\vec{v}_{1}+\vec{v_{2}}=\vec{v},\vec{v} \in \mathbb{C}^m$$
Projections arise frequently in applications. One application we are interested in is when a matrix with a full eigen-basis, and when we want to know in what direction one of its eigen vectors may lie, to which we apply a projection matrix. 

### Orthogonal Projectors
An orthogonal projector projects onto a subspace $S_{1}$ along a space $S_{2}$ where $S_{1}$ and $S_{2}$ are orthogonal. There is also an algebraic definition of [[Orthogonal Projector]]. When $P$ is [[Hermitian]], that is to say that $P^H=P$. This result can be proved:

###### Theorem - A projector $P$ is orthogonal if and only if $P^H=P$
Consider $P\vec{x} \in S_{1}$, and $(I-P)\vec{y} \in S_{2}$, then we can determine that $P$ and $P^H$ are orthogonal by computing the dot product between all vectors from $P$ and one from $I-P$  and showing that they must always be 0:
$$(P\vec{x})^H \cdot (I-P)\vec{y}=\vec{x}^HP^H(I-P)\vec{y}=\vec{x^H(P^H-P^HP)\vec{y}=0}$$
By the fact that all projectors are symmetric, and specifically that our matrix is Hermitian, we can express the following equivalent statement:
$$\vec{x}(P-P^2)\vec{y}=\vec{x}(P-P)\vec{y}=0$$
Now we must show that an orthogonal projection is necessarily done by $P=P^H$. We can use [[Single Value Decomposition]] for this proof. Assume that we have two complementary subspaces given by $S_{1}$ and $S_{2}$ such that $S_{1} \perp S_{2}$, where $S_{1}=\{q_{1},q_{2},\cdots q_{n}\}$ where each $q_{i} \in \mathbb{C}^m$.  We can say something similar for $S_{2}$ except its basis vectors span from $n+1$ to $m$. For the projection matrix $P$, the vector $P$ projects onto $S_{1}$ along $S_{2}$. 

For any $x \in S_{1}$, it follows that $Px=x$ because we are projecting a vector belonging to the subspace onto itself, and for any $y \in S_{2}$ it follows that $Py=0$ since all vectors in $S_{2}$ are orthogonal to those in $S_{1}$. 

If we now consider an [[orthogonal matrix]] $Q$ where $Q_{j}=q_{j}$, then $PQ$ will consist of a matrix where every column after $q_{n}$ is zeroed out:
$$PQ=\begin{bmatrix} q_{1} & q_{2} & \cdots & q_{n} & \cdots & 0 \end{bmatrix}$$
We can then multiple by $Q^H$ on the left and we obtain the follow diagonal matrix, $\Sigma$, where all values are zeroed out after $n$:
$$Q^HPQ=\begin{bmatrix} e_{1} & e_{2} & e_{3} & \cdots &  e_{n} & 0 & \cdots & 0\end{bmatrix}$$
This gives the following SVD/[[Eigen Value Decomposition]] of $P$, also note since $P$ is Hemritian it follows that $P$ always is guaranteed an [[Eigen Value Decomposition]]:
$$P=Q\Sigma Q^H$$
But also we can verify that it is Hermitian now quite easily.

### Rank One Orthogonal Projector
An important type of projector is the rank one projector, where we project a subspace down onto a one dimensional space. Take $q$ where $q$ is an orthogonal vector. This direction is given by , and our projector is thus:
$$P_{q}=qq^H$$
We can construct higher rank projectors from this one. The project for the $m-1$ other dimensions is provided by doing $I-P_{q}$, which gives the complementary subspace of $P_{q}$.  For vectors that are not necessarily unit length we have a general formula:
$$P_{a}=\frac{aa^H}{a^Ha},P_{\perp a}= I-\frac{aa^H}{a^Ha}$$

### Projection with Arbitrary Basis 
We can also do projections with a basis that is not necessarily orthogonal by using the [[Moore-Penrose Pseudo Inverse]]. Let $A \in \mathbb{C}^{m \times n}$. The difference between the orthogonal projection and $y$ must always be orthogonal to each column of $A$:
$$a_{j}^H(y-v)=0$$
We can rewrite this as:
$$a_{j}^H(Ax-v)=0$$
Since this must be true for all $J$ we can write:
$$A^H(Ax-v)=0$$
But this is a [[normal equation]] which has a verifiable answer:
$$A^HAx-A^Hv=0 \iff A^HAx=A^Hv $$
$A^HA$ is invertible, and thus we obtain the [[Moore-Penrose Pseudo Inverse]]:
$$x=(A^HA)^{-1}Av$$
The general projector is expressed as:
$$P=(A^HA)^{-1}Av$$



---
# Projection with an Orthonormal Basis
Projector matrices are assumed to have a rank less than their size, and we can thus represent them in a more efficient way by using [[Reduced SVD]] rather than the [[Full SVD]]. If we only consider the full columns of $Q$ in our above factorization, we end up with the following result:
$$P=\hat{Q}\hat{Q}^H$$
The matrix $\hat{Q}$ also does not necessarily need to come from SVD, if we have orthonormal vectors $q_{1} \to q_{n}$ in $\mathbb{C}^m$, then any vector $v  \in \mathbb{C}^m$ can be represented as a part parallel to the projector $P$ and a part orthogonal to it:
$$v=r+\sum_{i=1}^n {(q_{i}q_{i}^H)}v$$
Where $r$ is some error vector or we can think of it as the remainder  between each component of $q$. We can express the component in $V$ thus as:
$$y=\hat{Q}\hat{Q}^Hv$$
![[Pasted image 20251002103851.png]]










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