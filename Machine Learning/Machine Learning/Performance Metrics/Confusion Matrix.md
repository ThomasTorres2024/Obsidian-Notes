---
title: Confusion Matrix
tags:
draft: "false"
---
# Background on Classification
If we are working on a [[classification]] problem, we want to be able to divide our data into two categories, one which is denoted as the positive category, or the set of items we are looking for, say in the instance of medical testing these are people with a rare illness, and a negative category where people are not sick. When we have multiple categories of things to look for, we can ignore the category where people are different. 

From this we have a couple of terms;
* [[True Positive]] - When a point is classified as positive and it actually is positive (TP)
* [[False Positive]] - When a point is classified as positive and it actually is negative (FP)
* [[True Negative]] - When a point is classified as negative and it actually is negative (TN)
* [[False Negative]] - When a point is classified as negative and it actually is positive (FN)

We can compute each of these quantities by counting the number of items that our model predicts and whether or not they actually are positive or negative. 
# Accuracy
A typical measure for success is [[Accuracy]], however this metric tends to be quite poor when we consider [[Imbalanced Data]]. We define accuracy as the number of correctly marked points out of the whole, that is to say:
$$\text{accuracy } = \frac{TP+TN}{TP+FP+TN+FN}$$
Very simply, the sum of all of $TP+FP+TN+FN$ is equivalent to all points that our model classified. And $TP+TN$ is the amount that our model got correct, which means it is the number of items where we actually predicted negative on a negative item and predicted true on a true item. So this is clearly a ratio of how likely we are to correctly predict something assuming that our data is good. 

#### Faults of Accuracy as a Metric
Accuracy is a poor metric in many cases because our performance can vary depending upon the model, and thus we tend to prefer giving [[confidence intervals]] with respect to a boundary for how good our model is. Secondly, we can quickly show how useless [[Accuracy]] is as a metric when we are using [[Imbalanced Data]]. 

# Imbalanced Data and Accuracy
Accuracy is quite useless when we are working with [[Imbalanced Data]], this is because we have a minority of points in one of the two categories we are looking to classify. We can predict everything to be in the majority, and our model would still perform excellently even though it says absolutely nothing about the structure of the underlying data, and doesn't actually give anything which is useful. 

For instance, in medical tests, a vast majority of people sampled do not have any ailment that we are looking for. If our model predicted everyone was in negative, we still would do quite well. 

We introduce 2 metrics here to deal with imbalanced data, [[Precision]] and [[Recall]]. 

#### [[Precision]]
[[Precision]] allows us to model the number of people which were correctly labeled as positive out of all people labeled as positive. If we predict everyone is negative, then our precision score will fall flat. The formula for precision is given by:
$$\text{precision } =\frac{TP}{TP+FP}$$
If everyone is predicted as being negative, then we clearly will get 0 here in the numerator, and our precision score will get rocked to 0. So we can no longer hide behind our accuracy score with a good model, we have a way of quantifying bad models which under predict the true number of positives.

We can cheat this score and make few true positive predictions. But, the [[Recall]] metric counteract this.

#### [[Recall]]
[[Recall]] asks us, out of all things which are actually true, [[False Negative]] and [[True Positive]]s, how many are actually labeled as a true positive? 
$$\text{recall } = \frac{TP}{TP+FN}$$
If we have imbalanced data and let everything be negative, again we are getting a low recall score. We could cheat this as well and let everything be positive, and give us a 1 score for recall. However, the precision score counts as a counterbalance to cheating the recall score. 
#### [[F-1 Score]]
When we cheat at [[Recall]] we get a 0% [[Precision]] score, and when we cheat at [[Precision]] we get a 0% [[Recall]] score. It turns out there is a way to counteract both. The [[F-1 Score]] is 50% when we cheat with recall, and 50% when we cheat with precision.  

Using the [[F-1 Score]] allows us to maximize both the [[Precision]] and the [[Recall]] scores. The formula for the [[F-1 Score]] is given by the following:
$$F_{1}= \frac{2 \cdot TP}{2 \cdot  TP + FP + FN} $$
$F_{1}$ is a very common metric, and typically is adequate in its predictions. $F_{1}$ is good at [[Binary Classification]], but if we have [[Multinomial Classification]] $F_{1}$ struggled. It also never factors [[True Negative]]s into its equation. 

The $F_{1}$ score is a [[Harmonic Mean]], which is used for taking the averages of rates and ratios, like speeds, and is given as the reciprocal of the Arithmetic mean of the reciprocals. 
# Confusion Matrix Introduction
Performance metrics like accuracy often do not tell us enough about our model. We encapsulate all the other information in a [[Confusion Matrix]], which allows us to represent the performance of our model, and potentially see where things are going wrong. We define a confusion matrix for [[Binary Classification]] by the following:
$$ \text{confusion matrix } = \begin{bmatrix} TP & FN\\ FP & TN \end{bmatrix}$$
It is significantly easier to diagnose what may be wrong with a model with high accuracy but little to no use by examining its confusion matrix. For instance, we could have a 95% accuracy model but with no predictions under the false positives or true negatives. Of course the other metrics would help show this as well, but this is just another way to demonstrate that fact.