---
title: Laplace Transform
draft: "false"
tags:
---
# Intuition
The end goal of the [[Laplace Transform]]s is being able to express a function as an equivalent sum of exponential functions given some $s_{i} \in \mathbb{C}$, where we have some $f(t) : \mathbb{R} \to \mathbb{R}$. We should be able to express:
$$f(t)=\sum_{i=1}^{k}c_{i}e^{s_{i}t}: c_{i}\in \mathbb{C}$$
For the sake of [[Differential Equations]] we are hoping to express a differential equation as an algebraic equation, and solve the algebraic equation, and then apply an [[Inverse Laplace Transform]] such that the differential equation is solved in the end:
![[Pasted image 20251221220112.png]]

For instance consider the function $\cos(t)$ which is clearly defined over the reals. We know that through [[Euler's Identity]] that $\cos(t)$ can be expressed using complex exponentials:
$$\cos(t)=\frac{1}{2}(e^{it}+e^{-it})$$

The Laplace transform itself defines some function $F(s)$ corresponding to $f(t)$ such that: $s \mapsto F(s)$. We use the term "[[Transform]]" as a mapping which  constructs a new function $F(s)$ with respect to $s$ for each value of $s$ chosen. If we were to visualize the output, there would be a [[pole]] corresponding to each $s_{i}$ somehow. 

We describe the [[Laplace Transform]] as the following:
$$F(s)=\int_{0}^\infty f(t)e^{-st}dt$$

Our goal is to be able to find these poles and find each $s_{i}$ such that we can express an equivalent version of $f(t)$ with respect the the $s$ space. The integral of this function should be able to detect which points along $S$ cause the function to jump significantly. Here is an example of some function in the $S$ plane using its poles:
![[Pasted image 20251221215016.png]]

---
# Complex Integration
To begin it's important to address the difficulties and changes of integrating in a complex setting compared to a real one. Instead of considering the more general integral given by
$$F(s)=\int_{0}^\infty f(t)e^{-st}dt$$
We instead consider the much simpler integral given by:
$$\int_{0}^\infty e^{-st}dt$$
Our intuition for this operation over the reals is simply the area underneath the curve. If we let $s=1$, then our area is 1. If $s$ large, then the area continues to decrease and heads to $\frac{1}{s}$ overall. But if $s \to 0$ then the area quickly tends towards infinity. We can try to generalize the notion of the integral to the complex plane 

Another way we can consider integration is by examining integration over a unit interval. We can think of it as a center of mass over the unit, and thus the average area over that length since we are only considering an area of 1, we only need to divide the integral by 1. We can then consider the total integral define from $0$ to $\infty$ as being the sum of the average unit areas. This notion of integration can be extended to the complex much easier than the other operation of area under a curve.

We can shift this idea over to the complex numbers now. Consider each unit interval along the integral, and then the average  of these values. We obtain a vector from each resulting unit length integral, and then then the sum of these vectors should ideally converge to some stable position, which constitutes another interpretation for complex integration within the context of the [[Laplace Transform]]. 

![[Pasted image 20251221231214.png]]

We can then consider the final position of the resulting vector $v=\langle x,y \rangle$, and then plot the magnitude of this vector in the $S$ plane, giving us $\|v\|$ for some $s=a+bi$. For the pet example considered in the video of the function $e^{-st}$, we have that  We will notice along the complex plane that there is a massive for $s=0$ since the integral completely diverges here:
$$\int_{0}^{\infty}e^{-0\cdot t}dt=\int_{0}^\infty dt \implies  \therefore  \text{integral diverges}$$We also have a direction described implicitly by $v$, so it follows that we can describe the angle using color.
![[Pasted image 20251221232059.png]]

It turns out also that if there is no real component for $s$, then the 

### Resolving Domain Issues 
If we consider the portion of the domain where $Re(s) < 0$ it follows that the Laplace transform without [[Analytic Continuation]] will necessarily diverge for all $Re(s)<0$. We will be able to resolve this using this technique. 

Notice that the integral $$\int_{0}^\infty e^{-st}dt=\frac{1}{s}$$
We want to be able to extend this to all all of the values in $S$, except for the pole of course at $s=0$. Consider when $Re(s)<0$ using this formula, it follows that we would have a negative area. This interpretation is flawed since our area would be negative. However, through [[Analytic Continuation]] we are able to extend the domain to all of $S$, except for the poles, in a meaningful manner. 

#### Analytic Continuation 
[[Analytic Continuation]] over the reals has infinitely many choices, even if the function is smooth. But over the complex numbers, there is a considerably more constrained definition. Even if we want to ensure that our function's analytic continuation is $C^1$ over some constrained domain we have a single choice. There is either one extension, or no such extension. 

If such a function exists, it is known as the [[Analytic Continuation]] of a function, which can reveal additional information about the function. For the [[Laplace Transform]], the [[Analytic Continuation]] of the function is given by:
$$\text{Analytic Continuation of }F(s)=\frac{1}{s}$$
Where we have a [[pole]] at $s=0$, which is a very pure example of what a pole is. 

All of this is true for the function:
$$\int_{0}^\infty1\cdot e^{-st}dt=\frac{1}{s}$$
Where $f(t)=1$, the simplest of functions. We can extend this to other exponential functions for $f(t)=e^{at}$ as well. When we consider the resulting position of the pole, it turns out it is located at $s=a$ along the $S$ plane:
$$\int_{0}^\infty e^{at}\cdot e^{-st}dt=\int_{0}^\infty e^{-(s-a)t}$$
The integral is essentially the same, and the pole still occurs when $s-a=0$ except here when $a=s$ then we get a pole. This lines up with the case where $a=0$ and therefore $f(t)=1$, and shows this is really just a generalization of that function. The resulting integral for this function is:
$$\int_{0}^\infty e^{-(s-a)t}=\frac{1}{s-a}$$
When there is a pole, we are able to find the given coefficient for our exponential function. When we find the poles of our function, we know the coefficients $a$, that allow our function to be expressed as a sum of exponentials. 

---
# Examples 

$$\large{\mathcal{L}}\{\cos(t)\}=\int_{0}^\infty \cos(t)e^{-st}dt=\int_{0}^\infty \left( \frac{1}{2}e^{it}+\frac{1}{2}e^{-it} \right)e^{-st}dt$$
$$=\int_{0}^\infty  \frac{1}{2}e^{it} e^{-st}dt+\int_{0}^\infty  \frac{1}{2}e^{-it} e^{-st}dt=\frac{1}{2}\left(\frac{1}{s+i}+\frac{1}{s-i}\right) \implies \text{ Function has a pole at: }s=i,s=-1$$

Visually, the same idea occurs when we consider the graphical intuition of the function. More generally, we should consider some $\cos(\omega t)$ instead of just $\cos(t)$ and we obtain the following result:
$$\large{\mathcal{L}}\{\cos(\omega t)\}=\int_{0}^\infty \cos(\omega t)e^{-st}dt=\frac{1}{2}e^{-it} e^{-st}dt=\frac{1}{2}\left(\frac{1}{s+\omega i}+\frac{1}{s-\omega i}\right)$$
$$=\frac{s}{s^2+\omega^2}$$
We can also obtain this result not using the [[Euler's Identity]] expression of $\cos(t)$, we can instead use the function given by [[Integration by Parts]]. We would obtain the same expression above of $\frac{s}{s^2+\omega^2}$, and then we would need to perform [[Partial Fraction Decomposition]] of the expression, to then obtain the poles as expressed above. 

Once we have the poles, we know the exponential components that we can use to express $\cos(\omega t)$ as the sum of these different exponents with the value of $s=\pm \omega i$ 
# Properties of the [[Laplace Transform]]
The [[Laplace Transform]] is a linear operator, which satisfies the following conditions for functions $f(t)$, and $g(t)$:
$$\large{\mathcal{L}}\{f(t)+g(t) \}=\large{\mathcal{L}}\{f(t)\}+\large{\mathcal{L}}\{f(t)\}$$
$$\large{\mathcal{L}}\{\delta f(t) \}=\delta\large{\mathcal{L}}\{f(t)\}:\delta \in \mathbb{C}$$
---
# Limitations
Not all functions can be neatly expressed as the sum of a finite sum of exponential functions, and require the use of infinitely many functions. 

---
# Old Laplace Transform Notes from my ODE Class of Fall 2024 (Reformat TODO)

\section{The Laplace Transform}
The Laplace transform is a transformation which converts  differential equations to algebraic equations. For differential equations which are difficult to solve, using the Laplace transform makes finding solutions for such equations very simple. The Laplace transform is an operator much like the differential operator and the integral - all of these functions take one function to the value of another function. 

The Laplace transform takes a function defined in terms of t, and converts it to a new function defined in terms of F, and is typically denoted as the following:
$$\mathcal{L}(t) = F(s)$$
We can define the Laplace transform to be:
$$ F(s) =  \int_{0}^{\infty} e^{-st}f(t) \,dt $$ 
Because we are computing the integral with respect to t defined for an upper and lower bound, the resulting end function will only be in terms of S if the integral converges. 

\hfill\break
\hfill\break
\textbf{Example}
\hfill\break
\hfill\break
$$\mathcal{L}(e^{at}), t \ge =  0$$
\[ \mathcal{L}(e^{at}), t \ge  =  \int_{0}^{\infty} e^{-st}e^{at} \,dt \] 
\[ \mathcal{L}(e^{at}), t \ge  =  \int_{0}^{\infty} e^{t(a-s)} \,dt \] 
$$\left[ \frac{e^{(a-s)t}}{a-s} \right]_0^\infty$$

The result of the laplacee transform here is  dependent upon the values of s and a chosen. If the difference between s and a is greater than zero, than plugging 0 into this term means raising a value greater than  one by infinity, meaning it will diverge to infinity. For the difference being equal or less than zero, the value converges to:
$$\mathcal{L}(e^{at}) =\frac{1}{s-a}$$

\hfill\break
\textbf{Laplace of the Heavyside Step Function}
The Heavyside step function is defined  as u(t-a) such that when  t $\ge$ a, u(t-a) = 1, and for t $\le$ a, u(t-a)=0. If we are to take the laplace of this  function notice that its area from 0 to a is 0, since only at a is does u(t-a) begin to have the value of one. From a to $\infty$ we can thus write the following expression for the Laplace transform:
$$\mathcal{L}(u(t-a)) =\int_{a}^{\infty}e^{-st}\,dt$$
$$= \left[\frac{e^{-sa}}{-s} \right]_{a}^\infty = \frac{e^{-sa}}{s}$$
\hfill\break
\hfill\break
\textbf{Laplace of $t^n$}
\hfill\break
\hfill\break

The Laplace of the Gamma function is useful for evaluating $\mathcal{L}(t^n)$, because the gamma function and laplace are quite similar looking:
$$F(s) = \mathcal{L}(t^n) = \int_{0}^{\infty} e^{-st}t^n\,dt$$
$$\Gamma(a)=\int_{0}^{\infty}e^{-t}t^{a-1}dt$$
\hfill\break
\hfill\break
By evaluating this integral using repeated integration by parts, we get the result that:
$$\mathcal{L}(t^n) = \frac{(n+1)!}{e^{s+1}}$$

\hfill\break
\hfill\break
\textbf{Linearity of the Laplace Transform}
\hfill\break
\hfill\break
The Laplace Transform is given to be a linear transformation. Theorem 5.1 asserts that the transformation satisfies the property that:
$$L(f+g) = L(f) + L(g)$$
$$L(cf) = cL(f)$$
Given this, the Laplace transform therefore satisfied the properties of a linear transformation

The properties of linearity satisfied by this function appear to come from the fact that integrals can have constants taken out of them, satisfying the second property, and the fact that integrals and their contents can be split apart into:
$$\int f(x)+g(x) = \int f(x) + \int g(x)$$
Given these principles, it seems simple for these properties to be satisfied.

This property can be practically used to split apart the Laplace of some given function, g(t) for instance take:
$$L(5-3e^{-2t}) = L(5) + L(e^{-2t})$$
$$L(5) = 5\frac{1}{s} - 3 \frac{1}{s+2} $$
Again this principle comes from the fact that when we evaluate the integral we can split it in parts via the addition property of integrals, which is analogous to splitting up the Laplace operator's contents.

\section{Existence of the Laplace Transform}
The Laplace transform does not exist for all functions. For all of the functions involved in solving constant-coefficient equations, it is known tha the Laplace transform exists.
This means that, if we are given a sinusoid, an exponential, a constant, or a polynomial, then the Laplace transform's integral will converge, and give us a valid result. This is the case for all piecewise functions which do not grow "too fast". To determine whether or not the Laplace Transform of a function exists if it satisfies two conditions, being piecewise continuity and exponential order. 
\hfill\break
\hfill\break
\textbf{Piecewise Continuity}
A function can be said to have piecewise continuity if for some finite number of points, the graph has "jump discontinuity," meaning that at these points, the left and right handed limits match their respective sides, but are not equal to one another. All of the function seen in the solutions to constant coefficient differential equations satisfy this property, e.g. sinusoids and exponential. 
\hfill\break
\hfill\break
\textbf{Exponential Order $e^{at}$}
The intuition for this concept is that, in some graph, after some value T in the graph, all values of t can be said to be bounded by two exponential functions. We can write this idea more formally as: 
$$-Me^{at} \le f(t) \le Me^{at}$$

Again the same functions such as sinusoids, exponentials to the form $e^t$, constants, and polynomials satisfy this relationship, however functions of the form, $e^{t^2}$ for instance will fail since at some point, $e{t^2}$ will usurp any of the functions of the form $Me^{at}$ which surround it since a is merely a constant.  

\hfill\break
\hfill\break
The book offers a proof of this fact:
$$F(s) = \int_{0}^{\infty}e^{-st}f(t)\,dt=\int_{0}^{T}e^{-st}f(t)\,dt + \int_{T}^{\infty}e^{-st}f(t)\,dt$$
We know that the integral running from 0 to T converges since T is finite, and that the function is piecewise convergent. On the right integral running from T to $\infty$, we can use the integral comparison test to see if it will converge or diverge.

$$ \Bigg| \int_{0}^{\infty}(e^{-st}f(t)\,dt)\ \Bigg| \le \int_{0}^{\infty}\lvert e^{-st}f(t) \,dt \rvert \le \int_{0}^{\infty}Me^{-st}e^{at}\,dt$$

We can re-write the final integral in this sequence as:
$$M\int_{0}^{\infty} e^{(-s+a)t} = \frac{e^{-t(s-a)}}{s-a}\Bigg|_{T}^{\infty} = \frac{e^{-T(s-a)}}{s-a} $$

This convergence only occurs when the value of s $\ge$ a, resulting in a convergent integral and thus satisfying the test.

\hfill\break
We finally arrive at theorem 5.2, that given a function f(t) along the interval $[0,\infty)$ which is piecewise continuous and of Exponential Order, we can claim that the Laplace transform of the function exists. 

\section{Properties of Certain Laplace Transforms}

In a Laplace transform the value $L(t^n) = \frac{n}{s}L(t^{n-1})$ which is true via the gamma function. 
For Laplace transforms involving the form $L(e^{at}f(t) = L(s-a)$

\hfill\break
\textbf(Theorem 5.4 Power Series with Laplace Transform)
\hfill\break

One of the key properties of Laplace transforms for practically computing them is being able to express a function and its derivatives in terms of itself. This is where the algebraic part of converting a differential equation to an algebraic equation comes into play. 
Consider L(f'(t)) which we can apply the laplace transform to, and then use integration by parts to solve:

$$L(f'(t)) = \int_{0}^{\infty} e^{-st}f(t)\,dt = e^{-st}f(t) \bigg|_{0}^{\infty} + s \int_{0}^{\infty} e^{-st}f(t) $$
$$sL(f(t)) - f(0)$$
Notice that this provides a relationship between the Laplace of the derivatives of f(t) and the laplace of f(t) itself. Doing this process iteratively, say applying this for f''(t), f'''(t), ... $f^{n}$(t) gets us the following result, which is essential for solving differential equations:
$$L(f^{n}) = s^nL(f) - s^{n-1}f(0) - s^{n-2}f'(0) - s^{n-2}f''(0) - ..... - f^{n-1}(0)$$

As the book says this roughly equates the process of taking the nth derivative of the function with multiplying it by s n many times.

\hfill\break
\textbf{Translation Property}
\hfil\break
The translation property shows that the Laplace transform's output value is shifted by some value when a function is shifted over by a as $s-a$. This happens when the function is multiplied by $e^{at}$. 
This works since multiplying $e^{-st} \cdot e^{at}f(t) $ changes the exponential's power, and thus we can rewrite it and factor out a negative sign, in turn shifting the laplace transform down by s-a. 
\hfill\break

\section{Inverse Laplace Transform}
The inverse Laplace transform is used to reverse the Laplace transform to express a function in terms of s in terms of t again. We often make use of partial fractions to do this

\hfill\break
\textbf{Definition of the Inverse Laplace Transform}
\hfill\break
The inverse Laplace transform is a way to convert a Laplace transformed function, that is a function given by F(S) to a variable in the t space, that is a function f(t). This works if F(s) = L(ft). 
There are some functions where the Laplace transform's inverse, $L(t)^-1$ is not unique, meaning that L(f(t)) = L(g(t)), but $L^-1{f(t)} \neq L^-1(f(t))$ for f(t) and g(t) such that f(t) $\neq$ g(t). However the functions which this actually matters for are discontinuous functions which are effectively the same but just have
different values for their points of discontinuity. Computing the Laplace transform's inverse is cumbersome and uses a contour integral over the complex numbers, and thus we stick to practically computing the value by using a table. 
\hfill\break
\textbf{Properties of Linearity}
The inverse Laplace transform satisfies properties of linearity, and is given explicitly by the Bromwich integral. I haven't taken compelx analysis yet, but I think the following principles we have with normal integrals will hold under complex analysis where we can consider $\mathcal{L}^{-1}((h(s)+g(s))$ to be the same as evaluating two instances of the bromwhich integral where f(s) is chosen to be either h(s) or g(s). The same can be said for just extracting a constant out of the integral c. Therefore we get:

$$\mathcal{L}^{-1}(f(s)+g(s)) = \mathcal{L^{-1}(f(s)}+\mathcal{L^{-1}(g(s)}$$
$$\mathcal{L^{-1}(c \cdot f(s)} = c \cdot \mathcal{L^{-1}(f(s)}$$

The inverse Laplace transform is given by the following integral and makes seeing these properties easier:
$$F(S) = \frac{1}{2 \pi i} \int_{\gamma-i\infty}^{\gamma+i\infty}e^{st}f(s)\,ds$$

\hfill\break

\section{Solving Differential Equations with Laplace Transforms}
In order to solve differential equations, we convert a differential equation to s, and solve for the differential equation in the s space, and then convert it back to the t space using the inverse Laplace transform. 

\section{Linear Systems of Differential Equations}
We are given a system of differential equations, where we know some functions, but have n functions that we want to solve for. We have several methods of solving these systems, one of them is by substitution. 


