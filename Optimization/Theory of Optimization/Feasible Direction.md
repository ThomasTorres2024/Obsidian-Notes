---
title: Feasible Direction
tags:
  - Optimization
draft: "False"
---
# Feasible Direction 
Let us consider a [[feasible set]] $\Omega$ in an [[Optimization]] problem, and let us focus on $x \in D$. We can define a [[Feasible Direction]] as the vector $\vec{x}+\alpha \vec{d}$, where $\exists \alpha \in \mathbb{R}^+$, such that $\vec{x}+\alpha \vec{d} \in \Omega$. If $\vec{x}$ is an interior point, it follows that any $\vec{d}$ satisfies the condition mentioned above. However, if $\vec{x}$ is a boundary point, then  we cannot point away from our [[feasible set]] $\Omega$, thus we get a relatively large restriction on the possible values of $\vec{d}$

# Example 

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



