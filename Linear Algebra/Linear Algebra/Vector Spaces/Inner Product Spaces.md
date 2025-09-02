---
title: Inner Product Spaces
tags: 
draft: "false"
---
# Inner Product Spaces Introduction 

The inner product can be thought of as a generalization of the standard dot product that is defined over $\mathbb{R}^n$, such that we can bring a lot of the nice concepts we work with in Euclidean geometry such as angles and lengths into other vector spaces. 

The standard inner product for $\vec{x},\vec{y},\vec{z} \in \mathcal{V}$ over the reals is given by: 

$$\vec{x}\cdot \vec{y} = \vec{x}^T\vec{y}=\sum_{i=1}^n \vec{x}_{i}\cdot \vec{y}_{i}$$
For the complex numbers we have:

$$\vec{x}\cdot \vec{y} = \vec{x}^H\vec{y}=\sum_{i=1}^n \overline{\vec{x}_{i}}\cdot \vec{y}_{i}$$
Where we take the complex conjugate of each element in $\vec{x}$. We do this because we can calculate magnitudes with the inner product:

$$\vec{x} \cdot \vec{x }=\vec{x}^H\vec{x}=|x_{1}|^2+|x_{2}|^2+\cdots+|x_{n}|^2$$
To obtain the magnitude of the vector, all we would need to do is take the square root of each of its components squared: 

$$\| \vec{x} \|=\sqrt{\vec{x}^H\vec{x}}=\sqrt{|x_{1}|^2+|x_{2}|^2+\cdots+|x_{n}|^2}$$

This is where the notion of distance comes from in relation to inner product spaces. We can also define cosine along inner product spaces. 

---
# Cosine Derivation 

We can define cosines given two vectors, $\vec{x},\vec{y} \in \mathcal{V}$ given it is an inner product space by using orthogonal projection. We will project $\vec{x}$ onto $\vec{y}$. 

We can express $\vec{x}$ as the sum of a vector orthogonal to $\vec{y}$ denoted by $\vec{x}_{\perp}$ and by a vector parallel to $\vec{y}$, which scales the vector by some amount, $c$. 

Thus, we get the following set of relations: 

$$\vec{x}_{\perp}+c \cdot \vec{y}=\vec{x}$$
$$\vec{x}_{\perp}=\vec{x}-c\cdot \vec{y}$$
We know that this vector must be orthogonal to $\vec{y}$, so we can compute its inner product, and it will evaluate to zero: 

$$\vec{x}_{\perp}\vec{y}=\vec{x}^H\vec{y}-c\vec{y}^H\vec{y}=0$$
$$\Longleftrightarrow \vec{x}^H\vec{y}=c\vec{y}^H\vec{y}$$
$$\Longleftrightarrow c=\dfrac{\vec{x}^H\vec{y}}{\vec{y}^H\vec{y}} = \dfrac{<\vec{x},\vec{y}>}{\| \vec{y} \|^2}$$

The side adjacent to our angle is the projection given by $\vec{y} \cdot \dfrac{<\vec{x},\vec{y}>}{\| \vec{y} \|^2}$, and the hypotenuse is given by $\vec{x}$, and the opposite side is given by $\vec{x}_{\perp} = \vec{x}-\vec{y} \cdot \dfrac{<\vec{x},\vec{y}>}{\| \vec{y} \|^2}$. This forms a right triangle since $\vec{x}_{\perp}$ is orthogonal to $\vec{y}$. We can use the fact that $\text{cos}(\theta)=\dfrac{\text{a}}{\text{h}}$ to give: 

$$\text{cos}(\theta)=\dfrac{\text{a}}{\text{h}}=\dfrac{<\vec{x},\vec{y}> \|y \|}{\| \vec{y} \|^2 \|x\|}= \dfrac{|<\vec{x},\vec{y}>|}{\|y\| \| x\|} $$
We restrict the value of the dot product to be positive with the absolute value to restrict our angle. 

---
# Properties of Inner Product Spaces 

The form which an inner product takes may change depending upon the type of vector space that we are examining, however, to even define an inner product for an arbitrary vector space $\mathcal{V}$ with associated field $\mathbb{F}$, the following criteria must be satisfied in order for an inner product to be definable on it. 

If we are working over $\mathbb{F}=\mathbb{R}$, then our inner product rules are as such: 
1. $<\vec{x},\vec{x}> \text{ } \mathbf{\geq}  0$
2. $<\vec{x},\vec{x}> = 0 \Longleftrightarrow \vec{x} =\vec{0}$
3. $<\vec{x},\vec{y}>={<\vec{y},\vec{x}>}$ (symmetric)
4. $<\vec{x},\alpha\vec{y}+\beta\vec{z}> \text{ } = \alpha <\vec{x},\alpha\vec{y}> + \beta<\vec{x},\vec{z}>$ (bilinearity)

If we are working over $\mathbb{F}=\mathbb{C}$, then our inner product rules are as such: 

1. $<\vec{x},\vec{x}> \text{ } \mathbf{\geq}  0$
2. $<\vec{x},\vec{x}> = 0 \Longleftrightarrow \vec{x} =\vec{0}$
3. $<\vec{x},\vec{y}>=\overline{<\vec{y},\vec{x}>}$ (the bar denotes conjugation, so conjugate symmetry)
4. $<\vec{x},\alpha\vec{y}+\beta\vec{z}> \text{ } = \alpha <\vec{x},\vec{y}> + \beta<\vec{x},\vec{z}>$ (linearity in the second argument, sesquilinear)

The first property ensures positive semi-definiteness, which means that all vectors are guaranteed to have a length above $0$ when we look at their magnitude squared, which is given by an inner product with itself. The second property ensures that the inner product is positive definite, only evaluating to $0$ when $\vec{x} =\vec{0}$, meaning all other vectors must evaluate to a positive magnitude. 

The third property is symmetry over the reals, as we can commute real numbers without any problem when we perform an inner product. For complex numbers, we perform the complex conjugate on $\vec{x}$, so we must take the conjugate in order to cause the signs to flip back for the complex values in $\vec{y}$ and to flip the sign in $\vec{x}$. 

The real inner product is symmetric in both arguments due to us having real numbers we can freely commute, and is linear only in the second argument in the complex case since we conjugate the first argument. 

All of these properties induce a vector norm as well. Since the Cauchy-Schwarz identity is automatically true for such a space, the triangle rule for norms is automatically satisfied, which is a step we can use to prove this rule.  

---
# Proof of the Cauchy-Schwarz Inequality 

The Cauchy-Schwarz identity states that for $\vec{x},\vec{y} \in \mathcal{V}$ where $\mathcal{V}$ is an inner product space, that: 

$$|\vec{x}\cdot \vec{y}| \leq \| \vec{x} \| \| \vec{y} \|$$

Let us begin by examining $\| \beta \vec{x} - \vec{y}] \|^2$ where $\beta \in \mathbb{R}$:

$$\| \beta \vec{x} - \vec{y}] \|^2=(\beta\vec{x}-\vec{y})^T(\beta\vec{x}-\vec{y})=\beta^2\vec{x}^T\vec{x}-\beta\vec{x}^T\vec{y}-\beta\vec{y}^T\vec{x}+\vec{y}^T\vec{y}$$
$$=\beta^2\|\vec{x}\|^2-2\beta<\vec{x},\vec{y}>+\| \vec{y} \|^2 \geq 0$$
We can think of this as a quadratic equation. Since $\vec{x}$ and $\vec{y}$ belong to an inner product space, $\| \beta \vec{x} - \vec{y }\| ^2 \geq 0$. We can treat the above identity as a quadratic equation which is greater than or equal to zero at all values of $\beta$. We can use the quadratic equation to solve for its roots. 

Since the parabola opens upward and is at least centered at zero, this means that its discriminant will result in a complex value, so it must contain a negative under the radical sign. That is to say: 

$$\sqrt{(-2<\vec{x},\vec{y}>)^2-4\|x\|^2|y|^2} \in \mathbb{C}$$
Which indicates that:

$$(-2<\vec{x},\vec{y}>)^2-4\|x\|^2|y|^2\leq 0$$
$$ \Longleftrightarrow 4<\vec{x},\vec{y}>^2 \leq 4\|x\|^2|y|^2\leq $$
$$\Longleftrightarrow |\vec{x} \cdot \vec{y}| \leq \|x\||y| $$
Which finally yields the Cauchy-Schwarz inequality. 

Intuitively, I think of this inequality as a corollary from the cosine identity. Since we know that $\text{cos}(\theta)=\dfrac{|\vec{x} \cdot \vec{y}|}{\| \vec{x} \| \| \vec{y} \|}$, we know cosine is bound between $-1$ and $1$, and for most cases, unless the vectors are oriented in the same direction and thus linearly dependent, it is the case that the hypotenuse will be greater than the numerator, so our answer would tend to have an absolute value of less than one, which would imply that the denominator is larger. I tend to think of this identity as a concretization of this rather obvious fact, since the hypotenuse in a right triangle is always the largest side. 

