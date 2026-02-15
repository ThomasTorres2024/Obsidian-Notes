---
title: Euler's Totient Function
tags:
  - NumberTheory
draft: "False"
---
# Euler's Totient Function
[[Euler's Totient Function]] allows us to calculate the number of natural numbers that are [[Relatively Prime]] to a given number $n$:

$$\phi(n) = \begin{cases}1  \text{ for } n=1 \\ \\ \text{number of natural numbers k} \newline 1 \leq k < n, \text{ with } \gcd(k,n)=1 \newline \text{for } n > 1 \end{cases}$$
For instance consider $\phi(6)$. We can directly compute the result by looking at the natural numbers in $[1,6]$, and determining all numbers $k \in [1,6]$ where $\gcd(k,6)=1$:
$$\{1,2,3,4,5,6 \} \implies 1 \text{ and 5} \text{ are rel prime}$$
Therefore, $\phi(6)=2$. 

Furthermore, for prime $p$, we know that $\phi(p)=p-1$, since all of the numbers from $[1,p]$ except $p$ are relatively prime, for instance consider $p=5$:
$$\phi(5) \implies \{1,2,3,4,5 \} \implies 1,2,3,4 \text{ are rel prime} \implies \phi(5)=4$$
For a prime $p$ we also know that the following are relatively prime. Consider $p^n$. Then on the interval $[1,p^n]$ there are $p^n$ many numbers we are considering.

### Power Property
Then:
$$\phi(p^n)=p^n-p^{n-1}$$
We need to consider each $p,2p,3p, \dots p^n$, of which there are $p^{n-1}$ many. We can then take out the $p^{n-1}$ numbers that are NOT relatively prime to $p^n$, and then we obtain the above result. 

### Multiplicativity Property 
For $\phi(mn)$ if $m$ and $n$ are [[Relatively Prime]] then:
$$\gcd(m,n)=1 \implies \phi(mn)=\phi(m)\phi(n)$$

We can also use prime factorization of a number to evaluate the totient function. 


---
# Examples.) 
### EX 1.)
$$\phi(50)=\phi(2\cdot 5^2)=\phi(2) \phi(5^2)= 1 \cdot (5^2-5)=20$$
