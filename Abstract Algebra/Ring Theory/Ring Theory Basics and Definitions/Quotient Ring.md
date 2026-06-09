---
title: Quotient Ring
tags:
  - AbstractAlgebra
draft: "False"
---
# Quotient Ring
Let $R$ be a [[Ring]] and let $A \subseteq R$. $R$ is an [[Abelian Group]], so $R$ is automatically a [[Normal Subgroup]]. This allows us to form the [[Quotient Group]]:
$$\frac{R}{A}=\{r+A:r \in R \}$$
Where the addition of [[Coset]]s is the [[Binary Operation]] on this group defined as:
$$(r_{1}+A)+(r_{2}+A)=(r_{1}+r_{2})+A$$
We want to extend this notion to rings with the operation of multiplication in the following:
$$(r_{1}+A)(r_{2}+A)=r_{1}r_{2}+A$$

This only works when some [[Subring]] $A$ is an [[Ideal (Rings)]] of $R$, and not just a subring. 

---
# Theorem.) Existence of a Quotient Ring
Let $R$ be a [[Ring]] and let $A$ be a [[Subring]] of $R$, then the set of cosets $\{r+A:r \in R\}$ is a ring under addition and multiplication operations defined in the following form:
$$(s+A)+(t+A)=(s+t)+A$$
$$(s+A)(t+A)=(st)+A$$
If and only if $A$ is an ideal of $R$. 

$Proof.$ 
We know that the cosets of $A$ in $R$ form an [[Abelian Group]] under addition, so we already know that $A$ automatically forms a [[Quotient Group]], and thus the properties of associativity and distributivity for multiplication automatically transfer to $A$ from $R$. All that needs to be shown that multiplication of cosets is well defined $\iff A$ is an ideal of $R$. 

Suppose that $A$ is an ideal and that $s+A=s'+A,t+A=t'+A$. By definition then $s=s'+a$ and $t=t'+b$ for some $a,b \in A$. Then we can express:
$$st=(s'+a)(t'+b)=s't'+at'+s'b+ab$$

Since we assumed that $A$ is an ideal, then $at',s'b \in A$ by the absorbing property of $A$, and thus we have:
$$st+A=s't'+A$$
Thus, multiplication is well defined if $A$ is an ideal of $R$. 

Conversely it must be shown that if multiplication is well defined, then $A$ is an ideal. 
Let $a \in A,r\in R$. Then:
$$a+A=0+A=A$$
Since multiplication is well defined, then we have that:
$$\begin{align}
ar+A=(a+A)(r+A) = (0+A)(r+A) \\
=(0r+A) \\
=0+A=A
\end{align}$$
It must thus be the case that $ar\in A$, since $ar+A=A$, likewise we can say the same for $ra\in A$, so $A$ is an ideal. 

The result thus follows since we have shown both directions and all other relevant criteria. 

---
# Examples.)

### Example 1.)
$$\frac{\mathbb{Z}}{4\mathbb{Z}}=\{0+4\mathbb{Z},1+4\mathbb{Z},2+4\mathbb{Z},3+4\mathbb{Z} \}$$
We apply the modulo argument on each integer added, for instance:
$$\begin{align}
(2+4\mathbb{Z})+(3+4\mathbb{Z})=5+4\mathbb{Z}=(1+4\mathbb{Z}) \\ 
(2+4\mathbb{Z})(3+4\mathbb{Z})=5+4\mathbb{Z}=(2+4\mathbb{Z})
\end{align}$$

### Example 2.) 
$$\frac{2\mathbb{Z}}{6\mathbb{Z}} = \{0 +6\mathbb{Z},2+6\mathbb{Z},4+6\mathbb{Z} \}$$We apply the modulo argument on each integer added, for instance:
$$\begin{align}
(4+6\mathbb{Z})+(4+6\mathbb{Z})=8+6\mathbb{Z}=(2+4\mathbb{Z}) \\ 
(4+6\mathbb{Z})(4+6\mathbb{Z})=16+6\mathbb{Z}=(4+6\mathbb{Z})
\end{align}$$

### Example 3.)
$$\begin{align}
R=\mathbb{Z}^{2 \times 2},I=(2\mathbb{Z})^{2 \times 2}
\end{align}$$
Note that:
$$\frac{R}{I}=\left\{ \begin{bmatrix}
r_{11} & r_{12} \\
r_{21} & r_{r_{22}} 
\end{bmatrix} + I : r_{ij}  \in \mathbb{Z}_{2} \right\}$$
From this we obtain that $\left| \frac{R}{I} \right| = 2^4=16$. For $3 \times3$ we would likewise have $2^9$ many choices. For example under this group:
$$\begin{bmatrix}
7&8 \\
5&-3
\end{bmatrix}+I=\begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix} + \begin{bmatrix}
6 & 8 \\
4 & -4
\end{bmatrix}+I=\begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix} + I$$
### Example 4.) 
Let $R=\mathbb{Z}_{3}[x]$, and $I=\langle x^2+1 \rangle$. How many distinct cosets does $\frac{R}{I}$ have? Note that:
$$x^2+1+I=0+I=I$$
This is to say that $x^2+1=0 \iff x^2=-1 \iff x^2=2$ over $\frac{R}{I}$. Thus, we have that $x^3=x^2(x)=2x$ in $\frac{R}{I}$. For $x^4=(x^2)(x^2)=1$ over $\frac{R}{I}$. From this it can be deduced that:

$$\frac{R}{I}=\{ax+b+I : a,b \in \mathbb{Z}_{3} \}$$
This gives then $3\times3$ possibilities for [[Coset]]s. For an example of multiplication in this group consider:
$$(ax+b)(cx+d)=acx^2+(ad+bc)x+bd=(ad+bc)x+(bd-ac)$$
Which follows from the fact that $x^2=-1$ in $\frac{R}{I}$ again. 

Furthermore, we have that $(x+1)^2=x^2+2x+1=2x$ is true in $\frac{R}{I}$. 

Then we have that:
$$(x+1)^4=(2x)^2=4x^2=(1)(-1)=1$$
Which entails that $(x+1)$ is a unit in $\frac{R}{I}$, and also has order $8$. Thus it must be the case that all $8$ other non-zero elements of $\frac{R}{I}$ are all units and have multiplicative inverses. We can conclude that $\frac{R}{I}$ is a field. 

### Example 5.) $R=\mathbb{Z}_{5}[x]$, then as above $I=\langle x^2+1\rangle$

We suppose that $\frac{R}{I}=25=5^2$ many elements. 

Here:
$$(x+1)^4=(2x)^2=4x^2=4(-1)=-4=1$$
And thus $x+1$ is a unit and $|x+1|=4$. 

It is also the case that $R$ is not a Field since $R$ has zero divisors:

$$\begin{align}
(x+2)(x+3)=x^2+2x+3x+6=x^2+5x+5+1=x^2+1=0
\end{align}$$
Holds over $I$ in the last $2$ equalities. Thus, $x+2,x+3$ are both zero divisors in $\frac{R}{I}$, and thus this quotient ring is not a field.  

