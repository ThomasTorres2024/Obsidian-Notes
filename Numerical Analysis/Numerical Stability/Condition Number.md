---
title: Condition Number
tags:
draft: "False"
---
# Condition Number Overview
The condition number of an algorithm or a problem tells us, for the function $f(x) : \mathcal{X} \mapsto \mathcal{Y}$ that if we select some small $\delta$ and consider a perturbation of $x$, how large the corresponding change will be to $f(x)$. We can compute this result by considering the following. 

Let the perturbation of the function $f$ be given by:
$$f(x+\delta x) -f(x)$$
If we let $\delta x$ be a perturbation of $x$, and consider the  following limit:
$$ \hat{\kappa}= \lim_{\delta \to 0} \sup_{\|\delta x\| \leq \delta} \frac{\|\delta f \|}{\|\delta x\|}$$
We can determine the limit by computing the [[Jacobian]] Matrix of $f$, denoted by $J(x)$. If we take the limit as $\delta \to 0$ then, we obtain that the [[Condition Number]] is actually equivalent to the following:
$$\hat{\kappa}=\|J(x)\|$$
This measure here is known as the absolute [[Condition Number]]. 

---
# Relative Condition Number 
For some instances, we might only be concerned with relative changes, and the change of $J(x)$ with respect to how the value of $f(x)$ and $x$. Under this model we use the following condition number (notice we do not use the hat): 
$$\kappa(x) = \lim_{\delta \to 0 } \sup_{\|\delta x \| \leq \delta} \left( \frac{\|\delta f\|}{\|f(x)\|} \bigg/ \frac{\|\delta x\|}{\|x\|}  \right)$$
Which simplifies nicely to: 
$$\kappa(x)= \frac{\|J(x)\|}{\|f(x)\|/\|x\|}$$
Relative Condition numbers tend to be used more often in numerical analysis than absolute condition numbers. 