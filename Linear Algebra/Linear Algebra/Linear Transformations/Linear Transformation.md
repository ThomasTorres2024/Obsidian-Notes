---
title: Linear Transformations
tags: 
draft: "false"
---
# Linear Transformations

We can think of a linear transformation as a type of function that operates on vector spaces and outputs vectors in another vector space. For the [[Vector Space]] or spaces, $\mathcal{V,W}$, a linear transformation $\mathcal{L} : \mathcal{V \rightarrow W}$ has the following properties: 

1. $\mathcal{L}(\vec{v}_{1}+\vec{v}_{2})=\mathcal{L}(\vec{v}_{1})+\mathcal{L}(\vec{v}_{2})$
2. $\mathcal{L}(\alpha \cdot \vec{v}_{1}) = \alpha \mathcal{L}(\vec{v}_{1})$ for $\alpha \in \mathbb{F}$

We can think of the first property as satisfying the fact that addition of elements in $\mathcal{V}$ and then applying the transformation is equivalent to adding transformed vectors in $\mathcal{W}$.

Likewise, scaling a vector and then transforming it under $\mathcal{V}$ is equivalent to transforming a vector and then scaling it afterwards. 

The domain of our given function is $\mathcal{V}$ and our given co-domain is $\mathcal{W}$. 

Some examples of more typical linear transformations include 

1. The identity map, which maps a vector to itself: $\mathcal{Id}(\vec{v}) = \vec{v}, \vec{v} \in \mathcal{V}$
2. Mapping by a matrix, $A \in \mathbb{R}^{n \times m}$ for $\vec{x} \in \mathbb{R}^m$, then our given linear transformation is $\mathcal{L}_{A} : \mathbb{R}^m \rightarrow \mathbb{R}^n$, $\mathcal{L}_{A} = A\vec{x}$
3. Let $M \in \mathbb{R}^{m \times m}$ and $N \in \mathbb{R}^{n \times n}$ be fixed matrices then we can define the following linear transformation: $\mathcal{L}_{MN}(X) = MXN$ for $X \in \mathbb{R}^{m \times n}$

Some examples of exotic linear transformations include [[derivatives]], [[integrals]], and laplace transforms, as all of these satisfy the two conditions of [[linearity]]:

1. The set of continuous functions on $C[a,b]$, with linear transformation $S : C[a,b] \rightarrow \mathbb{R}$: $$S(f(x)) : = \int_{a}^bf(x)dx, \forall f \in C[a,b]$$
2. The derivative operator given by $D : \mathcal{P}^n \rightarrow P^{n-1}$ defined by: $$D(p(x))=\frac{d}{dx}(p(x)), \forall p(x) \in \mathcal{P}_{n}$$
---
# Additional Properties of Linear Transformations 

Let $\mathcal{L : V \rightarrow W}$ be a linear transformation. The following can be said:

1. The $\vec{0}_{\mathcal{V}}$ vector is always mapped to the $\vec{0}_{\mathcal{W}}$ vector: $$\mathcal{L}(\vec{0}_{\mathcal{V}})=\vec{0}_{\mathcal{W}}$$If we consider that $0 \cdot \vec{0}_{\mathcal{V}}= \vec{0}_{\mathcal{V}}$ then we can write: $$\mathcal{L}(0 \cdot \vec{0}_{\mathcal{V}})= 0 \cdot \mathcal{L}(\vec{0}_{\mathcal{V}})= \vec{0}_{\mathcal{W}}$$
2. If $\mathcal{L}(\vec{0}_{\mathcal{V}}) \neq \vec{0}_{\mathcal{W}}$ then $\mathcal{L}$ is not a linear transformation, since it would violate scalar multiplication rule. 
3. For $\vec{v}_{1},\vec{v}_{2},\cdots,\vec{v}_{n} \in \mathcal{V}$ and scalars $a_{i},a_{2},\cdots,a_{n} \in \mathbb{F}$ then: $$\mathcal{L} \left(\alpha_{1}\vec{v}_{1}+\alpha_{2}\vec{v}_{2}+\cdots+\alpha_{n}\vec{v}_{n}  \right)=\alpha_{1}\cdot\mathcal{L}\left(\vec{v}_{1}\right)+\alpha_{2}\cdot\mathcal{L}\left(\vec{v}_{2}\right)+\cdots+\alpha_{n}\cdot\mathcal{L}\left(\vec{v}_{n}\right)$$
$$\mathcal{L}\left( \sum_{i=1}^n \alpha_{i}\vec{v}_{i}\right)=\sum_{i=1}^n \alpha_{i}\mathcal{L}(\vec{v}_{i})$$
4. $\mathcal{L}(-\vec{v})=-\mathcal{L}(\vec{v}), \forall \vec{v} \in \mathcal{V}$, this clearly comes from the scalar multiplication properties of linear transformations 
---

# [[Nullspace]] and Range of Linear Transformations 

Every linear transformation has several subspaces associated with it. Let us consider the linear transformation $\mathcal{L} : \mathcal{V} \rightarrow \mathcal{W}$. 

There are two primary subspaces we are interested in studying for our $\mathcal{L}$, mainly the set of vectors in $\text{dom}(\mathcal{L})$ that get mapped to $\vec{0}_{\mathcal{W}}$ and the set of all vectors that resulting from the mapping. 

The nullspace or kernel of $\mathcal{L}$ is formally defined as:
$$\text{ker}\left(\mathcal{L}\right)=\{ \vec{v} \in \mathcal{V} : \mathcal{L}(\vec{v})= \vec{0}_{\mathcal{W}} \}$$
We also denote this as the nullspace of $\mathcal{L}$, and is given by $\mathcal{N(L)}$. 

The range of $\mathcal{L}$, also known as the image, is given by the equivalent definitions:
$$\mathcal{Im(L)}=\mathcal{R(L)}:=\{\vec{w} \in \mathcal{W} : \vec{w} = \mathcal{L}(\vec{v}) \text{ for } \vec{v} \in \mathcal{V} \}$$
$$\mathcal{R(L)}:=\{\mathcal{L(\vec{v}) : \vec{v} \in \mathcal{V}} \}$$
From these definitions we can verify that the following are subspaces:
1. $\mathcal{R(L)} \subseteq \mathcal{W}$
2. If $S \subseteq V$, then $\mathcal{R(S)}$ is a subspace of $\mathcal{W}$
3. $\mathcal{N(L)}$ is a subspace of $\mathcal{V}$

---
# Linear Transformations of a Matrix 

Matrices are a primary focus of study in linear algebra, and are examples of a linear transformation between two vector spaces. Let us consider $A \in \mathbb{R}^{m \times n} : \mathbb{R}^m \rightarrow \mathbb{R}^n$, then we can define its kernel and null space accordingly: 

$$\mathcal{R}(A):=\{A\vec{x} : \vec{x} \in \mathbb{R}^{n} \}=\mathcal{R(L}_{A})$$
$$\text{ker}\left(A\right)=\{ \vec{x} \in \mathbb{R}^n: A\vec{x} \vec{}= \vec{0}_{\mathcal{W}} \}$$We can express $\mathcal{R}(A)$, given that $A=[\vec{a}_{1},\vec{a}_{2},\cdots,\vec{a}_{n}]$ as:

$$\mathcal{R}(A)=\text{span}\{\vec{a}_{1},\vec{a}_{2},\cdots,\vec{a}_{n} \}$$
We can derive this expression using some definitions: 

$$\mathcal{R}(A)=\{A\vec{x} : \vec{x} \in \mathbb{R}^{n} \}=\sum_{i=1}^n\vec{a}_{i}\cdot x_{i}=\text{span}\{\vec{a}_{1},\vec{a}_{2},\cdots,\vec{a}_{n} \}$$
We also have the row space of $A$ which is given by $\mathcal{R}(A^T)$ as:

$$\mathcal{R}(A^T):=\{A^T\vec{x} : \vec{x} \in \mathbb{R}^{m} \}=\mathcal{R(L}_{A^T})$$
---
# [[Rank]] [[Nullity]] Theorem 

For a matrix $A \in \mathbb{R}^{m \times n}$ we define the following: 

1. $\text{rank}(A)=\text{dim}(\mathcal{R}(A))$ is the "$\textbf{column rank}$" of a given matrix, which gives the number of linearly independent columns 
2. $\text{rank}(A^T)=\text{dim}(\mathcal{R}(A^T))$ is the "$\textbf{row rank}$" of a given matrix, which gives the number of linearly independent rows. Note that 
3. $\text{dim}(\mathcal{N}(A))$ is the nullity of $A$, which is the number of columns in $A$ that are linearly dependent 
4. $\text{dim}(\mathcal{N}(A^T))$ is the nullity of $A$, which is the number of rows in $A^T$ that are linearly dependent 

We

The rank nullity theorem relates the number of columns and rows that are in their respective row space and null space to the total size of the matrix. In our matrix $A$, it follows that:

$$\text{dim}(\mathcal{R}(A))+\text{dim}(\mathcal{N}(A))=n$$
$$\text{rank}(A)+\text{nullity}(A)=n$$
Which basically tells us the total number of independent and dependent columns is equal to the total number of columns. A similar relation exists for $A^T$. 

$$\text{dim}(\mathcal{R}(A^T))+\text{dim}(\mathcal{N}(A^T))=m$$
$$\text{rank}(A)+\text{nullity}(A^T)=m$$

As well, it most be emphasized that:

$$\mathcal{R}(A)=\mathcal{R}(A^T)=r=\text{rank}(A)=\text{rank}(A^T)$$
The rank nullity theorem extends itself beyond matrix vector products and to linear transformations in general. Let us consider the vector spaces $\mathcal{V,W}$ such that $\text{dim}(\mathcal{W})=p$ and $\text{dim}(\mathcal{W})=k$ with the linear transformation $\mathcal{L: V \rightarrow W}$. 

It follows that:

$$\text{dim}(\mathcal{R(L)})+\text{dim}(\mathcal{N(L)})=\text{dim}(\mathcal{V})$$
---
Another way we can think of this is that the rank and the dimension of $N(A^T)$ is equal to the total number of columns, and the rank plus the dimension of $N(A)$ gives the number of rows. 

A matrix is said to be [[full rank]] if $\text{rank}(A)=\text{min}(n,m)$. 