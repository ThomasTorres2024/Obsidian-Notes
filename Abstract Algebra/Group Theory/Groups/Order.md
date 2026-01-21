---
title: Order
tags:
draft:
---
# Order of a [[Group]]
The [[Order]] of a [[Group]] is is called its order. The [[Order]] of a group is denoted by $|G|$. A group may have either finite or infinitely many elements. 

The group $\mathbb{Z}$ has infinitely elements, whereas $U(10)=\{1,3,7,9 \}$ has 4 elements. 

---
# Order of an Element 
The [[Order]] of an element $g \in G$ , is the smallest positive integer $n$ such that $g^n=e$. If this characteristic cannot be satisfied, for some $n$, then we say that $n=\infty$, which means that that element has an infinite [[Order]]. 

We denote an element's order by $|g|$ or $O(g)$. 

---
# Example 1.) $U(15)=\{1,2,4,7,8,11,13,14 \}$ with multiplication $\mod(15)$. 
First observe that $|U(15)|=8$. 

We can compute $O(7)$ by performing repeated multiplication mod 15:
$$7^1=7$$
$$7^2=49 \mod(15)=4$$
$$7^3=4\cdot 7 = 13$$
$$7 \cdot 13=1$$
It took $7^4=1$, which is our identity element $\therefore O(7)=4$. 