---
title: Async
tags:
draft: "false"
---
# Asynchronous programming: futures, async, await 

What are asynchronous operations? Asynchronous operations let our program complete work while waiting for other operations to finish. If we are getting some data from the network, writing to database, or reading data from a file, we likely do not want to wait for these external operations to finish, and we can do something else while waiting in the mean time.

Asynchronous computations return [[Future]] objects or sometimes [[Stream]] if our program is in multiple parts. We use async and await keywords to access these functions. 

The following is an errant example of async functions.
```dart
// This example shows how *not* to write asynchronous Dart code.

String createOrderMessage() {
  var order = fetchUserOrder();
  return 'Your order is: $order';
}

Future<String> fetchUserOrder() =>
    // Imagine that this function is more complex and slow.
    Future.delayed(const Duration(seconds: 2), () => 'Large Latte');

void main() {
  print(createOrderMessage());
}
```
If we look here, we see that we return a future string object without awaiting it, and this is bad, we never actually properly await the function and its output.

A synchronous operations blocks other operations from running until its execution is complete. A synchronous function only performs synchronous operations. 

An asynchronous operation allows other operations to execute before a task completes. An asynchronous function has at least one asynchronous operation, and also can perform synchronous operations. 

---
# What is a future?
Futures in dart are initialized instances of the future class. A future is an asynchronous function, which has two states, uncompleted, or completed. 

Uncompleted is the dart term that refers to a future which has yet to produce a value. If our future operation completes, we get a value, otherwise we end up getting an error.

If the future function fails, it completes with an error. 

Review of Future -
* Future(T) produces a value of type T
* if no such value is there then we have Future(void)
* Future can be either uncompleted or completed 

---
# Async and Await 
Async and Await gives us ways to define asynch functions and use their results. To define an async function just add async before the function body:
```dart
void main() async { ··· }
```

If the function has a return type, then make sure to set it to ```Future<T>```

We can await tasks within an aync function:

```dart
print(await createOrderMessage());
```

More example async code:
```dart
Future<void> printOrderMessage() async {
  print('Awaiting user order...');
  var order = await fetchUserOrder();
  print('Your order is: $order');
}

Future<String> fetchUserOrder() {
  // Imagine that this function is more complex and slow.
  return Future.delayed(const Duration(seconds: 4), () => 'Large Latte');
}

void main() async {
  countSeconds(4);
  await printOrderMessage();
}

```
We synchronously count awaiting the order, and when it's up we get our order back.