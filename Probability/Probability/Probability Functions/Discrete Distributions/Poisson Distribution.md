---
tit;e: Poisson distribution
tags: 
draft: "false"
---
# Poisson distribution Definition 

We define the [[Probability Mass Function]] of the [[Poisson Distribution]] by:
$$\mathbb{P}[X=k]=\frac{\lambda^k e^{-\lambda}}{k!}$$
$\lambda$ is our "rate" parameter and $\lambda \in \mathbb{R}^+$. Each $k \in \mathbb{N}\cup \{ 0 \}$. We can verify that this PMF is valid easily. Each probability is already positive, since each component is already positive, and these operations are closed over the positives. All we need to do is verify that the probabilities sum to 1. 

#### Verifying that the PMF is 1 
$$\sum_{k=0}^\infty \frac{\lambda^k e^{-\lambda}}{k!} = e^{-\lambda} \sum_{k=0}^\infty \frac{\lambda^k }{k!} = e^{-\lambda} \cdot e^{\lambda} = 1$$
Thus, the [[Poisson Distribution]] is a valid [[Probability Density Function]]. 

We can also compute the [[Expected Value]] of the [[Poisson Distribution]] for $X$  ~ $\text{Pois}(\lambda)$:
$$\mathbb{E}[X] = \sum_{k=0}^\infty \frac{k\lambda^k e^{-\lambda}}{k!}= \lambda e^{-\lambda} \sum_{k=1}^\infty \frac{\lambda^{k-1}}{ (k-1)!} $$
Let $j=k-1$. It follows that:
$$=\lambda e^{-\lambda} \sum_{j=0}^\infty \frac{\lambda^{j}}{ (j)!} = \lambda \cdot(e^{-\lambda + \lambda})=\lambda$$
Therefore, the [[Expected Value]] of our PMF is $\lambda$, or its rate. This is the most widely used [[Probability Density Function]] in the real world. We use this distribution for counting the number of things, the number of "successes". We have a large number of trials, that could lead to success or failure. 

Some examples of [[Poisson Distribution]]s include:
1. Emails in an hour. We consider this to be a poisson since overall the likelihood that we get an email from people, but we are considering many of them. 
2. Another example is the number of chips in a chocolate chip cookie. We have a lot of chips, but relative to doe not really. We have a lot of positions, and a small probability. 
3. The number of earthquakes in a region, again lots of days in a year and small probability. 

#### [[Variance]] of the [[Poisson Distribution]]:
By definition of Variance:
$$\mathbb{E}[X^2] = \sum_{k=0}^\infty k^2 \frac{e^{-\lambda}\lambda^k}{k!}$$
The computations for this part are a bit tedious. All we do is take derivatives of the original taylor expansion and multiply both sides by $\lambda$ after taking the derivative with respect to it such that we can substitute it back into our expression above. This results in:
$$=\lambda^2 + \lambda$$
We lastly subtract the mean squared, which is just $\lambda^2$, so in conclusion we have that $\mathbb{V}[X]=\lambda$. 

---
# Poisson Paradigm/Poisson Approximation 
Most things we work with that are reasonably thought of as a [[Poisson Distribution]] are in reality not actually from this distribution, but it is nice to think of them in this way. 

Suppose that we have a lot of events, $A_{1},A_{2},\cdots,A_{n}$ and $\mathbb{P}[A_{i}]=p_{j}$ We have that $n$ is large and each $p_{j}$ is small. The events may be [[Independent]] or may be "weakly dependent". We claim that the number of events, $A_{n}$ that occur are approximately Poisson. 

We would expect that $\lambda$ is the expected number of things that occur, which would be given by summing the probability of our events, so it should be that:
$$\lambda = \sum_{j=1}^n p_{j}$$
This is also known as the "Poisson Approximation". If each [[event]] is [[Independent]], then it follows that we have the sum of $n$ [[Bernouli Trial]]s, and if it is furthermore the case that each trial has the same [[probability]], then our resulting $\lambda$ is $np$ and we would get a [[Binomial Distribution]].

We want to show that $\lim{n \to \infty}$ that   the [[Binomial Distribution]] actually converges to the [[Poisson Distribution]]. 

---
# WTS That the [[Binomial Distribution]] Converges to the [[Poisson Distribution]] 
Let $X$ ~ $\text{Bin}(n,p)$. Let $n\to \infty$, and $p \to 0$. We are interested in the case where our $\lambda = np$ is held constant. Let $k$ be a fixed number. We want to know as apply these rules, what happens to the PMF of the binomial:
$$\mathbb{P}[X=k] = {n \choose k} p^k(1-p)^{n-k}$$
We want to express every variable in terms of $n$. Let $p = \frac{\lambda}{n}$ since $\lambda = np$. Also, we can rewrite our $n$ choose $k$ as its definition:
$$= \frac{n \cdot (n-1)  \cdots(n-k+1) \lambda^k}{k! n^k} \cdot \left(1-\frac{\lambda}{n} \right)^n \cdot \left(1-\frac{\lambda}{n} \right)^{-k}  $$
Let us consider  $\lim_{n \to \infty}$. Since we let $k$ be constant we are going to pull it out to the front:
$$=\left(\frac{\lambda^k}{k!}\right) \cdot \left(1-\frac{\lambda}{n} \right)^n =  \left(\frac{\lambda^k}{k!}\right) \cdot e^{-\lambda} $$
Our fraction at the start goes to 1 since we can match each $n-j$ with an $n$ in the denominator, which gets us to $1$ in total. There is also an $e$ identity in there, and the $-k$ part goes to $1$ since the probability goes to 0. 

Thus the [[Binomial Distribution]] converges to the [[Poisson Distribution]] as $n$ increases to infinity. 

---
# Connection Between the [[Normal Distribution]] 
If we allow $\lambda \to \infty$, our [[Poisson Distribution]] would tend towards a [[Normal Distribution]]. 

---
# [[Moment Generating Function]] Calculation
We can determine the [[Moment Generating Function]] of a [[Poisson Distribution]] by using [[LOTUS]]:
$$\mathbb{E}[e^{tx}]=\sum_{k=0}^\infty e^{tk}e^{-\lambda}\frac{\lambda^k}{k!} = e^{-\lambda} \sum_{k=0}^\infty \frac{(e^t\lambda)^k}{k!}=e^{-\lambda } e^{\lambda e^t}=e^{\lambda(e^t-1)}$$
If we let $X$ ~ $Pois(\lambda)$, $Y$ ~ $Pois(\mu)$, and we want to find $X+Y$ the [[Convolution]] of the two [[Random Variables]], we can also use the MGF to simplify calculations. Since $X$ and $Y$ are independent we get:
$$\mathbb{E}[e^{t(x+y)}]=\mathbb{E}[e^{tx}]\cdot \mathbb{E}[e^{ty}]=e^{\lambda(e^t-1)} \cdot e^{\mu(e^t-1)}=e^{(\lambda + \mu)(e^t-1)} \implies X+Y \text{ is Pois}(\lambda + \mu) $$
We already could have determined the mean via [[Linearity]] of the [[Expected Value]], but the interesting thing is that we can determine the distribution of the summed [[Random Variables]].   If $X$ and $Y$ are dependent, let us consider when $X=Y$ then, $X+Y=2X$. We would not get back a [[Poisson Distribution]]. The [[mean]] and [[Variance]] would not conform, since the variance would be $4\lambda$ and the mean would be $2\lambda$, which violates the properties of a [[Poisson Distribution]]. 