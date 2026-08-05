---
title: Formal Product
tags:
  - LinearAlgebra
draft: "False"
---
# Formal Product

The [[Formal Product]] of two [[Vector Space]]s $V,W$ denoted by $V*W$ is the following set:
$$V*W= \text{span} \{ v * w : v \in V, w \in W \}$$
And there is no relation between the symbols $v,w$. We define that each $(v*w) \in V*W$ is [[Linearly Independent]] from each other, meaning that every vector has no relation to the other vectors, resulting in a ridiculously large [[Vector Space]]. We can convert this into the [[Tensor Product]] by considering standard rules of vector addition and scaling, namely:

$$(v_{1},w_{1})+(v_{1},w_{2})=(v_{1}+v_{2},w_{1}+w_{2})$$
$$\lambda(v,w)=(\lambda v, \lambda w)$$
