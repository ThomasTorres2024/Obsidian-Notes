---
title: Tensor Product
tags:
  - LinearAlgebra
draft: "False"
---
# Tensor Product 
The [[Tensor Product]] takes two [[Vector Space]]s, $U,V$ and produces a third vector space $W$ from the preceding 2. Here we denote the [[Tensor Product]] between $2$ vector spaces by $U \otimes V$. 

If we have $\text{dim}(U)=n,\text{dim(V)}=m$ and $u,v \in \mathbb{N}$ then $\text{dim}(W)=mn$ for $W=U \otimes V$. We also expect that for $x \in U$ and $y \in V$ that there is some corresponding "product" that preserves linearity, such that  for $z=x \otimes y$ that there is a linear correspondence where:

$$(\alpha x_{1} + \alpha_{2} x_{2}) \otimes y = \alpha_{1}(x_{1} \otimes y_{1}) + \alpha_{2} (x_{2} \otimes y_{2} ) $$
And a similar result should also hold for $x \otimes (\alpha_{1}y_{1} +\alpha_{2}y_{2})$, which is to say that $x \otimes y$ should form a bilinear vector valued function of $x$ and $y$. 

Furthermore if $u,v$ are linear functionals on $U$ and $V$ respectively, then their product, $w$, $w(x,y)=u(x)v(y)$, should be some "general element" of the [[Dual Space]] $(U \otimes V)'$. 

To technically describe [[Tensor Product]]s it is useful to describe them indirectly as the [[Dual Space]] of another space. 

Also, a [[Tensor]] is simple an element of a [[Tensor Product]]. 

---
# Extension From the [[Formal Product]] 

The [[Formal Product]] of two [[Vector Space]]s $V,W$ denoted by $V*W$ is the following set:
$$V*W= \text{span} \{ v * w : v \in V, w \in W \}$$
And there is no relation between the symbols $v,w$. 

We would like the properties of factoring scalars (that the formal product is a [[Bilinear Form]]) and distributivity to hold. This will give us the following properties where $*$ still denotes the formal product between vectors of their respective vector space:
$$(v_{1}+v_{2})*w = v_{1}*w+v_{2}*w$$
$$(cv)*w = c(v*w)$$
$$v*(cw)=c(v*w)$$
One way that we can create a [[Vector Space]] with such properties is via a [[Quotient Vector Space]]. Let us consider the following [[Vector Space]] that we quotient out by:

$$I= \text{span} \begin{cases}
(cv) *w - c(v*w) & c \in \mathbb{R} \\ 
v*(cw)-c(v*w) & v \in V \\
(v_{1}+v_{2})*w - (v_{1}*w+v_{2}*w) & w \in W
\end{cases}$$
Then we can define the following product: 

$$V \otimes W = V * \frac{W}{I}$$
Here we can show that $V* \frac{W}{I}$ has a "nice structure" preserving the multiplicative properties that we want. Thus:

$$\begin{align}
(cv) \otimes w = (cv)*w + I \\
=(cv)*w + (c(v*w) - (cv)*w )+I
\end{align}$$
Here $c(v*w)-(cv)*w \in I$ and is equal to $0$ wrt $I$. But notice that: 

$$=c(v*w)+I=c(v \otimes w)+I$$
Since the $(cv)*w$ and $-(cv)*w$ cancels. 

---
### Definition [[Tensor Product]]
The [[Tensor Product]] between finite vector spaces $U,V$ is the dual of the vector space of all [[Bilinear Form]] on $U \oplus V$. For $x \in U$ and $y \in V$ we have that $z=x \otimes y$ is the element $z \in U \otimes V$ such that $z(w)=w(x,y)$ for every [[Bilinear Form]] $w$. 

This is a quick rigorous definition that ensures that the dimension of the resulting [[Vector Space]] is multiplicative, and that the tensor product is linear. 

Another approach to the [[Tensor Product]] is the set of all symbols of the following form for $U \otimes V$:
$$U \otimes V = \sum_{i} \alpha_{i}(x_{i} \oplus y_{i})$$
This conforms to the bilinearity and multiplicativity of the resulting vector spaces.

The particular disadvantages of these definitions is that they are not able to adequately extend these objects to infinite dimension vector spaces and to [[Module]]s. 

---
# (Theorem) Basis of a Tensor Product 
If $B_{v}=\{v_{1},v_{2},\cdots, v_{n} \}$ and $B_{w}=\{w_{1},w_{2},\cdots, v_{n} \}$ then $B_{V \otimes W}$ is:

$$B_{V \otimes W} = \{ v_{i} \otimes w_{j} : 1 \leq i \leq m, 1 \leq j \leq n \}$$
So $\text{dim}(v \otimes w)=(\text{dim }V)(\text{dim }W)$. (We can also think of this as another way to construct a new vector space such that we get one with the dimensions that are multiplying the size of the vector spaces, where as the Direct Sum adds dimensions). 

We can prove that the $V \otimes W$ is a finite linear combination of elements of the form $v \otimes w$ with $v \in V$ and $w \in W$. Here for $v \in V$ and $w \in W$:

$$v= \sum_{i=1}^m a_{i}v_{i} \quad w= \sum_{j=1}^n b_{j}v_{j}$$
Thus:
$$v \otimes w = \left( \sum_{i=1}^m a_{i}v_{i}  \right) \otimes w = \sum_{i=1}^m a_{i}(v_{i} \otimes w )$$
The last equality is a result of the properties of the [[Quotient Vector Space]] that we defined the [[Tensor Product]] as being distributive. 
$$\sum_{i=1}^m a_{i}\left( v_{i} \otimes \sum_{j=1}^n b_{j}v_{j} \right) = \sum_{i=1}^m  \sum_{j=1}^n  a_{i}b_{j} (v_{i} \otimes w_{j})$$
Thus it spans the set. 

---
# Examples 
### Example 1 - Functions
Let $U$ be the set of all polynomials of the variable $s$ and the coefficients be in $\mathbb{C}$, and let $V$ be the set of all polynomials in variable $t$, and let $W$ be the set of all polynomials in the two variables, $s,t$. Clearly, $U,V,W$ are all complex [[Vector Space]]s. We would like to define $W$ here as the [[Tensor Product]] between $U$ and $V$, and the product of any polynomial $x(s) \in U, y(t) \in V$, we would have some $z(s,t) \in W$ such that $z(s,t) =x(s)y(t)$. 

### Example Basis for $\mathbb{R}^2 \otimes \mathbb{R}^3$:
$$\mathbb{R}^2 \otimes \mathbb{R}^3 = \text{span} \left\{ \begin{bmatrix}
1 \\ 0 \end{bmatrix} \otimes \begin{bmatrix}
1 \\ 0 \\ 0 \end{bmatrix} , \begin{bmatrix}
1 \\ 0 \end{bmatrix} \otimes \begin{bmatrix}
0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix}
1 \\ 0 \end{bmatrix} \otimes \begin{bmatrix}
0 \\ 0 \\ 1 \end{bmatrix}, \begin{bmatrix}
0 \\ 1 \end{bmatrix} \otimes \begin{bmatrix}
1 \\ 1 \\ 0 \end{bmatrix} , \begin{bmatrix}
0 \\ 1 \end{bmatrix} \otimes \begin{bmatrix}
0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix}
0 \\ 1 \end{bmatrix} \otimes \begin{bmatrix}
0 \\ 0 \\ 1 \end{bmatrix},  \right\}$$
Note that this and $\mathbb{R}^{2 \times 3}$ and $\mathbb{R}^{6}$ are all Isomorphic Vector Spaces since their Dimension is equivalent and this is the only requirement for isomorphism. 