---
title: Amortized Analysis
tags: 
draft: "false"
---
# Introduction
Amortized Analysis is interested in finding the total runtime of an algorithm, and less the run of each operation. We also believe that standard [[big o]] analysis, that is worst-case or average case, may be too pessimistic, so amortized helps us get a more realistic way to measure runtime of our algorithms. 

We have several ways to go about understanding amortization with four different methods:
1. Aggregate Method
2. Accounting Method
3. Charging Method
4. Potential Method

We will exemplify these analysis methods by looking at [[Hashing]] table doubling, binary counters, and [[2-3 Trees]]. 

---
# Example - Table Doubling 
If we store $n$ items in a [[Hashing]] table, using say hashing with chaining, then we have an expected cost of $O\left(1+\frac{m}{n}\right)$. 

If $n \to m$, then we would double m, so $m'=2m$, and we would need to copy everything within the table, which would take a total of $O(m)$ work since we are doing $2m$ operations. Typical worst case analysis would indicate that insertion would be of linear complexity. 

In total, we only would double our table $\text{log}(n)$ many times, so for inserting $n$ many objects our total runtime would look like:
$$\Theta\left( \sum_{i=1}^{\text{log}(n)}2^i \right)=\Theta(n)$$
Which entails that with $n$ insertions, we have $\Theta(n)$. If we think about the cost on average, we would see that our average cost per operation is $\Theta(1)$. 

This gives us an [[Amortized Analysis]] cost of $\Theta(1)$ for insertion into a hash table. This is an example of the "Aggregate Method".

---
# [[Aggregate Method]]
A method for determining the [[Amortized Analysis]] cost of performing $k$ operations. Loosely we can think of this as:

$$\text{aggregate method cost } =  \dfrac{\sum_{i=1}^k \text{ op cost} }{k}$$
This gives us our total amortized cost per operation. This is a simplified very flexible definition. When we mix in operations like delete, our sum isn't as clear, but for inserting $n$ elements strictly, it is a good enough tool

---
## (Definition) Amortized Bounds Operation
Given a sum of operations, we can assign a cost for each operation, which we will refer to as the "amortized cost", such that we will preserve the total sum of the operations involved:

$$\sum_{\text{op}} \text{amortized cost} \geq \sum_{\text{op}} \text{actual cost}$$
We always want our total cost to be either as big or bigger than the actual cost involved of our operations. Generally, we only really care about the sum of all of the operations after we have finished doing all of them. We are not interested in the individual or worst time, just what happens after we are finished with the whole. 

This definition is generally a lot more flexible. 

### (Example) [[2-3 Trees]] 
To construct an empty [[2-3 Trees]], it takes $O(1)$ time worst case. 

For insertion, our amortized cost is $O(\text{log}(n)^*)$, and for deletion we have an amortized cost of $\emptyset$.   We can think of deletion as being $\emptyset$ because we cannot delete more elements than we have inserted. 

If we wanted to consider the cost for a runtime of a [[2-3 Trees]], given the initialization of $c$ many trees, insertion of $i$ many nodes into them, and then $d$ many deletions where $d \leq i$ (since d cannot be) greater than $i$, then we would get the following:
$$O(c+i\text{log}(n)^*+d\text{log}(n)^*)=O(c+i\text{log}(n)^*+d\cdot0)$$
Hence we can treat $d$ as zero. We also have to note that our operations are not of constant size. Initially insertions are constant size, but then they shrink and grow with respect to how our data structure changes 

If we let our $n^*$ be the overall maximum cost of any such operation, then our analyses will still hold true since they provide an upper limit. 

---
# [[Accounting Method]]
Let us define a bank account, and an operation can store credit in the bank account. The bank account can never go negative, but our summation always must be $\geq 0$. Each operation costs some amount of money. 

We pay for operations using credit stored in the bank as long as our balance is non-negative. If we don't use the remaining balance, then we have a nice upper bound

We have an operation which we can use to pay for time using credit in our bank. We also have that our balance is always non-negative. 

#### Argument for [[2-3 Trees]] $O(\text{log}(n))$ Insertion and $\varnothing$ for deletion
We can reuse the [[2-3 Trees]] example above, and we can argue that insertions are still $O(\text{log}(n))$ while deletions are $\varnothing$ time complexity. Again, the root of arguing this is that we cannot delete more than we insert, so inserting $i$ items would result in at most $i$ deletions, meaning we do $O(2i\text{log}(n) = O(\text{log}(n)$ complexity.  

For each insertion, we put a coin worth $O(\text{log}(n))$. Deletions consume 1 coin. Therefore, the amortized cost of our operation is:
$$\text{amortized cost} = \text{actual cost + deposits - withdrawls}$$
#### Argument for [[Hashing]] $O(n)$ insertion 
When we insert an item in our table, we insert a coin of value $c=O(1)$. We start with an array of size 1, and add an item to it. The next insertion sees us double the table to size two, and then we remove the coin from the first value and move to the second slot. In order to perform the increase in size of our table, we use our coins used to insert previous items to expand the table for more items. 
1. $[X(o)]$
2. $[X,Y(o)]$ 

The next two insertions will cause our table to move to four slots, and then it will take on the following form:
$$[X,Y,W(o),Z(o)]$$
The next set of insertions will result in an array of size 8. Half of the items, 4, have coins, and 4 do not. When $n=m$, that is the number of items we have inserted is equal to the table size, then we have $\frac{n}{2}$ total coins. 

This results in an amortized cost given by:
$$ \text{amortized cost } =  \Theta(n)-c\dfrac{n}{2}$$ Our amortized cost turns out to be $0$ if $c$ is sufficiently large, around the size of $2.$ We still need to deposit and withdraw coins, which still operates in constant time, so overall it turns out that we have a constant time for insertion according to the [[Accounting Method]]. 

---
# [[Charging Method]]
Allow operations to charge cost retroactively to their past (?????????), we can only go to the past not the future. The cost we are deducting from the past is added back to the future. In total this gives us the following formula for our amortized cost:
$$\text{amortized cost = actual cost - total charge to past + total charge in future } $$

#### (Example) Table Doubling 
After we double our table, our table is half full. To get from half full to completely fully, we have to do $\frac{n}{2}$ insertions. We will say instead that the next time we double our array, we charge our doubling to the $\frac{n}{2}$ insertions we made:
![[Pasted image 20250812040837.png]]
Whenever we do a doubling operation, we charge inserts to the last series of doublings. In order to make our doubling free, we need to charge $\Theta(n)$. We have $\frac{n}{2}$ items, and we want to distribute our charge as $\Theta(1)$ to each item. We never double count, and we only insert once. 

Our amortized cost of doubling turns out to be none and insertion cost is constant time. 

#### (Example) Table Doubling and Halving
We want to maintain that our table always is within a factor of the number of items in our table. When the table is 100% full we double it. If the table is 25% full, we will half it (if we allow our fullness to be like 50% we run the risk of having to resize our table again). 

When we double our full array its half full. When we shrink a quarter array, it goes back to half full. So regardless of which we are using, we always get 50% back for our array size which is far from 100% to 25%. 

We consider a halving operations to have $\frac{m}{4}$ deletions since the last resize operation of either type. 
We consider doubling to be $\frac{m}{2}$ insertions our last resize. 

Halving costs $\Theta(m)$ time and doubling also costs $\Theta(m)$ time. We have $\Theta(m)$ operations to charge to, and we charge constant for each of the operations. We never charge an operation more than once. I really am not sure what's going on here in all honesty it doesn't seem to prove anything?

---
# [[Potential Method]]
Much like the [[Accounting Method]], we have a bank account with a balance. We need to define a potential function, $\phi$, we can think of it like potential energy, that maps data structure configuration to a non-negative integer. 

In accounting, we store our credit, our deltas, but with the potential function we use our function to compute the amount 

We can define our amortized cost as:
$$\text{amortized cost = actual cost + } \Delta \Phi$$
Where $\Delta \Phi = \Phi(\text{after op}) - \Phi(\text{before op})$ 

The main idea here is that our $\Phi$ will telescope as we add up all of its terms:
$$\sum \text{amortized costs} = \sum \text{actual costs} + \Phi(\text{end})- \Phi(\text{beginning})$$
We pay for $\Phi(\text{beginning})$ at beginning of time when no operations have occurred thus far. Our cost should be either $O(1)$ or $\varnothing$. We also need to make sure its non-negative. 

#### (Example) Binary Counter
Given a binary counter, like "0011010111" and we want to increment it by $1$ then, we get the following binary sequence, "0011011000". Many bits changed, but via amortization only a constant number of bits change. We can use the potential method here to work through this. 

The increment operation has a cost of 1 operation, and then the number of trailing ones $O(1 + \text{number of trailing 1s})$. Let us define $\Phi = \text{total number of 1 bits}$. 

The increment operation destroys $t$ 1 bits, and creates one. Our amortized cost is:
$$1+t-t+1=2$$
