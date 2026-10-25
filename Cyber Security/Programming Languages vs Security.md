---
title: Programming Languages vs Security
tags:
  - Secure_Programming
draft: "False"
---
# Define Language Vulnerabilities 

Constructs in languages can give rise to vulnerabilities because they are:

* Incompletely specified 
* Exhibit undefined behavior 
* Implementation Dependent 
* Difficult to Use Correctly 

---
### Predictability and Vulnerabilities 

* Predictable 
	* Run time behavior should be predictable from source code examination 	
*  Language Vulnerability
	* Property of a language that contributes to or is strongly correlated with application vulnerability 
* Application Vulnerability 
	* Security weakness, safety hazard, defect

For example in C, the strcpy method is vulnerable and is a language vulnerability. If strcpy is used, the program becomes unpredictable. 

---
### Unpredictability in Language Specification 

Unpredictable behavior from language specification comes from:
* Incomplete/Evolving Specification
* Undefined behavior 
* Unspecified behavior 
* Implementation-defined behavior
* Difficult features
* Inadequate language support 

#### Unpredictability in Language Usage 

* Porting and interopability 
	* Different choices for undefined behavior
	* Implementation defined behavior
	* Library function differences
	* Differences in hardware/OS support
	
* Compile Selection and usage 
	* Compiler quality
	* Compiler options affect output
	* Compiler is a blackbox under the hood when we program but we need to be aware of the machine code it produces 

---
# Vulnerable Language Feature Categories 

The following consist of vulnerable language features in general: 

* Types and Type Conversions
* Variables and Scoping
* Operators and expressions
* Control Flow
* Memory Model
* Specification
* Other (Macros, Generics, Compile/Runtime, Libraries)

### Type System 
Statically typed languages allow us to detect type related issues earlier. 

* Java < 1.5 : Integer i=5; is an incompatible type in these versions of java 
* Ada
	* Type Celsius is a new float
	* type Farenheit is new Float
	* Cannot assign a celsius to farenheit by accident 
* Dynamic Typing (the process of automatically casting a type to some compatible type during operations) eases development with type inference. Consider the following valid comparisons in (some) languages:

```
"foo" == TRUE, "foo"=0, TRUE !=0
```

### Type System: Strings 

* Null Termination
	* Considered by some to be __the most expensive mistake in language design__, made worse by library functions such as gets() and strcpy()

* Better design: address + length
	* More efficient 
	* Less likely to make off by one errors 

* Still really bad. Using one type of string in a language that uses the other. 

### Type System: Arrays

In some languages, bound check is optional. 

* This is usually excluded for performance reasons 
* Failure to check if an index is within the correct bounds can lead to over writing data, leaking data, or crashing  

### Type System: Pointers and Casting

Casting points from one type to another allows for flexibility in data interpretation:

```C
struct sockaddr_un my_addr;
bind(sfd,(struct sockaddr*) &my_addr,
	sizeof(struct sockaddr_un));
	)

```
Using the wrong type may lead to out of bounds reads and writes:
```C

char arr[10];
void* alias=arr;
int *other = alias; 

```

All of the operations above are _completely legal_ and have no warnings. But, if we were to write ```other[9] != arr[9]``` it would return as true. 

The reason why it fails here is that, 32 bit code that cast pointers to integers were broken when moving 64-bit environments. 

### Type System: Multiple Interpretations

C has unions (TODO I am not sure what this is double check)

```C
union { int i; double d; char c[4]; } 4;
assert(sizeof(u)==8);
```

The idea here is to save space. We use these as "variable" type variables (?????). Moves type system into application domain and ultimately has __no__ protection against using wrong types. 

---
# Variables and Scope 

```C++

int a; 

class A {int a; int foo() {return a;} }

```
If the declaration of $A::a$ is removed, ::a will be referenced instead. 


### Variables - Initialization 

* Referencing a variable before it is assigned causes bad calculations or crashes in the case of variables 
* Languages that require declaration can catch these at compile time 
* Static analysis can catch most of this for other languages 
* For most scripting languages this will be a run time error. 

---
# Operators and Expressions

- Inconsistent operator precedence rules. The following under the hood are interpreted as the same 
	- $x-1==0$ is  $(x-1)==0$
	-  x&1 == 0 is $x$ & (1 == 0) which is just $0$
* gcc does not warn about any of these patterns by default, but -Wparentheses allows these errors to become visible 
* clang warns with no options

---
# Control Flow 

For instance in C consider the switch statement:

```C

switch(a){
	case 3: do_3();
	case 5:
		do_5();
		break;
	case 8:
		do_8();
		break; 

}

```
We would like to be able to ensure that every case in the range is covered, unless we use default. We may want to use default in the instance where we are trying to catch a logic error. 

### Control Flow: Statement End 

C and C++ allow:
```C++

for(y=1,x=1;x<4;++x){
	y=x*x;
}

```
The additional semicolon on the first line will almost always cause some kind of error. But, the computation can also be done as the following:

```C++

for (y=1,x=1;y=x*x,x<y;++x)

```

But this in particular is unreadable and not nice to work with. In C++ we have a way to handle tasks like this, in C++ 20 with iotas:

```C++

auto range = std::ranges::views::iota(1,4);
auto y = std::accumulate(range.begin(),range.end(),1,std::multiples<int>());

```

### Control Flow: Return Values 

Consider the following function:
```
bDoSomething(int /*in/d1,int /*out*/&o1)

```
The result of this function returns true on success, and results in the variable o1. o1 should NOT be used if false was returned. This style of programming is hard to use for computation. 

```Java

int iDoSomething(int /*inI d1){
	if (d1>100)
		throw new IllegalArgumentException();/**/}
}

```

We can use the above function in computation, but IllegalArgumentException is an unchecked exception in Java. So it doesn't need to be declared to be thrown or caught. 


---
# Memory Model
* Explicit deallocation may be missed, or worse done twice
* Even garbage collection needs hints sometimes 
	* Without them memory leaks can still happen
	* Without them performance can still suffer 
* C's pointers lose information about how much data is stored at that location (it affects many items usually)
* In C++, alloc()/free() new/delete and new[]]/delete[] need to be paired, but correct usage is not decidable at compile time. Even when obvious, the compiler does not warn. 

---
# Unspecified Behavior 
A language specification may omit the behavior of some constructs. Take for example C:

* The order in which operands of an assignment are evaluated 
* The order of side effects of initialization list expressions
* The layout of storage for function parameters 

---
# Undefined Behavior in C 

Accessing out of bounds in array 
```C 
int arr[5];
int value=arr[10]; //undefined behavior
```

Dereferencing a null pointer:
```C

int *ptr=NULL;
*ptr=5; //Undefined behavior

```

Modifying a variable multiple times between sequence points:
```C
i=i++;
```

Dereferencing a point after it has been deleted:
```C

int *p = new int;
delete p;
*p = 10;

```

Using an uninitialized variable:
```C

int x; 
std::cout << x; //Undefined Behavior

```

Modifying the same variable in a single expression:
```C
int i=0;
i =i++1 + ++i; //undefined behavior

```

### Undefined Behavior in Java
Java attempts to eliminate undefined behavior but it can still occur. For example, out of bounds array access throws an exception but may crash the program is it not handled:

```java

int[] arr=new int[5];
int value = arr[10]; //Throws ArrayIndexOutOfBoundsException

```

Null Point Dereference:
```Java

String str = null;
int length = str.length(); //NullPointerException

```

### Undefined Behavior in Python
Python minimizes undefined behavior by raising exceptions. Example, division by zero:

``` Python
x=5/0.0 # Raises ZeroDivisionError, C/C++ == inf
```

Index out of bounds:
```Python

list=[1,2,3]
value=lst[10] #Raises Index Error

```

### Undefined Behavior in Rust 
Rust aims for safety, but undefined behavior is possible in unsafe blocks. Dereferencing a raw pointer without proper checks:

```Rust

let ptr : *const i32 = std::ptr::null();
unsafe{
	*ptr =10;//Undefined Behavior
}

```

Indexing an array out of bounds in unsafe code:
```Rust

let arr = [1,2,3];

unsafe{
	let value = *arr.get_unchecked(10); //Undefined Behavior
}

```

---
# Implementation

### Implementation Variability in C 
Size of data types:
```C
sizeof(int); //May vary between platforms, e.g. 2,4, or 8 bytes

```

Order of bitfields in structs:
```C

struct{

	unsigned a: 3;
	unsigned b: 3;
	
};
//The order and packagingmay very 
```

behavior of left shift on negative values:
```C

int x=-1;
x << 1; //Implementation-defined behavior

```

### Implementation Variability in C++
Order of evaluation of function arguments:

```C++

f(g(),h()); //Order of g() and h() unspecified

```

Storage duration of temporary objects 
```C++

const std::string& ref = std::string("temp"); //Lifetime of this variable may vary 

```

Size of standard containers:
```C++

std::vector<int> v; 
v.reverse(100); //Memory overhead depends on the implementation of this method

```

### Implementation Variability in Java 

Garbage Collection Timing:
```Java

System.gc(); //No guarantee when or if GC will run

```

HashCode Implementation:
```Java 

Object obj = new Object();
int hash = obj.hashCode(); //Implementation-dependent 

```

### Implementation Variability in Python

Dictionary key ordering, before Python 3.7
```Python
d={"a":1,"b":2,"c":3}
#Order not guaranteed here before Python 3.7 
```

Integer overflow handling:
```Python

x = 2**1000 # Behavior depends on python version, handled as BigInt 

```


### Implementation Variability in Rust
Memory layout of structs in absence of repr attribute:
```struct MyStruct{

	a:u8,
	b:u32,
}
``` //Layout is unspecified without #[repr(C)]