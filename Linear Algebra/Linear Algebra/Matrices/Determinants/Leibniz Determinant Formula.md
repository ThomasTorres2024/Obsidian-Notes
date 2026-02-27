---
title: Leibniz Determinant Formula
tags:
  - LinearAlgebra
draft: "False"
---
# Leibniz Determinant Formula

The [[Determinant]] is a map from a matrix, $$ \large \det(A) : \mathbb{C}^{n \times n} \mapsto \mathbb{C}$$
[[Determinant]]s are linear with respect to each row, are antisymmetric, and the volume of the $n$ basis vectors is $1$. It can be shown that there is one and only one function that satisfies this result. The [[Determinant]] of a matrix we can intuitively think of as the hypervolume of a parallelepiped. 

We can describe the condition that the basis vectors have a volume of $1$ with the following notation:
$$ \large \text{vol}(e_{1},e_{2},\dots, e_{n}) = 1$$
Let us calculate the following:
$$ \large \text{vol} \begin{pmatrix}
\begin{pmatrix}
a _{11} \\ \vdots \\ a_{n_{1}}
\end{pmatrix} & \begin{pmatrix}
a _{12} \\ \vdots \\ a_{n_{12}}
\end{pmatrix} & \dots & \begin{pmatrix}
a _{1n} \\ \vdots \\ a_{nn}
\end{pmatrix}
\end{pmatrix}$$
We can simplify the notation by letting the last $n-1$ vectors by using $*$:

$$\large = \text{vol} \begin{pmatrix}
\begin{pmatrix}
a _{11} \\ \vdots \\ a_{n_{1}}
\end{pmatrix} \dots (*) 
\end{pmatrix} $$
By linearity, we can extract each each component of $$\large \begin{bmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n}
\end{bmatrix}^T$$So:
$$\large \large = \text{vol} \begin{pmatrix}
\begin{pmatrix}
a _{11} \\ \vdots \\ a_{n_{1}}
\end{pmatrix} \dots (*) 
\end{pmatrix} = \text{vol} \begin{pmatrix}
a_{11}\vec{e_{1}} + \dots + a_{n1}\vec{e_{n}} \dots, (*) 
\end{pmatrix} $$
(By linearity)
$$\large =a_{11} \cdot \text{vol}(e_{1},(*)) + \dots + a_{n_{1}} \text{vol}(e_{n},(*))$$
(Using Summation Notation)
$$ \large = \sum_{j,=1}^{n}a_{j,1} \text{vol}(\vec{e_{j,}}, (*) ) = 

\sum_{j,=1}^{n}a_{j,1} \text{vol} \begin{pmatrix}
\vec{e_{j}} & \begin{pmatrix}
a _{12} \\ \vdots \\ a_{n_{12}}
\end{pmatrix} & \dots & \begin{pmatrix}
a _{1n} \\ \vdots \\ a_{nn}
\end{pmatrix}
\end{pmatrix}$$
We can apply the same idea again and obtain the next result:
$$\large =\sum_{j_{1}=1}^{n} \sum_{j_{2}=1}^n a_{j_{1}1} a_{{j_{2}2}} \text{vol} \begin{pmatrix}
\vec{e_{j_{1}}} & \vec{e_{j_{2}}} & \begin{pmatrix}
a _{13} \\ \vdots \\ a_{n_{13}}
\end{pmatrix} & \dots & \begin{pmatrix}
a _{1n} \\ \vdots \\ a_{nn}
\end{pmatrix}
\end{pmatrix} $$
We can apply this algorithm until we have gone through all vectors in the matrix and obtain:
$$\large=\sum_{j_{i}=1}^n\sum_{j_{2}=1}^{n}\dots \sum_{j_{n}=1}^{n}a_{j_{1}1}a_{{j_{2}}2}\dots a_{j_{n}n}\cdot \text{vol}(\vec{e_{j_{1}}}, \vec{e_{j_{2}}}, \dots , \vec{e_{j_{n}}} )$$
We have successively applied the linearity property to obtain the above result. We can apply the properties of anti-symmetry and the volume of the $n$ basis vectors being $1$ to obtain the following:

$$=\sum_{j_{i}=1}^n\sum_{j_{2}=1}^{n}\dots \sum_{j_{n}=1}^{n}a_{j_{1}1}a_{{j_{2}}2}\dots a_{j_{n}n}\cdot \text{vol}(\vec{e_{j_{1}}}, \vec{e_{j_{2}}}, \dots , \vec{e_{j_{n}}}) =\begin{cases}
0 & \text{if vol linearly dependent} \\ \\
1 & \text{if vol linearly independent} 
\end{cases}$$
We can simplify our notation here by considering an $n$ tuple of entries from our set, that is we can consider some [[Permutation]] of items (this has a connection to the [[Symmetric Group]]), we denote the sum here by (note that ALL entries must be distinct in each sum of the terms):
$$\large = \sum_{(j_{1},j_{2},\dots,j_{n}) \in S_{n}} a_{j_{1}1}a_{{j_{2}}2}\dots a_{j_{n}n}\cdot \text{vol}(\vec{e_{j_{1}}}, \vec{e_{j_{2}}}, \dots , \vec{e_{j_{n}}})$$
We know that:
$$\large \text{vol}(\vec{e_{j_{1}}},\vec{e_{j_{2}}}, \dots \vec{e_{j_{n}}}) = \begin{cases}
\quad1 & \text{even number of exchanges to get this ordering}\\ 
\text{ }-1 & \text{odd number of exchanges to get this ordering}
\end{cases}$$
This is also known as the "sign" of the permutation, which is to say the sign of:
$$(j_{1},j_{2},\dots,j_{n}) \in S_{n}$$
This gives us another rewriting which is even more elegant: 
$$\large = \sum_{(j_{1},j_{2},\dots,j_{n}) \in S_{n}} a_{j_{1}1}a_{{j_{2}}2}\dots a_{j_{n}n}\cdot \text{sign}(j_{1},j_{2},\dots j_{n})$$
This at last gives us the [[Leibniz Determinant Formula]] for $A \in \mathbb{R}^{n \times n}.$
