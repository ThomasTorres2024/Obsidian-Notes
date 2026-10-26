---
title: Multihead Attention
tags:
  - Machine_Learning
  - LLMs
draft: "False"
---
# Multihead Attention

We want to build a [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]] which uses [[Attention (Transformers)]] across multiple heads. 

Let us construct a [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]] with the following architecture. Assuming the following, we have a dictionary size of $50,000$, an embedding size of $d=512$, and $L=1024$ is our __sequence length__ (number of words the model can process at one time). 

We want to begin by converting each word to a number through the process of [[One Hot Encoding]], "hello" $\to$ gets converted to some vector $x$ in $1 \times 50,000$. We then take an embedding matrix, $W \in \mathbb{R}^{50,000 \times 512}$. 

Then by doing $xW$ we get a representation in $\mathbb{R}^{1 \times 512}$. Let us assume we have a sentence with 1024 words. Then, this gives that our resulting representation matrix will be of size $\mathbb{R}^{1024 \times 512}$.

So far we have previously seen an architecture with a single attention head. Under this model we have the following: 

---
## Simplified (Singleheaded Attention) Algorithm

Let us recount the simplified singlehead attention on a single layer:

1. Start with $X \in \mathbb{R}^{1024 \times 512}$
2. Obtain $Q$ via $Q=X \cdot W_{Q} : W_{Q} \in \mathbb{R}^{512 \times 512}$ 
3. Obtain $K$ via $K=X \cdot W_{K} : W_{K} \in \mathbb{R}^{512 \times 512}$ 
4. Obtain $V$ via $V=X \cdot W_{V} : W_{V} \in \mathbb{R}^{512 \times 512}$

(Note that $Q,K,V \in \mathbb{R}^{1024 \times 512}$)

5.  $A= Q \times K^T \in \mathbb{R}^{1024 \times 1024}$
6. $\text{out}=A \cdot V \in \mathbb{R}^{1024 \times 512}$
7. Keep computing this through each layer.  

---
# Introduction to Multiheaded Transformers 

Let us assume that we want $8$ heads. We have $512$ features in total. One of the reasons we are interested in doing this is to __increase total model complexity__. By adding more layers we can also increase the complexity, but these computations cannot be done in parallel whereas the __heads and partitioning of the matrices can be done in parallel__ quite easily since every head is independent from one another in terms of computation.

When we do multiheaded computation, each head gets its own set of features to work with and do computations on. For instance the first $Q^{(1)}$ goes off of the first $64$ features, $Q^{(2)}$ $65 \to 128$, $Q^{(8)}$ on the last $64$. Practically all of this is stored as a single Matrix. 

In the multiheaded attention style we for sure get more parameters at the end through $W_{0}$ thast would have not ocurred before hand. 

We can choose to work only on the first $64$ features instead, since each head now works on $64$ features. Now that the data is split up into $8 \times 8$ chunks, we can do normal $Q,K,V$ operations on them but with smaller chunks.

Through this model, we will have that $W_{K}^{(1)},W_{Q}^{(1)},W_{V}^{(1)} \in \mathbb{R}^{64 \times 64}$. We will also have a new set of $Q^{(1)},K^{(1)},V^{(1)}$ which will be in $\mathbb{R}^{1024 \times 64}$ together:

$$\begin{align}
X^{(1)} \in \mathbb{R}^{1024 \times 64 } \longrightarrow \begin{cases}
 Q^{(1)}=X^{(1)}W_{Q}^{(1)} \\
 K^{(1)}=X^{(1)}W_{K}^{(1)} \\
 V^{(1)}=X^{(1)}W_{V}^{(1)} 
\end{cases} \longrightarrow A^{(1)}=Q \cdot (K^{(1)})^T \quad \longrightarrow \text{out}^{(1)}=A^{(1)}V^{(1)} \in 1024 \times 64 \\
 \vdots \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad   \quad \quad \quad \quad \quad \quad \quad \quad  \quad \quad   \vdots \quad \quad  \quad \quad  \quad \quad  \quad \quad \quad \quad \quad \quad \quad \quad  \quad \quad  \quad \quad \quad \quad   \vdots \\

X^{(8)} \in \mathbb{R}^{1024 \times 64 } \longrightarrow \begin{cases}
 Q^{(8)}=X^{(1)}W_{Q}^{(8)} \\
 K^{(8)}=X^{(1)}W_{K}^{(8)} \\
 V^{(8)}=X^{(1)}W_{V}^{(8)} 
\end{cases} \longrightarrow A^{(2)}=Q \cdot (K^{(8)})^T \quad \longrightarrow \text{out}^{(8)}=A^{(8)}V^{(8)} \in 1024 \times 64
\end{align} $$

We have a corresponding set of weight, attention, out and $Q,K,V$ type matrices for each layer. They all have the same dimensions for each head. 

Once we have computed the respective outputs from each layer, we then take them and compress them into a single matrix at the end of size $\mathbb{R}^{1024 \times 512}$, which is the size of out originally in the singleheaded transformer. Note that $W_{0} \in 512 \times 512$, another learnable matrix at the very end. This is where we get out real output

$$\text{out }_{1024 \times 512} = \begin{bmatrix}
\text{out}^{(1)} \\
\text{out}^{(2)} \\
\text{out}^{(3)} \\
\text{out}^{(4)} \\
\vdots \\
\text{out}^{(8)}
\end{bmatrix}_{1024 \times 512} \cdot W_{0} $$


Everything that we have which is learnable so far consists of all of the different $Q,K,V$ type matrices, the embedding matrix is also learnable, and the $W_{0}$ matrix is too.  

We want to slice column wise for our words, otherwise they would be only going row by row and we would still have to deal with the issue of __words being processed independently__ where we lose context inbetween each word. So we must split column wise. 

---
# Multiheaded Attention Practically

In practice we do not need separate head matrix multiplications for $Q,K,V$. Instead, we stack the head weight natrices together, so $W_{Q}$ is a combination of all of the $W_{Q}$ head matrices:

$$W_{Q}= \begin{bmatrix}
W_{Q}^{(1)} & W_{Q}^{(2)} & \dots &  W_{Q}^{(H)}
\end{bmatrix}_{d \times hd_{k}} : d_{k} = \frac{d}{h} $$

$$ \begin{align}
Q = X W_{Q} = \begin{bmatrix}
\dots \text{word}_{1} \dots \\
\dots \text{word}_{2} \dots \\  
\vdots \\
\vdots \\
\dots \text{word}_{n} \dots
\end{bmatrix}
\end{align} \cdot \begin{bmatrix} \\

\text{weight matrix}  \\
 \\

\end{bmatrix} =\begin{bmatrix}
\dots \text{Q embedding word}_{1} \dots \\
\dots \text{Q embedding word}_{2} \dots \\ \\
\vdots \\  
\dots \text{Q embedding word}_{n} \dots
\end{bmatrix}

$$

From this we can obtain the $Q$ head matrices, $Q_{1},Q_{2},\dots Q_{n}$ by splitting them up by the features per head count:

$$Q^{(1)} = \begin{bmatrix}
\dots \text{first } d_{k}  \text{ Q embedding word}_{2}  \dots \\
\dots \text{first } d_{k}  \text{ Q embedding word}_{2}  \dots \\
\vdots \\  
\dots \text{first } d_{k}  \text{ Q embedding word}_{2}  \dots \\
\end{bmatrix} \quad \dots \quad Q^{(8)} = \begin{bmatrix}
\dots \text{last } d_{k}  \text{ Q embedding word}_{2}  \dots \\
\dots \text{last } d_{k}  \text{ Q embedding word}_{2}  \dots \\
\vdots \\  
\dots \text{last } d_{k}  \text{ Q embedding word}_{2}  \dots \\
\end{bmatrix}  $$

Conceptually, the heads each operate on their own respective features and do their own computation and output. Then, their values are passed out through the layer. It turns out that this concptually is the exact same thing as doing the overall $X\cdot W_{Q}$ multiplication (just a giant product) in practice. 

Once we have our $Q$, we need to use the __individiual parts of $Q$ for future computations.__  We will proceed with each head computation after obtaining $K_{1},\dots K_{8}$ and $V_{1},\dots,V_{8}$. 

In the original paper, we only work on the different features _after_ we have our $Q,K,V$. Some vision transformers split on the datamatrix we receive as input $X$, though this is not standard. 