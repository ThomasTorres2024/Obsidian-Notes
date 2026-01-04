---
title: Stochastic Gradient Descent
tags:
draft: "false"
---
[[Stochastic Gradient Descent]] is a variation of the [[Gradient Descent]] algorithm which considers [[Batches]] of data compared to single vectors which are fed in and iterated over. As an aside, most modern day machine learning problems can be reduced to the following form, which is also known as finite sum problems in machine learning parlance:
$$\min_{x} \frac{1}{n } \sum_{i=1}^{n} f_{i}(x)$$If we allow $n \to \infty$, then we are  working with "Stochastic Optimization Problems" in Optimization theory. In machine learning, a common set up for this problem is as follows:

$$\text{Training Data: } \{ (x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{n},y_{n})  \} \in \mathbb{R}^{d}\times \gamma$$
In machine learning, both $d$ and $n$ are very large, where $d$ is the dimension of the data, and $n$ is the number of training/data points. This is what is meant by "large scale machine learning".  It turns out that [[Deep Neural Networks]] can be written using a finite sum problem:
$$\frac{1}{n} \sum_{i=1}^{n} \text{loss}(y_{i},h(x,a_{i})) = \frac{1}{n} \sum_{i=1} ^{n} f_{i}(x) $$
---
# Issues with Classical [[Gradient Descent]]
[[Gradient Descent]] in its classical formulation really struggles with massive $n$ and $d$. It is a very large sum, if our dataset is huge, it takes hours to days for this to possibly compute for a single step. 

The classical formulation for [[Gradient Descent]] is the iterative equation:
$$x_{k+1}=x_{k}-\eta_{k} \frac{1}{n} \sum_{i=1}^n \nabla f_{i}(x_{k})$$
In [[Stochastic Gradient Descent]], we instead opt to use the gradient computed at the point $i(k)$ where $i(k) \in \{1,2,3,\dots ,n\}$, and instead we perform the following update:
$$x_{k+1}=x_{k}-\eta_{k}\nabla f_{i}(k)x_{k}$$
The advantage of this idea is that we only need to compute a single gradient, instead of that of a massive sum. If we look at how the [[Stochastic Gradient Descent]] algorithm works, we see that with each iteration, the algorithm doesn't uniformly converge in distance, it has some random component, and oscillates up and down, but the overall behavior brings to a minimum.  The randomness of the algorithm makes it considerably more sensitive to different step sizes. 

As the step sizes gets larger, the overall convergence graph becomes a lot noisier. Another thing about the algorithm is that, fluctuation during the initial stages of the algorithm is a lot less than when the algorithm gets closer to the point. Once the algorithm gets closer to the point, we begin to diverge a lot more. We also are fine with using this descent method since it helps us avoid [[overfitting]]. We enter some kind of chaotic behavior or get stuck near the optimum. 

#### Mathematical Background Behind [[Stochastic Gradient Descent]] 
Why does this idea work mathematically? 

We can work through a basic optimization problem that can be solved analytically, consider the following equation where all values are scalars:
$$\min f(x)=\frac{1}{2} \sum_{i=1}^n(a_{i}x-b_{i})^2 $$
$$\nabla f(x)=0 \implies x^*=\frac{\sum_{i}a_{i}b_{i}}{\sum_{i}a_{i}^2}$$
This provides the full gradient to us. Instead, we can think of minimizing each component of the gradient. If we think of our function geometrically, we have a family of quadratics that we are trying to work with. 

We can find the value which minimizes each individual component:
$$\min f_{i}(x)=\frac{1}{2}(a_{i}x-b_{i})^{2} \text{ is } x_{i}^*=\frac{b_{i}}{a_{i}}$$
However, we can observe that $x^{*} \in  [\min_{i} x_{i}^{*},\max_{i} x_{i}^{*}]=R$. If we have some scalar that lies outside of this region $R$, we obtain the fact that a component of the true direction of the [[Gradient]] is a component of the vector and that by moving along that direction we would still be making some progress.  

Once we reach the "Region of Confusion", outside of the bounds of our gradient, we have significantly higher fluctuations. The behavior here isn't predictable, it isn't necessarily the case that our stochastic gradient will have any parts in common with the true gradient. 

In the realm of optimization, [[Stochastic Gradient Descent]] is a rather poor method because we fluctuate substantially and do not get a true minimum. But in the context of machine learning, we tend to get a nicer more robust model. 

---
# Key Mathematical Idea behind [[Stochastic Gradient Descent]] 
Suppose that we do not directly have access to $f(x)$ and $\nabla f(x)$ we only have noisy estimates of these instead. Any time we deal with a substantial amount of data, we should rely on randomization in order to speed up the process. The way we go about randomization to speed up our computations here is by using [[Stochastic Gradients]], $g(x)$ such that:
$$\mathbb{E}[g(x)]=\nabla f(x)$$
I am not really sure why this is supposed to work, but in statistics terms this is an "Unbiased Estimator", and furthermore, we have a manner to constrain the amount of fluctuations that occur by controlling [[variance]]. Our goal is to minimize the [[variance]], which in turn means that our [[Stochastic Gradients]] are better and better. 

We also want our speed of convergence to be pretty good for our algorithm, which we need to ensure as well. 

---
# Variants of [[Stochastic Gradient Descent]]:
When we introduce randomness into [[Gradient Descent]], we need to define our sense of randomness. We do this first by considering a version of [[Sample With Replacement]] and [[Sample Without Replacement]]. 
### Version 1.) of SGD [[Sample With Replacement]] 
* We begin with some feasible $x_{0}$
* For $k=0,1,\dots,$
	- Version 1 - Randomly pick an index $i$ with replacement
	- Use $g_{k}-\nabla f_{i}(x)$ as the stochastic gradient 
	- Update $x_{k+1}=x_{k}-\eta_{k}g_{k}$

### Version 2.) of SGD [[Sample Without Replacement]] 
* We begin with some feasible $x_{0}$
* For $k=0,1,\dots,$
	- Version 1 - Randomly pick an index $i$ without replacement
	- Use $g_{k}-\nabla f_{i}(x)$ as the stochastic gradient 
	- Update $x_{k+1}=x_{k}-\eta_{k}g_{k}$

In the real world, we tend to use the [[Sample Without Replacement]] because we want to optimize our GPU performance. If we need to [[Sample With Replacement]] each time, then we have to randomly select an item, which kills GPU performance, versus simply shuffling our items once off the rip and then iterating over each index of the shuffled items - which is much faster. 

The first version is used in analysis, and the second version for practice. 

### Using Mini-Batches 
In order to stabilize our [[Stochastic Gradients]], we consider a sample of points in a mini-batch instead of using the average of several randomly sampled batches of items within our dataset. We express our batch as $I_{k}$:
$$x_{k+1}=x_{k}-\frac{\eta_{k}}{|I_{k}|} \sum_{j \in I_{k}} \nabla f_{j(x_{k})}$$
We do not gain too much from using mini-batches per computation, but it is very important for GPU parallelization. Large mini-batches don't really help that much either. If we have more compute, we can handle larger batch sizes, but we start to look a lot more like [[Batch Gradient Descent]], which is good for optimization but poor for machine learning, since this decreases our region of uncertainty and causes us to overfit generally. 