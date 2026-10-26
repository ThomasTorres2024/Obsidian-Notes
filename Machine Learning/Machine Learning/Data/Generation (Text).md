---
title: Generation (Text)
tags:
  - Machine_Learning
  - LLMs
  - Transformer
draft: "False"
---
# Text Generation

In generation we predict a word at a time. If we have inputs provided that are used in training, we can essentially do [[unsupervised]] learning. We can ask a model to predict the next word in the sentence. 

For some given sentence, "hello there how are you" as an input, how many $x$ and $y$ training examples can be constructed?

It turns out that we can construct for some sentence with $n$ words, we can produce $n-1$ training samples. 

---
# Procedure 
We use a number to word approach. We take the last row of a [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]], suppose that it has $1 \times 512$ for its dimensions. Secondly, we need a projection layer matrix $W_{512 \times 50,000}$ and obtain a vector similar to the [[One Hot Encoding]] vector from before:

$$\begin{align}
\underbrace{\begin{bmatrix}
\dots \dots \dots
\end{bmatrix}}_{\text{Embedding Vector}} \cdot \underbrace{W_{512 \times 50,000}}_{\text{Projection Layer}}
\end{align} = \text{Pseudo One Hot}_{1 \times 50,000}  \\
\longrightarrow  \text{Softmax}(\text{Pseudo One Hot}) \xrightarrow{\text{Take Max Val}} \text{Predicted Word}$$
Since we have some negative values and not properly scaled values we use the [[Softmax]] value in order to get a nice [[Probability]] distribution. This makes interpretation much easier to work with. 

### Putting Generation all Together:

$$\underbrace{X}_{\text{Input}} \to \underbrace{\begin{bmatrix}
Q \\
K \\
V
\end{bmatrix}}_{\text{Layer 1}} \to \dots \to \underbrace{\begin{bmatrix}
Q \\
K \\
V
\end{bmatrix}}_{\text{Layer }\ell } \to \begin{bmatrix}
\text{Latent} \\
\text{Repre.}
\end{bmatrix} \to \text{Proj. Layer} \to \text{Softmax} \xrightarrow{\text{Extract Max Val}} \text{Predicted Word }  $$
For simplicity we just have a simplified version of the transformer. 

#### Text Generation Underlying Idea

When we feed in the word in our input we __do not want to recover the same word__, we want a new word that is the most likely word from our previous word. So for instance, if we have "hello" we would expect there:

$$\underbrace{\text{Hello}}_{\text{Input}} \to \underbrace{\begin{bmatrix}
Q \\
K \\
V
\end{bmatrix}}_{\text{Layer 1}} \to \dots \to \underbrace{\begin{bmatrix}
Q \\
K \\
V
\end{bmatrix}}_{\text{Layer }\ell } \to \begin{bmatrix}
\text{Latent} \\
\text{Repre.}
\end{bmatrix} \to \text{Proj. Layer} \to \text{Softmax} \xrightarrow{\text{Extract Max Val}}  \underbrace{\text{There}}_{\text{Predicted}}  $$
If we zoom into the latent representation, we only extracting the last word. Let's let the example sentence in this example now be "Hello There How are you",  and we want to predict you from "are":

$$\begin{bmatrix}
\text{hello CONTEXT rep} \\
\text{there CONTEXT rep} \\
\text{how CONTEXT rep} \\
\text{are CONTEXT rep}
\end{bmatrix}_{4 \times 512} \xrightarrow{\text{Latent Representation}} \begin{bmatrix}
\text{are context rep}
\end{bmatrix}_{1 \times 512}$$

#### Summary of Process

- Mathematics of the conversion process is similar to text to numbers approach, but we essentially reverse it
- In generation our input is a set of words, and we want to predict the next 
- Output of the last row of the last layer is used to predict the next word. 

---
# Data Generation

For generation what do we need to train? We can predict one word at a time. If we have any input data it can __automatically be used for training without any additional labeling__. Even in the sentence "hello there how are you" we can get $4$ samples for this:

$$\begin{align}
\text{Hello} \to There \\
\text{Hello There} \to How  \\
\text{Hello There How} \to Are  \\
\text{Hello There How Are} \to You 
\end{align}$$
This means generally for $n$ words we can produce $n-1$ training samples in total.

---
# What is the issue in text generation?

A model generally has a lot of redundant inputs. We want some way to speed up a forward pass. For instance in "hello there how are you", regardless of what we feed a [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]], the representation of hello there, hello there how, and so forth will all represent hello in much the same way. 

$$\begin{align}
\begin{bmatrix}
\text{hello rep }_{1 \times 512} \\
\text{hello there }_{1 \times 512} \\
\text{hello how }_{1 \times 512} \\
\text{hello are }_{1 \times 512}\\ 
\text{hello you }_{1 \times 512}
\end{bmatrix} \cdot \underbrace{W_{Q}}_{512 \times 512}
\end{align} = \begin{bmatrix}
\text{hello Q }_{1 \times 512} \\
\text{hello Q }_{1 \times 512} \\
\text{hello Q }_{1 \times 512} \\
\text{hello Q }_{1 \times 512}\\ 
\text{hello Q }_{1 \times 512}
\end{bmatrix}$$
We should be able to see that "hello" in each sentence should __only__ have a representation that depends upon itself, and none of the other words. The same is true for both $K$ and $V$. 

For both the $Q,K,V$ matrices it should be apparent that the representation of hello is always independent from the others. In the sentences, "hello" and "hello there how are you", the representations of hello in both the $Q.K,V$ computations will be _identical_. 

This is significant since instead of passing in each word at once we can pass in all $n-1$ and still get the same results. Recall here that there is no mixing and we are just working a single layer of a transformer. 

---
# Attention Computation 

Let's consider the baby representation with just $QK^T$. 

![[Pasted image 20261026025524.png]]

Hello only sees itself here in this example. We can continue this process including other example with the next $2$ words:

![[Pasted image 20261026025622.png]]

Here we mask different parts of the attention in order to simulate not seeing different parts of the input. If we have "hello there how are" we get:

![[Pasted image 20261026025736.png]]


Thus for the [[Attention (Transformers)]] computation, we can take a [[Lower Triangular Matrices]] representation of the attention matrix in order to get the input as if we only entered $n-k$ words, we would blank out the remaining $k$ cases. We would do this by setting each $k$ to numerically negative infinity (since $e^{-\infty}=0$ very unrigorously)

Here let's just suppose we are working with $n=5$ many words in "hello there how are you" disregarding everything we have above:
 $$\begin{array}{c|ccccc} & \text{hello} & \text{there} & \text{how} & \text{are} & \text{you} \\ \hline \text{hello} & \cdots & -\infty  & -\infty & -\infty & -\infty \\ \text{there} & \cdots & \cdots & -\infty & -\infty & -\infty \\ \text{how} & \cdots & \cdots & \cdots & -\infty & -\infty \\ \text{are} & \cdots & \cdots & \cdots & \cdots & -\infty \\ \text{you} & \cdots & \cdots & \cdots & \cdots & \cdots \end{array}$$ This is how our attention matrix would look like instead. 

 We should recall $A=\text{softmax}\left( \frac{QK^T}{\sqrt{ d_{k} }} \right)$. For instance with $[2,4,5,7]$, and only want the first $2$ terms, if we use $-\infty$ for the values we want to ignore, they would not be included in our computation. 

---
# Layer Output and Masking

When we use this particular representation $AV$ in the output of our layer, we can essentially isolate each word, thus the embedding is only built on top of the relevant words. 

$$\begin{array}{c|ccccc} & \text{hello} & \text{there} & \text{how} & \text{are} & \text{you} \\ \hline \text{hello} & \cdots & 0  & 0 & 0 & 0 \\ \text{there} & \cdots & \cdots & 0 & 0 & 0 \\ \text{how} & \cdots & \cdots & \cdots & 0 & 0 \\ \text{are} & \cdots & \cdots & \cdots & \cdots & 0 \\ \text{you} & \cdots & \cdots & \cdots & \cdots & \cdots \end{array}_{5 \times 5} \cdot \begin{bmatrix}
\text{hello V }_{1 \times 512} \\
\text{there V }_{1 \times 512} \\
\text{how V }_{1 \times 512} \\
\text{are V }_{1 \times 512}\\ 
\text{you V }_{1 \times 512}
\end{bmatrix}_{5 \times 512} = \begin{bmatrix}
\text{hello CONTEXT }_{1 \times 512} \\
\text{there CONTEXT }_{1 \times 512} \\
\text{how CONTEXT }_{1 \times 512} \\
\text{are CONTEXT }_{1 \times 512}\\ 
\text{you CONTEXT }_{1 \times 512}
\end{bmatrix}_{5 \times 512} $$
Say we just consider the "hello" representation with context. Due to the fact that the hello row has $0$'s after hello's own attention, we only take hello with respect to itself. 

![[Pasted image 20261026030543.png]]

For "hello there" we have the first two words as input:

![[Pasted image 20261026030705.png]]

How and are __notably are not included__. 

Notably we are interested in the __last layer of the output__ since it has seen every single word in the sequence:

![[Pasted image 20261026030857.png]]

---
# Masking and Generation

If on the last layer $\ell$ we pass in all of the words at once and use them to predict the next word in the sequence:

![[Pasted image 20261026031300.png]]

We use hello to predict there, there to predict how, how to predict are, and are to predict "you". This is the total output from the operation. 
### Masking Summary

* We do not feed in the sentence "hello there how are you" in chunks of words like "hello", "hello there", ... , "hello there how are you" in chunks, instead we pass __the entire sentence in at once__

* By applying masking in the attention computation of the [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]] we are able to feed in the sentence "hello there how are you all at once". This is the big advantage of using masking

* We can then use different rows on the output layer 