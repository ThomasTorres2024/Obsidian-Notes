---
title: Types (Programming Languages)
draft:
tags:
  - Fundamentals_Prog_Langs
---
# Types in Programming Languages
A type in [[Programming Language]]s is essentially the equivalent of a set in math. When a variable is initializes, say for instance 
```
int n = 4;
```
We are saying that $n \in \mathbb{Z}$, and the programming language tries to encode this fact. $n$ cannot be a string, and it cannot be a float. Types also have common methods that work on then. For instance there are many different operations that only work on integers, for instance the $\mod(n)$ operator in many different languages, or even more abundantly string manipulation methods.  

We can add and subtract integers in many programming languages, but the same operators on strings is generally undefined behavior. 

---
# Primitive Types vs Constructed Types
Languages in the modern day support constructed types. Languages begin with "primitive types". We can then build more advanced types out of these types and define them as programmers. More formally we define primitive and constructed types in the following:

Any type that program that can use a type but cannot define on its own is a __primitive type__. Any type that a program can define for itself is a __constructed type__. 

The definition for each [[Programming Language]] should describe the definition of each type. Sometimes these definitions are very strict on what is permitted, whereas in some other instances we have more liberty to what can be assigned. For instance Java defines an integer to always be some number in the range of $[-2^{31},2^{31}]$ (this is intended to be the case since Java is meant to be platform independent, and always should compile to the same everywhere). Whereas C or ML have definitions that depend upon the compiler, and so it may differ on some devices if translating to machine code in 1 way results in a more efficient program or compilation process.  

---
# Type Hierarchies 
Depending upon the programming language, the language may support the fact that some types are actually subtypes of other types in the language. Say for instance in C we have the following type hierarchy:

$$\text{char} \subseteq \text{short } \subseteq \text{int} \subseteq \text{float} \subseteq \text{double} $$

A conversion that takes a type from a lower type to a higher type is known as a widening conversion, and this generally is safe to do. But a conversion from a type that is higher to one that is lower is known as a narrowing conversion and generally is unsafe. 

---
# Enumerations 
A simple way to construct a set in math is to explicitly list the items within a set. One way that this can be done in a language is by using Enumerated types. 

We define new types that have their own identifying name. For instance, if we wanted a type for coins, we could do the following (example is in C):

```C
enum coin {penny, nickel, dime, quarter};
```
Some languages, such as C and Pascal, like to have each type in an enumeration indexed, and allow us to work with these types by a particular 

---
# Tuples 
The idea of a Tuple is related to that of the [[Cartesian Product]]. For sets, $A,B$, the [[Cartesian Product]] is $A \times B$. By repeated use of this operation we can produce $n$-tuples, or tuples with $n$ many elements. 

In C for instance, [[Struct]]s are a type of tuple. Structs are just tuples where each member has a named component that we can work with. In Python we directly can assign and work with tuples. The way Structs are handled in C places all of the items that are assigned in order in memory, and this is something the user is exposed to. Whereas in ML, all of this is hidden and abstracted from the user. 

---
# [[Array]]s Strings and Lists 
Let $A$ be a set of characters. The set $A^{''}$ is the set of vectors of size $n$ such that for $v \in A^{''}$ we have for $v_{i} \in A$.  We can think of $A^{''}$ as another way to rephrase repeated application of the [[Cartesian Product]].  

Almost all languages have array types. Some languages support $0$ based indexing, whereas others support $1$ based indexing (Lua, MatLab). 

---
# Unions 
In math, for sets $A,B$ we have that:
$$A \cup B = \{x \in A \lor x \in B\}$$
We can define a type ourselves that consists of elements from one type and of elements from another. In Python, for the set type, we have an explicit union operator. 

---
# Subtypes
For some type $S$, we can define a subtype $T$ such that $T \subseteq S$. Typically the subtype inherits the operations that are in $S$, but we can also define additional operations for $T$ that are unique to it. 

Note that in OOP, we do this often with classes, and use inheritance to either override previous methods and support them in a new way, or to define additional operations. 

---
# Function Types 
For sets $A,B$, we define a function type to be a mapping defined by $A \to B$. 
[[Functional Language]]s tend to be the programming languages which support the most operations on functions. Depending upon the language, the way that functions are treated and can be modified varies significantly. 

---
# Uses for Types
### Type Annotations
A type annotation is necessary in a language that is not dynamically typed like C or Java where the type of a variable remains the same for the execution of the entire program. Whereas in a language like JS or Python that is dynamically typed, allowing ourselves to annotate the type is a good thing and generally leads to less issues during program execution. 

### Type Check
If we perform some operation on a data, we need to be able to ensure that the operation performed on the data actually has that the data is of a specific type. If we are trying use modulus on a non-integer, we might run into an issue. The program/compiler makes an explicit check for the type before actually running some corresponding code. If the data does not match the expected type, then we get an exception and the program might crash. 

We also have dynamic and static type checking. Dynamic type checking occurs in languages which do not compile, languages like Python or MatLab, which do not have an intermediary step of translation to machine code. These languages only perform checks as needed during execution. If there is mistyped and poorly designed code, as long as the interpreter never reaches those lines, the code executes fine. Static type checking is used in compiled languages like Java and C++. During compile time, all of the code and all paths, even those that aren't written down, are type checked, and those that do not match result in an error message and the compiler crashing. 

## Type Equivalence 
In order to check if two types are the same we need a notion of types being equivalent. Some languages go by nominal checking,  which is to say if two types are declared with the same type's name, they are recognized as the same type. This is the case for Rust. There is another type equivalence known as structural equivalence. Say two types have identical components, then the compiler reads them as being the same. This is the case for Haskell.  


