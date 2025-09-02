---
title: Sine and Cosine Integration Formulas
tags: 
draft: "false"
---
# Wallis Product for Sine and Cosine 
We can define the Wallis product for sine and cosine in the following: 

# Product of 2 sines, 2 cosines, 1 sine and 1 cosine

We can derive the following using a system of equations and the given trig identities for cosine and sine: 

$$\text{sin}(\alpha+\beta)=\text{sin}(\alpha)\text{cos}(\beta)+\text{cos}(\alpha)\text{sin}(\beta)$$
$$\text{cos}(\alpha+\beta)=\text{cos}(\alpha)\text{cos}(\beta)-\text{sin}(\alpha)\text{sin}(\beta)$$
$$\text{sin}(\alpha-\beta)=\text{sin}(\alpha)\text{cos}(\beta)-\text{cos}(\alpha)\text{sin}(\beta)$$
$$\text{cos}(\alpha-\beta)=\text{cos}(\alpha)\text{cos}(\beta)+\text{sin}(\alpha)\text{sin}(\beta)$$
We can "derive" these formulas with Euler's identity, so memorizing these is no big deal. 

We can re-arrange the cosine and sine and get a new equivalent expression. Then using the two identities, we can sum them together and we get a difference of signs which allows us to cancel the other combined sign. In total this leaves us the sum of angle trig function. 

This gives us the following formulas:

$$\int \text{cos}(ax)\text{cos}(bx)dx=\int \dfrac{\text{cos}((a+b)x)-\text{cos}((a-b)x)}{2}dx$$
$$\int \text{sin}(ax)\text{sin}(bx)dx=\int \dfrac{\text{sin}((a+b)x)+\text{sin}((a-b)x)}{2}dx$$

