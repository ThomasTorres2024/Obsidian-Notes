---
title: Parameters
tags:
  - Fundamentals_Prog_Langs
draft: "False"
---
# Parameters 
Parameters are another type of variable in addition to the global/static, function/local variables, and dynamic heap allocated variables. Parameters are passed into functions. 

A function's header and body is its definition, whereas its duties are the function body. The parameters in the header of a function definition are known as the __Formal Parameters__ and in the corresponding function call, the values passed in are the __Actual Parameters__. 

This leads to the following questions. How is the correspondence between actual and formal parameters established, and how is the value of an actual parameter transmitted to a formal parameter. 


---
# Correspondence 
One way is by assigning each variable in positional order, so the first formal parameter's value is equivalent to the value of the first actual parameter, the second is equivalent to the second, and so on. 

Some languages such as Ada have keyword parameters, which allow us to assign variables by using the name of the formal parameter and setting it equal to some actual value. 

---
# Parameter Value Transmission 

#### By Value
On top of this there are two different techniques, by using value and reference. This essentially copies the value of the variable passed in. This is also called "copy-in" and is very common. It is the only method in Java. 

#### By Reference 
For passing parameters by reference, the formal parameter is an alias/reference to the value passed in. We do not copy value and use the original which is initialized else where. It is still frequently used in C++.




