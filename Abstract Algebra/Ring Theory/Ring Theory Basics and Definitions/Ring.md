---
title: Ring
tags:
  - AbstractAlgebra
draft: "False"
---
# Ring Motivation
Rings are Algebraic [[Group]] like structures with $2$ [[Binary Operation]]s which makes them interesting, since many mathematical objects have $2$ operations such as integers, reals, and matrices. 

---
# Ring Definition
A ring $R$ is a set with two [[Binary Operation]]s, addition and multiplication respectively denoted by $a+b$ and $ab$ for $a,b \in R$. The following properties hold true. 

1. Closure : $a+b,ab \in R$
2. $a+b=b+a$
3. $(a+b)+c=a+(b+c)$
4. There is an additive [[Identity Element]] namely, $\exists 0 \in R$ such that $a+0=0+a=a : \forall a \in R$
5. For each $a\in R$ $\exists a^{-1} \in R$ such that $a-a=-a+a=0$
6. $a(bc)=(ab)c$
7. $a(b+c)=ab+ac \quad (b+c)a=ba+ca$

The first $4$ axioms mandate that any ring has an [[Abelian Group]] structure for the $+$ operation and simply closure for the $\cdot$ operation. 

The only things that really can be said about the multiplication operation is that it is associative and distributives over addition. 

If $R$ is commutative with a multiplicative identity, and $a$ is a non-zero element of $R$ with a multiplicative inverse such that $\exists a^{-1} \in R$ where $a(a^{-1})=a^{-1}a=1$, then we say that $a$ is a [[Unit (Ring Theory)]]. 

If every non-zero element of $R$ is a unit then say that $R$ is a [[Field]]. 

---
# Terminology
If $R$ is commutative and $a,b \in R$ where $a\neq0$, we say that $a$ divides $b$ or that $a$ is a factor of $b$ if $\exists c \in R$ such that $ac=b$. 

If $a$ doesn't divide $b$ we write that $a\not \bigg|b$. 
We can express repeated additions by $na$ where:

$$na=\sum_{i=1}^n a : a \in R, n \in \mathbb{N}$$

---
# Examples of Rings 

### Example 1.) $\mathbb{Z}$ 
$\mathbb{Z}$ naturally has its own addition and multiplication operations, and has its own units, namely $1,-1$. 

### Example 2.) $\mathbb{Z}_{n}$
$\mathbb{Z}_{n}$ with addition and multiplication $\mod n$ is a commutative ring with unity $1$. The set all of units of this [[Ring]] is given by $U(n)$. 
### Example 3.) $\mathbb{Z}[x]$ 
The polynomials in $x$ with integer coefficients with standard addition and multiplication of them. Commutative ring with identity $p(x)=1$. 
### Example $4.)$ $\mathbb{Z}^{2\times 2}$
The set of all $2 \times 2$ matrices with integer coefficients with multiplication and division. All of the units of $\mathbb{Z}^{2 \times 2}$ are matrices $A \in \mathbb{Z}^{2 \times 2}$ where $\det(A)=\pm 1$. 

### Example 5.) $2\mathbb{Z}$ 
Even integers with the usual addition and multiplication. Commutative ring, but no identity. 

### Example 6.) $R=\{ f : f \text{ is cts on }[0,1],f(1)=0\}$
$R$ is commutative under point addition and multiplication of functions, but there is no multiplicative identity. Elements of $R$ satisfy the following:
$$(f+g)(a)=f(a)+g(a)$$
$$(fg)(a)=f(a)g(a)$$

### Example 7.) Direct Sums of Rings
Let $R_{1},R_{2},\cdots,R_{n}$ be Rings. We can construct a new Ring in the following manner, consider $\bigoplus_{i=1}^n R_{i} =\{ (a_{1},a_{2},\cdots,a_{n}) : a_{i} \in R_{i} \}$

Here addition and multiplication are performed component wise, namely:

$$(a_{1},a_{2},\cdots,a_{n})+(b_{1},b_{2},\cdots,b_{n})=(a_{1}+b_{1},a_{2}+b_{2},\cdots,a_{n}+b_{n})$$
$$(a_{1},a_{2},\cdots,a_{n})\cdot(b_{1},b_{2},\cdots,b_{n})=(a_{1}\cdot b_{1},a_{2} \cdot b_{2},\cdots,a_{n} \cdot b_{n})$$
---
# Properties of Rings

### Theorem.) Ring Rules of Multiplication

1. $a0=0a=0$
2. $a(-b)=(-a)b=-(ab)$
3. $(-a)(-b)=ab$
4. $a(b-c)=ab-ac \quad (b-c)a=ba-ca$
If $R$ has an [[Identity Element]] $1$, then:

5. $(-1)a=-a$
6. $(-1)(-1)=1$

$Proof.)$ 
For $1$ we have that 

$0+a{0}=a{0}=a(0+0)=a0 + a0$

Then:
$$0+a0=a0+a0 \iff 0=a0$$
From cancellation. 

For $2$:
$$a(-b)+ab=a(-b+b)=a{0}=0$$
Then we add $-ab$ to both sides and obtain:
$$a(-b)=-ab$$
For $3$, we make use of $2$:
$$(-a)(-b)=-a(-b)=-(-ab)=ab$$

For $4$ we have:
$$a(b-c)+ac=a(b-c+c)=ab$$
 We can subtract $ac$ from both sides and obtain:
 $$a(b-c)=ab-ac$$
 The proof for $(b-c)a=ba-ca$ is similarly done. 

For $5.$ $(-1)a+a=(-1)a+1(a)=(-1+1)a=0a=0$
Notice then that:
$$(-1)a+a=0 \iff (-1)a=-a$$
For $6$ we have that:
$$(-1)(-1)=1\cdot 1 = 1$$


Just like for groups, the identity element and inverses of elements in $R$ are unique under multiplication. 

---
# Theorem ). Uniqueness of the Identity of Inverses

If a commutative ring $R$ has an identity, then it is unique. If an element of $R$ has a multiplicative inverse, then it is unique. 

$Proof.)$ 

Suppose $R$ has $2$ units $e,g$ such that $e\neq g$.  It must be the case that $eg=g$ since $e$ is an identity element preserving $g$. Furthermore, we must also have that $eg=e$ since $g$ is also an identity element and by the transitive property $e=g$. So the identity of a Ring is unique. 

Suppose $a$ is a unit in $R$ with $2$ inverses $b,c$ such that $b\neq c$. Then:

$$ab=ac=1 \iff bac=b \iff (1)c=b \iff c=b$$
Thus multiplicative inverses are unique.
$$$$

