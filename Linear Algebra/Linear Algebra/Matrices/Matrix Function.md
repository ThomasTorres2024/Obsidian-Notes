---
title: Matrix Function
tags:
  - LinearAlgebra
---
# Matrix Function Definition
There are many possible ways to define [[Matrix Function]]s, here we will look for functions $f:\mathbb{R}^{n \times n}\to \mathbb{R}^{n\times n}$, using the definition of the [[Matrix]]'s spectral form ([[Spectral Theorem]]). 

We define the following [[Linear Transformation]] $f$:
$$f(A)= \sum_{i=1}^n f(\alpha_{i} )E_{i}  $$
Where we simply map the [[Eigen Value]] to a new value where each $\alpha_{i}$ is an eigen value. 

One such example is the square root function:
$$\sqrt{ A } = \sum_{j} \sqrt{ \alpha_{j} }E_{j} $$
Here $\sqrt{ A }$ must be [[positive semidefinite]] and also $(\sqrt{A })^2=A$ in order to uniquely satisfy the definition for acting as the square root of a matrix (Also this idea is incredibly obvious if we consider the [[Polar Decomposition]]). 