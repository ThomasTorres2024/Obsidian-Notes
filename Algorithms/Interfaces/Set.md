---
title: Sets
tags: 
draft: "false"
---
# Sets
A set is a type of interface, it is a collection of things. We can continue to add items to the set on end.  For instance, we could have a set of student IDs, which are nice because we can run [[Sorting]] algorithms on them.  

A set is a container. and it is equipped with the following operations:
```
build(A) | given an interable A, build sequence from items in A
len()    | return the number of stored items in A

find(k)  | determine if element k is in A

insert(x) | add key x, replace x if it already exists in A
delete(x) | delete key x from A
```
We want to be able to insert things into $A$, and we also want to know how many things it has.

For static operations on sets, we have the ability to search through the set in the find method.
We  want to be able to determine of some element $k \in A$. 

For Dynamic operations we have insert and delete because we would like to be able to remove elements from our set. 

We also have some operations related to order that we would like to find implementations for, that involve finding the minimum element, maximum element, the next largest or smallest element, and returning items in a one by one order. 

We want to find some concrete implementations of  sets 

---
# Implementations 
#### Unordered Array Implementation of a Set 
We could choose an array implementation of our set, where we store each of our elements $x_{1},x_{2},\cdots,x_{i}$ in an array arbitrarily, so we would get something like:
$$\text{set}=[x_{1},x_{2},x_{3},\cdots,x_{n}]$$
If we were to use this for our implementation, all we would need to do is search through each element of the list, which gives us an algorithm that operates on $O(n)$. This is a reasonable way to implement sets, but if we have high amounts of data, we want to find more clever ways to go about this.

If we want to be quicker, an array implementation is rather poor.

#### Ordered Array Implementation of a Set
Lets say we have ordered elements of a set, $a_{1},a_{2},\cdots,a_{n}$ we could have a much nicer implementation for finding maximum, minimum elements, and searching. 

We know that we can use binary search to find any element, so it gives us a nice $o(\text{log}(n))$ runtime using [[Sorting]] algorithms. 

| Data Structure | Container        | Static          | Dynamic       | Order   | Order           |
| -------------- | ---------------- | --------------- | ------------- | ------- | --------------- |
|                | build(A)         | find(k)         | insert/delete | min/max | prev/next       |
| Array          | $n$              | $n$             | $n$           | $n$     | $n$             |
| Sorted Array   | $n\text{log}(n)$ | $\text{log}(n)$ | n             | $o(1)$  | $\text{log}(n)$ |
