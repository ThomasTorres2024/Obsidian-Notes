---
title: Ockham's Razor in Machine Learning
tags:
draft: "false"
---
# Ockham's Razor in Machine Learning
Ockham's Razor is a principle in English in common parlance that says something to the effect of, the most likely reason is the simplest reason. In [[Machine Learning]] we say that the simplest model tends to be the one that is the most generalizable and the ideal model. If we have a super complicated [[decision boundary]], what happens is that we learn all of the information in the [[training set]], rather than the underlying pattern of our information. 

This is described in the graph.  
![[Pasted image 20250908223340.png]]
We have a general rule that complexity is bad in our models. For an example of overfitting check the following below:

![[Overfitting.svg]]
The curve above in Green is an example of overfitting, the boundary is quite nice, but it fails to see the underlying pattern and much simpler decision curve. We add a form of [[regularization]] to our [[loss functions]] that penalizes complexity:
$$\frac{1}{n} \sum_{i=1}^n l(f(\vec{x}),y_{i})+\text{Complexity}(f)$$
This forces us to reduce Complexity in our models when we want to optimize our loss function above. 

This rule does not apply everywhere, as in the context of [[Neural Networks]], we have several different models of regularization that we could use including:
* [[Logistic Loss]]
* [[Hinge Loss]]
* 