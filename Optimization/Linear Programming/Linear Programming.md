---
title: Linear Programming
---
# Overview of Linear Programming
Linear programming is the optimization of a linear cost function generally given by:
$$\min c^Tx=\sum\limits_{i=1}^{n}c_{i}x_{i}$$
With the constraint set given by:
$$Ax=b : A\in \mathbb{R}^{m \times n}, m < n$$
(Note that we are interested in these particular constraints, since we already have answers for other shapes of $A$ especially if $A$ has an [[Inverse Matrix]])

And the constraint that $x \geq 0$ which means $x_{i } \geq 0$ in $x$.  Due to these constraints, we have restricted ourselves to the first octant. 

For instance consider the following objective function with the constraint set:
$$\min x_{1}+2x_{2}+5x_{3}$$
$$x_{1}+x_{2}+x_{3}=3$$
Our resulting "feasible set" is a plane bounded by the $xy$ plane, $xz$ plane, and the $yz$ plane. Our resulting figure is some truncated plane:

![[Pasted image 20260103054954.png]]

Given a linear function, which our objective function is, the constraints are at the borders of the function with the boundary. They must result at the intersection with the different planes. For large values of $m$ and $n$, it turns out that there an exponential amount of corners to check, which makes the run time of the algorithm extremely high. 

There are 2 approaches to solving this problem, either using the [[Simplex Algorithm]] or the [[Karmarkar Algorithm]]. 

# 1.) [[Simplex Algorithm]] 
We begin at a corner, and then we move to the next corner, and continue to move until we have reached some minimum. This is similar to [[Machine Learning/Machine Learning/Algorithms/Optimization/Gradient Descent]] but only on corner points. 

In the worst case, the [[Simplex Algorithm]] would be $O(2^n)$, as we have to check all of the exponentially many corners. The average case of the simplex algorithm is far more common, and tends to be of polynomial time complexity.  On average, it is fast. It can also be shown that [[Linear Programming]] problems belong to the world of [[Complexity Class P]] Algorithms. 

# 2.) Karmarkar Algorithm 
The idea is to travel within the [[feasible set]], instead of along the exterior. Essentially we apply [[Machine Learning/Machine Learning/Algorithms/Optimization/Gradient Descent]] on the entire instead of the outside. 

Both of these algorithms still have not entirely beaten the other, and both have their own respective use cases. 

# [[Dual LP]]
Instead of solving the exact [[Linear Programming]] problem, we can opt to solve the [[Dual LP]], which is essentially the inverse of the problem. The set of constraints that we have becomes the function we are trying to optimize over, and the set of functions we are trying to optimize become the constraints. Furthermore, we are go from looking from a max to a minimum, and vice versa. 

In some way, this is the equivalent problem here as the original, and by solving one of the problems we are able to solve both. The [[Dual LP]] problem for our original [[Linear Programming]] problem would have the form of the following for [[Weak Duality]]
$$\max b^{T}y \text{ for } y_{1},y_{2},\cdots y_{m}$$
With the constraint set for any $x$
$$A^{Ty}\leq c, b^{T}y \leq c^Tx $$
We can prove the identity that: $b^{T}y \leq c^Tx$:
$$b^Ty=x^TA^Ty$$
But note that $A^{T}y\leq c \implies x^TA^{T}y\leq x^Tc=c^Tx$, and thus we get our constraint. 

---
# Two Person Games
Let us consider a game of 2 people, $X$ and $Y$. Let us consider the "Payoff Matrix":
$$P=\begin{pmatrix} 1 & 2 \\ 4 & 8\end{pmatrix}$$
This is the "Payoff Matrix from $x$ to $y$". $x$ will choose a row, and $y$ will choose a column. $x$ will pay player $y$. $y$ collects, and they want to maximize. This is a "zero sum game", what $x$ pays goes to $y$, there is no third party involved. $x$ wants to make the amount they pay small, and $y$ wants to make the amount $x$ pays large. Player $x$ will tend to choose row $1$, and player $2$ will tend to choose column 2. 

This point here is a [[Saddle Point]] at $P_{12}=2$, since it is a minima for player $x$ and a maxima for player $y$. It is not the case that the optimal point is a [[Saddle Point]]. Consider this other payoff matrix:
$$P=\begin{pmatrix}1 & 8\\ 4 & 2\end{pmatrix}$$
$y$ will gravitate towards the second column. $x$ will thus gravitate towards the second row. But if $x$ chooses the second row all of the time, then $y$ will choose the first column some of the times, so that he can get the $4$. But, if $y$ chooses the first column all of the time, $x$ will pick column 1, with only a payoff of $1$. Therefore $2$, is not actually a saddle point since it doesn't minimize for $x$ always while always maximizing for $y$ since there is some deeper strategy at play here. 

In turn we have some "mixed strategy", where $y$ will choose the columns with some probabilities such that the sum of the probabilities adds to 1:
$$\begin{pmatrix} 1 & 8\\ 4 & 2 \end{pmatrix} \cdot \begin{pmatrix} p\\1-p \end{pmatrix}=\begin{pmatrix}p(1) +8(1-p) \\ p(4)+2(1-p)
 \end{pmatrix}$$
 We impose that $p$ is subject to the constraint that: $0 \leq p \leq 1$.
 
 Player $x$ will do something similar but for $0 \leq q \leq 1$ except we use the columns instead of the rows:
 $$P^{T}\begin{pmatrix} q \\ 1-q\end{pmatrix}= \begin{pmatrix}q+(1-q)4\\8q+(1-q)2\end{pmatrix}$$
 It turns out that the game settles down once $y$ selects $p$ such that the outcomes of the game are equivalent, meaning that there is no difference in how $x$ performs. $y$ could take advantage of $x$ being lazy, but once this occurs we can determine the optimal $p$ such that:
 $$p+8-p=4p+2-2p \iff 6p=9 \implies p =\frac{2}{3}  $$
 It turns out that the optimal strategy is some combination of pure strategies, which consists of picking a specific row or column.  We can convert this Game Theory problem into a [[Linear Programming]] problem by using [[Dual LP]]. It's also interesting to note that [[Linear Programming]] problems do not solve $3$ or $n$ person problems, and that these models generally are way too simple to solve such difficult problems. 