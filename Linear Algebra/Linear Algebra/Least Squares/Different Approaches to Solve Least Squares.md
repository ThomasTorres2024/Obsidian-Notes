---

---
Solutions to least squares must account for the efficiency of the algorithm being used and its numerical stability. We have to distinct cases  given $A\in\mathbb{R}^{m \times n}$, where $m \geq n$ for the system of equations given by $Ax=b$:

#### Case 1. $A$ is Full Rank 
###### Method 1.) [[normal equation]]s
This is the classical method to solve least squares and is used when $A$ has full rank. We make use of the [[Cholesky Factorization]] of $A^H A$ since this matrix is [[Positive Definite Matrix]]. Our system then reduces to solve the system of equations given by:
$$A^HA=R^HR \implies R^HRx=A^Hb$$
From here we compute $w=Rx$, and then solve $R^H w=A^H b$, and then back substitute $w$ back into $w=Rx$, and then solve the system for $x$:
![[Pasted image 20251013155036.png]]
This algorithm costs an overall $mn^2+\frac{1}{3}n^3$ flops. 

###### Method 2.) [[QR Factorization]]:
We can use [[Householder Transformation]]s or [[The Gram-Schmidt Process]] to convert $A$ into $A=QR$. Solving This problem then becomes a matter of solving the system $Rx=Q^Tb$, which is easy since $R$ is assumed invertible here because it is rank $n$ and $n \times n$. 

More thoroughly, we need to express that $A=\hat{Q}\hat{R}$, and we must project $y$ onto the  [[Orthogonal Projector]] formed by $P=\hat{Q}\hat{Q}^H$ in order to get a solveable system. From this we obtain:
$$\hat{Q}\hat{R}x=\hat{Q}\hat{Q}^Hb$$
$$\hat{R}x=\hat{Q}^Hb$$
Now all we need to do is solve the upper triangular system since $\hat{R}$ is full rank and thereby [[non singular]]. So:
$$x=\hat{R}^{-1}\hat{Q}^Hb$$
Or we can just solve it via back sub. 
![[Pasted image 20251013155712.png]]

We can also derive this expression from the normal equations listed above. The work for this algorithm costs approximately:
$$2mn^2 -\frac{2}{3}n^3 \text{ flops }$$
###### Method 3.) SVD 
Given the [[Reduced SVD]] of $A$ we can say $A=\hat{U} \hat{\Sigma} V^H$. We can express the projection into the range of $A$ by $P=\hat{U}\hat{U}^H$, and thus $y=Pb=\hat{U}\hat{U}^H b$. So our system of normal equations becomes:
$$\hat{U} \Sigma V^Hx=\hat{U}\hat{U}^Hb$$
$$\Sigma V^Hx=\hat{U}^H b$$
If we let $V^Hx=w$, then $\Sigma w = \hat{U}^Hb$, we can solve for $w$ using a diagonal system of equations. We can then back sub into $w$ to find $x$. Note that this is also equivalent to just multiply the entire expression by:
$$x=A^\dagger b=V \Sigma^{-1}U^H b$$
This operation is generally more costly than [[QR Factorization]] or [[normal equation]]s, especially when $m$ is approximately $n$, but tends to even out when $m \approx n$. The highest part of the computational cost is finding [[Reduced SVD]] here. In general we take around this many [[flops]]:
$$2mn^2+11n^3 \text{ flops }$$

![[Pasted image 20251013160439.png]]
#### Case 2. $A$ is Nearly Dependent
If $A$ is nearly [[linearly dependent]], it means that one of its singular values is almost zero, but not quite, it is some super low floating point number that could cause difficulties. Using other methods might be nice, but using [[Reduced SVD]] here is the most beneficial. We make use of a truncated version of [[Reduced SVD]], and set some threshold on the $\sigma$s from $\Sigma^{\dagger}$ that we are allowed to use in our approximation. Let this number be called, $r$, then our approximation is given by the [[Pseudo-Inverse Matrix]] of $A$ expressed using the [[Reduced SVD]] of it: 
$$A^\dagger=V\Sigma^{\dagger}U^H=\sum_{i=1}^r \sigma_{i} v_{i}u_{i}^H \text{ where } r = \text{ rank of A }$$
Now given $Ax=b$, we could use $A^\dagger$ to solve it by:
$$x=A^\dagger b$$
Using this method is numerically stable but inefficient. It is  useful when $A$ is [[linearly dependent]].  

#### Case 3. A is dependent 
If $A$ is a matrix that is [[linearly dependent]], we make use of a truncated version of [[Reduced SVD]], and the [[Pseudo-Inverse Matrix]] of $A$. In the case where $A$ is not full rank, its [[Pseudo-Inverse Matrix]] is expressed in the following way:
$$A^\dagger=V\Sigma^{\dagger}U^H=\sum_{i=1}^r \sigma_{i} v_{i}u_{i}^H \text{ where } r = \text{ rank of A }$$
Now given $Ax=b$, we could use $A^\dagger$ to solve it by:
$$x=A^\dagger b$$
Using this method is numerically stable but inefficient. It is  useful when $A$ is [[linearly dependent]].  

---
# Comparison of Algorithms

If we are trying to maximize speed, we should use the [[normal equation]]s, but getting any decent result out of this is unlikely especially if the system is big because it is [[numerically unstable]]. If we want precision, especially on a low rank, or a nearly low rank case, then we go with SVD for stability. If we want a medium ground where we have full rank and a system that is confidently full rank and still a good quality answer, we would make use of the [[QR Factorization]] algorithms, preferably using [[House Holder Reflectors]] and NOT [[The Gram-Schmidt Process]] or the [[Modified Gram-Schmidt Process]]. 