---
title: Input and Output Structure
tags:
draft: "False"
---

We have described the standard I/O procedure in the [[Interrupts]] section and is fine for small amounts of data, but for Bulk data, we need other methods. To solve this we use, [[Direct Memory Access]] (DMA). We sett up the buffers pointers and counters for the I/O Device, and then we send an entire block of data to the CPU directly from the IO device or vice versa. 

One interrupt per block is generated, and tells the [[CPU]] that the operation has completed, unlike for small I/O of the size of a [[Byte]] which sends an interrupt for each byte. 

Some systems use "switch" architecture instead of [[bus]] architecture, which makes DMA even more effective. 

