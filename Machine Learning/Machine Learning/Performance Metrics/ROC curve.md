---
title: ROC Curve
tags:
draft: "false"
---
# ROC Curves 
ROC curves are used in [[classification]] problems in order to represent the ratio of true positives to the ratio of false positives. We want to measure for every false prediction, how many true predictions do we have. 

We can start by taking an arbitrary decision boundary that bisects our dataset. Everything on one side is classified as 1 point, and everything on the other side is classified as another. 
![[Pasted image 20250917143721.png]]
For example, everything left of this model is classified as +, everything else is -. If we placed the model to the left of the +, then we would see that our true positive rate goes to zero, since everything to the right is 0, but our false positive rate goes to 0 since since all of the - points are correctly classified. 

If we put our boundary on the other side past the last point on the right, out true positive rate would go to 1, and our false positive rate would go 1 as well, since every true point is marked as a +, and every negative point is marked incorrectly. 

When we look at an ROC curve, we are looking at the rate of change of true positives to false positives, which means for every good guess, we have how many bad guesses at a very high level. The worst possible model we have is a model where we are doing 1 true guess gets 1 false positive in $y=x$, and the worst corresponding area we could get is thus $0.5$, which corresponds to randomly guessing. 

If we invert our model, if it happens to be below $0.5$, and flip it over the $y=x$ line, we get a better model. 

---
# Building ROC curves 
We can just build an ROC curve by taking 1 step along the FP axis by starting at the last point, and for each negative we see, we walk one unit along FP, and for each + we walk one above, and repeat this process until all points have been passed:
![[Pasted image 20250917144754.png]]

---
# Model Success with [[ROC curve]]s 

A good model is one which is significantly larger and has a higher initial spike than one just trails off much slower. An ideal curve would have an area of 1 and would look like the following:

![[Pasted image 20250917144909.png]]


