---
title: Fourier Transform
tags:
  - Functional_Analysis
draft: "False"
---
# Fourier Transform Properties 

$Theorem$. Let $f \in L^1(\mathbb{R})$ and $f(x) \leftrightarrow F(\omega)$, then: 

1. (Time Shifting) $f(x-x_{0}) \leftrightarrow e^{-i\omega x_{0}}F(\omega)$

2. (Frequency Shifting) $e^{i\omega_{0}x} f(x) \leftrightarrow F(\omega-\omega_{0})$

3. (Scaling) $f(ax) \leftrightarrow \frac{1}{|a|} \cdot F\left( \frac{\omega}{a} \right): a \neq 0.$ Particularly, $f(-x) \leftrightarrow F(-\omega)$

4. (Time Differentiation) If $f \in C^1(\mathbb{R}) \cap C_{0}$ and $f' \in L^1(\mathbb{R})$ then $f'(x)\leftrightarrow i \omega \cdot F(\omega)$

5. (Frequency Differentiation) If $xf\in L^1(\mathbb{R})$, then $F\in C^1(\mathbb{R})$ and $x\cdot f(x) \leftrightarrow i \cdot F'(\omega)$. Equivalently $-ix \cdot f(x) \leftrightarrow F'(\omega)$

---
# Fourier Transform Properties Remarks 
1. shifting of $f$ by $x_{0}$ to the right $(f(x-x_{0}))$ corresponds to a rotation of the Fourier transform by $-\omega x_{0}$ in the complex plane. 

2. The rotation of $f$ by $\omega_{0}x$ in the complex plane corresponds to a shifting of the Fourier transform by $\omega_{0}$ to the right $F(\omega-\omega_{0})$

For $1.\quad 2.$ we observe that a shift reflects a rotation of $\hat{f}$ in the complex plane and vice versa. 

3. When $a>1$, the horizontal shrink of $f(x)$ by a factor of $a$ in $f(ax)$ corresponds to the horizontal stretch and vertical shrink by a factor of $a$ in $\left( \frac{1}{|a|} F\left( \frac{\omega}{a} \right) \right)$

This corresponds to the idea that a signal that is dispersed in the time domain is compressed and squished in the frequency and vice versa. Where one is elongated, the other is stretched. 

Another thing to note, if $f$ is even so is $\widehat{f}$, the same goes for if $f$ is odd as well. 

---
# [[Convolution]] Theorem 
Let $f,g \in L^1(\mathbb{R})$, then $(f*g)(x) \leftrightarrow \widehat{f}(\omega) \cdot \widehat{g}(\omega)$

---
# Duality 
If $f(x) \leftrightarrow F(\omega)$ then $F(x) \leftrightarrow 2\pi \cdot f(-\omega)$. This is due to the fact that: 

$$\check{f}(x)=\frac{1}{2\pi}\widehat{f}(-x)\implies \widehat{\widehat{f}}(x)=2\pi f(-x)$$