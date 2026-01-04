---
title: Variable Importance
tags:
draft: "false"
---
# [[Variable Importance]]
In [[Decision Tree]]s we may ask if the top feature within a [[Decision Tree]] is the most predictive. We want to be able to ask how useful a certain variable is to classify certain data. How important is a certain feature to classification of our data. The idea is very intuitive, but precisely defining is not something that we are given. 

In a [[Decision Forest]] it is a lot easier to say how much a single variable matters than in a [[Decision Tree]]. 

We can model the reliance of our data by scrambling data and then examinign the maragin of error. 

We have permuted error vs non-permuted, and the result is just the average distance. All we need to do is scramble our data and see what our result is.

For instance in the Rise algorithm, we want to classify things, and we want to observe which pixels are the most important. We add some noise or black out our image, and then we see how the result occurs after that, if the data comes out quite poorly, then we can infer that this region was likely quite important. We need to be able to permute the pixels such that it isn't the same signal. 

In data science, it is a quite common questions to know what features are the most important in our data set. 

---
# Rashomon Sets
Rashomon sets are the set of all good models given some constraints. The Rashomon set for decision trees, is for a specific dataset, for some loss term. This is very important for [[Variable Importance]]. 

If we look at all possible decision trees within a set, we have a good way to see what the most important variable is. Originally this idea was for [[Decision Tree]]s because we have some random chance there and can make equivalent trees quite easily. 

We have similar problems for [[Neural Nets]], so the space of [[Rashomon Sets]] is a set which is considerably longer. For [[Decision Tree]]s in a 10,000 entry Data table, we can compute them in a week. But for [[Rashomon Sets]] on [[Neural Nets]], we have to literally sample from the data. 

---
# Variable Importance 
Measure how important a given variable is to determine a model's prediction.

Variable importance is necessary when we have a lo of data with too many variables, and also when interventions are expensive/immoral

I we scramble a particular column in our dataset, then we can measure how much it effects our output by computing a new output and the predicted output

We can't find $g*$ generally: 
* The function $g^*$ we are claiming that exists isn't something that we really know well, and many models may predict very well, so that makes $g*$ hard to find 
* We also on sample a fraction of the population [[Finite Sample Bias]]
* We can also not measure every variable here, [[Unobserved Confounding]]. For example consider the forest fires per year versus the sale of ice-cream, and how they correlate because they tend to correlate to the temperature of the year. 

Find surrogate that let us avoid $g^*$, we want to be able to build up [[Variable Importance]] to $g^*$ without directly using it since such a function is impossible

Each $f_{u}$ that is able to model our performance below some loss threshold is included within the [[Rashomon Sets]]. The case for population loss has a loss which we assume to be less than the loss for the [[Empirical Loss]], because there is some skewdness to our data. 

We have a specific term for $\epsilon_{n}$, which is inversely proportional to $n$, which so as $n\to \infty$, our $\epsilon_{n}$ decreases. 

We want to look at the variable importance for each $f_{u}$. We also have a way to bound the probability of these models when we scramble them We can still get estimate bounds for 