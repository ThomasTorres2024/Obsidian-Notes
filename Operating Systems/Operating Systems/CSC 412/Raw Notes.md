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