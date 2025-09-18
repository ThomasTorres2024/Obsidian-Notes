---
title: Time
---
Where do we get time on our systems? When we go on our system and check for the time, we query the hardware clock. Times in Unix are [[C]] strings and unsigned integers. [[C]] Strings are strings which end with a '0'. 

In memory, a C string with size 7, where the index at 7 under the hood is '\0'. The string $s$, is really a pointer to each character. The ascii encode is a 0 for a string. We could have a string of thousands of characters before we find the 0. 

We need to be mindful of the precision of our measurements for the clock. 

---
