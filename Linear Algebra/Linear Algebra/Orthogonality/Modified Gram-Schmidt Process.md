---
title: Modified Gram-Schmidt Process
---
# Modified Gram-Schmidt Process
The modified [[The Gram-Schmidt Process]], is a process which takes of a set $n$ linearly independent vectors and finds and a basis which spans the same set such that the new basis is orthogonal. [[The Gram-Schmidt Process]] is [[numerically unstable]], so we have to make some changes to it in order for it to not break early on. 

[[The Gram-Schmidt Process]] uses rank 1 projectors at each iteration to force orthogonality, but the [[Modified Gram-Schmidt Process]] take $j-1$ projections of rank $m-1$. Note that $P_{\perp q}$ is the projector onto the null space of $q$.  

We can form the $j$th projector by taking of the first $j-1$ projectors and taking their product. Instead of continually projecting onto rank 1 subspaces, we compute the next $v_{j}$ by taking a product with new projector matrices.

Our algorithm for the [[Modified Gram-Schmidt Process]] looks like this:
