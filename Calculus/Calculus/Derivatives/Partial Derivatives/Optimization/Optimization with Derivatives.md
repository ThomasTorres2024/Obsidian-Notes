---
title: Optimization with Derivatives
tags: 
draft: "false"
---
# Optimization Problems Introduction

When trying to optimize functions we try and find the point at which the value of a  function is maximized, meaning that all other points in the range of a function on some interval are less than (in the case of maximization) the highest point, or the point is less than all other values in the range of the function. 

### Single Variable Calculus Intuition
In the case of multivariable calculus for a function of $\mathbb{R}^n$, we must consider optimizing over several variables in order to obtain our result.

We will restrict ourselves first to the case where we have a function $f : \mathbb{R}^2 \rightarrow \mathbb{R}$ and consider how we can find the lowest point or highest point along the function. 

In single variable calculus we try to find the coordinate $c$ at which some function $y(x) : \mathbb{R \rightarrow R}$ satisfies $y'(c) =0$. The point $(c,y(c))$ is a [[critical point]] of the function, the point at which the function stops changing.

We run a concavity test on $y''(c)$ to determine if the function is increasing, decreasing, or neither.

### Multivariable Calculus Extension of Optimization of a Function
We can analogously apply a second rule for a function of two variables given by $g(x,y) : \mathbb{R^2 \rightarrow R}$.

We would find the points $(x_{0},y_{0})$ such that our partial derivatives of our surface $g$, satisfy:
$$\dfrac{\partial}{\partial x} g(x,y)|_{(x_{0},y_{0})}=g_{x}(x_{0},y_{0})=0$$  $$\dfrac{\partial}{\partial y} g(x,y)|_{(x_{0},y_{0})}=g_{y}(x_{0},y_{0})=0$$ 
Effectively, we are solving for a flat/horizontal tangent plane on the surface $g$. The tangent plane should never move at all with respect to $x$, and should not move at all with respect to $y$. This is related to the fact that the tangent line of a function which is optimized is also flat, meaning that it has accumulated the maximum amount of change that a function allows up to a point. 

In turn our function for a tangent plane is really just $z=z_{0}$ where $z_{0}$ is a constant. 

For example, in the following graph, we see that the minima of the surface is the $z=0$ plane:


![[Pasted image 20250620181732.png| center |256 ]]
If we also examine the equation of a tangent plane:

$$z=z_{0}+a(x-x_{0})+b(y-y_{0})$$

We see that the plane is constant when the $x$ component and $y$ component of the plane equation are zero, which happens when the partial derivatives are zero for $g$ at the critical points. 

#### Definition of a Critical Point
We call a "$\textcolor{pink}{\textbf{critical point}}$" for a surface of two variables $g$, a point denoted by $(x_{0},y_{0})$, at which the surface of $g$ has partial derivatives which satisfy:

$$g_{x}(x_{0},y_{0})=0$$
$$g_{y}(x_{0},y_{0})=0$$

For an arbitrary function $f(x_{0},x_{1},\cdots,x_{n}) : \mathbb{R}^n \rightarrow \mathbb{R}$, we can similarly define a critical point by the point in $\mathbb{R}^n$,  $(a_{0},a_{1},\cdots,a_{n})$, that satisfies the following for all partial derivatives of $x_{i}$ for the function $f$: 

$$\dfrac{\partial}{\partial x_{i}} f(x_{0},x_{1},\cdots,x_{n}) |_{(a_{0},a_{1},\cdots,a_{n})} = 0$$

Which basically says that every partial derivative evaluates to zero when inputting the set of coordinates at the critical point. Instead of having a constant plane as in the $\mathbb{R}^2$ we would have a constant "hyperplane" of the form $y=y_{0}=f(a_{0},a_{1},\cdots, a_{n})$.

We have three ways to classify our critical points that reveal if they actually are minima, maxima, or a saddle point. 

1. [[local maxima]] - A maxima occurs if the value of the function is greater than all other values in some interval around the point
2. [[local minima]]  - A minima occurs if the value of the function is less than all other values in some interval around the point
3. [[saddle point]]- A point that is neither a minima or a maxima but still critical. It doesn't minimize or maximize anything locally and requires more inspection for anything to be said about it. 

---
# Least Squares Via Max-Min 

For a set points, typically deprived from experiment, we can find a line such that the squared distance between this line and our experimental data is minimized. 

Our experiment would be denoted by:

$$P=\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{n},y_{n}) \}$$
We also have our best fit line with the parameters $\alpha$ for slope and $\beta$ for our y-intercept:

$$y=\alpha{x}+\beta$$
The problem of least squares has us find the values of $\alpha$ and $\beta$ that minimize the total $R^2$ distance to our best-fit line. This is the measure of $R^2$ error, and a way to rephrase our goal is to find the curve which has the least error.

We like working with $R^2$ error since our minimization polynomial is a nice function to work with. If we were to minimize over $R^1$, in a taxicab metric, we would run into issues with the absolute value function $|x|$ being undifferentiable at $|x|=0$. 

The error at each point would be given by the expected result from our best fit curve, and the actual result. 

$$E=y_{i}-(\alpha x_{i}-\beta)$$
We would then square this error since we are dealing with squared error.
$$E^2=[y_{i}-(\alpha x_{i}-\beta)]^2$$
We can then take the sum of  each error term:
$$D(a,b)=\sum_{i=1}^n [y_{i}-(\alpha x_{i}-\beta)]^2$$
We can use our knowledge of optimization of multivariable functions to find the best line. We will take the partial with respect to $a$ and $b$:

$$\dfrac{ \partial D}{\partial a}= \dfrac{\partial}{\partial{a}} \sum_{i=1}^n [y_{i}-(\alpha x_{i}-\beta)]^2=\sum_{i=1}^n-2x_{i}[y_{i}-(\alpha x_{i}-\beta)]^2=0$$
$$\dfrac{ \partial D}{\partial b}= \dfrac{\partial}{\partial{b}} \sum_{i=1}^n [y_{i}-(\alpha x_{i}-\beta)]^2=\sum_{i=1}^n-2[y_{i}-(\alpha x_{i}-\beta)]^2=0$$
We set these equations to zero since we want to find the values of $\alpha$ and $\beta$ that cause our function to actually equal zero. 

$$  \sum_{i=1}^n-x_{i}[y_{i}-(\alpha x_{i}-\beta)]=\sum_{i=1}^n(-x_{i}y_{i}+\alpha x_{i}^2 +  \beta x_{i})=0$$
$$\sum_{i=1}^n(-y_{i}+\alpha x_{i} + \beta)=0$$We can factor out the $\alpha$ and express each as a nice relation:
$$\alpha\sum_{i=1}^n(x_{i}^2)+\beta\sum_{i=1}^n  (x_{i})=\sum_{i=1}^nx_{i}y_{i}$$
$$\alpha \sum_{i=1}^n x_{i} + n\beta=\sum_{i=1}^ny_{i}$$
Notice that the sums are just numbers, and so from this we get a linear system of equations that we can solve in a $2 \times 2$ linear system. 

We can just do Gaussian elimination on this to solve for our $\alpha$ and $\beta$:
$$\begin{bmatrix} \sum_{i=1}^nx_{i}^2 &\sum_{i=1}^nx_{i}\\
\sum_{i=1}^nx_{i} & n
\end{bmatrix} \cdot \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} \sum_{i=1}^nx_{i}y_{i} \\ \sum_{i=1}^ny_{i} \end{bmatrix} $$ 