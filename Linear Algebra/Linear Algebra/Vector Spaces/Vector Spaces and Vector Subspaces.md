---
title: Vector Spaces
---
# Vector Space Definition

A vector subspace $\mathcal{V}$ is a set which consists of elements known as vectors and satisfies three properties:

- $\mathcal{V}$ is non-empty, meaning it contains at least one item 
- $\mathcal{V}$ is closed under scalar multiplication over the field $\mathbb{F}$ where $\mathbb{F}=\mathbb{C} \text{ or } \mathbb{F}=\mathbb{R}$, which is to say that for $c \in \mathbb{F}$ and $\vec{v} \in \mathcal{V}$ that $\vec{v} \cdot c \in \mathcal{V}$
- $\mathcal{V}$ is closed under vector addition, meaning that for some $\vec{v},\vec{w} \in \mathcal{V}$ then $\vec{v} +\vec{w} \in \mathcal{V}$

More formally we can think of a vector space as a group with an associated addition and scalar multiplication operation over a field. 

All of the properties a vector subspace must satisfy are the folowing:

---

# Linear Independence

Given a set, $S=\{ \vec{s}_{1}, \vec{s}_{2} , \cdots, \vec{s}_{n}  \}$, we can determine if $S$ is linearly independent if there is only one linear combination of elements from $S$ that gives $\vec{0}$, such that each scalar is the zero scalar. That is to say: 

$$\sum_{i=1}^n \alpha_{i} \cdot \vec{s}_{i}=\vec{0} \Longleftrightarrow \alpha_{i}=0$$
If this condition is met, we can call the set $S$ linearly independent. Otherwise, the set is linearly dependent. 

An equivalent condition for linear dependence is if we can express some $\vec{x} \in \mathbb{F}^n$  in more than one linear combination of vectors from $S$. That is to say: 

$$\sum_{i=1}^n \alpha_{i} \cdot \vec{s}_{i}=\vec{x}=\vec{x}+\vec{0}=\sum_{i=1}^n \beta_{i} \vec{s}_{i}=\sum_{i=1}^n(\alpha_{i}+\beta_{i})\cdot \vec{s}_{i}$$
Since the scalars for both vectors at least include one non-zero scalar in their linear combination, having a linearly dependent system implies that we can express any vector in its range an infinite number of ways. 

We can also 