---
title: Kernel
tags:
draft: "False"
---
# Kernel Introduction
The Kernel manages interactions between software running on a layer higher than itself, like drivers, user code, other user programs, and hardware underneath. The Kernel is launched via a bootstrap process and remains on until the program finishes executing. 

When we make Kernel level calls the kernel is executing these things on behalf of us. If a system makes calls to it and the Kernel executes it, the Kernel is the one in charge permitting the call. For instance a divide by zero error, the kernel will treat the error on behalf of the process. 

Interaction between the [[Kernel]] and the user is done through system calls. 

# Kernel Modes
The Kernel, particularly on [[Unix]] has two different modes of execution. There is the system mode and the user mode.
* [[System Mode]] - privileged with higher access rights and priorities to what one can do, types of changes one can make to the PC etc. We can only access the system space using this mode of privilege. A process can access to a system space through a call. 
* [[User Mode]] - less privileged. We run code from the user with user data. 

The [[Kernel]] manages two particularly important areas, the [[User Area]] or (u area) and the [[Kernel Stack]]. The user area cannot be accessed by user processes in writing mode in this address space. 

If a kernel is allows to execute multiple processes at once, then we need a stack to manage all of the different processes. 
# Contexts of the Kernel
The kernel can operate within two contexts, [[User Context]] and [[System Context]]. 

In [[User Context]], the [[Kernel]] is operating on behalf/at the service of a user process. The kernel answers a system call, and works to answer a call that comes from the user in [[User Mode]]. For 

User Context handles things like
* handle system calls
* handle [[Interrupts]] and [[Signals]] 

In [[System Context]], the kernel is doing things like keeping a table of open files, resources that the system can access especially memory
System Context
* maintain list of open files
* available resources like memory
*  keeping track of time, or enabling and closing [[Processes]]

A nice encapsulation of the two is in the following:
![[Pasted image 20250923132306.png]]
Something executing in the process space would include some code that we wrote that does not involve [[Kernel]] level causes, if we simply just executed some code declaring integers that would go there.

Something that is both process context and in system mode would include user run code/commands that are also using Kernel code, so for instance opening a file in C uses a kernel level call, as does segment faults and other exceptions. 

Code running in system mode and system context is completely inaccessible to the user, and consists of things important for the OS and its health and operations, like [[Interrupts]]. 