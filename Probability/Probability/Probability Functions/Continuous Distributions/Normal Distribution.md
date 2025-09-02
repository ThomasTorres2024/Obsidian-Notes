---
title: Normal Distribution
tags: 
draft: "false"
---
# Normal Distribution
The normal distribution, denoted $\mathcal{N}$, is the most famous distribution. It is the most famous because of the [[Central Limit Theorem]], which tells us that the addition of many [[Independent Random Variables]], then our distribution will resemble the [[Normal Distribution]].

These could be [[Discrete Distributions]] or [[Continuous Distributions]], but they add up to this one. This is what the theorem tells us. 
![[Normal_Distribution_PDF.svg.png]]
# The Standard Normal Distribution
The [[Standard Normal Distribution]] is given by $X$ ~ $\mathcal{N}(0,1)$, which tells us that this distribution has an [[Expected Value]] of 0 and a [[standard deviation]] of 1. 

The PDF of the standard normal given by:
$$f(z) = \frac{1}{\sqrt{2 \pi}} e^{\frac{-z^2}{2}}$$
The fraction at the start is a normalization constant, which we obtain by using a [[Taylor Series]] to do an approximation, or we use [[Polar Integration]]. This gives us our desired result. 

We can compute the [[Expected Value]] of the [[Standard Normal Distribution]] using the formula and property of integral of odd functions:
$$\int_{-\infty}^\infty \frac{z}{\sqrt{2 \pi}} e^{\frac{-z^2}{2}}=0$$
We can compute the [[Variance]] of the [[Standard Normal Distribution]] using the formula and property of integral of even functions, which turns out to be 1:
$$\int_{-\infty}^\infty \frac{z^2}{\sqrt{2 \pi}} e^{\frac{-z^2}{2}}=\int_{0}^\infty \frac{2z^2}{\sqrt{2 \pi}} e^{\frac{-z^2}{2}}$$
The [[Standard Normal Distribution]] has a CDF with its own name. We denote it by $\Phi(z)$:
$$\Phi(z) = \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^z e^{\frac{-t^2}{2}}dt$$
This CDF is calculated using tables or numerical methods. 

We also have the following property of its CDF:
$$\Phi(-z)=1-\Phi(z)$$
Intuitively, lets consider the [[Probability Density Function]] of the [[Standard Normal Distribution]]:
![[Pasted image 20250821061200.png]]
If we want to find $\Phi(-2)$, we could do it by doing $1-\Phi(2)$ since the little flap on both sides is symmetric, and basically what we are doing is getting the flap on the side when using this formula. 

---
# The General Normal Distribution
The general normal distribution is given by $X$ ~ $\mathcal{N}(\mu,\sigma^2)$ where $\mu$ is the [[Expected Value]] and $\sigma$ is the [[standard deviation]]. 

We have one [[Standard Normal Distribution]] that we can use to describe all other normal distributions by specifying a mean value and standard deviation. If we let $Z$ ~ $\mathcal{N}(0,1)$ then we can describe any $X$ by:
$$X=\mu + \sigma Z$$
The [[Expected Value]] of this result is simply $\mathbb{E}[X]=\mu$. Using the properties of [[Variance]], we should be able to see that $\mathbb{V}[X]=\sigma^2 \mathbb{V}[Z]=\sigma^2$. In conclusion, the two parameters that we feed into our distribution are indeed the [[Expected Value]] and the [[Variance]]. 

We can also express our [[Standard Normal Distribution]] in terms of our General Normal distribution by re-arranging some values:
$$Z=\frac{X-\mu}{\sigma}$$
This is known as [[Standardization]]. This is very useful transformation and a very simple one. This also takes out the units we are working with, which makes interpretation much nicer. 

---
# [[Probability Density Function]] of the Normal Distribution
Let us consider the [[Cumulative Density Functions]] of a general normal distribution, $X$:
$$\mathbb{P}[X \leq x ] = \mathbb{P} \left[ \frac{X-\mu}{\sigma} \leq \frac{x - \mu}{\sigma} \right] = \mathbb{P} \left[ Z \leq \frac{x - \mu}{\sigma} \right] = \Phi \left(\frac{x-\mu}{\sigma}\right) $$
We perform [[Standardization]] on both our $X$ and $x$. We can write the thing on the left as $Z$, however we immediately know that this is just the CDF for the [[Standard Normal Distribution]] with a different parameter.

To find the [[Probability Density Function]], all we would need to do now is take the derivative using the chain rule of the CDF of the standard normal. Since this function does not have an elementary representation, we can just cut to the chase and use its PDF with this parameter substituted inside of it:
$$\frac{d}{dx} \Phi \left(\frac{x-\mu}{\sigma}\right) = \frac{1}{\sigma \sqrt{2 \pi}} e^\left( -\left(\frac{x-\mu}{\sigma} \right)^2 \cdot \frac{1}{2} \right)$$
This gives us the [[Probability Density Function]] of the [[Normal Distribution]] as:
$$f_{x}(x)= \frac{1}{\sigma \sqrt{2 \pi}} e^\left( -\left(\frac{x-\mu}{\sigma} \right)^2 \cdot \frac{1}{2} \right)$$
---
# Identities Involving the Normal
Consider the normal distribution $X$ when we invert it, that is consider $-X$. We can define it as:
$$-X=-\mu + \sigma \cdot -Z \text{ = } \mathcal{N}(-\mu,\sigma^2) $$

We also have that given normal distributions $X_{1}$ and $X_{2}$ that:
$$X_{1}+X_{2}=\mathcal{N}(\mu_{1}+\mu_{2},\sigma_{1}^2+\sigma_{2}^2)$$
We also have for $-X_{2}$ that:
$$X_{1}-X_{2}=\mathcal{N}(\mu_{1}-\mu_{2},\sigma_{1}^2+\sigma_{2}^2)$$

---
# 68-95-99.7 Rule 
A description that a point is some number of standard deviation from the mean. If $x$ is within one standard deviation of the mean, which is to say that our data point has a chance of being constrained by some number of standard deviations from the mean:
$$\mathbb{P}[|x-\mu|< \sigma] \approx 0.68$$
$$\mathbb{P}[|x-\mu|< 2\sigma] \approx 0.95$$
$$\mathbb{P}[|x-\mu|< 3\sigma] \approx 0.99.7$$
![[1_empirical-rule.webp]]

---
# [[Standard Normal Distribution]] [[Moment Generating Function]]
Let $Z$  ~ $\mathcal{N}(0,1)$. Our $M(t)$ is given by:
$$M(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty e^{tz - \frac{z^2}{2}}$$
We can complete the square in the power, which allows us to solve the integral. 
$$ = \frac{e^{\frac{t^2}{2}}}{\sqrt{2\pi}} \int_{-\infty}^\infty e^{\frac{1}{2}(z -t)^2}dz$$
Using u sub we can convert this to the standard [[Gaussian Integral]], which cancels out our area, which leaves a nice MGF of:
$$M(t)=e^{\frac{t^2}{2}}$$
From this we can derive the Nonstandard [[Normal Distribution]]'s MGF:

#### Further Calculation of Higher Moments 
We can calculate further moments of $Z$. We know that by integrating odd functions that for $n$ is odd that $\mathbb{E}[Z^n]=0$. Even moments can be hard and very annoying to work with. We would much prefer to use the MGF. 


Given that our MGF is $M(t)=\text{exp}\left(\frac{t^2}{2}\right)$, subsequent derivatives of this function would be really annoying to do as $n \to \infty$. We want to apply the [[Taylor Series]] of our MGF to help ease calculations. Rewriting it in terms of the series we get:
$$M(t)= \sum_{n=0}^\infty \frac{(t^2/2)^n}{n!}=\sum_{n=0}^\infty \frac{t^{2n}}{n!2^n}$$
There is a bit of mismatch going on here that we want to be able to resolve, we can resolve it by multiplying the numerator and denominator evenly:
 $$=\sum_{n=0}^\infty \frac{t^{2n} \cdot (2n)!}{n!\cdot (2n)! \cdot2^n}$$
 Notice that this is very close to $\mathbb{E}[Z^{2n}]$. Seeing this, we can extract the coefficients that are not apart of this moment, and we can obtain:
 $$=\frac{2n!}{2^n\cdot n!}$$
 In total we get that:
 $$M(t)=\frac{(2n)!}{2^n \cdot n!}$$
 