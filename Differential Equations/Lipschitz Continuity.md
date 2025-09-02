---
tags:
  - None
draft: "false"
---
---
# Motivation for Lipschitz Continuity

The existence portion of the existence and uniqueness of differential equations requires the notion of Lipschitz Continuity for function to be satisfied locally. 

Let us consider a function, $f : \mathbb{R} \rightarrow \mathbb{R}$ where $f$ is continuously differentiable and $f$ is continuous. 

Note, a continuously differentiable function is a function that is differentiable for all values along its domain, and the derivative function is also a continuous one. 

$f$ is continuous since  continuous differentiability requires continuity along all points of $x \in \text{dom}(f)$. 

We can also view Lipschitz Continuity to be the needle that threads these two concepts. 

---
# Definition of Lipschitz Continuity 

Consider the function $V : \mathbb{R}^n \rightarrow \mathbb{R}^n$ which is called locally Lipschitz continuous if 
$$\underset{x \in \mathbb{R}^n} \forall \text{   } \underset{\epsilon > 0} \exists \text{ } \underset{L >0} \exists \text{ } \underset{y,z \in B_{e}(x)} \forall :  \| v(y)-v(z) \| \leq L \| y-z \|$$
Intuitively, for any point in the domain of $V$, we can define some neighborhood around the vector by $B_{\epsilon}(x)$ for some $\epsilon > 0$ where the distance times some constant factor is larger than the change in the function. 

This ensures that we will not have massive jumps between values in our function. 

A function satisfying these conditions is said to be locally Lipschitz continuous. Such a function satisfies two properties. 

1. $V$ is locally Lipchitz continuous $\implies$ $V$ is a continuous function 
2. $V$ is locally Lipchitz continuous $\implies \dfrac{\|v(y)-v(z) \|}{\| y-z \|} \leq L$ which tells us that the slope will always be  bounded by $L$. Locally, the slopes of the function are bounded.

Let the $C^1$ function $f : \mathbb{R} \rightarrow \mathbb{R}$. Fix $x \in \mathbb{R}, \epsilon > 0$. 

$$\dfrac{|f(y)-f(z)|}{|y-z|}=f'(\xi)$$

Which is guaranteed to be true for the mean value theorem for this function. 