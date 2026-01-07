---
title: Gradient Descent
tags:
draft: "false"
---
# Gradient Descent 
Our intuition for this is to compute the gradient and take steps in the negative direction of the gradient such that each time we get closer and closer to a minimum along the graph, as eventually we expected to hit a 0. 

We can determine if the hessian matrix is PD or ND at $x^*$, if it is PD then it is a local minima, if it is ND it is a local maxima of the function, which corresponds respectively to positive and negative eigen values of $H$. 

This is an iterative method where each time we take some step forward each time. in t-SNE and other modern function we take iterative steps to optimizing our solution, which is a huge idea. Gradient descent is used to compute minima. We start at some random point along our surface, and then invert the gradients sign and follow that path down and continue. 

The hard part about this is the learning rate, which is critical. This is a [[hyperparameters]] of [[Machine Learning/Machine Learning/Algorithms/Optimization/Gradient Descent]]. This is known as the [[learning rate]], how many steps will we end up taking? 

We begin by letting $t=0$ and using an iterative formula with randomly initialized weights, $w$:
$$w^{(t+1)}=w^{(t)}-\nu \cdot \nabla_{w}f(w^T)$$
If the learning rate is too small then we have an overly slow convergence, step sizes are absolutely massive for the conjugate gradient method. If our size is too large, there is a good chance that we overshoot and end up going way too far. Overshooting with a neural net will produce absolute nonsense within a few epochs (traversals through the dataset). 

We have several other ways of improving upon the standard [[Machine Learning/Machine Learning/Algorithms/Optimization/Gradient Descent]] algorithm:
*  [[Stochastic Gradient Descent]]
* [[Stochastic Gradient Descent with Momentum]] 
	The idea is if I walked down here already and consider this and I have some momentum here I've been here already and moved this way, then our gradient would be affected by that. The intuition is to think of a ball falling down on a gradient, which has some momentum term wile it falls.
* [[Adam Optimizer]]
	Variation of SGD with Momentum. The adam optimizer is commonly used. Sometimes if SGD sucks, then we should use Adam. 
# [[Machine Learning/Machine Learning/Algorithms/Optimization/Gradient Descent]] and Machine Learning
Optimizing a [[loss functions]] is a huge problem in machine learning. We can't do it directly, so do it with this method iteratively. There are a lot of gradient based optimal solutions which can find by performing gradient descent. 

Using gradient descent runs into functions which are very complex with many saddle points, local maxxes, and local mins. Real data also causes rounding error and issues. Thus we are trying yo minimize over an unfriendly function. 

#### [[Batch Gradient Descent]] 
Instead of doing a gradient descent over the whole dataset, we do it by sampling the dataset, and taking a step based on that sample. The idea is we can do 1 epoch with many more gradient descents, instead of optimizing for one item. 