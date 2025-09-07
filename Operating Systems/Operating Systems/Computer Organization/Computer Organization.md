---
title: Computer Organization
tags:
draft: "False"
---
# Computer-System Organization
Modern computers have multiple CPUs nd many device controller which are connected through a common [[bus]]. This provides access to the shared memory of each component. 

This is an overview of the basic components that every single modern computer has. 

---

# Basic Overview of Organization
# [[Interrupts]]
Interrupts stop current processes from running on the [[CPU]], forcing the CPU to begin focusing on a different device or piece of hardware.

## [[Storage Structure]]
The [[CPU]] can load instructions from memory, but programs must first be loaded into our memory to run. Computers, general purpose ones, typically only can let CPUs read in memory from [[Random-Access Memory]] RAM. This memory is rewritable memory and very fast to access. Main memory is implemented in [[Dynamic Random-Access Memory]].

## [[Input and Output Structure]]
A big part of OS is being able to manage I/O devices, and there are many of these devices. The [[Interrupts]] process for I/O already highlights small I/O on I/O devices, but for larger amounts it gets more interesting. 