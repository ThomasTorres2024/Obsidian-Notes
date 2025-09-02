---
title: Double Integrals
tags: 
draft: "false"
---
# Double Integral Introduction
The double integral allows us to take the volume of a function over a general non-square region. 

Consider a function $f$ over the region $R$,  where $f(x,y) \geq 0, \forall (x,y) \in R$. We can find the volume of the surface, $z = f(x,y)$. We can approximate the volume of $z$ by performing a Riemann sum in $\mathbb{R}^3$ where instead of computing blocks of area, we compute blocks of volume over $R$ to find our desired volume. 

We can finitely partition $R$ over a grid. We can consider each $(x_{i},y_{i})$ in the grid and the corresponding value $z_{i}=f(x_{i},y_{i})$. From this, we can calculate the volume of a rectangular prism with height $z_{i}$ and base of $\Delta A_{i}$. The volume of this prism is given by: 

$$f(x_{i},y_{i}) \Delta A_{i}$$

We can approximate the total volume over $R$ by: 

$$\sum_{i=1}^nf(x_{i},y_{i}) \Delta A_{i}$$
We can improve our approximation by decreasing the size of each $\Delta A_{i}$, which tightens the grid over our region $R$. 

We can define the volume over the total region $R$ by using a limit: 

$$\text{Volume} = \lim_{\| \Delta \| \rightarrow0} \sum_{i=1}^nf(x_{i},y_{i}) \Delta A_{i}$$

A more formal way to think of this limit is, we can state that the limit is equal to $L$ if for every $\epsilon > 0$ that $\exists \delta > 0$ such that

$$ \left| L - \sum_{i=1}^n f(x_{i},y_{i}) \Delta A_{i} \right| < \epsilon $$

$\forall \text{ partitions of } \Delta$ which satisfy $\| \Delta \| < \delta$ and for all choices of $x_{i}$ and $y_{i}$ in the $i$th region. 

The limits of this particular definition is limited to a case where $f$ is positive and continuous, however the general argument does not to need the function be positive or continuous. 

---
# Intuition behind Double Integrals 
We can think of a double integral finding an original area through some region, and then continually adding more and more through another set of points until we end up accruing volume on the maximum intervals of our region:
![[Pasted image 20250626214856.png]]
We can interpret our standard integral as:
$$\int \int_{R}f(x,y)\text{ }dA=\int_{x \text{ min}}^{x \text{ max}} \left[\int_{y\text{ min(x)}}^{y \text{ max(x)}}f(x,y)\text{ }dy\right]dx=$$
We go from the furthest bounds one one end to the furthest bounds on another to integrate over the whole region. 

---
# Definitions and Properties of Double Integrals 
We can define the volume over a region $R$ and equivalently the double integral of $f$ over $R$ as: 

$$\int \int_{R} f(x,y) \text{ } dA = \lim_{\| \Delta \ \rightarrow 0|} \sum_{i=1}^n f(x_{i},y_{i}) \text{ } \Delta A_{i}$$

This definition only holds if the limit exists and implies that $f$ is integrable over $R$. Otherwise, $f$ is not integrable over $R$. 

Some sufficient conditions for the double integral of $f$ on $R$ to exist are if $R$ can be written as a union of finite non-overlapping sub regions that are "vertically and horizontally simple" and that $f$ is continuous over $R$. 

We can define volume to be: 

$$V=\int \int _{R} \text{} f(x,y) dA$$

where $f(x,y) \geq 0 \forall, (x,y) \in R$, which results in the solid lying above the $xy$ plane 

---
# Properties of Double Integrals 
Let $f$ and $g$ be continuous over the closed region $R$, and let c be a constant 

1. We can factor constants out of double integrals:$$\int \int_{R} \text{} cf(x,y) dA = c \int \int_{R} \text{} f(x,y) dA$$
2. We can split up the sum of functions into 2 separate integrals $$\int \int_{R} \text{} (f(x,y)+g(x,y) )dA= \int \int_{R} \text{} f(x,y) dA+ \int \int_{R} \text{} g(x,y) dA$$
3. Our integral's volume is guaranteed to be non-negative if every point along the function is non-negative: $$f(x,y) \geq 0 \implies \int \int_{R} \text{} f(x,y) dA \geq 0$$
4. The double integral of a function $f$ which is greater than all values of $g$ over some region will have a larger volume: $$ f(x,y) \geq g(x,y) \implies \int \int_{R} \text{} f(x,y) dA \geq  \int \int_{R} \text{} g(x,y) dA$$
5. We can partition an integral into 2 non-overlapping sub regions: $$ \int \int_{R} \text{} f(x,y) dA =  \int \int_{R_{1}} \text{} f(x,y) dA +  \int \int_{R_{2}} \text{} f(x,y) dA$$

---
# Fubini's Theorem 
The following result is true if $R$ is vertically or horizontally simple region (we can decompose it how we normally would when setting up a double integral where x and y are dependent on one another for the region) , and $f$ is continuous on $R$. 

It follows that: 

$$ \int \int_{R} \text{} f(x,y) dA =  \int_{a}^{b} \int_{g_{1}(x)}^{g_{2}(x)} \text{} f(x,y) dydx$$

and 

$$ \int \int_{R} \text{} f(x,y) dA =  \int_{c}^{d} \int_{h_{1}(y)}^{h_{2}(y)} \text{} f(x,y) dxdy$$

Where $h_{1}$ and $h_{2}$ are continuous along $[c,d]$ and $g_{1}$ and $g_{2}$ is continuous along $[a,b]$. 

Intuitively, we can define our region of integration with respect to either dy or to dx first. The choice is arbitrary from a formal perspective, but from a computational one, we can choose the better bounds of integration in order to make computing the integral simpler. 

Some orders of integration cannot be computed, and will need to use numerical methods to solve, whereas if we switch the order of integration via Fubini we can actually obtain a precise result. 

---
# Applications
#### 1.Region Bounded Between Two Surfaces 

If we are given 2 surfaces, $z=f_{1}(x,y)$ and $z=f_{2}(x,y)$ we can equate the two surfaces and find the region on which both of them are defined.

Assume that the greater function is $f_{1}$, that is to say $f_{1}(x,y) \geq f_{2}(x,y) \forall (x,y) \in R$, then it follows that the area bounded between both regions is: 

$$ \int \int_{R} \text{} (f_{1}(x,y)-f_{2}(x,y))dA$$
#### 2. Average Value of a Function 

In the single variable case, we define the average value of a function over a region as: 

$$  \dfrac{1}{b-a} \int_{a}^b \text{} f(x) dx$$

We can extend this notion to double integrals for $f(x,y)$ over $R$:

$$ \dfrac{1}{A} \int \int_{R} \text{} f(x,y) dA$$
$A$ is the area of the region $R$. 
#### 3. Determine the Area of a Region
We can use a double integral to determine the area of a region we are integrating over:
$$\text{Area}(R)=\int\int_{R}1\cdot dA$$
We can use a variation of this where we have  $\delta$ ass our mass per unit, and if we have a flat surface we can use double integrals to represent the mass of the surface:
$$\text{Mass}=\int\int_{R}\delta\cdot dA$$
A triple integral would allow us to do this for general solids in space. 
#### 4. Weighted Average 
We can find the mass with a weighted density over some region by computing:
$$\text{Mass}= \dfrac{1}{\text{Mass}(R)} \int \int_{R} f\delta \cdot dA $$
#### 5. Center of Mass 
The center of mass is the average of the x and y positions of a flat mass. Its coordinates are given by double integrals:
$$\bar{x}=\dfrac{1}{\text{Mass}} \int \int x \cdot\delta  \cdot dA$$
$$\bar{y}=\dfrac{1}{\text{Mass}} \int \int y \cdot\delta  \cdot dA$$
#### 6. Moment of Inertia 
The moment if inertia is the rotational equivalent of how hard it is to move an object in rotational motion, it is the analog of mass in translational motion. It's something that can be done. I don't really care to write about this, this is a very physics example. 