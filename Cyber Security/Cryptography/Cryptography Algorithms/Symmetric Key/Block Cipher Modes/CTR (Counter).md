---
title: CTR (Counter)
tags:
  - Cyber_Security
  - Cryptography
  - Symmetric_Key_Cryptography
draft: "False"
---
A parallel [[Block Cipher]] mode which is used in [[Symmetric Key Encryption]]. Each block is encrypted by some __nonce__, which is an effectively unique random vector and some offset which is a "counter" that we iterate per each block. 

The nonce and key cannot be reused together. There is no dependency between any of the blocks either.

![[Pasted image 20261025114930.png]]

We apply the nonce and some conunter to the block encryption algorithm, cipher, and then use it and [[XOR]] on our plaintext to get some cipher text that can be parallel decrypted. Notice that we can parallel encrypt too. 


