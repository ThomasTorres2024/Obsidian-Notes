---
tiel: Security Principles
tags:
  - Secure_Programmiing
draft: "False"
---
### Authentication
Authentication is proof of identity, and is implemented by recieving input that consists of either something someone __knows__, __has__, or __is__, for example: 

* know (user name, password, questions)
* have (key, smart card, tokens, phones)
* are (biometrics like a finger print)

### Authorization 
Authorization is authority to perform some kind of action. For instance on windows some users need access to perform some actions if they are not admins and need to enter in admin credentials to do so. 

* __ACL__ - Access Control Lists 
* __MAC__ - Mandatory Access Control - no uuser control
* __DAC__ Discretionary Access Control - user control 
* __Bell-LaPaduula__ - No read up; No Write down; tranquillity 
* __Allowlist__ - Accepted, all other checks are bypassed 
* __Blocklist__ - Denied, regardless of other checks 

### Confidentiality 
Confidentality is access to data that is restricted only to authorized uusers. Implementations of this in practice consisit of:

- __Encryption__
	* Reversible scrambling functions (we can recover original message, ROT13, RSA)
	* Keys need to be stored
	* Access to these keys has to be protected as well
	
- __Data Retention__
	- Only keeps data for a specific task and as long as necesary to makke some requirements 
	- Keep data somewhere in the 'least accessible possible place', hard to access 

### Data/Message Integrity 

Ensuring that a message isn't tampered with or replaced. Note that __this does not prevent a message from being read by anyone__. Some implementations of this consist of crytographic hash functions like MD or SHA. 

Both of these make messages contain a short value computed from the message. We also have message authentication codes, signed hashes that provide authenticity of the person that signed it. 

The hashes are used to identify the sender. 

### Accountability
Association of action with some individual, whiich allows credit or blame to be assigned to a person as needed. 

This can be implemented by logging, which produuces a file of all of the actions taken by every actor. 

### Availability 
Service that is available to all authorized users at some expected quality of service. 

Implementation of availability consists of the following: 
* Coding/Engineering
	 -  Resource management, increase resources or optimize them 
* Fault tolerance 
	* Safe statre after recovery 
* Redundancy 
	*  Security components that are replicated in multiple places to stop a single choke point from messing up an appliciation

### Non-Repudiation
Undeniable proof of a transaction. 

Implementations
* Escrow - Third party that mediates part of all off the transaction
* There is no standard complete protocol 
* Independent party may need to verify that transaction occured 
* Evidence of Transaction :
	* Identities 
	* Transaction Details
	* Trusted Timestamps
	* Digital Signatures
	* Tamper-proof records 