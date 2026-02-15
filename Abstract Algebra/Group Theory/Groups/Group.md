---
title: Group
tags:
draft: "False"
---
# Group Definition
Let us consider the set $G$, with the associated [[Binary Operation]], $\circ$ (we tend to call the binary operation of our group multiplication) such that for $a,b \in G$, each ordered pair $(a,b)$ of elements in $G$ is mapped to another element in $G$, which we denote by $a \circ b$.  

We can say that the set $G$, is a group if with the [[Binary Operation]] the following is satisfied: 
#### Conditions for a Group
1. Associativity of elements in $G$: 
	- $\forall a,b,c \in G: (ab)c=a(bc)$ 
	- By this property any $abc$ can be written as such since the order is irrelevant
2. There is an [[Identity Element]] 
	*  $\exists e \in G$, s.t. $e \circ a = a \circ e = a$ 
3. Inverse Elements 
	* $\forall a \in G, \exists b \in G$ s.t. $a \circ b = b \circ a = e$
4. Closure of [[Binary Operation]]:
	* $\forall a,b \in G a \circ b \in G$
It should be noted that closure is typically included with definition of a [[Group]], but it is already implied since we have a [[Binary Operation]], so we assume it to be true. 

---
# Properties of Groups 
#### (Theorem 2.1) The identity element of the group, $e$ is unique. 
Suppose that the group $G$ has two identity elements, $e$ and $e'$, which implies, $a \in G$:
$$a \circ e = e \circ a= a \circ e' = e' \circ a = a $$
Let $a=e$. Then:
$$e \circ e' = e$$
Which is due to $e'$ being an identity element. But, it also follows that since $e$ is an identity element, it follows that:
$$e \circ e'=e'$$

$$\therefore e=e' $$
Therefore the [[Identity Element]] of a [[Group]] is unique. 
#### (Theorem 2.2) Cancellation
In a group $G$, the right and left cancellation laws hold. $\forall a,b, \in G$:
$$ba=ca \implies b=c$$
$$ab=ac \implies b=c$$
###### Assume $ba=ca$:
Since we have a group $G$, for $a \in G, \exists a^{-1}$. Then we can apply the [[Binary Operation]] to the right for each element:
$$ba=ca \iff ba\circ a^{-1}=ca\circ a^{-1} \iff b(a\circ a^{-1})=c(a\circ a^{-1})\iff bc$$
###### Assume $ba=ca$:
Since we have a group $G$, for $a \in G, \exists a^{-1}$. Then we can apply the [[Binary Operation]] to the right for each element:
$$ab=ca \iff a^{-1}\circ ab= a^{-1}\circ ac \iff  (a^{-1}\circ a)b= (a^{-1}\circ a)c \iff b=c$$
I silently applied the associative property of [[Group]]s, I just denoted them with brackets. 

##### (Not Sure Why Yet) 
The cancellation property in groups gives us the fact that in the [[Cayley Table]] for some group $G$, each element of $G$ appears once in each row and each column of the table. 

#### (Theorem 2.3) Uniqueness of Inverses 
For each $a \in G$, $\exists! b$ such that $a \circ b = b \circ a = e$ where $e$ is the [[Identity Element]] of the [[Group]]. 

Suppose for $a$, that we have the inverses $a_1^{-1}$ and $a_2^{-1}$ such that  $a_1^{-1} \neq a_2^{-1}$.
$$aa_1^{-1}=aa_2^{-1}=e$$
$$(a_1^{-1}a)a_1^{-1}=(a_1^{-1}a)a_2^{-1}$$
$$\therefore a_1^{-1}=a_2^{-1}$$
So, by inverses of the group are unique. We are allowed to do this because of the cancellation property in 2.2. 

#### (Theorem 2.4) Socks-Shoes Theorem 
For $a,b \in G$, $(ab)^{-1}=b^{-1}a^{-1}$. 

We can just compute the result of the expression $ab \circ b^{-1}a^{-1}$:
$$ab \circ b^{-1}a^{-1}=a(b \circ b^{-1})a^{-1}=aa^{-1}=e$$
Now $a^{-1}b^{-1} \circ ab=e$:
$$b^{-1}a^{-1} \circ ab=b^{-1}(a^{-1} \circ a)b=b^{-1}b=e$$
By the definition of inverse in a [[Group]], $\therefore (ab)^{-1}=b^{-1}a^{-1}$. 

---
# Powers of Groups 
For $n \in \mathbb{N}$ we express $g^n$ to be the repeated application of a [[Binary Operation]] with itself:
$$g^n=g \circ g \dots g$$
If $n$ is a negative integer, then $g^n$ is equal to:
$$g^n=(g^{-1})^{|n|}=(g^{-1})^{-n}$$
And if $n=0$ then:
$$g^0=e$$
We obtain the fact that $g^{a+b}=g^a \circ g^b, ab \in \mathbb{Z}$ 

For a group, it is not generally the case that:
$$(ab)^n=a^nb^n$$
(I think this is because we would be mistaking $(ab)\circ (ab) \circ (ab) \dots (ab) )$ with $a^nb^n$, these are clearly different. 

But there are inverse formulas for this product. 

---
# Examples of Groups

#### Ex 1.) $(\mathbb{Z},\cdot)$ 
The set $(\mathbb{Z},\cdot)$ with $\mathbb{Z}$ under multiplication can be shown not to be a group. We know that for $a,b \in \mathbb{Z}$, $a \cdot b \in \mathbb{Z}$, so the set is closed. We have the [[Identity Element]] of $e=1$ since $a\cdot 1 = 1 \cdot a = a$.  However, we fail since there is no inverse for each element, since take $a = 3$, $3x=1\implies x =\frac{1}{3}$, and $x \not \in \mathbb{Z}$ thus there are inverses not in the set. 

#### Ex 2.) $(\{1,-1,i,-i \},\cdot)$ 
We still have a multiplicative identity of $1$ for this set. Each element in the group has an inverse in the group, $1^{-1}=1,  -1^{-1}=-1, i^{-1}=-i. -i^{-1}=i$. Multiplication of complex numbers is associative. We can construct a [[Cayley Table]] and show that the set of numbers is closed under multiplication.   

#### Ex 3.) $\mathbb{Q}^+= \mathbb{Q} \cap (0,\infty)$ 
Let $a,b,c,d \in \mathbb{Z}^+$, and let $p=\frac{a}{b},q=\frac{c}{d}$, thus $p,q \in \mathbb{Q}^+$. 
$$p\cdot q =\frac{a}{b}\cdot \frac{c}{d}=\frac{ac}{bd} \in \mathbb{Q}^+$$
Thus multiplication under this group is closed. since $ac >0, bd > 0$. 

There is clearly an [[Identity Element]] of $1 \in \mathbb{Q}^+$ since $p \cdot 1 = 1 \cdot p$. 

We also know that each number has a multiplicative inverse of:
$$p \cdot \frac{1}{p}=\frac{a}{b} \cdot \frac{b}{a} = 1$$
Multiplication is associative as well over $\mathbb{Q}^+, \therefore$ it is a group.

#### Ex 4.) $G=(\mathbb{R}^+ \textbackslash \mathbb{Q}) \cup \{ 1\}$ 
This is not a group. We associativity, inverses, and an identity element, but we do not have closure. Consider $\sqrt{2} \in G$. $\sqrt{2}^2=2 \not \in G$. 

$\therefore G$ cannot be a group. 

#### Ex 5.) $G=(\mathbb{R}^{2 \times 2},+)$ 
Let $A,B \in \mathbb{R}^{2 \times 2}$:
$$A=\begin{bmatrix} a_1 & a_2\\ a_3 & a_4 \end{bmatrix}$$
$$B=\begin{bmatrix} b_1 & b_2\\ b_3 & b_4 \end{bmatrix}$$
$$A+B=\begin{bmatrix} a_1+b_1 & a_2+b_2\\ a_3 + b_3 & a_4 + b_4 \end{bmatrix}$$
Addition over the reals is associative, thus $A+B=B+A$ since the entries of this matrix can have their order swapped without affecting the value of the resulting matrix. 

The identity element is $e=\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ since:
$$A+e=e+A=A$$

For $A$ we have that $A^{-1}=\begin{bmatrix} -a_1 & -a_2 \\ -a_3 & -a_4 \end{bmatrix}$, since $A+A^{-1}=A^{-1}+A=e$.  

Since we are just element wise adding $0$ to each $A_{ij}$, which will not effect the value. 

For matrices, $A,B,C \in \mathbb{R}^2$:
$$(A+B+C)_{ij}=a_{ij}+b_{ij}+c_{ij}$$
We are really just summing over the reals, which is associative, therefore we can compute the expression in any order and get the dame result, so we obtain the result of associativity. 

$\therefore G$ is a [[Group]]. 
#### Ex 6.) $G=(\mathbb{Z}_n,+)$ is a group under addition $\mod(n)$.  
$$\mathbb{Z}_n=\{0,1,\dots, n-1 \}$$
For $a,b \in \mathbb{Z}_n$:
$$a+b =a+b \mod(n)$$
By the definition of modular addition, $a+b \in \mathbb{Z}_n$. 

Notice that $0+n=0$ and that $1+(n-1)=0$, and that $2+(n-2)=0$. If we index the elements Notice that the $k$th element $z_k \in \mathbb{Z}_n$ has the inverse of $z_{n-k}$.  

0 is clearly the [[Identity Element]] of the group. Also addition is associative over the integers even if they are modulo.  
#### Ex 7.) $G=(\mathbb{R}^*:=\mathbb{R} \backslash \{0 \})$ is a group under normal multiplication 
We are working with reals, and by definitions of the reals, they are associative and closed under multiplication. Clearly the identity element is 1. The inverse for any $a \in \mathbb{R}^*$ is $\frac{1}{a}$, since:
$$a \cdot \frac{1}{a} = \frac{1}{a} \cdot a=\frac{a}{a}$$
#### Ex 8.) [[General Linear Group]]  
Consider, $A,B \in GL(2,\mathbb{R})$. Then $A \cdot B$ we have that $\det(AB)=\det(A) \cdot \det(B) \neq 0 \implies AB \in GL(2,\mathbb{R}$, so we have that the group is closed. [[Matrix Multiplication]] is associative. The identity matrix is the identity element of the group, and is in the group since it has a determinant of 1. 

The general form for an [[Inverse Matrix]] is:
$$A^{-1}= \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
And can be algebraically verified to yield that $AA^{-1}=A^{-1}A=I_2$. 

Therefore, it is a [[Group]]. 

#### Ex 9.) [[Special Linear Group]]  (Read in that article)
Clearly $I_n$ the identity matrix $n \times n$ is the identity element here since $\det(I_n)=1$. 
[[Matrix Multiplication]] is associative. Also for $A,B \in SL(n,\mathbb{R})$ we have that $\det(AB)=\det(A)\det(B)=1$ so $AB \in SL(n,\mathbb{R})$. The inverse of some $A$ exists since its determinant is non-zero, and furthermore its determinant is the reciprocal of $A$, so $\det(A^{-1})=1 \implies A^{-1} \in SL(n,\mathbb{R})$. 

$$\therefore SL(n,\mathbb{R}) \text{ is a Group}$$
#### Ex 10.) The set of all real $n \times n$ matrices with real entries:
$$M(n,\mathbb{R})$$
Under matrix multiplication $M(n,\mathbb{R})$ is not a [[Group]], since it is not always the case that $\exists A^{-1}$ for $A \in M(n,\mathbb{R})$, that is to say there is not always an [[Inverse Matrix]]. 

But for addition, this essentially is just a little bit of a modification from the $2 \times 2$ proof. 

#### Ex 12.) $U(n)$ the set of all positive integers less than $n$ and relatively prime to $n$
We can show that $U(n)$ is a group under multiplication $\mod(n)$. For example let $n=10$, then we can examine the corresponding Cayley table:

| $\cdot \mod(10)$ | 1   | 3   | 7   | 9   |
| ---------------- | --- | --- | --- | --- |
| **1**            | 1   | 3   | 7   | 9   |
| **3**            | 3   | 9   | 1   | 7   |
| **7**            | 7   | 1   | 9   | 3   |
| **9**            | 3   | 7   | 3   | 1   |
By the conditions of this group, we always have $1$, so that serves as the [[Identity Element]]. We also have an inverse via the [[Division Algorithm]]. Multiplication is still associative, even if we are considering modular arithmetic. I am not sure how to verify closure. 

#### Ex 14.) Subtraction under $\mathbb{Z}$ 
Subtraction is not associative so this cannot form a group. 

#### Ex 15.)  Complex Numbers 
For $\mathbb{C}=\{a+bi, a,b \in \mathbb{R} \}$, the set is a [[Group]] under addition. 
The identity element is $0$, clearly since, $a+bi+0=0+a+bi=a+bi$. There is an additive inverse for $a+bi$ of $-a-bi$ since:
$$a+bi-a-bi=0$$
Addition is also associative. 
The set is NOT a [[Group]] under multiplication. This is because $\mathbb{C}$ contains $0$, which has no multiplicative inverse since it cannot be divided.

However, let us consider the set, $\mathbb{C}^*=\mathbb{C} \backslash \{0\}$, under multiplication.
Multiplication over $\mathbb{C}^*$ is associative, and is closed. Furthermore, the inverse for any element is $\frac{1}{a+bi}$. We still have the identity element of $1$, thus $\mathbb{C}^*$ is a group. 

#### Ex 16.)  The [[Roots of Unity]] 
For $n \in \mathbb{N}$ the $n$th roots of unit are defined by:
$$S= \left\{ \cos \left(\frac{2\pi k}{n}\right) ,i\sin \left(\frac{2\pi k}{n}\right) : k=0,1,\dots n-1  \right\}$$
Alternatively we can use [[Euler's Identity]] and represent any $s_1,s_2 \in S$ by $s_1=\exp\left(i\frac{2\pi k}{n}\right)$ ,$s_1=\exp\left(i\frac{2\pi j}{n}\right)$. We can check closure by using the identity with the following:
$$s_1\cdot s_2=\exp\left(i\frac{2\pi (k+j)}{n}\right)$$
If $k+j  > n$ then, we use periodicity to argue closure, otherwise we know that the index will be between the accepted values. We have $1$ as one of the roots of unit always for $k=0$, so we have the identity element. In order to get us back to the origin, we can multiply our element of $s_1$ by $c$ where 
$$c=\exp\left(2\pi i-i\frac{2\pi (k)}{n}\right)$$
The result of $s_1c=cs_1=1$ And of course the result is commutative. 
#### Ex 17.)  $\mathbb{R}^n$ 
Let us consider $v_1,v_2 \in \mathbb{R}^n$. 

Clearly we are associative here. The identity vector here is $\vec{0}=[0,0,0,\dots, 0]^T$. 

---
#### Euclidean Algorithm 
An integer $a$ has a multiplicative inverse, modulo $n$ iff $a$ and $n$ are relatively prime. 