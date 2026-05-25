---
title: Memory Management
tags:
  - Fundamentals_Prog_Langs
draft: "False"
---
# Memory Management 
Programming languages generally have two distinct types of memory, static memory and dynamic memory. __Static__ memory consists of, global data, compiled code, and "runtime system", and __Dynamic__ consists of the runtime stack (the [[Activation Record]]) 

---
# Typical Memory Layout 

![[Pasted image 20260406064944.png]]

The heap and stack tend to "grow towards each other", the stack pushes down and the heap pushes upward as there are more and more dynamic assignments. 

Runtime systems allocate memory dynamically via the __heap manager__. The heap manager in Java/C++ is the "new" keyword, in C it is the malloc function. 

Languages like Java and Python have a heap manager which directly handles any variables on the heap without any reference by using __Garbage Collection__, when variables are no longer used. 

In C we have to explicitly manage heap memory using malloc/free, which has its own associated memory issues including memory leaks and dangling pointer references (when free is called to early). 

When a memory leak occurs, free is never called on a corresponding block of memory which means that it remains occupied. 

With a dangling pointer we free too early. We try and change some attributes of a pointer associated with some slot of memory that has already been freed. If we allocate another slot of memory, it map overlap with the previous spot, and using the pointer the deallocated pointer may have unexpected effects. 

---
