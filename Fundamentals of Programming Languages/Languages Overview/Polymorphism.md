---
title: Polymorphism
tags:
  - FundamentalsProgLang
draft: "False"
---
# Polymorphism 
[[Polymorphism]] is a property of [[Programming Language]]s where the subtypes of a [[Types  (FPL)]] (typically in classes) can be treated as equivalent to their parent type. Trying to formally define [[Polymorphism]] is quite difficult. There are many forms of polymorphism that we must account for. 

---
# Overloading Polymorphism
Overloading polymorphism is a type of polymorphism where we take some function $f$, and the function $f$ has the name, but the function's declarations uses different types. The programming language uses the types provided to it to use the proper function with the correct signature to match the input types, assuming such a function exists. 

In languages like C++ we have operator overloading, which essentially is function overloading that we can implement by changing or providing meaning for some symbols in our code, like if we defined +,-, etc. 

Function names can also be overloaded by having functions that support multiple types. Underneath the hood languages essentially append the name(s) of the datatypes to the end of a function in order to support function overloading. 

---
# Parameter Coercion
Implicit conversion of a [[Types  (FPL)]] is known as coercion. If a type can be cast (typically through a widening conversion) to another type, then the compiler/interpreter for a language will accept this. For instance in Java if we have:
```java
void f(double x){
}
```
Using any subtype of double here, byte,short, etc, would be more than appropriate since these types can be converted safely to the double type. Coercion can be nice since it makes it not necessary to write obvious type conversions between different types when they should be equivalent. 

We may run into errors if we combine this idea with function overloading. Take the following functions, given some ```char x```:
```C++
int square(int x){
	return x*x;
}

double square(double x){
	return x*x;
	}
```
If $x$ is of type char, then using this code in many circumstances is ambiguous and is something the language needs to decide on. In C++ because a char is closer in the hierarchy than to double, it would use the integer variant. Some compilers may flag this as being ambiguous. The problem is worse when we consider multiple parameters. 

---
# Parametric Polymorphism 
The idea of parametric polymorphism allows us to define functions, classes, and other things in programming languages given a parameter name, typically $T$, where $T$ denotes a type. In C++ these are done through templates, in Java these are done through Generics. Rust supports these as well. 

There are 2 ways that a language supports parametric polymorphism. 
One such way is to create separate copies of polymorphic functions, which is what C++ does. From this point on we essentially would be doing function overloading. One of the weaknesses of this style of implementation is that the language must make many copies of the exact same code, increasing compile times. Another way to handle parametric polymorphism in a language, is to create a single copy of the function, which all different callers use. This slows down the overall execution speed, but it is a lot easier to compile and to produce and cuts out the need for all of the different function redeclarations. 

---
# Subtype Polymorphism 
Recall that a subtype is a subset. If a function works on a parameter in a given set, it can work on any parameter in the subset of that set. For instance, if we have a class $A$, and then $A$ has a childclass $B$, any method that works on $A$ should also work $B$ since by polymorphism $B$ can be treated as being of type $A$ since $B$ is a subset/subtype of $A$. 

---
# Dynamically Typed Languages 

In some languages like Prolog, Lisp, etc, dynamic type checking is used, which makes polymorphism irrelevant. Here, languages are a lot freer so to speak. We do not actually check at compile time, but during execution. This can cause a lot of errors at run time, and make it harder to debug. 