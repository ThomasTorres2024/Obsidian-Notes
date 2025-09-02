---
title: Johnson's Algorithm
tags: 
draft: "false"
---
# Johnson's Algorithm 
Johnson's Algorithm is a [[APSP]] algorithm which essentially checks if there are any negative weight cycles along our [[graph]], and if none exist then it enforces that all edges along our graph have strictly non-negative values.  

We transform a graph without [[negative weight cycle]] into a graph which has strictly non-negative edges, which we will all $G'$, and then run [[Dijkstra's Method]] many times along this graph. 

#### Algorithm Steps 
- Compute each $\delta(s,v), \forall v \in V$ using Bellman ford. We modify $G \to G_{s}$ by placing node $s$ such that $w(s,v)=0$, and then use bellman ford to probe for [[negative weight cycle]]s. 
- If $\exists \delta(s,v)=-\infty$, then we abort and stop looking
- Otherwise, we reweight  $G$ into $G'$ by reweighting each edge, $(u,v)\in E$ by $w'(u,v)=w(u,v) +\delta(s,u) -\delta(s,v)$ (we know we have no [[negative weight cycle]]s, so we know everything will abide by the triangle inequality so we apply this to all edges along $G$ when making $G'$) 
- Solve [[APSP]] on $G'$ with [[Dijkstra's Method]]

---
# Correctness
We have shown the correctness aspects of this graph to be trivial, since we have shown that each path weight will already be modified by the same amount beginning at one vertex and ending at another for every pair of vertices along our graph.  The correctness of this method was basically already argued and established in [[APSP]]. 

---
# Runtime 
Doing the check with bellman ford takes $O(|V||E|)$ time. 

Doing the re-weighting takes $O(|E|)$ time. 

Doing [[Dijkstra's Method]] takes $O(|V|^2\text{log}(|V|)+|E|)$ time. 