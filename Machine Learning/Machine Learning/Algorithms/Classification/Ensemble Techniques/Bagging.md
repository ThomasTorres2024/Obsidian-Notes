---
title: Bagging
tags:
draft: "false"
---
# Bagging 
[[Bagging]] is an [[ensemble method]] which trains many weak learners in parallel, and generally tends to produce very good results. 

Produced in 1996, train man models on random subsets of the data, we want to reduce variance an overfitting, take collective vote of everything, should be faster bc we can do models in parallel, we determine by classification voting, mean/median if regression or 

[[Bootstrapping]]
If we have a dataset $D$, we create $n$ boot strap samples, the standard way to do this is that each amount is of size $n$, same as dataset, but we same with replacement we may have doubles or more entries or missing potentially, which is how we go about forming the data to train our weak learners

we infer things via voting 

[[Random Forests]] is a similar idea but we are taking random features of the data and random feature selection
with random forests instead of taking all features, we take a subset, because decision trees split on features, and if we want a good variety leave out some features, especially if we use a greedy method like splitting on information 

similarly we aggregate via majority vote ehre too 

we can use 

Final remarks with random forests and bagging, very performant, robust to outliers, we can create all decision trees at once

limitations sparse data is really bad for this tree, 

Create bootstrap samples 