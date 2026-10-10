---
title: Softmax
tags:
  - LLMs
  - Machine_Learning
draft: "False"
---
# Softmax 

[[Softmax]] is an [[activation function]] which is given by the following:

$$\text{Softmax}(x_{i})= \frac{e^{(x_{j})}}{\sum_{j=1}^K e^{(x_{j})}}$$
Assume here that $x_{i}$ is an element of a set, and we are summing over the set of all items.

We do not use a standard normalization (I don't like the definition they used, it's different than [[Norm]]s in Linear Algebra/ML so this is just an awful example since in L2 we have either squares or in L1 abs values)
$$\text{lecture norm}(x_{i})= \frac{x_{i}}{\sum_{j=1}^K x_{j}}$$
We like [[Softmax]] as well because it produces __large differences in between our scores__, which allows us to distinguish what is important. 

For instance:
$$\begin{bmatrix}
.7 \\
.3
\end{bmatrix} \xrightarrow{\text{Softmax}} \begin{bmatrix}
0.98 \\
0.02
\end{bmatrix}  $$
