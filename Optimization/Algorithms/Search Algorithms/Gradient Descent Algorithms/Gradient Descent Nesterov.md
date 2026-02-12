---
title: Gradient Descent Nesterov
draft: "False"
tags:
---
# Gradient Descent Nesterov/Adagrad
Nesterov's descent is a modification of the [[Optimization/Algorithms/Search Algorithms/Gradient Descent Algorithms/Gradient Descent]] algorithm that takes us back. Like the momentum idea, it involves 3 steps:

$$x_{k+1}=x_{k} + \beta(x_{k}-x_{k+1})-s\nabla f(x_{k}+ \beta(x_{k}-x_{k-1}))$$
We can re-write this in two steps for better clarity:
$$x_{k+1}=y_{k}-s\nabla f(y_{k})$$
$$y_{k+1}=x_{k+1}+\beta(x_{k}-x_{k+1})$$
This is a second order method, since it involves 3 different steps. We want to be able to express this as 2 first step equations. We can repeat the same process used for [[Gradient Descent with Momentum]], and it turns out that the optimal parameters for $s$ and $\beta$ happen to be the exact same as with momentum, which is to say:
$$S_{\text{optimized}}=\left( \frac{2}{\sqrt{\lambda_{Max}}+\sqrt{\lambda_{Min}+}} \right)^2$$
$$\beta_{\text{optimized}}=\left( \frac{\sqrt{\lambda_{Max}}-\sqrt{\lambda_{Min}+}}{\sqrt{\lambda_{Max}}+\sqrt{\lambda_{Min}+}} \right)^2$$
