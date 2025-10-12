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









