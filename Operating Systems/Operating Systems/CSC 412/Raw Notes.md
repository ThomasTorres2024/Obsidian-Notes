9/23/25 notes raw- Mostly on processes and how scheduling works under the hood
The OS when executing needs to make sure P0 has their states saved in memory before we begin executing a new item. If we want P1 to be promoted, we need to restore the state of P1 from PCB, so PCB1 runs. Eventually, PP1 might terminate need io, we save state of P1, and restore P0 fom PCB0. 

In UNIX we distinguish running between running in user mode and hen running in kernel mode. 

Process Scheduling
We have a low level scheduler, and it must have very fast throughoutput. When a process is created, its basically put in ready state always or refused on modern CPUs. We have a ready queue for our CPU, where each item should access our CPU first. We also still have our IO many IOs. If we have another process and we need to add it, the scheduler will order a process in our ready queue, it satisfies some aspect. If a process goes to do I/O/Terminates, back to ready etc, we take the head of the queue. In practice, all we do is have a linked list that stores our PCBs togeher. .

Second scheduler, if we've been running for too long it puts us back, one has premention 

What's a good scheduler? Well we want to maximize the CPU use, most expensive of the system, so CPU should never be idle, put it to use always, throughput maximize items completed per time unit

We want to maximize these things too but its hard to measure these, like predictability, we want thngs to finish around the same time. Justice, a process should always be able to run a process.

we want to minimize 
Turnaround time, the time between submission of a process and its termination. We want to minimize te amount of time a processor waits for a CPU, which is the waiting time, it is NOT the time spent in the waiting state. Response time, time for an interactive process before first output to user. 

Preemptive vs non-preemptive scheuling, non-preemptive is when our process leaves the cpu voluntarily, preemptive removes items for us. Windows, US, MacOS, all are preemptive. 

The time slice is known as quantum, the amount of time we have spent in the CPU. We still have the same amount of time between our saving and restoring states and pulling items out from the CPU, we don't want all of our time to be spent on saving our state and restoring our state. 

* Switches to Time*

Where does the notion of time come from on a CPU? We have oscillators that use crystal clocks that oscillate at some constant time. Temperature really effects our time, so as CPU gts warmer, then 

Classic Scheduling Algorithms
- no premption, no io, just termination. we have a normal queue no pq, and w just seve the first elements to the cpu each time


---
9/30/25 
# Process Creation

Today we will cover the process ID mostly. 

The user is identified with a specific number. The admin has their own number. This is uid 0 and also the root. Logging in generally means going to where the root is. Any process on our computer has two pairs of identifiers, uid and gid. 

In Unix the pid continues to increase. This allows us to order processes based on this fact, we can impose a sense of age on them.

All process are created by another process except for 0 are created by another process. The way that we create more processes is by forking, thus every product has a parent process, tthe id of the process that created its child processes. 

In unix the boot task has PID 0

The fork function is called from the parrent process It goes to the process table and generates a child process with the according information, makes a [[Process Control Block]] for it. +

The first thing our program does in C is try to load into memory the values of everything initialized, bfore the first line of main is even run. 

An example of a program laucnhing another program is using a basch script, we call the kernel. When we create a process everything is the same except for the process ID. THus when we copy a program we are doign this behind the scenes. 

In old code it would common to write int p = fork(), nowadays we prefer pid_t because it is an unsized long whereas int can take negative values. 

When we use fork, we create a child process. The parent will have the pid returned, but the child will get 0. 

Immediately after we fork a process, we need to check, am I the child or am I the parent. Anything else will be wrong.  This means that we need to check if p is 0, which implies we are the child. 
If we try and fork and we get a negative then we did something wrong, something happened.

Say if we do the following:
```
for(int k=0; k<3;k++){
	pid_t p=fork();
}
```
We do not know which one is running, which process, this si the result of the scheduler which determjnes this for us. This generates $2^k$ many children. 

Generally, process code should look like this
```
for(int k=0; k<3;k++){
	pid_t p=fork();
	
	//if our process is bad and has a bad PID 
	if(p<0){
		call for hold;
	}
	//generally we want to call a function that handles our children with the number of other processes, k
	else if(p == 0){
		childFunction(k);
	}
	
}
```
The child function should be void. It also must end with exit(0) in our child function. We don't want to return back up to our loop and continue repeating the same process. If we make our program to adapt to many many cores, then we can do multiprocessing and get more CPU time. 

#(To Do) draw tree for processes creating one another
 
We cannot build our program around the idea that we know what CPU our program is using ahead of time. 

The exec command allows us to run programs. It flushes the parent, which in this case would be bash, and instad we can execute something else. 

When we wait for children to wait we have a function for this.

We also have the flush command, when we use flush, which halts the console's output since the console uses a buffer, and isn't a straight away thing. 

---
# Forking day 2 
When a function is called its contents are put onto the stack, all of its contents are loaded into our tack memory.When execution is complete, we clear all of our stack memory and go back to main. 

The fork call is another call on the stack, but instead we make a new process with its own main, own fork etc. 

There are process hierarchies in unix with the ids of its children, and they also have different pids etc, they also have links to all of the sibling pointers. We have younger sibling and older sing pointers. We have a pointer from the parent to the oldest child. 

The call to [[Exec()]] is similar to that of [[Fork()]], in that we insert a new command instead of cloning our current command. 


```C
./prog ls -la ->>

//this particular one executes ls
execvp(argv[1],argv+1)
```
Execvp takes in the command, and then the list of args for the new program. Here, we are giving a command, and then list of args 

For instance for command:
```
./prog ./sum 12 20 30
```
(remember all things here are C style strings.)

```./sum``` is essentially a pointer to a command, and the remainder are condensed into a list known as the argv list. Our argv list here would look like: 
```
argv={"sum","12","20","30",NULL}
```

---
# Memory Management 
10/7/25

Environment list environ, an array of C strings with definitions of the form name

The stack pushes a [[Stack Frame]] onto the stack and stores all of the local variables of a function. 

---
# 

We are tasked with taking a queue of items and then having to laod them into a region of memory full of parititions. For each process we find the most suitable region and load it into memory, there is almost always some aount of wasted space. If a process cannot be loaded into a partition, it remains in the waiing staste in the queue. 

If a partition is freed from memory, then we can begin to query if items in the queue can fit into an of thes blocsks. 

Internal fragmentation, space wasted within a partition, so if we have a partition of 1500kb and a program only uses 900 kb, then the difference of 600kb would result in the space wasted or itnernal frag 

External fragmentation - when we want to split a partition into multiple partitions so that we can combine it 

Also another thing we need to check in our queue is if its fair, especially if theres a giant processing locking a small one. So we solve this maybe by multiple process lists. 

Multiprogramming with variale paritions
Once something is loaded into a block of memory it cant be shuffled around or moved at all. Here we resolve the issue of internal frag but not external, so we have a lot of additional space surrounded by our programs. 

- Allocation of a free hole
We have a coupe ways to find the blocks, we have the first fit which gets us the first accessible block, the best fit is the smallest hole that can accomodate us, worst fit looks for an exact fit and if nothing is found then we look for the biggest block that the smalle

---
# 10/16/25 More on memory management
We can represent memory as a bitmap. For instance we could set up a schema where we have a list of our memory where each entry corresponds to if we have filled it up or not. If it is 1 then it is full, if it is 0 it is not. All we are trying to do is find a hole of the correct size. 

Because we allocate $2^n$ in this general scheme, there is going to be some natural amount of internal fragmentation. There's also external fragmentation still since we may not use up everything. We waste a lot of memory storing the table, so if we have a lower amount of bits stored, we end up just wasting a lot more.

It turns out that we can store our free space as a linked list in memory. Each node has either if our block has a process in its place or a hole, It has the start address, the end address, and a pointer to the next. Another advantage is that we have an automatic way of telling if we have a process or a hole.

If we make an insertion, we need to be able to update the following hole, since a hole, or other process, always follows a process, and if it is a hole.

If a process terminates, and its next to a hole, then the space where the process was becomes, a hole. We then add the size of the next one and get a larger hole. We then repeat this process continually until we hit a process or end the linked list traversal. 

---

Journaling system, if there is an error transferring files then the jounraling system takes account of this and does something. We want to be able to store all info in the instance of a crash.

---
# Interprocess Communication
We have a few ways to communicate between dfferent programs in C:
lock files, 

We are mostly interested n working with processes that communicate with each other by passing files to each other. 

#### Pipes and FIFOs
Some of thee arliest IPC solutions Unnamed pipes are standard pipes, and are related to forking, establishes communications through related processes. Pipes are also undirectional 

One is meant to read, and one is meant to write. 

The pipe icon in unix is given by "|", it takeds the outpt o 1 process uses it for anothe rprocess

FOr intane in ```ls | grep De ``` we take the ouput of ls and feed it into grep. 

Pipes just say a number of bytes, we have to define some way to interpret the raw bytes that come in as a signal. On the receiving end we receive a block of $N$ bytes, again decodng is entirely our job here. 

When we use this forking model for IPC, the parent creates the pipe. It has a writing end and a reading end. Children have copy of the pipes that we create. gh

A pipe is really an array of 2 integers in C. 

```
FILE* fp=fopen(<path>,r)
int fd=open(<path>,...)

//fd is the file descriptor when our higher level function makes a low level call to C

```
pipe opens 2 files in C, one file to read from, and one file to write to 

At the start of the program we should write macros to define the read end and the write end. 

---
# Pipes (Cont.) 10/23/25 
Pipes are used like reading and writing itno files, pips are uentiely aunware of strings etc, we need a language and format that we can encoce and later decode 

We send a value that comes before the value to tell its lngth or send it as a string with a ]0 char at the end 

```
int PtC[2];
pipe(PtoC);

```

We make a pipe in C we make a lower level call to a file open call to open one in read and only and one at read write, these are added to a PCB. 

Case if we have a writer parent that writes to many child reader processes. Our parent process has a list of all files open on its PCB. In the PCB of our $n$ child processes we have the list of the file. When one of the child processes closes, note our kernel has a list of all of the child processes that have the file open, if one of the readr terminates, it goes to the address opened up and it walks through each process, and removes the accordng one which just terminated. 

When we try to write when no more readers are open then we encounter an error. 

On the reading end cloe the writ end no point to write. 

If our writing process 

# 11/4/25 Multithreading
Threading/multi thread, we take a process and its contents, and make it multi threaded. The single threaded process initially just has one register, one stack, versus the multithreaded process which has its own register/stack, etc. The benefit here is thread creation is much faster than fork creation, and also everything in a multi-threaded process can access the same [[Heap]]. 

Multi-threaded programming is essential, its soething needed as its the only way to really speed up our code especially if there's no significant change in processor spead. 

A thread has its own registers, progra counter, stack, thread ID, threads however share the same code section, the same heap, if we hit all of them with a signal like exit, then the entire process, not just the thread, gets nuked. 

We have a law known as Amdahl's Law which gives us a formula for a potential increase in our programs. We can think of our program sort of in a serial way, where we have things that are only serial vs things that can occur concurrently. 

We should think of this as like what fraction of our code is done in a serial way, and what way can be done in a concurrent way? 

Balance
- each thread should do about even work
Data Splitting, data dependency 
Does one thread rely on other threads
DO multiple threads need the same data? synchronization
testing and debugging issues 

Is the kernel aware of threads? depends on our OS in linux, windows, etc the kernel is ware of all threads, we also have the many to many model which maps multiple kernel threads to user threads 
- user space library
- kernel level library
- many threads to kernel model

We have a couple main threads, POSIX, Windows, Java, and C++ threads. POSIX pthreads,Windows, and JAva. pthreads are still used but we use a lot of C++ threads nowadays 

---
# Code Samples for 11/4/25

a thread is a c++ class, that came out in c++11, 

A created thread must be either detached or joined. A detach thread does it's own thing we don't check for it anymore. By default, whena  thread is created it must be joint, or at the end, we need to have it join, can cause awful segfault errors. We can very easily stop threads by some boolean that causes the thread to end. 

Generally better practice is passing a ptr to our thread functions specially as the threads get bigger, dont pass references to a struct to a function in c++, massive errors from thread functions are either caused by this, or by 

Integration by Random Points 
generate $n$ random points within a small region bound between $x$ min $x$ max and $y$min and $y$max. 
We determine if we are below the curve at that point, we have around $N$ total points and $n$ underneath teh curve.

We can approximate the area by:
$$\frac{n}{N}\cdot A \approx \int f(x)dx$$
We can use multiple threads to do multiple points altogether to add points along the region. It's important to note that we really need the 


