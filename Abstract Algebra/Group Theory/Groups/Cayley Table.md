---
title: Cayley Table
tags:
draft: "False"
---
# [[Cayley Table]] Definition
For a [[Group]] $G$, for every $x_1,x_2 \in G$, we represent every $x_1 \circ x_2$ in the Group in the following manner:

For instance, consider the group for the operations of rotations and reflections, on a square, we would thus generate the following table:

| $\circ$ | e   | r   | r²  | r³  | s   | sr  | sr² | sr³ |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| **e**   | e   | r   | r²  | r³  | s   | sr  | sr² | sr³ |
| **r**   | r   | r²  | r³  | e   | sr  | sr² | sr³ | s   |
| **r²**  | r²  | r³  | e   | r   | sr² | sr³ | s   | sr  |
| **r³**  | r³  | e   | r   | r²  | sr³ | s   | sr  | sr² |
| **s**   | s   | sr³ | sr² | sr  | e   | r³  | r²  | r   |
| **sr**  | sr  | s   | sr³ | sr² | r   | e   | r³  | r²  |
| **sr²** | sr² | sr  | s   | sr³ | r²  | r   | e   | r³  |
| **sr³** | sr³ | sr² | sr  | s   | r³  | r²  | r   | e   |


