---
title: Exterior Derivatives and Differential Forms
draft: "False"
tags:
  - Calculus
---
# Exterior Derivatives 
We can view [[Exterior Derivative]]s as an extension of [[Fundamental Theorem of Calculus]] and the [[Fundamental Theorem of Calculus for Line Integrals]]. We should be able to generalize these ideas to the $n$th degree. Some operations, such as the [[Cross Product]] cannot be generalized to higher dimensions. So, we want to try and generalize the language we use to talk about derivatives and the differential forms of the [[Curl]], [[Divergence]], [[Line Integral]], and [[Gradient]]. 

We want to introduce the notion of forms. For instance a one form is of the $Pdx+Qdy$ is a 1 form (I assume because this is a scalar). Secondly we have two forms which for example are of the form $F dxdy$. 

We can consider an $n$ form from this previous notion. We want to define an operator $d$ which takes an $n$ form to an $n+1$ form. 

For instance we could take the curl:
$$\omega = Pdx+Qdy$$
Then:
$$d\omega = \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)dxdy$$
Using this notation, we can express [[Green's Theorem]] as:
$$\int_{\partial D} \omega  = \int_{D} d \omega$$
We can think of this as an operation which switches the boundary of $D$, $\partial D$ with the volumetric region of $D$. 

### 0-Forms 
Let $K$ be an open set in $\mathbb{R}^3$. A $0$-Form on $K$ is a real valued function, $f : K \to \mathbb{R}$. If we can differentiate $f$ once it is of class $C^1$ and if we can differentiate $f$ twice then it is of class $C^2$. 

We can add two 0 forms together to obtain a new one and we can multiply them in order to obtain a new $0$ form, for instance consider two 0 forms of the form:
$$f_{1}(x,y,z) = xy +yz$$
$$f_{2}(x,y,z) = y\sin(xz)$$
Then:
$$(f_{1}+f_{2})(x,y,z)= xy+yz+y\sin(xz)$$
And:
$$(f_{1}f_{2})(x,y,z)=y^2x\sin(xz)+y^2z\sin(xz)$$



