
In generation we predict a word at a time. If we have inputs provided that are used in training, we can essentially do [[unsupervised]] learning. We can ask a model to predict the next word in the sentence. 

For some given sentence, "hello there how are you" as an input, how many $x$ and $y$ training examples can be constructed?

It turns out that we can construct for some sentence with $n$ words, we can produce $n-1$ training samples. 

---
# What is the issue in text generation?

A model generally has a lot of redundant inputs. We want some way to speed up a forward pass. For instance in "hello there how are you", regardless of what we feed a [[Machine Learning/Machine Learning/LLM/Model Types/Transformer|Transformer]], the representation of hello there, hello there how, and so forth will all represent hello in much the same way. 

For both the $Q,K,V$ matrices it should be apparent that the representation of hello is always independent from the others. In the sentences, "hello" and "hello there how are you", the representations of hello in both the $Q.K,V$ computations will be _identical_. 

For the [[Attention]] computation, we can take a [[Lower Triangular Matrices]] representation of the attention matrix in order to get the input as if we only entered $n-k$ words, we would blank out the remaining $k$ cases.

How do we numerically accomplih this? We should recall $A=\text{softmax}\left( \frac{QK^T}{\sqrt{ d_{k} }} \right)$. For instance with $[2,4,5,7]$, and only want the first $2$ terms, if we use $-\infty$ for the values we want to ignore, they would not be included in our computation. 

When we use this particular representation $AV$ in the output of our layer, we can essentially isolate each word, thus the embedding is only built on top of the relevant words. 

After we pass in $n-1$ through the network, 