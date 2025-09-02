---
title: Change of Variables in Integration
draft: 
tags:
---
# Change of Variables : Polar Coordinates 
We change to integrating in a different system of coordinates to make integration easier. For instance, computing the following integral is fairly difficult in cartesian coordinates:

$$\int_{0}^1 \int_{} (1-x^2-y^2)dA$$
But if we convert this to polar coordinates it is a lot easier to work with. 

When converting to polar, we simplify integrals of circles, cardioids, rose curves, and generally integrands which contain $x^2 + y^2$. We can use the following important identities for conversion from cartesian to polar coordinates: 
$$x=r\text{ cos}(\theta) \text{  and  } y = r \text{ sin}(\theta)$$
$$r^2=x^2+y^2 \text{  and  } \text{tan}(\theta) = \dfrac{y}{x}$$
We can summarize these in an image:
![[Pasted image 20250626223852.png]]

When integrating over a rectangular region, we consider summing rectangular prisms given by $f(x_{i},y_{i}) \Delta A_{i}$ where $\Delta A_{i}$ is a square region. In the polar case, we are instead considering a small polar region that we will find the volume of given by:

$$\sum_{i=1}^n f(x_{1},y_{1}) \Delta A = \sum_{i=1}^n f(r_{i}\text{ cos}(\theta_{i}),r_{i}\text{ sin}(\theta_{i}))r\text{ }dr \text{ }d\theta$$

We can obtain this substitution by using the formulas for $x=r\text{ cos}(\theta) \text{  and  } y = r \text{ sin}(\theta)$ and the size of polar region which is given by: $\Delta A_{i}=r_{i} \Delta r_{i} \Delta \theta_{i}$. 

We can obtain this particular substitution by examining the small portion of a circle with angle $d\theta$ and radius $dr$, which using the formula for area of a smaller arc of a circle gives us: 
![[Pasted image 20250626234509.png]]
If our new $\Delta A$ segment is really small, it will have the value of a square, and thus its approximate area is given by $\Delta r \cdot r\Delta \theta$. The $r$ comes from the arc of the circle area.

#### Example:
Let us consider $f=1-x^2-y^2$. We can start with our polar substitution by noticing that we can express it as:
$$f=1-(x^2+y^2)=1-r^2$$