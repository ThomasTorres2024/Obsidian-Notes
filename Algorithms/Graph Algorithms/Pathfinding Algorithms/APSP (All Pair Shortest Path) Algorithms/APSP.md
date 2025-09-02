---
title: APSP (All Pairs Shortest Paths)
tags: 
draft: "false"
---
# All Pairs Shortest Paths
Similar to [[single source shortest paths]], All Pairs Shortest Paths (APSP) tells us $\delta(u,v)$ between all $u,v \in V$, meaning that we get the distance between all possible pair paths within our [[Graph]]. This implies that our runtime will be on the order of $O(|V|^2)$, meaning we need to link each vertex with all other $|V|-1$ vertices in our graph to get its path and so forth. 

This will serve as the lower bound of our algorithm which operates with maximal efficiency - $\Omega(|V|^2)$. We can think of this in the same way as going through our $|V|$ vertices for the single source path problem, except we have to go through all possible paths and so this gives us our limit. 

An immediate first thought solution to this problem is to use our other SSSP algorithms like [[Bellman-Ford]], [[Breadth First Search]], [[DAG Relaxation]], and [[Dijkstra's Method]] for appropriate graph types to get roughly quadratic runtimes on each algorithm. This is a "stupid" solution, it is nearly brute force on the vertices, but it works and is able to solve our problem in polynomial time. 

Here is a chart for the APSP algorithms and their runtime complexities: 

| Algorithm             | Runtime                                  | Best Usecase                                                                                                |
| --------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [[Bellman-Ford]]      | $O(\|V\|^2\|E\|)$                        | A graph which has both positive and negative weight entries, potentially allowing [[negative weight cycle]] |
| [[Dijkstra's Method]] | $O(\|V\|^2\text{log}(\|V\|)+\|V\|\|E\|)$ | Can only be used on graphs with positive entries. Works on cyclic graphs.                                   |
There are several algorithms we could use that reduce our runtime from simply repeating [[single source shortest paths]] in parallel. We will consider the case of directed graphs without negative weight cycles in our discussion of these algorithms. 

We want to be able to run Dijkstra's on our graph which has mixed weights but no [[negative weight cycle]]s. We can find shortest paths along this graph by finding a mapping to a new graph from our original $G$, $G'$ which preserves shortest paths and has the property that every edge weight will be $\geq 0$. 

A shortest path in $G$ should continue to be a shortest path in $G'$. If we can do this transformation, all we need to do is run [[Dijkstra's Method]] on that new graph, and that would solve the problem. This leads us to our first claim: 

### Claim: We can compute distances in $G$ from distances in $G'$ in $O(|V|^2 +|V||E| )$
We have the new graph $G'$, which can run [[Dijkstra's Method]] $|V|$ times, which gives us a shortest path tree beginning at each vertex $s$, and then we can bring this to our graph $G$, which has the same edges but just different weights. 

All we need to do is compute our shortest distances on the graph in $G$ using [[Breadth First Search]] or [[Depth First Search]] for that particular $s$, and then we do this over all $s \in V$, and then we obtain the algorithm with a runtime of $O(|V|^2 + |V||E|)$ 

We also have another important claim to address, namely that this algorithm outlined is impossible if $G$ contains a [[negative weight cycle]]:

### Claim: Not possible if $G$ contains [[negative weight cycle]] 
If $G$ contains a negative weight cycle, then a shortest path is $-\infty$, which implies that our shortest path is not simple. However, shortest paths in a graph where all weights are greater than or equal to zero are simple. 

---
# Ways of Resolving Negative Edges in Graph
One way which we may initially think of resolving the problem of having negatively weighted edges in our graph is by adding a large enough number to each weight on our graph, however, this does not preserve the shortest path, as it biases us towards certain paths and edges that wouldn't otherwise be present. 

### Claim: Add $h$ to all outgoing edges from $v$, and take away $h$ from all incoming edges  
Another way we could preserve shortest paths is by adding some $h$ to all outgoing edges of vertex $v$, and subtract weights to all incoming edges from $v$. We claim that shortest paths are preserved under their transformation. 

##### Proof:
Consider path $\pi$, which has weight $w(\pi)$. Let us modify vertex $v$'s edges by adding $h$ to all of its outgoing edges, and decreasing the weight of its incoming edges by $h$. 

If our path, $\pi$ does not goes through vertex $v$ then the weight of our path is not modified, so our path's length is preserved 

If our path, $\pi$ goes through vertex $v$ then our overall path weight has not changed, since we added $h$ to it and decreased it by $h$, which balances out to 0 when we consider the outcoming and incoming weights of our path. We want this to extend beyond a single modified vertex $v$, and have it encompass all vertices in our graph. 

Let us define a function function, $h : V \rightarrow \mathbb{Z}$, denoted $h(v)$.  Let us consider graph $G'$, based on the above transformation for each $v \in V$. We set an $h$ for each vertex and add this potential to all incoming edges, and subtract it from all outgoing edges. 

### Claim: SPs are still preserved 
Let us consider path, $v_{0} \to v_{k}$, a path which has $k$ edges. We claim that the path, $\pi$, still has the same weight even after apply our potential function to it. 

Let us consider the updated weight of $\pi$ which we will denote by $w(\pi_{1})$:
$$w(\pi_{1})=\sum_{i=1}^k w'(v_{i-1},v_{i})=\sum_{i=1}^k w(v_{i-1},v_{i})+h(v_{i-1})-h(v_{i}) = w(\pi)+ h(v_{0})-h(v_{k})$$
In effect we change the weights between all paths by the same constant amount, so in total we are modifying every path by the same amount. 

At every step along our path, we want $\exists h$ such that $w'(u,v)=w(u,v)+h(u)-h(v) \geq 0$.  
Does there exist such an $h$ that does this? 

We get the following identity by re-arranging the above expression:
$$h(v) \leq h(u) + w(u,v)$$
Note that this is basically the triangle equality. It will work as long as we do not have negative infinite weights. We need all of these values to be finite since infinite values don't do anything. 

We can add a new vertex $s$ with a 0 weight edge to all of the vertices along our graph. This new modified graph, $G_{s}$. We can then determine the shortest path $S$ to all nodes along the graph. If a vertex has negative infinite weight here in $G_{s}$, then $G$ must have a negative weight cycle since nothing loops back into $S$. This allows us to abort. 

Otherwise, we reweight everything using our shortest distance from $s$, to be the total shortest distance. 

```
if(for all of v in V, at least one d(s,v)==-infty):
	abort
else:
	reweight h(v)=d(s,v)

```

This gives the main idea behind [[Johnson's Algorithm]]. 