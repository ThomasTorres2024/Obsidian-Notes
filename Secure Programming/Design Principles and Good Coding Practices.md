---
title: Design Principles and Good Coding Practices
tags:
draft: "False"
---
# Design Principles and Good Coding Practices 

## Least Privilege 
The principle of least privilege is that access to assets should be limited to people and programs required to perform work. 

For this we have a couple of access control models which can be used:
* ACL - Access Control Lists 
* MAC - Mandatory Access Control, no user control
* DAC - Discretionary Access Control - user control
* Bell-LaPadula No read up, No write down, tranquility before change (?)
* Allow-List - Accepted, all other checks are bypassed
* Block-List Denied, regardless of other checks 

### Example -
For instance, SimpleWebServer allows access to all files on the drive. How is this preventable? 

This can be prevented by checking if the path is within the webroot, which has a corresponding function in particular languages. For instance in C++ we have ```realpath``` and in Java we have ```getCanonicalPath```. 

#### Why should the web server not be run as root?
Even a file with mode 000 can be read by root (no executes, no writes, no reads). If there is a vulnerability found which allows code to be executed, trojans can be installed on the machine. 

---
### Defense in Depth 

### Diversity of Defense 
Having multiple implementations of the same features is useful for verification. If we can have these features run concurrently we avoid single points of failure. 

Having multiple types of defenses in place leads to more patches and a greater chance that a malicious actor code find more code to exploit. 

### Architecture 
Our goal with architecture is to minimize the attack surface. For example, any place where the user would input information is a vector for attack and thereby reducing the total number of input sites we would decrease the number of attacks to our system. It makes auditing this code a lot easier. 

Another point of interest is in web development. Using a single point of entry is useful to help filter through web requests. 

Another crucial idea is to segment services. If we have several isolated critical services in several components, it makes it a lot harder to go on to attack other services. 

Lastly we also want to balance 3rd party libraries and in house code. Using 3rd party libraries means we do not always fully know what's going on and part of our security is outsourced to the provider. 

---
## Secure by Default 
Under this model we have "no default" and "derived passwords". By default some features are put to off. We also want to minimize the total amount of time spent in privileged code. 

Here we may want to deny running as admin if not needed or if it is dangerous. We want to be able to drop privileges from users if it is possible and when it is possible so that everyone is default again. Lastly, privileges are requested only when they are needed. 

---
## Secure by Design - Services 
Under this model, configuration is provided from outside of a container. Sensitive data is also provided from the outside. The OS file system is read only and is very minimal. Local dependencies get tested and shipped.

Persistent storage is done elsewhere. Design is to shutdown cleanly and to restart when previous run fails. Design restarts even when previous run failed. We also have stdout/stderr for logs. We are isolated from other services. 

Note well that the [[Kernel (OS)]] is still shared even between different services. 

---
## Convenience and Security 
Users tend to avoid difficult to use systems, and will also like to use easy passwords. If they need to use hard passwords they will need to write them down or use password managers. This is quite different from saying there is a trade off as much as that convenient does not mean easy to bypass necessarily. 

---
## Implementation Vulnerabilities
Even if a design is correct, bugs can still occur in the process of implementation. This is notoriously the case for [[Encryption]]. 

There is also the confusion of data and control. Consider the cases of [[SQL Injection]] and [[AI Prompts]]:

* User Input interpreted as commands
	* AKA "Command Injection"
	* Examples include [[SQL Injection]] and [[XSS Scripting]] (which is essentially the injection of malicious [[Javascript]] into [[HTML]] files)
* AI Prompts
	* [[Large Language Model]]s inherently are non deterministic 
	* They have non deterministic detection of "prompt vs thinking"/tool-use in the context window 
	