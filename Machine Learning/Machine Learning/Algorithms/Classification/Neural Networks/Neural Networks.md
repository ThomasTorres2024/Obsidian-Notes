---
title: Neural Networks
tags:
draft: "false"
---
# Intro to Neural Networks
Neural networks traditionally are used for [[Classification]]. We begin with a training set of the form:
$$\mathcal{D}=\{ x_{1},x_{2},\dots,x_{d} \} : x_{i} \in \mathbb{R}^m $$
Suppose we are doing [[Binary Classification]], therefore our neural net, $h(x) : \mathcal{D} \to \{-1,1 \}$ where each element corresponds to one of the two classes. We are interested in developing the function $h(x)$ using the training data such that we can accurately predict the outputs for some given $x$. 

We want to interpret the output of our $h(x)$ in the following way:
$$\begin{cases}
F(x) \geq 0 & \text{ when } -1 \\
F(x) <0 & \text{ when } +1
\end{cases}$$

We are not trying to find a full mapping, but instead a general mapping true for a majority of the cases. This is done because we do not want to [[overfitting]]. The most common [[activation function]] used in [[Neural Networks]] in the modern day is the [[Rectified Linear Unit]] function:
$$\text{Relu}(x)=\max(0,x)$$
![[Pasted image 20260104064143.png]]
A neural network consists of 3 layers, the architecture varies depending upon the task and what is optimal. The input layer consists of some vector $x \in \mathcal{D}$. It serves as the layer which contains our data. We then pass the data into the hidden layer(s), where a matrix vector product is performed in between the input layer and the hidden layer. 

We know that $x \in \mathbb{R}^m$, and let us say that the hidden layer is of size $h_{1}$. Then the matrix vector product must conform such that the weight matrix, $A$ yields:
$$A_{1}x \in \mathbb{R}^{h_{1}}$$
Therefore, $A \in \mathbb{R}^{h_{1} \times m}$. Once the value has been passed through to the hidden layer, we apply an [[activation function]], which allows our model to represent [[Non-linear Data]]. This is important because without the [[activation function]], our model is constrained to be a [[Linear Transformation]], and only useful for linear problems. 

Depending upon our architecture and the problem we are solving, we can introduce another hidden layer of size $h_{2}$, and we can choose another matrix $A_{2} \in \mathbb{R}^{h_{2} \times h_{1}}$
 such that the dimensions conform and we pass along information. 

The idea behind the neural net is that we are learning more and more information about the data at each level as we feed forward through the network. We may have a different [[activation function]] for the output layer, but the same idea takes hold of a matrix-vector operation followed by some non-linear [[activation function]]. 

We can express our neural network as a composition of functions in the following form:
$$\hat{y}=F(x)=h(A_{k}(h(A_{k-1}h(A_{k-2}h(\dots h(x))) ))$$
 More clearly, we have:
 $$y_{1}=h(A_{1}x)$$
 $$y_{2}=h(A_{2}y_{1})$$
 $$y_{3}=h(A_{{3}y_{2}})$$
What can be said about the neural network classifying function, $F(x)$? Well, it is a continuous function, as $h(x)$ is continuous, and we are composing it with the output of itself. The function is also piecewise linear, due to the [[Rectified Linear Unit]] function. 

This is a theoretically interesting statement since we want to create some $F(x) \approx X$ where $X$ is the [[Probability Distribution]] that generated $\mathcal{D}$, and so $h(x)$ and our [[Neural Networks]] need to be relatively robust at approximating these functions. It turns out since out using piecewise linear functions is a sufficient way to go about this task. 

---
# Training Neural Networks
How do we learn weights in a neural network? The intuitive way of handling [[Neural Networks]] is through [[Gradient Descent]] and calculating the gradient of our neural network function, $F(x)$, however this computation is very expensive, and thus we have the [[Backpropagation]] algorithm, which iteratively computes the [[loss functions]]'s loss at every stage of the network. 

Since our function if of the form:
$$F(x)=F(F(F\dots(F(X))))$$
The gradient quickly become complicated. 