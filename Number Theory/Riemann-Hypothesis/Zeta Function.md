---
title: Zeta Function
tags:
draft:
---

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\cdots$$
$$\frac{1}{2}\zeta(s)=\frac{1}{2}+\frac{1}{4^s}+\frac{1}{6^s}+\cdots$$
Every term not a product of two survives:
$$\zeta(s)-\frac{1}{2}\zeta(s)=1+\frac{1}{3^s}+\frac{1}{5^s}+\frac{1}{7^s}+\cdots$$
$$\zeta(s)\left(1 -\frac{1}{2} \right) = 1+\frac{1}{3^s}+\frac{1}{5^s}+\frac{1}{7^s}+\cdots$$
Apply process to each prime $p$
$$\zeta(s)\left(1 -\frac{1}{2} \right)\frac{1}{3} = \frac{1}{3}+\frac{1}{9^s}+\frac{1}{15^s}+\frac{1}{21^s}+\cdots$$

$$\zeta(s)\left(1 -\frac{1}{2} \right)\left(1 -\frac{1}{3} \right) =1+\frac{1}{5^s}+\frac{1}{7^s}+\frac{1}{11^s}\cdots$$
As we repeat this process ad infinitum we eliminate all primes and get:
$$\zeta(s) = \dfrac{1}{\prod_{p \in \mathbb{P} } ( 1-\frac{1}{p^S})} = \prod_{p \in \mathbb{P}} \frac{1}{1-\frac{1}{p^s}}$$