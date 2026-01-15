---
title: Quicksort
tags: 
draft: "false"
---
# Quicksort Motivation
[[Quicksort]] is a [[Las Vegas Algorithms]] that allows us to turn an array into a [[Sorted Array]]. 

Our main goal is practical performance and not algorithmic complexity. We have two interesting properties, one that we have an in place sorting algorithm which takes no auxiliary space and is this $O(n)$

In total all of the work is in the dividing step. We need to partition our array in 3. There are around three different variants of [[Quicksort]], including a [[Las Vegas Algorithms]] that we want to focus on. 

Given an in element array $A$, let us pick a pivot element $x \in A$, and then we will partition $A$ into subarrays.  In total, we break our array into three parts, everything left of our pivot point at $X$, which we will call $L$, the central element $E$, and on the right side $G$ for all elements that are greater. 

We want to recursively sort our subarrays of $L$ and $G$, so in turn we can do this in place so all we are doing is putting things back together, so in turn our combination time is trivial. From here we can look at the different runtimes for different [[Quicksort]] variants, which will be quick except for the [[Las Vegas Algorithms]] variant.

---
### (Variant) Basic [[Quicksort]]
We pivot on either the first element or the last index, so $A[1]$ or $A[n]$. We want to partition our given $x$, which will require an $O(n)$ time operation. We move things either to the left or right of our pivot at each iteration. 

If we have $A[1]$ as our pivot, then we will be able to see that our algorithmic complexity is actually $O(n^2)$. One side, $L$ or $G$ has $n-1$ elements, and the other has $0$. So in total, our recurrence relation here would be:
$$T(n)=T(0)+T(n-1)+\Theta(n)$$
Which eventually results in a runtime when solved of:
$$=\Theta(n^2)$$
At the beginning of the use of this algorithm, we have to shuffle it, which increases the chances that we have a nice value in the middle. 

We want [[Quicksort]] to have a worst time runtime of $n\text{log}(n)$. We want to find the pivot of our array intelligently. We would find the median value in our array.  

We can find the median using the $\Theta(n)$ [[Median Selection Algorithm]]. With this in mind, our new [[recurrence relation]] is:
$$T(n)=2T\left(\frac{n}{2}\right)+\Theta(n) + \Theta(n)$$
We have two theta $n$ terms because we need to consider the time for selecting our median, and then performing our partitions. This algorithm is practically very bad, since it has a recursive call for the median on each partition, and on top of that does [[Quicksort]] things. While it is asymptotically on par with [[Merge Sort]], this variant does not perform very well.  

---
### (Variant) [[Randomized Quicksort]]
The [[Randomized Quicksort]] is a [[Las Vegas Algorithms]].  $X$ is chosen at random from array $A$. The expected time is $O(n\text{log}(n))$ for all input arrays $A$. This is no longer our worst-case, but what we expect it to perform in. 

We will choose to examine another variant of [[Quicksort]], this time [[Paranoid Quicksort]]. This algorithm is interested in finding a balance partition. It might take a little longer than normal, but that's fine that's what [[Las Vegas Algorithms]] are supposed to do. 

We choose a random element $\in A$ to be our pivot, we perform the partition until the resulting partition until the cardinality of our left and right sides matches either one of the following identities:
$$|L| \leq \frac{3}{4}|A| \text{ and } \frac{3}{4}|A| \geq |G| $$
We allow ourselves some amount of imbalance at each level of the recursion. When we choose our port, if we were to choose it from the sorted array just to make this easier to see, we would want to choose it from the middle half portion, and not the end quarter portions.

![[Pasted image 20250813015426.png]]

A call is good with probability of $\geq \frac{1}{2}$. If $T(n)$ is the time required to sort our array, then our resulting recurrence relation will be:
$$T(n)=T \left(\frac{n}{4} \right) +T \left(\frac{3n}{4} \right) + \mathbb{E}[\text{number iterations}] \cdot cn $$Our pivot finding function is randomized, so we use an expected value. Generation is $O(1)$ or $c$, and 