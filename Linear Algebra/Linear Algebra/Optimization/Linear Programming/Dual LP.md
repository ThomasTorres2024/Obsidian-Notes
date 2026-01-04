---
title: Dual LP
tags:
draft: "false"
---
# Dual LP Problem 
For any [[Linear Programming]] problem, there is a [[Dual]] [[Linear Programming]] problem that is equivalent to the "Primal" [[Linear Programming]] problem. We have the properties of [[Weak Duality]] and [[Duality]]. 

### 1.) Weak Duality Property 
In a maximum [[Linear Programming]] problem, the value of the primal for any feasible solution is bounded from above by any feasible solution to its dual. For the objective function $\bar{z}$, and the corresponding dual objective function, we can write the following for the maximum and minimum cases:
$$\max \implies \bar{z} \leq \bar{w}$$
$$\min \implies \bar{z} \geq \bar{w}$$
### 2.) Unboundness Property 
If the primal problem has an unbounded solution, then the dual problem is infeasible. This property arises from the weak duality property. If the primal problem is unbounded, then the objective functions have no guaranteed bounds.

### 3.) Strong Duality Property 
If the primal dual problem has a finite optimal solution, then do does the dual problem, and the values of the primal and dual objective function are equal at their optimal solutions:
$$z^*=w^*$$
---
# Primal and Dual Problem Comparison
Any [[Linear Programming]] problem can be considered as the Primal or the Dual. 

| Primal LP                | Dual LP                  |
| ------------------------ | ------------------------ |
| feasible                 | feasible                 |
| infeasible               | infeasible               |
| infeasible               | infeasible and unbounded |
| infeasible and unbounded | infeasible               |
