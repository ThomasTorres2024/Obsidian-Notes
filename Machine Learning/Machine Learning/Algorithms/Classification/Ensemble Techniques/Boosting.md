---
title: Boosting
tags:
draft: "false"
---
# [[Boosting]]

Boosting is an ensemble technique in machine learning, where we take multiple methods and combine them to create an overall better classifier. we want to have many classifiers that aren't very strong, but as these are combined, we create an overall stronger predicter $F$. In the case of boosting we make $f_{1}$, and then we make $f_{2}$ based on the performance of $f_{1}$, and so on until we end up producing all of the different $f$s necessary. 

In bagging we create all of our functions at once instead of sequentially, that is in parallel as opposed to sequentially here. 

#### Weak Learner Definition
a classifier that needs to be better than random guessing, at least by a little, so the probability of a guessing correctly is more than 50%. The idea is if we combine many weak learners together we can create an overall strong learner together from all of this info. 

Shallow decision trees, linear models, help us generate overall stronger decision boundaries, our weak learners are very fast to make, and so our model is very fast to make overall. 

If we have many weak classifiers, then we can sum up the weak models performance, and overall get our resulting strong classifier. This means that each model, $h_{i}(x)$ has its own associated weight when making our decision $a_{i}$. Let $H(x)$ denote the strong classifier, then it follows that:

$$H(x)=\text{sign}\left(\sum_{i=1}^Ta_{i}h_{i}(x)\right)$$
If we are given enough info we can construct a single predictor with a very high accuracy, and this is something that we can prove mathematically. 

#### Training
We have training weights where when we are setting up our weak learners, we need to be able to weigh them based on the data they are operating on. The slideshow uses examples of linear decision boundaries. When we train our sets we ensure that their error performs above a given threshold, $\epsilon$. 

We make a partition where one side is classified as one category and the other category as another set. The data that is misclassified by the decision boundary is weighted more heavily for the next function produced. We repeat the process until we have found enough classifiers. 

For instance the email classifier that uses boosting would take in all of the different emails, that contain the word buy, then we make a second weak learner that goes from this and determines like if its amazon then its not spam. We train the second model based on the first one. We base off of what our first model gets wrong, and then we make a new model based on what was wrong. This is the key part of boosting. 

Another point of contrast, compared to [[Random Forests]] and [[bagging]] methods, we do not evenly weight the models we produced, whereas both of these models tend to group up the weights evenly. For instance if we are making use of decision stumps, we weigh some stumps over others.

We have several different approaches for boosting, of the successful ones is [[Adaboost]].