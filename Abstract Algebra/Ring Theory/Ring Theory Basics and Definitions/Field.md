---
title: Field
tags:
  - AbstractAlgebra
draft: "False"
---
# Field
A [[Field]] is a [[Ring]] where $\forall a \in R, a \neq0, \exists a^{-1},aa^{-1}=a^{-1}a=1$ where $1$ is an [[Identity Element]] under multiplication. 

Every [[Field]] is also necessarily an [[Integral Domain]] since every field is commutative, has no [[Zero Divisor]]s, and has a unit. 

---
### Example 9). A [[Field]] with $9$ Elements 
$$\mathbb{Z}_{3}[i]=\{ a+bi :a,b \in \mathbb{Z}_{3}\} $$
$$=\{0,1,2,i,1+i,2+i,2i,1+2i,2+2i \}$$
Is the ring of Gaussian integers mod $3$. This set can be confirmed to be a field by writing its Cayley table out we can observe that it satisfies all of the properties of a Field. 

### Example 11.) $\mathbb{Q}[\sqrt{ 2 }]=\{ a+b\sqrt{ 2 } :a,b \in \mathbb{Q} \}$
This is clearly a ring which is commutative and has an identity element. It can also be shown that this is a [[Field]]. If $a+b\sqrt{ 2 }\neq0 \in \mathbb{Q}[\sqrt{ 2 }]$, then:
$$\frac{1}{a+b\sqrt{ 2 }}=\frac{1}{a+b\sqrt{ 2 }} \cdot \frac{a-b\sqrt{ 2 }}{a-b \sqrt{ 2 }} = \frac{a}{a^2-2b^2} -\frac{b}{a^2-2b^2} \sqrt{ 2 } $$
Which is defined always for any $a,b \in \mathbb{Q}$. 
