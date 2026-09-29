---
title: Security Implementation
tags:
  - Secure_Programmiing
draft: "False"
---
# Security Implementation
We want to determine if the cost of implementing some security feature is worthwhile. We can examine the cost $C$ and the benefit $B$ off performing some security changes. Given some event $E$ that could occur, 

$$\text{Loss}=\mathbb{P}(E) \text{Loss}(E)-\text{Cost}(\text{Protection})$$
$$\text{CostEffectiveness}=\frac{\text{Cost}_{new}-\text{Cost}_{old}}{\text{Benefit}_{n ew}-\text{Benefit}_{old}}$$
We also have to consider an initial cost and a recurring cost. If we also audit during the design process we can save a significant amount, 60x, by cost of patching. 

### Where is Security needed?
Security has to be applied at every single level. At the levels of:
* Physical Hardware
* [[Firmware]]
* [[Operating System]]s/[[Networks]]
* [[Software]]/Applications

At every level we need to be able to ask, who has access to these resources, what can they do with their levels of access, what are the security requirements at each level, and what assuumptions can be made about the other layers. 
### When is security needed?

* Requirements - Necessary security 
* Design - How should the security requirements be implemented 
* Coding - Implementing and testing 
* Building - Secure development environment, supply chain, code signing 
* Deployment - Checksuums, signatures, permissions, and setup
* Maintenance - Doing all of the above again for updates 

### What tools do we have?
Each layer has security controls that the next layer builds upon. 
* Hardware provides protection rings and trusted key storage 
* Operating systrems provide [[Process (OS)]] isolation, [[File System]] access controls 
* Application developers have role based security in their appliciation
* IT assigns roles to different users 
* End users set passwords weak permisisions and share information 

### What procedures can be used to implement security?

When designing software and systems:
* Define system users and their responsibilities
* Enumerate data storage locations and their requirements 
* Defiine auditing requirements
* Define performance requirements
* Define reliability requirements

When writing software:
* Be familiar with language specific issues 
* Use "static analysis" where possible
* Create testing plan for significant use cases
* Ensure design requirements are still met 

When testing software:
* Use [[Unit Tests]] for validation 
* Use regression tests (tests that re run functional and non fuunction tests that ensure that code still works after a change update or bug fix) for known issues 
* Use coverage tests to ensure proper execution (amouunt of code used during execution)
* Use integration testing to check external interfaces 
* Use performance tests based on expected usage (speed and execution of a test)

