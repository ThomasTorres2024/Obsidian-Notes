---
title: Lines in n Space
---
We need to be able to generalize the notion of a line between cases where we can visualize in 1,2 and 3 dimensions. We have to be able to algebraically and analytically approach higher dimensional lines. We can do this by describing lines using vectors and examining the general structure of lines in both 2 and 3 dimensions. Let us consider $l(t) : \mathbb{R} \to \mathbb{R}^2$
$$l(t) = (x_{0},y_{0}) + t(a,b) = (x_{0}+ta,y_{0}+tb) \Longleftrightarrow x_{0}+t\vec{v}$$
It is important to make some observations about the notation we are using and to stay consistent in said notation. Our function on the left consists of points, we have something that is scaled by $t$, that we consider our [[Direction Vector]], and a point that we add to our direction vector to move it from the origin to elsewhere in the plane. 

The next equality signifies that we can write this line as a 2 tuple of points and the natural result of distributing $t$. Lastly, we have that there is a bijection and thereby equivalence between the line, $l(t)$ and the vector valued function $\vec{l}(t) = x_{0} + t\vec{v}$, which allows us to express a vector valued function much more succinctly and generally as a direction vector, which is scaled by $t$, plus an $n$ tuple in space that moves the origin around of our function. Notice that if $t=0$, then our origin is strictly determined by $x_{0}$.  
#### General Line Equation Between Points $P$ and $Q$ 
We can use the notion of the equation of a line above to generate a general line equation that spans through points $P$ to $Q$. If $P$ is the origin point, and it goes through $Q$, we know that the direction vector between $P$ and $Q$ can be obtained by $Q-P$. Our initial point is also $P$. We can substitute these into our general line equation above and obtain:
$$l(t)=(Q-P)t + P$$
We can rewrite this equation in a way which is much nicer to work with. Let us factor out $P$:
$$l(t)=(Q-P)t + P=(1-t)P+Qt$$
We get some nice interpretations from this. Since we already know that we begin at point $P$, we know that when $t=0$, that our line will leave us at point $P$, since it's just the origin of where we are at. If we want to get point $Q$, all we need to do is let $t=1$, which eliminates $P$ and gets us to $Q$.

If we want to restrict ourselves to a line equation bound between the initial and terminal points $P$ and $Q$ we need to restrict our $t \in [0,1]$. Otherwise, $t$ will span outside of our equation unless $P=Q=\vec{0}_{n}$.  

#### Alternating Forms 
We can look at the line that passes through $(x_{0},y_{0},z_{0})$ with direction $\langle a,b,c \rangle$, then we can write the following line equation:
$$\mathcal{l}(t)=(x_{0},y_{0},z_{0})+t(a,b,c)$$
$$
\Longleftrightarrow  \begin{cases}    x=x_{0} + at  \\ y=y_{0} + bt \\   z=z_{0} + ct  \end{cases}
$$
$$\Longleftrightarrow \frac{x-x_{0}}{a}=\frac{y-y_{0}}{b}=\frac{z-z_{0}}{c}$$
The 2nd step is obtained by component wise addition of our elements. It is clear to see that when we do [[vector addition]] on our elements, that we will get everything in the piecewise equation. 

The last step we obtain by rearranging each side, and expressing everything in terms of $t$. When we do this, we get the last result.