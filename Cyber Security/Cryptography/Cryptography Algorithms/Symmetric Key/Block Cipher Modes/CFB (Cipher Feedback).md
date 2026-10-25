---
title: CFB (Cipher Feedback)
tags:
  - Cryptography
  - Cyber_Security
  - Symmetric_Key_Cryptography
draft: "False"
---

# CFB

CFB is a [[Block Cipher]] mode used for [[Symmetric Key Encryption]] and we can think of it as a variant of [[CBC (Cipher Block Chaining)]].

In CFB we apply some initialization vector (similar to [[Salting]]) before the plaintext. We then feed the noise into our key, pass the plaintext in, applying a [[XOR]] operation. We get out some cipher text, and this becomes the initialization vector. We keep repeating this process for each text block:

(CFB)

![[Pasted image 20261024181910.png]]

(CBC, for Comparison)
![[Pasted image 20261024180842.png]]

This algorithm also makes use of serial encryption and decryption. Each block's encryption depends on the previous ciphertext. Since we use XOR after the encryption block we can use it as a Stream Cipher (???)