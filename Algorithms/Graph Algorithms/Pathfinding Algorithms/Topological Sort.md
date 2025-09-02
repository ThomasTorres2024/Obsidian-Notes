---
title: Topological Sort
tags: 
draft: "false"
---
# Topological Sort Motivation and Definition
Given a [[Directed Acyclic Graph]], we should be able to define an order such that we can [[traverse]] the entire graph. If we are studying at a university and want to take classes and be able to take all of them, we need to have a notion of what courses to take before we take other courses:
![[Pasted image 20250719233337.png]]
Another problem which motivates us is ensuring that all dependencies for a program are built before running the program itself. 
![[Pasted image 20250719233507.png]]

In order to perform a sort, we need a notion of an order. We introduce the idea of a [[topological ordering]], where for any two vertices in our graph, $A,B$ where there is a directed edge from $A$ to $B$ ($A,B$) then $A$ will appear before $B$ in our ordering. 

[[Topological Sort]] is an algorithm which finds a [[topological ordering]] in $O(|V|+|E|)$ time.  Topological orderings are not unique. There may be more than one way to achieve our answer. 

Not all graphs have Topological orderings, as graphs with [[cycle]]s are forbidden, and the graph must be directed. 

It also follows that every [[Tree]] has a [[topological ordering]] since each tree has no cycles. To find the ordering for trees, all we have to do is target the roots and add them in any order to our topological sort. We can then add the parents that correspond to these children and so on until we get to our root node:
![[Pasted image 20250720003039.png]]
We could include our nodes in the following order:
$$A,C,D,E,B,G,H,K,J,F,I$$

---
# Topological Sort Algorithm
We can generate a [[topological ordering]] by running the Full [[Depth First Search]] algorithm on each node in our [[Directed Acyclic Graph]]. We add nodes that have finished starting from the back, we add the node which finished first to the end, all the way to the first node we began at when we finish executing. 

So, all we end up doing is adding each node that finished to the front of our order. This gives us a reversed order of our visits, which is a valid topological ordering. We can express this in the following algorithm.

