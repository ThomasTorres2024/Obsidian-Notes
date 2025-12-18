---
title: CNNs
draft: "false"
tags:
---
Convolutional neural networks are a specific [[Neural Networks]] architecture that makes use of "covolving" over an image, which yields a smaller algorithmic complexity and memory cost. 

We begin with some preprocessing, applying edge detection to the image using an edge filter:

![[Pasted image 20251213004320.png]]



We begin by making the input layer the image, and then extracting each region of the image according to a "stride length":