---
title: Direct-Mapped Caches
tags:
  - Computer_Organization
draft: "False"
---
# Direct-Mapped Caches 

[[Cache]]s are grouped into different classes based on $E$ ([[Cache Memory]]), the number of cache lines per set. A cache line with one line per set is known as __a direct mapped cache__. Direct map caches are the simplest to understand and implement. 

Let us trace an example of the directed map in action. Say the CPU requests an instruction to read memory word $w$. The CPU requests from the L1 cache. If the cache has a copy of $w$ then have an L1 cache hit, and the cache extracts $w$ and returns it to the CPU. Otherwise, we have a miss, and the CPU has to wait while the L1 cache requests a copy of the block containing $w$ from memory. When the block returns from memory, the L1 cache stores the block in one of the cache lines, extracts it from the block and returns it to the CPU. 

We condense this into three simple steps:

1. Set Selection 
2. Line Matching 
3. Word Extraction

We can see this in the following:
![[Pasted image 20261017221434.png]]

---
### Set Selection in Direct-Mapped Caches 

In this step, the cache extracts the set $s$ index bits from the middle of the address for $w$, these correspond to a set number. We can sort of think as this as indexing into an [[Array]] by a provided number. 

### Line Matching in Direct-Mapped Caches
We now need to determine if in the set $i$ that we have identified, and we want to determine if a copy of $w$ is stored in one of the cache lines contained in $i$. Since we are in a direct mapped cache this is easy since there is only a line per set. 

Now we look for the valid bit, if it is marked as valid (1) we proceed. Then we have a cash hit and a value is contained in the set we finish and proceed to extraction. 

### Word Selection in Direction-Mapped Caches

Now we select by the bit offset. The last step gives us the where the word starts in the block by giving us the first byte of the word. We can think of it as a an [[Array]]. 

### Line Replacement on Misses in Direct-Mapped Caches 

If the cache misses, then we need to retrieve the block from the next level in [[Memory Hierarchy]]. We replace the existing content. If there is content full of valid cach lines, then one of the existing lines has to be evicted. For a direct mapped cach where each set has exactly one line, replacement policy is trivial and we always replace the full line with the newly fetched one. 

---
# Conflict Misses in Direct-Mapped Caches 

Conflict misses are common in real programming and can cause massive performance problems. Conflict misses in direct mapped caches occur when programs access arrays whose sizes are a power of $2$. 

Consider the following program that computes a dot product of two vectors:

```C

float dotprod(float x[8],y[8])
{
	float sum=0.0;
	int i; 
	
	for(i=0; i < 8;i++){
		sum+=x[i]*y[i];
	}
	
	return sum; 
	
}

```

The following function has good space locality wrt $x,y$. We would expect to experience many cache hits during this program's execution. 

If we consider the example where the floats are each $4$ bytes, that $x$ is loaded in the $32$ bytes of contiguous memori which starts at address $0$, and $y$ immediately starts adter $x$ at address $32$. We will continually read and write from addresses in $x$ to addresses in $y$ never re-reading values that we already added (I think the example in the book relies on LRU):

![[Pasted image 20261017233506.png]]

Here we are experiencing __"thrashing"__. 

---
# Why do we use the middle bits?

Why do we use the middle bits in the for the set index instead of the high-order bits? The reason why is because 