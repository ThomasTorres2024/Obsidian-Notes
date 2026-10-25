---
title: Asymmetric Encryption
tags:
  - Cryptography
  - Asymmetric_Key_Encryption
  - Cyber_Security
draft: "False"
---
# [[Asymmetric Key Encryption]]

Approach to encryption wherein two linked keys are used, a public key and a private key. Public key can be used to encrypt content, and the private key can be used to decrypt our messages. 

Two common algorithms for this topic are [[RSA]] and [[ECC]]. 

[[Asymmetric Key Encryption]] gives us authentication.

---
# Motivation

Allows strangers to communicate with confidentiality. Everyone who wants to communicate with someone else just needs a public key, though this needs to be authenticated in order to properly function. 

We can put puublic keys in a directory so dissemination is easy. 

#### Example
* Alice recieves Bob's public Key from Bob or a trusted repoistory
* Alice uses that key to encrypt a message to Bob
* Bob uses his private key to decrypt 

---

# Notation 

Let $m$ be the plaintext message, $F$ the encryption function, $F^{-1}$ is the decryption function, $k_{p}$ is the public kfye, $k_{s}$ is the secret key and $c$ is the cipher text. THen we have:

$$\begin{align}
c=F(m,k_{p}) \\
m=F^{-1}(c,k_{s}) \\
m=F^{-1}(F(m,k_{p}),k_{s})
\end{align}$$
---
# Algorithms

The most famous assymetric key encryption algorithms are [[RSA]] and [[ECC]]. 