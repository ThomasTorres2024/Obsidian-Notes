---
title: Learning Functions
draft: "False"
tags:
---
# Learning Function
The [[Learning Function]] is the function that is optimized during [[Optimization/Gradient Descent|Gradient Descent]] in [[Neural Networks]]. We can think of a [[Learning Function]] as some $F(x,v_{0})$ where $x$ consists of the weights, and $v$ consists of some sample feature vectors. $x$ consists of the bias vectors, $b_k$ and the matrices $A_k$, which are part of the linear aspect of forward propagation:
$$x=\{A_{1},A_{2},\dots,A_{l},b_{1},b_{2},\dots,b_{l} \}$$
The weights and biases are optimized during the training process in  [[Neural Networks]].

Using standard notation we obtain the following during forward propagation at some hidden layer, given the vector $v$:
$$z=A_kv+b_k$$
$$v=\text{Activation}(z)$$
Where the activation function is non-linear. Iteratively, on the next layer, we feed $v$ into the next layer and continue our propagation until we reach the final layer, the output layer. The output layer may have no bias, it also may have no activation function, The architecture varies. Oftentimes, $|x| > |v|$. We often have that $x$ is underdetermined because there are significantly more items in the set of $x$ than in the set of $v$ (I used cardinality syntax). 

For our $F(x,v_0)$, we are often looking for the $x$ such that we minimize some [[Loss Function]]: which is given by the following form. Let $y_{i}$ be the corresponding correct result for some $v_{i}$: 
$$L(x)=\frac{1}{n}\left[\sum_{i=1}^nF(x,v_{i}) -y_{i} \right]$$
Depending upon the [[Loss Function]] that we choose, we may compute the squares of the error if we are using [[Mean Squared Error]]. 
