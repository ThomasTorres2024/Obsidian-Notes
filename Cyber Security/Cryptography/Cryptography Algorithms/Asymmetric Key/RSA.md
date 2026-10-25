---
title: RSA
tags:
  - Cryptography
  - Cyber_Security
  - Asymmetric_Key_Encryption
draft: "False"
---
# RSA 

[[RSA]] is an [[Asymmetric Encryption]] algorithm named after its inventors, Rivest, Shamir, and Adelman in $1978$. It is used in [[SSL]], [[PGP]], and many other places. The algorithm uses number theory to factor large numbers composed of two [[Prime]] numbers. 

Key sizes are usually $1024$ (deprecated), 2048, or 4096 bits. 

We have $n=p_{1}p_{2}$ where $p_{1},p_{2}$ are prime. 

The public key is a large composite number $n$, and we have some encryption exponent $e$ which is comprimeto $\phi(n)=(p-1)(q-1)$. 

The private factors are composed of factors of $n=p_{1}p_{2}$. 