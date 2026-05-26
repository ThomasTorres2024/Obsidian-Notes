---
title: Activation Record
tags:
  - Fundamentals_Prog_Langs
draft: "False"
---

# The Runtime Stack 

![[Pasted image 20260403084211.png]]

We can observe a pattern here for the runtime stack. A stack pointer points to the return address of another activation record, and then that activation record has a pointer to another record on the stack, and so on which gets the content of the return address of the next activation record. 

