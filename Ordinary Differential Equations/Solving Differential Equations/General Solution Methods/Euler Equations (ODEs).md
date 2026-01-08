---
title: Euler Equations
tags:
draft: "False"
---
# Euler Equations Overview
We can solve [[Second Order Homogeneous Differential Equations]] by using [[Euler Equations (ODEs)]], which are equations of the form (we can generalize it to the $n$th degree)
$$\sum_{i=0}^n c_{i}y^{(n)}:c_{i}\in \mathbb{C}$$
A solution to an equation of this form are the functions, are the roots of the above polynomial formed using the $c_i$s:
$$P(x)=\sum_{i=1}^nc_ix^i$$
Where each root $r$ can be used to express a solution to the differential equation in the form:
$$y(x)=e^{rx}$$
If all of our $r$ roots of the polynomial $P(x)$ are unique $\implies$ that our solution set just consists of equations of this form. If we have repeated roots, for every repeated root of $r$ then the following can be verified to be solutions to the homogeneous equation via the [[Wronskian]]:
$$y(x) \text{ can be of the form: }xe^{rx},x^2e^{rx},\cdots x^{n-1}e^{rx}$$
We can easily verify solutions are of the form $e^{rx}$ to begin with. If we set $y=e^{rx}$, then we can divide all sides of the equation by this quantity, and obtain the polynomial $P(x)$, so clearly the solutions begin with the roots. We obtain the rest from just adding on an $x$, which we can see are all linearly independent via the [[Wronskian]]. 

We can prove the result via induction. Let the power of $x$ be 0 and $1$ to start:
$$\mathcal{W}(e^{rx},xe^{rx})=\begin{bmatrix} e^{rx} &  xe^{rx}\\
r e^{rx} & e^{rx}(rx+1)
\end{bmatrix}$$
$$\det(\mathcal{W})=e^{2rx}(rx+1)-xre^{2rx}=e^{2rx} \neq 0 ,\forall x,r \in \mathbb{R}$$
Now if we assume this is the case for $n-1$ and we want to show it is true for $n$:
$$\mathcal{W}(x^{n-1}e^{rx},x^ne^{rx})=\begin{bmatrix} x^{n-1}e^{rx} &  x^ne^{rx}\\
 x^{n-2}e^{rx}((n-1)+rx^2) & (x^{n-1})e^{rx}(rx+n)
\end{bmatrix}$$
$$\det(\mathcal{W})=x^{2n-2}e^{2rx}(rx+n)-x^{2n-2}e^{2rx}((n-1)+rx^2)=0$$
$$\iff (rx+n)(n-1+rx^2)=0$$
It is not the case $\forall r,x$ that $\det(\mathcal{W})=0, \therefore$ the functions $x^{n-1}e^{rx},x^{n}e^{rx}$ are [[Linearly Independent Functions]].  

---
# Solving [[Second Order Homogeneous Differential Equations]] using [[Euler Equations (ODEs)]]:

The solution to the differential equation, $ay'' + by' +cy = 0$ can be solved by substituting $y=e^rx$, where $a,b,$ and $c$ are constants, and $a \neq 0$  

$$y = e^rx$$
$$y = r\cdot e^rx$$
$$y = r^2\cdot e^rx$$

Substituting these values into the equation

$$a[r^2e^rx] + b[r\cdot e^x] + c[e^rx]$$

$e^x$ can be factored, out and then divided out 
$$e^rx(ar^2 + ar +c) = 0$$
$$ar^2 + ar +c = 0$$

The equation beneath is known as the characteristic equation. The result is a simple quadratic form which can be easily solved for using the quadratic formula equal to $r$. 

### Cases Based Around the Discriminant: 
Recall the equation for the discriminant in the quadratic formula:
$$b^2-4ac > 0$$

### Case 1.) $r_1 \neq r_2$ Distinct Roots
Given this case, then there are two real distinct solutions for r, therefore the equation of the 2nd order can be written as:
$$y_{1}(x) = e^r_{1}x$$
$$y_{2}(x) = e^r_{2}x$$

Verifying that the two equations are linearly independent using the [[Wronskian]]:
$$ w(y_{1}(x),y_{2}(x)= 
\begin{bmatrix}
    e^r_{1}x & e^r_{2}x\\
    r_{1}e^r_{1}x' & r_{2}e^r_{2}x\\
    \end{bmatrix}
$$

Computing the Wronskian results in an expression which is linearly independent. We can use theorem four to write this expression out:

$$y=c_{1}e^{r_1x} + c_{2}e^{r_2x}$$
This is true only for the case where $r_1 \neq r_2$. 
### Case 2, $m_{1}$ = $m_{2}$ repeated root 

Occurs when $b^2-4ac = 0$, and results in $m = \frac{-b}{2a}$. This gives the result, $y_{1} = e^{mx}$. We need to use the method of [[Reduction of Order]] in order to find the second solution. 

$$y_{1}=e^{mx}$$
$$y_{2}=e^{mx}\cdot v(x)$$
$$y_{2}'=e^{mx}(mv(x)+v'(X))$$
$$y_{2}''=e^{mx}(mv(x)+v'(x))$$

Substituting these values back into the original equation:

$$ae^{mx}[v''+2mv'+m^2v] + be^{mx}[v'+mv] + cve^{mx}=0$$
$$a[v''+2mv'+m^2v] + b[v'+mv] + c=0$$
$$av''+v'(2am+b) + m(am^2+bm+c)v =0$$

We know that $m(am^2+bm+c)$ is equal to the root, which is also equal to zero. $(2am+b)$ is equivalent to the root, which is also zero.
$$av''=0$$
$$av'=c_{1}$$
$$av=c_{1}x+c{2}$$

To make this simpler, we discard the $c_{1}$ and $c_{2}$, and get that:
$$y_{2}=xe^mx$$

If we have repeated real roots, then the solution to this equation is given by:
$$y_{1}=c_{1}e^{mx}+xc_{2}e^mx$$

### Case 3.) Homogeneous Equations with Constant Coefficients, Complex Solutions

The expression, $ay'' + by' + cy=0$ can be reduced to $am^2 + bm +c$, by allowing $y(t) = e^t$, and then reducing the expression. If the roots to the quadratic equation are complex, than the solution set to the equation. This is given if and only if the discriminant, $b^2-4ac <0$. 

We obtain the following
$$y=c_{1}e^{p+iq} + c_{2}e^{p-iq} $$

Using [[Euler's Identity]] we can write the expression as:
$$y=c_{1}e^{px}(\cos(qx)+i\sin(qx) + e^{px}(\cos(qx)-i\sin(qx)$$
$$y=c_{1}e^{px}(c_{1}+c_{2}\cos(qx)+(c_{1}i - c_{2}i)e^{px}\sin(qx))$$

We can rewrite this by choosing $c_{1} = c_{2} = \frac{1}{2}$, which in turn causes the complex part to vanish since the difference of $c_{1}$ and $c_{2}$ is taken:
$$y=c_{1}e^{px}(c_{1}+c_{2}cos(qx)+(c_{1}i$$

We can also rewrite this relationship using $c_{1}=c_{2}=\frac{i}{2}$, which results in another real solution:
$$e^{px}\sin(qx)$$

We can assert that these two solutions are linearly independent by taking the wronskian of the two functions thus resulting in $e^{2px}q \neq 0$. Using the two solutions of the equation, we get the result that the general solution for a constant equation is: 