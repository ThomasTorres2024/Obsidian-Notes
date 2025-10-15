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




