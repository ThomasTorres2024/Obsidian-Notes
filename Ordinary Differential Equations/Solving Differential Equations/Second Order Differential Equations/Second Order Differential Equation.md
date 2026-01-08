---
title: Second Order Differential Equations
tags:
draft: "false"
---
# Overview of [[Second Order Differential Equation]]
Second order Linear ODEs have a variety of solutions. The form of solution depends upon the type of second order equation given. The general form for equations of the  second order is:

$$A(x)y'' + B(x)y' +  C(x)y = F(x)$$

Which can be condensed to by dividing each term by A(x):

$$y'' + p(x)y' +  q(x)y = f(x)$$

Given that a 2nd order [[Ordinary Differential Equation]] is a [[Homogeneous Differential Equation]], meaning that it can be written as
$$y'' + p(x)y' +  q(x)y = 0$$

it can be shown that there are an infinite family of solutions given by:
$$y=y_{1}c_{1}+y_{2}c_{2}$$

It can be shown that this solution set is equivalent to the solution of the differential equation by taking its first and second derivatives, and then substituting its values into the general form of the homogeneous differential equation. 
$$y'=y_{1}'c_{1}+y_{2}'c_{2}$$
$$y''=y_{1}''c_{1}+y_{2}''c_{2}$$
Substituting these values into the general form for a homogeneous differential equation:
$$(y_{1}''c_{1}+y_{2}''c_{2}) + p(x)(y_{1}'c_{1}+y_{2}'c_{2}) +  q(x)(y_{1}c_{1}+y_{2}c_{2}) = 0$$
$$(y_{1}''c_{1} + py_{1}'c_{1}+ qy_{1}c_{1})+(y_{2}''c_{2}+py_{2}'c_{2} + qy_{2}c_{2}) = 0$$
$$c_{1}(y_{1}'' + py_{1}'+ qy_{1})+c_{2}(y_{2}''+py_{2}'+ qy_{2}) = 0$$
$$c_{1}\cdot0+c_{2}\cdot0=0$$

This shows that the solution $y=c_{1}y_{1}+c_{2}y_{2}$ is equivalent to zero and thus solves the differential equation, which is also equal to zero since it is homogeneous. 

---
# [[Existence and Uniqueness Theorem]] for [[Second Order Differential Equation]]

For the second order differential equation $y'' + p(x)y' + q(x)y = f(x)$,
$\exists$ a solution for x $\in$ interval I, and y(a) = $b_{0}$ and y'(a) = $b_{1}$.

Given these two initial conditions, we can use $y=c_{1}y_{1} + y_{2}c_{2}$ and its derivative $y'=c_{1}y'+c_{2}y_{2}'$ to solve for the values of $C_{1}$ and $c_{2}$.

The solution set to a homogeneous ODE of the second order can be provided by: 
$$y=y_{1}c_{1}+y{2}c_{2}$$

provided that both $y_{1}$ and $y_{2}$ are both [[Linearly Independent Functions]]. 

