When we train a well, we want to ensure that we can have a train-test split. We want to have some data specifically for training our model, and some data which we can use to verify that our training good. Our data needs to be [[Generalizeable]], meaning that we are not just memorizing and [[Overfitting]] on our data. 

One solution we have is to partition our data sets into "blocks". We then use a larger number, 80%-90% to train our model, and then the remaining 10% to test that our training was correct. Cross validation allows us to do two nice things. We can select our models such that they optimize our [[hyperparameters]] of our model (for instance in [[KNN]] this would be $k$), or [[evaluation]] of a model which gives us how good our models are compared to each other. We compare their [[confidence intervals]] and their means, and see if they overlap. The overlapping models are not different in a statistically significant. We take one such model and use it, which is how we can obtain a model with the ideal hyperparameters, because remember we are optimizing our function for its test score.

![[Pasted image 20250917134918.png]]
In [[Cross Validation]] we partition our data into an array. We consider a fold, the $i$th fold and save it for testing, and train our model on the other remaining $n-1$ segments of data. We then test is on the block and compute our metrics. We complete this process for all entries. In turn, our algorithm here is quite an expensive one. We want to limit our segments to small amounts. 

We can also use [[Cross Validation]] to compare algorithms, and the algorithm that performs the best are the algorithm(s) which have the same confidence interval. We don't care about the [[mean]] of a model's performance.

---
# Parameter Tuning in Cross Validation
We can use cross validation in order to find the the regularization term for the test set. But, we don't have access to the test set, so we can obtain it by performing [[Cross Validation]] on our training set. Whichever parameter fed into our function works best is selected. Thus, we are adding another level on top of cross validation where we need to find another $k$ value. Each corresponding value of $k$ gets trained, and we are doing $n$ folds per $k$ value, so we see another very high algorithmic complexity algorithm.

When we are done, we do another report on each model trained on each individual $k$ value, and get the confidence interval of its performance. We only train [[regularization]] this way, since if we have more than 1 parameter, we have to search over a grid of values which are even more expensive. 

---
# Nested [[Cross Validation]]
Nested cross validation makes use evaluation and tuning. We first tune our parameters until we get a decent parameter. We can then evaluate our algorithm on the outer loop. The algorithm we are also evaluating here includes the algorithm for evaluating our turning parameters. 

### Ideal Model
If we want to find the ideal model we make use of the [[parameter tuning]] part of this. We don't need to do the evaluation on the outside since we just want the model. 

---
# [[Cross Validation]] and Imbalanced Datasets 
If we have a set that is not balanced, then we can take the minority points and be sure to distribute them evenly into each fold, because the presence of these points is so small. 

---
# Tips for [[Cross Validation]]
If training is very expensive, we can skip using CV for regularization just to get the parameter. We can also reduce fold count as well, from 10 folds to 5, and some people even do 3. Also, it is important to note that a parameter which performs really well for some small set of the data might not generalize well to the whole set.