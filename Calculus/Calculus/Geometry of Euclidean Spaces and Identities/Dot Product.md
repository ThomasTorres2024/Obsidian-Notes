---
title: Dot Product
tags:
draft: "false"
---
# Dot Product Definition
The dot product is an an operation which takes, $\mathbb{R}^n \to \mathbb{R}$, which tells us how much one vector aligns with the direction of another vector when we perform a [[vector projection]].

Given $\vec{x},\vec{y}\in \mathbb{R}^n$, then we define our dot product by:
$$\vec{x} \cdot \vec{y} = \sum_{i=1}^n x_{i}y_{i}=x_{1}y_{1}+x_{2}y_{2}+\cdots+x_{n}y_{n}$$
Note that the dot product is an operation which takes, $\mathbb{R}^n \to \mathbb{R}$. 

The dot product has the following properties:
1. Positive Definiteness
$$\vec{x} \cdot \vec{x} =\sum_{i=1}^n x_{i}^2 \geq 0 \text{ only 0 iff } \vec{x} = \vec{0}$$
2. Constants are commutative
$$(c\vec{u})\cdot \vec{v}=\vec{u}\cdot(c\vec{v})=c(\vec{u} \cdot \vec{v})$$
3. Distributive Rule 
$$\vec{u}\cdot(\vec{v}+\vec{w})=\vec{u}\cdot\vec{v}+\vec{u}\cdot \vec{w}$$
4. Commutative 
$$\vec{v} \cdot \vec{u}=\vec{u} \cdot \vec{v}$$

We define the [[Euclidean Norm]] of a [[Vectors]] given by:
$$\|v\|_{2} = \sqrt{\left( \sum_{i=1}^n v_{i}^2 \right)}=\sqrt{v_{1}^2+v_{2}^2+\cdots + v_{n}^2}$$
Note that $v \cdot v = \| v\|^2$. This is a very useful equation. The dot product is at its largest when vectors are parallel to one another and facing in the same direction, smallest when they vectors are anti-parallel, and orthogonal when the dot product is 0. 

---
# Cosine Angle Identity 

We can also define the cosine identity using the dot product between $\vec{x},\vec{y}$ for the angle $\theta$ in the range of $0 \leq \theta \leq \pi$. When we move beyond $\mathbb{R}^3$, we lose the ability to see our angle. When we generalize our angle beyond the third dimension, we consider the angle to lie within a plane, a 2d subspace of $\mathbb{R}^n$. We can consider their angle in this way. 

The cosine identity states that:
$$u\cdot v = \|u\|\|v\| \text{cos}(\theta)$$
We could solve for angles in higher dimensions by considering the plane they are constrained on and doing some less than pleasant math, or we could just use this formula and get a much easier result much quicker. 

This equation can be derived by vector projections, or by the law of cosines. I prefer deriving it with vector projections. We can solve for the angle $\theta$ in this way:
$$\theta = \text{cos}^{-1}\left(\frac{u \cdot v}{\|u \| \|v\|}\right)$$
Notice that we are only allowed to do this because we restrict our domain to be within the range of $0 \leq \theta \leq \pi$. When we constrain our interval we can only get one answer. Otherwise, our inverse functions wouldn't mean much, and this is why we place a constraint on our [[Inverse Cosine]] function. 

So we can conclude that the above inverse is fine. We want our dot product to have a unique answer, which forces our two vectors when they share a dot product of zero to have the unique angle of $\theta =\frac{\pi}{2}$:
$$u \perp v \Longleftrightarrow u \cdot v = 0$$
#### (Note) On connection to the Inner Product
The dot product is a subset of the set of all inner products. The inner product induces a norm, which allows us to define the notion of angles. For more general inner products, we can use the angle given by the cosine identity when we consider abstract spaces like those of polynomials, matrices, or things that are more exotic. 

This gives us the conclusion that the cosine and sine are orthogonal functions which will be very useful for Fourier analysis.

---
# Cauchy-Schwarz Inequality 
We also have this famous inequality which states that for $x,y$ that:
$$|x \cdot v | \leq \|x\| \|v\|$$
This comes from the cosine identity above, and since cosine is constrained between 1 and -1 it follows easily:
$$\frac{|\vec{u} \cdot \vec{v}|}{\|\vec{u}\|\vec{v}\| } = |\text{cos}(\theta)| \leq 1$$
--- 
# Triangle Inequality 
For $\vec{x},\vec{y}$ we have that:
$$\| x + y\| \leq \|x\| + \|y\|$$
This is to say that for any given side in a triangle, that the sum of the other two sides is always greater than or equal to it, and only equal in the case where the vectors added are  [[Linearly Dependent]]. 

We can prove this result using the [[Cauchy-Schwarz Inequality]], and is connected to it:
$$\|x+y\|=\|x\|^2+2(x\cdot y)+\|y\|^2$$
Again by [[Cauchy-Schwarz Inequality]] we have that:
$$\|x\|^2 +2(x \cdot y) + \|y\|^2 \leq \|x\|^2+2\|x\|\|y\| + \|y\|^2$$
Which gives us the triangle inequality as stated above.

---
# Orthogonal Projection
The projection of a vector $\vec{v}$ onto $\vec{u}$ is just a constant multiple of vector $\vec{u}$, so it is $c \cdot \vec{u}$. 

It turns out that the constant is:
$$c=\frac{(v \cdot u)}{\|u\|^2}$$
So our parallel component or projection of $\vec{v}$ onto vector $\vec{u}$ is given by:
$$\vec{u}\frac{(\vec{v} \cdot \vec{u})}{\|u\|^2}$$

The way you derive this expression is by dotting the orthogonal component of our parallel part, which gives us the above formula:
$$\vec{u_{\perp}}+\vec{u}\cdot c = \vec{v} \Longleftrightarrow \vec{u}_{\perp}=\vec{v}-\vec{u}\cdot c$$
$$\vec{u}_{\perp}^T\vec{u}=(\vec{u}\cdot\vec{v}-\|u\|_{2}^2c)=0$$
$$\Longleftrightarrow c =\frac{\vec{u} \cdot \vec{v}}{\| \vec{v} \| \|\vec{u} \|}$$
