---
title: Locality
draft: "False"
tags:
  - Computer_Organization
---
# [[Cache]] Locality 

Locality is the principle that during the course of a [[Program]] that data items that are near other recently referenced data items (spatial locality) or that were recently referenced (temporal locality). A program that has good spacial locality has that a value which is referenced once will have nearby values accessed soon. A program with good temporal locality will re-read these values soon again. 

### Strides
The stride in a program refers to refers to how many elements are skipped when reading data. When we have a stride-1 program we essentially access each value in some Iterable container. When we have a stride $k$ iteration, we access $0,k,2k,...$ and so on. 

Strides are also important in the context of multidimensional [[Array]]s. If we consider the following program:

```C

int summarrayrows(int a[M][N]){
	
	int i,j,sum = 0;
	
	for(i =0; i < M; i++){
		for (j=0; j < N;j++){
			sum+=a[i][j];
		}
	}
	
	return sum; 

}

```

The array is stored in row major order, and its access is also done in row major order. So we have good locality again. Now consider the next program: 

```C

int summarrayrows(int a[M][N]){
	
	int i,j,sum = 0;
	
	for(j =0; j < N; j++){
		for (i=0; i < M;i++){
			sum+=a[i][j];
		}
	}
	
	return sum; 

}
```

Here we have poor spatial locality. We can read in memory with a stride-$N$ reference pattern, so we are reading in a lot of memory that we won't access as quickly as in the row major manner. 

The row wise program works better since we scan memory row wise, and the second function (on the bottom) struggles with column wise iteration since data is stored row-wise. 

---

# Summary 

- Programs that reference the same variables tend to have a higher temporal locality

- Programs with stride-$k$ reference patterns, the smaller the stride, the smaller the stride the better the spatial locality. Programs with stride-1 reference patterns have good spatial locality (higher chance of reading in nearby data), whereas programs that tend to hop on around memory with large strides have poor spatial locality 

- Loops have good temporal and spatial locality. The smaller the loop body and the greater the number of loop iterations, the better the locality

