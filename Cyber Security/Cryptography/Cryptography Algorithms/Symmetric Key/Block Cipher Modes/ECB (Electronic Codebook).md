---
title: ECB (Electronic Codebook)
tags:
  - Cyber_Security
  - Cryptography
  - Symmetric_Key_Cryptography
draft: "False"
---
# ECB 

ECB is a [[Block Cipher]] mode used for [[Symmetric Key Encryption]]. 

We begin with some plaintext $m$, and split the plaintext into several blocks. We can encrypt each in parallel separately and decrypt them in parallel too. 

![[Pasted image 20261024180448.png]]

ECB suffers from a significant pitfall, namely that no other noise is introduced during the process. Because no other noise is added, ECB can reveal blocks of data that are identical (similar problem to rotation ciphers). 

![[Pasted image 20261024180635.png]]
