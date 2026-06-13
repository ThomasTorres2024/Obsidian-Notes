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

---
# Theorem.) A Field Contains $\mathbb{Z}_{p}$ or $\mathbb{Q}$.  
If $F$ is field where $\text{char}(F)=p$, then $F$ contains a subfield isomorphic to $\mathbb{Z}_{p}$, and if $\text{char}(F)=0 \implies F$ contains a subfield isomorphic to $\mathbb{Q}$. 

$Proof.)$
By a theorem of [[Ring Homomorphism]]s, then we have that for any ring with unity, that the ring contains either $\mathbb{Z}_{n}$ or $\mathbb{Z}$ where $n=\text{char}(R)$. Automatically we can say that $\text{char}(F)=p \implies \mathbb{Z}_{p} \leq F$.  In the second case, we let $\text{char}(F)=0 \implies$
$$T=\{ ab^{-1} : a,b \in S, b\neq 0 \}$$
If $F$ is a field then we know that $b^{-1}$ exists and that it is non-zero, so this definition of $T$ holds. We want to then show that $\mathbb{Q} \cong T$. By the theorem that we used for the homomorphism, we can express that the following is an isomorphism of rings: 
$$\begin{align}
\phi: \mathbb{Z} \to F \\
k \mapsto k \cdot 1
\end{align}$$
Hence $S=\{k \cdot 1 : k \in \mathbb{Z} \}$. Let us define $\psi : \mathbb{Q} \to T$ and $\frac{p}{q} \mapsto \phi(p) \phi(q)^{-1 } \quad q\neq0 = (p\cdot 1)(q\cdot1)^{-1}$. 

It is necessary to show that $\psi$ is multiplicative, additive, surjective, injective, and well defined in order to complete the result. 

---
# Theorem.) The Field of Quotients
Recall that $\mathbb{Z}$ is not a field, but $\mathbb{Z} \subseteq \mathbb{Q}$, which is a field where every element of $\mathbb{Q}$ is a quotient of $2$ integers. This generalization can be constructed into the __"Field of Quotients"__. 

$Proof.)$
Let $D$ be an [[Integral Domain]]. Then, $\exists F$ a field called the field of fractions that contains a subring isomorphic to $D$. Let $s=\{(a,b) : a,b \in D, b\neq 0 \}$. 

We define the [[Equivalence Relation]] on $S$ by:
$$(a,b) \equiv (c,d) \iff ad=bc$$
Let $F$ be the set of equivalence classes of $S$ under "$\equiv$". Denote the equivalence class containing $(x,y)$ by $\frac{x}{y}$. We define $+, \cdot$ on $F$ by:
$$\frac{a}{b} + \frac{c}{d } = \frac{ad+bc}{bd}$$
$$\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$$
Since $D$ is an integral domain where $bd \neq0 \implies b\neq0, d\neq 0$ since this is an integral domain. We need to be able to show that the [[Equivalence Class]]es are well defined. 

In order to do this, suppose that $\frac{a}{b} = \frac{a'}{b'}$ and $\frac{c}{d} = \frac{c'}{d'}$ such that $ab'=a'b$ and $cd'=c'd$. Then we have that: 
$$\begin{align}
(ad+bc)b'd'=adb'd'+bcb'd' \\
=(a'b)dd'+(c'd)bb' \\
=a'd'bd+b'c'bd \\ 
=(a'd'+b'c')bd
\end{align}$$
This entails that:
$$\frac{ad+bc}{bd}=\frac{a'd'+b'c'}{b'd'}$$

And thus $+$ is well defined. Secondly we need to show that $\cdot$ is also well defined. Consider the following:
$$\frac{ac}{bd}=\frac{a'c'}{b'd'}$$
Now it needs to be shown that $F$ is a field. If $1$ is the unity of $D$, then an easy check is to show that $\frac{0}{1}$ is the additive identity of $F$ and $\frac{1}{1}$ is the multiplicative identity. 

The additive inverse of $\frac{a}{b}$ is $-\frac{a}{b}$ while the multiplicative inverse of a non-zero element $\frac{a}{b}$ is $\frac{b}{a}$. All we have to do is prove commutativity, which is trivial for addition since $+$ forms a group, and $\cdot$ forms multiplication which can be trivially checked to have the property. 

---
### Example ). 
Let $p$ be prime, then $\mathbb{Z}_{p}(x)=\left\{  \frac{f(x)}{g(x)} : f(x),g(x) \in \mathbb{Z}_{p}[x], g(x) \neq 0  \right\}$ is an infinite field of $\text{char}(\mathbb{Z}_{p})=p$ and is an infinite field.  