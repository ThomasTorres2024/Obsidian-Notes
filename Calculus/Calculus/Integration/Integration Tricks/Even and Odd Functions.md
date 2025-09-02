---
title: Integration Tricks
tags: 
draft: "false"
---
# Even and Odd Function Integration Tricks 

We define an even function by the given function $f$ satisfying, $f(x)=f(-x)$ and an odd function $g$, satisfying $g(-x)=-g(x)$ 

For an $\textbf{odd}$ function $f$, its given definite integral is zero along the bounds of $a$ and $-a$. This is due to symmetry:

$$\int_{-a}^af(x)dx=F(a)-F(-a)=0$$

This is because some region of area under $f$ is negative from $(0,a]$ and  positive from $[-a,0)$ or vice versa. The areas thus cancel out. 

For an $\textbf{even}$ function $g$, its given definite integral along $a$ to $-a$, is really just two times the area from $[0,a]$. In conclusion we can write that:

$$\int_{-a}^a g(x)dx=2\int_{0}^ag(x)dx$$
---
# Integral  Bound Tricks 

$$\int_{a}^{-b}f(x)d(x)=-\int_{-b}^af(x)dx$$
--- 
# Special Functions

##### "Circle" or Semicircle Type integrals given by:

$$\text{ For a semi circle:}\int_{-r}^r\sqrt{r^2-x^2}dx=\dfrac{\pi r^2}{2}$$
$$\text{ For the fourth of a circle:}\int_{0}^r\sqrt{r^2-x^2}dx=\dfrac{\pi r^2}{4}$$
#### Reverse Product Rule
$$\int f'g + g'f = fg +c$$
Example:

$$\int e^x(x^5+5x4)=e^xx^5+C$$
 