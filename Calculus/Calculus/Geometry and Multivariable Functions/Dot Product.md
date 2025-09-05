GIven $x,y\in \mathbb{R}^n$, then we define our dot product by:
$$x \cdot y = \sum_{i=1}^n x_{i}y_{i}$$
Note that the dot product is an operation which takes, $\mathbb{R}^n \to \mathbb{R}$. 

The dot product has the following properties:
1. Positive Definiteness 
2. Constants are commutative
3. Distributive Rule 
4. Commutative 

We define the [[Euclidean Norm]] of a [[Vectors]] given by:
$$\|v\|_{2} = \sqrt{\left( \sum_{i=1}^n v_{i}^2 \right)}$$
Note that $v \cdot v = \| v\|^2$. 

We can also define the cosine identity using the dot product between $x,y$ for the angle $\theta$ in the range of $0 \leq \theta \leq \pi$. When we move beyond $\mathbb{R}^3$, we lose the ability to see our angle. When we generalize our angle beyond the third dimension, we consider the angle to lie within a plane, a 2d subspace of $\mathbb{R}^n$. We can consider their angle in this way. 

The cosine identity states that:
$$u\cdot v = \|u\|\|v\| \text{cos}(\theta)$$
This equation can be derived by vector projections, or by the law of cosines. We can solve for the angle $\theta$ in this way:
$$\theta = \text{cos}^{1}(\frac{u \cdot v}{\|u \| \|v\|})$$
Notice that we are only allowed to do this because we restrict our domain to be within the range of $0 \leq \theta \leq \pi$. When we constrain our interval we can only get one answer. 

So we can conclude that the above inverse is fine. We want our dot product to have a unique answer, which forces our two vectors when they share a dot product of zero to have the unique angle of $\theta =\frac{\pi}{2}$:
$$u \perp v \Longleftrightarrow u \cdot v = 0$$
The dot product is a subset of the set of all inner products. The inner product induces a norm, which allows us to define the notion of angles. For more general inner products, we can use the angle given by the cosine identity when we consider abstract spaces like those of polynomials, matrices, or things that are more exotic. 

This gives us the conclusion that the cosine and sine are orthogonal functions. 

---
# Cauchy-Schwarz Inequality 
We also have this famous inequality which states that for $x,y$ that:
$$|x \cdot v | \leq \|x\| \|v\|$$
This comes from the cosine identity above, and since cosine is constrained between 1 and -1 it follows easily. 

--- 
# Triangle Inequality 
For $x,y$ we have that:
$$\| x + y\| \leq \|x\| + \|y\|$$
---
# Orthogonal Projection
The projection of a vector $v$ onto $u$ is just a constant multiple of vector $u$, so it is $c \cdot u$. 

It turns out that the constant is:
$$c=\frac{(v \cdot u)}{\|u\|^2}u$$
The way you derive this expression is by dotting the orthogonal component of our parallel part, which gives us the above formula. 