---
title: Storage Structure
tags:
draft: "False"
---
# Storage Structure 
The [[CPU]] can load instructions from [[Random-Access Memory]] to run, and is typically implemented as [[Dynamic Random-Access Memory]]. Each storage system has the basic functions of storing and holding data until it needs to be retrieved. Storage differs based on its function, like the speed at which we can access it, the size of the information that we can store, and the volatility of the memory being used. 

Computers have other forms of memory outside of RAM. When the computer turns on, a [[Bootstrap Program]] runs, which loads the [[Operating System]]. RAM loses its content when the machine turns off or is lost otherwise. Thus, it cannot hold the bootstrap program. 

The program uses [[Electrically Erasable Programmable Read Only Memory]] (EEPROM), and other forms of [[Firmware]] which is nonvolatile and lingers after the computer turns off. This type of memory is mostly used be static programs and data that we don't need to write over. 
#### Memory as a Byte Array
Memory is generally stored as an [[Array]] of bytes. Each byte of the array has its own address. We can interact with memory by using a sequence of load or store instructions on specific memory addresses. 

The load function takes a byte or word from main memory to an internal [[Register]] in the CPU, and the store function moves content of a register into the main memory  

#### Instruction-Execution Cycle 
In a typical Instruction-Execution Cycle on [[Von-Neumann Architecture]], we fetch an instruction from memory, and store that instruction in the [[Instruction Register]]. We run through the instruction loaded into the register, which decodes the instruction and then maybe fetches some more data and puts it into more registers. We may store the result of the execution in memory as well. 

Sometimes we want programs and the data programs generate to stay in memory even when the computer it is shut off.  On most computers this is not possible because of two conditions. 

1. [[Main Memory]] is too small to store all needed programs and data forever. 
2. Main Memory is volatile, meaning power goes off to the computer, it no longer has access to the contents of the program or its source code 

---
# Secondary Storage 

Therefore, computers have a secondary storage in addition to the very fast CPU storage that is very volatile and temporary which is an extension of main memory. Secondary Storage is able to store a lot of information permanently. The most common secondary storage devices are [[Hard-Disk Drives]] (HDDS) and [[nonvolatile memory devices]] (NVM), which can store programs and data. 

Most programs are stored in [[Secondary Storage]] until loaded into memory. Secondary Storage is often the source and the destination for data. Secondary Storage is quite slow, and thus it is of central importance to a computer. 

# [[Tertiary Storage]]
Tertiary Storage consists of slow memory that is usually used as a backup for content. 

---
# Basic Storage Structure
The computer stores information as [[Bit]]s. A bit has two values, either $0$, or $1$. All other storage comes from collections of bit together. A [[Byte]] is a collection of 8 bits. On most computers it is a very convenient chunk of storage. 

Another term that we use to describe a collection of bits is [[word]], which is a "given computer architecture's native unit of data", which is constructed from one or more bytes. For instance, a computer which has $64$ bit architecture has $8$-[[Byte]] words $(64/8)$. 

We tend to measure things in collections of bytes for instance:

| Name          | Size           |
| ------------- | -------------- |
| Kilobyte (KB) | 1024 Bytes     |
| Megabyte (MB) | 1024$^2$ Bytes |
| Gigabyte (GB) | 1024$^3$ Bytes |
| Terabyte (TB) | 1024$^4$ Bytes |
| Ptabyte (PB)  | 1024$^5$ Bytes |
In Networking we round our bits because precision is super important there but here not so much. 

---
# Other Types of Memory Layouts
Instead of just having the Main Memory CPU/Volatile memory and the secondary storage we could have some operating systems that have a [[Cache Memory]], [[CD-ROM]], [[Blu-Ray]], [[magnetic tapes]], and so on. 

---
# Storage Hiercarchy
We can visualize the main types of memory and the hierarchy they live within:
![[Pasted image 20250907141608.png]]Registers, cache, main memory, and nonvolatile memory, uses semi conductor memory.
