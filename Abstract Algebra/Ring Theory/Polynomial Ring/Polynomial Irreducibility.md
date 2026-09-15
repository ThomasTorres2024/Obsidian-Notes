---
title: Polynomial Factorization
tags:
  - AbstractAlgebra
draft: "False"
---
### Definition). "Content"
The "Content" of a [[Polynomial]] for the polynomial $p(x)=\sum_{j=0}^n \alpha_{j}x^j$ is the greatest common divisor of the integers $\alpha_{n},\dots,\alpha_{0}$. 

### Definition). "Primitive Polynomial"
A primitive polynomial is an element of $\mathbb{Z}[x]$ with content $1$.  

### Gauss's Lemma 
Gauss's Lemma states that the product of two primitive polynomials is itself primitive. 

$Proof).$ 
Let $f(x),g(x)$ be polynomials that are primitive. BWOC assume $f(x)g(x)$ is not prime, thus we can assume that there is some prime $p$ such that $p$ is a factor of this polynomial. Now consider the following:
$$\begin{align}
\overline{f(x)} = f(x) \text{ mod}(p) \quad \quad   \overline{g(x)} = g(x) \text{ mod}(p) \\
 \overline{f(x)g(x)}= f(x)g(x) \text{ mod}(p)
\end{align}$$
Notice that $\overline{f(x)},\overline{g(x)},\overline{f(x)g(x)} \in \mathbb{Z}_{p}[x]$, which is an [[Integral Domain]] since $p$ is a prime. Then we have the following:
$$\overline{f(x)} \cdot \overline{g(x)} = \overline{f(x)g(x)} = 0 $$
Since we are over an integral domain then $f(x)=0 \lor g(x)=0$. This means that either one of $f,g$ has coefficients which are a multiple of $p$ and are thus composite which contradicts the fact $f,g$ are primitive $\therefore$ 

### Theorem). 
Reducibility over $\mathbb{Q} \implies$ reducibility over $\mathbb{Z}$. 

$Proof).$ 
Suppose that $f(x)=g(x)h(x)$ where $g(x),h(x) \in \mathbb{Q}[x]$.  Assume $f(x)$ is primitive (we can divide both $f(x),g(x)$ by the content of $f(x)$).

Let $a$ be the LCM of the denominators of the coefficients of $g(x)$ and $b$ be the LCM of the denominators of the coefficients of $h(x)$. 

Then:
$$abf(x)=ag(x) \cdot bh(x) $$
And thus we have that $ag(x),bh(x) \in \mathbb{Z}[x]$. Let $c_{1}$be the content of $ag(x)$ and let $c_{2}$ be the content of $bh(x)$. Then:
$$ag(x)=c_{1}g(x) \quad bh(x)=c_{2}h_{1}(x)$$ where both $g_{1}(x),h_{1}(x)$ are primitive and $abf(x)=c_{1}c_{2}g_{1}(x)h_{1}(x)$.Since $f(x)$ is primitive, then its content must be $ab$. Secondly, since the product of primitive polynomials is also primitive, then the content of $c_{1}c_{2}g_{1}(x)$ is thus $c_{1}c_{2}$. Therefore $ab=c_{1}c_{2}$ and $f(x)=g_{1}(x)h_{1}(x)$ for $g_{1}(x),h_{1}(x) \in \mathbb{Z}[x]$ 
and $\text{deg}(g_{1}(x))=\text{deg}(g(x))$ and $\text{deg}(h_{1}(x))=\text{deg}(h(x))$

We are able to cancel out the $ab$ and $c_{1}c_{2}$ and obtain our result over the integers, which concludes the proof. 

#### Example).
Let $f(x)=6x^2+x-2=\left( 3x-\frac{3}{2} \right)\left( 2x+\frac{4}{3} \right) =g(x)h(x)$. Then here we have that $a=2,b=3 \implies c_{1}=3,c_{2}=2$ and then $g_{1}(x)=2x-1$ and $h_{1}(x)=3x+2$. This finally gives us:
$$\begin{align}
2\cdot3 (6x^2 + x -2)=3\cdot 2(2x-1)(3x+2) \\
6x^2+x-2=(2x-1)(3x+2)
\end{align}$$

---
# Irreducibility Tests 
### Theorem).
Let $p$ be a [[Prime]] and suppose that $f(x) \in \mathbb{Z}[x]$ with $\text{deg}(f(x))\geq1$. Let $f(x)$ be the polynomial in $\mathbb{Z}_{p}[x]$ obtained by reducing all coefficients of $f(x) \text{ mod}(p)$. If $f(x)$ is irreducible over $\mathbb{Z}_{p}$ and $\text{deg}(f(x))=\text{deg}(\overline{f(x)})$, then $f(x)$ is irreducible over $\mathbb{Q}$. 

$Proof).$ 
From the above theorem, if $f(x)$ is reducible over $Q$ then $f(x)=g(x)h(x)$ with $g(x),h(x) \in \mathbb{Z}[x]$ s.t. $h,g$ have degrees less than that of $f$. Let $\overline{f(x)},\overline{g(x)},\overline{h(x)}$ be the polynomials obtained by reducing the coefficients by $\text{mod(p)}$. Then, $\text{deg}(f(x))=\text{deg}(\overline{f(x)})$ (true when the coefficient of $f(x)$ is not a multiple of $p$) but then $\text{deg}(\overline{g(x)})\leq \text{deg}(g(x))< \text{deg}(f(x))$ and $\text{deg}(\overline{h(x)})\leq \text{deg}(h(x))< \text{deg}(h(x))$. But notice that $\overline{f(x)}=\overline{g(x)} \overline{h(x)}$ but $\implies \Longleftarrow$ since we assumed $\bar{f(x)}$ cannot be reduced over $\mathbb{Z}_{p}$. 

It is important to note that the converse of this theorem is __not__ true. 
#### Example). 
Let $f(x)=21x^3-3x^2+2x+9$ then over $\mathbb{Z}_{2}$ we have $\bar{f(x)}=x^3+x^2+1$. Since $\bar{f(0)}=1,\bar{f(1)}=1 \implies \bar{f(x)}$ is irreducible over $\mathbb{Z}_{p} \implies$ it is irreducible over $\mathbb{Q}$.  

For an example of the converse failing, notice that over $\mathbb{Z}_{3}$ it is $2x$ and thereby reducible, but it being reducible over $\mathbb{Z}_{3}$ does not suddenly make it reducible over $\mathbb{Q}$. 

It is __important__ to note with this that, it is only when some $p$ is found such that $\overline{f(x)}$ is irreducible over $\mathbb{Z}_{p}$ when we can apply the result, finding some $p$ doesn't ensure it. Also not finding some $p$ does not automatically mean that the result is reducible. Consider over $\mathbb{Q}, x^4+1$ it is reducible over every $\mathbb{Z}_{p}$.  This is a generally useful method for checking for reducibility when our polynomial's degree is greater than 3 and has rational coefficients. 

### Example. 
Let $f(x)=\frac{3}{7}x^4-\left( \frac{2}{7} \right)x^2+\frac{9}{35}x + \frac{3}{5}$. We can show that $f(x)$ is irreducible over $Q$. Let $h(x)=35f(x)=15x^4-10x^2+9x+21$. Then, $f(x)$ is irreducible over $Q$ if $h(x)$ is irreducible over $\mathbb{Z}$. Now apply $\text{mod}(2)$ irreducibility test:
$$h(x) \text{ mod}(2) =x^4 + x + 1  $$
Thus $\bar{h(x)}$ has no zeroes over $\mathbb{Z}_{2}$. Furthermore, $\bar{h(x)}$ has no quadratic factor. We can obtain this from seeing that $x^2+x+1$ isn't a factor via long division and that $x^2+1,x^2$ have zeroes. This entails that $\bar{h(x)}$ is irreducible over $\mathbb{Z}_{2} \implies$ irreducible over $\mathbb{Q}$. 

It isn't necessary to check fourth degree factors since this would put us already above the polynomial's degree. For $x^3$, we would be introducing a zero with either $x^3,x^3+1$ same for $x$ or $x+1$ therefore it is irreducible over $\mathbb{Z}_{2}$.

### Example 8). 
Let $f(x)=x^5+2x+4$. The first theorem for degree 2-3 polynomials cannot satisfy this, neither can the mod 2 irreducibility test, thus we'll try mod 3:
$$\bar{f}(x)= \text{mod}(3) f(x) = x^5+2x+1$$
Notice that $\bar{f}(0),\bar{f}(1),\bar{f}(2) \neq 0 \implies$ no linear factors. Secondly $\bar{f}(x)$ may have a quadratic factor. If it does let such a factor be given by $x^2+ax+b$, which leaves $9$ possible entries. Any entry with a $0$ is taken out automatically, which leaves $x^2+1,x^2+x+2,x^2+2x+2$ all of which fail under long division.  We cannot include $x^3,x^4$ since these would need a corresponding $x^2,x$ term respectively to get $x^5$ when these are already ruled out. Thus, $\bar{f}(x)$ is irreducible over $\mathbb{Z}_{3} \implies  \bar{f}(x)$ is irreducible over $\mathbb{Q}$. 

### Theorem - Eisenstein's Criterion).
This is an irreducibility theorem which allows us to categorize some polynomials as being unfactorable over $\mathbb{Q}$:

Here is the theorem:
Let $f(x)= \sum_{i=0}^n \alpha_{i} x^i \in \mathbb{Z}[x]$. If there is a prime $p$ such that $p \not\large| a_n, p  \large| a_{n-1} \dots , p \large | a_{0}$ and $p^2 \not \large| a_{0} \implies f(x)$ is irreducible over $\mathbb{Q}$

$Proof).$ 
If $f(x)$ is reducible over $\mathbb{Q} \implies \exists g(x),h(x) \in \mathbb{Z}[x]$ such that $f(x)=g(x)h(x)$ where $1\leq \text{deg}(g(x))$ and $1\leq \text{deg}(h(x))<n$. Then we can express the following:
$$g(x)=\sum_{i=0}^r b_{i}x^i \quad h(x)=\sum_{j=0}^s c_{j}x^j$$
Then let us write:
$$f(x) = \sum_{l=0}^n a_{l}x^l$$
Notice the following, that $p |a_{0}$ but $a_0=b_{0}c_{0} \implies$ only one of $a_{0},b_{0}$ is divisible by $p$ since otherwise $p^2$ would divide $a_{0}$. WLOG $p$ divides $b_{0}$ and not $c_0$. Notably, $a_{n}=b_{r}c_{s}$, and thus we can conclude that $p$ cannot divide $a_n$ so it also cannot divide $b_r$. There is a least integer $t$ such that $p$ does not divide $b_{t}$. Consider now, $a_{t}=b_{t}c_{0}+b_{t-1}c_{1}+\dots+b_{0}c_{t}$. By assumption $p$ divides $a_{t}$, which forces $p$ to divide $b_{0}c_{t}$, but this cannot occur since we already have inferred that $b_0,c_t$ are NOT divisible by $p$. Therefore, BWOC Eisenstein's Criterion holds. 

### Corollary Irreducibility of the $p$th Cyclotomic Polynomial 
For any prime $p$ the following polynomial is irreducible over $\mathbb{Q}$:
$$\Phi_{p}(x)= \frac{x^p-1}{x-1} = x^{p-1}+x^{p-2} + \dots + x+1 $$
$Proof)$. 
Let $f(x)=\Phi_{p}(x+1)= \frac{(x+1)^p-1}{(x+1)-1}$ so:
$$f(x)= x^{p-1}+ {p\choose_{}{1}}x^{p-2} +{p \choose{}{2}}x^{p-3}+\dots+ {p \choose{}{1}} $$
Notice that every coefficient of $f(x)$ except for $x^{p-1}$ is divisible by $p$, and the last term is not divisible by $p^2 \implies$ by Eiensstein's criterion that $f(x)$ is irreducible over $\mathbb{Q}$. 
### Example 9). 
The polynomial $3x^5+15x^4-20x^3+10x+20$ is irreducible over $\mathbb{Q}$ since $5 \not| 3$ and $25 \not 5|$, but all other coefficients are divisible by $5$. 

---
# Relationship Between Maximal Ideals, Fields, and Irreducible Polynomials 

##### Theorem). 
Let $\mathbb{F}$ be a field and $p(x) \in \mathbb{F}[x]$. Then, $\langle p(x) \rangle$ is a [[Maximal Ideal]] in $\mathbb{F}[x]$ iff $p(x)$ is an [[Irreducible Polynomial]] over $\mathbb{F}[x]$. 

$Proof).$ 
Suppose $\langle p(x) \rangle$ is a maximal ideal in $\mathbb{F}[x]$, then $p(x)$ cannot be the 0 polynomial since $[0]$ and $\mathbb{F}[x]$ are __not__ maximal ideals in $\mathbb{F}[x]$. Now suppose $p(x)=g(x)h(x)$ is a factorization of $p$ over $\mathbb{F}$. If $p(x)=g(x)h(x)$, then $\langle p(x) \rangle \subseteq \langle g(x) \rangle \subseteq \mathbb{F}[x]$. 

This gives that either $\langle p(x) \rangle = \langle g(x) \rangle$ or $\mathbb{F}[x]=\langle g(x) \rangle$. In the first case we get equality of the degrees of the polynomials, and in the second $\text{deg}(g(x))=0$. This gives that $p(x)$ cannot be factored into polynomials of lower degree in $g(x),h(x)$. 

Now, suppose that $p(x)$ is irreducible over $\mathbb{F}[x]$. Let $I$ be any ideal of $\mathbb{F}[x]$ such that $\langle p(x) \rangle \subseteq I \subseteq \mathbb{F}[x]$. Because $\mathbb{F}[x]$ is a principal ideal domain, we know that for some $g(x) \in \mathbb{F}$ that $\langle g(x) \rangle = I$. Thus, $p(x) \in \langle g(x) \rangle$, which entails that $p(x)=h(x)g(x)$ where $h(x) \in \mathbb{F}[x]$. Notice that since $p(x)$ is assumed irreducible then either $g(x)$ is constant or $h(x)$ is constant. If we have that $g(x)$ is constant then $\langle g(x) \rangle = I$ in the second case, in t he first case we have that $I=\mathbb{F}[x]$ 

### Corollary 1). $\mathbb{F}[x] \text{\\} \langle p[x] \rangle$ is a field 
Let $\mathbb{F}$ be a field and let $p(x)$ be an irreducible polynomial over $\mathbb{F}$, then $\mathbb{F}[x] \text{\\} \langle p [x] \rangle$ is a [[Field]]. 

$Proof).$
Using the above theorem given this condition then $\langle p [x] \rangle$ is a [[Maximal Ideal]].  Then recall the fact that for any maximal ideal quotiented out of its respected ring, the result is a field. Therefore it is a field. 

### Corollary 2). $p(x) \bigg| a(x)b(x) \implies p(x) \bigg|a(x)$ or $p(x) \bigg|b(x)$
Note that this is a [[Polynomial]] equivalent of [[Euclid's Lemma]]. 

$Proof).$ 
Recall that $p(x)$ is irreducible, then $\mathbb{F}[x] \text{\\} \langle p[x] \rangle$ is a field, and must then be an integral domain. Secondly, since $\langle p(x) \rangle$ is a [[Maximal Ideal]] it is therefore a [[Prime Ideal]]. Since $p(x)$ divides $a(x)b(x)$ then $a(x)b(x) \in \langle p(x) \rangle$ which entails that either $a(x) \in \langle p(x) \rangle$ or $b(x) \in \langle p(x) \rangle$. 
