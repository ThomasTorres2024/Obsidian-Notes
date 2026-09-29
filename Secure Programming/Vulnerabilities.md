### Definition
A __vulernability__ is a weakness in the system. An __attack__ is an exploit of a vulnerability. A __threat__ is a potential of an attack. 

Some vulnerability types occur a lot more than do others, some examples of this consist of MITRE, OWASP, and NIST.

### STRIDE Threat Model
Spoofing - Thread action aimed at accessing and use of another user's credentials such as username and password. The control for this factor is Authnetication. 

Tampering - Threat action intending to maliciously change or modify persistent data

---
# Mitigation
### Threat Analysis
Most important aspect is the data, what data do I have that needs to be protected, we have classes of data, like usernames, passwords (sometimes users are also sensitive for some sensitive applications).

We are interested in a data flow diagram, how does data flow through the system, what are the entry and exist points. Where are the trusy boundaries 

Threat agents, who could attack the system internally and externally? Many times there can be threats from within the organization as well. Not everyone on the inside needs such access, this can break the security model. Need to ensure least privilged users cannot gain higher level of access 

Scenarios - What kinds of vulnerabilities and weaknesses could expose assets to untrusted agents? For example things like on Word, like adding images or a scripting language. If the image contains malicious code this allows for remote code execution. 

Assess systems - What mitigations are in place to protect against these scenarios?

Assess risk - What is the impact of any unmitigated risk? Nowadays we generally care a lot about any incursions and won't brush these things are aside, maybe low probability hacks we ignore too. 

Documentation - Things we tell end users, how to configure their system to make it secure, not using a default password as well 

## Security in Software Requirements 
- Validations
	-  Can each input be validated, for instance emails, phone numbers credit cards. put restrictions on usernames as well. Harder to enforce this in the context of forums
* Error Handling
	- Is the error internal or external, like compilation in code vs run time error. A run time error would be say trying to open a file that does not exist. 
	- Handling all different error values. Examine all the types of errors that can be produced. Need to catch all different exception types in Java. 
- Authorization and Data Protection
	- Identify types of data that needs to be protected
	- What assets and commands require levels of authorization, create some kind of access model that allows particular users to access some 
	- Data requires protection, determine what data needs this and what data doesn't. What set of protection does a particular bit of data require?
* OWASP and other sources provide checklists for different applications on the kinds of things that need to be checked 
* Insecurity by Obscurity
	* If something unknown is supposed to make it unknown, this isn't security. For instance, if we send out a weblink from some server, it has to pass through multiple servers, lots of different things along the way that could see or obtain the server, potentially items on the PC,

### Input Validation Example
```java
public static final double price = 20.00;
int quantity = currentUser.getAttribute("quantity");

// import to verify above is true 
// interestingly in java there's no unsigned int 
// should also check the total number of things that are being requested 

double total = price*quantity;
chargeUser(total);


```

```C

char sNumber[10];
sprintf(sNumber, "%d",a);

//creates buffer of 10 chars, and tries to print it
//say we have a ="2000000000", then we do not have enough room for the nul terminator, \0
//also it will NOT include the negative sign either in -200,000,000

```

Member Buffer handling

```rust

fn main(){

	use std::fmt::Write;
	let mut buf = [0u8;10];
	let mut s = String::new();
	
	write!(&mut s, "")

}

```

Crashes because this can happen exceeds buffer but no vulnerability 

##### Use After Free
```C

char *buf = malloc(10);
strcpy(buf,"test");
free(buf);

//uses after free 
//undefined behavior, if something happened else in the memory after this, we get a different value coming out
printf("%s\n",buf);

```

##### Integer Overflow
```C

unsigned int size = 429497295; // max 32 bit
unsigned int total = size + 1; //wraps to 0
buffer = realloc(buffer,total);

// 
//note this happens on a 32 bit system, maybe possible on 64 
//instead of allocating something we allocate nothing since the amount here was wrapped to 0 
//also we get a memory leak, we lose pointer the original memory area 

```

##### Authentication Example
```perl

my $q = new CGI; 

if ($q->cookie('loggedin) ne "true"){

}

```

* First checks if the user is logged in. Otherwise authenticate user with what they set as their username and password and exit.
* Cookies are a user controlled value, this is a terrible idea, a user could just spoof themselves as being the admin if they wanted to 

##### Infinite Loop
```C

int processMessageFromServer(char *addr, int port){
	
	do{
		
		connected = connect(servsock, (struct sock addr *)&servaddr,
		sizeof(servaddr));
		
		//get negative back on failure. only continue if
		//connection worked 
		if(connected > -1){
		
		}
	  
      	
	} while (connected < 0);
	//idea is to continue execution here until we connect
	
}

```
* This code fails since it assume we can connect, it needs the server to respond 

### Path Traversal 
```perl

my $dataPath = "/users/cwe/profiles";
my $username = param("user");
```

* If a user specifies a name with "../" or something of that nature, then the user might be able to print contents of some file out that they were not meant to see 
* Server should restrict access to sensitive files 

##### Unrestricted File Upload


```php

move_uploaded_file($_FILES['file']['tmp_name'], "/var/www/uploads" . $_FILES['file]['name']);

```
- Uploaded files could contain malicious content, like javascript which could be dangerous to a site 

---
# HTTP Server Analysis

HTTP is a simple text protocol. We expect first that the client sends, like post, get delete, etc. 

Any two applications has 2 portions, a server and a client side. On the server:

##### Server:
* Create socket, usually on some specific port
* Listen/accepts connection
* Process connection
* Close 

##### Client:
* Create socket to a specific ip port, we need the other endpoint, need the hostname do a lookup get its IP and then some specific port
* Connect
* Process Connection
* Close 

Question on the hw about the behavior of the code, 