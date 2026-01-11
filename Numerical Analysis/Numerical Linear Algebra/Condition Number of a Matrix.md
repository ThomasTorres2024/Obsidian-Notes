---
title: Condition Number of a Matrix
tags:
draft: "False"
---
# Condition Number of a Matrix
The product $\|A\| \cdot \|A^{-1}\|$ occurs frequently and is given a name, the [[Condition Number of a Matrix]], with an arbitrary [[Matrix Norms]]:
$$\kappa(A)=\|A\|\cdot \|A^{-1}\|$$
If $\kappa(A)$ is small, then we can say that the [[Condition Number]] is [[Well-Conditioned]], however, if it is large $\kappa(A)$ is large then it is [[Ill-Conditioned]]. If $A$ is not invertible, we sometimes write that:
$$\kappa(A)=\infty$$
If we use the [[Euclidean Norm]] then it follows that:
$$\kappa(A)=\frac{\sigma_{\text{max}}}{\sigma_{\text{min}}}$$
We can also think of this ratio as the Eccentricity of a hype ellipse. 

For rectangular matrices $A \in \mathbb{C}^{m \times n}$ the [[Condition Number]] of the matrix is defined in terms of the [[Moore-Penrose Pseudo Inverse]]:
$$\kappa(A)=\|A\| \cdot \|A^\dagger\|$$
If we are working in the context of [[Least Squares]], we tend to use the [[Euclidean Norm]], so we would express our result for $A$ where $m \geq n$ and the [[Rank]] of $\text{rk}(A)=n$, so:
$$\kappa = \frac{\sigma_{1}}{ \sigma_{n}}$$
