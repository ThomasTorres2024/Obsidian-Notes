---
title: Loss Function
draft: "False"
tags:
---
# Loss Function
In its most basic formulation, the [[Loss Function]] is the sum of the error rate for each sample vector, $v_{0}$ given its prediction $\hat{y}$  and its corresponding correct prediction, $y$. The [[Loss Function]] depends upon the metric we employ to measure the total error for each point. There are a couple common options:

1. $L^2$ Error/[[Mean Squared Error]] : $$ \text{MSE}= \sum_{i=1}^n \|y-\hat{y}\|_{2}^2$$
	This metric is particularly useful for [[Least Squares]]
2. $L^1$ loss/[[Mean Absolute Error]]:
$$\text{MAE}=\sum_{i=1}^n \|y-\hat{y}\|_{1}$$
3. [[Hinge Loss]] This is particularly useful for [[Classification]] problems, and also used for [[Support Vector Machines]]. 
4. [[Cross Entropy Loss]] is used to measure the loss in [[Neural Networks]]. 