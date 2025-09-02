---
tit;e: Random Variables
tags: 
draft: "false"
---
# Sample Space

We can obtain information about a distribution by performing "$\textbf{random experiments}$", which are simply actions to get information about a distribution. From each random experiment, we get an "$\textbf{outcome}$".

The set of all outcomes we can call the "$\textbf{sample space}$", which we denote by $\Omega$. Each outcome is the smallest unit of the sample space. We call a collection of outcomes an "$\textbf{event}$". 

For example, a common introductory example in probability is a tetrahedral die, where rolling any particular side has an equal probability of being rolled. The die has four sides, each of which have a $\frac{1}{4}$ chance of being rolled. 

Our sample space would consist of all of the possible faces that the die could land on, so this would encompass:

$$\Omega =\{1,2,3,4 \}$$
Each face that the die could land on is denoted by a number. We could arbitrarily group some subset of elements from $\Omega$ into a new set, and we could call this an event, since it is simply a collection of outcomes. 

For instance, consider the subset, $\{1,2 \}$.

More examples of sample spaces and events include:
* The sample space for the outcomes of a pull would consist of $\Omega =\{Y,N \}$, indicating yes or no on a ballot.
* The genotypes of alleles from a randomly chosen collection of plants, $\Omega = \{PY,PG,WY,WG\}$
* Rolling two six sided die and considering their sum, $\Omega= \{1,2,3,4,5,6,7,8,9,10,11,12\}$
* The outcomes of rolling two die as a 2 tuple: $$ \Omega = \left\{
\begin{array}{cccccc}
(1,1) & (1,2) & (1,3) & (1,4) & (1,5) & (1,6) \\
(2,1) & (2,2) & (2,3) & (2,4) & (2,5) & (2,6) \\
(3,1) & (3,2) & (3,3) & (3,4) & (3,5) & (3,6) \\
(4,1) & (4,2) & (4,3) & (4,4) & (4,5) & (4,6) \\
(5,1) & (5,2) & (5,3) & (5,4) & (5,5) & (5,6) \\
(6,1) & (6,2) & (6,3) & (6,4) & (6,5) & (6,6) \\
\end{array}
\right\}.$$
* The event of rolling doubles, $A = \{(1,1),(2,2),(3,3),(4,4),(5,5),(6,6) \}$
* The event of rolling evens $E=\{2,4,6 \}$, the event of rolling odds $O = \{1,3,5 \}$
---
# Set Theory Notation and Sample Spaces

We can treat sample spaces and sets interchangeably. Any time we would use set notation on events of sets. For instance, $A \subseteq B$ would be equivalent to saying that the event $A$ is a subset of the event $B$. 

Here is some of the set notation that we use in probability for any two events $A,B$  where $A \subseteq \Omega, B \subseteq \Omega$:
* $A \cup B$, the union of events $A$ and $B$ occurring 
* $A \cap B$ the intersection of two events occurring
* $A^c$ the complement of $A$, all events not contained in $A$ in the sample space
* $\varnothing$, the empty set, which contains no elements 

Two events are said to be $\textbf{disjoint}$ or $\textbf{mutually exclusive}$ if they have an empty intersection: 

$$A \cap B = \varnothing \Longleftrightarrow A\text{ and } B \text{ mutually exclusive }$$
We also have some basic rules involving these operations that come from set theory. These are fairly self explanatory: 

$$A \cup \varnothing =A$$
$$A \cap \varnothing =A$$

We denote events by capital letters generally. 

---
# Probability Functions

For finite cases, a probability function, $\mathcal{F} : \Omega  \rightarrow [0,1]$, which maps outcomes from the sample space to $[0,1]$. 

An example of such a function can be applied to the sample space for a die given by $\Omega = \{1,2,3,4,5,6 \}$ which evenly maps each probability to $\dfrac{1}{6}$. 

This is an example of an "equally probable" space. We can also have probabilities that are not uniform. Overall, we are assigning probabilities to each outcome in the sample space such that each probability itself is non-zero and that the sum of their probabilities is 1. These rules are crucial for creating probability functions. 

For events in $A \subseteq \Omega$ we can determine the probability of the event by summing the probabilities of the outcomes in $A$:

$$\mathbb{P}[A]=\sum_{a \in A}\mathbb{P}[a]$$
---
# Infinite Sample Spaces 

In probability and statistics we often encounter infinite sample spaces. Infinite sample spaces have a sample which contains an infinite amount of outcomes. From this, we have to cases where $\Omega$ is countably infinite and uncountably infinite. 

1. In the case that our sample space is countably infinite, it follows that we can assign a probability to each value since there is a bijection between this set and the natural numbers, and we can thus take a sum over it. This constitutes a discrete probability function in tandem with the sample space being a finite size. 

2. If the sample space is uncountably infinite, we cannot assign its probabilities manually through a probability function, and instead we have a probability density function which is not finite. 

---
# Probability Functions Axioms

Every probability function satisfies the following axioms. These axioms are intuitive. The range of a probability function is $[0,1]$ with a domain of the sample space $\Omega$. 

1. Any event $A \subseteq \Omega$, $\mathbb[P](A) \geq 0$
2. $\mathbb{P}[\Omega]=1$
3. For the sequence of disjoint events, $A_{1},A_{2},\cdots,$ then their probability is given by: $$P \left( \bigcup_{i=1}^\infty A_{i}\right) = \sum_{i=1}^\infty \mathbb{P}(A_{i})$$
Any function that satisfies these 3 axioms is a probability function. With these three axioms we can go on to prove further rules for our probability function: 

4. $\mathbb{P}(\varnothing)=0$
5. For the disjoint events, $A_{1},\cdots,A_{n}$ in $\Omega$ then $$\mathbb{P} \left(\bigcup_{i=1}^nA_{i} \right)=\sum_{i=1}^n\mathbb{P}(A_{i})$$
6. $\mathbb{P}(A^c)=1-\mathbb{P}(A)$
7. If $A \subseteq B,$ then $\mathbb{P}(A)  \leq \mathbb{P}(B)$
8. $\mathbb{P}(A \cup B)$ = $\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A \cap B)$

These rules can be formally proved using our three axioms and the other further results. We also have DeMorgan's laws which apply to our sets: 

$$(A \cup B)^c = A^c \cap B^c \text{ and } (A \cap B)^c = A^c \cup B ^c$$
We also have distributive laws: 
$$A\cap(B \cup C)=(A \cap B) \cup (A \cap C) \text{ and } A\cup(B \cap C)=(A \cup B) \cap (A \cup C)$$ 