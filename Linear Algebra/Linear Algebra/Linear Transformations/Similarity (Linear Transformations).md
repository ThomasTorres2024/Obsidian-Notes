---
title: Similarity
tags:
  - LinearAlgebra
draft: "False"
---
# Similarity 
The definition of similarity arises from the following questions.

1. If $B$ is a [[Linear Transformation]] on $V$, what is the relationship between the matrix $(\beta_{ij})$ with respect to $\mathcal{X}=\{ x_{1},x_{2},\ldots,x_{n} \}$ and $\mathcal{Y}=\{y_{1},y_{2},\ldots,y_{n}\}$ with the matrix $(\gamma_{ij})$. 
2. If $(\beta_{ij})$ is a matrix, what is the relationship between the linear transformations $B,C$ defined respectively by $Bx_{j}=\sum_{i} \beta_{ij}x_{i}$ and $Cy_{j}=\sum_{i}(\beta_{ij})y_{i}$

In order to answer question $1$ consider the matrix $(a_{ij})$ with the associated linear transformation $A$ such that $Ax_{j}=y_{j}$ (see change of basis section in Linear Transformations). 

Now we can express the following:
$$\begin{align}
Bx_{j}=\sum_{i} \beta_{ij}x_{i} \\
By_{j}=\sum_{i}\gamma_{ij}y_{i}
\end{align}$$
Using the definition for the linear transformation $A$ we can actually express the following:
$$\begin{align}
By_{j}=BAx_{j}=B\left( \sum_{k} \alpha_{kj}x_{k}  \right) \\
= \sum_{k} \alpha_{kj}Bx_{k}=\sum_{k} \alpha_{kj} \sum_{i} \beta_{ik}x_{i} =\sum_{i}\left( \sum_{k} \beta_{ik}\alpha_{kj} \right)x_{i}
\end{align}$$
And likewise:
$$\begin{align}
By_{j}=\sum_{k} \gamma_{kj}y_{k}=\sum_{k}\gamma_{kj}Ax_{k}=\sum_{k} \gamma_{kj} \sum_{i} \alpha_{ik} x_{i} \\
= \sum_{i} \left( \sum_{k} \alpha_{ik} \gamma_{kj} \right)x_{i}
\end{align}
$$
Since both of these are equivalent we obtain the following:
$$\sum_{k} \alpha_{ik} \gamma_{kj} = \sum_{k} \beta_{ik} \alpha_{kj} \iff A \cdot C = B \cdot A$$
We can write these in [[Matrix]] form, but it is important to note that $A,B$ are written as linear transformations with respect to the basis $\mathcal{X}$ whereas $C$ is written with respect to the basis $\mathcal{Y}$, which makes writing them tricky. However, if we know $A,B$ we can express $C$ in the following form assuming that $A$ is an invertible linear transformation:
$$C=A^{-1}BA$$

From this idea of [[Similarity (Linear Transformations)]], we get [[Similar Matrices]] when we associate our [[Linear Transformation]]s with some [[Matrix]]. 

In order to answer the second question, we need to observe the following:
$$Cy_{j}=CAx_{j}$$ and:
$$\sum_{i}\beta_{ij}y_{i} = \sum_{i} \beta_{ij} Ax_{i} =A\left(  \sum_{i} \beta_{ij} x_{i}  \right) =ABx_{j} $$
(I don't know how, maybe this is some property that we necessarily want for $C$ since we are interested in similarity? that's my guess anyway) this somehow leads to the following:
$$CAx_{j} =ABx_{j}$$
And after this its fairly straight forward:
$$\iff  C=ABA^{-1}$$

---
