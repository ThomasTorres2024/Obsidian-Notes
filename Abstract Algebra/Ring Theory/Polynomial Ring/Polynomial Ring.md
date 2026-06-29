---
title: Polynomial Ring
tags:
  - AbstractAlgebra
draft: "False"
---
# Polynomial Ring
A [[Polynomial Ring]] is a [[Ring]] of [[Polynomial]]s over some commutative ring. We define a [[Polynomial Ring]] in the following: 

For commutative ring $R$, the set of formal symbols:
$$R[x]=\left\{  \sum_{k=0}^n a_{k}x^k : a_{k} \in R \right\}$$
Two elements of a [[Polynomial Ring]] are considered equal $\iff$:
$$\sum_{k=0}^n a_{k}x^k = \sum_{k=0} ^n b_{k}x^k \iff a_{k} = b_{k} \quad  \forall k $$

The [[Binary Operation]]s of addition and multiplication of [[Polynomial]]s in the ring context are the same definitions as in standard algebra. 

---
### Theorem). 
If $D$ is an [[Integral Domain]] then $D[x]$ is an [[Integral Domain]]. 

$Proof.)$
All that needs to be shown is that $D[x]$ is commutative, has an identity element, and no zero divisors. 

Since $D$ contains an identity element $I$ for multiplication, then we can consider strictly it as a polynomial, where it then has the property that $If=fI$ for $f \in D[x]$ since $I$ is an identity element. $D[x]$ is commutative when $D$ is which can be algebraically verified by considering the product of two $f(x),g(x) \in D[x]$ in excruciating detail. 

To show no zero divisors, if we simply consider some $f(x),g(x) \in D[x]$ such that $f(x) \neq 0, g(x) \neq0$ entails that the leading coefficient in both polynomials is non-zero, and thus their product is also non-zero. 

$$\therefore D[x] \text{  is an integral domain}$$
---
### Theorem). The [[Polynomial Division Algorithm]] 
The [[Polynomial Division Algorithm]] states that for all $f(x),g(x) \in k[x]$ where $k$ is a [[Field]] and $k[x]$ is a [[Polynomial Ring]], that there is a unique $q(x),r(x)$ such that:

$$f(x)=q(x)g(x)+r(x)$$

Where the degrees of $r(x)$ and $g(x)$ satisfy:
$$0\leq \text{deg}(r(x))<\text{deg}(g(x))$$
For the proof, go to [[Polynomial Division Algorithm]]. 

---
### Theorem). 
A polynomial of degree $n$ over a [[Field]] has at most $n$ zeroes, counting multiplicity. 

$Proof.)$ 
We proceed with induction on $n$. A polynomial of degree $0$ has no zeros. 

Suppose now that $f(x)$ is a polynomial of degree $n$ over a field, and $a$ is a zero of $f(x)$ of multiplicity $k$. Then:
$$f(x)=(x-a)^kq(x) :q(a) \neq 0$$

From this we can see that: 
$$\begin{align}
\text{deg}(f(x))=\text{deg}((x-a)^kq(x)) \\
=k+\text{deg}(q(x))=n
\end{align}$$
Here we still have that $k \leq n$. If $f(x)$ has no zeroes other than $a$ then we are done and obtain $k=n$. OTOH if $b\neq a$ and $b$ is a zero of $f(x)$, then:
$$f(b)=(b-a)^kq(b) \implies f(b)=0$$
So $b$ is a zero of $f(x)$ and a zero of $q(x)$ moreover, which has the same multiplicity for $f(x)$. 
 
---
### Theorem - Every [[Ideal (Rings)]] in $k[x]$ is a principal ideal. 
Suppose $I \subseteq k[x]$ is an [[Ideal (Rings)]]. Take $p(x) \in I$ such that $p(x)$ is a [[Monic Polynomial]] and that $\text{deg}(p(x))$ is minimal over all polynomials of positive degree, which ensures that $p(x)$ is not a constant [[Polynomial]]. We want to show that $p(x)$ generates the entire [[Ideal (Rings)]]. 

Suppose that $f(x) \in I$ and we can use the [[Polynomial Division Algorithm]] to express:
$$f(x)=p(x)q(x)+r(x) \quad 0 \leq \text{deg}(r(x)) < \text{deg}(p(x)) $$

Since $p(x)$ is assumed to have minimal degree so we have that  $\text{deg}(r(x))=0$.  From this we obtain $2$ cases, that either $r(x)=0$ or $r(x) \neq 0$. 

### Case 1.) $r(x)=0$
In this case, we have that $f(x) \in I \implies f(x)=p(x)q(x) \implies f(x) \in \langle p(x) \rangle$ and thus since $f(x)$ is arb. we have that $I \subseteq \langle p(x) \rangle$, and we also know that $p(x) \in I$ by assumption and thus $\langle p(x) \rangle \subseteq I$.

### Case 2.) $r(x) =\alpha \neq 0$
Since $k$ is a [[Field]] then $\alpha$ is a [[Unit (Ring Theory)]]. Since we have a unit $\alpha$ in the [[Ideal (Rings)]], then the whole [[Ring]] must be contained in the ring and thus we have that:
$$\langle p(x) \rangle = k[x]$$
This concludes the proof. 

### $\textcolor{red}{\text{Example: }}$ - $\mathbb{Z}[x]$ is not a PID. 
Let the following:
$$I=\langle x , 2 \rangle = \langle a_{n}x^n+a_{n-1}x^{n-1}+\cdots+a_{1}x+2a_{0} : a_{i} \in \mathbb{Z} \rangle $$ Suppose that $p(x) \in\mathbb{Z}[x]$ with $\langle p(x) \rangle = I =\langle x,2 \rangle$. Then:
$$2 \in \langle p(x) \rangle \implies 2 = p(x)f(x) \quad f(x) \in \mathbb{Z}{x}$$
However this entails that:
$$\text{deg}(p(x))=\text{deg}(f(x))=0$$
Which means that both $p(x)$ and $f(x)$ are constant polynomials. This means that $p(x)=1$ or $p(x)=2$. But if $p(x)$ were $1$ then it would entail that the entire Ring is equal to the ideal, which is not the case (trivially true since the constant term need not be even). This forces $p(x)=2$. 

But, since $p(x)=2$, then we have that $x$ is a multiple of $2$ but this is clearly not true, and since $x$ is one of the generators of the [[Ideal (Rings)]] it follows that  $\mathbb{Z}[x]$ is __not__ a [[Principle Ideal Domain]]. 