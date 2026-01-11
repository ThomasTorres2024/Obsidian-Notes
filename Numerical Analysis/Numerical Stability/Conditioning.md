---
title: Conditioning
tags:
draft: "false"
---
# Conditioning Overview
In numerical analysis we are interested in the conditioning of a problem, and the conditioning of an algorithm. If we perturb a problem or algorithm, how much can we expect the resulting problem or algorithm to change its output?

We are interested in determining if a problem or an algorithm are [[ill-conditioned]], which means that, for some small perturbation, we would expect a very different result than the actual result. 

---
# Conditioning of a Problem
The [[Condition Number]] of a problem tells us if a problem is [[ill-conditioned]] or not. The way we formally approach [[Condition Number]]s of problems is by considering 2 normed [[Vector Space]]s, $\mathcal{X},\mathcal{Y}$, and some, usually continuous, and generally not linear function $f : \mathcal{X} \mapsto \mathcal{Y}$. 

We consider the behavior of the function $f$ at the point $x \in \mathcal{V}$, we might refer to this as a problem and also a problem instance. A problem that is [[Well-Conditioned]] results in small changes to $f(x)$ whereas a problem that is [[Ill-Conditioned]] results in large changes to $f(x)$. 

