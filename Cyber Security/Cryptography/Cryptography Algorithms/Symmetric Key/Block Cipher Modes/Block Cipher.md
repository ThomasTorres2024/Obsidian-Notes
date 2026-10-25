---
title: Block Cipher
tags:
  - Cryptography
  - Cyber_Security
  - Symmetric_Key_Cryptography
draft: "False"
---
# Block Cipher 

A [[Block Cipher]] is a [[Cryptography]] algorithm for [[Symmetric Key Encryption]]. We begin with some message $m$. We break the message down into chunks of $64$ (DES), $128$ (AES), or $256$ .

The standard for splitting is AES, meaning chunks of $128$ blocks. Modern processors also have instructions that make AES much faster. The older block choice is DES, which is slower per block and weaker overall.

---

# Block Cipher Modes 

From here this is a whole slew of [[Block Cipher]] algorithms that can be examined: 

* [[ECB (Electronic Codebook)]]
* [[CBC (Cipher Block Chaining)]]
* [[CFB (Cipher Feedback)]]
* [[OFB (Output Feedback)]]
* [[CTR (Counter)]]

Each mode has its own strengths and weaknesses. 