---
title: Random Forests
tags:
draft: "false"
---
# [[Random Forests]] 
[[Random Forests]] are based around the [[Decision Tree]] algorithm, where our goal is to produce a group of [[Decision Tree]]s, this makes up a [[Decision Forest]]. We take the average of the results of our trees, and we get an ensemble result. The [[Decision Forrest]] is a black box model. We lose [[Interpretability]] as we add more trees. 

The way we train [[Random Forests]] is by [[bagging]], we take a subset of the $n$ points, and we sample with replacement to grow a tree from them. 

As a common example for [[Decision Tree]]s we ask the question, will a custom wait for a restaurant as a pretty typical problem. 

The decision forest starts by choosing $m$ features randomly, and then evaluates the splitting criteria on the trees, and run the same algorithm essentially. 

With bootstrap resamples. There is no pruning at all on these trees. 

Random forests are very nonlinear as well, very predictive.
