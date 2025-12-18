#### Definition
Model Selection is used for selecting a model out of a set of different models which should be the best. We need to look at the different models produced from our data, and determine which is the best by using [[Evaluation Metrics]] of our specific models. 

We typically like to compute the mean standard deviation, and other typical test statistics on our model. 
#### Motivation
We want to find models which reduce the overall [[Overfitting]] of our data set, and so that the models tend to be more [[Generalizeable]] to other datasets. In other words we want to learn the underlying pattern more. 

The way we go about determining the ideal parameters for our model is by using a technique like Grid Search or Random search. This part is known as "Hyperparameter tuning". 

# [[Overfitting]] and [[Underfitting]]
Overfitting refers to when a model is too complicated to try and perfectly match the underlying data by essentially memorizing it, and thereby the generalization becomes quite poor. Underfitting refers to when a constructed model is too simple to replicate the underlying structure of the data.

# [[training set]], [[validation set]], [[test set]]
The train, test, and validation split of a dataset tries to isolate a portion of the original data that we will use to verify that our training has performed well and that our model can generalize to other datasets involving the same variables quite well. We isolate a test set at the very end so we can evaluate our model after training it to see how it performs compared to other models. 

We can use a validation set to find the best hyperparameters and then find the best model out of a set of models. This is important for $k$ fold [[Cross Validation]] and [[Stratified Cross-Validation]]. 

---
# Cross Validation

Cross validation, given $k$, takes the dataset and makes $k$ even partitions of the dataset. We then let each partition take a turn at being the [[validation set]], and then train the others on the remaining $k-1$ folds. When then determine the models performance given the hyperparameters we initially fed it, by averaging its performance across all of the $k$ iterations. 

![[Pasted image 20251024113755.png]]

A variation of [[Cross Validation]] is known as [[Stratified Cross-Validation]], which performs the same operation, except that the partitions of the train set try to preserve the same class distribution in each sample when our data is not evenly distributed. 

We also have [[Leave One Out Cross Validation]], which is an extreme version of [[Cross Validation]], where we train on $n-1$ datapoints, and reserve 1 point $n$ to test on. This is particularly effective if $n$ is somewhat small, like $\leq 1000$, but if we have several thousand then this idea is not reasonable.

We also have [[Leave P Out Cross Validation]], which is the same idea but instead of leaving out $1$, we leave out $p$  many points where $p$ is a small value. 

Once we have found our optimal hyperparameters from repeated [[Cross Validation]] testing, we can train our model on all of the train set, and then perform a test with the [[test set]] to obtain the final performance estimate:
![[Pasted image 20251024114332.png]]

Another way that we can prevent [[Overfitting]] is by normalizing our data. Another thing which helps our algorithms converge and perform better is by normalizing our data. For instance, we may want to constrain the range of the values of our data, and apply different ways of scaling like by the [[mean]] or by a [[Z-score]]. There are other methods as well that might be able to clean up redundancies, but overall by normalizing our data we ensure that our data is closer to ideal and more usable for our models, therefore our resulting models should be much better.

--- 
# Summary of Above Strategies:

![[Pasted image 20251024121003.png]] 