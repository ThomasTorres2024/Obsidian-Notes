---

---

The [[Exponential Distribution]] is a [[Probability Density Function]] with one parameter known as the rate, $\lambda$, the rate at which an event occurs. We denote an exponential distribution by $X$ ~ $Exp(\lambda)$. 

The [[Exponential Distribution]] has [[Probability Density Function]] of:
$$f_{x}(x)=\lambda e^{-\lambda x} \text{ if } x > 0, \text{ else } 0$$
It is clear to see that $\forall x, f_{x}(x) \geq 0$ and that $\int_{0}^\infty \lambda e^{-\lambda x} =1$, so we can verify that this is a valid PDF. 

We also have the [[Cumulative Density Functions]] which is given by:
$$F(x) = \int_{0}^x \lambda e^{\lambda t }dt =  1 - e^{-x\lambda}, x>0$$
We can standardized the [[[Exponential Distribution]] much like how we standardized the [[Normal Distribution]]. Let $Y=\lambda X$, then $Y$ ~ $Exp(1)$. Let us consider the [[Cumulative Density Functions]] of $Y$:
$$\mathbb{P}[Y \leq y] = \mathbb{P}\left[X \leq \frac{y}{\lambda}\right]=1-e^{-y}$$
Thus, this is enough to show that $Y$ has an exponential CDF where $\lambda = 1$. We can now compute $\mathbb{E}[Y]$ using [[integration by parts]], which yields:
$$\mathbb{E}[Y]= \int_{0}^\infty ye^{-y}dy=1$$
The [[Variance]] can be calculated by using $\mathbb{E}[Y^2]-(\mathbb{E}[Y])^2$ and using the [[Gamma Function]]:
$$=\int_{0}^\infty y^2 e^{-y}dy-1= 1 $$
We can compute the general [[Expected Value]] now. Since we let $Y=\lambda X$, we have that $X = \frac{Y}{\lambda}$, so:
$$\mathbb{E}[X]=\mathbb{E}\left[\frac{Y}{\lambda}\right]=\frac{1}{\lambda} \cdot \mathbb{E}[Y]=\frac{1}{\lambda}$$
Computing our variance is similar, but since the variance is not linear, taking the lambda out will result in a squared term:
$$\mathbb{V}[X]=\frac{1}{\lambda ^2}$$
---
# Relevance of the Exponential Distribution
Why is this distribution important? One such reach is because it is has a [[Memoryless]] property. This means that, regardless of how long we have waited, its like we are starting over from new. In terms of probability this is to say that:
$$\mathbb{P}[X\geq s+t | x \geq  s] = \mathbb{P}[X \geq t]$$
Basically, if we have already waited $s$ minutes, and have to wait through $t$ more, this is the same thing as just waiting through $t$ minutes, meaning that our starting point is not affected by how much time has already passed. 

We can start by considering the [[Survival Function]]
$$\mathbb{P}[X \geq s]= 1-\mathbb{P}[X \leq s]=e^{-\lambda s}$$
Then looking at the memorylness property and applying [[Conditionality Probability, Independence, and Trees]]:
$$\mathbb{P}[X\geq s+t | x \geq  s] = \frac{\mathbb{P}[X \geq s +t]}{\mathbb{P}[X \geq s]} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = \mathbb{P}[X \geq t]$$
The [[Exponential Distribution]] is the ONLY [[Memoryless]] distribution. We can use this property to solve things like $\mathbb{E}[X | X > a]$. Using [[Linearity]] we can write:
$$\mathbb{E}[X | X > a ] = a + \mathbb{E}[X - a | X > a ]= a + \frac{1}{\lambda}$$
Instead of needing to use calculus and other math to get at our answer all we need is the memoryless property. 

#### Proof that the [[Exponential Distribution]] is the only [[Memoryless]] Continuous Distribution
If $X$ is a [[Random Variables]] that is continuous with the memoryless property, then $X$ ~ $\text{Exp}(\lambda)$. Let $F(x)$ be the [[Cumulative Density Functions]] of $X$, then $G(X) = P(X > x) = 1 - F(x)$ . We can write out the memoryless property using $G(x)$:
$$G(s+t)=G(s) \cdot G(t)$$
If we let $s=t$ then we would get:
$$G(2s)=G(s)^2$$
Similarly we would get $G(3s)=G(s)^3$ and $G(ks)=G(s)^k$. For rational numbers we would also get $G(\frac{m}{k}s)=G(s)^{\frac{m}{k}}$, and for reals more generally $G(xs)=G(s)^x$.  This statement is true for $x>0$ and for all of $s$. If we let $s=1$ then we get:
$$G(x)=G(1)^x$$
Which gives an exponential equation:
$$= e^{x\text{ln}(G(1))}$$
If we let $\lambda = -\text{ln}(G(1))$, since the quantity should be negative already, we would have:
$$=e^{-x \lambda}$$
Essentially any continuous [[Memoryless]] distribution can be represented as an [[Exponential Distribution]]. 

---
# Calculation of the [[Moment Generating Function]] of the [[Exponential Distribution]] 

The MGF of an exponential, $X$ ~ $\text{Exp}(\lambda)$ can be calculated by doing the following integral:
$$\mathbb{E}[e^{tx}]=\int_{-\infty}^\infty e^{-\lambda x}\cdot e^{tx}=\int_{0}^\infty e^{-x(\lambda-t)}=\frac{1}{\lambda-t}$$
The MGF is only defined given that $t < \lambda$, as there is a discontinuity at $t=\lambda$. Given this MGF we could find the [[mean]], [[Variance]], and third moment easily by taking derivatives with respect to $t$ of the MGF above. 

Instead of having to take an annoying amount of [[derivative]]s of our function, we can just recognize that $\frac{1}{\lambda -t}$ looks a lot like a geometric series. If for instance, $\lambda = 1$, then we would have that:
$$\sum_{n=0}^\infty t^n= \frac{1}{1-t}$$
This result is valid for $|t|<1$. Here, we don't need to use derivatives. In the [[Taylor Series]] expansion of the [[Moment Generating Function]], we have that each [[moment]] is the coefficient of the [[Taylor Series]] corresponding to our [[Moment Generating Function]]. We can Modify our series slightly by dividing it by $n!$ and multiplying it by the same thing to more closely resemble our [[Moment Generating Function]]'s [[Taylor Series]]:
$$\sum_{i=0}^\infty \frac{n!(t^n)}{n!}$$
By the definition of [[moment]] as the coefficient of the taylor series, we have that the moment is thus $n!$. This gives us each moment of $Exp(1)$. 

If we consider the more general exponential case, for $Y$ ~ $Exp(\lambda)$, we can consider $X=\lambda Y$. We can see that $Y$ has a mean of $1$ now, and that $Y^n=\frac{X^n}{\lambda^n}$. We can now take the expected value to obtain:
$$\mathbb{E}[Y^n]=\mathbb{E}\left[ \frac{x^n}{\lambda^n} \right]= \frac{n!}{\lambda^n}$$
Which falls out of our knowledge of $Exp(1)$. 