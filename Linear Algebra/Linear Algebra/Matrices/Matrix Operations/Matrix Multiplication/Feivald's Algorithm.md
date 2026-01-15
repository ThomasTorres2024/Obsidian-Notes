---
title: Monte Carlo Matrix Multiplication Algorithm
tags: 
draft: "false"
---
# Introduction
We want to compute the matrix $C$ which is equal to the product of the matrices $A$ and $B$:
$$C=AB$$
The simple deterministic and algorithm that comes from the definition of our algorithm is an $O(n^3)$ algorithm. There's some slight different in-between adding and multiplication on computers, nowadays these computations are about equivalent. The same goes for the [[Karatsuba Algorithm]] for multiplication of integers, where we try and level out the number of multiplications in favor of addition. 

There is also the [[Strassen Matrix Multiplication Algorithm]], which allows us to multiple two $2 \times 2$ matrices with 7 multiplications instead of 8, which results in a nicer running time of: $O(n^{\text{log}_{2}(7)})$ which is about $\approx O(n^{2.81})$. We can go to $O(n^{2.71})$, and for multiplications for $70 \times 70$, we can further improve our result. 

The best complexity algorithm for [[Matrix Multiplication]] was the [[Coppersmith-Winograd]] which was about $O(n^{2.376})$. 

These deterministic algorithms are generally very bad, and have high constants associated with them, then we need an absolutely massive matrix we need to use, like a billion by billion matrix. 

Our verification algorithm should be considerably better than the above listed algorithms. Generally, we want a verification algorithm of  $O(n^2)$, and should principally beat the other solvers above.

If $C=AB$, then the probability that our output is correct should always be 1. 

If $C \neq AB$, then we can impose a lower bound that the probability we are outputting the correct answer as being less than or equal to half. 

Since our algorithm is $O(n^2)$, we can repeat it for some constant number of $k$ times, and in turn we will see the probability that we incorrectly output our result get halved each time. 

Our runtime, more precisely, is thus $k\cdot O(n^2)$. 

---
# Algorithm Description
The algorithm works for matrices of real valued entries, but it is much easier to prove over the field of $\text{mod}(2)$. Just to make this nicer to write out, I will write $\mathbb{F}=\text{mod}(2)$. Over the reals we would still be using the same time complexity since our arithmetic operations are constant time. 

#### (Definition) [[Frievald's Algorithm]]
A very straight forward algorithm, but it has the nice property that the error of misdiagnosing an incorrect multiplication is $\frac{1}{2}$. 

Let us consider a random binary vector, $r \in \mathbb{F}^n$.  Since we are working in binary, we can assume that $\mathbb{P}[r_{i}=1] \geq \frac{1}{2}$ independently for $i=1,\cdots,n$. 

Another implicit assumption we are making is that our two matrices, $A,B \in \mathbb{F}^{n \times n}$. 

Instead of outright computing $AB$, we want to consider the product of $A(Br)$ first, where we compute $Br$. Note however though that:
$$A(B\vec{r})=C\vec{r}$$If the two are equivalent, then we would output yes, otherwise output no. We have a total of three different matrix vector products here, since we need to compute $B\vec{r}$ and then $A\cdot(B\vec{r})$ and lastly $C\vec{r}$. 

If $AB=C$ then there are no false positives here. This property should come from associativity of matrix operations, that is to say that:
$$A(B\vec{r})=(AB)\vec{r}=C\vec{r}$$
Our $\vec{r}$ is random, so it is possible it might be a bad vector that doesn't reveal that there is a discrepancy between our end matrices. If we keep generating different $\vec{r}$, we want to analyze the correctness that $AB \neq C$ and see with what probability this happens. 

#### (Proof) Prove Correctness of $AB \neq C$
We claim that if $AB \neq C$, then we want to show that $\mathbb{P}[AB\vec{r}\neq C \vec{r}] \geq \frac{1}{2}$. 

For the purpose of analysis, we are not going to actually compute this, let:
$$D=AB-C$$
We want to discover the entries where $D \neq 0$. We need to show that over half of our vectors $\vec{r}$ show that $D \neq 0^{n \times n}$. Specifically we show that:
$$\mathbb{P}[D\vec{r} \neq 0] \geq \frac{1}{2}$$We want to examine when $\vec{r}$ is a bad vector and doesn't allow us to see that there is a discrepancy.  We want to show that for each bad vector there is a good one, which allows us to claim the above probability rule. 

Let us break this into cases. Consider the following case:
1. $D\vec{r}=0^{n \times n}$.  If $D=AB-C \neq 0 \implies \exists i,j$ such that $D_{ij} \neq 0$. Let us examine this entry, $D_{ij}$. Let us create a vector, $\vec{v}$ which is really $\vec{e}_{j}$. When we multiply these two things out we get, the matrix $D\vec{v}$. We will observe that in $(D\vec{v})_{j}$ that our entry is non-zero. 

	Let us take any $\vec{r}$ that can be chosen such that $D\vec{r}=0$. Let us then consider $\vec{r}'=\vec{r}+\vec{v}$. When we consider $D\vec{r}'$ we have that:
	$$D\vec{r}'=D(\vec{r}+\vec{v})=D\vec{v}\neq 0$$
	This is because $D\vec{v}$ isolated the $j$th column from $D$. We can show that $\vec{r}$ to $\vec{r}'$ is [[injective]]. Since $r'=r+v$, we know that our vector only differs by a single element at position $j$ effectively bitflipping it.  

	 For $D\vec{r}=0$, we can discover an $\vec{r}'$ such that $D\vec{r}' \neq 0$, and show that there is a 1 to 1 mapping between $r$ and $r'$.  The number of $D\vec{r} \neq 0 \geq$ the number of $r$ for which $D\vec{r}=0$. 

Due to our above argument, we can finally state that:
$$\mathbb{P}[D\vec{r} \neq 0] \geq \frac{1}{2}$$
If we continually run this for $k$ times, we can bring down our total probability that we are wrong to $2^{-k}$, which is very nice to work with for our verification algorithm. 