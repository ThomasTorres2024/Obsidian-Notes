---
title: Authorization
tags:
  - Secure_Programmiing
draft: "False"
---
# Policy Definition

- System Type
- Rules
- Changes 

### Policy Administration 
* System of changing policy definition 

### Policy Enforcement 
* System applies defined rules to actions 
---
# Authorization Model, Basic Terms

- Subject - A user or service in the system 
- Object - An entity that contains or recieves information 
- Operation - Some action initiated by a subject 
- Permission - Association of (Subject, Object, Operation)
- Access Control List - A list of permissions associated with an Object containing the operations allows or denied by a Subject 
- Attribute -  Some systems allow extra attributes to be assigned to Subjects or Objects 

The system checks if a Subject has permission to perform an object by iterating the access control list. 

### Extended Terms 

* Separation of Duty - Prevent Misuse by breaking responsibility for a task into at least two pieces 
* Domain - Group of processes to which a set of permissions apply 
* Owner - Subject that is responsible for an Object 
* Role - Collection of permissions requiried for a defined task 

---
# Access Control Models 

### Discreationary Access Control (DAC)
* Object owner has __some__ control over permissions
* Benefits: less administrative overhead
* Issues: Transitive read access, potential policy violations 

### Mandatory Access Control
* System enforces security policy, owners do not dictate permission
* Use cases: Governmentand military systems (Bell-La Padula model)


---

# Role-Based Access Control 

- Subjects assigned Role(s)
- Objects Operations associated with provided Role
- Roles can be nested to create hierarchies
	- Separation of Duty: requires multiple roots 
* Benefit - Simplifies Administrative Management 
* Challenge - Role design complexity, role overlap issues, separation of duties 

---
# Authorization Model Decision Framework 

Every model has scenarios where they tend to have issues and do not perform well. We thus need to select models based on both strengths and limitations to meet application needs. 

---
# Context Constraints

* Time or Event Based Policy 
	* Workers only have access during their shift 
	* Workflow determines access 
* Device Type
	* Does the device meet security requirements?
* IP Address 
* Location
	* Are additional challenges necessary because of a new location 

---
# Authorization of Implementation

There are several algorithms for determining access:

* [[Unix]] Model:
	* Owner
	* Named User
	* Owner's Group
	* Named Group
	* Other
	* Deny

* Fixed: Policy to either accept or deny, where we have a list of exceptions
* Sorted Order: First Match (???), this could be difficult to maintain properly 
* Inherited Permissions - Walk Hierarchy ([[Tree]]) (Users that have some role will inherit the permissions of anything less than that on the hierarchy). 

### Auditing
* Easy to audit: What subjects have access to this objects?
* Hard to audit:  What access does Subject have to all Objects?

---
# Capability Lists 
* Permissions associated with subjects, not objects (bit of an inverse of the situation with ACL)

### Auditing 
* Easy to audit: What access does Subject have to all Objects?""
* Hard to audit: What subjects have access to this object? 

---
# Role-Based Access Control

* Role is a semantic construct which policy is formulated
	* Roles assigned to subjects and operations associated with roles
	* Simplifies administration by managing permissions at role-level
	* These properties usually make the scheme more comprehensible 

* Hierarchical RBAC - Partial Ordering of Roles 
	* Difficulties 
		* Designing appropriate roles
		* A large number of roles is hard to main and may need more levels 
		* Making exceptions may not be possible (this may be considered a positive)
		* Granularity of Permissions 
		* Overlap of Roles could erase separation of duties 

* Rule Based Access Control
	* Allows a system based on properties other than identity of Subjects and Objects 
	* Might test attributes of Object or Subject
	* Might test environmental constraints
	* Benefit - Flexible System
	* Issue - Difficult to test 
---

# Impersonation
- Allows a person to become another person on the system
- Full - Gains full privileges of that subject 
- Limited - Can perform some set of operations
- Should be Audited

---
# Separation of Duty
- System checks for conflicting roles 
- System requires two distinct subjects of the same Role, or system requires two subjects of different Roles 
	- 