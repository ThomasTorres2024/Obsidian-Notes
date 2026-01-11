---
title: Vandermonde Matrix
tags:
draft: "False"
---
# Vandermonde Matrix 
The [[Vandermonde Matrix]] is formed from a set of points $\mathcal{D}=\{(x_1,y_1,),(x_2,y_2),\dots (x_n,y_n) \}$ such that we put all of the $y$ values in a vector $\vec{y}=[y_1,y_2,y_3,\dots, y_n]$ and we encode all of the $x_1$ and their corresponding values to the $n$th degree in order to provide a solution to [[Least Squares]], for instance:

Let $V$ be the [[Vandermonde Matrix]]:

$$ V= \begin{bmatrix} t_{1}^n & \cdots & t_{1}^3 & t_{1}^2 & t_{1} &1 \\ t_{2}^n & \cdots & t_{2}^3 &  t_{2}^2 & t_{2} & 1\\ t_{3}^n & \cdots & t_{3}^3 & t_{3}^2 & t_{3} & 1 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ t_{n}^n & \cdots &t_{n}^3 & t_{n}^2 & t_{n} & 1 \end{bmatrix} $$
It can be proved that the [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] of $V, \det(V)\neq0$. Since any polynomial can be defined by passing through $n$ distinct points, we can find a unique polynomial of degree $n-1$ that fits through all of the given points. We set up the following equations we are looking to minimize as:

$$ \left\|\begin{bmatrix} t_{1}^n & \cdots & t_{1}^3 & t_{1}^2 & t_{1} &1 \\ t_{2}^n & \cdots & t_{2}^3 &  t_{2}^2 & t_{2} & 1\\ t_{3}^n & \cdots & t_{3}^3 & t_{3}^2 & t_{3} & 1 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ t_{n}^n & \cdots &t_{n}^3 & t_{n}^2 & t_{n} & 1 \end{bmatrix} \cdot \begin{bmatrix} \alpha_{3} \\ \alpha_{2} \\\alpha_{1} \\ \beta \end{bmatrix}  -\begin{bmatrix} y_{1} \\ y_{2} \\ y_{3}  \\ \vdots \\ y_{n}  \end{bmatrix}\right\|^2=\|V\vec{x}-\vec{b} \|^2 = \| \vec{\epsilon} \|^2=\vec{\epsilon}^T\vec{\epsilon}$$
If $\det(V) \neq 0 \implies$ that we can easily find our set of coefficients for the polynomial by computing:
$$\vec{x}=V^{-1}\vec{b}$$
We can show that the [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] of $V$ is given by:
$$\det(V)=\prod_{0 \leq i < j}^n(x_j-x_i)$$$$=[(a_n-a_1)(a_n-a_2)\cdot \dots  (a_n-a_{n-1})]\times [(a_n-a_1)(a_n-a_2)\cdot \dots  (a_n-a_{n-2})]\dots$$
Also note that this is why we assume that any $a_i \neq a_j$ when $i \neq j$, otherwise we would get a 0 which would ruin our product.

As long as the values of $x_i$ are unique, we never run into a $0$, so we ideally should be able to apply row operations until we get this resulting formula. 

Let us consider some Vandermonde matrices of small dimensions to verify the formula:
$$\det\left( \begin{bmatrix} 1 & a_1\\ 1 & a_2 \end{bmatrix} \right)=a_2-a_1$$
For the $3 \times 3$ case observe that:
$$\det\left( \begin{bmatrix} 1 & a_1 & a_1^2\\ 1 & a_2 & a_2^2\\
1 & a_3 & a_3^2
\end{bmatrix} \right)$$
We can use [[Elementary Row Operations]] in order to reduce the the current matrix into something more manageable. Let us consider $r_2 - r_1 \to r_2, r_3 -r_1 \to r_3$:
$$\det\left( \begin{bmatrix} 1 & a_1 & a_1^2\\ 0 & a_2-a_1 & a_2^2 - a_1^2\\
0 & a_3 -a_1 & a_3^2 -a_1^2
\end{bmatrix} \right)$$
Then we can compute the resulting [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] using [[Cofactor Expansion]] we can factor out the following factors for the second and third rows and obtain:
$$=(a_2-a_1)(a_3-a_1)\det\left( \begin{bmatrix} 1 & a_1 & a_1^2\\ 0 & 1 & a_2 + a_1\\
0 & 1 & a_3 +a_1
\end{bmatrix} \right)$$
We can then use [[Cofactor Expansion]] to obtain the determinant of a $2 \times 2$ matrix, giving us the result:
$$=(a_2-a_1)(a_3-a_1)(a_3-a_2)$$
We can prove this result using induction. For the base case, we have already shown that the [[Vandermonde Matrix]] of $n=2$ is valid, the same goes true for the $n=1$ case which is trivial. We can assume it holds for $n-1$. We want to show it is true for $n-1$.  

Given the Vandermonde of $n \times n$, we can perform [[Elementary Row Operations]] to remove the $1$ from the leftmost column, leaving a row of zeros underneath the top 1. 

$$\det\left( \begin{bmatrix} 1 & a_1 & a_1^2 & \dots & a_1^{n}\\ 0 & a_2-a_1 & a_2^2 - a_1^2 & \dots & a_2^n-a^n_1 \\
0 & a_3 -a_1 & a_3^2 -a_1^2 & \dots & a_3^n-a^n_1 \\
\vdots & \vdots &  \vdots & \ddots & \vdots\\
0 & a_n -a_1 & a_n^2 -a_1^2 & \dots & a_n^n-a^n_1
\end{bmatrix} \right)$$
We then apply [[Elementary Column Operations]] to remove the other values from the top most row, which leaves a clean 1:
$$\det\left( \begin{bmatrix} 1 & a_1 & a_1^2 & \dots & a_1^{n}\\ 0 & a_2-a_1 & a_2^2 - a_1^2 & \dots & a_2^n-a^n_1 \\
0 & a_3 -a_1 & a_3^2 -a_1^2 & \dots & a_3^n-a^n_1 \\
\vdots & \vdots &  \vdots & \ddots & \vdots\\
0 & a_n -a_1 & a_n^2 -a_1^2 & \dots & a_n^n-a^n_1
\end{bmatrix} \right)$$
Let us apply the operation of column reducing the $n-1$th, but we scale the $n-1$th column by $a_1$ column from the $n$th column: 
$$=\det\left( \begin{bmatrix} 1 & a_1 & a_1^2 & \dots & 0\\ 
0 & a_2-a_1 & a_2^2 - a_1^2 & \dots & a_2^n-a_{n-1}a^{n-1}_2 \\
0 & a_3 -a_1 & a_3^2 -a_1^2 & \dots &a_3^n-a_{n-1}a^{n-1}_3  \\
\vdots & \vdots &  \vdots & \ddots & \vdots\\
0 & a_n -a_1 & a_n^2 -a_1^2 & \dots & a_n^n-a_{n-1}a^{n-1}_n
\end{bmatrix} \right)$$
We can repeat this process. Each column will contain $(a_n-a_1)$, which can be factored out, leaving the resulting matrix:
$$= \prod_{i=2}^n(a_i-a_1) \det\left( \begin{bmatrix} 1 & 0 & 0 & \dots & 0\\ 
0 & 1 & a_2 & \dots & a_2^n \\
0 & 1 & a_3  & \dots &a_3^n \\
\vdots & \vdots &  \vdots & \ddots & \vdots\\
0 & 1 & a_n  & \dots & a_n^n
\end{bmatrix} \right)$$
Notice that the determinant of this matrix here is another [[Vandermonde Matrix]]. By our inductive hypothesis, we know that this determinant evaluates to:
$$\left[\prod_{i=2}^n(a_i-a_1) \cdot \right] \prod_{1 \leq i < j}^{n-1} (a_i-a_j) = \prod_{0 \leq i  < j}^n (a_i-a_j) =\det(V)$$
And since we assume that no $a_i \neq a_j$ for $i \neq j \implies \det(V) \neq 0$:
$$\textcolor[RGB]{153, 115, 235}{\boxed{\therefore \det(V) \neq 0 \text{ given that each } x_i \neq x_j \text{ for } i \neq j }} $$
