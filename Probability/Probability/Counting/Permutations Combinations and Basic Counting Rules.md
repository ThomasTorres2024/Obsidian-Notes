---
tit;e: Permutations Combinations and Basic Counting Rules
tags: 
draft: "false"
---
# Permutations Combinations and Basic Counting Rules 

With small examples, such as a tetrahedral die being rolled once, we only have four items in our sample space:

$$\Omega = \{1,2,3,4 \}$$
It is easy to observe and count this quantity. Some sample spaces have a size that is much larger to count over and to fully observe. We need to develop better techniques to handle these larger sample spaces. 

For example, the sample space we observe by rolling 2 die consists of 36 elements, which can be manually counted, but can also simply be observed in the $\textbf{basic principle of counting}$ which is also known as the $mn$ rule. 

---
# Basic Principle Of Counting

The basic principle of counting states for experiment 1 which has $m$ outcomes and experiment 2 which has $n$ outcomes respectively, then the total number of outcomes is $mn$. 

We can generalize this rule to some $k$ experiments in the following: 

$$\prod_{i=1}^km_{i}$$
Where we simply multiply experiment $i$ has $m_{i}$ outcomes, and taking the product of them naturally gives us the total number of outcomes. 

--- 

# Permutations 

Many times we run into experiments where we have an original $n$ many items we select from, and then remove 1 item resulting in $n-1$ items that we still need to choose from and so on. If we were to remove all items then we would clearly be removing $n!$ items since at each stage of removal we have $k$ choices, and then remove 1, and then have $k-1$ choices in the next step and so on: 

$$n! = \prod _{i=0}^n (n-i)$$
It might not always be the case that we are removing every element from our original n items, and we sometimes only remove the first $k$. This results in the more general permutation formula. We can first recognize our original product as:

$$n\cdot (n-1) \cdot (n-2) \cdot \cdots (n-k+1)$$
Notice that this is equivalent to writing:

$$\dfrac{$n\cdot (n-1) \cdot (n-2) \cdot \cdots (n-k+1) \cdot (n-k)!}{(n-k)!}=\dfrac{n!}{(n-k)!}$$
---
# Combinations

Sometimes the order of our experiments is not relevant, as permutations take order into account. We want to be able to skirt around this, so we divide by the total number of trials, $k$. 

We denote this as "n choose k" which is given below:

$$ {n \choose k} = \dfrac{n!}{k!(n-k)!}$$
---
# Binomial Theorem 

We can expand the polynomial given by $(x+y)^n$ using the binomial theorem which gives:

$$(x+y)^n = \sum_{i=1}^n {n \choose k} x^k y^{n-k}$$
