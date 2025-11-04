Raw Notes 9/25/25

Modern data is extremely high dimensional. Take a single image, which is a 224x224 RGB object, which has $\geq 150$ dimensions. We are working with extremely high dimensional spaces. 

We can't examine all of the dimensions of our data, and we want to be able to bring them down to a lower, more comprehensible dimension. We want to understand how things are transformed across dimensions and how things are altered by that transformation. We want to reduce the number of dimensions of our dataset while maintaining our structure. 

A vast majority of algorithms except in the last few years to tend to lose a significant amount of information and the overall structure of our data. If we have a new dataset, we want to develop some intuitions for what our dataset is doing. We want to know the distribution of data, which allows us to better apply models and to attack it.

Being able to dimensionality reduction is very hard. 

---
This is an [[unsupervised]] method. We don't have anything we are testing against. We are searching for a [[latent structure]], or a nice potentially low dimensional structure from a high-dimensional data. Our goal is to maintain our structure.

We have basic things like feature reduction and non-linear transformation. We also have [[PCA]],[[Kernel PCA]], [[t-SNE]], [[autoencoders]], and different [[Matrix Factorizations]]. 

Different methods tend to preserve different properties of our datasets. The clusteredness of one set is one such thing we want to preserve. We may want to preserve distances, or neighborhood structure which implicitly preserves distances, among others. 

We may want to take our columns and reduce the amounts of redundancy. This is especially true in trees. We typically want to do some kind of [[preprocessing]] on our dataset. It turns out also if we have 3,000 columns, and 2 are independent and the other 2998 are dependent, then our 2 independent columns can be used to represent our se and improve the model.

We are also very interested in [[Data Compression]] in machine learning, it is especially important for embedded systems. 

---
# Projections
We want to find the orthogonal distance between a group of points 

Mathematically we are finding points on the line such that we minimize the distance to our points given that the line we are measuring from is orthogonal. We can project our data onto any type of line. 

We want to maintain the spread of our data. Our main goal for a projection is to maximize the variance of our dataset. We define variance by:
$$\sigma^2 = \frac{1}{n} \sum_{i=1}^n (x_{i}-\mu)^2 $$
Intuitively this is a calculation of the mean squared distance from any point in our dataset to our line. 

Covariance Matrix:
$$\Sigma = \begin{bmatrix} \text{var}(i) & \text{cov}(i,j)\\ \text{cov}(j,i) & \text{var}(i) \end{bmatrix} $$
Notice that $\Sigma \in \mathbb{R}^{m \times m}$ and $\Sigma^T=\Sigma$. We can think of $\Sigma$ as packaging for the slopes of our values. 

---
# [[Random Forests]] 
[[Random Forests]] are based around the [[Decision Tree]] algorithm, where our goal is to produce a group of [[Decision Tree]]s, this makes up a [[Decision Forest]]. We take the average of the results of our trees, and we get an ensemble result. The [[Decision Forrest]] is a black box model. We lose [[Interpretability]] as we add more trees. 

The way we train [[Random Forests]] is by [[bagging]], we take a subset of the $n$ points, and we sample with replacement to grow a tree from them. 

As a common example for [[Decision Tree]]s we ask the question, will a custom wait for a restaurant as a pretty typical problem. 

The decision forest starts by choosing $m$ features randomly, and then evaluates the splitting criteria on the trees, and run the same algorithm essentially. 

With bootstrap resamples. There is no pruning at all on these trees. 

Random forests are very nonlinear as well, very predictive.

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

---
# [[Dimension Reduction]] Techniques 

t-SNE 

[[PaCMAP]] tries to preserve both the global and local structures of the dataset. We try to preserve both at the same time, and our way of doing it by first identifying the global structure, and then finding the local structure within it. We have a loss term for closer neighbors, and for further neighbors. The neighbors loss is bigger if the terms are closer, and the further loss is larger if points are closer. 

[[LocalMap]] our goal is to make [[Dimension Reduction]] better in 2d by not moving points to be too close and to reduce it. We iteratively compare 2d and nd distance and then make adjustments based on this fact. 

[[UMap]]
Tries to keep the $k$ nearest neighbors of a point together throughout both. [[UMap]] is way better than [[t-SNE]] in runtime, and does a better job at preserving distances

[[ParamRepulsor]] 

[[InfoNC-tSNE]] improvement on [[t-SNE]].  Uses loss function of [[InfoNCE]] 

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

---
# Logistic Regression (Alvarez Slides)
We want to be able to model the relationship between variables using regression. It is the same idea as [[Linear Regression]] where we try and find the relationship between two variables, an input and a target variable, for instance:
$$y=mx+c$$
Where $x$ is the input, $M$ is the matrix of weights, and $Y$ is our output/prediction values. Our inputs and $y$ are fixed. Our goal of [[Linear Regression]] is to find the best weight matrix. In this case we assume that there is a linear relationship between the input and the target. 

For instance if we have have house size vs house prices, we could assume a linear assumption because house size grows with respective to house prices. We want to predict a concrete number. 

[[Logistic Regression]] is a similar idea, but we want to be able to predict a probability instead of a real number. Say we have two categories, green apples versus red apples. We want to find the decision surface that differentiates between two different classes. We are interested in lienr classifi4rs specifially. 

Thes asre simple models that give us boudns between 2 types of data. Given a dataset we want to learn a decision bondary between 2 classes. Based on the features of our input we want to be able toc ategorize if our outputs will go to 1 or -1. We can go from this dataset of X,y to a learning algorithm. 

we need some way of esuring that our approximation is a good one, so we want to find the best values of $M$ for the best prediction of our data. 
Logistic regression forms the [[decision boundary]] that is linear between 2 groups of data.

The sign function is a very simple function that classifies our data. We don't know what happens if $x=y$, but we wan keep the two halves separate. 

If $w^Tx>0$ then we have a class 1 or + class, and if $w^Tx<0$ then we have a class 2 or $-$ class. Since we are looking for decision boundaries we are looking for functions of the form $b=w_{1}x_{1}+w_{2}x_{2}$. 

THe weight matrix is initialied to random variables to begin with. 

During the learning process we initialzie a random line through a binary dataset, and continue iteratios of learning until te line full bisects the two lines in an ideal set. We need to find a balance here between [[Overfitting]] and also [[Underfitting]] from our training set. Each iteration corresponds to a training cycle and then passing the back propagation back at each time. 

#### [[Binary Classifier]]
A binary classifier takes a datast $D$ which contains $x$ vectors, and the outputs for these values are either $-1$ or $1$. Here, we are modeling the tendency for a value of probability.

We feed our results into the sigmoid function, here we are predicting probability, so we have a prediction that is between 0-1, so the probability. If the score is close 1 confident about model, if the model is 1/2 not confident at all. 

Here we express 

# Maximum Likelihood Estimation
How do we find the best values of $W$? To find the best values of $W$, we need to sue a stats function to estimate parameters of $W$. How do we verify this is the best weight function after w have fed it through? If the score is high of our MLE then we can assume we are in a good position. 

If the product of te probability estimators are close to 1 then we re good, we have the arg min that we have the negative likelihood estimation which can be fond using the negative log likelihood as well. 

The lost function is always convex, it always give us the best global minimum, and need to use gradient descent or other second order methods 

---
# 10/20/25 - Gradient Descent

Our intuition for this is to compute the gradient and take steps in the negative direction of the gradient such that each time we get closer and closer to a minimum along the graph, as eventually we expected to hit a 0. 

We can determine if the hessian matrix is PD or ND at $x^*$, if it is PD then it is a local minima, if it is ND it is a local maxima of the function, which corresponds respectively to positive and negative eigen values of $H$. 

This is an iterative method where each time we take some step forward each time. in t-SNE and other modern function we take iterative steps to optimizing our solution, which is a huge idea. Gradient descent is used to compute minimas. We start at some random point along our surface, and then invert the gradients sign and follow that path down and continue. 

The hard part about this is the learning rate, which is critical. This is a [[hyperparameters]] of [[Gradient Descent]]. This is known as the [[learning rate]], how many steps will we end up taking? 

We begin by letting $t=0$ and using an iterative formula with randomly initialized weights, $w$:
$$w^{(t+1)}=w^{(t)}-\nu \cdot \nabla_{w}f(w^T)$$
If the learning rate is too small then we have an overly slow convergence, step sizes are absolutely massive for the conjugate gradient method. If our size is too large, there is a good chance that we overshoot and end up going way too far. Overshooting with a neural net will produce absolute nonsense within a few epochs (traversals through the dataset). 

# Stochastic Gradient Descent
# Stochastic Gradient Descent with Momentum 
The idea is if I walked down here already and consider this and I have some momentum here I've been here already and moved this way, then our gradient would be affected by that. The intuition is to think of a ball falling down on a gradient, which has some momentum term wile it falls.
# Adam Optimizer 
Variation of SGD with Momentum. The adam optimizer is commonly used. Sometimes if SGD sucks, then we should use Adam. 
# [[Gradient Descent]] and Machine Learning
Optimizing a [[loss functions]] is a huge problem in machine learning. We can't do it directly, so do it with this method iteratively. There are a lot of gradient based optimal solutions which can find by performing gradient descent. 

Using gradient descent runs into functions which are very complex with many saddple points, local maxxes, and local mins. Real data also causes rounding error and issues. THus we are tryinh yo minimize over an unfriendly function. 

Batch Gradient Descent 
Instead of doing a gradient descent over the whole dataset, we do it by sampling the dataset, and taking a step based on that sample. The idea is we can do 1 epoch with many more gradient descents, instead of optimxing for one item. 

---
# [[Boosting]]
10/22/25
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

Another point of contrast, compared to [[Random Forests]] and [[bagging]] methods, we do not evenly weight the models we produced, whereas both of these models tend to group up the weights evenly. For instance if we are making use of decision stumps, we weigh some stumps over others, 
#### Adaboost

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

---
# Bagging 
[[bagging]] is an [[ensemble method]] which trains many weak learners in parallel, and generally tends to produce very good results. 

Produced in 1996, train man models on random susbets of the data, we want to reduce variance an ovefitting, take collective vote of everything, should be faster bc we can do models in paralell, we determine by classification voting, mean/medan if regression or 

[[Bootstrapping]]
If we have a dataset $D$, we create $n$ boot strap samples, the standard way to do this si that each amount is of size $n$, same as dataset, but we same with replacement we may have doubles or more ntries or missing potentially, which is how we go about forming the data to train our weak llearners

we infer things via voting 

[[Random Forests]] is a similar idea but we are taking random features of the data and random feature selection
with random forests instead of taking all features, we take a subset, because decision trees split on features, and if we want a good variety leave out some features, especially if we use a greedy method like spliting on information 

similarly we aggregate via majority vote ehre too 

we can use 

Final remarks with random forests and bagging, very performant, robust to outliers, we can create all decision trees at once

limitations sparse data is really bad for this tree, 

Create bootstrap samples 