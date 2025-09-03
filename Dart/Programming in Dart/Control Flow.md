[[Dart]] Loops have a [[C]] family syntax when using $i$ based loops. We also have foreach loops that look like python:
```
for (int score in scores){

}
```

Note also that in our for each loops we have a method that allows us to do some filtering on the elements we are working with using the "where" function:
```
for (int score in scores.where((s) => s > 50 )){

}
```

If and else statements have standard syntax as well. Equality signs are just 2 equal signs. 