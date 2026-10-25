---
title: Cache Memory
tags:
  - Computer_Organization
draft: "False"
---
# Cache 

Caches are essentially small storage devices near the [[CPU]] which use SRAM for fast read/write operations to make programs run much quicker. 

Caching works well with datatypes that have nearby data elements in Arrays, but in [[Linked Lists]] we would struggle since addresses are not sequential. [[Hashing]] Tables can also be potentially be problematic. Anything with high sequential access makes hashing an inefficient operation due to cache [[Locality]]. 

#### Cache Hits 

When a program needs a particular data object $d$ from level $k+1$, it looks for $d$ in one of the blocks stored at level $k$. If $d$ is in level $k$ this is a __"Cache Hit"__. Our program can read $d$ directly from level $k$. By nature of the [[Memory Hierarchy]] this is significantly quicker than reading directly from level $k+1$. 

#### Cache Misses 

If data object $d$ is not cached at some level $k$, then we have a __"Cache Miss"__. When a miss occurs, the cache at level $k$ fetches the block containing $d$ from the level $k+1$. This may overwrite some existing memory at level $k$ if the cache is already full.

This is known as a __"Cache Eviction"__. The block that is evicted is sometimes referred to as the __"Victim Block"__. Our selection process for the block is known as the "replacement policy", and varies depending upon the architecture. A common choice is LRU (Least Recently Used, (i.e. the block that read from the longest ago)).

Once we have read in data $d$ from level $k+1$ at level $k$, we can normally read in data from $d$ at level $k$. We keep it here with the expectation it will be used in later accesses. 

##### Cache Miss Types

There are several kinds of cache misses. One kind of cache miss is known as a __"cold cache miss"__ or alternatively as a __"compulsorary cache miss"__. Cold misses are likess likely to occur in a steady state when the cache has been warmed up sufficiently after repeated memory access. These types of misses are obligated to occur when we need to write data into a clean slate cache with nothing in it. 

When we deal with misses, there has to be a placement policy which determines where to place a block retrieved from level $k+1$ at level $k$.  The most flexible policy is to allow any block from $k+1$ to be stored at level $k$.

For caches that are close to the CPU, this is generally hard to implement, as it's harder to allocate blocks closer to the CPU.  We typically restrict blocks at level $k+1$ to a subset of blocks at level $k$ instead of allowing them to map wherever. Each Restrictive placement policies of this type lead to another type of cache miss, called a __"conflict miss"__. The cache is large enough to hold the referenced data, but because the cache maps to the same portion of the block it continues to miss. The reason these types of misses occur is because we have __more addresses than items that fit in a set__. 

We have another type of miss occur that's called a __capacity miss__, which is similar to a __conflict miss__ in that we run out of 

With [[Direct-Mapped Caches]] where we have $1$ way associative caches we need to kick out something __anytime they share the same set value__, otherwise we add the value. When we add additional $k$-way associativity we have to check an additional set of tags during any given operation meaning more operations in total. 

Notably conflict misses occur due to the [[Pidgeon Hole Principle]]. 

---
# Summary 

![[Pasted image 20261017175333.png]]

Memory hierarchies based on caching work because slower storage is cheaper than faster storage and because programs exhibit [[Locality]] through either temporal or spatial locality.  


