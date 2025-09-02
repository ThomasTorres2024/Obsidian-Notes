---

---

Let us consider $X\textasciitilde{\text{Binom}(n,p)}$ and  $Y\textasciitilde{\text{Binom}(m,p)}$. We can see in three ways that $X+Y=\text{Binom}(n+m,p)$. It can be a bit tedious and troublesome to compute our [[Convolution]] below.

1. Since $X$ and $Y$ are independent and do not affect one another, we are simply repeating the same [[Bernouli Trial]] an additional $m$ times, so our resulting distribution would just be another binomial distribution
2. We can think of $X=x_{1}+x_{2}+x_{3}+\cdots+x_{n}$ where each $x_{i}: 0 < i \leq n$ is a [[Bernouli Trial]] and likewise we have $Y=y_{1}+y_{2}+y_{3}+\cdots+y_{n}$. We can think of the sum of the two random variables as: $$X+Y=\sum_{i=1}^n x_{i}+\sum_{j=1}^m y_{i}$$ This is clearly just the definition for $\text{Binom}(n+m,p)$, so it follows that $X+Y=\text{Binom}(n+m,p)$
3. We can lastly approach this problem by considering $\mathbb{P}(X+Y=k)$. Using the definition of probability here we  have that: $$\mathbb{P}(X+Y=k)= \sum_{j=0}^k \mathbb{P}(X+Y=k | X=j)\mathbb{P}(X=j)$$ $$=\sum_{j=0}^k \mathbb{P}(Y=k-j) | X=j)\mathbb{P}(X=j)=\sum_{j=0}^k \mathbb{P}(Y=k-j) | X=j) {n \choose j} p^jq^{n-j}$$ We can use the fact that $X$ and $Y$ are [[Independent Random Variables]], so the condition on $Y$ that $X=j$ doesn't affect our probability of $Y=k-j$, so we can just write out it's Binomial distribution definition: $$= \sum_{j=0}^k {m \choose k-j} p^{k-j}q^{m-k+j} \cdot {n \choose j} p^jq^{n-j} = p^kq^{m+n-k} \sum_{j=0}^k {m \choose k-j}{n \choose j}$$ We can reduce the inside of our sum as the [[Vandermonde Identity]], which really is just ${ m +n \choose k }$. This gives us the following: $$\mathbb{P}(X+Y=k)={m+n \choose k} p^kq^{m+n-k}$$ which shows that our probability is really equivalent to $\text{Binom}(n+m,p)$

---
# [[Expected Value]]
#### Let $X$ ~ $\text{Binom}(n,p)$
$$\mathbb{E}[X]= \sum_{k=0}^n k {n \choose k} p^kq^{n-k} $$
We can rewrite this expression by canceling a $k$ in the denominator, and extracting an $n$ from the numerator and then factoring it out to yield:
$$=n\sum_{k=0}^{n-1}  {n-1 \choose k-1} p^kq^{n-k} $$
We can also factor out a $p$ and then set our initial bound for $k$ from $0$ to $1$, which makes our sum take on the following form:
$$=np\sum_{k=1}^{n-1}  {n-1 \choose k-1} p^{k-1}q^{n-k} $$
If we let $k-1=j$ and make the following substitution we get:
$$=np\sum_{j=0}^{n-1}  {n-1 \choose j} p^{j}q^{n-1-j} $$
We see that the sum becomes a 1, so this gives us a resulting:
$$\mathbb{E}[X]=np$$
#### Linearity Demonstration 
We can also prove this using the [[Linearity]] property of the [[Expected Value]] of our distribution. We know that for $X$:
$$X=\sum_{i=1}^n x_{i}$$
We can see then that:
$$\mathbb{E}\left( X  \right) = \mathbb{E}\left( \sum_{i=1}^n x_{i}  \right) = \sum_{i=1}^n \mathbb{E}[x_{i}]=np$$
#### [[Variance]] Calculation
The most direct obvious way would involve [[LOTUS]], which would not be fun to work with. Let us consider our Bernoulli, $X$, as the sum of $n$ indicator probability functions, this thus gives:
$$X= \sum_{i=1}^n I_{i}$$
Let us consider $X^2$:
$$X^2=\sum_{i=1}^n \sum_{j=1}^n I_{i} \cdot I_{j} $$
Let us take the [[Expected Value]] of each side:
$$\mathbb{E}[X^2]= \mathbb{E} \left[ \sum_{i=1}^n \sum_{j=1}^n I_{i} \cdot I_{j} \right]= n \mathbb{E}[I_{1}^2]+2 {n \choose 2} \mathbb{E}[I_{1}I_{2}]$$
The right hand most simplification we make is based on symmetry. The probabilities of the indicator variables that are squared are all equivalent, so we only need to consider the product of $n$ many of then. We can similarly argue something for the product of the two indicator variables, which has a probability of two bernouli trials occurring which is thus $p^2$. This makes our expected value:
$$=np+n(n-1)p^2$$
Now using the [[Variance]] formula, we get our final result:
$$Var(x)=np-np^2+n^2p^2-n^2p^2=np-np^2=np(1-p)=npq$$
---
# MGF Calculation
Let $X$ ~ $Binom(n,p)$. We can determine the [[Moment Generating Function]] using a sum of the MGF of $n$ independent [[Bernouli Trial]]s:
$$\mathbb{E}[e^{tx}]=pe^t+q$$
The [[Binomial Distribution]]'s MGF would thus be product sum of all of the $n$ Bernoulli's. Let $Y$ ~ $Binom(n,p)$. We can see this from:
$$\mathbb{E}\left[\text{exp} \left(t \cdot \sum_{i=1}^n X_{i} \right)\right]= \prod_{i=1}^n \mathbb{E}[X_{i}] = (pe^t+q)^n$$
$$=M(t)= (pe^t+q)^n $$

