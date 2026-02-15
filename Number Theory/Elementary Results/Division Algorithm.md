---
title: Euclidean Algorithm
tags:
  - NumberTheory
draft: "False"
---
# Euclidean Algorithm  

For $a,b,c \in \mathbb{N}$, then the following conditions are satisfied, we can show that division is an equivalence relation. 
* $a|a$, satisfies reflexivity
* If $a|b$ and $b|c$ then $a|c$  
* If $a|b,b|a$ then $a=b$ 

We can prove that if $a|b,b|c$ that $\exists m,n \in \mathbb{N}$ s.t.:
$$b=am, c=bn$$
So $c=(am)\cdot n = a(mn) \text{ (associativity) } \implies a|c$. 

We can show that the result is [[anti-symmetric]] as well.
Suppose that $a|b$ and $b|a$. Then, $\exists x,y \in \mathbb{Z}$ s.t.:
$$ax=b,by=a$$
But notice that we can substitute $b$ into the right side identity:
$$by=axy=a(xy)=a$$
$$\iff a(xy)-a=0 \iff a(xy-1)=0$$
Since $a\neq 0$, then $xy-1=0$ so $xy=1 \implies x=y=1$. This is because $a,b \in \mathbb{N}$ so $x,y \in \mathbb{N}$, thus:
$$a\cdot 1 = b \iff a = b$$
---
# More Divisibility Rules:
For $a,b,d,x,y \in \mathbb{Z}$ (non-zero as needed)
* If $d|a \wedge d|b \implies d|(ax+by)$ 
* If $d|a \implies dx|ax$
* If $dx|ax \implies d|a$
* If $d|a \implies \frac{a}{d}|a$ 

Proofs
1. $d|a, d|b, \implies \exists e,f \in \mathbb{Z}: a=de, b=df$ so: $$(aed+bfd)=d(ac+bf) \implies d|(ax+by)$$
2. If $d|a \implies \exists e$ s.t. $de=a$, then: $$ax=dex=(dx)a\implies dx |ax$$
3. If $dx|ax \implies dx=eax \implies eax-dx=0 \implies  x(ea-d)=0 \implies$ but $x \neq 0$ so $ea-d=0 \implies ea=d \implies$ divisible by both $x$ and $d$. 
4. If $d|a \implies de=a \implies e =\frac{a}{d}$, since $e \in \mathbb{Z}$ this is okay, then $a=de=d\frac{a}{d} \implies \frac{a}{d} | a$. 
---
# The [[Division Algorithm]]
Suppose $a \in \mathbb{Z}$, and $b \in \mathbb{N}$. Then $\exists! q,r, \in \mathbb{Z}$ s.t. $a=bq+r$ for $0 \leq r < b$. 
Consider $A=\{a-bx|x \in \mathbb{Z} \} \cup \mathbb{N}$.  