---
title: Pytorch
---
[[Broadcasting]] in python refers to operations performed on vectors or matrices themselves instead of just individual elements.

When we try to do matrix operations in Pytorch, these operations are already determined and handled by the library. When we are broadcasting, we are broadcasting across the entire array. For instance if we just scale up a vector. 

If we do matrix vector products, these operations also take place. We can use the operations size and shape in order to get the sizes of our matrices. They need to conform, since our data is always confined to a matrix.

We can also do this one line when we obtain the mean of each row and [[Standard Deviation]] of each entry, and we can compute a normalization of a matrix column-wise with 1 line. We prefer to use inbuilt arrays with numpy and pytorch than in vanilla python. 

It's also important to do checking also especially n a notebook and verify that not such errors are occurring. We can also use assert statements to check things at each stage.

##### Python vs Numpy Arrays
We always prefer dealing with fixed-size length arrays in C instead of using python lists which are very complicated objects compared to C arrays. 

### Creating Arrays 
Numpy has a lot of built in functions for adding elements to vectors and arrays by filling them with elements. In a numpy array, every element is the same type. Everything is the same type, maybe an integer or float, which is known as the dtype. 

We also have the linspace argument which increments through our array by some amount. 

We can also create random valued arrays with integer entries or entries between 1-0. In python, we have a copy function, which might give us problems if we run into pointers, we should always stick to the inbuilt copy function to avoid simply getting the pointer to an array. 

### Boolean Indexing 
We can get subsets of our data by using things like a[v>5] or something similar. 

---
# Axis
What axis are we doing things on? In torch, the axis is zero by default. In numpy, it considers the sum across all values if we do the sum with no axis mentioned. 

If we specify an axis, like $0$ we get over rows, if we do over $1$ then we get a sum over columns. When we specify an axis, it outputs a vector corresponding to each column. 

---
# Numpy Matrix Operations
We operations that are non-element wise. The @ is the matrix multiplication sign. We also have the matmul function which is actually matrix multiplication, is preferred, and much clearer to work with. 

---
# Broadcasting
If we have some incomplete notation 