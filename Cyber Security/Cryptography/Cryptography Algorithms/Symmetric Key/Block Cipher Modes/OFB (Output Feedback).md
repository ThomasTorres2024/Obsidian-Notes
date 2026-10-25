---
title: OFB (Output Feedback)
tags:
  - Cyber_Security
  - Cryptography
  - Symmetric_Key_Cryptography
draft: "False"
---

# OFB
OFB is another serial encryption decryption [[Block Cipher]] mode  used for [[Symmetric Key Encryption]] and we can think of it as a variant of [[CBC (Cipher Block Chaining)]].

We pass an initialization vector into a block cypher, extract some plaintext, and [[XOR]] it. We get some resulting cipher text. 

We take the encrypted initialization vector and feed that into the next block cipher encryption, and keep repeating the process continually. 

(OFB)
![[Pasted image 20261025114441.png]]

We can think of this as a variantion of [[CFB (Cipher Feedback)]] where instead of feeding the cipher text in, we feed in the block cipher encryption after the vector has been passed in, and keep repeating the process.  

