---
title: Backpropagation
tags:
draft: "false"
---
# Backpropagation
Recall that the general formula for a neural network is a repeated function composition applied to the input vector of a function:
$$F(x)=F_{n}(F_{n-1}(F_{n-2}(\dots F_{1}(x))))$$
In order to compute the [[Gradient]] of $F(x)$ we need repeated application of the chain rule applied to this expression. Let us consider some smaller example of $F$:
$$F(x)=F_{3}(F_{2}(F_{1}(x)))$$
If we wish to compute the following, we would make use of the [[Chain Rule]] from Calculus, we can compute the following quantity:
$$\frac{dF}{dx}=\frac{dF_{3}}{dF_{2}}(F_{2}(F_{1}(x)))\cdot \frac{dF_{2}}{dF_{1}}(F_{1}(x))\cdot \frac{dF_{1}}{dx}(x)$$
This is the basic case for a single variable function. In deep learning, we need to be able to handle million variable functions.

When we need to compute gradients, we need to use the [[Partial Derivative]]s of a function. We have two methods for computing these partials, either by going forwards, from the interior of the function outward, or from the the last function to the first one. Often, the functions we use in our computation are independent of one another, and going forward does a lot of unnecessary computations. We consider computation graphs that are later on nullified, and don't go anywhere in our [[Gradient]] computation, so we instead opt to go in from the back. I think we also do this because going forward has a lot of repeated computations that we already use which are completely unnecessary for the actual computation of our gradients. 

It turns out that [[Backpropagation]] is something that is significantly quicker when done backwards than forwards. This comes from the fact that we can reuse parts of the chain rule in our computation. 

The way Strang explains this is in the following:
![[Pasted image 20260105071802.png]]

The left [[Computational Graph]] is the [[Computational Graph]] when going forward. This is just for computing $dF/dx$, not even for $dF/dy$, which is also needed. We would need to duplicate the same graph twice, plus there is additional work on [[Partial Derivative]]s which are never once used for any computation. Whereas in the second [[Computational Graph]] on the right, we have a single computational graph which will yield the results of $dF/dx$ and $dF/dy$ going backwards without needing to step over computations that have already been completed. 