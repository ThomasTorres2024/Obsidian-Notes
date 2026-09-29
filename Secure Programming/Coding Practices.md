---
title: Coding Practices
tags:
  - Secure_Programming
  - Cyber_Security
draft: "False"
---
# Coding Practices 
When working with a compiled language, its best to enable all compiler warnings. Use assertions to verify internal preconditions are correct. 

We are also encouraged to make use of strong types, and write functions "without side-effects". 

Errors should be handled appropriately, and we should understand the resource management of the language. For instance if we have a built in garbage collector or we are in C/C++ and have to do this ourselves. We should also make use of code analysis tools. 

In gcc the following can be used as compiler warnings:
```
Wall -Wextra -Wmisleading-indentation -Wconversion -Wshadow -Wcast-align -Wmissing-declarations -Wmissing-prototypes -Wnested-externs -Winline -Wunused -Wmisleading-indentation -pedantic-errors
```

In g++ we have everything used in gcc and the following:
```
Weffc++ -Woverloaded-virtual -Wold-style-cast -Wsign-conversion -Wsign-promo -Wstrict-null-sentinel -Wnon-virtual-dtor ✔ javac (Oracle): -Xlint:all
```

In php we have in the developer environment ```error_reporting(E_ALL)``` and in C# we have ```/warn:4```. 

---
## Using Assertions
Assertions are conditions which should always be true in a program. Importantly, there are no side effects to assertions.

Our environment or compilation may remove assertions so that code does not rely on the side effects, consider the following:

* Java: java -ea 
* C/C++: ```#include <assert.h>```
* C/C++: ```#define NDEBUG```

---
### Assertions vs Exceptions

* Assertions should be used for internal consistency checks and __NOT__ for input validation from users. 
* Assertions should __NOT__ be used for public method parameter checks 
* Assertions should only test conditions that are __not false__
* When we have things that might be poorly formatted we would tend to use Exceptions. 

Each language generally has their own variants of exceptions:
* In Java assert() throws the AssertionError
* In C/C++ assert() calls abort()
* PHP issues warnings and can terminate 

---
## Write Functions without Side Effects 

Functions should do one thing and do it well. Functions need to be separated. One function should do I/O with console, files and networks etc. We should also make use of ```const``` modifiers when they are available if we have values hat do __not__ change. 

Consider the following code that does two things:
```
function checkPassword ( username , password ) {      dbPassword = getPasswordByUserName ( username); 
     if ( password == dbPassword ) { 
     sessionstart(); return true; } 
     return false ; 
}
```

The function starts a session __and__ it also determines if the password checked is equivalent or not. 

---
### Using Strong Typing 

Strong typing allows the compiler to find mistakes. Good compilers will "optimize away overhead of simple objects" (I assume this means turning them just into variables or something easier to work with?).  

Consider the following:
```java 

class UserName{ string sUsername;

	public:
		UserName(string username) : sUsername(username){}
string getUserName() {return sUserName;}

}

UserName newUser(postUserName);
newUser="me"; //this is invalid, we are trying to
//assign a str to user name 

```

---
### Error Handling 

We generally prefer to do exception handling than error codes. We want to handle errors as close to the source as possible, and make sure that we do not lose information during the stack trace. We want to translate errors into higher level messages during the stack trace as well. 

For example consider the following in a voting system:
* The vote was not cast 
	* The selected option was not valid
		* '+' is not an integer in the range $[1 \dots 3]$

---
### Null Values

We want to avoid turning null values if possible. If we return null from a function we lose the ability to chain for instance:

* ```get().compute().transform()```
* If get or computer returns nulls, we get a null pointer exception (NPE) 
* It is better that get and compute throw separate errors so it is easier to determine where the failure happened 

We prefer to return an empty container instead of null, like a null list or null tuple. 

#### Null Values in Java

```java

public class nullthis{
	static class A{
		public void f() {System.out.println("in f");}
	};
	
	public static void main(String argv[]){
		A a=new A();
		a.f();
		
		A b = null;
		b.f();
	}
}

```

The line ```b.f()``` gives a NPE.

#### Null Values in C++
```C++

class A{
	public:
		void f() { std::cout<< "in f" << std::endl;}
}

int main(void){
	A a, *b = nullptr;
	a.f();
	b->f();
	return 0; 
}

```

---
# Strings in C vs C++

In C strings are represented as character arrays. There is no inherent length, we must pass this with each call that modified. We require a \0 at the end for termination.

We should use "n" versions of functions like snprintf, etc. 

In C++ we have std::strings, which come from the standard container. These track the internal length of our strings. The tradeoff is that 50% more space is used via the default allocator. It may be "harder to use a secure buffer".

---

### Safe Function Calling

In C++ values for basic types is supported by default. We also get objects returned by ref/pointer. We prefer to return const references, which prevent the nullptr and the target of the pointer from being changed. 

In python we have reference objects by default. We need static type checking for const like. 

And in rust everything is immutable by default.

---

## Resource Allocation 

Principally we want to constrain a resource to the scope of a single function. Through this we have:

* Resource Allocation is initialization (RAII)
* Ensures resources are even released on errors 

Otherwise, ensure that all other code paths release the resource properly. 

---
# Use code Analysis Tools
* Java : FindBugs
* C: lint / clang-tidy
* C++
	* cppcheck
	* clang-tidy
	* flawfinder
* php : PHP Mess Detector 
* .NET : Fxcop
* Python: flake8, pyre

---
## Adding Dependencies 

- We can open and closed source dependencies in order to speed up development
- At the end of the day we as the programmers are responsible for everything delivered in the final, even the dependencies 
- We need to be able to evaluate the quality of the code in a package

	- Does it use safe constructs?
	- Does it include unnecessary features? Can we disable them?
	- Does it contain test-suites?
	- How are changes reviewed? 

* We need to verify the functionality of each module that is included 
* Scrutinize point releases to existing dependencies
* Use containers or VMs to build
* Automate dependency release checks CVEs 