---
title: 
tags: 
draft: "false"
---
# Dual Space Definition

For a [[Vector Space]] $\mathcal{V}$, $\exists \mathcal{V}^*$ another vector space isomorphic to $\mathcal{V}$. This vector space contains all linear forms or linear functionals, that is linear transformations given by $f : \mathcal{V} \rightarrow \mathbb{F}$. 

We know that linear functionals are linear transformations. We can also show that the space of linear functionals is another vector space. Consider linear functionals $f,g \in \mathbb{V}^*, \vec{x} \in \mathbb{V}$, and scalar constants $c \in \mathbb{F}$. It follows that: 

$$f(\vec{x})+g(\vec{x})=(f+g)(\vec{x}) \text{ and thus } (f+g) \in \mathcal{V}^*$$
$$c\cdot f(\vec{x}) \text{ thus } c \cdot f \in \mathcal{V}^*$$
$$\text{The zero map is a mapping in } \mathcal{V}^*$$
In conclusion $\mathcal{V}^*$ is closed under vector addition, scalar multiplication, and is non-empty. Thus $\mathcal{V}^*$ is a vector space. 

Notice that $\mathcal{V}^*=\mathcal{L}(\mathcal{V},\mathbb{F})$. I'm not really sure why but we are able to use a theorem that tells us the dimension of $\mathcal{V}^*=\mathcal{L}=\text{dim}(\mathcal{V}) \cdot \text{dim}(\mathbb{F})=\text{dim}(\mathcal{V})\cdot 1= \text{dim}(\mathcal{V})$. 

This apparently allows us to find an isomorphism between $\mathcal{V}$ and $\mathcal{V}^*$ since they have an equivalent number of basis vectors when $\mathcal{V}$ is a finite dimensional vector space. 

---
# Dual Space Basis 

We will denote the basis of the space $\mathcal{V}$ by $\{\vec{v}_{1},\vec{v}_{2}, \dots , \vec{v}_{n} \}$ and the basis of $\mathcal{V}^*$ by $V=\{f_{1},f_{2}, \cdots f_{n} \}$.

We can determine each $f_{i}$ by evaluating the basis at each identity vector, as is true for any linear transformation. 

We can define a dual basis as the set of functions $f_{i}$ defined by $f_{i}(v_{j}) = \begin{cases} 1 & \text{if } i =j \\ 0 & \text{if } i \neq j \end{cases}$
This is known as the Kronecker delta product. Essentially $f_{i}(\vec{v}_{j})$ evaluates to 1 on the $i$th basis vector and 0 otherwise. 

We can prove that this basis of functionals is indeed a basis of $\mathcal{V}^*$. We can prove that it is linearly independent and spans $\mathcal{V}^*$.

##### I.) Proof of Linear Independence 

We can prove that the basis is linearly independent by showing each $\alpha_{i}=0$ which implies that it is the only linear combination which results in zero, which is the definition of linear independence:

$$\alpha_{1}f_{1}+\alpha_{2}f_{2}+\cdots+\alpha_{n}f_{n}=f_{0}$$

We then evaluate this function on any $\vec{v} \in \mathcal{V}$:

$$\alpha_{1}f_{1}(\vec{v})+\alpha_{2}f_{2}(\vec{v})+\cdots+\alpha_{n}f_{n}(\vec{v})=0$$

If we evaluate this expression at $\vec{v}_{1}$ then it follows that: 

$$\alpha_{1}f_{1}(\vec{v_{1}})+\alpha_{2}f_{2}(\vec{v_{1}})+\cdots+\alpha_{n}f_{n}(\vec{v_{1}})=\alpha_{1}=0$$

This follows since $f_{1}(\vec{v}_{1})=1$, so it follows that $\alpha_{1}=0$. This property is true for each basis vector in the set. 

As a result, each $\alpha_{i}=0$, and therefore it follows that the linear combination which results in $f_{0}$ is strictly when $\alpha_{i}=0$. Therefore, the set is linearly independent. 

##### II.) Proof that the Set Spans $\mathcal{V}^*$

We must show that $g \in \mathcal{V}^*$ can be represented by the following linear combination: 

$$g=\beta_{1}f_{1}+\beta_{2}f_{2}+\cdots+\beta_{n}f_{n}$$

Suppose that this is the case for some $f$. We can solve each $\beta_{i}$. Consider the function evaluated at an arbitrary $\vec{v} \in \mathbb{V}$:

$$f(\vec{v})=\beta_{1}f_{1}(\vec{v})+\beta_{2}f_{2}(\vec{v})+\cdots+\beta_{n}f_{n}(\vec{v})$$

We can determine each $\beta_{i}$ by cleverly choosing our vectors. Let us apply the same trick that we used above when proving linear independence on the basis and select the basis vectors in $\mathcal{V}$:

$$f(\vec{v}_{1})=\beta_{1}f_{1}(\vec{v}_{1})+\beta_{2}f_{2}(\vec{v}_{1})+\cdots+\beta_{n}f_{n}(\vec{v}_{1})=\beta_{1}$$

Therefore, $\beta_{i}=f(\vec{v}_{1})$. Likewise, $\beta_{2}=f(\vec{v}_{2})$ and generally $\beta_{i}=f(\vec{v}_{i})$. 

We simply need to equate that for any $g$ and $f$. If $g$ and $f$ are equivalent on all basis vectors in the basis for $\mathcal{V}$, it follows that $f=g$. 

We would plug $g$ into the place of $f$ on the left from the above statements, and at each step obtain that $f(\vec{v}_{i})=g(\vec{v}_{i})$. Thus, $f=g$.

In conclusion, we can express any arbitrary $f \in \mathcal{V}^*$ as a linear combination of the linear functionals from the set evaluated at their corresponding basis vector.
##### Conclusion

We have shown that the set $V$ is linearly independent and that $\text{span}(V)$ spans $\mathcal{V}^*$, we can conclude that $V$ is a basis for $\mathcal{V}^*$

We have also shown that for any $f \in \mathcal{V}^*$ that: 

$$f=\sum_{i=1}^nf(\vec{v_{i}})f_{i}$$

We can use this to practically calculate the coefficients of the basis functions for the vector space $\mathcal{V}^*$. 

Another Peyam represents in his video that I cannot represent is that each functional in the base can be graphed with respect to each base vector in $\mathcal{V}$ with a spike at $\vec{v_{i}}$ at 1, and 0 for every point in the discrete function. 
 
---
# Dual Space Example 

Consider $\mathcal{V}=\mathbb{R}^2$ with the associated basis $\{ \begin{bmatrix} 2 & 1  \end{bmatrix}^T, \begin{bmatrix} 3 & 1  \end{bmatrix}^T \}$

We are looking to find a basis $\beta^*=\{f_{1},f_{2} \}$ for the vector space $\mathcal{V}^*$. We can begin by using the Kronecker delta function and see that $f_{1}(\begin{bmatrix} 2 & 1  \end{bmatrix}^T)=1$ and $f_{2}(\begin{bmatrix} 3 & 1  \end{bmatrix}^T)=0$. 

The functions $f_{1}$ and $f_{2}$ are expressible as a linear combination of $x+y$, two linear variables since we are working in 2 dimensions:

$$f_{1}=\alpha_{1}x+\alpha_{2}y$$
$$f_{2}=\beta_{1}x+\beta_{2}y$$
Since we know what $f_{1}$ evaluates to for each basis vector in $\mathcal{V}$, we know enough information to find $f_{1}$. We can explicitly write out the linear system below that satisfies the above conditions when evaluated at $[2,1]^T$ and $[3 ,1]^T$ respectively: 

$$2\alpha_{1}+\alpha_{2}=1$$
$$3\alpha_{1}+\alpha_{2}=0$$
Notice that this is a matrix equation which we can simply use Gaussian elimination on to find our alphas: 

$$\begin{bmatrix} 2&1\\3& 1 \end{bmatrix} \begin{bmatrix} \alpha_{1}\\\alpha_{2}\end{bmatrix} = \begin{bmatrix} 1\\0\end{bmatrix}$$

We can likewise do this for the other system for $f_{2}$:

$$\begin{bmatrix} 2&1\\3& 1 \end{bmatrix} \begin{bmatrix} \beta{1}\\\beta{2}\end{bmatrix} = \begin{bmatrix} 0\\1\end{bmatrix}$$

Notice that the calculation is essentially the same. The only difference is that instead of using $\vec{e}_{1}$ we use $\vec{e}_{2}$.

Also note that the matrix we are using is the transposition of the basis:

$$\begin{bmatrix} 2&3\\1& 1 \end{bmatrix}^T=\begin{bmatrix} 2&1\\3& 1 \end{bmatrix} $$

This arises because linear functionals are row vectors that take in a set of inputs and convert them into a scalar, in effect a dot product. When we construct our matrix trying to solve for our $f_{1}$ and $f_{2}$ we lay our coefficients for the basis on their side since in a linear functional, in order to obtain a scalar output we need to evaluate them in the functionals at these points. 

