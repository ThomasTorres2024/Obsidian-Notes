---
tags:
  - Secure_Programming
  - Cyber_Security
title: Testing
draft: "False"
---
# Testing

We have various kinds of testing:
* Static/Dynamic 
	* A static test is more of a code analysis, tries to find bugs by looking at the code as it is (maybe like Rust Analyzer)
	* Dynamic Analysis is running code with several test inputs and seeing its performance. This can be either automated or done manually. 
* Clear/Opaque-Box
	* Clear box is known code, meaning we can access it and directly deal with different code paths, dealing with different edge cases etc. 
	* There also opaque (black box) tests, where we only know the input and the output. These tests are still useful but a very different kind. 
* Unit
	* A type of test where for every function or module within a codebase we write a separate test for each. 
* Integration
* Regression
* Coverage
	* Ensure all code is actually executed

---
# Static Code Analysis

These consist of compiler warnings, lint-type tools (lint is the first C program to have done it and has this name), Code Reviews can be done if we have [[Git]] pull requests. 

Each type of tool can find different flaws

- Variables used before initialization
- Incorrect comparisons and conversions
- Resource leaks
- Dangerous functions
- Infinite loops, might make some very easy to spot especially if they are subtle. Take for example we have a forloop with $>$ instead of $<$ or something.

---
# Runtime Testing

We want our code to perform functions as expected:
* Procedure expected output
* Includes security Features

Input Validation - Code Detects bad Input 
Run time behavior
* Code doesn't incorrectly access memory
	* Accessing memory out of range, buffer maybe to small
* Code doesn't use too many resources to perform actions
	* Depends on the computation we expect to perform, and how many resources we are going to use. 
	* Example, the web server thast wanted to read an entire file that was very large into memory. This is something we would like to be able to evaluate.
* [[Race Condition]]s hard to test manually; but tools exist 

```bash

valgrind --leak-check=full ./target_program
valgrind --tol=helgrind ./target_program

```

If we compiled code with all of our flags, we would be able to do quite well with these. 


---
# Parsers and Generators

* Parsers are difficult to implement Properly, since they deal with user input, which can be anything. The more we can constrain user input, the more we can test our code and make sure it meets our requirements. 
* Considerations:
	* Format - Does it meet the requirements. 
	* Length - What size is appropriate for chunking? What do we do when a user gives us a 4kb long name?
	* Depth - Are there recursive structures? Important for [[HTML]] documents or maybe zipped files. Virus scanners do not want to use too many resources, so if there are many recursive directories, it might just stop at some arbitrary directory and might not want to continue. Same can be true for overly complicated HTML until page decides not to render it
	* Evaluation - Use a state machine. We can use a state machine to track where we are in the file when processing it. 

When creating a paraser, we also want to create a generator for validation. 

* Generator should be able to generate all acceptable strings.
* Generator should be able to generate rejectable strings as well.

These should only break on a single condition, having extra things wrong doesn't really help.

---
# Fuzzing

* Another automated tester. 
* We throw noise at a program to see how it responds. 
* Crashes the program means this isat least denial of service, but often is also an exploitable avenue. 
* "Smart" fuzzing is doable with tools like "american fuzzy lop". Tries to force code down different paths
	* Takes some input flips bits trying to explore all paths
	* Saves input that causes crashes for further investigation

```
afl-fuzz -i inputs -o outputs -- ./target\_program
```


---
# Unit Testing

* Unit may be function class or module level
	* Tests external behavior, not implementation 
* Some functions we need to test might be complicated and naturally run off of a database, so we need mock objects to run things. Sometimes we might make these too simple and they can backfire. 

---
# Coverage Testing
- Check that every line is reached
- Compilers can tell when a line is never reached
- Example tools per language 

	- C/C++ gcov/llvm-covv
	- Python python3-coverage

```

gcc -coverage -lgcov -o main main.c

```

---
# Testing Frameworks

* Annotate or name functions or classes that represent tests
* Build a separate binary to run all the tests
* Produces a report of tests run and failures 
* Sometimes requires refactoring of code into more generic pieces 

	* Functions that read from stdin or write to stdout should take a file/stream handle instead of referencing them directly
	* Use istream/ostream in C++ so the i/o can be from a file or a string
	* Use InputStream/PrintStream in Java
	* Use IOBase in Python (supports StringIO/BytesIO/FileIO)

---
# Integration Testing 

- Sending/Receiving data from other programs or 3rd party libraries
- Documentation says how it should behave, not how it does
- Especially important to have during dependency upgrades
	- Read release notes, not breaking change
	- Check patches for safety
* Sometimes successful operations also have failures
	* By Default MySQL will truncate a field to the size of the column, produces a warning but says it succeeded. A separate call is needed to determine if this happened. This is default behavior
	* Use STRICT_TRANS_TABLES to prevent the truncting this behavior and we get a proper error

---
# CI/CD

* Integrate and automate testing in dev pipeline
	* Rules like, on push to branch run test suites
	* Or on push to branch deply to qa website
* Detect issues early for faster releases 
* Enhances product reliability 

---
# Logging
- Use a logging system
- Very important for testing, if we log every operation we have a trace of what actually happened and what executed to see the errors that happened and fix them
	- Specificying destinations by severity
	- Specifying destinations by source
	- Timestamps
	- Code Location
	- Formatting the data

---
# Null Values 
- Does the environment distinguish between null,empty,0?
- Static analysis might be able to check annotated code:
	- @Nullable value could be null
	- @NonNull value is never null
* FindBugs or Checker Framework supports these

---
# [[Types  (FPL)]] 
* If using a weakly typed system, might be necessary to check
* PHP note
	* is_int Says if variable is integer
	* is_numeric Checks for decimal floating values from string 
* Java: Integer.parseInt() (if this is built in and doable for us in advance, just use this )

---
# Range
- All values for data type (INT_MIN, INT_MAX)
- A subset of values (0-10)
- A specific set of values (a,e,i,o,u)
- A value with a particular property (greater than 0, prime)

---
# Writing a Parser
- Never should assume input has the correct format
- How does the parser handle invalid input?
	- Error
	- Warning
	- Ignore (explicitly)
	- Ignore (implicitly)
	- Reduce functionality
		- maybe not enable a feature or something if parsing is weird (think of config files)
* Track location for error reporting
* Parse entire entry before processing
* Example: Parsing CSV file: ensure fixed number of columns
	* If our criteria is we have 10 columns then stop there.
	* If we have an arbitrary csv file but we don't care about the number of columns, but say we need the same number of columns, we could have a verification step that errors out in this case 

---
# Regular Expressions

Regular Expressions allow for validating the format of a string using a template:



* ? - 0 or 1 
* () - a group
* "$*$" 0 or more
* "$+$" 1 or more
* $\{ n, \}$

IP Example:
We have $4$ integers separated by periods, where each 

---
# Integer Overflow
* All basic data types have a finite range of values
* Integers can range from $-2^{31},2^{31}-1$
* Arithmetic on these types cause values to go out of range
* Integer.MAX_VALUE+1 == Integer.MIN.VALUE

---
# Race Conditions
* File access race condition
* TOCTOU - Time of check time of use 
	* do a check before we open and try to mess with the file 
* Check for ownership and other file permissions before reading a file
* Relies on not being able to replace file between check and access
* Creating temporary files must be done with care, we need to create and double check location and permissions before using.

---
# Memory Handling Errors
* Static analysis can pick up overflows
* For dynamic testing, providing a lot of data causes program to crash if it vulnerable to overflow
* Sometimes dynamic analysis tools will miss overflows that only onwrite a few bytes
* Tools like valgrind can give exact location of where a buffer overflow happened
* gcc/g++ has an -fsanitized=address option to detect memory errors
* 