---
title:
---
(Chapter 4)
What is a process? It's a dynamic entity, a program in action.  A [[program]] is just a dead piece of code, it is some static file. Since a process is dynamic, it has a state. The OS can infer things about the status of the process. 

For a given program, it is the case that 2 or more processes can run the same program/code. We want to know things like when does a program start executing, and how long has it been launched for. There is CPU time and also user time involved here that we need to be able to express as a duration. We want to know how much memory our program is using, maybe how many files it has opened. We also have the program counter, which is the address of the line of code currently being executed. There are many other features, like pausing a process and saving its state, 

It is entirely possible our process was paused mid-execution at the step of a calculation. We need to be able to restore the state that our process was in. 

For instance, if we are stopped in the middle of the execution of an arithmetic expression. We assign brackets into our equation to enforce order of operations or at least we can think of it in this way. This is what our compiler would see. It then converts our equation into an [[Abstract Syntax Tree]] which is capable of parsing the expression and evaluating it. Internally the operation varies a lot depending upon the language we are using. 

ASTs are recursive. In Java, Python, and C# we evaluate the left subtree recursively, and then the right recursively. In C++ we use a different way to traverses through abstract syntax trees. We evaluate each set of nodes with terminal children and do the operation. But in C++ we just want to do things quick.

#### Note. Dif in Compilers In Evaluating Arithmetic Expression
say if:
```
int x =6;
int y = x++;

//then y would be 7 after line y executes, we evaluate first and then we do it

//could compute to be either 6 or 7 depending upon the compiler, so it is big to note 
//the decrement and increment property
//we are never sure of the order of our evaluation
y=++x-x++;
```
When we get [[Interrupts]], we need to be able to maintain the state of our program's execution. The OS saves the only knowable information about a process during the save process into a PCB, a [[Process Control Block]]. 

The types of information we save into the [[Process Control Block]] includes:
* Every user has an ID number
* Start and run time
* Memory usage
* Files opened
* Program Counter 
* Values in [[Register]]s 

We only take account of these things during an interrupt, means whenever the [[Kernel]] activates or deactivates the process.

---
# Modes
We have two different modes of a process. A user mode, and a system mode. 

During user mode, a process is running its own code and manipulating its own data. Code that would be [[User Mode]] is:
```
int x=12;
x+=3;

//or 
float y = cos(3.5f)
a[]={3,5,6}
```
[[System Mode]] is when we are running code from the Kernel.  This requires access to the kernel data. For instance the following is system mode:
```C
FILE* fp = fopen("fileName");
```
fopen is actually a [[C]] runtime pointer, but this runtime pointer is actually a system pointer, that makes a system call. The [[Kernel]] has a table of all currently open files that has a record of all files that are not yet closed. As a result our code, even though we wrote it, is actually writing in system mode.

---
# States of a Process Throughout its Lifetime

Our state begins as new when it is created. We have to create an id for the process, allocate memory, and our state remains as new. 

Our process then becomes ready when it is loaded into memory. It has a [[Process Control Block]] created, all it needs is [[CPU Time]]. 

Once the [[Processes]] get [[CPU Time]], then the program is running. We can be running for awhile. We might be in user mode, system mode either is fine. We have 3 possible ways to terminate from the running state.

One is IO, one is termination, and one is waiting. Based on the amount of time, the [[Scheduler]] may take our program and return it to the ready state. Which forces us out of a program after $n$ minutes. 

* Terminate by just closing or exiting, crashing etc, maybe a seg fault. The OS needs to remove the [[Process Control Block]], update any tables, and so on and so forth. 
* We could be doing some IO where our program is waiting on some kind of input or output. OS pulls away [[Processes]] from the [[CPU]] to do some IO. When IO is done we go back to the CPU because something could be running already.    

The fairly confusing part of this is waiting. We are not waiting on the [[CPU]], we are waiting on the [[IO]]. 

A process also can be terminated and do IO at any point. 

Imagine if we have 1 [[CPU]] with 4 [[Processes]] running, $P_{1},P_{2},P_{3}$ and $P_{4}$. 