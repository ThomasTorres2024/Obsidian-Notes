---
title: Prolog
tags:
  - Fundamentals_Prog_Langs
draft: "False"
---
# Prolog 
[[Prolog]] is a [[Logical Language]]. We begin with __facts__ which are declarations of true statement. In prolog these must be positive assertions. 

In Prolog, a program is a collection of facts and rules. A simple prolog program can be of the following form: 

```
man(phil).
man(john).
woman(betty). 
```

Prolog will treat all of the above statements as true and add them to the existing knowledgebase. Prolog programs are executed by posing queries to the knowledge base For instance the following are queries: 

```
?-man(phil). 
?-woman(phil).
```

---
# Prolog Queries and Goals 
A query is a way to extract information about a logical program. When a Query contains a variable, it is existentially quantified. For instance in the following Query: 

```
?-parent(X,liz)
```

We would get all $X$ such that $X$ is a parent of Liz, and would be false if no such parent exists. A variable in Prolog is something that __begins with a capital letter__, everything else is a constant and written in lowercase. 

---
# Compound Queries 
Conjunctions can be used in querying as well. We can use compound statements with the conjunction operator, for instance consider: 

```
? -  parent(X,Y), parent(Y,ann).
```

When Prolog tries to satisfy the compound condition it will always make that sure that both $Y$ always have the same values. In the language of prolog, this is called a compound goal, which in order to be satisfied  needs to have its subgoals satisfied. 

Prolog makes use of unification and backtracking to find _all_ of the different solutions to a compound goal. 

Unification is a type of pattern matching, that instantiates variables with terms/objects on. Backtracking allows us to search all unifications (substitutions) which make a query true. 