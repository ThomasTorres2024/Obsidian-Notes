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

The output in the next layer in the tridea