---
title: Text Generation
tags:
  - LLMs
  - Generative_AI
draft: "False"
---
# [[Machine Learning/Machine Learning/LLM/Model Types/Transformer|Transformer]] Classification

Text generation is essentially a reverse process of encoding numbers. The word encoding approach used here is the [[One Hot Encoding]] process, followed by multiplication of an embedding layer. How is this process reversed?

We start with some embedding vector in our output, $\mathbb{R}^{1 \times 512}$, and we want to use this to predict the next word in a sentence. We start by multiply with a projection layer:
$$\text{embedding vec}_{1 \times 512} \cdot W_{512 \times 50,000} \in \mathbb{R}^{1 \times 512}$$
Ideally we would have a one hot encoded (binary) vector, but usually when we do the product, we get a vector with many different values, there is no neat answer. Our way of handling this is by using the [[Softmax]] function to convert them into a reasonable range (no constraints on range originally). 

We then do $\text{max}(\text{softmax}(\text{embedding vec}_{1 \times 512} \cdot W_{512 \times 50,000}))$ which allows us to then convert this number in a dictionary to a useable number. 

##### Why do we want to use softmax instead of just taking the maximum value from the neural net?

Say we have $[-3,-1]$. Comparing values here is a bit weird, and softmax helps us make more sense of the underlying mechanisms since softmax gives us [[Probability]] (Probabilities) that work out.  

---
# Additional Notes

When using our model and training our transformer, we can input our word, and we want the model to output some next following word in the sequence, not the same. 

When we get to the last layer, we only use the LAST row of the output instead of the whole thing. 