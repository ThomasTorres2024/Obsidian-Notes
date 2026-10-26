---
title: Transformer Classification
tags:
  - LLMs
  - Transformer
  - Machine_Learning
---
# Transformer Classification

For classification tasks what do we need to train? We need data with labels. We have some input text and some class we want to assign it to. We can take in some content from our model and compute the model's predicted class label, $\hat{y}$:

![[Pasted image 20261026023329.png]]

We then compute the error using a [[Loss Function]], usually [[Cross Entropy]] as a common metric. From some training we would typically get something like the following:

$$\begin{align}
y = \begin{bmatrix}
0 & 0 & \dots & 1 & \dots & 0
\end{bmatrix} \\
\hat{ y} = \begin{bmatrix}
0.05 & 0.1 & \dots & 0.3 & \dots & 0.01
\end{bmatrix}
\end{align}$$
The predicted label is the highest probability in the output vector, $p_{c}$ for the $c$th class. Here the loss function is:
$$\ell  = -\sum_{c=1}^K y_{c} \ln(p_{c})$$
Where $K$ is the number of classes, $c$ is the output from $0-1$ (since it is a [[Probability]]) and $p_{c}$ is predicted output. To minimize loss we would have $y_{c}=1$ and $p_{c}=1$. 

We perform a [[Backpropagation]] on the model and update the respective weights  of the model.  