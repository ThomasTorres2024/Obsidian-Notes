---
title: Cryptography
tags:
  - Secure_Programming
  - Cyber_Security
draft: "False"
---
# Cryptography 

Cryptography is the study of encoding and decoding messages so that we can securely encrypt a message and have the recipient read the message not allowing any other party to pry into the contents of the message. 

We require a "cryptographic primitive", an Algorithm used as a building block for a cryptographic system. 

From the algorithm we can construct a "Cryptosystem", a set of [[Function]]s which are responsible for encryption, decryption, and key generation. 

---
# Characters 

Commonly in formal papers in cryptography we have several common characters used for the same purpose:

* Alice, Bob, and Carol all send and receive messages to one another
* Trent is a trusted third party
* Eve listens and monitors the communications between Alice and Bob 
* Mallory is an active attacker on the system
---
# Encryption Algorithms 

### [[Substitution Cipher]] 

Avery weak algorithm used to encrypt messages written with latin script. We treat the alphabet as cyclic and rotate each letter by some fixed amount $n$ from its original value.

Very susceptible to frequency analysis, easily broken (also easy to brute force

 The key takeaway from this algorithm is that we should have a high [[Entropy]] in our algorithm, and that __any one byte should not give away others__ in the system. 
### [[Symmetric Key Encryption]]

[[Symmetric Key Encryption]] algorithms are a set of Algorithms which 


(1)

Primitive building blocks operations that build these things can be constructed in different ways. 

---
(6) ciphers

Simplest possible [[Cryptography]] is substitution cypher like the ceasar cipher, [[Rot13]] (special since half of 26), symmetrical operation, since rotating again gets you back to the original. Generally easy to break due to the number of spaces given, can match words easily 

We want a high [[Entropy]] output, should look like garbage and not give our resu;ts away.

---

(7)

These are all symmetric keys where the key to encrypt and decrypt is equal.

$m$ is the message in plain text, $F$ is the encryption function, $F^{-1}$ is the decryption function, $k$ is the pre-shared key (everyone has one), and $c$ is the Cipher text:
$$\begin{align}
c=F(m,k) \\
m=F^{-1}(c,k) \\
m=F(F^{-1}(c,k),k)
\end{align}$$
18
Theoretical model of perfect secrecy, a key model 

19
Bit flipping can be protected against using [[Hashing]] to check authenticity of the message. 

---

(22) assymetric encryption

link public and private keys, server has private key we have pub key 

---

(29)

symmetric vs assymmetric
