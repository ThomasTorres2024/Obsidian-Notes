In C and C++ common sources of memory issues arise in:

* buffer overflow, if not enough space is allocated to some kind of input, additional memory outside of the expected amount is added
* dangling pointers
* memory leaks 

C,C++ run into numerous errors and are generally unfriendly during compilation. These languages rely on manual memory allocation through malloc and free in C, and new and delete in C++ respectively. In C there are numerous systems for building such as make, cmake, muck etc..

In Rust, there is also manual memory allocation but with significant safety checking. There is also a single building application used across platforms which is called cargo. In Rust numerous classes of programs are already prevented (though there's a keyword named unsafe which allows for this), for one checks exist that do not allow code with dangling pointers to compile. 

In C we consistently need to check the null pointer exception in the instance of failure, for instance cosider fopen and malloc. 

Rus doesn't have variatic functions like in C/C++ that allow for $n$ args to get passed into a function, instead in rust we have macros. Say we want to print something with $n$ args, then during compile time the macro generates a corresponding function that has n arguments 

In Rust we do not have exceptions precisely, we have __panics__, which terminates a program safely, but there is no way to catch an error. This can make assert statements tricky especially in library code. 

---
### Types 

In Rust there is an Option type, which takes in parameter $T$ and is a form of parametric polymorphism. Something of Option is either some instance of itself or none, and in order to compile and run any such code it must first be checked. Similarly we have Result to a std::vector$\langle \text{string} \rangle$ which inputs a parameter type and some general error which is how an instantiation of Result is checked

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

Rust __is not__ an object oriented language. Rust deals with class oriented behavior in "Trait" behavior. 

---

### Invariant Def -
- a statement where truth can be checked at any time 

### Loop Invariant -
A statement of the condition should be true when entering a loop and true after every iteration. During the operation however the condition we are iterating against may be changed during execution of the loop. There's also some correspondence between [[Induction]] and this notion here of loop invariance. 
### Rust Tools
Rust quickcheck 
- useful mechanism for automatic case generation and error checking 

Use cargo clippy, linter, mentions things that are not idiomatic, maybe too complex

### Invariants of a [[Sorting]] Algorithm (Insertion Sort)

```rust 

pub fn insertion_sort<T:PartialOrd>(s: &vec<T>){
	
	//similar to how a 
	for i in 1..s.len(){
		let int j = i;
		
		while j>0 && s[j-1] > s[j]{
			s.swap(j-1);
			j-=1;
		}
		
	}
	assert(issorted(s[0:i]));
}

pub fn is_sorted<T:PartialOrd>(s : &vec<T>) -> bool{
	for i = 0..s.len(){
		
	}
}

fn main(){
	let mut a = vec![42,1,3,7,2,70];
	
	insertion_sort($insertion_st a);
	
	//this is needed for displaying contents of a vector 
	//traits, display and debug are here
	println!("{:?}",a);
}


```

The above code should fail to compile if anything passed in is not orderable, for instance the entirety of a hashmap. While its keys can be sorted, the map itself cannot be. 

The loop invariant here is that for for $i$ in the range of $0,\text{len}(s)$ that it it is sorted through these indices and we hope that this is maintained. It's trivially true when we start when $i=0$ (pretend it starts at $1$). We hope that when $i=\text{len}(s)$ and we stop executing by then we will have that all of contents of the vector will be sorted  
 
Foor loop here is a bit similar to the way for loops are written in [[Python]] through some range

```rust

let counter: HashMap <string,usize> = words;
	
	//this "consumes collection and takes ownership of it"
	// "destroys" words
	
	//this is basically a reduce function map is the accumulator word 
	//is the iterator 
	.into_iter().fold(HashMap::new(),|mut map,word{
		*map.entry(word).or.insert(0) += 1;
	}
	
	//in HashMap::new() we create a new hashmap, 
	//by map,this serves as a return type  
	
	map 
	
	});
except
```

In this sample we have a loop that is not explicit, we have a "fold" (this is similar to [[Reduce (Functional Programming)]]) 

---
# Option Types in Rust 

Sometimes in Rust we want to be able to deal with things that are either one type or null, which is where we make use of "__Options__".  Under the hood, Options is either Some(T) or a null pointer namely None. 

Consider the following code:
```rust

fn lookup_player(id u:32)->Option<String>{
	if id == 1{
		return Option::Some("crabby".to_string());
	}
	return Option::None;
}

```

Here we have the Option::None type to denote nothing, and otherwise we need to convert the &str type to String, and then make it an option via the Some function. 

There is a shorthand in rust that we can use in order to assign things correctly if the value is None or not:

```rust
let player = match lookup_player(1)?;
```

We have several options for extracting the $T$ from Option$<T>$, namely:
- unwrap
	- Panics on none type 
	- avoids pitfall of referencing a nullpointer 
	-  ```rust
	  
		let z : Option<u32> = foo();
		do.something(z.unwrap()); //do something expects u32 type, not option
		
		//passing z alone makes code uncompileable
		//with unwrap if z is a value, then we operate, otherwise we panic
		//and func never called 
	  
	  ```
* unwrap_or(x) 
	* always evaluates x
	* Takes parameters for what to do if none occurs
	* Best way to handle thi is by offering some kind of default value
* unwrap_or_else(x)
	* only evaluates x if its valid 
* Pattern Matching
	* Similar to cases, every case needs to be exhaustively handled here and secondly if not we need to have some default case 
	* ```rust 
	  let z open<u32>=foo();
	  match z{
		  Some(val)=>{do something}
		  None => eprintln!("some error");
	  }
	  ```
* ? (Question Mark Operator)
	* ```rust
	
	fn bar(x:u32) -> Option<u32>{
		let z : Option<u32> = foo(x);
		
		//here ? means try to extract value from z
		//if theres a val, then call this function
		//if instead 
		let y = do.something(z?);
		some(y)
		
	}
	  
	  ```

	* Under the hood we check if z is null or not 
	* In the some case it's exactly like the match case, in the none case the compiler generates code such that the result will be null
	* We can only use $?$ in a function that returns either Option$<T>$ or Result$<T>$. 
	* Example with Result$<T>$: 
	* ```rust 
		
	   ``` 
---
# Ownership in Rust 
Ownership is a feature that allows Rust to be a memory safe language, which involves the use of "borrowing" and "slices". The central feature of the rust language is __Ownership__. Many modern languages opt for programs having their own garbage collector or likewise having programmers mangage allocations and deallocations manually. Memory management is handled in rust by owernship, which is a third option, essentially a set of rules that the compiler will check during compile time. 

#### Rules of Ownership 
* Each value in rust has a variable called its owner 
* There can only be one owner at a time
* When the owner goes out of scope, the value is dropped. 

##### Ownership and the String Type
The String type is (to my understanding) like a C++ string type instead of a C string and is stored on the heap. Consider the following code, which is wrong:

```rust

let s1 = String::from("hello");
let s2 = s1; 

println("{}, world!",s1);

```

You will get a __value moved error__. In most normal languages we would have two separate pointers looking at the same value on the [[Heap]], and referencing one of them here should be fine. In order to mitigate bugs like double frees, we require that only __one variable has access to its contents__ and as soon as we let s2 be s1, the s1 pointer becomes __invalid__. 

---
# Result 
The result type in Rust, Result$<T,E>$ is either an Ok(T) or Err(E) type where E tends to be a string type. We 

---
# Traits 

Traits in rust are a language feature that defines shared behavior across different types. These are similar to interfaces in other languages, but also contains other capabilities like default method implementation and generics. 

Take the following Rust:

```Rust

pub trait Summary{
	fn summarize(&self) -> String;
}

pub struct Tweet{
	pub username: String,
	pub content: String, 
	pub reply: bool,
	pub retweet:bool,
}

impl Summary for tweet{
	fn summarize(&self) -> String{
		format!("{}: {}",self.username, self.content)
	}
}

```

---
# Iterators 
* One important trait is that of an iterator.
* An iterator allows us to express the notion that can be traversed or iterated over. 
	* separates logic of how we visit from what we do 
* Vecs are iterable 

### Iterators as Traits:
```Rust

trait Iterator{
	type Item; 
	fn next(&mut self) -> Option<Self::Item>;
}

```
* The key here is the next() function
* We do not want to call next() directly always
* Key Points:
	* iter() iterates over &T
	* iter_mut() iterated over &mut T
	* into_iter()
		* iterated over $T$ itself
		* Since into_iter() takes self by value using a for loop to iterate over a collection consuems that collection 

