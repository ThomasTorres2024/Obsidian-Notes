---
Probabilistic Algorithm: 
tags: 
draft: "false"
---
## (Definition) Randomized Algorithm
A randomized algorithm is an algorithm that generates $r \in \{ 1,\cdots,R\}$. We generate the number and then execute our algorithm in some way with respect to this number. 

We would also expect that despite given the same inputs, we could get different outputs because we assume that our algorithm does not have pseudo random number generations. The algorithm may run for a different number of steps or produce different outputs, potentially generating the incorrect output with some [[probability]]. 

Generally, we want to reduce the probability of incorrect output to be something quite small. We also want to understand the runtime for our probabilistic algorithms. 

From this we have two categories of algorithms:
1. [[Monte Carlo Algorithms]], algorithms that are probably correct, we have a constant probability that we get a correct answer 99% of the time. An example of a Monte Carlo algorithm is the [[Feivald's Algorithm]]. We are not guaranteeing that our matrix really indeed is the correct product, but we are able to reduce our margin of error nicely. 
2. [[Las Vegas Algorithms]], meaning we run in what is likely to be [[Polynomial Time]]. [[Quicksort]] is enough to give us a fully sorted array, but it might not run in the nice $O(n\text{log}(n))$ time. 

Either our algorithm is correct and probably fast, or fast and probably correct. These are the two types of tradeoffs we are working through. 

The lecturer also mentions an in-between: 
3. [[Atlantic City Algorithms]], meaning that our algorithm is either probably right and probably fast, and by some transformation we can convert them into [[Monte Carlo Algorithms]] or [[Las Vegas Algorithms]] 