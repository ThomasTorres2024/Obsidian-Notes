---
title: Linear First Order Differential Equations
tags:
draft: "false"
---
# Linear First Order Differential Equations 
We are interested in finding the $y$ that satisfies [[Ordinary Differential Equation]]s of the following form given that $y$ is linear and of the first order:
$$y'+p(x)y=q(x)$$
Notice that this is the general form of any first order linear differential equation. We can derive this expression by first considering a more simple version of the question for all linear first order [[Homogeneous Differential Equation]]s of the form:
$$y'+p(x)y=0$$
Since the equation is separable we can write:
$$\frac{dy}{dx}+p(x)y=dy+dx\cdot p(x)y=0$$
$$\frac{dy}{y}+p(x)dx=0$$
$$\ln(y)+C=-\int p(x)dx \iff y=A\exp\left(-\int p(x)dx\right)$$
To extend this idea to all first order linear equations, we instead consider the "Method of Integrating Factor". Let $I(x)$ be a function defined by:
$$I(x)=\exp\left( \int p(x)dx \right)$$
Multiple both sides of the general form of the DE by $I(x)$:
$$I(x)y'+p(x)I(x)y=q(x)I(x)$$
Notice that $p(x)=\frac{d}{dx} \int p(x)$, so we are able to express this DE using the [[Product Rule]] from calculus. Let $p(x)I(x)=\frac{d}{dx}I(x)$ so, we can express our equation as:
$$\frac{d}{dx}\left[ y\cdot I(x) \right]=\frac{d}{dx}\left[ y\cdot \exp\left( \int p(x)dx \right) \right]=  q(x)I(x)dx$$
Then by the [[Fundamental Theorem of Calculus]]:
$$\iff  y\cdot I(x)=\int q(x)I(x)dx \iff y=\frac{\int q(x)I(x)dx}{I(x)}$$
For the original differential equation:
$$y+y'p(x)=q(x)$$
We can conclude that:
$$\textcolor[RGB]{153, 115, 235}{\boxed{ \therefore y= \frac{(\int q(x) \exp (\int p(x))dx)+C}{\exp(\int p(x))} }}$$
Also, just to reiterate:
$$\textcolor[RGB]{153, 115, 235}{\boxed{\therefore I(x)=\large  \exp\left( \int p(x)dx\right)}}$$