---
title: Bellman-Ford
tags: 
draft: "false"
---
# Bellman-Ford Introduction
Bellman-Ford gives a method for determining the [[shortest path]] from a source node, $s$ along graph $G$, with [[edge]]s that have [[weights]] that are any integer value. Previously, we saw [[DAG Relaxation]], which is an algorithm that allows us to find the shortest path along [[Directed Acyclic Graph]]s. 

We need to be able to overcome the obstacle of an infinitely long path. We need to first be able to detect the existence of a negative weight cycle. 

---
#### Sub-Problem 1.) Detecting a Negative Weight Cycle Along Undirected Graph $G$:
Given the undirected graph, $G$, we can determine with $G$ has a [[negative weight cycle]] if it turns out that we have a single negative edge, which would allow us to continually traverse the edge back and forth. 

Detecting a [[negative weight cycle]] along  a [[Directed Graphs]] is more difficult. 

#### Sub-Problem 2.) If Algorithm $A$ solves SSSP in $O(|V|(|V|+|E|))$, then show how we can solve $SSSP$ in $O(|V|\cdot|E|)$:
The two algorithms have the same asymptotic runtime if $|V|$ is asymptotically larger than $|E|$.  We could use [[Breadth First Search]] or [[Depth First Search]] to find everything connected to $s$ 
We want to find a method to determine negative weight cycles on directed graphs, and then to find an algorithm that solves SSP in $O(|V|(|V|+|E|))$.

# Simple Shortest Paths 
We have some claims that we want to verify.

1. If $\delta(s,v)$ is finite, then $\exists$ a shortest $s-v$ path that is simple, meaning that the path passes through each vertex at most once. 

	To prove this fact, let us consider the case where there was a shortest path that contained a cycle. We know that the cycle must be positive, because if it were negative we could continually keep looping. 
	
	```mermaid
	graph LR;
		S((S)) --> C((C))
		C((C)) --> C((C))
		C((C)) --> V((V))
	```
	It must be the case that our loop has a positive value. Since our cycle has non-negative weight, we can remove a cycle from our cycle $C$, and keep repeating this process, until we end up creating a simple path. 

	 We know that for a [[simple path]] that does not repeat vertices, we have at most $|V|-1$  edges that we can traverse. 

	Importantly, this allows us to impose an upper bound on the total number of paths to consider, which helps us constrain our search. 

	 Let us also introduce the $k$-Edge Distance, $\delta_{k}(s,v)$ which gives the shortest path distance, if reachable, in $k$ edges. If we have that $k=|V|-1$, it follows that:
	 $$\delta_{|V|-1}(s,v) \implies  \text{ shortest path between s,v if finite}$$
	 Note this isn't an IFF if we have a path of infinitely many edges, but in the case of a finite path we get a nice limit for the number of edges. If our graph had all positive weight edges, we would be done. 

2. If $\delta(s,v)=-\infty$ then $v$ is reachable from a witness

	If $\delta_{|V|}(s,v) < \delta(s,v) \implies$ $\delta(s,v)$ has a negative weight cycle 

	We have already established that a minimum path of finitely many edges is at most $|V|-1$ edges. If we have more edges than this quantity with a path that is still minimum, then we are guaranteed to have a negative weight cycle, which would therefore imply that:
	$$\delta_{|V|}(s,v)=-\infty$$
	If we can find a vertex, $v$ that has this property, then, it follows that there is a negative weight cycle. We call $v$ a "witness". We can prove this idea via contradiction. Is it possible that we could have a witness that satisfies $\delta_{|V|}(s,v) < \delta(s,v)$ that is non-infinite? 

3. 

