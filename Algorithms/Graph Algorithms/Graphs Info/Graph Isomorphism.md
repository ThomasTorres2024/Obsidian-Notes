---
title: Graph Isomorphism
tags: 
draft: "false"
---
# Graph Isomorphism Introduction
If we have two graphs, $G_{1}$ and $G_{2}$, even if graphs have different nodes with different names and edges between them, it may be the case that there is a mapping between the different node sets that results in the two graphs secretly being the same. 

For example consider the following two graphs:
![[Pasted image 20250729002912.png]]

If we are able to find a correspondence between the [[node]]s of our [[Graph]] that preserves our [[edge]]s between the nodes, then it follows that our two graphs are isomorphic. 

We can more formally define an isomorphism between the two graphs if $\exists \Phi : V_{1} \to V_{2}$ which forces the following constraint:
$$\forall u,v \in V_{1}, (u,v) \in E_{1} \iff (\Phi(u),\Phi(v)) \in E_{2}$$
Which is to say that the mapped version of our edge is also guaranteed to be in $E_{2}$ iff there is a corresponding graph in $E_{1}$. We do not even know if Graph Isomorphism is an NP complete problem for all graphs, but for specialized trees polynomial time algorithms do exist that guarantee such mappings. 

---
# Algorithms for Identifying Isomorphic Trees 

#### AHU
AHU allows us to serialize our tree into a string. We can then compare our string with the string of another graph and if they are equivalent it follows that the tree is equivalent as their is a bijection between each string and tree. 

We assign a 'Knuth Tuple' to each leaf node. We then go to the parents of the leaf node, and then for all parents which have greyed out children with a knuth tuple, we would wrap the tuples of the children in our new tuple in this layer:
![[Pasted image 20250729005306.png]]
We keep repeating this process:
![[Pasted image 20250729005342.png]]
When we reach the last layer, we need to be able to sort our tuples from each branch into a new tuple. Our resulting tuple would be: ![[Pasted image 20250729005531.png]]
We could now encode another tree using this method and then compare the strings character by character. 