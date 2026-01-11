---
title: Linear Forms
tags: 
draft: "false"
---
# Definition of a Linear Form 
A [[linear]] form is a mapping from $\mathcal{V} \rightarrow \mathbb{F}$ where $\mathcal{V}$ is a vector space and $\mathbb{F}$ is the associated field, which is either the real or complex numbers. 

Any linear form is given by some $f_{\vec{v}}(\vec{w})=\vec{v}^H\vec{w}$

Linear forms are [[Linear Transformation]]. We can verify this below: 

$$f_{v}(c \cdot(\vec{w}+\vec{u}))=\vec{v}^H(c \cdot(\vec{w}+\vec{u}))=\vec{v}^H(c \cdot\vec{w})+\vec{v}^H(c \cdot\vec{u})=c\vec{v}^H\vec{w}+c\vec{v}^H\vec{u}=cf_{\vec{v}}(\vec{w})+cf_{\vec{v}}(\vec{u})$$

In conclusion, $f_{v}$ is a linear transformation since it satisfies the properties of linearity. 

---
# Examples of Linear Forms 
Linear forms take on a wide number of forms. They are ubiquitous. For example consider: 
#### 1.) [[Integral]] map $F:\mathcal{P}_{3} \rightarrow \mathbb{R}$: where $g(x) \in \mathcal{P}_{3}$
$$F(g(x))=\int_{0}^{1}g(x)dx$$
$F$ can be shown to be linear:  
$$F(c \cdot(g(x)+f(x)))=\int_{0}^{1}(g(x)+f(x))dx=c \cdot \int_{0}^{1}g(x)dx + c \cdot \int_{0}^{1}f(x)dx = c \cdot F(g(x)) + c\cdot F(f(x))$$

#### 2.) Evaluation of a Polynomial at $x=3$, $E_{3} : \mathcal{P}_{3} \rightarrow \mathbb{R}$ for $g(x) \in \mathcal{P}_{3}$

$$E_{3}(g(x))=g(3)$$
$E_{3}$ can be shown to be linear:

$$E_{3}(c \cdot (f(x)+g(x)))=c(f(3)+g(3))=c \cdot f(3)+ c \cdot g(3)=c\cdot E_{3}(f(x))+c\cdot E_{3}(g(x))$$
#### 3.) [[Trace]] of a Matrix $\mathbb{C}^{n \times m} \rightarrow \mathbb{C}, A,B \in \mathbb{C}^{n \times m}$

$$\text{Tr}(A)=\sum_{i=1}^{\text{min(n,m)}}A_{ii}$$
$\text{Tr}$ can be shown to be linear: 

$$Tr(c(A+B))=\sum_{i=1}^{\text{min(n,m)}}(cA_{ii}+cB_{ii})=c\sum_{i=1}^{\text{min(n,m)}}(A_{ii})+c\sum_{i=1}^{\text{min(n,m)}}(B_{ii})=c\cdot \text{Tr}(A)+c\cdot \text{Tr}(B)$$
---

# Theorem, All Linear Forms are a "[[Dot Product]]"

For a finite dimensional $\mathcal{V}$ over a field $\mathbb{F}$, with a basis $B$, given a linear form $f:\mathcal{V} \rightarrow \mathbb{F}$, then $\exists! \vec{v}$ such that: 

$$f_{\vec{v}}(\vec{w})=\vec{v}^H\vec{w}$$
Which in English means that we can describe the linear form as an inner product between $\vec{v}$ and $\vec{w}$ 

We can essentially force the the resulting expression to yield a scalar. The way I personally like to think of this map is by evaluating some kind of linear function given some parameter list, which we just neatly describe with matrix notation or summation notation. 

In terms of matrix algebra, we want our $\vec{v}^H$ to have a size of $(1 \times n)$ and $\vec{w}$ to have a size of $(n \times 1)$
The resulting size of this matrix is $1 \times 1$ which is clearly a scalar. 

Just to make this super explicit: 

$$f_{\vec{v}}(\vec{w})=\vec{v}^H\vec{w}=\begin{bmatrix}\bar{w_{1}}\\ \bar{w_{2}} \\\vdots \\ \bar{w_{n}} \end{bmatrix} \cdot \begin{bmatrix}{v_{1}} & {v_{2}} &\cdots & {v_{n}} \end{bmatrix} = \sum_{i=1}^n \bar{w_{i}}v_{1}$$
---

# Determining Vectors that Cause Linear Transformations
For each linear transformation above, we will determine the associated vector to describe each linear form: 

#### 1.) Linear Form of Integral Function, $F(g(x))$:

If we assume that the 1 index of a vector corresponds to a constant degree polynomial, then we can consider integration to be: 

$$f_{\vec{v}}(\vec{w})=\begin{bmatrix} 1 & \frac{1}{2} & \frac{1}{3} & \frac{1}{4}\end{bmatrix}\cdot\vec{w}$$
#### 2.) Evaluation of a polynomial, $p(x)$ at $x=3$:

$$E_{3}(\vec{p)}=\vec{v}^H\vec{p}=\begin{bmatrix} 1 & 3 & 9 & 27\end{bmatrix} \cdot \vec{p}$$---
# Linear Forms Form a Vector Space 
This result is important for [[Dual Spaces]], and allow us to argue that the dual space is a valid [[Vector Space]]. Consider linear forms $f,g$ that perform $\mathcal{V} \rightarrow \mathbb{F}$. It follows that: 

$$(f+g)(c\vec{x}+c\vec{y})=f(c\vec{x} + c\vec{y})+g(c\vec{x}+c\vec{y})=cf(\vec{x}) +cf(\vec{y})+cg(\vec{x})+cg(\vec{y})$$
$$=c\cdot f(\vec{x}+\vec{y}) + c\cdot g(\vec{x}+\vec{y})$$
In conclusion $(f+g)$ is linear and implies that linear forms constitute a vector space. 