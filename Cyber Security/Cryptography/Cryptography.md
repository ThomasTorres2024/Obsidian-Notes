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

[[Symmetric Key Encryption]] algorithms are a set of Algorithms which require that both parties use the same key to encrypt and decrypt messages. The main challenge is sending the key over safely. 

*  [[Block Cipher]]s
	* [[ECB (Electronic Codebook)]]
	* [[CBC (Cipher Block Chaining)]]
	* [[CFB (Cipher Feedback)]]
	* [[OFB (Output Feedback)]]
	* [[CTR (Counter)]]
* [[One-Time Pad]]
* [[Stream Cipher]]s 

---
# Bit Flipping Protection 

In some cipher modes bit flipping in the cipher stream may make some changes to predictable bits in plaintext. In order to safe guard against this we use message authentication codes (MAC) to check that data is unaltered. 

An Encrypt-then-MAC check needs two keys. MAC must be unforgeable. We for this we have the following:
$$(c=F(m,k_{1}), M=H(m,k_{2}) )$$
The reciever can check integrity of the message before decryption. Bit flipping can be protected against using [[Hashing]] to check authenticity of the message. 

It is __particularly important to do Encrypt-and-MAC__ and __not__ MAC-then-Encrypt. The former order produces a MAC version of the text, and the second version encrypts our verification of the text. 

Briefly used in SSL and TLS. 

---
# Authenticated Encryption with Associated Data (AEAD)

One primitive provides confidentiality and integrity. 

$$(c,t)=\text{Seal}(m,k,n,A)$$
Here $n$ is some nonce and $A$ is associated data. $A$ is authenticated information, but it is not encrypted, such as packet headers. 

Open returns $m$ if the tag $t$ verifies, and fails else. 

There are a few common structions for this:
* [[AES-GCM]] AES in counter made a GHASH based authenticator
* [[ChaCha20-Poly1305]] [[Stream Cipher]] authenticator, fast without AES hardware 

---
# [[Asymmetric Key Encryption]]

Approach to encryption wherein two linked keys are used, a public key and a private key. Public key can be used to encrypt content, and the private key can be used to decrypt our messages. 

Two common algorithms for this topic are [[RSA]] and [[ECC]]. 

[[Asymmetric Key Encryption]] gives us authentication.




---

(22) assymetric encryption

link public and private keys, server has private key we have pub key 

---

(29)

symmetric vs assymmetric
