---
title: LocalMAP
draft:
tags:
---
# Conversion to a Graph
LocalMAP converts a dataset into a graph. The graph contains both positive and negative edges. We can optimize the embedding of the graph by applying forces along the positive and negative edges of the graph. We want to apply attractive and repulsive forces along the graph which result in clusters forming. 

It is easy to misclassify a point and group it with another cluster if an edge is constructed between one point and a point that should not belong to it. If this occurs, [[Dimension Reduction]] algorithms tend to apply positive attractive forces between the two edges which bring them together where they should not. If we have many false positive edges, this behavior applied in total will result in many 

Another pain point for data graphs is a potential lack of negative edges between far points. If there are not enough, then the attractive force tends to pull clusters together. As the dataset increases, the number of negative edges becomes insufficient and less effective typically. 

LocalMAP looks to adjust the graph during dimension reduction. LocalMAP eliminates false-positive edges between nodes on the data graph using a method similar to outlier detection in robust statistics. We also add more negatively weighted edges between nodes, which create crisper cluster boundaries.

Dimension reduction is an unsupervised task. Previous dimension reduction algorithms do not consider readjusting weights along the graph of data. The graph is generally considered to be fixed. Our main idea is to remove outliers that destroy performance. We do not trust each element in the graph as if it were correct. 

Positive attractive forces are applied along the nearest neighbor edges between points which are close in the high dimensional space, and repulsive forces are applied along the FP edges. An NN edge is "preserved" between two different point if the points are placed nearby in the low dimensional embedding. We need a way to discern which NN edges should be maintained, and which should be pruned. One way we can go about this is by taking some arbitrary pair of NNs given by ($i,j$) and examining if "they shayre a greater number of common neighbors" (somehow the higher neighbor count corresponds to more )  then generally we would expect these points, due to the attractive force, to converge to some local neighborhood of points. 

As the scale and size of a dataset increases, the number of repulsive edges in the graph tends to be insufficient. We would hope that there would be enough to apply negative forces such that distinct and separate clusters of data would begin to form. However, since we usually do not have enough in typical DR algorithms, we do not get clusters that are separated nearly as nicely. 

# LocalMAP Finally

LocalMAP tries to correct 2 key issues in older dimension reduction algorithms. We try to remove false positive edges that apply an attractive force, and try to add negative edges that apply a repulsive force since large datasets tend to have more nearest neighbor edges than far pair edges. We handle both of the key insights by doing more "local computation". Both computation 1 and 2 are done in the final stage of of optimization. 

#### Computation 1.) 
LocalMAP adjusts the weights of NN edges dynamically (graph is not fixed). Some of the following principals are applied in reweighting NN edges:
1. Increase weights for NNs that are close in low-dimensional space 
2. Decreased weights for NNs that are far in low dimensional space 
3. Avoid large forces, we want convergence 
4. We want a relatively simple objective function 




##### Computation 2.) 
We "resample FP edges to be local" 

# Algorithm Overview
LocalMAP begins with an embedding provided by PaCMAP which has 3 different pairs in its graph, nearest neighbor pairs, mid near pairs, and further point pairs. 
# Potential Errors
Due to the underlying structure of the LocalMAP algorithm, there is a chance that we hallucinate clusters by adding negative weight edges and forcing things together. We also may reduce the total number of clusters together by pruning the number of edges where a positive force is applied. 