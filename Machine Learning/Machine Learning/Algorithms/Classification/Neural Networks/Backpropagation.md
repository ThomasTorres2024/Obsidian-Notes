---
title: Backpropagation
tags:
draft: "false"
---
# Backpropagation
Recall that the general formula for a neural network is a repeated function composition applied to the input vector of a function:
$$F(x)=F_{n}(F_{n-1}(F_{n-2}(\dots F_{1}(x))))$$
In order to compute the [[Gradients]] of $F(x)$ we need repeated application of the chain rule applied to this expression. 