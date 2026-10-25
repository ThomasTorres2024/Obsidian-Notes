---
title: CNNs
draft: "false"
tags:
---
# CNN Intro 

Convolutional neural networks are a specific [[Neural Networks]] architecture that makes use of "covolving" over an image, which yields a smaller algorithmic complexity and memory cost. Instead of feeding in each individual pixel into the input layer of the neural network, we want to consider different windows of the image by considering some window size of $m \times m$ being moved across an image. This is the main idea behind a CNN.

When we receive a single image, the image is actually a rank-3 tensor consisting of RGB channels. The image is run through an edge detection algorithm (in the video I am using for notes, we are using a "Sobel Edge Detector", the lecture notes from class appeared to have something else), and we output different layers from the image. The main idea is that we can output some new set of images with a different kernel. 

For instance this would look like: 

$$\begin{bmatrix}
1 & 0 & \dots & \dots  \\
-1 & 0 & \dots & \dots \\
 \dots & \dots & \dots & \dots
\end{bmatrix} \otimes  \begin{bmatrix}
0 & 1 \\ -1 & 2 
\end{bmatrix} \to  $$

We take the "kernel" of an image, slide it over various portions of the image continually through the process of [[Convolution]], obtain an enhanced image, and then perform some information extraction. This is due to the fact that CNNs were very computationally expensive on normal images. 

Modern CNNs are interested in learning how to create the kernels, and this procedure is a learnable one. 

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

Convolve means that we slide and filter over all spatial lcoations within our image, instead of each pixel having a weight, we learn the unit for each, and we "convolve" across the image. Mathematically we take some "kernel" some fixed grid sized of pixels, and then slide it across each section of the image where the kernel is some stride size. The [[Convolution]] operation used here is given in the following:

$$f(t) * g(t) = \int_{-\infty}^\infty f(t- \tau )g(\tau)d \tau = \int_{-\infty}^\infty f(\tau) g(t-\tau)d \tau$$
![[Pasted image 20261025134726.png]]

We can think of the convolution as an accumulation o the intersection between the two functions. Similarly in CCNs we are making use of this operation:

$$\begin{align}
\underbrace{\begin{bmatrix}
\textcolor{red}{\begin{bmatrix}
1 & 0 \\
-1 & 0
\end{bmatrix}} & \begin{matrix}
-2 & 1  \\
1  & 2
\end{matrix} \\ \begin{matrix}
0 & 2  \\
1 & 0
\end{matrix} & \begin{matrix}
1 & 0  \\
0 & 1
\end{matrix}
\end{bmatrix}}_{\text{Input Image}} \otimes \underbrace{ \textcolor{blue}{\begin{bmatrix}
0 & 1  \\
-1 & 2
\end{bmatrix}} }_{\text{Kernel}} = \underbrace{\begin{bmatrix}
1 & &  \\
& & & \\
& & &
\end{bmatrix}}_{\text{Output}} \\
\text{Output}(0,0) = 1 \cdot 0 + 1 \cdot 0 + -1 \cdot -1 + 2 \cdot 0 = 1
\end{align}$$Note that for the convolution process we are actually using the [[Hadamard Product]]. We slide the window on the in input image over by $1$ to the end to the right, below, and so on until we full fill out our output:

![[Pasted image 20261025135639.png]]
#### Why is the [[Convolution]] operation relevant to image classification?

When we convovle the image with kernels we can produced enhanced versions of the image. These enhanced versions are much easier to work with during image classification than the raw image originally:

![[Pasted image 20261025135945.png]]

In summary kernels are convolved with images to produce different enhancements. 

---
# Image Processing

Previously we would take in some raw image data, manually find a kernel, and then enhance the image and extract features _manually_. We would feed it into a machine learning algorithm and then obtain a class label during the [[Classification]] stage.

The reason why we handled images this was due to the limited amount of compute power at the time, which has obviously ballooned in present years. 

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

---
# Questions about CNNs

### 1). What is the CNN operation?
A mathematical operation implemented as a learnable filter to extract features from images. 

### 2). Why are CNNs so effective on images? 

In the convolution operation, weights of the filter are __learnable parameters__. This allows a model to learn how to extract importan features from the image itself. 

For one we do not need to do any conversion of images to some smaller size. Say in our architecture we have some sliding image of size $5x5$ giving 25 total learnable parameters $+1$ from the bias, so $26$ each. Each gets their own respect activation function. Suppose we have $6$ such kernels, we would thus have $5 \times 5 \times 6+6=156$ total learnable parameters. Adding another such kernel would only be $26=25+1$ parameters, where $25$ come from the kernel again $1$ is the bias. 

Adding in parameters is fairly efficient too. 
##### Why is this significant?
For FFNs, when we tried to add a single neuron we added $51,200$ neurons, and here we added only $26$ for each. 

---
### Example

Let's say we are using a CNN on text classification. And that we have the following $100$ word sentence that we have embedded. Let us follow this through the model:

$$\begin{bmatrix}
w_{1} \text{ one hot} \\
w_{2} \text{ one hot} \\
\dots \\
w_{100} \text{ one hot}
\end{bmatrix}_{100 \times 20,501} \cdot W_{20,501 \times 512} = \text{Embedding}_{100 \times 512}$$ 
The number of unique words in the dataset is $20,501$. The input is $100$ words for each document being classified and the embedding dimension is $512$. For one, unlike in a FFN we do __not need to flatten the input__. For the sake of argument we will treat the text like an image of size $100 \times 512$.

We have some number of kernels. Let us suppose we have $6$ kernels, each of which does some operation on the image independently in $5\times 5$ size. Each square has $25$ learnable parameters, plus a bias. 

![[Pasted image 20261025141320.png]]

We convolve the image and obtain some resulting output. We feed them into an [[activation function]].

#### Model Architecture Questions

* How many learnable parameters are in the input layer?
	* We have $6$ kernels, each of which is of size $5 \times 5$. Each parameter in the kernel is trainable. Each kernel has its own bias. So we have $(5^2)\cdot 6 + 6=156$ model parameters.  
	
* If we add another kernel how many parameters will be added?
	* We add $5 \times 5$ parameters for the sliding window and then $1$ for the bias, so $26$. 

* Why is this significant?
	* Cost for FFNs for adding a single neuron was massive, here we are just adding $26$ neurons. 

---
# Example CNN Architecture 

![[Pasted image 20261025141800.png]]


We can this of the convolution layers and pooling layers as a means to simply produce a __latent representation of the data__, that is a representation that is much easier to classify. We then take the outputs produced that we vectorize them and cocatenate them, and feed them into a FFN. More abstractly our model can be thought of as:

$$\begin{bmatrix}
\text{Image}
\end{bmatrix} \xrightarrow{\text{Convolve}} \text{Latent Representation} \xrightarrow{\text{Flatten to 1D}} \text{FFN} \to \text{Classification} $$

We are essentially looking for data in our architecture wherein we can easily separate the classes data than would be done otherwise if we  tried to classify the image as is. The FFN at the end of the model is meant to be an easier to classify variant of the model, so we avoid difficult training issues. The latent data is also in a form that is generally easier to learn. 


---
# Fundamentals of a CNN 

### Overall Model
With CNNs we apply many levels of various non linear activations, convolutions, maximum pooling etc operations, and then we obtain a __latent representation of the data that is easier to classify__ (transform the data that makes classes easily separable by boundaries or a line). We then feed the result through a [[FFN]] and predict it on some result. 
### Why are we using a [[FFN]] at the end?
FFNs are difficult to work with in train in the context of __complex__ FFNs, with too many layers or neurons. A complex model means too many trainable parameters.

FFNs attached are generally a lot easier to work with on the processed images. 

---
# Why are CNNs not as effective for [[Natural Language Processing]]? 

We should first examine why it is so effective for images to begin with. Say we had a kernel with an image of a soccer ball $S$, and some image $I$. Say there is some soccer ball portion baked into Image $I$ in the bottom right hand corner. I will denote its pixels by $S_{2}$. If we convolved over the whole thing, we would see the highest output in the convolution process in the bottom righthand corner of the model:

$$\underbrace{\begin{bmatrix}
\dots & \dots & \dots \\
\dots & \dots & \dots \\
\dots & \dots & S_{2}
\end{bmatrix}}_{\text{Image}} \otimes  S_{1} \xrightarrow{\text{Convolution}} \begin{bmatrix}
\dots  & \dots & \dots \\
\dots & \dots & \dots \\
\dots & \dots & \text{Highest Output}

\end{bmatrix} $$
We would have the highest output where the two items would overlap. This useed to be a good method for image identification a long time ago. 

#### How are we going about processing the information in the image?

We can think about this operation of [[Convolution]] as a torch in a dark room. We overall do not have much access to every part of the image at once. We only have context for a small portion at each time. This is baked into the fact of how the window shifts and moves around. We never look at the image in its whole. 

We can think of this idea as a __receptive field__, which is the size of the input used in computing the output. We only look at pieces of the image in total. 

In CNNs, during the process of convolution, only a small total of the percent of the data is passed over. If we tried to proceed and summarize text in this manner, our model would fail. We call this quantity used the __receptive field__.

### Why is a small receptive field bad in NLP?

Generally when we are lookng at some very small and selective window of text, we need to have the entire context is order to adequately represent and give a good summary about it. For instance even in a story during the start and the end of it it is very different. We would not have an effective mechanism in order to process text. We cannot gain a good understanding of the text from isolated pieces of text. 

