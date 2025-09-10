A database for sparse matrices with thousands of matrices, very useful for testing. Gives highlights of non-zero entries in the matrix:

```Matlab
address='url';
websave('file-name.mat',address);
load('file-name.mat');
```

Mat lab optimizes storage and operations with sparse matrices significantly. The sparse format is very important. As soon as we multiply some $A$ that is sparse by a non-zero vector, we get a full vector. 

This is also very important for matrix algorithm testing.