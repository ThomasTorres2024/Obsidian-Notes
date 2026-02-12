---
title: Golden Section
tags:
  - Optimization
draft: "False"
---
# Golden Section Search 
[[Golden Section]] search is a [[Search Method]] for functions of the form $f: \mathbb{R} \to \mathbb{R}$. It is an iterative method, that begins with some initial guess, $x_0$, and then uses $f,f',$ and $f''$ in order to get closer and closer to the exact minimum of $f$. 

The [[Golden Section]] method only makes use of the function $f$, and tries to find the [[Local Minima]] of a function such that $x^* \in [a_0,b_0]$. Let the [[feasible set]] be $\Omega = [a_0, b_0]$. We can compute the next two points, $a_1$ and $b_1$ which are contained within this interval. 

We make use of the [[Golden Ratio]] during this procedure, and denote this ratio by $\phi$, such that:
$$a_1 = a_0 + \phi(b_0-a_0)$$
$$b_1 = (1-\phi)(b_0-a_0)$$
```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[x=1cm]

  % Number line
  \draw[->] (0,0) -- (10.5,0);

  % Key points
  \coordinate (a) at (1,0);
  \coordinate (c) at (4,0);
  \coordinate (d) at (6,0);
  \coordinate (b) at (9,0);

  % Ticks
  \foreach \p in {a,c,d,b} {
    \draw (\p) ++(0,0.12) -- ++(0,-0.24);
  }

  % Labels
  \node[below] at (a) {$a$};
  \node[below] at (c) {$c$};
  \node[below] at (d) {$d$};
  \node[below] at (b) {$b$};

  % Interval highlight
  \draw[ultra thick] (a) -- (b);

  % Interior points
  \fill (c) circle (2pt);
  \fill (d) circle (2pt);

\end{tikzpicture}
\end{document}
```
In the diagram here $c$ is $a_1$ and $d$ is $b_1$. Essentially we can think of point $d$ as a shift by $\phi|AB|$  from $b$ and we can think of $c$ as a shift by $|AB|$ from point $a$. 

We want to iteratively modify the bounds we are working within as we continue through the algorithm. We then compute $f(a_1)$ and $f(b_1)$ and then we determine which bound we should shrink the left and right boundaries of our interval to by comparing the values. 

Since we are looking for the minimum, we want to be in a region where $f$ is decreasing. If we have that $f(a_1) < f(b_1)$ then, we shrink our $\Omega$ from $[a_0,b_0]$ to $[a_0,b_1]$, assuming that the true answer likely lies in the new modified interval. Likewise, if $f(a_1) > f(b_1)$, then we shrink the domain from $[a_0,b_0]$ to the interval $[a_1,b_0]$. 

Let use suppose that $f(a_1)<f(b_1)$. 
When we get to the next stage, we reapply the same idea. We let $a_0:=a_0, b_0:=b_1$, and now we compute a new $a_2$, which we move to be $\phi|ab_1|$ from $b_1$. We repeat the same procedure, and shrink the domain again. 

Similarly, if $f(a_1) > f(b_1)$, then we would let $a_0:=a_1$ and recompute a new point which would be $|a_1b_0|\phi$ from $b_1$.  We continue iterating the process until the length of the subdomain, $|ab| < \epsilon$, which means that we should have converged towards something close.  

Once we attain this size, we can find the approximate [[Local Minima]] by performing:
$$x^*\approx\frac{a_{\text{final}} + b_{\text{final}}}{2}$$
Which is to say half of the subinterval. 

