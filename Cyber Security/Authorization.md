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
	- Purchaser cannot authorize a purchase greater than some amount
	- Authorizer cannot be the purchaser 

---
# Designing an Authorization System

- First Set of Questions:
	- What are the subjects, operations, objects
	- What policies need to be implemented
	- How is the policy defined
	- How is the policy redefined 
	- Is delegation required 

* Which system can implement tje Policy?
	* Where is the Policy defined?
	* Where is the Policy Enforced?
	* How is the Policy enforced?


### Evaluating an Authorization System
* Steps required to reconfigure 
* Support of least privilege 
* Support of separation of duty
* Number of relationships to create a policy
* Adaptability to change 
* Interoperability 
* Testability
* Performance
* Detection of conflicts 

---

# Authorization Logging
* Why log Authorization Activity?
	* Compliance
		* Regularatory requirements like HIPAA, GDPR, SOC 2
	* Security Investigation
		* Detect and investigate breaches
	* Accountability
		* Track who did what and when
	* Anomaly Detection, Identity suspicious patterns
	* Audit Trail: Prove system behavior for disputes

### Authorization vs Authentication Logging
* Authentication: Who are you
* Authorization: What can you do (access grants denials operations)
* Both are needed, but we give them separate log streams 

#### Essential Authorization Log Fields:
* Timestamp: [[ISO 8601 format]], [[UTC Timezone]], millisecond precision
* User/Subject: UID, Username, ServiceAccount Name
* Action: Specific Operation attempt, read write deletre publish
* Resource: Object Identifier, type, and sensitive classification
* Decision: ALLOW or DENY
* Reason: Why access was denied

### Context Information:
* Source IP address and geolocation
* Device/Client identifier
* Session Id or request Correlation ID
* Role(s) activate time of request 
* Environment (dev/staging/prod)

---
# Where to store Authorization Logs?

- Application Logs: local but vulnerable to tampering
- Centralized logging: ELK stack, splunk, clouudwatch
- Dedicate Audit Database: Immutable, append only tables 
- Log Aggregation Service: Cloud provider (AWS Cloud Trail, Azure Monitor)


### Log protection Requirements:
* Immutability: Logs cannot be modified or deleted by users 
* Integrity: Detect tampering, checksums, digital signatures
* Retention: Follow compliance requirements often 1-7 years 
* Access Control: Restric who can read logs (auditors compliance)
* Encryption: Protect logs in transit and at rest
* Resiliency: Multiple copies of logs to prevent loss; ideally in separate physical locations 

### Where in the Code to Log? 
* Before Check: Log the authorization request
* After Decision: Log the agllow/deny decision
* On Enforcement: Log when policy is actually applied
* On Violation: Log suspicious or dangerous access patterns

### Logging Info:
* INFO: Successful authorization checks
* WARN: Denied access attempts, policy near limits
* ERROR: Authorization system failures, miscofngiruation
* CRITICAL: Separation of duty violations, privilege escalation attempts 

### Trade-offs:
- Logging everything, audit completeness but high storage and performance 
- Logging selectively performance gain but potential compliance gaps 

---
# Sensitive Data Handling 
- What not to Log:
	- Passwords, API keys, tokens, secrets
	- Personal identifying information
	- Payment card data, SSNs
	- Medical or health information
	- Content of the resource being accessed 

* Logging Resources Access Safely:
	* Log resource ID, not resource content 
	* Example: Log User accessed Patient Record 12345, not details

* Handling PII in logs
	* React or hash identifiers in non sensitive logs
	* Separate audit logs from application logs
	* Encrypt logs containing PII
	* Apply least privilege to log access 