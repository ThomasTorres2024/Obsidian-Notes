---
title: Spherical Coordinates
tags: 
draft: "false"
---
# Introduction to Spherical Coordinates
We can represent a cartesian position, $(x,y,z)$ as two angles and a radial measurement given by $(\theta,\phi,\rho)$. $\rho$ is the distance from the origin. $\theta$ describes the angle between $x$ and $y$ as it does it [[polar coordinates]].  $\phi$ describes the angle between the $z$ axis and the plane where $y$ goes through $\theta$. 

We can think of $\phi$ as the latitude, and we can think of our $\theta$ as the longitude. 

Our $\phi$ and $\rho$ really are just polar coordinates again in the $r-z$ plane. 
![[Pasted image 20250630205329.png]]
If we can express the formulas as two polar coordinates, then we don't need to worry about formulas here, but we have some formulas we could use to express out coordinates here:
$$x=r\cdot \text{cos}(\theta)=\rho \cdot \text{sin}(\phi) \text{cos}(\theta)  $$
$$y=r\cdot \text{sin}(\theta)=\rho \cdot \text{sin}(\phi) \text{sin}(\theta)  $$
$$z=\phi\text{ cos}(\phi)$$
And our $\rho$ is analogous to $r$:
$$\rho = \sqrt{x^2+y^2+z^2}$$
---
# Examples Of Spherical Graphs

The graph $\rho =a$ is a sphere of radius $a$ centered at 0. 

The graph $\phi = \dfrac{\pi}{4}$ is a cone which is declined at $\dfrac{\pi}{4}$. 
If $\phi = \dfrac{\pi}{2}$ we get the entire $xy$ plane. 

---
# Volume Element
In order to perform [[Triple Integrals]] involving spherical coordinates, we must first perform a [[Change of Variables]]. We need to determine the volume element, $dV$ of our function. 

We can begin with an approximation formula:
$$\Delta V = \Delta \rho \cdot \Delta \theta \cdot \Delta \phi$$
To get a better approximation let us consider a slice of our region:
![[Pasted image 20250630220551.png]]
Our rectangular region is the result of the product of two parts. One is the standard result from converting polar to spherical, and the top part basically just askes us to find the radii to our circle section, which turns out to be $r \text{ sin}(\theta) d\theta$. To take this to a volume, we need to tack on $d\rho$. This gives us everything we need.

We can just take the product of both regions, and we obtain:
$$dV=\text{ sin}(\theta)r^2d\theta \cdot d\rho \cdot d\phi$$
---
#### Example - Integrating Using Spherical Coordinates

Let us consider the region bound a plane and sphere given respectively by:
$$z=\dfrac{\sqrt{2}}{2}$$
$$z^2+x^2+y^2=1$$

![[Pasted image 20250630221955.png]]
Our integral will take the form of any volume integral using triple integrals, namely:
$$\int \int \int_{V}1 \cdot dV$$
Using the formula $z=\rho \cdot \text{cos}(\theta)$, we can express our $\rho$ as:
$$\rho = \dfrac{1}{\sqrt{2}\text{cos}(\theta)}$$
We can see that our $\rho$ is bound between $1$ and $\dfrac{\sqrt{2}}{2}$ by our graphic above. So we get our first set of bounds:
$$\int \int \int_{\frac{\sqrt{2}}{2}}^{1}dV$$
If we sketch out and do a cross section of our graph, we would be able to determine with trigonometry that our lowest bound of $\phi = \frac{\pi}{4}$ , and that our greatest $\phi=0$. Lastly, we can see that we go all around the $z$ axis, so we know our $\theta$ is bound around $2\theta$ and $0$. 
![[Pasted image 20250630225600.png]]
Our resulting integral is:
$$\text{volume}=\int_{0}^{2\pi} \int_{0}^{\frac{\pi}{4}} \int_{\frac{\sqrt{2}}{2}}^{1}d\rho \cdot d\phi \cdot d \theta$$
---
# Applications
We can use spherical coordinates to calculate gravitational attraction and spherical coordinates. 