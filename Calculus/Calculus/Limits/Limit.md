---
title: Limit
tags:
draft: "false"
---
# Limit Definition
Consider the function $f : U \subseteq \mathbb{R} \to \mathbb{R}$, and $a \in U$. We want to know the value that our function approaches as $x \to a$. We want to know what the value should converge to intuitively, and the value our function tends towards is given by $\mathcal{L}$. The standard notation for a limit addresses $$\lim_{x \to a} f(x) = \mathcal{L}$$We have two conditions to satisfy in order for our limit to exist in the one dimensional case. We can approach $a$ by the left, $x\to a^{-}$ and through the right, $x \to a^{+}$. If these limits are equal it follows that our limit exists. Therefore the following must be true in the scalar case:
$$\lim_{x \to a^{-}} f(x) = \mathcal{L}=\lim_{x \to a^{+}} f(x) \iff \mathcal{L}=\lim_{x \to a} f(x) = \mathcal{L}$$

Visually, this is what we need to find along a graph. 
![[Pasted image 20250912124004.png|500]]

---
# [[Epsilon-Delta Limit]] Definition 
The epsilon-delta definition of a [[Limit]] is a more rigorous definition of the limit. Our more concrete idea of approaching a value is to specify that at a point $a \in \mathbb{R}$, we can specify some $\delta$, which gives a neighborhood around $a$ in which every value of our function is constrained by the length between some $f(x)-\mathcal{L}$, where $\mathcal{L}$ is our limit, and $x \in (a-\delta,a+\delta)$. To put all of this together here is a graphic and a definition for a limit existing that we can make use of:

![[Pasted image 20250912125121.png]]
Here we see that we can constrain our $x$ to be along the interval $(a-\delta,a+\delta)$, which then constrains the output value for $y$ by to be in the interval $(l-\epsilon,l+\epsilon)$. More rigorously, our function $f(x)$ can get arbitrarily close to $L$ by taking values of $x$ which are closer and closer to $a$. 

This gives us enough background to give the definition of the epsilon-delta limit:
$$ \text{limit of a function exists at } a \iff \forall \delta >0, \exists \epsilon | \text{ }0 <|x-a| < \delta \implies 0 < |f(x)-\mathcal{L}| < \epsilon  $$
Again, we specify that if the limit exists, we need there to be some little interval around our point $a$ where if our $x$ comes closer to $a$, then our function value $f(x) \to \mathcal{L}$. 

---
# Structure of Delta Epsilon Proofs
We can prove delta epsilon limits by first letting that $\epsilon > 0$, and then supposing that $0 \leq |x-a| < \delta$
. We want to use this supposition to then argue that $0<|f(x)-\mathcal{L}| < \epsilon$. Often, what happens is we want to get our function minus the limit into a form where we bring up our $|x-a|$ again, and we can then put $\delta$ in front of it. We can then find an $\epsilon$ in terms of $\delta$ since by the chain of inequalities we worked through, it should follow that $|f(x)-\mathcal{L}|$, and we get some $\delta$ out of it, and if we equate $\epsilon$ here to the whole thing we would get that $\epsilon > |f(x)-\mathcal{L}|$, which is what we wanted to prove. Therefore, by expressing our $\epsilon$ in terms of $\delta$, if it is possible, would give us conditions sufficient to satisfy our Delta-Epsilon limit. 

---
# Alternative Definition for the Limit

Another useful way to think of limits is:
$$\lim_{x \to a} f(x) =b \iff \text{As } x \to a, f(x) \to b$$
Which is to say that as our value $x$ tends towards the limiting point, our $y$ value also tends towards the limiting point.

---
# Notes on the Limit
1. Intuitively, we can make $F(x)$ arbitrarily close to $\mathcal{L}$ by taking $x$ closer to $x_{0}$, but never actually at $x=x_{0}$, this is something that does not interest us in finding the limit of a function
2. If there is no such limiting point $B$ that satisfies the limit definition, then the limit does not exist 
3. $\lim_{x \to a} \text{ means that } x \text{ is very close to } x_{0}, \text{but } x\neq x_{0}$
4. If the limit exists, then the limit is unique

---
# Limit Properties 
Let $\lim_{x \to x_{0}} F_{1}(x)= b_{1}$ and $\lim_{x \to x_{0}} F_{2}(x)= b_{2}$
1. $$\lim_{x \to x_{0}}c\cdot F_{1}(x)=c\cdot b_{1}$$
2.  $$\lim_{x \to x_{0}} F_{1}(x) + F_{2}(x)=b_{1}+b_{2}$$
3. If $f$ is a scalar function:  $$\lim_{x \to x_{0}}\cdot F_{1}(x)\cdot F_{2}(x)=b_{1}\cdot b_{2}$$
4. If $f$ is a scalar function:
 $$\lim_{x \to x_{0}}  \frac{F_{1}(x)}{F_{2}(x)}=\frac{b_{1}}{b_{2}} \text{(if } b_{2} \ne 0\text{)} $$
 5. For $F(x) = (f_{1}(x),f_{2}(x),\cdots,f_{n}(x)) \in \mathbb{R}^n$ and $b = (b_{1},b_{2},\cdots,b_{m}) \in \mathbb{R}^m$: $$\lim_{x \to x_{0}} F(x)=b \iff \lim_{x \to x_{0}} f_{i}(x)$$
 