---
title: Bilinear Forms
tags: 
draft: "false"
---
# Definition of Bilinear Form 

First we should establish what we mean by a "form". A form is a function that takes vectors from some vector spaces to scalar fields:
$$\mathcal{V}_{1}\times\mathcal{V}_{2} \times \cdots \times \mathcal{V}_{n} \rightarrow \mathbb{F}$$
We call a mapping between 1 [[vector space]] and a [[scalar field]] a one form or a co-vector. Bilinear forms involve 2 vector spaces.

For vector spaces $\mathcal{V},\mathcal{W}$ and a field $\mathbb{F}$, we can define a bilinear mapping as: $\mathcal{V} \times \mathcal{W} \rightarrow \mathbb{F}$. 

A bilinear map, $B$ is given by $B(\vec{x},\vec{y})$ where $\vec{x} \in \mathcal{V},\vec{y} \in \mathcal{W}$ and satisfies the following properties, which are equivalent to saying that $B$ is [[linear]] in both of its arguments:
$$B(\vec{x}+\vec{w},\vec{y})=B(\vec{x},\vec{y})+B(\vec{w},\vec{y}) \text{ and } B(\vec{x},\vec{y} + \vec{w})= B(\vec{x},\vec{y}) + B(\vec{x},\vec{w})$$$$B(\lambda \vec{x},\vec{w})=\lambda B(\vec{x},\vec{w}) \text{ and }B(\vec{x},\lambda\vec{w})=\lambda B( \vec{x},\vec{w})$$
This implies that for the linear functions $B$ restricted to some fixed vector $\vec{x} \in \mathcal{V}$ and $\vec{y} \in \mathcal{W}$ then we in turn get the respective linear functions: 

$$g_{\vec{v}}(\vec{w})=f(\vec{v},\vec{w})$$
$$h_{\vec{w}}(\vec{v})=f(\vec{v},\vec{w})$$

These following functions are linear when restricted to a single vector. 

The inner product is an example of a bilinear map which is defined along $\mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}$ for the vectors $\vec{v},\vec{w} \in \mathbb{R}^n$ as:

$$\vec{v}^T\vec{w}=\vec{w}^T\vec{w}$$

We can make a more general bilinear form where $\mathbb{R}^m \times \mathbb{R}^n \rightarrow \mathbb{R}$ for vectors $\vec{x} \in \mathbb{R}^m$ and $\vec{y} \in \mathbb{R}^n$ using $A \in \mathbb{R}^{m \times n}$:

$$\vec{x}^TA\vec{y}=\begin{bmatrix}x_{1} & x_{2} & \cdots &x_{m} \end{bmatrix}  \begin{bmatrix}a_{11}  & \cdots &a_{1n} \\ \vdots & & \vdots\\ 
a_{m1} & \cdots & a_{nm}\end{bmatrix} \begin{bmatrix}y_{1} \\ y_{2} \\ \vdots \\ y_{n} \end{bmatrix} $$

We can work out the matrix vector product for this and obtain the result as a sum:

$$\vec{x}^TA\vec{y}=\sum_{i=1}^n\sum_{j=1}^n a_{ij}v_{i}w_{j}$$

We can prove that this function $f(\vec{x},\vec{y})$ is linear in both arguments in two swoops:

$$f(c\cdot(\vec{x}+\vec{v}),\vec{y})=(c\cdot(\vec{x}+\vec{w}))^TA\vec{y}=c\cdot(\vec{x}^T+\vec{w}^T)A\vec{y}=c\cdot\vec{x}^TA\vec{y}+c\cdot\vec{w}^TA\vec{y}$$

$$f(\vec{x}.\vec{v}+\vec{y})=\vec{x}^TA(c\cdot(\vec{v}+\vec{y}))=c\cdot\vec{x}^TA(\vec{v}+\vec{y})=c\cdot x^TA\vec{v}+c\cdot x^TA\vec{w}$$

Thus, $f$ is linear in both arguments. 

This is considered the "canonical" form for a Bilinear Form. The dot product is simply given when $A=I_{n}$  We are able to prove this result as well.

---
# Proof of the Canonical form of the Bilinear Form

Given any vector spaces $\mathcal{V}$ and $\mathcal{W}$ over field $\mathbb{F}$ with respective bases $\{\vec{v}_{1}, \cdots \vec{v}_{m} \}$ and $\{\vec{w}_{1}, \cdots \vec{w}_{n} \}$, if $\mathcal{V} \times \mathcal{W} \rightarrow \mathbb{F}$ is a bilinear form then there exists a unique matrix $A \in \mathbb{F}^{m \times n}$ such that $f(\vec{v},\vec{w})=\vec{v}^TA\vec{w}$ yields a scalar. 

---
# Metric Tensors 

Metric tensors are bilinear forms that satisfy properties of [[similarity]] and [[p[ositive definite]]ness for a vector $\vec{v}$. Metric tensors are also symmetric. That is to say: 

$$g(\vec{v},\vec{w})=g(\vec{w},\vec{v})$$

$$g(\vec{v},\vec{v}) = \| \vec{v} \|^2 \geq 0$$