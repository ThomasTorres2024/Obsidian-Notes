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