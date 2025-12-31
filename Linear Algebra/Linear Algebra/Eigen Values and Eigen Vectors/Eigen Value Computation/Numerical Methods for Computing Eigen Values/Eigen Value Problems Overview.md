---
title: Eigen Value Problems Overview
draft: "False"
tags:
---
# Overview 
[[eigen value]] algorithms are interested in either computing a single eigen value, or multiple eigen values. Some algorithms are very good at peeking into the matrix and only getting a few very efficiently, whereas others are very good at extracting all of the eigen values of a matrix efficiently. 

This page is meant to be a summary and organizer of all of the details of the eigen-value algorithms. 

### Methods for Single Eigen Values
1. [[Power Iteration]]
### Methods for Some Eigen Values
1. [[Bisection]]
### Methods for All Eigen Values 
1. [[QR Algorithm With Shifts]]
2. [[QR Algorithm without Shifts]]
3. [[Jacobi Iteration]]

# Horrible Methods for Eigen Value Computation
It goes without saying but never numerically use [[Determinant]]s for computation of anything numerically. If we go about trying to solve eigen-values of $A$ by their definition in $\det(A-\lambda I)$ we run into the fact that this matrix is generally [[ill-conditioned]]. We lose information almost always. 