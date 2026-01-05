---
title:
---
# Decision Tree Introduction
Decision trees are hierarchical models for [[Classification]] and [[regression]]. These structures are like those of trees. [[Decision Tree]]s are composed of a root node, internal nodes, and leaf nodes. 

[[Decision Tree]]s are quite old but they are very important for the modern day. [[Decision Tree]]s were used to make [[Random Forests]], and have been adopted into [[Optimal Tree]]s, which are the best possible trees. [[Optimal Tree]]s are hard to make, we could run through them by brute force, but our problem is [[NP-Hard]]. Developing the best tree is a relatively open problem in Machine Learning.

Decision trees create very nice nonlinear decision boundaries, very interpretable, and have fast inference. However, training can be very expensive, we can overfit as well, data is very sensitive to small changes. Some complex functions might need exponentially large trees, where we actually would need exponentially more parameters to take account of. 

----
# Issues in Scaling
If we had 500 binary features, then the total number of possible trees would grow to $2^{500}$.  Find optimal binary trees is extremely computationally expensive. 

---
# Binary Trees and Vectors
When we are going through a binary tree, we input a vector, $\vec{x}$, and at each $x_{i}$ of our vector, then we lead to a new node with another binary decision. There are also equivalent Binary Trees. 

Essentially every path is a "rule" which we can represent as a series of conjunction and disjunction statements. If our statement is true, then we predict yes.

![[Pasted image 20250922152505.png]]

For instance if it is sunny and normal humidity, we cane press this as a rule:
$$\text{sunny} \wedge \text{normal humidity } \implies  \text{play tenis}$$

Decision trees are immediately important and interpretable because of this fact. We can also generate counterfactuals pretty clearly, if we changed one factor then we would have gotten different output somewhere else. In [[Neural Networks]], we lose [[Interpretability]], but here it is fully retained. 

---
# [[Decision Tree]] Expressiveness
We can handle discrete values by inputting them and outputting them really easily. We can also take continuous values and discretize them by considering inequalities, like if the temperature is more than 20 degree, we could have a node where we write:
$$\text{temp > 20}$$Which creates a nice binary split:

---
# Hypothesis Space 
If we have more leaves, or something more flexible, then we are able to learn more complex functions. Using functions in this way also results in the potential of [[Overfitting]]. If we try to develop a tree with a near perfect [[Train Score]], it is likely we just memorized the entire dataset we are learning from. 

#### Preventing Overfitting 
One way we can prevent [[Overfitting]] is by removing irrelevant features. If we know that certain features are not very relevant, we can remove them. We can increase the size of the dataset too. We can also use thresholds or some kind of statistical measure in order to stop our training early, if we get to 0.9 accuracy we might be able to stop then and there. This process is known as [[Bounding]]. We also have post-training pruning, which removes branches that are not very significant to performance if they do not add very much [[Information Gain]]. 

It turns out that we can always get 0% testing error as long as we do not have repeat entries, and we can continue to split ad infinitum. 

If our tree is too small, we likely have errors in our training set. If our tree is deep, then we likely will have an awful test score. Finding an optimal tree is again [[NP-Hard]]. The more data we get, we get exponential growth. T
#### Learning Goals for [[Decision Tree]]
We generally want to look for smaller [[Decision Tree]]s that are consistent with the training data. These are likely to be [[Generalizeable]] to other datasets. 

We are looking for a tree that maximizes our test score with the fewest number of possible branches. Such a tree is almost certainly generalizeable. 
#### Finding DTs 
DTs are hard to fine, this is an [[NP-Hard]] problem. We need to use heuristics in order to find a good tree. There is no known polynomial time algorithm for finding a good tree. 

# Decision Tree Boundaries
DTs allow us to partition boundaries quite well that [[Linear Classifiers]] would struggle on. We are able to create and model datasets even with a low depth. 

---
# Consistent Hypothesis
Consistency isn't something we can expect in the real world or in any practical circumstance. We can get pretty close by [[Overfitting]]. A consistent tree exists for every dataset. 

---
# Creating [[Decision Tree]]s 

### 1. Entropy Model 
We need to calculate the [[Entropy]] of our data, which allows us to select our most prominent feature. We want a set which is mostly the same, we want to work with something that is the most entropic. This is a very early thought in the development of these algorithms. This is also known as the [[purity]] or [[uncertainty]]. We want to split in a way that minimizes the total [[Entropy]]. 

We can calculate [[Information Gain]] after splitting on a particular feature. We can calculate the [[Entropy]] of the first group, and then the entropy of the second group, 

![[Pasted image 20250922154023.png]]

For instance here, on the left we are actively partitioning our dataset into branches where we are gaining information, we are able to actually distinguish and thereby classify the points, whereas on the right at each stage we still have the same entropy as when we began. When we build trees, we want to find the characteristic that results in the highest [[Information Gain]]. If we have a high [[Information Gain]], that means that our decision was very good and it lowered the [[Entropy]] of our sets. 

---
# [[Regression Tree]]s
[[Regression Tree]]s return real valued numbers. We take some [[Summary Statistic]] at a leaf node, and obtain a real number as a result.

---
