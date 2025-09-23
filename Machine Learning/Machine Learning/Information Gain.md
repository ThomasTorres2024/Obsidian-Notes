---
title: Information Gain
tags:
draft: "false"
---
# Information Gain Intuition
Information gain is a metric which allows us to measure how much we have reduced [[Entropy]] in our model. [[Entropy]] is the measure of how indeterminate our data set is, that is the ratio between one category and the other category within our set very loosely. 

If we are able to isolate all data to only have one category in it, then we are dealing with something with zero [[Entropy]]. We know with 100% certainty that what we are looking at is a specific set, and contains no elements of different categories. If we have a perfectly even ratio, that is $1:1$ of both categories, our [[Entropy]] score reaches its maximum at 1. If we were to guess here, guessing either category would have equal probability of occurring, and so we can't say anything about our information. 

When we are working with a model, and want to be able to bisect our data into two distinct categories, we need to be able to get to the point where our entropy reduces and reduces until we can firmly classify our categories.

# Decision Trees and [[Information Gain]]
In the context of [[Decision Tree]] algorithms, we examine our features, and look for the feature at every iteration which is responsible for the greatest [[Entropy]] reduction. This is the idea of [[Information Gain]], how much does splitting on a variable actually tell us?

# Information Gain Formula
Information gain is defined by the following, given that $\mathcal{D}$ is our dataset, and $H$ is the entropy function, we get the $IG$ function, or the [[Information Gain]]ed function:
$$IG(D,A)=H(D)$$

