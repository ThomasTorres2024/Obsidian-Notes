---
title: Multivariable Functions
tags:
draft: "false"
---
# Multivariable Functions Definition
We are interesting in functions over the reals, more specifically in functions of the form:
$$F:U \subseteq \mathbb{R}^n \to \mathbb{R}^m$$
Which take [[vector]]s in some region of $\mathbb{R}^n$ and map to some subset of $\mathbb{R}^m$. We can define the [[Graph]] of a function as the set of all of a functions inputs and outputs, more specifically as the set given by:
$$\text{graph of } F=\{(\vec{x},F(\vec{x}) \in \mathbb{R}^{m+n}  : \vec{x} \in U \}$$
The [[Contour]] or [[Level Set]] of value $c \in \mathbb{R}$ is the set where, for a function $f : \mathbb{R}^n \to \mathbb{R}$:
$$\text{contour of } c =\{ \vec{x} \in U : f(\vec{x})=c \} \subset \mathbb{R}^n$$
A level set is a [[Level Points]] if $n=1$,[[Level Curve]] if $n=2$, and a [[Level Surface]] if $n=3$. This is a collection of all points where the function achieves the value $C$. We are interested in this particular idea because it helps us visualize and work with functions that have graphs in $\mathbb{R}^3$, because their functions are very complicated. [[Level Set]]s allow us to see how our function works. For instance consider when $f(x,y)=x^2+y^2$. The level curve at different levels of $c$ will be given by a set of concentric circles centered at the origin:
![[Pasted image 20250912174119.png]]
Another example of a function of this type is $f(x,y)=x^2-y^2$. When we take its level curves, we get a family of hyperbolas that degenerate into straight lines through the origin:
![[Pasted image 20250912174239.png]]

---
# Visualizing Multivariable Functions
For each function that has a graph in $\mathbb{R}^2,\mathbb{R}^3,\mathbb{R}^4$, we have techniques to visualize functions in these dimensions. To visualize graphs in $\mathbb{R}^2$, we just would graph them, these functions are relatively simple. To visualize graphs in $\mathbb{R}^3$, we can graph them, which would be hard, so instead we determine different contours of our set which greatly reduces their complexity. 

A graph in $\mathbb{R}^4$ can only be comprehended by contours. 
![[Pasted image 20250912174753.png]]

We can also interpret our functions and their graphs as contours of higher dimensional functions. 
* Consider $y=f(x)$. We can interpret this as the level curve of a multivariable function given by $z=f(x)-y$ when $z=0$.
* The function $z=f(x,y)$ can be thought of as the contour of $w=f(x,y)-z$ when $w=0$ as well 
