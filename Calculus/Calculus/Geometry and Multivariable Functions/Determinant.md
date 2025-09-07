---
title: Determinant
---
In the two by two case, for a 2x2 matrix we have that its determinant is:
$$\text{det}\left(\begin{bmatrix} a & b\\ c& d \end{bmatrix} \right)=ad-cb$$
We also use bars around a matrix to denote the determinant around a matrix, and in the context of the MTH 437 course is not absolute value. 

We can compute higher dimensional matrices by using the cofactor expansion by computing the sum of the determinant of correctly signed minor matrices. 

We can also use any row or column to iterate over in order to compute our determinant. Any even valued iteration in our expansion will have a negative sign in front of it. 

---
# Properties of the Determinant 
The properties of the determinant appear to come from fundamental Row Operations that we can perform on matrices. They effect the determinant of the matrix in the following ways:
1. Column swaps correspond to introducing a negative sign to our determinant:
$$[\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]=-[\vec{a}_{2},\vec{a}_{1},\vec{a}_{3}]$$
2. If a column contains $c$, we can factor it out: $$[c\cdot\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]=c\cdot[\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]$$
3. Addition of columns does not change the determinant:
$$[\vec{a}_{1}+\vec{a}_{2},\vec{a}_{2},\vec{a}_{3}]=[\vec{a}_{1},\vec{a}_{2},\vec{a}_{3}]$$
