[[PCA]] is an algorithm that reorders an [[Eigen Value Decomposition]] of our dataset. We choose $\max{\lambda_{i}}$ to be the first entry in the matrix $\wedge$ of $A=X\wedge X^H$. It turns out that this eigen vector maximizes our total variance. We end up just removing lower dimensional data, and only worrying about the high level data. 

Approach:
We want te ceter of the data. We want the covariance matrix. We then do an eigen decomposition on the covariance, and sort the eigenvectors by eigen values in decreasing order. We can use $V$ as our projection matrix. The larger our Eigen value, the more important our component. The eigen value that corresponds to the highest [[Variance]], which is why we sort our data in such a way. 

All of our eigen values are guaranteed to be positive semidefinite. For dimension reduction, ignore eigen vectors associated with smaller eigen values. 1st dimension likely explains the most amount of variance within our dataset. The more and more eigen values we include, the more variance we incur. 

---
# Tradeoffs 
There is no optimization. There is also a straight forward interpretation, very simple and nice to work with. We also fail to preserve local neighborhoods. For instance, in the MNIST dataset, our clusters for our data differ significantly if we use a modified PCA optimization method known as PACMAP. In the example for this in PaCMAP, we are able to much better preserve the structure of our data 

PCA was targeted for the technolgoy of its time. 