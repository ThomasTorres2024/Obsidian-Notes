---
title: Adaboost
draft: "false"
tags:
---
# Adaboost

A particularly important boosting algorithm from 1995. 

One of the of the most famous algorithms for boosting. We begin by taking some kind of partition, and associating it with something in classification, and then we take another one based on what we got wrong, what we got wrong we weight higher, and then we do the same thing iteratively until we have a higher decision boundary overall. This is the training procedure that I described above essentially.

Some of the weak learners we use are partitions are decision stumps (decision trees that only split on a single feature ), or linear decision boundaries, which when combined produces a nice decision boundary that isn't overly complicated due to the conditions of our learners. 

We don't really overfit because of the unique features of Adaboost due to the fact that we use weak classifiers so we can't get very detailed decision boundaries, limiting our number of classifiers limits overfitting, and type of classifiers does that. 
# Algorithm For Adaboosting

Given training set $X=\{(x_{1},y_{1})\cdots(x_{m},y_{m})\}$ 
* each $y_{i} \in \{-1,+1\}$ 
* for $t \in \{1,2,3,\cdots,T \}$
	* construction distribution $D_{t}$ on $\{1,\cdots,m \}$ (I believe in this stage, we are re-evaluating the weights of our data, where misclassified points gain a higher weight)
	* Compute weak classifier $h_{t}:X\to\{-1,+1 \}$
	* $h_{t}$ has the small error, $\epsilon_{t}$ on $D_{t}$, and is given by the probability of misclassifying a datapoint in $D_{t}$ ($e_{t}=\mathbb{P}[h_{t}(x_{i})\neq y_{i})]$
* Lastly output the final classifier $H_{final}$

We can construction our distributions of our data each time by the following algorithm. Our goal is to weigh the data points that were misclassified as higher. 

#### Algorithm (Constructing $D_{t}$)
$D_{1}(i)=1/m$ (Initialize all weights to being equally probable)
* After at least one pass, we have some previous $D_{t}$, so we can now use this information to compute $D_{t+1}$ iteratively. 
* $$D_{t+1}(i)=\frac{D_{t}(i)}{Z_{t}}\times \begin{cases} e^{-\alpha_{t}} & \text{ if }y_{i} \neq h_{t}(x_{i})\\e^{\alpha_{t}} & \text{ if }y_{i}=h_{t}(x_{i}) \end{cases}=\frac{D_{t}(i)\exp(-\alpha_{t}y_{i}h_{t}(x_{i}))}{Z_{t}}$$
* Intuitively this above step means, give a higher weight to misclassified points, hence the positive $\alpha_{t}$, and the lower points aren't as important for following iterations so we opt for an $-\alpha_{t}$ in the exponent to weigh correctly classified points less. Note also that $Z_{t}$ is a positive normalization constant
* Also $\alpha_{t}=\frac{1}{2}\ln\left(\frac{1-\epsilon_{t}}{\epsilon_{t}}\right)$
Our final classifier makes use of the constants we just calculated, $\alpha_{t}$, so that is how we get our final weights:
$$H_{final}(x)=\text{sign}\left( \sum_{t=1}^T \alpha_{t}h_{t}(x) \right)$$
Here is a nice way to put it without all my exposition:
![[Pasted image 20251023010531.png]]

Here is some actual code for it:
```python
# generate toy dataset
np.random.seed(42)
X = np.random.randn(300, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)
# train AdaBoost
clf = AdaBoostClassifier(
DecisionTreeClassifier(max_depth=1),
n_estimators=100
)
clf.fit(X, y)
```

An important feature of Adaboost is that it tends to have a pretty good test error that decreases even far after the fact that its train error has gone way down. Adaboost and its structure is particularly resistant to overfitting. 

# Advantages and Disadvantages 

Very fast simple easy to code, no hyperparameters to tune other than $T$, the number of models. Flexible, we can use any weak learner, like decision surfaces (linear), stumps, low depth binary trees. It is very easy to implement. 

Our performance depends on data and weak learners, so little data means worse results, noisy data can mean worse results since we amplify the noise. 

We can fail if too weak base learners causing underfitting, or strong base learners causing overfitting, we are very susceptible to noise here, we reweight incorrect data positively so this in turn increases the importance of the noise

We have gradient boosting algorithms as well on top of this that are more modern and industry standard like XGBoost, LghtGBM, and CatBoost. 