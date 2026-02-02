---
title: Simplex Method
tags:
draft: "False"
---
# Simplex Method
The [[Simplex Method]] is a method for finding the extrema of a [[Linear Programming]] problem where the objective function is linear and the constraint sets are linear. It is almost always the case that in our constraint set, we restrict ourselves to the first quadrant/octant etc. 

Graphically, we can think of letting our objective function $f$, stretch over the feasible region by considering various [[Contour]]s of $f$ (e.g for $f(x,y)=z$, let $z=k$, a constant). 

### Example 
Let us consider the following maximization problem:
$$f(x,y)=2x+5y$$
With the following [[feasible set]]:
$$\begin{cases} x-y \geq 0\\ 3x+y \leq 5 \\ x \geq 0\\ y \geq 0 \end{cases}$$
We want to be able to determine the domain of the optimization problem graphically, which can elucidate a potential solution to the problem.


```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[domain=0:4] % Set default domain
    % Draw grid and axes
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};

    % Plot f(x) = x
    \draw[color=red, domain=-0.2:2] plot (\x,\x) node[right] {$f(x) = x$};

    % Plot f(x) = sin(x) (note the 'r' for radians)
    \draw[color=blue, domain=-0.2:2] plot (\x,5-3*\x) node[right] {$f(x)=5-3x$};
    
    % for floor and wall
     \draw[color=blue, domain=-0.2:2] plot (\x,0) node[right] {};
    %\draw[color=blue] plot (\x*0,\x) node[right] {};
    
	  \foreach \x/\y in {0/0, 1.25/(1.25, 1.666666666666/0} {
	    \fill (\x,\y) circle (2pt);
	  }


\end{tikzpicture}
\end{document}
```

Therefore we obtain the following feasible set that consists of the triangle which is enclosed by the 3 points above. Furthermore, it turns out that an optimal solution to our problem in [[Linear Programming]] must be one of the three boundary points, therefore our given region is:

```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[domain=0:4] % Set default domain
    % Draw grid and axes
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};

    % Plot f(x) = x
    \draw[color=red, domain=0:1.25] plot (\x,\x) node[right] {$f(x) = x$};

    % Plot f(x) = sin(x) (note the 'r' for radians)
    \draw[color=blue, domain=1.25:1.66666666] plot (\x,5-3*\x) node[right] {$f(x)=5-3x$};
    
    % for floor and wall
     \draw[color=blue, domain=0:1.66666666] plot (\x,0) node[right] {};
    %\draw[color=blue] plot (\x*0,\x) node[right] {};
    
	  \foreach \x/\y in {0/0, 1.25/(1.25, 1.666666666666/0} {
	    \fill (\x,\y) circle (2pt);
	  }


\end{tikzpicture}
\end{document}
```


We can find the boundary points by determining the points of intersection between the functions in the feasible set. In order to find the extrema, we then consider multiple contours of $f(x,y)=2x+5y$:

```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[domain=0:2] % Set default domain
    % Draw grid and axes
    \draw[very thin,color=gray] (-0.1,-1.1) grid (1.5,1.5);
    
    %\draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    %\draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};
    
    
    \draw[->] (0,0) -- (0,2.5) node[above] {$f(x)$};
	\draw[->] (0,0) -- (2.5,0) node[right] {$x$};
    
	
	%contour set 
	\foreach \k in {-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11} {
	  \draw[orange, domain=0:3]
	    plot (\x, {(\k - 2*\x)/5});
	}

    % Plot f(x) = x
    \draw[color=red, domain=0:1.25] plot (\x,\x) node[right] {$f(x) = x$};

    % Plot f(x) = sin(x) (note the 'r' for radians)
    \draw[color=blue, domain=1.25:1.66666666] plot (\x,5-3*\x) node[right] {$f(x)=5-3x$};
    
    % for floor and wall
     \draw[color=blue, domain=0:1.66666666] plot (\x,0) node[right] {};
    %\draw[color=blue] plot (\x*0,\x) node[right] {};
    
	  \foreach \x/\y in {0/0, 1.25/(1.25, 1.666666666666/0} {
	    \fill (\x,\y) circle (2pt);
	  }

\end{tikzpicture}
\end{document}
```

The optimal solution set is the set that intersects with one of these lines such that value of our objective function, which going forward here I will denote by $f$, must be at one of these points. We can then just compare the values and find which satisfies our criteria.

Clearly the point at $(1.25,1.25)$ is the maxima of $f$, whereas the points at $(2/3,0)$ and $(0,0)$ minimize $f$. 

For an alternative example, we can consider the circle between its origin at $p$ and how far its radius extends, supposing that it must intersect with one of the points in our [[feasible set]]. 

#### Example 2.) 
Let us consider a non-linear objective function given by $$\max / \min f(x,y)=x^2-2x+y^2-4y+5$$Notice that use completing the square we can allow this to be expressed as:
$$f(x,y)=(x-1)^2+(y-2)^2=k$$
And again, we can consider the set of [[Contour]]s for different values of $k$. Let our constraint set be given by:
$$\begin{cases} x-y \geq 0\\ 3x+y \leq 5\\ x \geq 0, y \geq 0 \end{cases}$$
Solving for the boundary conditions we can obtain the following 3 points:
```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[domain=0:4] % Set default domain
    % Draw grid and axes
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};

    % Plot f(x) = x
    \draw[color=red, domain=0:1.25] plot (\x,\x) node[right] {$f(x) = x$};

    % Plot f(x) = sin(x) (note the 'r' for radians)
    \draw[color=blue, domain=1.25:1.66666666] plot (\x,5-3*\x) node[right] {$f(x)=5-3x$};
    
    % for floor and wall
     \draw[color=blue, domain=0:1.66666666] plot (\x,0) node[right] {};
    %\draw[color=blue] plot (\x*0,\x) node[right] {};
    
	  \foreach \x/\y in {0/0, 1.25/(1.25, 1.666666666666/0} {
	    \fill (\x,\y) circle (2pt);
	  }


\end{tikzpicture}
\end{document}
```
These are the same constraint sets as our previous problem. Now we can consider various contours now. Let $O=(0,0)$ and $C=(5/4,5/4)$,  $A=(0,5/3)$, and lastly $B=(1,2)$:  
```tikz 
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[domain=0:4] % Set default domain
    % Draw grid and axes
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};

    % Plot f(x) = x
    \draw[color=red, domain=0:1.25] plot (\x,\x) node[right] {$f(x) = x$};

    % Plot f(x) = sin(x) (note the 'r' for radians)
    \draw[color=blue, domain=1.25:1.66666666] plot (\x,5-3*\x) node[right] {$f(x)=5-3x$};
    
    % for floor and wall
     \draw[color=blue, domain=0:1.66666666] plot (\x,0) node[right] {};
    %\draw[color=blue] plot (\x*0,\x) node[right] {};
    
	  \foreach \x/\y in {0/0, 1.25/1.25, 1.666666666666/0, 1/2} {
	    \fill (\x,\y) circle (2pt);
	  }
	  
	  	%contour set 
	\foreach \k in {2,3} {
	  \draw[orange, domain=0:2]
	    plot (\x, { sqrt(\k - (\x*-1)^2) +2 });
	}
	


\end{tikzpicture}
\end{document}
```
