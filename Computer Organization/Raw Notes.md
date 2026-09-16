In C and C++ common sources of memory issues arise in:

* buffer overflow, if not enough space is allocated to some kind of input, additional memory outside of the expected amount is added
* dangling pointers
* memory leaks 

C,C++ run into numerous errors and are generally unfriendly during compilation. These languages rely on manual memory allocation through malloc and free in C, and new and delete in C++ respectively. In C there are numerous systems for building such as make, cmake, muck etc..

In Rust, there is also manual memory allocation but with significant safety checking. There is also a single building application used across platforms which is called cargo. In Rust numerous classes of programs are already prevented (though there's a keyword named unsafe which allows for this), for one checks exist that do not allow code with dangling pointers to compile. 

In C we consistently need to check the null pointer exception in the instance of failure, for instance cosider fopen and malloc. 

Rus doesn't have variatic functions like in C/C++ that allow for $n$ args to get passed into a function, instead in rust we have macros. Say we want to print something with $n$ args, then during compile time the macro generates a corresponding function that has n arguments 

---
### Types 

In Rust there is an Option type, which takes in parameter $T$ and is a form of parametric polymorphism. Something of Option<T> is either some instance of itself or none, and in order to compile and run any such code it must first be checked. Similarly we have Result<T,E> which inputs a parameter type and some general error which is how an instantiation of Result is checked

In C we have numerous types with a less logical system of presentation:
- int (32 bytes)
- short (16 bytes)
- unsigned integer
- float

And in rust we can make this explicit:
- u8
- i8
- i16
- u32
- i32
- u64
- i64
