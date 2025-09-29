Raw Notes 9/25/25

Modern data is extremely high dimensional. Take a single image, which is a 224x224 RGB object, which has $\geq 150$ dimensions. We are working with extremely high dimensional spaces. 

We can't examine all of the dimensions of our data, and we want to be able to bring them down to a lower, more comprehensible dimension. We want to understand how things are transformed across dimensions and how things are altered by that transformation. We want to reduce the number of dimensions of our dataset while maintaining our structure. 

A vast majority of algorithms except in the last few years to tend to lose a significant amount of information and the overall structure of our data. If we have a new dataset, we want to develop some intuitions for what our dataset is doing. We want to know the distribution of data, which allows us to better apply models and to attack it.

Being able to dimensionality reduction is very hard. 

---
This is an [[unsupervised]] method. We don't have anything we are testing against. We are searching for a [[latent structure]], or a nice potentially low dimensional structure from a high-dimensional data. Our goal is to main our structure.

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
# Methods 