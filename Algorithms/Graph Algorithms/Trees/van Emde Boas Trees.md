---
title: van Emde Boas Trees
tags: 
draft: "false"
---
# van Emde Boas Trees
An old data structure invented in the seventies that has taken a lot of time to understand and use in useful ways. 

van Emde Boas Trees are similar to [[Binary Search Tree]]s, and perform a similar function, but they are quicker, and they are not built off of the [[Comparisons]] model but instead using the [[Word-Ram Model]]. 

We want to maintain a set of $n$ elements which are non-negative except for:
$$\text{maintain set} = \{0,1,2,\cdots,u-1 \}$$
We can maintain a set with negative entries with small modifications as well. 

We want to maintain the operations of:
* Insertion
* Deletion
* Successor 

[[AVL Tree]]s and [[Red Black Tree]]s allow us to perform these operations in $\text{log}(n)$ time, but [[van Emde Boas Trees]] can allow us to perform this operation in $\text{log}(\text{log}(u))$ time. Typically, $u<2^{32}$, so $\text{log}(\text{log}(u))$ is rather small, and actually quicker than $\text{log}(n)$. 

A common way we might be able to get a $\text{log}(\text{log}(u))$ is by taking a tree with a height of $\text{log}(u)$ and then to perform some kind of [[Binary Search]] or partition on it. Intuitively we are "binary searching on levels of a tree."

In the standard recursive case for an [[AVL Tree]] we have the following recurrence relation for our operation runtimes:
$$T(k)=T \left(\frac{k}{2} \right)+O(1) = O(\text{log}(k))$$
Here, $k=\text{log}(u)$. We want our recurrence to look like this:
$$T(\text{log}(u))=T \left(\frac{\text{log}(u)}{2} \right)+O(1) = O(\text{log}(\text{log}(u)))$$
We will take the square root of the number of things we are working with, and then continually process the square root of the items over and over, which results in this runtime. 

---
# Bit Vector for Constant time Delete and Insert Operations

We can index an array to support insert and delete operations in $O(1)$ by initiating an array of size $U$, which we call a [[Bit Vector]]. A 0 in the bit vector indicates that an item is not in our set, and a 1 indicates that an item is in our set. 

A successor query may be of $O(u)$ time, and the only thing we can do is continue probing until we get to a 1, which may take awhile, however this is our starting point. Our algorithm starts by partitioning segments within our array as a "cluster" or a "galaxy". 

We want to be able to accelerate our successor search. At each set of indices, we could form some kind of tree where we keep taking an "or" of each of the two indices:

![[Pasted image 20250810043717.png]]

The value at the head of each tree is responsible for the [[summary vector]], which tells us if there is anything at each segment of our array. We check to see if anything is within the segment to start, and then we continually access each cluster with items and check to find the first item within it in order to find our successor. 

We want to split our clusters into sizes of $\sqrt{u}$ each since we want to have a recursion of $O(\sqrt{u})$ involved. When it comes to our insert operation, if we have a 0 in our [[summary vector]] for the cluster's head, we set it to 1. Insert is still an $O(1)$ computation. 

When finding our successor to $x$, we have a few options. One, we can spend $O(\sqrt{u})$ time looking for a successor in $x$'s cluster, that or we proceed to the next cluster with a $1$ in the summary vector (which also takes $O(\sqrt{u})$ time to find), and then we look through the next cluster for the successor, which will lastly take $O(\sqrt{u})$. 

Our total runtime is $O(\sqrt{u})$, which is a considerable improvement on $O(u)$, but we can still do better to get our double log of $u$. 

---
# Representation of an Integer as High and Low Parts 

We want to express the number $x$ in terms of $\sqrt{u}$, given by:
$$x=i\sqrt{u}+j:0 < j < \sqrt{u}$$
$i$ is the cluster number, and $j$ is the position within our cluster. 
![[Pasted image 20250810052054.png]]
For instance $9$ here is representable as $9=2\cdot 4 +1$, which tells us that $i=2$ meaning we are in the 2nd cluster, and that we are in position 1 of the cluster. 

From this we get the following:
$$\text{high}(x)= \left\lfloor \frac{x}{\sqrt{u}} \right\rfloor$$
$$\text{low}(x)= x \text{ mod}(\sqrt{u})$$
This is enough to give us the index of our item, which be at:
$$\text{index}(i,j)=i\sqrt{u}+j$$

We can see where these numbers come from if we look at the binary representation of 9. If we were to look at the binary representation of 9 we see that:
$$9=1001_{\text{ base } 2}$$
I'm not really sure why, but this has something to do with this? We somehow cut out the middle bits and bitshift them over and really consider that. Personally, I see the interpretation of us finding the cluster and then finding the index within the cluster way more useful. 

---
# Recursive Part
Let us consider the entire van Emde Boas structure we want to represent, and denote it $V$. We want $V$ to consist of an array of all of our clusters, and a [[summary vector]] 

* $\text{V.cluster}[i]$  An array of all clusters, where each cluster is of size $\sqrt{u}$ with indices from $[0,\sqrt{u}-1]$, and the total array structure that encapsulated it which is of size $u$
* $\text{V.summary}$ again of size $\sqrt{u}$ with the same indices as a cluster above 

Let us consider the operations of Insert and Summary. 

If we want to perform, $\text{insert}(V,x)$ where $x$ is a number that we want to put into its according cluster. We want to insert into the cluster of $\text{high}(x)$, and then insert it at the $\text{low}(x)$ position in the cluster:
$$\text{Insert}(V.cluster[\text{high}(x)]).\text{low}(x)$$
We also want to insert into the index of our [[summary vector]] at $\text{high}(x)$ to maintain our summary structure as well. If we consider the successor structure 

Let us now consider the Successor function of $V$ for $x$:
$$\text{Sucessor}(V,x)$$
We let $i=\text{high}(x)$ and $j=\text{Successor}(V.cluster[i],\text{low}(x))$

We check to see if the successor to this number is in this cluster, if it is not, then we find the next non-empty cluster using the successor of the [[summary vector]] to get the successor of $i$, which will eventually get us the smallest number in the next non-empty cluster:

```
i=high(x)
j=V.successor(V.clusters[i],low(x))

if j == infty:
	i = successor(V.summary[i])
	j = successor(V.cluster[i],-infty)

return index(i,j)

```
This is not optimal, but is still $O(\sqrt{U})$, because we make a recursive call more than once, potentially multiple times. To get our desired log log $u$ call, we need only a single recursive call instead of multiple. 

We want to be able to get rid of our other recursive calls under if $j$ is infinite. One way we could do this in constant time is to keep track of what the minimum is in each cluster.  

This would be enough to get us the call for: ``` j = successor(V.cluster[i],-infty)```. We need another way to get rid of ```i = successor(V.summary[i])```. Another way we can get around this additional call is by storing the max, which allows us to avoid the call to scan within the cluster since we can already verify if our current cluster will have other values. If no such values are in there, we can go on to find the successor of our summary vector at $i$, and we can just get the minimum from that. 

We can re-write our successor function as:

```
i=high(x)

#if this check is true we are guaranteed a successor in our substructure 
if(low[x]<V.cluster[i].max):
	j = successor(V.cluster[i].low(x))
else:
	i=successor(V.summary[high(x)])
	j = V.cluster[i].minx

return index(i,j)
```

If we are left of the max we look for it within our cluster, and if we are right of it we immediately go to the next cluster and get the min there. In the recurrence relation of our problem we would get a single recursive call, which would (somehow?) give us a runtime of:
$$O(\text{log}(\text{log}(u)))$$
We could also make insert a log log $u$ operation. The first time that we insert into a cluster, it turns out that our operation is a bit expensive, since we need to update the summary vector that corresponds to the cluster at our point. 

We need to make sure that we are not storing our min and max recursively, and when inserting into a blank cluster, we set the max and min automatically to be the same as the inserted value, so this makes our runtime less costly. 

We also need to insert into the summary structure, meaning that we need to insert into the [[summary vector]] and give it a $1$ if it has no yet been initialized, the way we go about this is by checking if it is 1 or not. 

We also need to insert function to perform in $O(\text{log}(\text{log}(u)))$ time. We can achieve this by forcing a recursive call to our insert function to occur only once instead of twice. Our basic current code (ignoring setting maxes and mins when we have nothing here) for insert is the following:

```
Insert(V,x):
	Insert(V.cluster[high(X)].low(x))
	Insert(V.summary,high(x))
```

If we have that our cluster is empty, we set our min and max and then we stop, we do not actually add it to our cluster. We then set our successor for the cluster in the [[summary vector]] to have a value corresponding to our index. We can detect if our cluster is empty if its min value is none. Our refactored code looks like:

```
Insert(V,x):
	if V.min == None:
		V.min=V.max=x
		return 

	if x < V.min: swap(x,V.min)
	if x > V.max : V.max=x

	#check if empty, if not empty then we need to make summary contain values 
	if V.cluster[high(x)].min==None:
		Insert(V.summary,high(x))

	#insert value regardless 
	Insert(V.cluster[high(x)],low(x))
```
If we have to make our [[summary vector]] report a value for this segment of the tree, we can add a 1 to the corresponding position of said vector, and then the recursive call on the bottom simply sets the constant time check if min is none. 

In both cases again, just like with the successor function, we make a single call, so this leaves our recursive formula with the solution of $O(\text{log}(\text{log}(u)))$. 

This finally gives us our notion of [[van Emde Boas Trees]] at the end. 

---
# Delete Function

Deleting the min is a bit special since min is special. 

```
Delete(V,x):

	#special case for min, we want this to be constant time and to be the last thing in our 
	#cluster  
	if x==V.min:
		i = V.summary.min
		if i == None:
			V.min = V.max = None
			return 
		x = V.min = index(V.cluster[i].min)
	
	Delete(V.cluster[high(x)].low(x))

	#if our min is empty, that means everything else in our cluster is empty, so we did that in O(1) time and we don't need to worry, so all we have to do is 
	if V.cluster[high(x)].min == None:
		Delete(V.summary,high(x))

	if x=V.max:
		if V.summary.max == None:
			V.max=V.min
		else:
			i = V.summary.max 
			V.max = index(i,V.cluster[i].max)
```

For the min case we need to recursively delete the min, and for the max case we need to delete the max element and find the next one in our vEB Tree. 

---
# Complexity 
The lower bound on all of our operations turn out to be $\Omega(\text{log}(\text{log}(u)))$, and holds for $u$ within the specified bounds of  $u$, and also space complexity for our structure. It turns out that we have this runtime if:$$u=n^{\text{log(n)}}$$ And we have a space complexity of:
$$O(u)$$
This is an issue since it isn't in terms of $n$. It turns out that our space complexity in terms of $n$, with some modifications to our data structure, is about:
$$O(n \text{log}(\text{log}(u)))$$
We want to only store the non-empty clusters, which gets us to close linear space of $n$. We can turn our $V.cluster$ into an array, which helps us a lot here in storing our total space.

There is a fix that allows us to further reduce our space to $O(n)$ mentioned in the lecture. I'm not really sure what it's saying and what to do with it, but it's apparently an option that allows us to remove the additional log log term. 