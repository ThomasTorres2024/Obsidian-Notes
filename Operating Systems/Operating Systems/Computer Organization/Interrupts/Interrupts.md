# [[Interrupts]] 
Interrupts alert the CPU to events that require attention. [[Interrupts]] are sent to the [[CPU]] by [[hardware]] along the [[system bus]]. Interrupts are crucial for the interaction between [[software]] and [[hardware]]. CPU interrupts stop execution of the system, and transfers execution to a fixed location immediately. The fixed location typically has the address of where the "service routine for the interrupt is located", we execute the routine here, and then the CPU resumes computation on the interrupt. and cause it to focus on the thing which sent its request. 

We generally handle each interrupt with a specific handler and process for dealing with each kind of interrupt. Interrupts happen very often and must be handled very frequently, so we want to be able to deal with them quickly. We use a "table (I assume hashmap?)" of pointers to different interrupt routines. We access the table directly, there are no intermediate routines.

We store the table of interrupt responses in [[low memory]], meaning the first several hundred memory addresses in our machine. We have the addresses of the interrupt service routines for different devices plugged into our computer. This is known as the [[Interrupt Vector]]. The [[Interrupt Request]] gives a unique number corresponding to the vector, which then gives us the address of the interrupt service routine. 

If we need to change the processor state, that is the current values in the [[register]]s in our CPU, then we need to save our current state, and then execute our interrupt process, and then once it has terminated we return our saved state. 

![[Pasted image 20250907013645.png]]

---
# Interrupt Implementation 

We implement [[Interrupts]] using a wire directly in the [[CPU]] [[hardware]] known as the [[interrupt-request line]]. The CPU detects if a controller asserted a request, if it does it reads the interrupt number and jumps to the interrupt handler routine 

A [[Device Controller]] raises an interrupt through the [[interrupt-request line]] and sends a signal to the CPU. This allows the CPU to respond to asynchronous events. Modern interrupts need more sophisticated handling features than just this.


1. We need the ability to stop interrupt handling if needed
2. The ability to dispatch the proper input handler for a device 
3. We need to beable to respond to high and low priority interrupts in accordance with their degree of urgency 

These features are handled by the CPU and the [[interrupt controller hardware]] in modern computer hardware.

There are two kinds of interrupts, [[Maskable Interrupts]] and [[Non-Maskable Interrupts]]. We can disrupt and stop the execution of a [[Maskable Interrupts]], giving the developer and user more control, for this we reserve IO devices, external hardware requests, or timer interrupts. For [[Non-Maskable Interrupts]] we typically have critical failures like a memory failure, loss of power, or [[Watch Dog Timer]]

![[Maskable-and-Non-Maskable-interrupts.jpg]]

---
# Interrupt Chaining 
Typically, given an [[Interrupt Vector]], we have more devices than address spaces in our interrupt vector, so instead we make use of [[Interrupt Chaining]]. Our [[Interrupt Vector]] points to the head of a list of Interrupt Handlers. When the interrupt is raised, the handlers on the list are called until we can find a suitable one that handles the request. 

This structure gives us some compromise between a massive table with a lot of overhead and having a single routine to handle an interrupt. 

For instance, here is the Intel Processor Event Vector table, here the first 31 interrupts are reserved for [[Non-Maskable Interrupts]]. and the remaining 32-255 are used for [[Maskable Interrupts]]:
![[Pasted image 20250907085708.png]]

---
# Interrupts Summary
Interrupts are used to handle [[Asynchronous events]] and for many other reasons. Device controllers and hardware faults raise interrupts. Modern computers have a list of [[Interrupt Priorities]]. Interrupts are used very heavily in modern computing, so it is critical that we have a good way of handling them. 