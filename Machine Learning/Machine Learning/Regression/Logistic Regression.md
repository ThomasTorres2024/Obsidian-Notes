---
title: Logistic Regression
tags:
draft: "false"
---
# Logistic Regression
Logistic Regression tries to compute a linear [[decision boundary]]. We can take the formulation of a typical least squares problem where we are trying to solve for $W$ and $\vec{b}$ given the results of each column $\vec{y}$, and the :
$$\vec{y}=WX+\vec{b}$$
Let us denote the two categories that $\vec{y}$ encompasses are $+$ and $-$. We want every $+$ to inhabit every value above the decision boundary, and every $-$ underneath the decision boundary. We want to be able to determine which side corresponds to which class, and we want to be able to classify new points based on the boundary that we generate. 

We can determine which side of the decision surface we are on by computing, for $\vec{x} \in X$, $W^T\vec{x}$. If $W^T\vec{x} >0$, then we can conclude that $y$ is of the $+$ class, and likewise if $W^T\vec{x}<0$ then we can conclude that $y$ is of the $-$ class. 

In turn, we want to take in a dataset $X$, that is able to generate $W$ and $b$ such that we have a surface which can classify items on the trainset above some threshold of error. 

Another way that we can think of our $W^Tx$ and its sign is by using $\text{sign}(W^Tx)$, which constricts our output to being $0$ if $W^Tx=0$, $1$ if $W^Tx>0$ and $-1$ if $W^Tx<0$. 

In turn we can describe this as a function given by $h(x)$, which is our prediction function that maps elements of a dataset $X$ to what class it predicts they belong to:
![[Pasted image 20251015164017.png]]

Generally the types of linear surfaces we are trying to finda re known as hyperplanes, which generalize the notion of lines, and planes, into higher dimensional objects to the $n$th degree.

---
# Learning Decision Surfaces
The process of determining the actual decision surface initializes a line with random parameters through the dataset, and then performs back propagation to recompute the weight matrix, and iteratively performs this process until we have reached a satisfactory score on our [[loss functions]]. 

To see how we could evaluate the score of a model , consider the following dataset:
$$A=\begin{bmatrix} 1& 0 & 0\\ 1 & 0 & 1\\ 1 & 1 & 0\\ 1 & 1 & 1 \end{bmatrix}$$
which corresponds to the results $y=\begin{bmatrix} -1 & -1 & -1 & 1 \end{bmatrix}^T$. It turns out if $w=\begin{bmatrix} -1.5 & 1 & 1 \end{bmatrix}^T$, then the resulting $Aw$ yields $y$:
$$Aw=y \iff y^T=wA^T$$
If we compute each entry, we can clearly observe that this is model works for all of the points. 

---
# Logistic Regression Formally
Logistic regression models the probability of an output given an input. Unlike [[Linear Regression]], we are not trying to model a function defined over all reals, but to estimate probabilities.

Let $\mathcal{D}=\large\{ (x_{1},y_{y}),\cdots,(x_{n},y_{n}) \large\}$ be the dataset we will try to create a [[decision boundary]] over. Let $x_{i} \in \mathbb{R}^d,$ and let each $y_{i} \in \{-1,+1\}$. This is just formally saying that we have 2 classes, and have a dataset of $n$ rows with $d$ features that we are trying to iterate over. 

[[Logistic Regression]] is a [[Linear Classifiers]] with a non-linear [[activation function]].  Instead of using the sign function we opt to use the sigmoid or logistic function:
$$\sigma(x)=\frac{1}{1+e^{-x}}=\frac{e^x}{e^x+1}$$
The [[Logistic Curve]] maps $\mathbb{R} \to [0,1]$. The function is both continuous and differentiable, so it is very important to us. 

Remember when we expressed $h(x)$ in terms of the sign function. We want to do something similar here, but instead express it in terms of $\sigma(w^Tx)$. We can use this function to give us an estimation for how likely it is that our $x$ belongs to class $+1$ or $-1$:
$$h(x)=\sigma(w^Tx)=\frac{1}{1+\exp(-w^Tx)}$$
We can also determine the Probability of class $+1$ and $-1$ explicitly using this function:
$$\mathbb{P}[y=+1|x]=\sigma(w^Tx)$$
$$\mathbb{P}[y=-1|x]=1-\sigma(w^Tx)$$
$$=\frac{1+\exp(-w^Tx)}{1+\exp(-w^Tx)}-\frac{1}{1+\exp(-w^Tx)}=\frac{\exp(-w^Tx)}{1+\exp(-w^Tx)}=\frac{1}{\exp(w^Tx)+1}=\sigma(w^Tx)$$
Also note that: $\sigma(w^Tx)=\sigma(-w^Tx)$. 

In summary, here is a graphic that describes what we are performing:
![[Pasted image 20251015172552.png]]

---
# Solving Logistic Regression
We can use [[Maximum Likelihood Estimation]] to determine the weight matrix $w$. MLE is commonly used to determine parameters of an observed dataset $D$ throughout statistics and machine learning. We have the data set $X$ which is composed of $n$ features such that:
$$X=\sum_{i=1}^n x_{i}$$
For the sake of simplifying this expression, we assume that each $x_{i}$ is independent of one another. Let $L$ be a function of $w$, and estimate the probability that we have seen the data from $X$. Since we independent, using the definition of a joint probability mass function we can write that:
$$\mathcal{L}(w)=\mathbb{P}[x_{1},w]\cdot \mathbb{P}[x_{2},w]\cdot \mathbb{P}[x_{3},w]\cdot \dots \cdot \mathbb{P}[x_{n},w]=\prod_{i=1}^n \mathbb{P}[x_{i},w]$$
We thus want to be able to find the $w$ that maximizes $\mathcal{L}(w)$:
$$w^*=\arg \max_{w} \mathcal{L}(w)$$
We want to take conditional data likelihood and and express our problem in terms of that:
$$\mathcal{L}(w)=\prod_{i=1}^n \mathbb{P}[y_{i},x_{i}]$$
Thus:
$$w^* = \arg \max_{w} \prod_{i=1}^n \mathbb{P}[y_{i}|x_{i};w]$$
$$=\arg \max_{w} \left( \prod_{i=1}^n \frac{1}{1+e^{-y(i)w^Tx(i)}} \right)$$
$$=\arg \max_{w} \text{ }\sum_{i=1}^n \log  \left( \frac{1}{1+e^{-y(i)w^Tx(i)}} \right)$$
$$=\arg \max_{w} \text{ } -\sum_{i=1}^n\log \left(1+e^{-y(i)w^Tx(i)}\right)$$
$$=\arg \min_{w} \text{ } \frac{1}{n} \sum_{i=1}^n \log  \left({1+e^{-y(i)w^Tx(i)}} \right)$$This term is equal to $w^*$, and is also known as [[negative log likelihood]]:
$$w^*=\arg \min_{w} \text{ } \frac{1}{n} \sum_{i=1}^n \log  \left({1+e^{-y(i)w^Tx(i)}} \right)$$
There is no closed form solution of this function, however the loss function is a [[Convex Function]], which means that its local minimums re global minimums. We can use [[Gradient Descent]] in order to find $w^*$. 

In turn now that we have a way to compute and solve for $w^*$, we now know $h(x)$, and so we can classify new points. we can write that:
$$\mathbb{P}[+1|x] \geq 0.5 \implies \text{ x is +1}$$
$$\mathbb{P}[+1|x] < 0.5 \implies \text{ x is -1}$$
Our boundaries have the following form:
![[Pasted image 20251015191607.png]]

### Example Of a Boundary 
![[Pasted image 20251015191638.png]]
# Properties of Logistic Regression
Lost function is still convex, so we have a global minimum. We can use [[regularization]] to avoid [[Overfitting]], so we are "Robust to Overfitting". Our weights allow us to ascribe variance to certain features and is important for [[feature importance]]. Lastly, the decision boundary of our function is still linear.


---
# Other Names 
Logistic regression goes by other names, like [[neuron]]s or [[perceptron]]s as well. 























