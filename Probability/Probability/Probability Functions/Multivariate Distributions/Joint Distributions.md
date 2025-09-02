---
title: Joint Distributions
tags:
draft: "false"
---
# Joint Distributions Definition
[[Joint Distributions]] are distributions of the sum of multiple random variables. Let $X$ and $Y$ be [[Bernouli Trial]]s, possibly dependent or independent. Let us consider the distribution $X+Y$.

# Discrete Case 

The Joint [[Cumulative Density Functions]] is given by:
$$F(x,y) = \mathbb{P}[X \leq x, Y \leq y]$$
We also have a joint [[Probability Mass Function]] which is given by:
$$\mathbb{P}[X=x,Y=y]$$
If it is the case that $X$ and $Y$ are independent we would have that:
$$\mathbb{P}[X=x,Y=y] = \mathbb{P}[X=x]  \cdot \mathbb{P}[Y=y] $$
Which comes directly from the definition of [[Independent Random Variables]]. 

The [[Marginal Cumulative Density Function]] is the CDF when we only consider one random variable, either $X$ or $Y$ here. If we only consider $X$, it would be given by:
$$\mathbb{P}[X \leq x]$$
The product of the marginal CDFs also must be equivalent to the joint CDF:
$$f(x,y)=f_{x}(x) \cdot f_{y}(y)$$
In order to determine a [[Marginal Distribution]] all we would need to do is sum up the variable we are interested in finding the marginal for, $X$, over all possible values of $Y$:
$$\mathbb{P}[X=x]= \sum_{y} \mathbb{P[X=x,Y=y]}$$

---
# Continuous Case 
A joint [[Probability Density Function]] is given by the hypervolume of our random variables over some region, for instance in this case we would consider the volume over a 2 dimensional function:
$$\mathbb{P}[(x,y) \in B] = \iint_{B} f(x,y)dxdy$$
We say that $X$ and $Y$ are independent if and only if we can write the joint CDF as a product of the marginals:
$$F(x,y)=F_{x}(x)F_{y}(y)$$
The [[Marginal Distribution]], which is a [[Probability Density Function]], can be found in the continuous case via:
$$f_{y}(y) = \int_{-\infty}^\infty f_{x,y}(x,y)dx$$
Which is equivalent to integrating out the other value, since we want to determine the value over all other values of $x$.

The joint [[Cumulative Density Functions]] of a PDF, $F(x,y) = \mathbb{P}[X \leq x, Y \leq y]$, then we can determine the PDF by doing the following:
$$f(x,y) = \frac{\partial^2}{\partial x \partial y}$$
For any valid joint distribution, it must be the case that :
$$\iint_{A}f(x,y)dxdy=1$$
The [[Conditional Distribution]] of $Y|X$ is:
$$f_{Y|X}(y|x) = \frac{f_{x,y}(x,y)}{f_{x}(x)}$$
This looks quite similar and is derived from [[conditional probability]]. We basically obtain the conditional distribution by dividing by the marginal density. We also have something similar to [[Bayes' Rule]]:
$$f_{Y|X}(y|x) = \frac{f_{x,y}(x,y)}{f_{x}(x)} = \frac{f_{X|Y}(x|y)f_{y}(y)}{f_{x}(x)}$$
We also have a test for independence using the PDFs:
$$f_{x|y}(x,y)=f_{x}(x)f_{y}(y)$$
#### (Example) Joint Uniform Distribution, Independence 
Let us consider a [[Uniform Distribution]] over the unit square. where $x,y \in [0,1]$ where the probability of anything within the unit square is $c$ and 0 otherwise. 

We can determine $c$ by doing $\frac{1}{\text{Area}(R)}=1$, which turns out to just be 1 since the area we are looking over has an area of one. Marginally, our $X$ and $Y$ are independent values where $X$ and $Y$ are both uniform between $[0,1]$, which is fairly intuitive. 

#### (Example) Joint Uniform Distribution, Dependence
If we consider the region of a unit disc, given by $x^2 + y^2 \leq 1$ and we have that our distribution is uniform. We want to find the marginal distributions. The joint PDF has a uniform distribution, so we must have a probability of 1 over the probability, which is $\frac{1}{\pi}$. 

We should be able to see that $x$ and $y$ are very dependent. We know that if we have some $x$ which is close to $1$, we know that $y$ is very constrained, and that it must be very close to the edges around $1$. The values here are heavily dependent values.

The PDF for this function is, for $x,y \in \{x,y : x^2 + y^2 \leq 1 \}$, $f(x,y) = \frac{1}{\pi}$ and else 0. 

We can compute the marginal distributions for this distribution by doing integrals. We need to determine the bounds of integration when finding the marginal of y. We can see that our bounds will be given by:
$$y^2 \leq 1 - x^2$$
So, we have that our bounds are $\pm \sqrt{1-x^2}$. 
$$f_{x}(x) = \int f(x,y) dy = \int_{\sqrt{1-x^2}}^{\sqrt{1-x^2}} \frac{1}{\pi}dy =  \frac{2 \sqrt{1-x^2}}{\pi} : -1 \leq x \leq 1$$
We can see that our [[Marginal Distribution]]s are not uniform. By symmetry we have that our conditional distribution for $y$ is:
$$f_{y}(y) = \frac{2\sqrt{1-y^2}}{\pi} : -1 \leq y \leq 1$$
We can also find the conditional distribution given that $-\sqrt{1-x^2}\leq y \leq \sqrt{1-x^2}$ and that $x \in [0,1]$, then we have that:
$$f_{y|x}$$