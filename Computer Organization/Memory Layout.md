The canonical portion is always the same. The following is an __address that uniquely maps to a byte in RAM__. The program and the [[Operating System]] each have a different perspective of the memory and their own local address space, whereas globally the operating system maintains its own mapping. 

$$\begin{align}
\underbrace{\begin{bmatrix}
64 \text{ bits}
\end{bmatrix}}_{\text{"canonical"}} \underbrace{\begin{bmatrix}
48 \text{ bits}
\end{bmatrix}}_{\text{"tag"}} \underbrace{\begin{bmatrix}
10 \text{ bits}
\end{bmatrix}}_{\text{"set order"}} \underbrace{\begin{bmatrix}
6 \text{ bits}
\end{bmatrix}}_{\text{"offset"}}
\end{align}$$

We have in total $128$ bits for the whole portion. Every [[Byte]] in memory has a memory address, and depending upon the architecture in the modern day each byte has $64$ bit addresses. 

Let us assume we are operating under $2$ way set associativity, for some place in the cache 
