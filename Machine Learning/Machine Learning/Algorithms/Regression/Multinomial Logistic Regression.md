---
title: Multinomial Regression
draft: "false"
tags:
---
# Multinomial Logistic Regression
[[Multinomial Logistic Regression]] is a [[Multinomial Classification]] algorithm that uses [[Logistic Regression]].  The [[Multinomial Logistic Regression]] algo ts a bit more complicated than that variant, DOING the same idea involving many classes, more than just 0s and 1, and we want to classifythe mnist data set 

[[Multinomial Logistic Regression]] optimizes over the [[Softmax]] function instead of the [[Sigmoid]] function. 

From [[Softmax]] we get unnormalized weights, all must be poirifved, unomrlaized pro ablities here, lastly make sure that probabilities go to one at the end \

here we learn weights , and instead of just feeding only  layer to he ne, with logisitc regression
W here is a larger vector now from weight stuff 
instead of sticking things into th sigmpid, w throw it intn the softmax function, make it all positive and make it all sum to 1 

softmax instead of sigmoid, and more classes 

we predict the weight with the highest p4robability score, and the one that does the best at minimziing our loss function

$$W^* =\text{argmax}_{w} \frac{1}{n} \prod_{i=1}^n$$
We have a one hot encoding for how our labels shold be be represented. Our max here is teh probablty the highest probability of the softmax is the same as a 1 hot encoing nmber, when we misclassify take negative log of the probability of our class if we get it wrong, and overal, we want to minimize this quantit yacross the sum of all items in our set. The lowest loss option that is well tained should always have like 0.9999 accuracy for an image it is successfully trained on.

When we compute our raw scores, we take the scores and then feed them into soft max. intuitively with the image classification we want to see what pixels what tendencies most ld validations Intuitively, we are finding high dimensional planes to partition our classes in a higher dime sjonal space 
