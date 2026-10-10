---
title: Attention
tags:
  - Machine_Learning
draft: "False"
---
# Attention (Transformers)

Building off of the simplified model of [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]]s previously described, mathematically attention is $A=Q \times K^T$ where $Q=X \times W_{Q}$. It is important to note that this matrix is also __not necessarily a symmetric matrix__. 

We are multiply each word by a weight matrix to try and get a better feature representation of that word. We need to have the [[Transpose]] here so that can actually multiply $Q,K$ in some form.

If $Q,K \in \mathbb{R}^{5 \times 512}$ then the resulting matrix $QK^T \in \mathbb{R}^{5 \times 5}$. Take the following:

$$ \underbrace{ \begin{bmatrix} \mathbf q_1^{\mathsf T}\\ \mathbf q_2^{\mathsf T}\\ \mathbf q_3^{\mathsf T}\\ \mathbf q_4^{\mathsf T}\\ \mathbf q_5^{\mathsf T} \end{bmatrix} }_{5\times512} \; \underbrace{ \begin{bmatrix} \mathbf k_1 & \mathbf k_2 & \mathbf k_3 & \mathbf k_4 & \mathbf k_5 \end{bmatrix} }_{512\times5} = \begin{bmatrix} \mathbf q_1^{\mathsf T}\mathbf k_1 & \mathbf q_1^{\mathsf T}\mathbf k_2 & \mathbf q_1^{\mathsf T}\mathbf k_3 & \mathbf q_1^{\mathsf T}\mathbf k_4 & \mathbf q_1^{\mathsf T}\mathbf k_5\\ \mathbf q_2^{\mathsf T}\mathbf k_1 & \mathbf q_2^{\mathsf T}\mathbf k_2 & \mathbf q_2^{\mathsf T}\mathbf k_3 & \mathbf q_2^{\mathsf T}\mathbf k_4 & \mathbf q_2^{\mathsf T}\mathbf k_5\\ \mathbf q_3^{\mathsf T}\mathbf k_1 & \mathbf q_3^{\mathsf T}\mathbf k_2 & \mathbf q_3^{\mathsf T}\mathbf k_3 & \mathbf q_3^{\mathsf T}\mathbf k_4 & \mathbf q_3^{\mathsf T}\mathbf k_5\\ \mathbf q_4^{\mathsf T}\mathbf k_1 & \mathbf q_4^{\mathsf T}\mathbf k_2 & \mathbf q_4^{\mathsf T}\mathbf k_3 & \mathbf q_4^{\mathsf T}\mathbf k_4 & \mathbf q_4^{\mathsf T}\mathbf k_5\\ \mathbf q_5^{\mathsf T}\mathbf k_1 & \mathbf q_5^{\mathsf T}\mathbf k_2 & \mathbf q_5^{\mathsf T}\mathbf k_3 & \mathbf q_5^{\mathsf T}\mathbf k_4 & \mathbf q_5^{\mathsf T}\mathbf k_5 \end{bmatrix} $$
Here each entry of the [[Attention (Transformers)]] matrix is the similarity measure between the two words where the similarity provided in this simplified instance is simply the [[Inner Product]]:
$$ \begin{array}{c|ccccc} & \text{hello} & \text{there} & \text{how} & \text{are} & \text{you} \\ \hline \text{hello} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{there} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{how} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{are} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{you} & \cdots & \cdots & \cdots & \cdots & \cdots \end{array} $$

* The attention computation is a [[Similarity Measure]] for how similar each word is to each other 

* Big Picture: The attention computation compares different words in the sentence together. This is important for developing context. 

* We are still missing normalization 

---
# Normalization

We have two remaining steps to fully process the Attention Matrix. First, we need to divide the product $\frac{QK^T}{\sqrt{ d_{k} }}$ where $d_{k}$ is the dimension of the $W_{K}$ matrix (it is square). 

The reason we divide by $\sqrt{ d_{k} }$. The main reason why is that there is a high [[Variance]] in this part of the transformer. Dividing by this amount causes __vanishing gradients__. 

We want to ask ourself here, are attention similarity scores normalized? We apply the [[Softmax]] function to each row of the Attention matrix:

$$\begin{array}{c|ccccc} & \text{hello} & \text{there} & \text{how} & \text{are} & \text{you} \\ \hline \text{hello} & v_{1} & v_{2} & v_{3 } & v_{4} & v_{5} \\ \text{there} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{how} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{are} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{you} & \cdots & \cdots & \cdots & \cdots & \cdots \end{array} $$
We want to normalize over the values of each row. So here, the normalizing factor is:

$$\sum_{k=1}^5 e^k = e^{v_{1}}+e^{v_{2}}+\dots + e^{v_{5}} $$
Each value in the first row then becomes $\frac{e_{v_{k}}}{\sum_{j=1}^5 e^j}$:

$$\begin{array}{c|ccccc} & \text{hello} & \text{there} & \text{how} & \text{are} & \text{you} \\ \hline \text{hello} & \frac{e_{v_{1}}}{\sum_{j=1}^5 e^j} & \frac{e_{v_{2}}}{\sum_{j=1}^5 e^j} & \frac{e_{v_{3}}}{\sum_{j=1}^5 e^j} & \frac{e_{v_{4}}}{\sum_{j=1}^5 e^j} & \frac{e_{v_{5}}}{\sum_{j=1}^5 e^j} \\ \text{there} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{how} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{are} & \cdots & \cdots & \cdots & \cdots & \cdots \\ \text{you} & \cdots & \cdots & \cdots & \cdots & \cdots \end{array} $$
Now we iiteratively apply this to each row of the matrix until we have normalized all such rows. 