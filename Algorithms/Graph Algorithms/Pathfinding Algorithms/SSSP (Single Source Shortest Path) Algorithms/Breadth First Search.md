---
title: Shortest Path Problem
tags: 
draft: "false"
---
# Shortest Path Problem
A [[path]] is a sequence of vertices that take us from one vertex to another vertex along a [[Graph]]. If we are looking for the smallest path, in turn we are looking for the path which is the smallest total distance, meaning that when we sum the [[weights]] of the edges along our graph, that we end up minimizing the total sum of them. 

Another way we could think of distance is the number of edges in our path minus 1 (since we need to account for the root node), and also the total number of edges is equivalent. 

# Shortest Path Algorithm Computation
Let us consider a set known as the "[[level set]]" of a vertex, which is the set of all points that are a distance $\delta$ away from our vertex. We denote our level set by:
$$L_{k}=\{ v \in V : d(s,v)=k \}$$
One way that we can achieve this end is by computing the level set for all $k$. which gives rise to an algorithm known as [[breadth-first search]].

We should be able to see that $L_{0}$ should contain only one node, which is the node we are beginning at - the source node, so:
$$\delta(s,s) = 0$$
There is a bit of induction going on here. From the level set 0 we can compute level set 1, from which we can compute level set 2, all the way to k. We can write some pseudocode for our algorithm. 

We need to continue searching until we get an $L_{n}$ where the level set is empty. We need to iterate through all vertices in our previous level set, and we also need to be able to determine if we have added a node to an existing list already. We scan through the nodes in the adjacency list and add them to our next node. We also know that our predecessor must be the node that we bridged from. 
```algorithm
i = 1 
while L_{i} != None:
	for v in L_{i-1}:
		for u in Adj(v):
			if u not in L_{j} for j in (0,i-1):
				add v to L_{i}
				P(v)=u
```
We are able to prove this by induction as well if we need to.

If we want to know the time complexity of our algorithm, it will be at least $O(|V|)$ since we iterate through all vertices, but we also have a for loop on top of it where we need to visit all of its nodes. We never re-visit a node also. 

We know for the iteration through the edges of our node that we will take $O(|E|)$ time, recall the formula seen in the [[Hand Shake Theorem]]:
$$\sum_{v \in V} \text{deg}^*(v)= \begin{cases} \text{undirected} & 2|E| \\ \text{directed} & |E|\end{cases} $$
Therefore, our algorithm is "linear time" meaning it is:
$$O(|V|+|E|)$$
Which is more expressive and captures more detail, since one term may dominate over the other. 