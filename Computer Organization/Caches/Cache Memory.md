---
title: Cache Memory
tags:
  - Computer_Organization
draft: "False"
---
# Cache Memories 

The increasing gap between main memory ([[Random-Access Memory]]) and CPU registers incentivized engineers to insert a small SRAM [[Cache Memory]] between the CPU and the main memory. The gap in performance between the CPU and main memory continued to grow, in turn added the L2 and L3 caches. 

The general principles of the caches is the same despite there being some variety between them. 

---
# Generic Cache Memory Organization 

Consider a computer system where each memory address has $m$ bits, giving in total $M=2^m$ unique addresses in total. 

A cache for such a system is organized as an array of $S=2^s$ cache sets. Each set consists of $E$ cache lines. Each line consists of a data block of $B=2^b$ bytes. A valid bit indicates whether or not the line contains meaningful information, and $t=m-(b+s)$ tag bits which uniquely identify the block stored in the cache line. 


![[Pasted image 20261017180237.png]]

In total we can describe a [[Cache]]'s organization using the tuple $(S,E,B,m)$. The size of the cache, $C$ is:
$$C=S \cdot E \cdot B$$
When the CPU is told to load some address $A$ of main memory, it sends $A$ to the cache. If the cache has a copy, it sends the word back to the CPU instantly. How does the cache know if contains a copy of the word at some address A? The cache is organized so that it can find the requested word by inspecting bits of its address quite similar to a [[Hashing]] Table with a very simple hash function. 

The number of tags per cache is given by $m-(b+s)$ where $b$ is such that $2^b=B$, $m$ is such that $2^m=M$ and $s$ is such that $2^s=S$. 

This is essentially how it works. Each address to the cache is paritioned into the following schema:

$$\begin{align}
\underbrace{\begin{bmatrix}
64 \text{ bits}
\end{bmatrix}}_{\text{"canonical"}} \underbrace{\begin{bmatrix}
48 \text{ bits}
\end{bmatrix}}_{\text{"tag"}} \underbrace{\begin{bmatrix}
10 \text{ bits}
\end{bmatrix}}_{\text{"set order"}} \underbrace{\begin{bmatrix}
6 \text{ bits}
\end{bmatrix}}_{\text{"offset"}}
\end{align}$$

The canonical portion is always the same. The following is an __address that uniquely maps to a byte in RAM__. The program and the [[Operating System]] each have a different perspective of the memory and their own local address space, whereas globally the operating system maintains its own mapping. 

We have in total $128$ bits for the whole portion. Every [[Byte]] in memory has a memory address, and depending upon the architecture in the modern day each byte has $64$ bit addresses. 

If we want to access something in the cache we can think of it as a three way hash. First we match the set part with the provided. This tells us the set. The tag then tells us the cache line, and the offset tells us in bits from the beginning of the block line we would expect to find our data.

Here is a summary of the above data:

![[Pasted image 20261017220236.png]]

---
# Practice Problems 

![[Pasted image 20261017220112.png]]
