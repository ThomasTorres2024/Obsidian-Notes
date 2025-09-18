---
title: Non-Independent Variables
tags: 
draft: "false"
---
# Non-Independent Variables Definition
Some functions actually have variables which are related to one another. In physics, we have the ideal gas law which states that for the function $f : \mathbb{R}^3 \rightarrow \mathbb{R}$ we have that $pV=nRT$ which can be used to substitute into a function to simplify it and express it in terms of only too. 

We also need to know how to work with rates of change in situations where our variables are not independent. 

More generally, if we think of some $f(x,y,z)$ with a function that relates the variables given by $g(x,y,z)=c$. If we have that the functions for $x,y,$ and $z$ are related, ideally we would be able to solve for one such function and be able to express it only using 2 variables. We may not always be able to solve directly, but if we have a function that relates the two sets, we might be able to relate them without having to do any solving. 

#### Example: 
Let us consider $g(x,y,z)=x^2+yz+z^3=8$ at the point (2,3,1). The differential of this constraints yields:
$$dg=2xdx+zdy+(y+3z^2)dz=0$$
We would be able to obtain this derivative by either implicitly differentiating the function, or by using the definition of the differential. After we plug in the point we get:
$$4dx+dy+6dz=0$$
We are able to move our derivatives to other sides and then express our differentials with respect to one another. We can move $dz$ to the other side to see how much we will change with respect to $dx$ and $dy$ and so on. If we want to interpret $z$ as a function of $x,y$ given by $z=z(x,y)$ then we can express our $dz$ as:
$$dz=-\dfrac{1}{6}(4dx+dy)$$
This is enough information to obtain our partial derivatives:
$$\dfrac{\partial z}{\partial x} = -\dfrac{2}{3} \text{ and } \dfrac{\partial z}{\partial y} = -\dfrac{1}{6}$$
# General Case 
Since our relation function, $g(x,y,z)=c$ then it follows that our [[differential]] will always be constant since $c$ is a constant, which gives us the following differential:
$$dg=g_{x}dx+g_{y}dy+g_{z}dz=0$$
We can thus express $dz$ as:
$$dz=\dfrac{-g_{dx}dx-g_{y}dy}{g_{z}}$$
We can think of our partial derivative as setting the function with respect to the opposite component to zero. For instance if we set $dy=0$ then we would get:
$$\text{if } dy=0 \implies dz=-\dfrac{g_{x}}{g_{z}}dx \text{ and thus } \dfrac{\partial z}{\partial x}=-\dfrac{g_{x}}{g_{z}} $$
$$\text{if } dx=0 \implies dz=-\dfrac{g_{y}}{g_{z}}dy \text{ and thus } \dfrac{\partial z}{\partial y}=-\dfrac{g_{y}}{g_{z}} $$
---
# Discrepancies in Change of Variables with Partial Derivatives 
Let us consider $f(x,y)=x+y$. Observe that $\dfrac{\partial f}{\partial x } = 1$. 

We can do a substitution on $x$ and $y$, let $x=u$ and let $y=u+v$. So, $f=x+y=2u+v$

If we then consider $\dfrac{\partial f}{\partial u}=2$. which gives us a contradiction since $u=x$, and our partials should be equal, not different. 

The subtlety here is that we are letting one variable to be treated as a non-constant in our partial derivative, and all others to be treated as constants. We are varying both $x$ and $u$ which is the same thing, but the variables we keep constant is where our error comes from. 

In conclusion we would get:
$$\dfrac{\partial f}{\partial x} \neq \dfrac{\partial f}{\partial u}$$Which is equivalent to keeping $y$ constant on the left while changing x, and on the right changing $u$ will keeping $v$ constant, but keeping v constant means keeping $y-x$ constant. In a case such as this, we need to be able to specify what is to be kept constant and what we vary, which requires new notation.

We will explicitly write what we are keeping constant on the outside of a set of brackets. Writing what we have above is equivalent to writing:
$$\left( \dfrac{\partial f}{\partial x} \right)_{y} \neq \left( \dfrac{\partial f}{\partial x} \right)_{v} = \left( \dfrac{\partial f}{\partial u} \right)_{v}$$
---
#### Example: Area of a Triangle
Consider the area of a triangle, given variables, $a,b,\theta$  where our area, $A$:
$$A=\dfrac{1}{2}ab\cdot \text{sin}(\theta)$$
Let us assume that $A$ is a right triangle. This would be equivalent to saying that:
$$a=b \text{ cos}(\theta)$$
This gives us our constraint. We want to determine how the area of our triangle changes as we vary $\theta$. 

We first have to define what our rate of change of $A$ with respect to $\theta$ actually means. If we think of $a,b,\theta$ as independent variables, then we can write out our [[differential]] simply as:
$$\dfrac{\partial A}{\partial \theta}=\left( \dfrac{\partial A}{\partial \theta} \right)_{a,b}=\dfrac{1}{2}ab\text{ cos}(\theta)$$
However, writing our differential out as this loses out on the fact that we are working with a right triangle. If we want to keep our right triangle, we can consider what happens we can examine what happens with $\theta$ when we vary $b$ and keep $a$ constant and vary $a$ and keep $b$ constant. 

If we keep $a$ constant and think of $b$ as a function of $a$ and $\theta$ then:
$$b=b(a,\theta)=\dfrac{a}{\text{cos}(\theta)}=a\text{ sec}(\theta)$$

If we keep $b$ constant and $a$ as a function of $b$ and $\theta$ then:
$$a=a(b,\theta)= \left(\dfrac{\partial A}{\partial \theta}\right)_{b}$$
There are 2 systematic methods to solve for $\left(\dfrac{\partial A}{\partial \theta} \right)_{a}$ that is provided in the lecture. We can do this using differentials. If we set $da=0$ and use our constraint that $a=b\text{ cos}(\theta)$ then it follows that:
$$da=\dfrac{\partial a}{\partial \theta} d \theta+\dfrac{\partial a}{\partial b} db=\text{cos}(\theta)db-b\text{ sin}(\theta)d\theta$$
It follows that:
$$db=\text{tan}(\theta)d\theta$$
In turn we can solve for $db$ and $d\theta$. Let us consider the differential of $A=\dfrac{1}{2}ab\text{ sin}(\theta)$:
$$dA=\dfrac{1}{2}b\text{ sin}(\theta)da+\dfrac{1}{2}a\text{ sin}(\theta)db+\dfrac{1}{2}ab\text{ cos}(\theta)d\theta$$
Since we set $da=0$ and we have a way to express $db$ in terms of $d\theta$ we can write the above as the following:
$$dA=\dfrac{1}{2}b\text{ sin}(\theta)da+\dfrac{1}{2}a\text{ sin}(\theta)db+\dfrac{1}{2}ab\text{ cos}(\theta)d\theta$$
$$dA=\dfrac{1}{2}a\text{ sin}(\theta)(b\text{ tan}(\theta))+\dfrac{1}{2}ab\text{ cos}(\theta)d\theta$$
$$dA=\dfrac{1}{2}ab\text{ sec}(\theta)d\theta$$
So in turn we get that:
$$\left(\dfrac{\partial A}{\partial \theta} \right)_{a}=\dfrac{1}{2}ab \text{ sec}(\theta)d\theta$$
Which makes sense since we are considering what happens when we treat $a$ as a constant, and vary $\theta$ and $b$, and we have a way to express $b$ in terms of $a$. 

We would also be able to get the same result if we applied the chain rule. 