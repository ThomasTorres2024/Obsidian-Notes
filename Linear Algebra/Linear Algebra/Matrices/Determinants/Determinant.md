---
title: Determinant
draft: "false"
tags:
---
# Determinant Definition
# Hadamard's Inequality 
Hadamard's inequality relates the determinant of a Matrix using the [[norm]] of the column vectors of some $A$. Let $A \in \mathbb{C}^{m \times m}$, then it follows that:
$$\det(A) \leq \prod_{i=1}^m\|\vec{a_{j}} \|: \vec{a_{j}} \text{ is a column vector of } A$$
Geometrically, we can think of this as a bound to the area that the vectors in the columns of $A$ span. If $A$ is [[linearly dependent]] it is obvious that $\det(A)=0$, and equality may be achieved on the right hand side as well in this case if $A=0$. However, if the columns of $A$ are mutually [[orthogonal]] it follows that the inequality above is actually equality if and only if this condition is satisfied. 

### Proof 1.) Using [[QR Factorization]]:
If $A$ is rank deficient then the identity is trivially true due to the positive definiteness of norms:
$$|\det(A)|=0\leq \prod_{j=1}^m\|a_{j}\|_{2}$$

Now consider when $A$ is full rank $\implies A=QR$. 
$$|\det(A)|=|\det(QR)|=|\det(R)|=\left| \prod_{i=1}^m|r_{ii}|\right|$$
Notice that:
$$a_{j}=\sum_{i=1}^jr_{i}q_{j}$$
Since $q_{j}\perp q_{i}$ for $i \neq j\implies$ we can use the Pythagorean theorem to express the following:
$$\|a_{j}\|^2=\sum_{i=1}^j\|r_{ij}\cdot\vec{q}_{i}\|^2=\sum_{i=1}^j(r_{ij})^2 \implies r_{jj}^2 \leq \|a_{j}\|_{2}^2 \iff r_{jj} \leq \|a_{j}\|_{2}$$
$$\implies \prod_{i=1}^m r_{ii} \leq \prod_{i=1}^m\|a_{j}\|_{2} \iff \det(A) \leq\prod_{i=1}^m\|a_{j}\|_{2}  $$
$$\textcolor[RGB]{153, 115, 235}{\boxed{\therefore |\det(A)|\leq \prod_{j=1}^m\|a_{j}\|_{2}}}$$
