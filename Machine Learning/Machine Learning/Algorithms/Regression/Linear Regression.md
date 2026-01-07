
# Raw Notes for 9/24/25
If some data is approximately linear, we can use linear regression to fit a set of points to a best fit line. We are looking for a line where $y=wx+b$ where $w$ is the weight of a dataset. 

We are more interested in a multivariable example, where:
$$y=w_{2}x_{2}+w_{1}x_{1}+b$$
Our hypothetical function of our data, $h$, is given by, where the weights $\vec{x},\vec{w} \in \mathbb{R}^d$.
$$h(x)=w^Tx+b$$The $b$ term is referred to as the bias. Sometimes practically we just add $b$ to our weight vector or we we have a 1 at the start of our data vector.

The hypothesis space is given by: $$\mathcal{H}=\{h_{w} :h_{w}(x) =w^Tx, w \in \mathbb{R}^d \}$$
Again we are assuming a linear relationship about our data and the labels here, we are assuming that the underlying data is in some way linear. When linear regression is used, we are making an extremely strong assumption about our data. 

---
# Applications
Linear regression is applied to many places, financial forecasting, environmental science, marketing, real estate, etc. The strongest underlying assumptions might be nice, and might allow us to pick our data the best. 

$$\mathcal{D}= \{ \vec{x}_{i},y \}, \vec{x} \in \mathbb{R}^d, y \in \mathbb{R}$$
When we are optimizing [[Linear Regression]], we are optimizing our squared loss. 

The residual is the difference between our prediction and the actual data. We want to find a function which has the smallest mean square error lost. 

There is a closed form solution for this. There is an analytical solution to minimize the loss of the function. We have a [[loss functions]] that we can minimize our result:
$$w^*=\text{ag}$$
The mean squared error function is actually a [[Convex Function]], which implies that local minimums are actually the global minimum of a function. If we can find a local minimum then, then it follows that our mean squared error is actually when our function has a zero derivative. We can minimize our result using the [[Pseudoinverse]] of the weight matrix $W$, or through [[Machine Learning/Machine Learning/Algorithms/Optimization/Gradient Descent]]. There are also MLEs.

Very high dimensional data is something we struggle to process, $O(nd^2+d^3)$. We can use mini-batching with gradient descent. For [[Time Series]] data, [[Linear Regression]] is useless, too many lines, can't possibly be useful. 

[[Linear Regression]] is also very sensitive to outliers in the data. 