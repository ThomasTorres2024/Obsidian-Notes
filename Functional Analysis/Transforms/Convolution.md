---
title: Convolution
tags:
draft: "False"
---
# Convolution Overview 
[[Convolution]] is used extensively in signal processing and in [[Convolutional Neural Networks]] for image processing. [[Convolution]] also connects to the [[Fourier Transform]] of a function. 

To describe [[Convolution]], we can use a [[Toeplitz Matrix]], and to describe  [[Cyclic Convolution]] we use a [[Circulant Matrices]] (which are [[Toeplitz Matrix]], but have the property of being cyclic and forming their own [[Group]]). 

---
# Acyclic [[Convolution]]

The discrete version of [[Convolution]] for 2 given vectors $c,d \in \mathbb{F}^n$ is given as follows:
$$(c \times d)_{k}=\sum_{i,j : i+j=k} c_{j}d_{j}=\sum_{i=1} c_{i}d_{k-i}$$
The general rule for this is that the indices of $i$ and $j$ should add to $k$, which we can reduce to a single variable by the expression on the right. We can extend this to continuous functions by considering the continuous functions $f(x),g(x)$ and convolving them:
$$f(x) * g(x) = (f * g)(x)$$
The discrete cases asks us for $k$, however the continuous case asks us for when both $f$ and $g$ are at $x$. The analog for the continuous cause is to use integration instead of summation:
$$(f*g)(t)=\int_{-\infty}^\infty f(x)g(t-x)dx$$
Here, there is a correspondence with the discrete variant, namely $x$ corresponds to $i$, and $t$ corresponds to $j$. $t$ is the amount of shift that we are applying to our functions. We may want to apply [[Cyclic Convolution]] if $f$ and $g$ are both periodic functions, say if $f$ and $g$ are sinusoidal. 

---
# Cyclic [[Convolution]]
If we have some [[Group]], $G$ and some $x,y \in G$, and we want $x * y \in G$ as well, we consider [[Cyclic Convolution]]. In the discrete case, we modify our formulas to remain cyclic by doing the following:
$$(c \times d)_{k}=\sum_{i+j=k \text{ mod}(n)} c_{j}d_{j}=\sum_{i=1}^{n-1} c_{i}d_{k-i}$$
---
# Multivariable [[Convolution]]
(I got the notes on convolution from # Lecture 32: ImageNet is a Convolutional Neural Network (CNN), The Convolution Rule, I honestly don't understand this particular section very well, I haven't learned about Fourier Analysis formally, so it's a mishmash of stuff. I added the Kronecker notes because I've encountered them before, but I really am confused by this, Strang was quite brief and fast here, I think)

In the case of a multivariable [[Convolution]], we opt to use a double integral instead of a single integral, since we are shifting two functions down now by the parameters of $t$ and $u$. Let us consider the functions $f(x,y), g(x,y)$, then the [[Convolution]] can be written as:
$$\iint_{t,u} f(t,u)g(x-t,y-u) \text{ } dudt$$
Generally here, the idea is the same overall. In two dimensions, we need to be able to apply some process to two matrices, $A,B \in \mathbb{R}^{n \times n}$ such that we obtain some $K \in \mathbb{R}^{n^2 \times n^2}$. The way this is handled is by the [[Kronecker Product]]. The [[Kronecker Product]] is handled by:
$$K=\text{Kron}(A,B)= 
A \otimes B =
\begin{bmatrix}
a_{11}b_{11} & a_{11}b_{12} & \cdots & a_{11}b_{1q} & \cdots & a_{1n}b_{11} & a_{1n}b_{12} & \cdots & a_{1n}b_{1q} \\
a_{11}b_{21} & a_{11}b_{22} & \cdots & a_{11}b_{2q} & \cdots & a_{1n}b_{21} & a_{1n}b_{22} & \cdots & a_{1n}b_{2q} \\
\vdots & \vdots & \ddots & \vdots &  & \vdots & \vdots & \ddots & \vdots \\
a_{11}b_{p1} & a_{11}b_{p2} & \cdots & a_{11}b_{pq} & \cdots & a_{1n}b_{p1} & a_{1n}b_{p2} & \cdots & a_{1n}b_{pq} \\
\vdots & \vdots &  & \vdots & \ddots & \vdots & \vdots &  & \vdots \\
a_{m1}b_{11} & a_{m1}b_{12} & \cdots & a_{m1}b_{1q} & \cdots & a_{mn}b_{11} & a_{mn}b_{12} & \cdots & a_{mn}b_{1q} \\
a_{m1}b_{21} & a_{m1}b_{22} & \cdots & a_{m1}b_{2q} & \cdots & a_{mn}b_{21} & a_{mn}b_{22} & \cdots & a_{mn}b_{2q} \\
\vdots & \vdots & \ddots & \vdots &  & \vdots & \vdots & \ddots & \vdots \\
a_{m1}b_{p1} & a_{m1}b_{p2} & \cdots & a_{m1}b_{pq} & \cdots & a_{mn}b_{p1} & a_{mn}b_{p2} & \cdots & a_{mn}b_{pq}
\end{bmatrix}

$$

For a two dimensional [[Fourier Transform]], we would 

---
# Convolution Rule 
The Convolution Rule is a rule between [[Matrix Multiplication]] of [[Circulant Matrices]] and [[Convolution]]. We can eloquently write this rule as, convolving by transforming by $F$ first and then convolving, or convolving first, and then transforming by $F$. 

Let us consider some [[Cyclic Convolution]] between $C,D$, and then the matrix $F$ which consists of the [[eigen vectors]] of the [[Circulant Matrices]] of size $n \times n$. Then we can argue that:
$$F(c \otimes d)=F(c) \odot F(d)$$
The "$\odot$" here denotes the [[Hadamard Product]], which is the component wise multiplication of two vectors: $\odot : \mathbb{R}^{n} \times \mathbb{R}^{n} \mapsto \mathbb{R}^n$  

As an aside, this entails that [[Convolution]] is a [[Linear Transformation]]. When we compute $C \times D$, because [[Circulant Matrices]] form a [[Group]] that is closed under [[Matrix Multiplication]], it follows that we have a new circulant matrix. (Somehow) It turns out that the diagonals of $CD$ actually come from $c \otimes d$. 

If we look at $CD$, we know that $CD$ is [[unitarily diagonalizable]] since $CD$ is normal. Furthermore we know that all circulant matrices of degree $n$ have the same [[eigen vectors]], so we can write that $C=X\Lambda_{1} X^H, D=X \Lambda_{2} X^H$ so:
$$CD=X\Lambda_{1} X^HX \Lambda_{2} X^H=X \Lambda_{1}\Lambda_{2}X^H$$
So, the eigenvalues of $CD$ are actually just the product of the eigen values of $C$ and the product of the eigen values of $D$. 

We can use this fact to our advantage. Since we know that $F(c \otimes d)$ gives the set of eigen vectors of the convolution, but we know that the eigen values of $CD$ can be obtained from computing the eigen values of $C$ and then the eigen values of $D$ separately, we can express it as:
$$F(c \otimes d) = (Fc) \odot F(d)$$
This proof is reliant upon the fact that the eigen vectors for $C$ and $D$ and for that matter all degree $n$ [[Circulant Matrices]] is equivalent. 

This rule is quite nice since we can actually compute a [[Faster Fourier Transform]] quite quickly. We can examine the computational cost of each operation here. In order to compute $F(c \otimes d)$, we need to do a computation on the scale of $N\log(N)+N^2$. The convolution process between $c$ and $d$ takes $O(n^2)$. And the [[Faster Fourier Transform]] takes $n\log(n) \implies$  the method here is of time complexity $O(n^2$.

If we consider the cost of $(Fc) \odot (Fd)$, we do 2 [[Faster Fourier Transform]]s, and then a Hadamard product. This is pretty cheap resulting in: $2n\log(n)+ n$ This gives us a time complexity of $O(n\log(n))$. Obviously, this operation is significantly quicker