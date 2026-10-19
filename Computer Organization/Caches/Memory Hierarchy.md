---
title: Memory Hierarchy
draft: "False"
tags:
  - Computer_Organization
---
# Memory Hierarchy

[[Storage Structure]]s in memory typically follow the rule that devices get slower and cheaper as we descend the hierarchy. Devices consist of the following usually we conceive of the following:

![[Pasted image 20261017162439.png]]

It should be notes that each layer of the hierarchy has its own organization which is complemented by the previous layer and so on. At each level, the smaller storage device above is a [[Cache]] for the storage devices below it. 

The way information is partitioned at each level is into "blocks", which are contiguous chunks of data. Every block has a unique address or name, which allows these blocks to be distinguished from other blocks. Depending on the model we are working with, some blocks have a fixed size and some others have a static size. [[HTML]] files on Web Servers have variable size, where most other blocks typically have a static size. 

Data is continually transferred between level $k$ and $k+1$ in block size "transfer units". For two adjacent blocks in our memory hierarchy they tend to share the same transfer unit size, whereas as we go down the transfer unit size for safe L1/L2 is much different than L2/L3. As an extreme example consider the difference between registers and cache, which operate at the basis of a word, but then between L2 and L1 weare dealing with bytes of data. 