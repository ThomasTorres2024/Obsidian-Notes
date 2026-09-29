---
title: Feed Forward Neural Network
tags:
  - LLMs
  - Machine_Learning
draft: "False"
---
# Feed Forward Neural Networks

In a feed forward [[Neural Networks]], we take some vector $\vec{x}$, and then apply an [[activation function]], and then a bias after each layer in a neural network. 

Say we have a two word sentence we wat to classify. We would take our two input sentences say with $20,501$ words, feed it through an embedding layer of $20501 \times 1$, and obtain a $2 \times 1$ embedding layer. Once the embedding layer is obtained, we would then pass it in our model. 

With respect to each sentence provided, we could plot each $\hat{y}$. We could possible construct a [[decision boundary]] which separates the sentiment of the respective sentences. 

If our decision boundary is not linear, we could opt to use a different type of activation function, namely the [[Sigmoid]] function. 

We could also add additional layers onto our network (namely multiple neurons) with layers connected together 

---
# Are feedforward Neural Networks enough for NLP?

### 1). What is the feed forward neural network doing on a fundamental mathematical level 

We are trying to approximate a function $f$ such that for any $x$, $f(x) \approx y$ 

### 2). Are there any limits to what kind of functions we can learn with feed forward neural networks. 

It has been a known result that mathematically, a neural network can learn any such function $f$. Any [[continuous]] function can be approximated in the __Universal Approximation Theorem__. 

The architecture provided had the following constraints: 
* Activation function is a sigmoid
* 1 hidden layer
* 1 input layer
* 1 output layer 

### 3). Why is any other model type/architecture necessary if FNNs can learn any type of continuous function? 

The UAT is an _existence_ proof guarantees that there is a one hidden layer model that exists which has a high accuracy, however the values of the weights, the biases, the number of neurons in the hidden layer are not given. We only know that such a model exists. 

Importantly the details for such a model existing are not really given. 

---
In general FFNs are difficult to optimize. 

For some FFn, in order to optimize the model, we could increase the number of neurons, or the number of hidden layers. If we have a large number of input values in our input layer, that connects to a single neuron, we need to add a new value to account for each. For $n$ input size, and $h$ is the number of hidden neurons, we generally have $n\cdot h$ values. 

If instead we were to __add more layers__, we would not really know what to do. Without information about the underlying data there is no proof or general design choice for what to do. For some linear data there are choices for how they should be approached but in the general, not really.  