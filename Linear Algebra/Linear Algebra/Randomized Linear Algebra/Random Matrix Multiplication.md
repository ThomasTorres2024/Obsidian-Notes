---
title: Random Matrix Multiplication
tags:
draft: "false"
---
# Introduction
When matrices become very large, we want to sample the columns and rows of a large matrix, $A$. Say we have large matrices $A$ and $B$ that we want to multiply together:

$$AB=\begin{bmatrix} \vec{a_{1}},\vec{a_{2}},\cdots\vec{a_{r}} \end{bmatrix}\cdot \begin{bmatrix} 
	\vec{b_{1}}^T\\
	\vdots\\
	\vec{b_{r}}^T\\
\end{bmatrix} = \sum_{i=1}^ra_{i}b_{i}^T$$
Our goal is to find a good approximation using the interpretation of [[Matrix Multiplication]] as a series of [[Outer Product]]s. We can approximate the matrix by first sample some of the rows, and then once we have a row, we have the column we need next. The way in which we sample the rows and columns is something we need to consider. 

We need to make sure that the resulting mean of our samples of $AB$ results in the matrix $AB$.  However, this doesn't account for the [[variance]], which is all over the place.  We then want to choose the probabilities:
$$\sum p_{j}=1$$
Such that these probabilities minimize the [[variance]], which is achieved by using [[Lagrange Multipliers]]. 

### Introductory Example
Say we have the matrix $[a, b]$, which has 2 columns. Both columns have an equal chance of being chosen. We are sampling twice. Each are weighted, and then we take an average of the samples. This is then our "Randomized Matrix" for each of the $s$ samples that we chose.

We have a couple ways of calculating the mean as well. Say we are finding the mean of the first sample, which is given by:
$$\mu=\sum\mathbb{P}_{j}[\text{Sample}]=\frac{1}{2}(a,0)+\frac{1}{2}(0,b)=\frac{1}{2}(a, b)$$
Then we can recover the matrix by multiplying by $s=2$ the number of samples, which recovers the matrix. 

For the variance recall that we are essentially tracking how far on average data points are from the mean to determine the spread of the data. 
$$ \sigma^2= \frac{1}{|X|}\sum_{x \in X} (x-\mu)^2$$
Here in the context of [[Random Matrix Multiplication]] we use the following formula for [[variance]]: 
$$ \sigma^2= \frac{1}{|X|} \sum_{x \in X} \mathbb{P}[x]\cdot (x-\mu)^2$$
For our example it turns out to be:
$$\sigma^2=\frac{1}{2}\left[(a,0)-\left(\frac{a}{2},\frac{b}{2}\right)\right]^2+\frac{1}{2}\left[(b,0)-\left(\frac{a}{2},\frac{b}{2}\right)\right]^2=\frac{1}{2}(a^2,b^2)$$
If it turns out that one of the elements is a lot larger than the other, then we should more heavily weight towards that item. Say if $b > a$, then we shouldn't do half and half for our probabilities. This brings us to [[Norm Squared Probability]]. If $b=2a$, then we should use a probability that our probability of picking $b$ is:
$$\mathbb{P}[B]=4\cdot \mathbb{P}[A]$$
Which is the intended conclusion of this section and algorithm. 

We also have another approach for computing the variance:
$$\sigma^2=\left(\sum_{x \in X} \mathbb{P}[x]^2\right)-\mu^2$$
---
# Overview of the Idea 
If we look at each column of our matrix, we can try and assign probabilities by setting weights as being higher when the norm is higher with the [[Norm Squared Probability]]. Another approach is mixing the columns, and track what we've done, and then operate on the mixed matrix. 

Here, we will let each $\mathbb{P}_{j}= \|a_{j}\|\cdot \|b^T\|$. Our goal is to have the probabilities  add up to one so we need to divide by the sum of the probabilities, which gives the formula:
$$\mathbb{P}(j)=\frac{\|a_{j}\|\cdot\|b_{j}^T\|}{C}=\frac{\|a_{j}\|\cdot\|b_{j}^T\|}{\sum_{i=1}^r \|a_{i}\|\cdot\|b_{i}^T\|}$$
Now we can actually approximate $AB$ using $s$ samples:
$$AB\approx \sum\mathbb{P}_{j}\cdot \frac{a_{j}b_{j}^T}{s\mathbb{P}_{j}}$$
If we take 1 sample, we can see that the mean of the sample will be equal to:
$$\frac{a_{j} b_{j}^T }{s}$$
And if we take all of these, it will turn out that that the $s$ should cancel, since we have sampled over all such outer products, which gives us the resulting matrix:
$$s\cdot \sum_{j=1}^r \frac{a_{j}b_{j}^T}{s}=\sum_{j=1}^ra_{j}b_{j}^T=AB$$
We can now use the formula for [[variance]] involving the mean on the exterior:
$$\sigma^2= \left(\sum_{j=1}^r \frac{\|a_{j}\|^2\|b_{j}^T \|^2}{s\mathbb{P}_{j}} \right)-\frac{1}{s}\|AB\|_{F}^2$$
Where the mean is taken using the Frobenius [[Matrix Norms]]. Notice however that:
$$\mathbb{P}_{j}=\frac{\|a_{j}\|\|b_{j}^T\|}{C} \implies \sigma^2=\left(C^2 -\|AB\|_{F}^2 \right)$$
This is a fixed number which is true given that we have successfully optimized our probabilities. Our goal here is to show that optimizing the probabilities results in:
$$C=\sum_{i=1}^r \|a_{i}\|\cdot\|b_{i}^T\|$$ We can begin by trying to optimize all of the values of $p_{k}$ by the constraint that:
$$\sum_{i=1}^r\mathbb{P}_{i}=1$$
Our objective function is to minimize:
$$f(j)= \frac{\|a_{j}\|^2 \|b_{j}^T\|^2}{\mathbb{P}_{j}}+\lambda \left( \left[\sum \mathbb{P}_{i} \right] -1 \right)$$
Where lambda is not an eigen-value, but instead is a scalar. Notice that the right hand side is actually equal to 0. We can now optimize this function by taking the partial derivatives with respect to each $P_{j}$: 

$$\frac{\partial f}{\partial P_{j}}=-\frac{\|a_{j}\|^2\|b_{j}^T\|^2}{\mathbb{P}_{j}^2}+\lambda=0$$
$$\iff \mathbb{P}_{j}^2 =\frac{\|a_{j}\|^2\|b_{j}^T\|^2}{\lambda} \iff \lambda = C$$
Before we do any sampling, we need to determine the probabilities, which turn out to minimize the variance we sample them based on the norms of the columns of our matrix. 