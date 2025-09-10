---
title: Flutter
tags:
draft: "False"
---
# Flutter
Flutter uses [[Dart]] so that we can develop Flutter apps very quickly and push them out to many platforms. Dart also has a reload feature that updates quickly, this is called "Hot Reload", meaning we do not need to continually recompile our code which makes testing a lot easier to work with. Flutter is an open source framework by Google that allows us to make very nice looking apps that are cross platform that run efficiently. All we need is a single codebase, which then gets compiled into machine code for the corresponding device being used to look at our application. 

* Why flutter? All we need is a single [[Dart]] codebase.
* We can take advantage of [[Material Design]] features, meaning we do not need to worry too much about how our app will look. 
* Layout principles are similar to [[CSS]]
* Flutter has a LOT of 3rd part packages that we can add to our program and is well documented 

In our web folder we need a folder because we have a web app. 

Pubspec Yaml is used for different libraries on flutter. We add different dependencies to our app here. This is because we do not have the dependencies installed, so we need to install of these.

To install these, all we need to do is use ```flutter pub get```, which will install our dependencies.

To run our app, all we need to do is to type ```flutter run```.


# Cura-Course Commands

The command, ```prima reset```, will reload our app and get to reload files. Prima is the service that does all the work here. 

```prima shutdown``` Saves the work and then it starts it back up

---
# Stateful/Stateless Widgets
what is the role of GIt?
what is the role of github?

Flutter - crossplatform apps 

---
# Callback Functions in Flutter
Callback functions are functions that are executed when a button is pressed. 

When we add const in front of a widget a lot of the work we would usually put in for resetting an application, so our code renders more efficiently. 

Flutter has a single navigator object manages what displays on the screen using a [[Stack]] to display what is there. The show welcome screen thus pushes the screen onto the stack. We can also pop items from navigator if needed. 

We have a setState() method which tells flutter that a widget needs to be updates on screen, which has the previous widget go away and render the next widget very quickly. 

Buttons in flutter are "disabled" if their onPressed is null or onLongPress are also null. 

