---
title:
tags:
draft: "false"
---
# Definition

Classification Algorithms take in a labeled data-set, $\mathcal{D}= \{(x,y) \}_{i=1}^n$, and map the data-set to a prediction function which serves as a [[decision boundary]]. We assume that each item in the data-set is binary, meaning it is labeled as having one attribute or another and that having the label is mutually exclusive.

The values in $x$ consist of our explanatory or [[Independent Variables]]. 

The goal of binary classification is to find a function $f(\vec{x})$ which takes entries from our [[Feature Matrix]] and produces a boundary within our dataset, such that anything which is on one side of the [[decision boundary]] belongs to one binary category, and everything on the other side belongs to the other binary category. 

We can write a generic classification algorithm, $A$ as the following map:
$$A : \mathcal{D} \to f$$
$$f : \vec{x} \to \mathbb{R}$$
Our function can predict whether or not a new $\vec{x}$ will belong to one category or to another category. The predicted value is given by:
$$f(\vec{x})=\hat{y}$$
For instance, If we feed a new image into our image prediction algorithm $x$, we get our prediction $\hat{y}$. Because the data we are working with is labeled, we can say that classification is a form of [[Supervised Learning]]. 

We want to be able to discretize our function into the two binary categories we are trying to classify. We will take the value of our function $f(\vec{x})=\hat{y}$, and then feed it into a sign function, which basically assesses which side of the [[decision boundary]] we are on:
$$\text{to determine the side of the boundary: } \text{sign}(f(\vec{x}))$$
--- 
# Test Set
We need to be able to split our data-set into a training set, and a testing set. We need to ensure that the two will be separate so that our [[Classification]] Algorithm learns the pattern and does not learn the noise so that we may avoid [[overfitting]]:

$$\mathcal{D}'=\{ (x,y) \}_{j=1}^n$$
---
# Error Functions
It is more than likely that our [[decision boundary]] will [[misclassify]] some data point fed into it. This only applies to points. We need to have a way to evaluate the error of our function. For this we introduce the notion of an error function, which quantifies how wrong on average our function is on training data:
$$Error(\hat{y},y)=\mathcal{L}(\vec{y},y)=\mathcal{L}(f(\vec{x}),y)$$
To make this concrete, let's consider the following example of a loss function:
### (Example) 
The following loss function makes use of the indicator function. We also impose a $\frac{1}{n}$ to get a rate parameter:
$$\mathcal{L}(f(\vec{x}),y)=\frac{1}{n} \sum_{i=1}^n \mathbb{1} 
 \begin{cases} \text{sign}(f(\vec{x})) \neq y & 1 \\\text{else } 0 \end{cases}
$$
If the sign of the predicted value does not equal the sign of the true value, then we added 1 to our sum as the value is errant. This particular function is not preferable. For one, the function is not [[Convex]], and furthermore its derivative is zero and has a discontinuity. We can't perform anything akin to [[Optimization/Gradient Descent]] or [[Newton's Method]] to further optimize our model.  

---
