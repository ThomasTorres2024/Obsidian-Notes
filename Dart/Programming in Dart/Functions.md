[[Dart]] functions are basically just [[C]] style functions. We don't need to specify types necessarily but obviously we should. 

If we specify a return type and give another type out, then our program crashes or could behave unexpectedly. 

We also have [[nullable]] and [[required]] parameters in our functions. A nullable one is an optional parameter, and a required parameter is necessary. 

We can pass in these parameters as such:
```
greet(required String name, required double age){
}
greet(name : "hi", age : 30 )
```