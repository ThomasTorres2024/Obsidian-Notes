---
title: Numerical Analysis
tags:
  - Numerical_Analysis
draft: "False"
---
# Calculus Review 1.)
### Definition). [[Limit]] Via Epsilon Delta 

[[Continuous Function (Class)]]  
[[Differentiable Function]] 

### Theorems 1.6
Differentiability -> Continuity 
Converse generally not true

### Theorem 1.7 Rolle's Theorem
Suppose $f \in C[a,b]$ and $f$ is differentiable on $(a,b)$. If $f(a)=f(b)$, then $\exists c \in (a,b)$ s.t. $f'(c)=0$. 

### Theorem 1.8 Mean Value Theorem
Suppose $f \in C[a,b]$ and $f$ is differentiable on $(a,b)$. If $f(a)=f(b)$, then $\exists c \in (a,b)$ s.t. 
$$f'(c)=\frac{f(b)-f(a)}{b-a}$$
### Theorem 1.11 Intermediate Value Theorem
If $f$ is continuous on $[a,b]$ and $K$ is any number in between $f(a)$ and $f(b)$, then there exists a number $c \in (a,b)$ such that $f(c)=K$. 


#### Example).
Using the intermediate value theorem to show that $5x^3+2x^2-4x=0$ has at least one solution in a given interval.
##### Solution
Calculate endpoint values, $f(-1)=1,f(0.5)=-8.75$ and since $0 < -8.75 < 1$ then by the IVT $\exists c$ s.t. $f(c)=0$. For completeness determine all such intervals and argue from that, determine the total number of zeroes 

### Theorem 1.9 EVT 
If $f \in C[a,b]$ then $c_{1},c_{2} \in [a,b]$ exist with $f(c_{1}) \leq f(x) \leq f(c_{2})$ $\forall x \in [a,b]$, and $c_{1},c_{2}$ either coincide with some $x$ s.t. $f'(x)=0$ OR we use the endpoints.

### Theorem 1.14 [[Taylor Series]] (Taylor's Theorem)
Intuitively we can think of this as if $x$ and $x_0$ are closen, in the definition of the derivative then:
$$f'(x) \approx \frac{f(x)-f(x_{0})}{(x-x_{0})} \implies f'(x)(x-x_{0})+f(x_{0})\approx f(x)  $$
(Add parts to the residual)

Example taylor polynomial for $n=2$ for $\cos(x)$:
$$P_{2}(x)=1-\frac{x^2}{2}$$
And then:
$$\cos(x)=1 - \frac{1}{2}x^2 + R_{2}(x) \quad R_{2}(x)= \frac{1}{6}x^3 \sin(\eta(x)) $$
Where $R_{2}(x)$ is the residual function.

Residual functions are important. If we have an upper bound for the function, we can determine a general approximation with our given taylor series, which we ca determine from:
$$f(x)-P_{3}(x)=R_{3(x)}$$
$$\text{max}_{x_{0}  \leq x_{2} \leq x_{1} }$$

---
# Round-off Errors and Computer Arithmetic 
Representing and doing calculations with results can cause errors. This does and will happen to us in all areas, linear systems, integrals, ODEs, etc. In a computer environment we need to be able to use a finite representation for any [[Real Number]]

Assyme that any machine number is represented in $k$ digit normalized form by:
$$f(y)= \pm_{0}.d_{1}d_{2}\dots d_{k}\cdot 10^n$$
For $1\leq  d_{1} \leq 9$. Say for example we want to represent with $k=4$ the number $201.7$ which is:
$$0.2017 \cdot 10^4$$
---
## How do we represent irrational numbers like $\pi,e$?
For one, we have chopping, where we chop of all values after some $k$:
* Chopping $e$ to $k=3$ gives $0.271 \cdot 10^3$
For rounding we use the $k+1$st digit to round the $k$th digit how we normally would:
* Rounding $e$ to $3$: $2.72=0.272\cdot 10^3$

To do any math with these numbers numerically we must perform the following

1. Represent numbers as finite digits rounding or chopping
2. Do operation using real arithmetic 
3. Convert back to finite digit representation

#### Example).
We want to find $\frac{e}{\pi}$. First we convert:  $\pi \to 3.141 \quad e\to {2}.718$
$$\frac{e}{\pi} \approx 0.8653 \bigg|29513 \to 0.8653$$
Notice that in this example we are __already off by a digit__, $\frac{e}{\pi} \approx 0.8652$. 

---
# Round off Error and Computer Arithmetic 

If $p$ is an approximation to $p^*$ then the absolute error is $|p^*-p|$ (here the exact we call is matlab's precision of up to 16 digits). 

Here the relative error is: $\frac{|p^*-p|}{|p^*|}$. 

In numeric representation for exact $y$:

Chopping $\frac{|y-fl(y)|}{|y|} \leq 10 \times 10^{-4}$
Rounding $\frac{|y-fl(y)|}{|y|} \leq 5 \times 10^{-4}$

In actual accuracy and significant digits we make use of relative error, if the following criteria is satisfied it means that we have $k$ significant digits in an approximation to $p^*$:
 $$\frac{|p^*-p|}{|p^*|} \leq 5 \times 10^{-4}$$
 When it comes to computing these things we should always compute things from left to right, as by order of operations.  
 
---

#### Example) Quadratic Formula
Consider $0.999x^2+59.4x+0.883=0$. We will use 3 digit chopping. Notice that eat number provided has $3$ significant digits. We will apply the formulas to obtain $x_{1},x_{2}$. 

Recall the quadratic formula:
$$x= \frac{-b \pm \sqrt{ b^2-4ac } }{2a}$$
Here for $b^2$, we need to $(59.4)^2=3528.36 = 0.35286 \cdot 10^4$, and then with chopping $3$ digits we get $3520$ so, $b^2 = 3520$. We can do the same for $4ac$, first we need to compute $(4a)=3.99$ and then $(4a)c=(3.99)(0.883)=3.523=3.52$ 

And then $b^2-4ac=3520-3.54=3516.48=3510$. Now we consider the square root, $\sqrt{ b^2-4ac }=\sqrt{ 3510 }\approx 59.24=59.2$. Now we need to handle the $\pm$:
$$\begin{align}
-59.4 + 59.2 = -0.2 \\
-59.4 - 59.2 = -118
\end{align}$$
And then from $2a=1.99$, we divide our above numbers by them and we get:
$$x_{1}=-0.100 \quad x_{2}=-59.2$$
Now when we minus by our "exacts" we get the following relative errors:

$$\text{rel}(x_{1})=5.725$$
$$\text{rel}(x_{2})=0.00411 \leq 5 \cdot 10^{-3} \to 4.11 \leq 5$$
Thus $3$ significant digits for $x_{2}$, but $0$ for $x_1$ since we have such a large rounding error. 

#### How to fix these errors?
Generally we want to avoid subtraction of numbers. Rationalize the numerator of $x_{1}$. 
$$x_{1}= \frac{-b \pm \sqrt{ b^2-4ac }}{2a} \cdot \frac{-b-\sqrt{ b^2-4ac }}{-b-\sqrt{ b^2-4ac }} = \frac{2c}{-b-\sqrt{ b^2-4ac }} $$
And thus by doing computation with the rationalization in mind our relative error here becomes $0.001$ which means that we have $3$ significant digits. 