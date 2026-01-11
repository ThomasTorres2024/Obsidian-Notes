---
title: Rank k Perturbation
tags:
draft:
---
# [[Rank k Perturbation]]

We build off of the back of a [[Rank 1 Perturbation]]. 

We want to generalize this result to any $u,v \in \mathbb{F}^{n \times k}$, where $\text{rk}(u)=\text{rk}(v)=k$. The resulting product of these matrices $uv^H$ will be of rank $k$ as well. 

From this we obtain a [[Rank k Perturbation]] of a matrix.

We are interested in the inverse of the following matrix: 
$$(I_n-uv^H)^{-1}$$
It turns out we can find this result by finding the inverse of a $k \times k$ matrix instead, though $uv^H$ is certainly of size $n \times n$. We want to show that the following is an inverse:
$$(I_n-uv^H)^{-1} = I+u(I_k-v^Hu)v^H$$
We can verify that this expression is a legitimate inverse:
$$(I_n-uv^H)^{-1}(I_n-uv^H)=I-uv^H+(I-uv^H)u(I_k-v^Hu)^{-1}v^H$$
$$=I-uv^H+(u-uv^Hu)(I_k-v^Hu)^{-1}v^H$$
$$=I-uv^H+u(I-v^Hu)(I_k-v^Hu)^{-1}v^H$$
$$=I-uv^H+uI_kv^H=I$$
