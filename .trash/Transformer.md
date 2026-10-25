---
title: Transformer
tags:
  - LLMs
  - Machine_Learning
draft: "False"
---
# Transformer

Transformers are optimal large language models that beat out [[FFN]]s which are difficult to optimize and have a lot of memory overhead. Secondly, CNNs have a much lower receptive field, which is necessary for textual analysis. 

---

A transformer is a type of model where we want a __receptive field__ (amount of information covered), which covers the entire document. For instance in [[Convolutional Neural Networks]], if something looks like an eye or nose, we are likely looking at a face, but for a transformer we need a more global sort of view. 

Let us consider the example sentence, "hello how are you". Let us perform a one hot encoding on each vector for a set of $512$ words, which gives vectors of the forms $512 \times 1$ (row vectors). 

We still want to involve the processes of a CNN in this particular model. Let's take a look at our data, we would get a matrix of size $5 \times 512$, and then our $3\times 3$ kernel and begin the [[Convolution]] process 

$$\begin{bmatrix}
\dots \text{ hello }\dots \\
 \dots \text{ there } \dots \\
\vdots \\
\dots \text{ you} \dots
\end{bmatrix}$$
We would only cover the first three words and the first three features associated with each word. This particular kernel size would not be very effective. If we wanted to cover the first three words and all of their respective features, we would use a kernel of the size $3 \times 512$, which covers the first $3$ words entirely, but not every word in the sentence. Recall that the process of [[Convolution]] here we are thinking of as a __similarity metric__, wherever we convolve it over and the corresponding output values are the highest, we would have the highest values. 

Another similarity measure that we could make use of is the [[Inner Product]]/[[Dot Product]]. If we wanted to measure the similarity of words in a sentence, we could do the inner product of each word, including the inner product of each word with itself. 

Consider the following sentence, we would need to take many inner products, for hello we would need to $\frac{n^2-n}{2}$ many dot products and we would obtain a [[Similarity Matrix]]. 

|       | hello   | there   | how     | are     | you     |
| ----- | ------- | ------- | ------- | ------- | ------- |
| hello | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| there | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| how   | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| are   | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| you   | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |

We refer to the similarity measure between words as __attention__. Under this methodology we are using the "__full receptive field__" since each word by each word has some value. Secondly, this is better than the initial kernel model with the extended windows for features since we examine the structure in its totality but it only took into account 4 words. 

---
If we have a transformer with embedding dimension $512$ and a document $100$ words, what does our input look like?

Recall that we do row wise storage of words. The document would be $100 \times 512$, meaning $100$ words, and then the respective embedding taking place in $512$ (note this cannot be [[One Hot Encoding]] as this would get each word entirely similar to itself and 0 everywhere else and thus be useless).

Consider now that we take our embedding matrix, $X \in \mathbb{R}^{100 \times 512}$ and multiply $X$ by its [[Transpose]] $X^T \in \mathbb{R}^{512 \times 100}$:

$$\begin{bmatrix}
\dots \text{ hello } \dots  \\
\dots \text{ how } \dots  \\  
\vdots \\
\dots \text{ you } \dots  \\ 
\end{bmatrix} \cdot \begin{bmatrix}
\vdots  & \vdots  & \vdots \\  \text{ hello } & \dots & \text{ you }  \\
  \vdots & \vdots & \vdots  \\
\end{bmatrix} = \begin{bmatrix}
\text{ sim(hello,hello) }  
\end{bmatrix} $$
This yields the [[Similarity Matrix]] where we find the similarity of each word with each word and itself. 

---
# What does the architecture look like? 
We have some input coming in, some $Q,K,V$ from the input, where the input is $x \in \mathbb{R}^{100 \times 512}$ (to reiterate $512$ is the [[Embedding]] dimension size). We have three associated weight matrices which are learnable:

$$W_{q} \in \mathbb{R}^{512 \times 512} ,W_{k},W_{v}$$
###### From which we can obtain:
$$\begin{align}
Q = X \cdot W_{q} \in \mathbb{R}^{100 \times 512}
\end{align}$$
How about if $W_{k}$ is a neural network with $512$ neurons:
$$K=X \cdot W_{k} \in \mathbb{R}^{100 \times 512}$$
Here we denote $I^{(n)}$ to be the identity matrix where $I^{(n)} \in \mathbb{R}^{n \times m}$ and that for $Y_{{m \times n}} \cdot I^{(n)}=Y_{{m \times n}}$. 

Let us define another matrix here, $A$, the __Attention__ as:
$$A=Q \times K^T = (X \times W_{q}) \times K^T = (X \times W_{q}) \times (X \times W_{k})^T $$
If $W_{q},W_{k}$ are identity matrices then we would get the following:
$$A=(X \times I^{(n)}) \times (X \times (I^{n}))^T = XX^T$$ Which again is the [[Similarity Matrix]]. 

There is also the $V$ in the transformer where $W_{v} \in \mathbb{R}^{512 \times 512}$, and we have:
$$V=X \times W_{v} \in \mathbb{R}^{100 \times 512}$$
$$\text{ out}=A \times V$$
The final output from our transformer out is $\text{out} = A \times V$. 

Our basic idea of the transformer is to repeat this computation in each layer of the transformer. 

A way we can think of $K,Q,V$ is that all of these are new feature representations of each word. Otherwise, if these were the identity we would get self attention for each word and every other word itself. When a transformer is trained the learnable parameters are $W_{k},W_{q},$ and $W_{v}$. 

We want to ask ourselves, what are we doing when we compute $Q,K?$ It turns out we are getting  __new feature representations for each of our words__. The same is true for $V$. 

---
### Example:
$$\begin{align}
x_{1} = \begin{bmatrix}
0.1 & 0.2 \\
0.3 & 0.4 \\
0.5 & 0.6 
\end{bmatrix} & \quad   x_{2} = \begin{bmatrix}
0.5 & 0.6 \\
0.3 & 0.4 \\
0.1 & 0.2 
\end{bmatrix} &  \quad W_{Q} = \begin{bmatrix}
0.1 & 0.7 \\
0.9 & 0.2
\end{bmatrix}
\end{align}$$

We want to be able to compute $Q_{1}=x_{1} \cdot W_{Q}$ and $Q_{2}=x_{2} \cdot W_{Q}$. Secondly, we want to notice the difference between $Q_1,Q_2$ Say that $x_1$ and $x_2$ respectively represent "man eats dog" and "dog eats man".  

$$Q_{1} = \begin{bmatrix}
0.19 & 0.11 \\
0.39 & 0.29 \\
0.59 & 0.47
\end{bmatrix} \quad Q_{2} = \begin{bmatrix}
0.59 & 0.47 \\
0.39 & 0.29 \\
0.19 & 0.11
\end{bmatrix}$$

Notice here that the representations for "man" (row 1 in first, 3rd in 2nd) are the same and the representation for "dog" is also the same (3rd in first and 1st in second).

This tells us that the $Q,K,V$ matrix computations the new feature representation of every word is __independent__ of the other words in the sentence. Words are only based on their own representations and the $W_Q$ matrix - we are not really getting any new information. 

If we keep repeating this operation down the network, we aren't actually creating any context between the words. 

### Problems:
###### Problem 1- Context matters. 
Ideally we want words to have __different__ representations when they are used. 

Sentence 1: I will run the race.
Sentence 2: Can you run this idea by the boss?

###### Problem 2 - Order Matters.
Order Matters. Dog eats man and man eats do do not mean the same thing.

It turns out we can check word similarity and develop context through [[Attention (Transformers)]], which is just the computation of $QK^T$. 

---
Now that attention has been computed, we have a single field left, namely "Out". 

$$\text{out}=A \cdot V$$
What do we want from this computation? $Q,K,V$ each individually work on words. We want our output to be a new feature representation of each word which takes into account the other words in the sentence, that is to say that they take into account the context of the words being used.

Namely we are interested in getting __a context sensitive representation of each word__. 

When we do $AV$ we get some amount of context associated with each word. Recall here that:

$$X \times W_{V} = V$$

Now let's examine the computation $A \cdot V$ where $A \in \mathbb{R}^{5 \times 5}$ and $V \in \mathbb{R}^{5 \times 512}$. 

$$\begin{bmatrix}
 \begin{array}{c|ccccc} & \text{hello} & \text{there} & \text{how} & \text{are} & \text{you} \\ \hline \text{hello} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{there} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{how} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{are} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{you} & \cdots & \cdots & \cdots & \cdots & \cdots \end{array}  
\end{bmatrix} \cdot  \begin{bmatrix}
\vec{v_{1}} \\
\vec{v_{2}} \\ 
\vec{v_{3}} \\ 
\vec{v_{4}} \\ 
\vec{v_{5}} \\
\end{bmatrix} = $$

Here each $v_{i} \in \mathbb{R}^{512}$. Let's take a look at the output computation, the first entry, we would take the first row of attention, $\vec{a_{1}}$ and take its inner product with the first column of $V$. 

![[Pasted image 20260929211140.png]]

Each column of $V$ corresponds to the feature representation of some word. The row vector is the attention score of hello with every word. The column is the feature representation V of different words. The dark blue $2$ comes from "there", likewise the dark blue $3$ comes from "how", the 4th from are, and the 5th you. 

![[Pasted image 20260929211743.png]]

Through this model we can mix information from the first word in the sentence with other words in the sentence. 

The first new feature value for hello is a representation which depends on two main things. The fircdotst thing it depends on is the __weighting__ factor that comes from the Attention Matrix. 

The second thing is that the __original first $V$ feature of the words__, there, how, are, and you. Each of these features is multiplied by a weighting factor that comes from the attention matrix. 

Likewise the entry $(A \times V)_{12}$ will be the inner product of the first row of $A$ by the 2nd column in $V$. 

Once we compute this for all column vectors of $V$ we eventually get a __context__ representation of the word hello for the first row of $A \times V$. 

We can continue this process for the second row, we then obtain a representation for "there" with respect to the context of the other words and so on.

---
# The Problem of Scaling

When it comes to scaling, we need to consider the [[Softmax]] function. When we finish computing the attention, we need to be able to normalize the values in attention in order to get a relative score of everything. 

The softmax function is given in the following:

$$\text{Softmax}(x_{i})= \frac{e^{(x_{j})}}{\sum_{j=1}^K e^{(x_{j})}}$$
$x_{i}$ is the output of the $i$th neuron in the layer. So here it would be the particular attention score we are working with. $x_{j}$ is a sum of all of the neurons outputs together, so a sum of the attention scores. Here, we apply [[Softmax]] row wise to the [[Attention (Transformers)]]. 

---
# Positional Encoding 

In the two sentences "man eats dog" and "dog eats man" the two sentences still appear as the same. We want the order of the two words to matter __before__ we do any computation in the transformer. 

The solution to making word order matter is __Positional Encoding__. The idea of this is to add a unique vector based on position to each of our words. In our example we have three words, so we need three vectors:

$$\begin{align}
PE_{1} =\begin{bmatrix}
0 & 0
\end{bmatrix} \\
PE_{2} =\begin{bmatrix}
0 & 1
\end{bmatrix} \\
PE_{3} =\begin{bmatrix}
1 & 0
\end{bmatrix}
\end{align}$$

Let us suppose that the embeddings of our words were the following:

$$\begin{align}
\text{man} \to [0.1 \quad 0.2] + [0 \quad 0] = [0.1 \quad 0.2]  \\
\text{eats} \to [0.3 \quad 0.4] + [0 \quad 1] = [0.3 \quad 1.4]  \\
\text{dog} \to [0.5 \quad 0.6] + [1 \quad 0] = [1.5 \quad 0.6] 
\end{align}
$$

Now if we compare this to the compositional encoding involving the sentence "dog eats man" we obtain: 

$$\begin{align}
\text{man} \to [0.5 \quad 0.6] + [0 \quad 0] = [0.5 \quad 0.6]  \\
\text{eats} \to [0.3 \quad 0.4] + [0 \quad 1] = [0.3 \quad 1.4]  \\
\text{dog} \to [0.1 \quad 0.2] + [1 \quad 0] = [1.1 \quad 0.2] 
\end{align}
$$
Under positional encoding, we can enforce that the two sentences are distinct now even before hitting the architecture. 

Originally, the paper which developed this coding scheme did __not make use of binary__ but instead a [[Fourier Transform]] to embed the values sinusoidally:

$$p_{t} = \begin{bmatrix}
\sin(\omega_{0t}) & \cos(\omega_{0t}) & \sin(\omega_{1t}) & \cos(\omega_{1t}  ) & \dots & \sin\left( \omega_{\frac{d}{2}-1}t \right) & \cos\left( \omega_{\frac{d}{2}-1}t \right) 
\end{bmatrix}^T$$
Where $t$ denotes the position of the word and $d$ denotes the embedding dimension. And $\omega_{k}= \frac{1}{10000^{2k/d}}$.  

For example, say we want to encode a very simple sentence:

$$\begin{bmatrix}
0.1 & 0.2 & 0.3 & 0.4
\end{bmatrix}$$
Here $d=4$ the dimension, and $t=0$ for the word "man". We can compute $\omega _{0}= \frac{1}{10000^{(2\cdot 0)/2}} = 1$. For $k=1$ we get $\frac{1}{10000}$. Now we just compute some values:

$$p_{t} = \begin{bmatrix} \sin(\omega_{0}t) \\
\cos(\omega_{0}t) \\
\sin(\omega_{1}t) \\
\cos(\omega_{1}t)
\end{bmatrix} \to p_{0} = \begin{bmatrix}
\sin(1 \cdot 0) \\
\sin(1 \cdot 0) \\
\sin(0.0001 \cdot 0) \\
\sin(0.0001 \cdot 0)
\end{bmatrix} \implies p_{0} = \begin{bmatrix}
0 \\ 1 \\ 0 \\ 1
\end{bmatrix}$$

Lastly we add this word to "man":

$$\begin{bmatrix}
0.1 \\
0.2  \\
0.3 \\
 0.4
\end{bmatrix} + \begin{bmatrix}
0  \\
1 \\
0 \\
1
\end{bmatrix} = \begin{bmatrix}
0.1 \\
1.2 \\
0.3 \\
1.4
\end{bmatrix} $$
How would this change if man was the third word? We would then recompute the positional encoding vector. 

Here, our input depends on the word order.

### Why do we use sinusoidal encoding compared to binary encoding? 

There are several things sinusoidal encoding has. We want the functions we are working with to be continuous. Word positions which are close to each other should have very similar representations, however just consider the numbers $7$ and $8$ which in binary are $0111$ and $1000$ respectively. There is a change of 4 numbers here. 

Furthermore, if we consider the [[Norm]] (L2) distance between vectors $7$ and $8$ using binary encoding we get $2$ whereas with sinusoidal encoding we get $\approx 0.96$. 

The position encoding function exhibits [[Linearity]] to some extent. Suppose we are position $a$, and we want to shift by some amount $b$. 

By sinusoidal encoding we can mathematically prove that $f(a+b)$ can be rewritten as:

$$f(a+b)=R(b)\cdot f(a)$$
Note that binary encoding __does not have this relationship__. Notice here that $R(b)$ and $f(a)$ are both single variable functions with respect to their own parameters. 

### Why do we need both the sine and the cosine functions? 

We want to maintain __uniform spacing__ between each of our position vectors. Technically this could also be accomplished if you used $\sin(x)$ and $\sin\left( x + \frac{\pi}{2} \right)$. 


### Why is the positional embedding not a set of learnable parameters? How can we make the positional embedding fixed?

In the original transformer paper, both the learnable and fixed positional embeddings were used. It was found that __using learnable embeddings did not make much of a difference in model performance__. 

---

# Layer Normalization

This addition does not solve any particular problem. All this does is generally improve model performance:

$$\hat{x_{i}} =\frac{x_{i}-\mu_{l}}{\sqrt{ \sigma_{l}^2 + \epsilon }} $$
The basic idea here is that this formula is applied to each layer $l$ and every entry in the resulting out from the layer. 

We compute the mean of all of the features and then the standard deviation. We normal each feature value by the mean and standard deviation next. $\epsilon$ here is a very small positive value added to ensure that the value in the denominator is non-zero in order to avoid divison by zero errors. 

---
# Skip Connections

When we train an NN, we keep feeding forward with our training data, use backpropagation algorithm during trainiing. 

Essentially we sent the error backwards through previous layers. The error is then used to update all of the trainable parameters of the network. 

### The Vanishing Gradient

Problem:

We want more layers in our [[Neural Networks]]. More layers means the network can learn more complex functions since we have more trainable parameters.

As our network gets deeper, the [[Gradient]] tends to vanish as we go from the output layer to the first layer. 

The soluution to this problem is the use of __skip connections__. These provide a way for us to build deep networks twith many layers (since we have a way for the error to be sent back). 

In a skip connection, when we go further, we add the input of $1$ layer to another layer in the future:

![[Pasted image 20260930022054.png]]