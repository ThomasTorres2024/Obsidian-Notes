---
title: Grammar
tags:
draft: "False"
---
# Grammar
A [[Grammar]] in a [[Programming Language]] is composed of four different parts. A set of tokens, a set of non-terminal symbols, the set of productions, and a start symbol that is non-terminal. 

Tokens are the "smallest unit of syntax". These are atomic elements not composed of anything else, for example strings in our language. In a programming language, we consider keywords such as (if,then,etc..) tokens and operators as single tokens. 

For instance, let us consider a small version of English:

![[Pasted image 20260126214711.png]]

Non-terminal symbols in our language are strings that are denoted by symbols in brackets, meaning that each [[node]] should have a child node at least. 

A production has a left hand side with an $=$ operator, and a right hand side4. The left hand side produces 1 non-terminal symbol, and the right side is a sequence of multiple things. A production gives us a way of building a parse tree. This essentially is a rule that allows us to replace the value of some symbol with that of another symbol.

Also, sometimes an empty string is a member of some programming languages. 

Program files are represented as text files, where we need to be able to distinguish from phrases, keywords, and other elements that are a part of the language from the perspective of each character in our program, including tabs white spaces, end of lines, etc, as a token. We need to be able to reconcile both viewpoints. We specify a grammar for the "lexical structure" and one for the "phrase structure". The previously discussed structure of a [[Parse Tree]] consists of the "phrase structure". The "lexical structure" parses the program as characters and is considerably simpler. 

When we want to compile a program, we have a scanner component, or the lexer, which reads in all tokens discarding whitespace and comments. Then, we have a parser which converts the file into a [[Parse Tree]]. 

---
# Other Forms of Grammar
Previous discussion of [[Grammar]] has been limited to "Backus-naur Form" grammar. There are some variants with slightly different notation. For instance EBNF adds some additional "meta symbols" that are not actually a part of the [[Grammar]] itself, but rather allow us to have an easier time reading and understand the language's underlying grammar. Any system that extends BNF is known as EBNF. 

We can also express [[Grammar]]s as a syntax diagram. These are meant to be easy for humans to understand but are fairly impractical and are not really machine understandable as much as a typical ruleset provided by BNF. 
