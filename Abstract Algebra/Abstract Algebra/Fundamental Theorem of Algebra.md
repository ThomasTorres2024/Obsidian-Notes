---
title: Fundamental Theorem of Algebra
tags:
draft: "False"
---
# Fundamental Theorem of Algebra Definition
The [[Fundamental Theorem of Algebra]] is a result for polynomials over $\mathbb{C}$, which states that for an $n$th degree [[Polynomial]] that we are guaranteed to have exactly $n$ roots over $\mathbb{C}$, and less than or equal to $n$ roots over $\mathbb{R}$. We can thus express any $n$th degree polynomial as the following product of complex numbers:
$$p(x)=\prod_{i=1}^n (x-r_{i})$$
It is also the case that not every root is a distinct root, as $x^2$ has two real valued roots at $x=0$, though the roots are repeated. $x^2+1$ has no real roots, but it has complex roots of $-i$ and $i$, so $x^2=(x-i)(x+1)$. 

The polynomial $p(x)$ with $k$ roots is divisible by its roots, since it can be expressed as a product of those roots. $p(x)$ must have a degree of at least $k$ since it is divisible by its $k$ roots. 

---
# Proof of the Theorem Using "Winding Numbers"
An equivalent statement to the fundamental theorem of algebra is that, every [[Polynomial]] has at least one [[root]]. This statement is easier to prove, and implies that every $n$th degree [[Polynomial]] has $n$ roots. 

#### (Corrolary) Every Polynomial Has 1 Root $\iff$ Every $n$th degree Polynomial has $n$ Roots over $\mathbb{C}$
Every $1$st degree polynomial can easily be shown to have 1 root algebraically. 

Inductively, let us assume that a polynomial of degree $n-1$ has $n-1$ roots over $\mathbb{C}$. Let $p(x)$ be an $n$th degree polynomial. This [[Polynomial]] has at least one root, let us call it $r_{n}$. It follows that it is divisible by its root, which must yield another polynomial of degree $n-1$ called $q(x)$:
$$\frac{p(x)}{(x-r_{n})}=q(x)$$
It follows that:
$$p(x)=q(x)(x-r_{n})$$
Which entails that $p(x)$ must have $n$ roots, since $q(x)$ has $n-1$ roots, and then the additional root giving $n$.  It can also easily be shown that if every $n$th degree polynomial has $n$ roots that it has at least one root, so these are thus equivalent statements. 

#### (Definition) Winding Number 
If we examine the graph of the input of $x^2$ and the output of $x^2$ as a disc, we would see that we rotate around the disc twice in the output, and once in the input (I believe this is because if we represent our points via a complex exponential, we are doubling the angle in the output so we can traverse it two times as fast). We can generalize this idea for $x^n$, which would result in us moving around the origin $n$ times while our input moves once. 

We call the number of rotations we make around the origin in one period the "winding number", $\text{wind}(u^n)=n$. 

If our output does not circle over the origin, say in $u+2$, we would have that $\text{wind}(u+2)=0$ since we never cross around 0. 

We would also see that for $2u^2-u-2$ that we would have two loops, but only one would go around zero, so we would only have a winding number of 1. 

If we continuously change a polynomial, $p(u)$ until we get $q(u)$ the winding number remains constant unless we cross over the origin itself. If our cycle passes through 0, this means that we have an undefined winding number. Passing through zero allows us to change the winding number of our function, it is the only way that can change.  

This tells us that if we continuously change $p(u)$ into $q(u)$ and if $\text{wind}(p(u)) \neq \text{wind}(q(u))$ that we must have crossed through a zero at some point. There must have been a polynomial, $f(u)$ between $p(u)$ and $q(u)$ that set $f(r)=0$, meaning that we set $r$ to be a root. 

We want to be able to find $f(u)$ in order to show that every $p(x)$ has a root. We can find the root by generalizing the method of increasing the coefficient on $u$ in the input function $u$ and $u^2$ by adding a constant, $r$ in our functions, and letting $r=0$ and then seeing what happens when $r \to \infty$, as we want to be able to cover all points:
$$
\lim\limits_{r \to \infty} 
 p(ru) \to q(ru)$$
 This allows us to capture all roots. If we have a root, we will see it with this method. We have to worry about our polynomial blowing up to infinity. If our polynomial is of the form:
 $$a_{n}x^n + \cdots a_{1}x+a_{0}$$
 Then if $x^n = (ru)^n$ then as $r \to \infty$, our term blows up. If we divide our polynomial by $r^n$ then we adjust it and all other terms:
 $$\frac{p(ru)}{r^n}=\sum_{i=1}^n \frac{a_{n}r^nu^n}{r^n}$$
 Every term will go to 0 other than the first term as $r \to \infty$ as they are asymptotically larger than anything, and in the leading term we get $a_{n}$ still. As $\lim\limits_{r \to \infty}$ we get that:
 $$\lim\limits_{r \to \infty}  \frac{p(ru)}{r^n} = a_{n}u^n$$
 The function $a_{n}u^n$ is a circle centered at the origin of radius $a_{n}$ which wraps around $n$, and has a winding number of $n$. If we consider what happens when $r=0$ then we also blow up to infinity, so we need to be able to account for this. Our fix is instead to consider the polynomial given by:
 $$\frac{p(ru)}{r^n+1}$$
 Which is protected when $r=0$. When $r=0$, we get that our polynomial evaluates to $a_{0}$
, as all other terms have $x=ur$. Our original point when $r=0$ is just a fixed number, which indicates that we have a winding number of 0. 

By the end we have a winding number of $n$, which indicates that there is at least one point at which our winding number changes, which tells us that:
$$\frac{p(zu)}{z^n+1}=0$$
The bottom can never be zero, so the numerator must be zero, so this means that:
$$p(zu)=0$$
Which implies that [[Polynomial]] $p$ must have at least one root. The fact that our polynomial has a winding number of $n$ at the end corresponds to the polynomial having $n$ roots. 

---
# Sources 
The Fundamental Theorem of Algebra - https://www.youtube.com/watch?v=RBRVL6nP2Dk&t=104s

