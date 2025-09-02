---
title: Isomorphic Vector Spaces
tags: 
draft: "false"
---
# Isomorphic Vector Space Introduction

Let us consider the following vector spaces: 

1. $\mathbb{R}^{2 \times 2}$ with associated basis: $\left\{ \begin{bmatrix} 1&0\\0&0 \end{bmatrix},\begin{bmatrix} 0&1\\0&0 \end{bmatrix}, \begin{bmatrix} 0&0\\1&0 \end{bmatrix}, \begin{bmatrix} 0&0\\0&1 \end{bmatrix} \right\}$
2. The polynomial space $\mathcal{P}^{3}$ with basis $\{1,x,x^2,x^3 \}$
3. $\mathbb{R}^4$ with basis $\{\vec{e}_{1},\vec{e}_{2},\vec{e}_{3},\vec{e}_{4} \}$

These are all dimension 4 vector spaces defined over the reals. There are a lot of properties that this different vector spaces don't have despite the four having the same dimension. 

Matrices have determinants and polynomials do not, polynomials have degree as well while vectors and matrices do not. These are very clearly different objects, and we should not expect that operations performed on one of these subspaces lines up with the operations that occur on another subspace. 

For example, let us consider $(x+1)(x+1)=x^2+2x+1$ which represents a product of $(1\cdot1 + 1 \cdot x)^2$ from the polynomial space $\mathcal{P}^3$ which corresponds to the basis vectors of $p_{1}$ and $p_{2}$.

Let us also consider $\left(\begin{bmatrix} 1&1\\0&0 \end{bmatrix} \cdot \begin{bmatrix} 1&1\\0&0 \end{bmatrix}=\begin{bmatrix} 1&1\\0&0 \end{bmatrix}\right)$ which comes from $\mathbb{R}^{2 \times 2}$ which represents a sum of the first two basis vectors and their product. It is clearly not equal to $r_{1}+2r_{2}+r_{3}$ but instead is equal to $r_{1}+r_{2}$. 

We would hope that these operations represent the same vectors across different vector spaces, however they clearly differ.  

---
# Isomorphic Vector Spaces Definition 

Given a linear transformation $T : \mathcal{V} \rightarrow \mathcal{W}$ on vector spaces $\mathcal{V,W}$ over the field $\mathbb{F}$, we can say that $\mathcal{V}$ and $\mathcal{W}$ are isomorphic if $T$ is invertible. 

We can call the vector spaces isomorphic given the condition of an invertible $T$ since $\mathcal{V}$ and $\mathcal{W}$ are vector spaces, and $T$ is a bijection between spaces since it is invertible. All we are doing is naming a valid bijection and enforcing that the resulting domain and range of our transformation are both vector spaces to achieve the isomorphism property. 

Let us consider $T : \mathbb{R}^{2 \times 2} \rightarrow \mathcal{P}^3:$ where we can define $T$ and $T^{-1}$ on the basis of each set respectively: 

$$ T \left(\begin{bmatrix} 1&0\\0&0 \end{bmatrix} \right)=1, \text{   } T^{-1}(1)=\begin{bmatrix} 1&0\\0&0 \end{bmatrix}$$$$T \left(\begin{bmatrix} 0&1\\0&0 \end{bmatrix} \right)=x, \text{   } T^{-1}(x)=\begin{bmatrix} 0&1\\0&0 \end{bmatrix}$$$$ T \left(\begin{bmatrix} 0&0\\1&0 \end{bmatrix} \right)=x^2, \text{   } T^{-1}(x^2)=\begin{bmatrix} 0&0\\1&0 \end{bmatrix}$$
$$T \left(\begin{bmatrix} 0&0\\0&1 \end{bmatrix} \right) = x^3, \text{   } T^{-1}(x^3)=\begin{bmatrix} 0&0\\0&1 \end{bmatrix} $$

More generally we can represent: 

$$T \left(\begin{bmatrix} a&b\\c&d \end{bmatrix} \right) = a+bx+cx^2+dx^3$$
and 

$$T^{-1}(a+bx+cx^2+dx^3)=\begin{bmatrix} a&b\\c&d \end{bmatrix}$$
---
# An Isomorphism is an Equivalence Relation 

For an isomorphism to be an equivalence relation it must be, reflexive, symmetric and transitive. We will denote an isomorphism by "$\equiv$", and consider the vector spaces of dimension $n$ $\mathcal{V},\mathcal{W},\mathcal{Z}$.

The isomorphism therefore must satisfy: 

1. Reflexivity: $\mathcal{V} \equiv \mathcal{V}$
2. Symmetry: $\mathcal{V}\equiv \mathcal{W} \implies \mathcal{W} \equiv \mathcal{V}$
3. Transitivity: $\mathcal{V}\equiv \mathcal{W} \text{ and }\mathcal{W} \equiv \mathcal{Z} \implies \mathcal{V} \equiv \mathcal{Z}$

#### 1. Reflexivity 
Consider the identity function $I_{\vec{v}}(\vec{x})=\vec{x}$. This function maps an input to itself. The function is also invertible because it is its own inverse. 

Thus, we are able to map $\mathcal{V}$ onto itself, and can conclude that isomorphisms are reflexive since we have named an appropriate linear transformation. 

#### 2. Symmetry 
Since we are given that $\mathcal{V} \equiv \mathcal{W}$ then it follows that $\exists T : \mathcal{V} \rightarrow \mathcal{W}$ such that $T$ is invertible. We are able to name an invertible function that maps $\mathcal{W} \rightarrow \mathcal{V}$, namely $T^{-1}$ which has an inverse of $(T^{-1})^{-1}=T$. 

Thus, $\mathcal{W} \equiv \mathcal{V}$,  Isomorphisms are symmetric since  $\mathcal{V}\equiv \mathcal{W} \implies \mathcal{W} \equiv \mathcal{V}$.

#### 2. Transitivity 
We are given that $\mathcal{V}\equiv \mathcal{W} \text{ and }\mathcal{W} \equiv \mathcal{Z}$, which implies that there exists $\exists T : \mathcal{V} \rightarrow \mathcal{W}$  and $\exists G : \mathcal{W} \rightarrow \mathcal{Z}$  where $T$ and $G$ are each invertible. 

We can find an invertible transformation between $\mathcal{V} \rightarrow \mathcal{Z}$ by taking the composition of $T$ and $G$:
$G \circ T : \mathcal{V} \rightarrow \mathcal{Z}$ which has inverse $T^{-1} \circ G^{-1}$. 

Since we have named an invertible mapping, we can conclude that $\mathcal{V} \equiv \mathcal{Z}$. In conclusion, Isomorphisms are transitive. 

In conclusion since we have shown reflexivity, symmetry, and transitivity, then it follows that isomorphisms are an equivalence relation.

---
# Conditions for Isomorphic Vector Spaces 

Isomorphic vector spaces simply need to have the same dimension in order to be isomorphic. We can do this by considering some vector space $\mathcal{V}$ which has dimension $n$ and then finding an invertible linear transformation between itself and $\mathbb{F}^n$. 

We will denote the basis of $\mathcal{V}$ by $V = \{\vec{v}_{1},\vec{v}_{2}, \cdots, \vec{v}_{n} \}$. 

The transformation $T : \mathcal{V} \rightarrow \mathbb{F}^n$ can be denoted as $f(\vec{v}_{i})=\vec{e}_{i}$ where we map the $i$th basis vector of $\mathcal{V}$ to the $i$th basis vector of $\mathbb{F}^n$. 

Likewise, the inverse of $T$ is given by: $T^{-1} : \mathbb{F}^n \rightarrow \mathcal{V}$ and is defined as $f^{-1}(\vec{e}_{i}) = \vec{v}_{i}$ which simply maps the basis vectors from the field space to the basis vectors of the other vector space. 

## Corollary 
As a corollary, if dim$(\mathcal{V}) =$ dim$(\mathcal{W})$ and both vector spaces are of finite dimension, then it follows from the fact that vector space isomorphisms are an equivalence relation, that $\mathcal{V} \equiv \mathcal{W}$. 

That is to say: $\mathcal{V} \equiv \mathcal{W} \Longleftrightarrow \text{dim}(\mathcal{V})=\text{dim}(\mathcal{W})$

This comes straight from the transitive property, since in our previous theorem we showed that $\mathcal{V} \equiv \mathbb{F}^n$ and $\mathbb{F}^n \equiv \mathcal{W}$ then $\mathcal{V} \equiv \mathcal{W}$.

We can formally  prove this fact: 

##### 1.) $\mathcal{V} \equiv \mathcal{W} \implies \text{dim}(\mathcal{V})=\text{dim}(\mathcal{W})$
Suppose dim($\mathcal{V})$=n and dim($\mathcal{W}$)=m. Since $\mathcal{V} \equiv \mathcal{W}$ $\exists T: \mathcal{V} \rightarrow \mathcal{W}$ that is also invertible. 

In order to have such a transformation, we need to have equivalent dimension in both $\mathcal{V}$ and $\mathcal{W}$, so it follows that the dimension of both spaces is equivalent. 

##### 2.) $\mathcal{V} \equiv \mathcal{W} \Longleftarrow \text{dim}(\mathcal{V})=\text{dim}(\mathcal{W})$
Since $\mathcal{V}$ and $\mathcal{W}$ have equal dimension, and their dimension is $n$ we can see that both $\mathcal{V}$ and $\mathcal{W}$ are respectively isomorphic to $\mathbb{F}^n$, which then by the transitivity property entails that both $\mathcal{V} \equiv \mathcal{W}$. 

Since we have showed 1.) and 2.) we can conclude that in order for vector spaces to be isomorphic they must have the same dimension. 

---
### Note about Dimensions of $\mathbb{C}^n$ on different ground fields 

If we select the reals for $\mathbb{C}^n$, then we will require $2n$ many dimensions to provide a basis for $\mathbb{C}^n$, since we have to represent the imaginary and real axes separately. However if we chose the complex numbers, we would could represent it in $n$ instead.  