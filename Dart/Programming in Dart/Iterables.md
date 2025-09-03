---
title: Iterables
tags:
draft: "false"
---
# Definition of [[Collection]]
A collection is an object which represents a group of objects. Objects in the collection are known as elements. Iterables are a type of collection. 

Some common collections include:
* Lists, items contiguously laid out in memory accessible by indexes sequentially 
* Sets, each item can only occur once in a set
* Map, a correspondence between key items and items in a set 

#### Definition of Iterable 
An iterable is a collection which can have all of its elements accessed sequentially. In dart iterables are an abstract class, we cant initiate things of this type, but we can make new iterables by creating lists or sets. These classes inherit the method of everything in the iterable class. Elements of a map are also iterable. 

We can initialize lists using iterable, but since we aren't using [[list]] we have to use ``iterable.elementAt(x)`` in order to get any element at an index. We can also convert iterables to list using

```iterable().toList()```

### Methods of Iterables 
One of the methods we can use is the for-in loop, which is just a for each loop in other languages, which allows us to sequentially go through all elements of our iterable set:

```dart
void main() { 
  const iterable = ['Salad', 'Popcorn', 'Toast'];
  for (final element in iterable) {
    print(element);
  }
}
```
The Iterable uses the Iterator, an object used by the for-in loop to read elements from the Iterable object. We don't really interact with it directly because it's safer and easier to do it just using  a for in loop. 

We also have the first and last properties of iterables. We do not have a pointer to the last element, we need to traverse through the entire collection, which takes $O(n)$ to do, so it is slow. If we use first or last on an iterable, results in a [[StateError]]:
```dart
void main() {
  Iterable<String> iterable = const ['Salad', 'Popcorn', 'Toast'];
  print('The first element is ${iterable.first}');
  print('The last element is ${iterable.last}');
}
```

We also have the firstWhere method, which allows us to search an array for an element that satisfies a criteria instead of having to do an entire for loop and manually look for an item:
```dart
String element = iterable.firstWhere((element) => element.length > 5);
```
Here's an example of it being used passing functions into our function:
```dart
bool predicate(String item) {
  return item.length > 5;
}

void main() {
  const items = ['Salad', 'Popcorn', 'Toast', 'Lasagne'];

  // You can find with a simple expression:
  var foundItem1 = items.firstWhere((item) => item.length > 5);
  print(foundItem1);

  // Or try using a function block:
  var foundItem2 = items.firstWhere((item) {
    return item.length > 5;
  });
  print(foundItem2);

  // Or even pass in a function reference:
  var foundItem3 = items.firstWhere(predicate);
  print(foundItem3);

  // You can also use an `orElse` function in case no value is found!
  var foundItem4 = items.firstWhere(
    (item) => item.length > 10,
    orElse: () => 'None!',
  );
  print(foundItem4);
}
```

We also have to introduce [[Predicates]], which are functions that return true when a condition is satisfied. 

### ```every()``` Method 
If we want to check that all items satisfy a condition, we might use a for in loop, but we can also just use the every method to clean things up. For instance:

```dart
return items.every((item) => item.length >= 5);
```
We also have the ```any()``` method, which returns true if at least ONE element satisfies the condition that we are looking for. 

For instance look at the following:
```dart
void main() {
  const items = ['Salad', 'Popcorn', 'Toast'];

  if (items.any((item) => item.contains('a'))) {
    print('At least one item contains "a"');
  }

  if (items.every((item) => item.length >= 5)) {
    print('All items have length >= 5');
  }
}
```

Here is an example of the any function:
```dart
if (items.any((item) => item.contains('Z'))) {
  print('At least one item contains "Z"');
} else {
  print('No item contains "Z"');
}
```

---
# Filtering 

We have filtering methods that allow us to return all elements from an Iterable that satisfy a condition. Consider the following code:
```dart
var evenNumbers = numbers.where((number) => number.isEven);
```
Any even number gets put in this iterable. The object evenNumbers is an iterable object.

Here is an example of using any, every, and where in combination:
```dart
void main() {
  var evenNumbers = const [1, -2, 3, 42].where((number) => number.isEven);

  for (final number in evenNumbers) {
    print('$number is even.');
  }

  if (evenNumbers.any((number) => number.isNegative)) {
    print('evenNumbers contains negative numbers.');
  }

  // If no element satisfies the predicate, the output is empty.
  var largeNumbers = evenNumbers.where((number) => number > 1000);
  if (largeNumbers.isEmpty) {
    print('largeNumbers is empty!');
  }
}
```

---
# ```takeWhile()``` and ```skipeWhile()``` Methods
These methods allow us to filter elements from Iterable. With takewhile, we read in elements into an iterable until we run into an element that we declare that has us stop searching. 

The skip while method does the opposite, we don't start loading things in until we finally get to the element we put in. consider the following example code:

```dart
void main() {
  const numbers = [1, 3, -2, 0, 4, 5];

  var numbersUntilZero = numbers.takeWhile((number) => number != 0);
  print('Numbers until 0: $numbersUntilZero');

  var numbersStartingAtZero = numbers.skipWhile((number) => number != 0);
  print('Numbers starting at 0: $numbersStartingAtZero');
}
```

---
# Mapping function
The mapping function allows us to map items from one iterable  to another iterable with some given transformation.  For instance look at the following where we times ten each number:
```dart
Iterable<int> output = numbers.map((number) => number * 10);
```
We can also convert some integers to strings:
```dart
Iterable<String> output = numbers.map((number) => number.toString());
```
```dart
void main() {
  var numbersByTwo = const [1, -2, 3, 42].map((number) => number * 2);
  print('Numbers: $numbersByTwo');
}

```
