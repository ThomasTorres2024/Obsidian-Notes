---
title: House Holder Reflectors
tags:
draft: "False"
---
# [[House Holder Reflectors]] Overview 
The idea of a House Holder reflector comes from trying to find a matrix such that we can reflect some vector $y$ over a hyperplane $H$. The [[House Holder Reflectors]] are tailored to be the matrices that are used in the  [[Householder Transformation]]. 

For some given vector, $x$ the [[House Holder Reflectors]] are [[Unitary Matrices]] defined by:
$$v=\|x\|e_1-x$$
$$F=I_n-2\frac{vv^H}{v^Hv}$$
The matrix $F$ is [[Hermitian]] and it is Unitary, so $F$ is [[unitarily diagonalizable]]. Since $F$ is unitary, the eigen values of $F$ have a complex modulus of $1$. Intuitively, we can see that one of the eigen values is one, if our vector is on the hyperplane. If we are orthogonal to the hyperplane, we will have an eigenvalue of -1.