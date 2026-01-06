---
title: CNNs
draft: "false"
tags:
---
# CNN Intro 

Convolutional neural networks are a specific [[Neural Networks]] architecture that makes use of "covolving" over an image, which yields a smaller algorithmic complexity and memory cost. Instead of feeding in each individual pixel into the input layer of the neural network, we want to consider different windows of the image by considering some window size of $m \times m$ being moved across an image. This is the main idea behind a CNN.

When we receive a single image, the image is actually a rank-3 tensor consisting of RGB channels. The image is run through an edge detection algorithm (in the video I am using for notes, we are using a "Sobel Edge Detector", the lecture notes from class appeared to have something else), and we output different layers from the image. The main idea is that we can output some new set of images with a different kernel. 

Often in our hidden layers we take smaller window sizes in order to save memory 

After having converted the main image into these sub-images, we will use these sub-images as the features for our learning. We can then pass this onto a new layer, and perform the same operation there. 

We begin with some preprocessing, applying edge detection to the image using an edge filter:

![[Pasted image 20251213004320.png]]

We begin by making the input layer the image, and then extracting each region of the image according to a "stride length":

---

# Convolutional Neural Networks

In a CNN we have a linear score function, $f=Wx$, which is just a linear classifier 

For a 2 layer function, we do a linear score, an activation, and then a linear score again. The neuron ativation components in the middle si important, otherwise all we would be doing is 1 big linear tf. Fully connected layer, where every member of one layer can see everything, but this isn't standard, because we dont want everything to take weights,  but at the end we nave a lot of fully connected layers

We need to sot of limit the number of connections we have otherwise we would be doing too many. In a layer neural network, we have that $f=W_{2}\max (0, W_{1}x)$, which is the RELU function. 

We want non linearity because we want to learn complicated transformations that take us the final steps, that we can then apply linear things to to work with. RELU is generally a good choice for most problems. We choose activation functions by getting computationally efficint functions that are also differentiable. 
$$a(W_{1}x+)$$
W's are random initially and then they are trained. 

After we fully do a run through of training, we want to know how changing thr weight changes the weight of the error function. 

Forward pass, we begin by doing some activation on the first layer. We then predict based on the forward pass, and then get the loss next, the dff ebtween our predicted and actual. Then we get to the back propgation srtep, we get the weights connectng the hiden layer and the layer before it, and the layer 3 vs layer 2, and layer 1. We keep repeating this and we gew esrkkmate.

Gradient descent is the enxt step, we ust update our weights with a little step. We only need 20 lines to implement this algorithm. Setting the number of layers and their size. We make our layers longer and wider. If we had an infintie number of neurons we can approximate any function given the neuroms .  Add more neurons allows us to get deeper and more interesting boundaries 

Problem, weights are too big, or too many weights go to zero. A few problems, a few solutions. We have $L_{2}$ regularization, Our loss term also includes our regularization term, and a dataloss diff between learned and predition. 

Back prob example:
$$f(x,y,z)=(x+y)z$$
$$q=x+y,q_{x}=1,q_{y}=1$$
$$f=qz,f_{q}=z,f_{z}=q$$
We want
$$f_{x},f_{y},f_{z}=$$
---
# Convolutional Neural Networks 
Convolve means that we slide and filter over all spatial lcoations within our image, instead of each pixel having a weight, we learn the unit for each, and we "convolve" across the image. 

"Stride", we step by $n$ when we convolve 
If we have a 300x300 image, and we have $n=3$, how many times are we going to be looking at the image based on this, we should be able to look at the image 100 times, vertically, and 100 times horizontally, giving us a total of $100^2=100,000$ different ways to look at it. 

With this method compared to the previous method, we are learning about different regions of the image, and we do less computations overall, instead of the rasterized vector of $300^2$ different weights, which is not good 

As we go down the total number of our samples increases 

### Max Pooling
We want to reduce the total size of the data in our network. Give our window size, we iterate over the image size, and then select the maximum value within the window, and then we add this to the new corresponding matrix produced from the pooling operation. 

Very common to make things smalle in our neural network. We pick some size in our matrix, 
we take the largest element of an entry of our matrix and 

- say we have a 22x22 img and a 5 by 5 stride, 
We have different ways to handle handle mismatch between our stride size and the size of our windows, well it turns out that one way here is by padding stuff with 0's, 1's, it depends 

How can we compute the stride given a 5 by 5 filter , and image of size 55, results in one of 

With neural nets we use random weights and there we can creatte our filters, 
NNs are pretty good at l

We can think of this ting as an image encoder and decoder, where we take an input image and can prodivimg some vectors that represent the image, we can then decode it and see our reuskrs 
# Connection to [[Toeplitz Matrix]] and [[Convolution]]
In [[Convolutional Neural Networks]] we apply the operation of [[Convolution]], which makes use of [[Toeplitz Matrix]] to make more efficient. This is because image data is absolutely massive, and therefore we need a good way to handle it in order to make our operations efficient. Strang doesn't really explain it, but the idea here is that we only need to compute $n$ many weights as opposed to $n^2$ many weights. 
