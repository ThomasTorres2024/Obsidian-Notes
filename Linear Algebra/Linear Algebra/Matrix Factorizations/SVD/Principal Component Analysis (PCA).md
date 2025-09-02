---
title: Principal Component Analysis (PCA)
tags: 
draft: "false"
---
# Principal Component Analysis 

PCA is still one of the most common methods at performing dimension reduction in a given data matrix, $\bar{X}$. We can reduce the total number of features in our matrix and boil it only to the most relevant components and observe clustering without clustering in other parts. 

Our data matrix is given below in the following: 

$$\bar{X}= \begin{bmatrix} \vec{x}_{1}^T \\  \vec{x}_{2}^T \\ \vdots \\ \vec{x}_{n}^T  \end{bmatrix}$$

We want to unpack $\bar{X}$ using SVD so that we can isolate $\bar{X}$ to the features which provide the best statistical interpretation of the matrix. 

We can compute a mean row vector with the following formula:  

$$\bar{x}_=\dfrac{1}{n} \sum_{j=1}^nx_{j}$$

We will construct an average matrix here by taking each 

