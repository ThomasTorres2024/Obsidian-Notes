```Matlab
size(A)
```

We can generate random matrices as well:
```MATLAB
x=rand(1,4);
y=rand(4,1);
```
To do a transpose we use:
```
x', y' etc
```

We have a normal product and also an element wise product:
```Matlab
x'*y
x.*y (element wise)
```

Solve linear systems:
```MATLAB
x=A\b
```
We can extract rows and columns from using the following:

To take column 2:
```MATLAB
B(:,2)
```
To take row 2:
```MATLAB
B(2:,)
```

To extract a region of a matrix:
```MATLAB
B(1:2,1:2)
```

Some commands might not work due to sparsity. If our matrix is decently sized we can fill it and it'll work. 