---
title: Symmetric Key Encryption
tags:
  - Cyber_Security
  - Cryptography
draft: "False"
---
# Symmetric Key Encryption 

In [[Symmetric Key Encryption]], we have two parties both of which share the same key $k$. We have a message $m$, its encrypted version $c$, and an Encryption Function $F$ and its corresponding decryption function $F^{-1}$  such that the following are satisfied:

$$\begin{align}
c = F(m,k) \\
m=F^{-1}(c,k) \\
m=F^{-1}(F(m,k),k)
\end{align}$$

Symmetric key Encryption is distinguished from asymmetric by the use of the same key $k$ in both parts. 

### Example Encryption-Decryption with Symmetric Key

For example, consider if Alice wants to send $m$ to Bob. 

1. Alice computes $c=F(m,k)$
2. Alice sends $c$ to Bob. Bob needs $k$ already, from some other channel.
3. Bob receives $c$ 
4. Bob computes $m=F^{-1}(c,k)$

