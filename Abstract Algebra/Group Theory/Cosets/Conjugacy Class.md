---
title: Conjugacy Class
tags:
  - AbstractAlgebra
draft: "False"
---
# Conjugacy Class 
Given some [[Group]] $G$ and a [[Subgroup]] $H \leq G$ we have that the conjugate subgroup of $H$ for a fixed $g \in G$ is given by:
$$gHg^{-1}=\{ ghg^{-1} : h \in H \}$$
Clearly, $H$ is a [[Normal Subgroup]] $\iff$ $gHg^{-1}=H \quad \forall g \in G$.  This gives the [[Conjugacy Subgroup]] idea. 

Following up on this idea, we have another one, which items can be written as $gxg^{-1}$ for $g\in G$ with the following:
### Definition). __Conjugacy Class__
$$\text{cl}_{G}(x)=\{ gxg^{-1}: g \in G \}$$
### Remarks).
* For any group, $\text{cl}_{G}(e)=\{e\}$
* If $x \in Z(G) \implies gxg^{-1}=x$ ([[Center of a Group]]). We only need to determine the $g \in G$ such that $g$ and $x$ do not commute in order to determine the elements of the class.
* $\text{cl}_{G}(x)=\{x \} \iff$ $x \in Z(G)$ 

---
# Theorem). 
[[Conjugacy Class]]es are an [[Equivalence Relation]]:
$Proof.)$
$$\begin{align}
x=exe^{-1} \implies  x Rx  \\
y=gxg^{-1} \implies x=g^{-1}yg \quad xRy \implies yRx \\
x=gyg^{-1},y=hzh^{-1} \implies x=(gh)z(gh)^{-1}
\end{align} $$
Therefore [[Conjugacy Class]]es form an [[Equivalence Relation]] and thus partitions any [[Group]] into [[Equivalence Class]]es. 

---
# Example). 
Conjugacy classes in $D_4$.

Let us consider $\text{cl}_{D_{4}}(r)$, we only need to compute the elements that do not commute with $r$, which gives the following:
$$\begin{align}
frf^{-1}=r^3 \\
(rf)r(rf)^{-1}=r^3 \\
(r^2f)f(r^2f)^{-1}=r^3 \\
(r^3f)f(r^3f)^{-1}=r^3 
\end{align}$$
Thus $\text{cl}_{D_{4}}(r)=\{r,r^3 \}$.

In order to compute $\text{cl}_{D_{4}}(f)$ we don't need to compute $e,r^2,f,r^2f$ since all of these elements commute with $D_4$ and thus we see that:
$$\begin{align}
rfr^{-1}=r^2f \\
r^3f(r^3)^{-1}=r^2f \\
(rf)f(rf)^{-1}=r^2f \\
(r^3f)f(r^3f)^{-1}=r^2f 
\end{align}$$
And thus we have that$\text{cl}_{D_{4}}(f)=\{f,r^2f \}$. For $\text{cl}_{D_{4}}(rf)$ we know that $|\text{cl}_{D_{4}}(f)|>1$ since it does not commute with all elements in the groups, and by pigeon hole principle it must contain $r^3f$ and thus $\text{cl}_{D_{4}}(rf)=\{ rf,r^3f\}$. 

We can express $D_4$ as a disjoint union in the following:
$$D_{4} = \{e \} \cup \{r^2\} \cup \{ r,r^3 \} \cup \{f,r^2f \} \cup \{r,r^3f \}$$
Visually this can be seen in the following:

<table style="border-collapse:collapse;text-align:center;">
<tr>
<td rowspan="2" style="background:#f8c9c9;border:1px solid black;padding:10px;">e</td>
<td rowspan="2" style="background:#cfd2ff;border:1px solid black;padding:10px;">r</td>
<td style="background:#cfd2ff;border:1px solid black;padding:10px;">f</td>
<td style="background:#cfd2ff;border:1px solid black;padding:10px;">r²f</td>
</tr>
<tr>
<td style="background:#cfd2ff;border:1px solid black;padding:10px;">rf</td>
<td style="background:#cfd2ff;border:1px solid black;padding:10px;">r³f</td>
</tr>
<tr>
<td style="background:#f8c9c9;border:1px solid black;padding:10px;">r²</td>
<td style="background:#cfd2ff;border:1px solid black;padding:10px;">r³</td>
<td colspan="2" style="border:none;"></td>
</tr>
</table>
---
# Additional Remarks
### Theorem).
Every [[Normal Subgroup]] is the union of [[Conjugacy Class]]es. 

$Proof).$
Suppose that $n \in N \triangleleft G$, then $gng^{-1} \in gNg^{-1} = N$. If $n \in N$ then its entire conjugacy class is contained in $N$ as well. 

## Theorem). 
Conjugate elements have the same [[Order]]. 

$Proof.)$ 
Consider $x,y=gxg^{-1}$ where $|x|=n$ then:
$$\begin{align}
y^n=(gxg^{-1})^n \iff  \\
y^n=gx^ng^{-1} \iff \\
y^n=e \\
\therefore |y|=n = |x|
\end{align}$$
---
# Structure Preservation
## Connections to [[Symmetric Group]]s 
If two elements in $S_{n}$ have the same cycle type, then when each is written as a product of disjoint cycles, there are the same number of length $k$ cycles for each $k$. 

For any $\sigma \in S_{n}$ we can write the cycle type as a list of $n$ integers as $c_{1},c_{2},\cdots,c_{n}$. For instance:
$$\begin{align}
(18)(5)(23)(4967) \longrightarrow 1,2,0,1 \\
(18424967) \longrightarrow 0,0,0,0,0,0,0,1 \\
\epsilon \longrightarrow 9,0,0,\cdots,0
\end{align}$$
## Theorem).
Two elements, $g,h \in S_{n}$ are conjugate $\iff$ they have the same cycle type. The intuition behind this idea is that permutations are essentially the same up to renumbering. 

For instance given $g=(12)$ and $h=(23)$ and lastly $r=(123456)$ then:
$$(123456)(23)(123456)^{-1}=(12)$$
Visually this can be observed in the following:

```tikz 
\usepackage{tikz}
\begin{document}


\begin{tikzpicture}[
    scale=1.0,
    every node/.style={circle, draw, minimum size=7mm, inner sep=0pt, font=\small},
    redv/.style={fill=red!60},
    yellowv/.style={fill=yellow!60},
    greenv/.style={fill=green!60},
    bluev/.style={fill=blue!60},
    pinkv/.style={fill=red!20},
    >=stealth
]

% ---------------- TOP LEFT ----------------
\begin{scope}[shift={(0,0)}]

\node[redv]    (a1) at (0,2) {1};
\node[yellowv] (a2) at (1.5,1.2) {2};
\node[greenv]  (a3) at (1.5,0) {3};
\node[bluev]   (a4) at (0,-0.8) {4};
\node[pinkv]   (a5) at (-1,-0.2) {5};
\node[greenv]  (a6) at (-1,1.2) {6};

\end{scope}

% ---------------- TOP RIGHT ----------------
\begin{scope}[shift={(7,0)}]

\node[yellowv] (b1) at (0,2) {1};
\node[redv]    (b2) at (1.5,1.2) {2};
\node[greenv]  (b3) at (1.5,0) {3};
\node[bluev]   (b4) at (0,-0.8) {4};
\node[pinkv]   (b5) at (-1,-0.2) {5};
\node[greenv]  (b6) at (-1,1.2) {6};

\draw[->,thick]
    (b1) to[bend left=40] (b2);
\draw[->,thick]
    (b2) to[bend left=40] (b1);

\end{scope}

% g arrow
\draw[->,thick] (2.5,1) -- (4.8,1)
    node[midway,above] {$g=(12)$};

% ---------------- BOTTOM LEFT ----------------
\begin{scope}[shift={(0,-5)}]

\node[greenv]  (c1) at (0,2) {1};
\node[redv]    (c2) at (1.5,1.2) {2};
\node[yellowv] (c3) at (1.5,0) {3};
\node[greenv]  (c4) at (0,-0.8) {4};
\node[bluev]   (c5) at (-1,-0.2) {5};
\node[pinkv]   (c6) at (-1,1.2) {6};

\end{scope}

% ---------------- BOTTOM RIGHT ----------------
\begin{scope}[shift={(7,-5)}]

\node[greenv]  (d1) at (0,2) {1};
\node[yellowv] (d2) at (1.5,1.2) {2};
\node[redv]    (d3) at (1.5,0) {3};
\node[greenv]  (d4) at (0,-0.8) {4};
\node[bluev]   (d5) at (-1,-0.2) {5};
\node[pinkv]   (d6) at (-1,1.2) {6};

\draw[->,thick]
    (d2) to[bend left=40] (d3);
\draw[->,thick]
    (d3) to[bend left=40] (d2);

\end{scope}

% h arrow
\draw[->,thick] (2.5,-4) -- (4.8,-4)
    node[midway,above] {$h=(23)$};

% vertical arrows r
\draw[->,thick] (0,-1.6) -- (0,-2.8)
    node[midway,right] {$r$};

\draw[->,thick] (7,-1.6) -- (7,-2.8)
    node[midway,right] {$r$};

\end{tikzpicture}

\end{document}
```


### Connections to Linear Algebra
If two Matrices ([[Matrix]]) are [[Similar Matrices]], then we can say that:
$$A=PBP^{-1}$$
And that the eigenvectors, eigenvalues, determinants, and maps under a change of basis are the same in each under conjugation. 