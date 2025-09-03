---
title: Variables in Dart
tags:
---
We have a few different ways of declaring variables in [[Dart]]. We have the "var" keyword, that allows our variable to get reassigned.

We have the [[final]] key word that means that a variable cannot change. The same is also true for the [[const]] keyword. 

Also [[Dart]] is a [[statically typed]] language, meaning that we cannot change the type of a variable once it already has been assigned 

We can add type annotations in place of [[var]],[[final]], or [[const]]. 

---
# Variable Annotations
Dart supports variable annotations for the following types:
* Numeric: int, double, float 
* bool
* string 

---
# Nulling Variables 
Unless otherwise specified, if a variable has no value it must be given one. We can bypass this property using a ? mark:
```
//not allowed
int points;
print(points);

//allowed 
string? chumungus;
print(chumungus);
```