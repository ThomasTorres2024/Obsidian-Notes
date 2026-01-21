---
title: Vector Space
tags:
draft: "False"
---
# Vector Space 
A [[Vector Space]] can be described by a [[Field]], $\mathbb{F}$, and a set which vectors are drawn from, $V$ that satisfies the following properties for $u,v,w \in \mathbb{V}$, and for the scalars $\delta,\gamma \in \mathbb{F}$:

1. Associativity of Vector Addition: $$u+(v+w)=(u+v)+w$$
2. Commutativity of Vector Addition: $$u+v=v+u$$
3. [[Identity Element]] of Vector Addition: $$\exists 0\in V, \text{ such that}, v+0=v, \forall v \in V$$
4. [[Inverse Element]]s of Vector Addition $$\text{For every } v\in V, \exists -v \in V:-v+v=0$$
5. Scalars from $\mathbb{F}$ are associative: $$\gamma (\delta v)=(\gamma \delta)v$$
6. Identity Element of Scalar Multiplication: $$1v=v, 1 \text{ is the }$$ [[Multiplicative Identity]] in $\mathbb{F}$
7. Distributivity of Scalar Multiplication: $$\delta(u+v)=\delta u +\delta v$$
8. Distributivity of Scalar Multiplication with respect to field addition: $$(\delta + \gamma)v=\delta v+\gamma v$$
Given that these properties are satisfied we can denote a [[Vector Space]] by the set with a field, a set of vectors, an addition and scaling operation:
$$\mathcal{V}=\{ V,\mathbb{F},+,* \}$$
Vector addition in the [[Vector Space]] forms an [[Abelian Group]]. We can verify that a [[Vector Space]] is actually a [[Vector Space]] if it abides by the above criteria. We can sidestep this condition if we have some subset of the current [[Vector Space]] that satisfies closure of addition of vectors, closure of scalars, and lastly the zero element resulting in the zero vector. This is the test for the [[Vector Subspaces]], given that $\mathcal{V} \neq \emptyset$.  

A vector space typically has a finite dimension, meaning that the [[basis]] of a vector space has a finite cardinality. 

We denote a [[Vector Space]] with an associated [[norm]] as a "Normed Vector Space", $(\mathcal{V},\| \cdot \|)$. 