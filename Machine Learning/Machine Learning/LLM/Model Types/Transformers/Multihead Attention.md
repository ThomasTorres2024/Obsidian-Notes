---
title: Multihead Attention
tags:
  - Machine_Learning
  - LLMs
draft: "False"
---
# Multihead Attention

Let us construct a [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]] with the following architecture. Assuming the following, we have a dictionary size of $50,000$, an embedding size of $d=512$, and $L=1024$ is our __sequence length__ (number of words the model can process at one time). 

We want to begin by converting each word to a number through the process of [[One Hot Encoding]], "hello" $\to$ gets converted to some vector $x$ in $1 \times 50,000$. We then take an embedding matrix, $W \in \mathbb{R}^{50,000 \times 512}$. 

Then by doing $xW$ we get a representation in $\mathbb{R}^{1 \times 512}$. Let us assume we have a sentence with 1024 words. Then, this gives that our resulting representation matrix will be of size $\mathbb{R}^{1024 \times 512}$.

So far we have previously seen an architecture with a single attention head. Under this model we have the following: 

---
## Simplified (Singleheaded Attention) Algorithm

Let us recount the simplified singlehead attention on a single layer:

1. Start with $X \in \mathbb{R}^{1024 \times 512}$
2. Obtain $Q$ via $Q=X \cdot W_{Q} : W_{Q} \in \mathbb{R}^{512 \times 512}$ 
3. Obtain $K$ via $K=X \cdot W_{K} : W_{K} \in \mathbb{R}^{512 \times 512}$ 
4. Obtain $V$ via $V=X \cdot W_{V} : W_{V} \in \mathbb{R}^{512 \times 512}$

(Note that $Q,K,V \in \mathbb{R}^{1024 \times 512}$)

5.  $A= Q \times K^T \in \mathbb{R}^{1024 \times 1024}$
6. $\text{out}=A \cdot V \in \mathbb{R}^{1024 \times 512}$

---
# Introduction to Multiheaded Transformers 

Let us assume that we want $8$ heads. We have $512$ features in total. One of the reasons we are interested in doing this is to increase total model complexity. By adding more layers we can also increase the complexity, but these computations cannot be done in parallel whereas the heads and partitioning of the matrices can be done in parallel quite easily since every head is independent from one another in terms of computation.

We can choose to work only on the first $64$ features instead, since each head now works on $64$ features. 

Through this model, we will have that $W_{K}^{(1)},W_{Q}^{(1)},W_{V}^{(1)} \in \mathbb{R}^{64 \times 64}$. We will also have a new set of $Q^{(1)},K^{(1)},V^{(1)}$ which will be in $\mathbb{R}^{1024 \times 64}$ together. 

We have a corresponding set of weight, attention, out and $Q,K,V$ type matrices for each layer. 

Once we have computed the respective outputs from each layer, we then take them and compress them into a single matrix at the end of size $\mathbb{R}^{1024 \times 512}$, which is the size of out originally in the singleheaded transformer. 

We want to slice column wise for our words, otherwise they would be only going row by row and we would still have to deal with the issue of __words being processed independently__ where we lose context inbetween each word. 