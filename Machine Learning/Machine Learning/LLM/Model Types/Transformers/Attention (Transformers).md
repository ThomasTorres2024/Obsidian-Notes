---
title: Attention
tags:
  - Machine_Learning
draft: "False"
---
# Attention (Transformers)

Building off of the simplified model of [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]]s previously described, mathematically attention is $A=Q \times K^T$ where $Q=X \times W_{Q}$. It is important to note that this matrix is also __not necessarily a symmetric matrix__. 

We are multiply each word by a weight matrix to try and get a better feature representation of that word. We need to have the [[Transpose]] here so that can actually multiply $Q,K$ in some form. This is the only reason we use it. 

If $Q,K \in \mathbb{R}^{5 \times 512}$ then the resulting matrix $QK^T \in \mathbb{R}^{5 \times 5}$. Take the following:

$$ \underbrace{ \begin{bmatrix} \mathbf q_1^{\mathsf T}\\ \mathbf q_2^{\mathsf T}\\ \mathbf q_3^{\mathsf T}\\ \mathbf q_4^{\mathsf T}\\ \mathbf q_5^{\mathsf T} \end{bmatrix} }_{5\times512} \; \underbrace{ \begin{bmatrix} \mathbf k_1 & \mathbf k_2 & \mathbf k_3 & \mathbf k_4 & \mathbf k_5 \end{bmatrix} }_{512\times5} = \begin{bmatrix} \mathbf q_1^{\mathsf T}\mathbf k_1 & \mathbf q_1^{\mathsf T}\mathbf k_2 & \mathbf q_1^{\mathsf T}\mathbf k_3 & \mathbf q_1^{\mathsf T}\mathbf k_4 & \mathbf q_1^{\mathsf T}\mathbf k_5\\ \mathbf q_2^{\mathsf T}\mathbf k_1 & \mathbf q_2^{\mathsf T}\mathbf k_2 & \mathbf q_2^{\mathsf T}\mathbf k_3 & \mathbf q_2^{\mathsf T}\mathbf k_4 & \mathbf q_2^{\mathsf T}\mathbf k_5\\ \mathbf q_3^{\mathsf T}\mathbf k_1 & \mathbf q_3^{\mathsf T}\mathbf k_2 & \mathbf q_3^{\mathsf T}\mathbf k_3 & \mathbf q_3^{\mathsf T}\mathbf k_4 & \mathbf q_3^{\mathsf T}\mathbf k_5\\ \mathbf q_4^{\mathsf T}\mathbf k_1 & \mathbf q_4^{\mathsf T}\mathbf k_2 & \mathbf q_4^{\mathsf T}\mathbf k_3 & \mathbf q_4^{\mathsf T}\mathbf k_4 & \mathbf q_4^{\mathsf T}\mathbf k_5\\ \mathbf q_5^{\mathsf T}\mathbf k_1 & \mathbf q_5^{\mathsf T}\mathbf k_2 & \mathbf q_5^{\mathsf T}\mathbf k_3 & \mathbf q_5^{\mathsf T}\mathbf k_4 & \mathbf q_5^{\mathsf T}\mathbf k_5 \end{bmatrix} $$
Here each entry of the [[Attention (Transformers)]] matrix is the similarity measure between the two words where the similarity provided in this simplified instance is simply the [[Inner Product]]:
$$ \begin{array}{c|ccccc} & \text{hello} & \text{there} & \text{how} & \text{are} & \text{you} \\ \hline \text{hello} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{there} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{how} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{are} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{you} & \cdots & \cdots & \cdots & \cdots & \cdots \end{array} $$

* The attention computation is a [[Similarity Measure]] for how similar each word is to each other 
	* To spell it out, on row $1$ we have the similarity between hello and itself, hello and there, hello and how, hello are are, and hello and you

* Big Picture: The attention computation compares different words in the sentence together. This is important for developing context. 

* We are still missing normalization 

