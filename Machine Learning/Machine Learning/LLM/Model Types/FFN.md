---
title: Feed Forward Neural Network
tags:
  - LLMs
  - Machine_Learning
draft: "False"
---
# Feed Forward Neural Networks

In a feed forward [[Neural Networks]], we take some vector $\vec{x}$, and then apply an [[activation function]], and then a bias after each layer in a neural network. 

A FFN is made of neurons that takes some inputs. Each input has a weight, and we feed these values into some [[activation function]]. Then we apply a bias, and feed it into either output layer. This is a very reduced view of a FNN but we do not have hidden layers:

![[Pasted image 20261025130241.png]]

We can describe these operations as:
$$\begin{align}
\hat{y}=f(x_{1},x_{2}) \\
\hat{y}=x_{1}w_{1}+x_{2}w_{2}+b
\end{align}$$
### Example

Say we have a two word sentence we want to classify as having either a positive or a negative sentiment. 

We would take our two input sentences say with $20,501$ words, feed it through an embedding layer of $20501 \times 1$, and obtain a $2 \times 1$ embedding layer. Once the embedding layer is obtained, we would then pass it in our model. 

$$[w_{1},w_{2}] \xrightarrow{\text{One Hot Encoding}} \begin{bmatrix}
w_{1} \text{ one hot} \\
w_{2} \text{ one hot}
\end{bmatrix}_{2 \times 20,501} \cdot W_{20,501 \times 1} = \text{Data Embedding}_{2 \times 1}  $$
If we were using the model as given above, we would simply feed the contents of the data embedding into the FFN since we have $2$ input parameters it matches the part above.

### Decision Boundary and Classification

With respect to each sentence provided, we could plot each $\hat{y}$. We could possible construct a [[decision boundary]] which separates the sentiment of the respective sentences. 

If our decision boundary is not linear, we could opt to use a different type of activation function, namely the [[Sigmoid]] function. 

We could also add additional layers onto our network (namely multiple neurons) with layers connected together 

### Configuring Activation Function and Model Parameters 

The more we can tweak our model the more advanced data are capable of rendering. If we have a [[linear]] [[activation function]], then we are guaranteed to have a linear decision boundary, which cannot generalize well to other problems.

If we use a non-linear activation function like a [[Sigmoid]] then we can develop a [[Logistic Regression]] model. This allows us to make a non-linear decision boundary.

However, if begin to chain multiple neurons together and connect them, the total complexity of the spaces we can develop significantly increases. With more neurons we can sovle the famous XOR problem. 

![[Pasted image 20261025131200.png]]

---
# Are feedforward Neural Networks enough for NLP?

Generally no. There are some significant drawbacks to using FFNs. A FFN can learn any continuous function via the Universal Approximation Theorem given the sigmoid activation function. The model he provided was rudimentary and only had a hidden layer, an input layer, and output layer. Overall training these parameters is extremely hard in practice but it __is possible__.  Let us examine some properties of FFNs. 

##### 1). What is the feed forward neural network doing on a fundamental mathematical level 

We are trying to approximate a function $f$ such that for any $x$, $f(x) \approx y$ 

##### 2). Are there any limits to what kind of functions we can learn with feed forward neural networks. 

It has been a known result that mathematically, a neural network can learn any such function $f$. Any [[continuous]] function can be approximated in the __Universal Approximation Theorem__. 

The architecture provided had the following constraints: 
* Activation function is a sigmoid
* 1 hidden layer
* 1 input layer
* 1 output layer 

##### 3). Why is any other model type/architecture necessary if FNNs can learn any type of continuous function? 

The UAT is an _existence_ proof guarantees that there is a one hidden layer model that exists which has a high accuracy, however the values of the weights, the biases, the number of neurons in the hidden layer are not given. We only know that such a model exists. In practice these values are __very difficult to find__ and are essentially only derived through experimentation. 

Importantly the details for such a model existing are not really given. 

---
##### Example FFN

$$\begin{bmatrix}
w_{1} \text{ one hot} \\
w_{2} \text{ one hot} \\
\dots \\
w_{100} \text{ one hot}
\end{bmatrix}_{100 \times 20,501} \cdot W_{20,501 \times 512} = \text{Embedding}_{100 \times 512} \xrightarrow{\text{Flatten}} \begin{bmatrix}
\boxed{x_{1}} \\
\boxed{x_{2}} \\
\vdots \\
\boxed{x_{51,200}}
\end{bmatrix} $$
Since the embedding vector has $51,200$ many features we need to flatten it for the input of a FFN. Say that we have $100$ neurons in the hidden layer. Then we will have $100$ weights for each input value, and one bias per neuron
$$\begin{bmatrix}
\boxed{x_{1}} \\
\boxed{x_{2}} \\
\vdots \\
\boxed{x_{51,200}}
\end{bmatrix} \to  \begin{matrix}
\boxed{f_{1}} \\
\boxed{f_{2}} \\
\vdots \\
\boxed{f_{100}}
\end{matrix} \xrightarrow{\text{Activation } \sigma } \hat{ y} $$
We have $5120100=51,200 \cdot 100 + 100$ many features. If our modle performs poorly at classification, say $0.5$ (maximum entropy) then we can augment the FFN by adding more parameters. If we add another neuron we have to add a weight from each of the $51,200$ inputs plus a bias. This means we then have $51,202$ more parameters in total. 

---
### Scaling
If we want to improve model performance we either add more layers or more neurons. 

In general if we have $n$ for an input size and $h$ neurons, we add $nh+1$ many parameters. This is a costly operation to do layer wise.

If we ad more layers then we have a design question. How many layers should we add, how many neurons should be per layer? it turns out there is no general answers here either, and it depends a lot more about the specific dataset we are working with. 


---

# Issues with Scaling FFNs for NLP

In general FFNs are difficult to optimize. 

For some FFn, in order to optimize the model, we could increase the number of neurons, or the number of hidden layers. If we have a large number of input values in our input layer, that connects to a single neuron, we need to add a new value to account for each. For $n$ input size, and $h$ is the number of hidden neurons, we generally have $n\cdot h$ values. 

If instead we were to __add more layers__, we would not really know what to do. Without information about the underlying data there is no proof or general design choice for what to do. For some linear data there are choices for how they should be approached but in the general, not really.  

FFNs run into vanishing [[Gradient]] issues as well. 