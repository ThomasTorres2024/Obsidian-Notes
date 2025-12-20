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