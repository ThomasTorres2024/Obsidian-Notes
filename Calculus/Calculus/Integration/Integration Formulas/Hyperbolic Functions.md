The hyperbolic functions are define from hyperbolic cosine and hyperbolic sine respectively. These functions have many properties that are similar to cosine and sine, and have intimate connections with their definition and [[Euler's Identity]]. 

We define $\text{sinh}$ and $\text{cosh}$ in the following:
 $$\text{sinh}(x)=\dfrac{e^x-e^{-x}}{2}$$
  $$\text{cosh}(x)=\dfrac{e^x+e^{-x}}{2}$$
  Notice that $\text{cosh}(x) > 0 \forall x \in \mathbb{R}$, and that $\text{sinh}(x)$ has negative and positive values. If we use the [[Taylor Series]] definition of $e^x$ and $e^{-x}$ we can expand our function to obtain Taylor Series for them:
  $$\text{sinh}(x)=\dfrac{\sum_{i=0}^n \frac{x^i}{i!} - \sum_{i=0}^n \frac{(-x)^i}{i!}}{2}=\sum_{i=0}^n \dfrac{x^{2i+1}}{(2i+1)!}$$
$$\text{cosh}(x)=\dfrac{\sum_{i=0}^n \frac{x^i}{i!} + \sum_{i=0}^n \frac{(-x)^i}{i!}}{2}=\sum_{i=0}^n \dfrac{x^{2i}}{(2i)!}$$
These look a lot like the Taylor Series for cosine and sine except if every term in the series happened to be positive and contained no signed entries. 

Let us recall that we can define our cosine and sine functions using [[Euler's Identity]]. We will shortly be able to see a connection between these functions and the hyperbolic functions:
 $$\text{sin}(x)=\dfrac{e^{xi}-e^{-xi}}{2i}$$
  $$\text{cos}(x)=\dfrac{e^{xi}+e^{-xi}}{2}$$
We can verify these identities by applying Euler's Identity and the even and odd properties of cosine and sine respectively:
$$\dfrac{e^{xi}-e^{-xi}}{2i} = \dfrac{\text{cos}(x)+i\text{sin}(x)-\text{cos}(-x)-i\text{sin}(-x)}{2i}=\text{sin}(x)$$
$$\dfrac{e^{xi}+e^{-xi}}{2} = \dfrac{\text{cos}(x)+i\text{sin}(x)+\text{cos}(-x)+i\text{sin}(-x)}{2}=\text{cos}(x)$$
We can define our hyperbolic cosine by substituting $xi$ into our argument of $x$ in our trig functions to obtain our desired answer:
$$\text{cos(xi)}=\dfrac{e^{(xi)i}+e^{-(xi)i}}{2}=\dfrac{e^{-x}+e^{x}}{2}=\text{cosh}(x)$$
We can interpret hyperbolic cosine as a rotation of the cosine function's domain by ninety degrees in the complex plane. To illustrate this, 

We can also do something similar for sine:
$$i\text{sin}(x)=i\dfrac{e^{(xi)}-e^{-(xi)}}{2i}=\dfrac{e^{xi}-e^{-xi}}{2}=\text{sinh}(iz)$$
Additionally we also have hyperbolic

---
# Derivatives and Integrals of Hyperbolic Functions

It can easily be shown that:
 $$\dfrac{d}{dx}\text{cosh(x)}=\text{sinh(x)}$$
$$\dfrac{d}{dx}\text{sinh(x)}=\text{cosh(x)}$$