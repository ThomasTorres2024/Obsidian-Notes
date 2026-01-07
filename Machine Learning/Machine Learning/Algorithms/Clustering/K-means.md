---
title: K-means
---
# [[K-means]] Introduction
[[K-means]] is an [[unsupervised]] learning algorithm, used for discovering patterns or groups within our data. Sometimes we have labels but we want to do clustering on them. Because this is [[unsupervised]] it will ignore all of the labels since they aren't very relevant. 

Given some data sometimes we want to see if we can observe any trends or groups within our data. Clustering algorithms are good at looking at data and observing [[clusters]], which give us the number of groups or items that fall into a set of categories. Deciding how we can come up with such an algorithm is fairly difficult, especially as cluster shapes changes.

---
# What is clustering and Applications
We have $n$ many operations, and we want to put them into $K$ clusters where everything within the cluster is very similar, and everything outside of it has a low similarity with objects outside of it. $K$ ranges from a few to hundreds. $N$ can be billions. Each observation is a very high dimensional vector, so this is very hard to work with.

This problem is NP hard. Also there is a trade of between how good we can compute a cluster, and how these things tend to cluster. Clustering is still well and alive in use for scientific discovery. Clustering can be used to make our data lower dimensional. If it turns out that we have 2 clusters with 3 features, we can just have a single binary feature of each class. This is important for data-preprocessing. 

---
# Clustering Unlabeled Data 

There is a level of subjectivity within clustering. How we divide our points into clusters is something that makes this a more complicated algorithm. Below we can take the same data and argue the following:
![[Pasted image 20250917153805.png]]

---
# Clustering Typs

### [[Partition Clustering]]
Centroid clustering is observation based. We partition our data set. Each partition has a centroid. If you are the closest to one centroid then you belong to that cluster. Each point has exactly 1 cluster. Each partition is represented by a single centroid. 

![[Pasted image 20250917161902.png]]

#### [[Hierarchical Clustering]]
Defines a tree like structure known as a dendrogram of clusters. We do not need any number of clusters in advance. Very sensitive to the distance metric between clusters.

#### [[Density Based Clustering]]
In regions which are high density, we form clusters that are of arbitrary size. We choose not to label anything outside of these two regions. Very sensitive to sparse or high dimensional data.
![[Pasted image 20250917162141.png]]

#### [[Distribution Based Clustering]]
We make an underlying assumption about the data, maybe that each piece of data belong to Gaussian clusters. Instead of assigning points to a single cluster, you have a probability of being a part of a cluster based on how far you are from each center. Here, we can have wider or tighter distributions:

![[Pasted image 20250917154144.png]]

---
# Distance Metric

Some of our common distance metrics are Manhattan, Euclidean, or cosine similarity:
$$\text{Euclidean Distance Between } (x,y) =d(x,y)=\sqrt{\sum_{i=1}^n(x_{i}-y_{i})^2}$$
$$\text{Manhattan Distance} (x,y) =d(x,y)=\sum_{i=1}^n|x_{i}-y_{i}|$$
$$\text{Cosine Similarity =} \text{ sim}(x,y)=\frac{\vec{x} \cdot \vec{y}}{\| \vec{x} \| \|\vec{y}\|}$$
---
# K-means Algorithm
Very popular and widely used. We are given a dataset of $n$ points and the desired number of clusters, $k$. We essentially want to optimize between the distance from each centroid to the set of points within each respective cluster. Our goal is to make the cluster-distance minimized within each partition of our data. 

We cannot do a brute force solution, we usually do an iteration. We start with $k$ many, and we assign each set of points to a set of [[centroid]]s. We add each to a new one.  We then minimize the distance between our points and centroid, and move the centroid further and further. When our cluster centroids stop moving then we have successfully converged. 

### K-Means Formally
We can formally state our problem here. Given a dataset of observations of $\mathcal{D}=\{\vec{x_{1}},\vec{x_{2}},\cdots,\vec{x_{n}}\}$ where each $\vec{x_{i}} \in \mathbb{R}^d$ and a number of [[clusters]] $K$, we can denote each cluster in our set by $C_{k}$. We have a total of $k$ clusters ranging from $1,\cdots,K$. We can say that if the data point $\vec{x_{i}}$ is in cluster $C_{k}$ that, $i \in C_{k}$. 

We can also see that the set of all clusters unioned would be the set all integers from $1$ to $n$ since each cluster is a set of points:
$$\bigcup_{i=1}^KC_{i}=\{1,2,\cdots, n \}$$
We should also have that no element occurs twice within any cluster. Which is to say that no clusters $i$ and $j$ where $i\neq j$ contain any subset that is not null:
$$C_{i} \cap C_{j} = \varnothing : i\neq j$$
##### Cluster Centroids 
Group representatives are given by $\{\vec{z_{1}},\vec{z_{2}},\cdots,\vec{z_{K}}\}$, and $\vec{z_{i}} \in \mathbb{R}^d$. Each representative, $\vec{z_{i}}$ is a centroid, and thus it is the mean of all observations in the cluster $C_{k}$. Let $r=|C_{i}$. 
$$\vec{z_{i}}=\frac{1}{r}  \sum_{j \in C_{i}} \vec{x_{j}}$$
We want to be able to find $\vec{z_{k}}$ such that we minimize the quantity:
$$\|\vec{x_{i}} - \vec{z_{k}} \| \text{ where } i \in C_{k}$$
We construct a cost function, which overall denotes the sums the sum of squares from each point to its centroid. In other words we compute the squared distance between a centroid and all of its points. Let us denote this function by $J$:
$$J=\text{argmin}(C_{1},\cdots C_{K}) \sum_{k=1}^K \sum_{i \in C_{k}]} \| \vec{x_{i}}-\vec{z_{k}}\|_{2}^2$$
We have two options from here, applying a useless bruteforce search algorithm, or an approximate solution which we can find using an efficient iterative method known as [[Lloyd's Algorithm]],  which makes use of relaxation.
### K-Means [[centroid]] computation algorithm description

```
 initialize k centroids randomly 
  
  while centroids not converged
	assign each point x to its nearest centroid
	recompute all cluster centroids 
	new centroid z_{k} is the mean of all observations in the group Ck
	  
```

* We begin by randomly initializing $K$ different centroids. And we then repeat this next step until our clusters converge to a final value. 
* We loop a condition to force every centroid to converge to 0
	* Assign each $x_{i}$ to its nearest centroid $z_{k}$.
	* Recompute all cluster centroids 
	* Set the new cluster $z_{k}$ to be the mean of all observations in a group $C_{k}$
	
We can break ties by selecting the group that has the smallest index. Empty groups are dropped. The algorithm is said to have fully converged when either group assignments are the same, but we typically stop this process much sooner when improvement falls off. 

We can also choose data points randomly for initial representatives or by using random assignment.

---
# Issues with K-means 
We know that $J$ will decrease with each step. We will get finite convergence this way. Because we randomly initialize our centroids, it is possible that we may converge to different points given different initial centroids. It is also the case that we are not guaranteed to converge to any globally optimal solution, even though we optimize within our classes. 

![[Pasted image 20250917171556.png]]

Results are very dependent upon our initial centroid placement. We also get different results for different values of $K$. Outliers in our data will also seriously mess up our dataset. 

# Fixes and Practical Approach
We can run [[K-means]] multiple times and select the smallest $J$ from our runs. we can also use the elbow method to choose the best $k$ value. We can use k-means++ which has better initialization, or some alternative methods like k-medoids or k-medians. 

## [[Elbow Method]]
The elbow method is also extremely important and useful. We can use it to find the ideal $k4 such that we minimize the total sum of squared distances to centroids. As $k\to \infty$, then $J\to0$, but we want to stop before there. We typically pick the point which resembles the inflection point of the graph before our value tends to stabilize. 

![[Pasted image 20250917171747.png]]

As $k\to\infty$, our centroids will tend to look more and more like our actual points, and eventually we get a distance of $0$ there, but that is completely useless. We are looking for the point of diminishing returns. We are looking for a "kink", a point at which we have a concavity change.