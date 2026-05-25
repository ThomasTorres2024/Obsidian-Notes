---
title: Memory Locations for Variables
tags:
  - Fundamentals_Prog_Langs
draft: "False"
---
# Memory Locations for Variables 

Modern programming languages tend to have the following types of variables, global variables, parameters (when passed into functions), (function) local variables (also known as automatic or activation-specific variables), member variables in the case of [[Object Oriented Programming]], and others. 

The language system keeps track of these values during the runtime of a program. 

---
# In [[Imperative Language]]s 
Memory management is quite apparent in [[Imperative Language]]s, since changing variables by name essentially mimics what the hardware is doing.

In [[Functional Language]]s and [[Logical Language]]s, it is not as clear as to where the variables are stored and what is happening behind the scenes. There is no global state, but variables still are bound to different memory locations. 

---
# Activation Records
In order to track variables for functions, compilers make use of a data structure known as the activation record, which collects all variables which belong to one function in the structure. 

We often refer to activation records as "frames". 

Languages which support recursion have a single activation record per function, whereas languages which do support recursion such as Java, C, C++, etc keep a [[Stack]] of activation records, one per function call. 

---
# The Runtime Stack 

![[Pasted image 20260403084211.png]]

We can observe a pattern here for the runtime stack. A stack pointer points to the return address of another activation record, and then that activation record has a pointer to another record on the stack, and so on which gets the content of the return address of the next activation record. 

