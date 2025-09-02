---
title: Hashing
tags: 
draft: "false"
---
# Hashing from Sorting
The problem of [[Hashing]] arises from sorting and wanting to access elements of a data structure in less than $O(\text{log}(n))$ time. This run time is quite good, however we can do much better. 

[[Sorting]] and algorithms discussed here arise from a comparison model, where each string and number has an inherent order to them, and thus we can arrange them based on said order. 

At some point we end up evaluating at some true or false along our model, until we get to a leaf in our tree where we stop adding things to our list. We can think of our problem as a Graph in this sense. We start at 1 comparison, and then we continue to branch. 

For some given tree of $n$ nodes, the minimum possible height is $\text{log}(n)$. The leaves represent the number of outputs for our array, and to traverse ourselves to one such leaf is really the equivalent of evaluating a root to leaf path along our tree. 

In the worst case, we need to do as many comparisons as our root to leaf path which is the longest, which turns out to be the height of the tree. Our tree will be balanced, so its height will be $\Omega(\text{log}(n))=h$. 

---
# Direct Access Array
The direct access array is essentially the same idea as a normal array. The only difference is that we impose keys on it, and that if an item has a key of $k$, it must be placed at position $k$ in our index, compared to a normal array where we can place any element anywhere inside the array. 

Sorting is limited since we are limited to this binary characteristic of a log limit. But if instead, we look for a constant factor RAM based idea, we can just as well store and access our information well. We want to be able to go to anywhere in memory in constant time based on a number for an address. We have a constant time operation.  

If something is at the corresponding address, we return nothing, or we can return the item we found.  We might not always want to do this simply with numbers, as some numbers are so large that actually forming an array out of them can be inefficient and cause poor performance, or it might not reflect the actual size we are trying to store.

| Data Structure      | Container        | Static          | Dynamic       | Order   | Order           |
| ------------------- | ---------------- | --------------- | ------------- | ------- | --------------- |
|                     | build(A)         | find(k)         | insert/delete | min/max | prev/next       |
| Array               | $n$              | $n$             | $n$           | $n$     | $n$             |
| Sorted Array        | $n\text{log}(n)$ | $\text{log}(n)$ | n             | $o(1)$  | $\text{log}(n)$ |
| Direct Access Array | n                | 1               | 1             | n       | n               |
The direct access array is good at finding items and deleting or inserting them. We also are making the assumptions that we can only sort integers. It uses a LOT of memory however.

The direct access array is also a [[Set]] Interface. 

We are also making a subtle assumption that our words are stored as nice sized, typically 64 as is standard, bits. We want to ensure that our largest key, $u$, will be smaller than $2^w$ where $2^w$ is the "word size" on our machine. 

It turns out also that if we have a small key-size, we might not need to use a hashing function, and instead we can just use a direct access array and get our result. 

# Hashing 
The direct access array has too many keys. It has keys in the range of $0,u-1$. We want to find a smaller set of keys that could store all of our data. We can map items from $0,u-1$ to a set of $m$ keys where $m<u$, to the range of $0,m-1$. Our function $h$ performs:
$$h:\{0,1,2,3,\cdots,n-1 \} \rightarrow \{0,1,2,\cdots,m-1 \}$$
We can store our key at the address which is given by, for some $x \in$ the key space of $u$, $h(x)$.  We need to be able to deal with collisions. $h$ cannot possible be an injective function since the cardinality of our $w$ space is less than that of our $u$ space. 

The function that we choose to perform this hashing must be a very good hashing function that results in a relatively uniform distribution of our values over the hash set. If we end up putting all $n$ of our values at a single index, our hashing fails. 

From here, we have two possible ways to handle collisions.  We have open addressing, and chaining. Open addressing is difficult to analyze, but is more practical. 

#### Hash Functions
Hash functions provide us with a reliable way to 
##### Division/Modulus Hash Function
The easiest way to get from a large space to a small space is simply by using the modulus operator. This is known as the "Division Hash Function", and gives keys for some $k \in U$ by:
$$h(k)=k\text{ mod}(m)$$
Where $m$ is the size of our new array. Each key will be constrained only a small subset of our array. This is a good idea if our distribution of keys in the original set $U$ is relatively uniform. 

This is essentially how python performs its hash functions. 

##### Universal Hash Functions
There are many universal hash functions, this is just an example of one. We want to consider this also as a family of functions where we consider $a,b \in \{0,1,2,\cdots,p-1\}$. For the key, $k \in U$  Our hash function is thus:
$$h_{ab}(k)=((ak+b)\text{mod}(p))\text{mod}(m)$$
We can generalize this function to be given by $H(p,m)$ where $p$ is a prime number such that $p>u$:
$$H(p,m)= \{ h_{ab} | a,b \in \{0,1,\cdots,p-1 \} \}$$
We want to randomly select a hash function so we can get around the user feeding us data that will conflict with our hash function and result in something that is very hard to process. We want to enforce that our universal hash function will have a collision rate that is less than that of $\dfrac{1}{m}$, which entails that our distribution is sparse, and will not intersect with itself often. 

We can define an indicator random variable, $X_{ij}$, given some $h \in H$ by the following:
$$X_{ij}=1 \text{ if } h(k_{i})=h(k_{j})$$
$$X_{ij}=0 \text{ otherwise }$$
If our keys intersect, we get $1$ back from our function. Otherwise, we get $0$. How do we write a chain in this model? A size of a chain at $i$ in our hash table is:
$$\text{size of chain at } i = X_{i} =  \sum_{j=0}^{n-1}X_{ij}$$
We can compute the expected value of our size of chain random variable given we are choosing $h$ from our set of hash functions $H$:
$$\mathbb{E}\{ X_{i}\} = \mathbb{E}\left\{ \sum_{j=0} ^{n-1}X_{ij}\right\}= \sum_{j=0}^{n-1}\mathbb{E}\{ X_{ij} \}$$
We can re-write this expression since we are guaranteed to get $1$ when $i=j$:
$$= 1+\sum_{i\neq j}^{n-1}\mathbb{E}\{ X_{ij} \}$$
We know that each key has a $\dfrac{1}{m}$ chance to collide with another key. Therefore, we can write our sum lastly to get:
$$=1+\sum_{i\neq j}^{n-1}\mathbb{E}\left\{ \frac{1}{m} \right\}=1+\dfrac{n-1}{m}$$
Since our choice of $m$ is sufficiently nice such that we can get a comparable result, our expected value is constant, so it turns out that the lookup time in our simple chaining method is constant. 

If we have too many values and the ratio is no longer is constant, we need to rebuild or hash table, just like the dynamic array. 

#### Chaining 
At every position along our array, we associate the address of a linked list. If it happens that two keys get mapped to the same key value in $m$, we can grow each linked list along the array and adding both. Therefore, we avoid the error of having a unique element associated with each index.

In order to maintain a nice $\Theta(1)$ lookup and removal/insertion time, we want to make sure that each chain is relatively small. 

We should note that when initializing this type of structure, we run into a constant factor memory overhead.
![[Pasted image 20250707050114.png]]

We can conclude that our hash table has an $o(n)$ build size, and find min and find max function, since it doesn't have a lot of vacant slots in memory. 

| Data Structure      | Container        | Static          | Dynamic       | Order   | Order           |
| ------------------- | ---------------- | --------------- | ------------- | ------- | --------------- |
|                     | build(A)         | find(k)         | insert/delete | min/max | prev/next       |
| Array               | $n$              | $n$             | $n$           | $n$     | $n$             |
| Sorted Array        | $n\text{log}(n)$ | $\text{log}(n)$ | n             | $o(1)$  | $\text{log}(n)$ |
| Direct Access Array | n                | 1               | 1             | n       | n               |
| Hash Table          | n                | 1               | 1             | n       | n               |
