---
title: Sorting Time Complexity
tags: 
draft: "false"
---
# Comparison Model
We can restrict the items in our sorting to support comparison for objects that we will treat as black blocks ([[Abstract Data Types]]) which have a notation of "order", so we can sort them in some manner. This gives us the operands:
$$(<,\leq,>,\geq)$$
Algorithms that make use of [[AVL Tree]]s, [[Red Black Tree]]s, and [[Sorted Array]]s would be optimal in finding an item using comparison. We can show that this operation is optimal in $\Omega(\text{log}(n))$.  

Sorting methods that function on our trees and also like that of [[Merge Sort]] are optimal and can be proved to be in $\Omega(n\text{log}(n))$ 

Our time comparison is based on the number of times we use our comparison operators. 

#### Decision Trees 
Decision trees are a graph structure that allow us to take a tree perspective to see how our algorithms function.  We can view our algorithm as a tree of all possible comparisons and their corresponding outcomes.

##### Example, Binary Search: 
For example, binary search is one such algorithm, which searched for a particular value, $n$, within our array. Let us look for $n=3$ in an array $A$ of size $3$. The resulting tree corresponds to the problem:
![[Pasted image 20250712213636.png]]
Generally writing these isn't bad for small searching algorithms, but a sorting algorithm will be of exponential size and will be difficult to express. But, it is quite nice to express an algorithm as these. 

---
# Searching Logarithmic Bound

An internal node in a decision tree corresponds to a binary decision in our algorithm. A leaf node corresponds to us finding the answer. We can denote our root to leaf path as a full execution of our algorithm on one instance, which is really the root to leaf path. Lastly our worst case run time is the length of the longest path from the root to the leaves, the [[height]]. 

| Decision Tree  | Algorithm           |
| -------------- | ------------------- |
| internal node  | binary decision     |
| leaf           | found answer        |
| root-to-leaf   | algorithm execution |
| path length    | running time        |
| height of tree | worst case run time |
Binary trees are quite easy to work with. The problem of a minima for sorting or searching is quite hard. We are using a decision tree, which in this instance is a [[Binary Tree]] and is therefore easier to work with, and we know that the minimum height of a binary tree is given by $\Omega(\text{log}(n))$, so it would follows that this our lower bound for searching. 

---
# Sorting Logarithmic Bound
For sorting, our lower bound can be shown to be $\text{log}(n)n$. Our decision tree grows exponentially at each stage. If we have a container of $n$ elements, it turns out that there are $n!$ possible permutations of the container. 

Since we are putting our sorting problem into the decision tree, when we consider the number of leaf nodes, we would have $n!$ nodes since the number of leaf nodes is equivalent to the number of end states of our problem, which would turn out to be $n!$ if all of our leaf nodes are unique. We have a lower bound for our leaf nodes, which appears to be:
$$\text{leafs} \leq n!$$
Therefore, the resulting size of our tree would be less than $\text{log}(n!)$, which is the minimum possible height of our tree, then we have found our complexity:
$$\text{height} \leq \text{log}(n!)$$
We could use [[Stirling's formula]] or we could write out our log as a sum. Using the sum we would see that:
$$\text{log}(n!)=\text{log}\left(\prod_{i=1}^n (n-i)\right)= \sum_{i=1}^n \text{log} (n-i)= \sum_{i=1}^n\text{log}(i)$$
Using some identities we can see that:
$$ \sum_{i=1}^n\text{log}(i) \geq \sum_{i=\frac{n}{2}}^n \text{log}(i) \geq \sum_{i=\frac{n}{2}}^n\text{log}\left(\frac{n}{2}\right) = \sum_{i=\frac{n}{2}}^n\text{log}\left(n\right)-1 = \frac{n}{2}\text{log}(n)-\frac{n}{2}  = \Omega(n\text{log}(n))$$
We previously used Stirling's Formula before to re-write our answer. 