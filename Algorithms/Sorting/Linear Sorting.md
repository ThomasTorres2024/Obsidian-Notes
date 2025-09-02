---
title: Linear Sorting
---
We have shown that under the condition of [[Comparisons]], which means that for all of our elements we have to make a series of at least $O(\text{log}(n))$ steps to properly compare any amount of items and see where along the list it should be situated. 

If we are to try and sort an array $A$, which consists of $n$ items, our entire space for the total number of arrays would be given by $n!$ which is really equal to the total number of permutation of elements within our array. If we think of the first element of our array that we examine having $n$ possible locations that it could be placed, and consider its final resting point fixed, then the for the next element we would consider, it could be slotted into $n-1$ places, and so on, which would give us:
$$\prod_{i=0}^n (n-i)=n!$$
Therefore, if we were to write out such a tree for our array sorting problems, our tree would have $n!$ many leaves, which reflects the total number of final states for our array $A$. 

If we were to put these bounds into our comparison tree from earlier in [[Hashing]], our tree would end up with a minimum depth of $\Omega(\text{log}(n!))$ which by [[Stirling's formula]] would give $\Omega(n \text{log}(n))$. 

It follows that any Comparison Based sorting algorithm would take $\Omega(n\text{log}(n))$ many comparisons. This follows from our analysis beforehand of the problem of comparisons in searching, which we had shown was bound with a floor of $\text{log}(n)$, and we are simply piggy-backing off of this fact. 

We want to be able to do better than this bound, and we can observe a set of sorting functions which are known as ${\color{red} \text{"Linear Sorting Functions"}}$, which operate in $O(n)$ time. If we operate on a small number of items, and assume all such items are unique, we can begin to discuss some of the methods which significantly cut down on our search time:

#### [[Direct Access Array Sort]] 
Let us initializes an array, $A$, which has a universe of $u-1$ keys with an array size of $u$. We can then stick each of our values in the array that we are trying to sort into our new array, $A$, where each of their keys should be placed, since they are numbers and unique, we do not run into any issues in the process of initialization of our array, and they fit cleanly into their keys. 

A lot of our cells tend to be empty in our array, or we expect that there would be a lot of space which is not being used properly. We can then take all of the indices that were along our array and insert them into a new array of the size of our original array in the order in which they are read along the direct access array.  

We can describe our process by the following:
* make our DAA 
* store item $x$ in index $x$ key in the DAA
* walk down our DAA and return items seen in order 

Making our DAA should take $O(u)$ time. Storing $n$ items our array will take $O(n)$ time. And lastly, traversing the DAA will take $O(u)$ time. 

Our total time complexity would be $O(u+n)$. We must first understand what $u$ could be. 

If it happens that $u$ is of comparable size to $n$, then it follows that our algorithm runs in $O(n)$ time. If we know that $u \leq n^2$, then our algorithm clearly is in $O(n^2)$. 

We are able to work through this by splitting up our numbers into two numbers, where we can map any integer key $k$ from $[0,n^2-1]$ to two smaller numbers, $(a,b)$.  We let our $a$ and $b$ be equal to:
$$a=k//n$$
$$b=k\text{mod}(n) $$
We can express any such $k$ as:
$$k=an+b$$
Which is like expressing $a$ with respect to a certain modulo group. Let us consider the array of elements we want to sort:
$$[17,3,24,22,12]$$
We can write these as tuples in the process described above:
$$[(3,2),(0,3),(4,4),(4,2),(2,2)]$$
Now we want to be able to sort this function in some way. We need to sort by our first digit, and also by our second digit. We need to know in which order to sort our objects. From this we introduce [[Tuple Sort]]. We can sort all numbers by their digits in the $n$s place and then sort each part on the end. It turns out though that our tuples may not actually be unique, and therefore, we need to be able

#### [[Counting Sort]] 
In order to deal with collisions and non-unique elements in our tuple arrays, we can put more than just a tuple at a key, we can put a pointer to a chain like in hashing. We need to ensure that we have order in insertion of these elements. To illustrate this point, we will perform operations on our list:

We can observe that if we sorted our list by its 1 element, we would get:
$$[(3,2),(4,2),(2,2),(0,3),(4,4)]$$
Where the second coordinate is non-decreasing. If we then inserted this into a DAA, with multiple chains associated for each $k$ coordinate (the first coordinate), we would end up preserving the structure of the first sort, and then imposing on it a second sort which adds another order on top of it. 

To illustrate what I am saying let's put this into an array with $n=5$ meaning corresponding keys, 0,1,2,3,4:
$$\text{DAA}=[[(0,3)],[],[(2,2)],[(3,2)],[(4,2),(4,4)]]$$
This process again is similar to [[Simple Chaining]], but instead we care about our order here. We do not overwrite our work on the lower digits, and we can handle non-unique elements.

Our time complexity for this is $O(n+u)$, since we instantiate our array of size $u$, and then we add $n$ items into our array. In this instance our $u=n$, so our run time is just $O(n)$. 

#### [[Radix Sort]]
Say if we had some $u$ bound by $n^3$ where $u \leq n^3$, we need to find a way to handle this. We know how to handle $n^2$ already. We can take a number of size $n^3$, divide it, and we get left with something of $n^2$, but this number we already know how to process. 

We can generalize this notion of breaking all of our integers of max size $u$ into a base $n$ tuple. By breaking an integer into $n$ components, we need to split it into an $n$ tuple, which will take $\text{log}_{n}(u)$ time. We have to run it over $n$ indices, so our runtime here amounts to  $\text{log}_{n}(u) \cdot n$. If it turns out that our $u \leq n^c$, this component would be equivalent to $O(n)$. 
 
We also have an additional factor of $n$ because we have to add each part to our new array, so our total runtime would be:
$$T(n)=n + \text{log}_{n}(u)n$$
Which is $O(n)$ if $u \leq n^c$.

We conclude with our runtimes here for Radix Sort and Counting Sort:

| Algorithm      | Time $O(\cdot)$        | In-Place | Stable? | Comments                    |
| -------------- | ---------------------- | -------- | ------- | --------------------------- |
| Insertion Sort | $n^2$                  | Y        | Y       | $O(nk)$ approximate runtime |
| Selection Sort | $n^2$                  | Y        | N       | $O(n)$ swaps                |
| Merge Sort     | $n\text{log}(n)$       | N        | Y       | stable, optimal comparison  |
| Counting Sort  | $n+u$                  | N        | Y       | $O(n)$ when $n=O(n)$        |
| Radix Sort     | $n+n\text{log}_{n}(u)$ | N        | Y       | $O(n)$ when $u=O(n^c)$      |
