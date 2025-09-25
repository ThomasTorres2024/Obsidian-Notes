
[[K-means]] often fails on specialized data, for instance spiral data. We start with each point as its own cluster. We find the nearest points to a cluster, and we keep repeating this process until we have a single cluster. After we add everything we in we make some final set of detachments from it.

We completely fail at some types of data, sometimes where data where [[K-means]] is quite good. 

We can construct [[Dendrogram]]s to visualize our [[Hierarchical Agglomerative Clustering]]. This is a form of [[Hierarchical Clustering]]. We can tune our number of clusters for the number of dendrograms. 

We are allowed to choose our own distance metric for this again, [[Manhattan Distance]], [[Euclidean]], [[Cosine Similarity]], etc. 