---
title: Sorting
tags: 
draft: "false"
---
# Sorting Introduction
The question of sorting asks us, given an array of arbitrary elements $X$, how do we take $X$ such that the array is sorted? We have two types of sorting to begin with. We have ${\color{red} \text{Destructive}}$ methods, which overwrite the original array and thus has additional memory overhead, and we have ${\color{red} \text{in place}}$ methods which operate on the same array itself which thus only incurs an $O(1)$ space cost. 

Let us examine some of the methods that allow us to sort our array. 

#### Permutation Sort 
Let us consider the unsorted array of $n$ elements, $X$. Permutation sort randomly shuffles the contents of our array until it is fully sorted:
```
def permutation_sort(A):
	for permutation in permutation(A):
		if is_sorted(permutation):
			return permutation
```
This should be intuitive since a sorted array is essentially just a [[permutation]] of the elements in our array that happens to satisfy our definition of sortedness. 

We need to be able to enumerate our permutations, of which there are $n!$. We know at least that our runtime will be $\Omega(n!)$. We also need to check that our permutations are sorted. 

We basically need to check that it is true that $x[i] \leq x[i+1]$  for every element in our array. 

This would give an overall runtime of $\Omega(n! \cdot n)$ at the lowest possible runtime. We use [[omega]] here instead of [[big o]], we know that omega is the lower bound on our runtime. 

This gives an example of an in place sorting algorithm. 
#### [[Selection Sort]]
Let us consider the array, $X=[8,2,4,9,3]$. The algorithm goes as follows. We will iterate from $0$ to a decrement bound that begins at the rightmost index and decrements each iteration. We select the highest number within our range, swap it with the end index, and keep repeating and repeating until we have selected all values.

Our inductive hypothesis would state that we would eventually get a sorted array for all arrays:
$$0.)\text{ } X=[8,2,4,9,3]$$
$$1.)\text{ } X=[8,2,4,3,9]$$
$$2.)\text{ } X=[3,2,4,8,9]$$
$$3.)\text{ } X=[3,2,4,8,9]$$
$$3.)\text{ } X=[2,3,4,8,9]$$
We can also solve this using recursion, where we keep feeding the function into itself by feeding the right bound into itself and decrement it, and swapping until the right bound is equal to 0, which gives the base case. 

This allows us to consider our runtime. If we have 1 element in total, then it follows that our array is sorted. Let us call our recursive function $S$. We can consider 1 run of $S$, where we do not look to sort the whole array, but simply perform 1 swap on it. Let us suppose we have $n$ many elements. Since it follows that:
$$S(1)=\Theta(1)$$
We can write the recurrence relation:
$$S(n)=S(n-1)+\Theta(1)$$
We suspect that our answer will take form of $n$, so we write our $S(n-1)$ as $c\cdot n$. This technique is known as [[substitution]]. We need to verify this works with our inductive solution, and then we can finish. 

Let us check:
$$cn=c(n-1) + \Theta(1)$$
$$0=-c + \Theta(1)$$
$$c=\Theta(1)$$
Since $c$ is a constant, we are fine. 

We can use this to express an overall relationship with our function. Let $T(n)$ be the runtime of our function. We can write our function recursively:
$$T(n)=T(n-1)-\Theta(1)$$
We hypothesize this is $O(n^2)$. Let substitute $T(n)=cn^2$:
$$cn^2 = c(n-1)^2+\Theta(n)=cn^2$$
$$\Theta(n)=2cn + c$$
---
#### [[Insertion Sort]] 
Insertion Sort is another algorithm that runs in $O(n^2)$ time, and is generally not very useful or efficient. Insertion sort functions pretty similarly to selection sort, but we begin with a "sorted" portion at some index, and look for the smallest value and then find the position to insert the value at as we iterate through the array:
![[Pasted image 20250704233954.png]]

---
#### Merge Sort 
If we think of single numbers alone, we can consider each number to be sorted. If we have two numbers, we can group them easily, and then sort which is larger simply by moving one to the left or right
![[Pasted image 20250704234529.png]]
We need to have a step where we take things that are larger than 2 blocks and put them together. It turns out that we have a trick for this that runs in linear time. The lecturer calls this "the 2 finger trick"

Basically, if we align two already sorted lists of numbers, we can process the entire list in constant time simply by iterating over them with two pointers, one on the top and one the bottom:
$$1,5,6,7 \leftarrow$$
$$2,3,4,9 \leftarrow$$
We compare which is the largest entry, and we insert it into our array. We then decrement the pointer along the array that had the largest entry, and compare it. After the first comparison we would get:
$$1,5,6,7 \leftarrow$$
$$2,3,4 \leftarrow  $$
$$\text{new}=[9]$$
Now we would compare $7$ and $4$ and clearly see that $7$ is larger, which would give:
$$1,5,6 \leftarrow$$$$2,3,4 \leftarrow  $$$$\text{new}=[7,9]$$
If we are partitioning our array into pieces of 2, we would be performing a binary operation, and then we perform $\text{log}(n)$ many $o(n)$ time operations to stitch back our matrix together and to get it fully sorted. 

We can describe our algorithm by continually partitioning our array, and then getting to the point where we hit the base case of 1 or 2 elements, which can easily be sorted, and then performing a merge on the elements using the 2 finger algorithm. 

#### Formalizing the Algorithm

For the array $A$ of $n$ elements, we take the position $\dfrac{n}{2}$, and call it $c$. We sort the indices on the left side from $0,\dfrac{n}{2}$ and then on the right side from $\dfrac{n}{2},n-1$. After that, we call our merge function.  

We can write this as:
```
def merge_sort(arr,start,end):
	if end-start > 1:
		pivot = (start+end)//2
		merge_sort(arr,start,pivot)
		merge_sort(arr,pivot,end)
		L,R=A[start:pivot],A[pivot:end]
		merge(L,R,A,a,b)
	
```
Our merge function, $S(n)$ we can express with the following recursive relation:
$$S(n)=S(n-1)+\Theta(1)$$
Which we showed earlier is clearly just $O(n)$.

Our time function for the merge sort function is $T(n)$. We can write out recursive relation in the following. We partition our array twice, and  run merge sort on the two halves, and then have to merge them together. So, this results in the following recursive definition of $T(n)$:
$$T(n)=2T\left(\dfrac{2}{n}\right)+\Theta(n)$$
Our intuition would have us believe that $T(n)=\Theta(n\text{log}(n))$. We can write this out in the following:
$$c\text{log}(n)\cdot n = 2 \cdot c\text{log}\left(\frac{n}{2}\right)\cdot \dfrac{n}{2}+\Theta(n)$$
$$c\text{log}(n)\cdot n =  c\text{log}\left(\frac{n}{2}\right)n+\Theta(n)$$
Which if we use some basic identities allows us to obtain:
$$\Theta(n)=c n \text{log}(2)$$
Which is consistent and gives us our proper runtime. 