---
title: Model Selection
draft: "false"
tags:
---
# Model Selection
Model selection gives a set of $1-n$ many models in the set $F$. These models have different parameters. People often just pick the highest accuracy one, there are risks of [[Overfitting]] or [[Underfitting]], or performing well. We thus have [[Hyperparameter Tuning]], which takes parameters for our models and them optimizing them.

For [[Decision Tree]]s this would include the total number of branches. We have grid search and random search as well as some Bayesian thing?

A model $F$ has perfectly learned the testing data provided. Again this doesn't really apply to [[Neural Nets]].

[[Underfitting]] is if a model is too simple to catch all of the necessary structure of the data. For isntance if we want to fit a quadratic curve with a linear model. It may mean taht we have too little training or the wrong type of data. For instance how many [[Epoch]]s have we done. An [[Epoch]] is roughly how many times we've iterated over the [[training set]]. 

The [[training set]] is the data we are using to train a model. Real tests need us to really set aside our information, and then use it at the end to report final numbers. A common machine learning problem is overfitting to already public models. This is very hard to do when we need to get a test number as high as everyone else's. If we are a business and the only people with the data, never give our data to anyone esle.

We want to simulate how the model on unseen data. In the medical world this is called retrospection and prospection. 

The way we do a train, validation and test set, we typically want 10-15% of the data way for tests, 10-15% for validation, and then the remainder for training. The job of us is to take the training set and then to separate it accordingly. 

---
# Pros and Cons of each method
For the train validation test split, we only need to run once, instead of say k-folds. It takes a lot more time. For instance gigantic sets could result in a 2 week [[Epoch]]. A single split could be bad, like we get random data in there that could skew it, but as the data set gets bigger we stop as it could lead to some problems.

K-fold is decent if we have enough 

Stratified k-fold/cross validation is really mportant becaus
