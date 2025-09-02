---
title: Algorithmic Complexity
tags: 
draft: "false"
---
# Definition
Algorithmic complexity can be defined as the [[big o]] runtime class that the solution to a problem resides within. 

Generally we have problems that are solvable in [[Polynomial Time]] and problems which are solvable in [[Exponential Time]]. Formally, we would denote our [[Polynomial Time]] class as $P$ and [[Exponential Time]] as $E$ we can express:
$$P \subsetneq E$$
Some problems that would be included in $E-P$ is in the $n \times n$ Chess class. We can establish a tree of all possible moves on the board, and ask if a specific player will win, and we can answer this question by exploring all possible paths along the tree, which is a demonstrably not [[Polynomial Time]]. Tetris, given a sequence of $n$ pieces we don't know if we can survive given a [[Polynomial Time]] algorithm, but we know that the problem is in [[Exponential Time]]. 

However, [[negative weight cycle]] is a [[Polynomial Time]] algorithm using [[Bellman-Ford]] on [[Directed Graphs]]. 

We also have a class of problems which can be solved in a finite amount of time, known as $R$, which formally be used to known as the recursive set of functions but is really anything we can work with. We have that:
$$P \subsetneq E \subsetneq R$$
There are many different classes in between, but we ignore these here. 

---
# Halting Problem and the Size of Not Computable Problems
In the [[Halting Problem]], we consider all problems which are outside of $R$. Given a computer program, we can ask if the program ever terminates. It turns out that no such algorithm exists which solves all such programs. This results in many problems being [[uncomputable]]. 

This is a type of a decision problem, and it turns out that many problems cannot actually be computed in the first place. We first can informally denote that a program is a string of bits, a finite string which can be translated into a binary number. 

A decision problem maps inputs to yes or no, where all inputs are just a number in $\mathbb{N}$. A problem is an infinite string of bits, where a bit corresponds to the answer of our problem as being yes or no in a binary string.

It turns out that our problem strings have a cardinality of that of $\mathbb{R}$, and are thus uncountably infinite, and those of the programs are the natural numbers, and since no bijection exists between the two functions, then we have that there are more problems than actual solutions that exist.  

Most problems we are interested in are solvable and are in $R$, including Chess and Tetris, even though those are exponential problems. 

---
# P vs NP
We have the $NP$ class. There is an ongoing debate in theoretical computer science if $NP = P$, but most people hypothesize that $P \subsetneq NP$. 

We can define our $NP$ programs first using a definition that is a bit odd. $NP$ problems are problems which are solvable in [[Polynomial Time]] using a "lucky algorithm". A lucky algorithm makes guesses all the time, and we make lucky guesses which result in the lucky guess, but ultimately we spend no time on the guesses that are not the guess we are looking for. 

In total, this results in a [[non-deterministic polynomial]] algorithm, which makes guesses then says either yes or no. A guess is lucky if we are guaranteed to lead us to a yes if such a yes exists. In a maze, if we have a source, we will choose a path that leads us to there, otherwise if we do not have an output, inputs do not mean anything. As long as we can find such a solution it is given to us in Polynomial time. 

For the game of Tetris, we have that tetris $\in NP$. For each piece, we need to do a polynomial number of guesses for each piece, and in the end we return yes if we survive, otherwise return no. If any such way to survive exists, we return yes, otherwise no. The question if it is possible for us to survive is in $NP$. but if it is impossible for us to survive is not. 

#### NP Definition 2 
An alternative definition of $NP$ is a set of decision problems which can be verified in [[Polynomial Time]]. As long as we can check that our answer is given in [[Polynomial Time]], then we can say that our problem is $NP$. 

Another way of solving Tetris is by providing a solution of moves for the $N$ pieces which can be verified in polynomial time that show that we survive. This would be the same as the definition of a program existing, since we can verify our solution in polynomial time. 

#### Verification Algorithm Definition
Given a problem input and a certificate, we have a [[Polynomial Time]] verification algorithm that satisfies two properties:
* $\forall$ yes input, $\exists$ certificate : verifier says yes 
* $\forall$ no inputs, $\forall$ certificates : verifier says no 

A lot of decision problems are $NP$, like Tetris and chess we can convincingly see why a given solution works for a given position and can be easily seen. 

---
# P vs NP Conjecture
Many people conjecture that $P \neq NP$. We also do not know if $NP=E$. These are very important problems in theoretical computer science, and this is something that we generally assume. 

We conjecture the two algorithms are different since the ability to make random guesses for inputs in polynomial time seems to be very different than normal algorithms, and has a way higher computational power, so we would generally believe that $P=NP$. 

---
# NP-Hardness 
We claim if $P \neq NP$ then Tetris $\not \in P$. 

$NP$ complete problems are the hardest problems in $NP$ on the boundary with exponential problems. 

NP hard problems are problems which are more difficult than any $NP$ problem or $NP$ complete. For instance, $EXP$ hard would be either $EXP$ complete or harder to compute. 

What does "as hard as" mean here? We think of this as a reduction problem. Say [[single source shortest paths]] problems and [[APSP]] problems, which are built on top of each other, or in our [[shortest path]] algorithms, many of which can be reduced to [[DAG Relaxation]] in some instance. Basically, we can boil a problem down to some other problem. 

If we have some problem $A$ that can be mapped to $B$, then it follows that $B$ is as hard as $A$. This would mean that every problem in $NP$ could be reduced to Tetris. 


