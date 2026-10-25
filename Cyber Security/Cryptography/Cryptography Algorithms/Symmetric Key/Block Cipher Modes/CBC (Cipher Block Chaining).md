---
title: CBC (Cipher Block Chaining)
tags:
  - Cyber_Security
  - Cryptography
  - Symmetric_Key_Cryptography
draft: "False"
---

# CBC

CBC is a [[Block Cipher]] mode used for [[Symmetric Key Encryption]] and is a variant of [[ECB (Electronic Codebook)]] that tries to handle a flaw in many blocks storing identical data by giving up on parallelization. 

![[Pasted image 20261024180842.png]]

We also add some initialization vector near the plaintext, this is similar to [[Salting]]. 

In order to decrypt the second $n$th block we must decrypt the $n-1$st block and the $n-2$th block and so on. We also add some initial noise to the the first chunk of plaintext and nowhere else during the process. 

During decryption we __need__ to use the previous block each time. (Says Serial Encrypt parallel decrypt, doesn't make much sense??)

