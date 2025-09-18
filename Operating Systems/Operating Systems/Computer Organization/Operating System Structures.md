---
title: Operating Systems Structures
tags:
draft: "False"
---
# OS System Structures
Most OS are very similar inside, we have a decided structure. The OS is something which allows us to interface between users and the resources, typically the [[hardware]]. The most expensive resource is the [[CPU]], and the one we want to optimize the use of. 

We also have memory systems with different IO devices. These are shared by 1+ users with 1+ applications. The OS deals with who gets what, and how to deal with conflicts of resource allocation. 

Users interact with the program in two differently ways, copying or deleing a file etc, by way of files. Before we had a way of accessing our OS through the CMD, but now its just another application.

What we have now is a bunch of processes that would like access to different resources. A program is a piece of code on the disk, it is static, it is dead. Once it is loaded it becomes a process, it has a status etc. [[Processeses]] are running programs. We could have 2+ running on the same program. 

Can at any point two processes access the same resources at the same time? Generally they can't, how do we deal with the conflict of access in a way that is fair. We have to deal with security here too. The more we add features, more users, networking, programs accessing the same info, we have a lot of new headaches to resolve involving security. In the 90s the OS used disc space to simulate having more RAM.

---
# Common Architecture 
IAS architecture is the most common which makes use of memory, CPU, and I/O devices, which all communicate togeher via buses. We have a control bus, an address bus, and a data bus telling us 

---
# Components and Functions
The operating system should be able to:
* load a process, launch a process, activate it
* we need to be able to suspend a process too, if we need to stop a process to focus on something else, w need to interchange between suspend and activate, we have to load things into registers and be able to save our info
* We need to be able to kill a process as well, we have 2 ways that can, one is a program has some kind of exit statement that tells us we are done, and when the user 

Memory Management, how do we actually load a process. 

Processes need to be able to talk. They either share some bock of memory that both processes read and write from. A and B, our processes, would then be able to agree with each other on a single protocol. Or, we either pass content directly to one another. Both are possible and are both used extensively since the 70s. 

If we can read and write from the same place, we create a much faster program. In theory this is the fastest. The messaging technique exists not because of a lack of memory because the OS would outright refuse it. Privacy isn't really a concern. Safety is our concern here. Passing between our processes turns out to be much safer. It can be quite difficult to do. 

---
# Structure of an OS
OS came from a single program that ran one program after another finished. OS grew out of this main idea, like Unix, Mac OS, and DOS. Here, every part of our program talked to the DOS peripheral. Our programs were super bad, sueper unsafe. We wanted instead a layered architecture. 

Below the OS will still had BIOs and such. We establish a hierarchy of how these things interact. We cannot bypass anything you can only support the layer above and below you. Each layer hides details a lot, nicer to work with. But, the problem with this is is that some parts of the OS exist at different layers, some between layers. It's a bit messy then to handle it. We could also get stuck between different labels. This system never went anywhere in reality. 

Instead we moved to [[Kernel]] architecture, which is still the system to this day. The idea is that we reduce the OS to its most basics. The kernel must do memory management, scheduling, synchronization, file systems, and some others.

GUI, networking, multimedia, all were moved instead to drivers. We are still essentially doing this in the current day. The kernel interfaces with the hardware, and also talks to things within our system that are lower level like drivers. 

The Kernel has an API with its own respective functions that need to be talked to in a certain way. For instance in [[C]], we make a call to the C runtime library when making a call. Underneath, the Unix kernel is running which opens this file via the open command in Unix. We are making a system call to the kernel by using this method. prinft as well is another kernel call. 

---
# Microkernel Architecture
People made the Kernel even smaller, does it need to know what files are and how we do that? We did away with vram, and a lot mor focus on IO. Files, networks, was all moved into "user space",
and the Microkernel was the new version of the OS. The problems with this is that the user layer talks to itself a lot, it is not that efficient for performance. 

---
# Modular Architecture
