---
title: Polynomial Ring
tags:
  - AbstractAlgebra
draft: "False"
---
# Polynomial Ring
A [[Polynomial Ring]] is a [[Ring]] over some 

---
# Theorem - Every [[Ideal]] in $k[x]$ is a principal ideal. 
Suppose $I \subseteq k[x]$ is an [[Ideal]]. Take $p(x) \in I$ such that $p(x)$ is a [[Monic Polynomial]] and that $\text{deg}(p(x))$ is minimal over all polynomials of positive degree, which ensures that $p(x)$ is not a constant [[Polynomial]]. We want to show that $p(x)$ generates the entire [[Ideal]]. 

Suppose that $f(x) \in I$ and we can use the [[Polynomial Division Algorithm]] to express:
$$f(x)=p(x)q(x)+r(x) \quad 0 \leq \text{deg}(r(x)) < \text{deg}(p(x)) $$

Since $p(x)$ is assumed to have minimal degree so we have that  $\text{deg}(r(x))=0$.  From this we obtain $2$ cases, that either $r(x)=0$ or $r(x) \neq 0$. 

### Case 1.) $r(x)=0$
In this case, we have that $f(x) \in I \implies f(x)=p(x)q(x) \implies f(x) \in \langle p(x) \rangle$ and thus since $f(x)$ is arb. we have that $I \subseteq \langle p(x) \rangle$, and we also know that $p(x) \in I$ by assumption and thus $\langle p(x) \rangle \subseteq I$.

### Case 2.) $r(x) =\alpha \neq 0$
Since $k$ is a [[Field]] then $\alpha$ is a [[Unit (Ring Theory)]]. Since we have a unit $\alpha$ in the [[Ideal]], then the whole [[Ring]] must be contained in the ring and thus we have that:
$$\langle p(x) \rangle = k[x]$$
This concludes the proof. 

### $\textcolor{red}{\text{Example: }}$ - $\mathbb{Z}[x]$ is not a PID. 
Let the following:
$$I=\langle x , 2 \rangle = \langle a_{n}x^n+a_{n-1}x^{n-1}+\cdots+a_{1}x+2a_{0} : a_{i} \in \mathbb{Z} \rangle $$ Suppose that $p(x) \in\mathbb{Z}[x]$ with $\langle p(x) \rangle = I =\langle x,2 \rangle$. Then:
$$2 \in \langle p(x) \rangle \implies 2 = p(x)f(x) \quad f(x) \in \mathbb{Z}{x}$$
However this entails that:
$$\text{deg}(p(x))=\text{deg}(f(x))=0$$
Which means that both $p(x)$ and $f(x)$ are constant polynomials. This means that $p(x)=1$ or $p(x)=2$. But if $p(x)$ were $1$ then it would entail that the entire Ring is equal to the ideal, which is not the case (trivially true since the constant term need not be even). This forces $p(x)=2$. 

But, since $p(x)=2$, then we have that $x$ is a multiple of $2$ but this is clearly not true, and since $x$ is one of the generators of the [[Ideal]] it follows that  $\mathbb{Z}[x]$ is __not__ a [[Principle Ideal Domain]]. 