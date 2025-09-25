---
title: Process Control Block
tags:
draft: "False"
---
# Process Control Block
PCBs are used to represent [[Processes]] by our system, and take account of the state of a process, the number of a process, the program counter (how far we are into execution of a program),registers, memory, limits, open files, etc. 

We need a pointer to each block of memory where our code is stored for a process. We also want to know the list of files opened. We only update the [[Process Control Block]] when we move from different states, like from ready to running etc.

We also have a process ID/process number, this is the ID of the number, and it is unique, each correlates to a single block. We also have process states, that tell us the state a process is in at that moment in time. The [[Program Counter]] indicates the address of the next instruction to be executed by the particular process, which makes sense since when execute code we execute code line-by-line, so we need to find the next to execute our code.

Registers are [[CPU Registers]], there are different kinds of registers, but this tells us which CPU registers a program is using.  We also have CPU Scheduling Information, which the [[Scheduler]] determines which order our processes should be executed in, and how long our program should be executed for. 

We also have the memory management information consisting of limits. We also have the [[IO]] Devices associated to our device. All of these ideas are grouped together in the [[Process Control Block]], which allows us to keep all of the relevant information for [[Processes]] in their own respective container. 