---
title: Transformer
tags:
  - LLMs
  - Machine_Learning
draft: "False"
---
# Transformer

Transformers are optimal large language models that beat out [[FFN]]s which are difficult to optimize and have a lot of memory overhead. Secondly, CNNs have a much lower receptive field, which is necessary for textual analysis. 

---

A transformer is a type of model where we want a __receptive field__ (amount of information covered), which covers the entire document. For instance in [[Convolutional Neural Networks]], if something looks like an eye or nose, we are likely looking at a face, but for a transformer we need a more global sort of view. 

Let us consider the example sentence, "hello how are you". Let us perform a one hot encoding on each vector for a set of $512$ words, which gives vectors of the forms $512 \times 1$ (row vectors). 

We still want to involve the processes of a CNN in this particular model. Let's take a look at our data, we would get a matrix of size $5 \times 512$, and then our $3\times 3$ kernel and begin the [[Convolution]] process 

$$\begin{bmatrix}
\dots \text{ hello }\dots \\
 \dots \text{ there } \dots \\
\vdots \\
\dots \text{ you} \dots
\end{bmatrix}$$
We would only cover the first three words and the first three features associated with each word. This particular kernel size would not be very effective. If we wanted to cover the first three words and all of their respective features, we would use a kernel of the size $3 \times 512$, which covers the first $3$ words entirely, but not every word in the sentence. Recall that the process of [[Convolution]] here we are thinking of as a __similarity metric__, wherever we convolve it over and the corresponding output values are the highest, we would have the highest values. 

Another similarity measure that we could make use of is the [[Inner Product]]/[[Dot Product]]. If we wanted to measure the similarity of words in a sentence, we could do the inner product of each word, including the inner product of each word with itself. 

Consider the following sentence, we would need to take many inner products, for hello we would need to $\frac{n^2-n}{2}$ many dot products and we would obtain a [[Similarity Matrix]]. 

|       | hello   | there   | how     | are     | you     |
| ----- | ------- | ------- | ------- | ------- | ------- |
| hello | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| there | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| how   | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| are   | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| you   | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |

We refer to the similarity measure between words as __attention__. Under this methodology we are using the "__full receptive field__" since each word by each word has some value. Secondly, this is better than the initial kernel model with the extended windows for features since we examine the structure in its totality but it only took into account 4 words. 

---
If we have a transformer with embedding dimension $512$ and a document $100$ words, what does our input look like?

Recall that we do row wise storage of words. The document would be $100 \times 512$, meaning $100$ words, and then the respective embedding taking place in $512$ (note this cannot be [[One Hot Encoding]] as this would get each word entirely similar to itself and 0 everywhere else and thus be useless).

Consider now that we take our embedding matrix, $X \in \mathbb{R}^{100 \times 512}$ and multiply $X$ by its [[Transpose]] $X^T \in \mathbb{R}^{512 \times 100}$:

$$\begin{bmatrix}
\dots \text{ hello } \dots  \\
\dots \text{ how } \dots  \\  
\vdots \\
\dots \text{ you } \dots  \\ 
\end{bmatrix} \cdot \begin{bmatrix}
\vdots  & \vdots  & \vdots \\  \text{ hello } & \dots & \text{ you }  \\
  \vdots & \vdots & \vdots  \\
\end{bmatrix} = \begin{bmatrix}
\text{ sim(hello,hello) }  
\end{bmatrix} $$
This yields the [[Similarity Matrix]] where we find the similarity of each word with each word and itself. 

---
# What does the architecture look like? 
We have some input coming in, some $Q,K,V$ from the input, where the input is $x \in \mathbb{R}^{100 \times 512}$ (to reiterate $512$ is the [[Embedding]] dimension size). We have three associated weight matrices which are learnable:

$$W_{q} \in \mathbb{R}^{512 \times 512} ,W_{k},W_{v}$$
###### From which we can obtain:
$$\begin{align}
Q = X \cdot W_{q} \in \mathbb{R}^{100 \times 512}
\end{align}$$
How about if $W_{k}$ is a neural network with $512$ neurons:
$$K=X \cdot W_{k} \in \mathbb{R}^{100 \times 512}$$
Here we denote $I^{(n)}$ to be the identity matrix where $I^{(n)} \in \mathbb{R}^{n \times m}$ and that for $Y_{{m \times n}} \cdot I^{(n)}=Y_{{m \times n}}$. 

Let us define another matrix here, $A$, the __Attention__ as:
$$A=Q \times K^T = (X \times W_{q}) \times K^T = (X \times W_{q}) \times (X \times W_{k})^T $$
If $W_{q},W_{k}$ are identity matrices then we would get the following:
$$A=(X \times I^{(n)}) \times (X \times (I^{n}))^T = XX^T$$ Which again is the [[Similarity Matrix]]. 

There is also the $V$ in the transformer where $W_{v} \in \mathbb{R}^{512 \times 512}$, and we have:
$$V=X \times W_{v} \in \mathbb{R}^{100 \times 512}$$
$$\text{ out}=A \times V$$
The final output from our transformer out is $\text{out} = A \times V$. 

Our basic idea of the transformer is to repeat this computation in each layer of the transformer. 

A way we can think of $K,Q,V$ is that all of these are new feature representations of each word. Otherwise, if these were the identity we would get self attention for each word and every other word itself. When a transformer is trained the learnable parameters are $W_{k},W_{q},$ and $W_{v}$. 

---
# Effects of Adding Additional Heads 

If we look at the total number of learnable parameters, we have $3 \times d \cdot \frac{d}{h} \cdot h + W_{0}$  where $W_{0}$ denotes the output vector for the layer. If we examine a 1-headed model we get $3 \cdot d^2 +W_{0}$ many parameters. This is to say that the effects of adding more heads __does not__ actually change the total model complexity since when we add more, we are not actually adding any parameters. 

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

---
# Where do we add the Softmax, Normalization, Skip Gradients, and Positional Encoding into our Model?

Let us take $d=512$ theembedding size, $h=8$ heads per layer, and $1024$ sequence length with a dictionary size $50,000$. 

### Pre-Processing For a Transformer
$$\begin{align}
\text{1024 Words} \xrightarrow{\text{One Hot Encoding}} A_{1024 x 50,000} \xrightarrow{\text{Embedding Layer}} WE_{50,000 \times 512} \to A\cdot WE=X_{{1024 \times 512}} \\

\end{align}$$

### Processing for Transformer Overall
$$\begin{align}
X_{1024 \times 512} \longrightarrow \underbrace{\oplus }_{\text{Position}} \longrightarrow \underbrace{\begin{bmatrix}
Q_{1}, K_{1},V_{1} \\
 \vdots \\
Q_{8}, K_{8},V_{8}
\end{bmatrix}}_{\text{Layer 1}} \longrightarrow 1024 \times 512 \longrightarrow \underbrace{\begin{bmatrix}
Q_{1}, K_{1},V_{1} \\
 \vdots \\
Q_{8}, K_{8},V_{8}
\end{bmatrix}}_{\text{Layer 2}} \longrightarrow 1024 \times 512  \\
\longrightarrow 1024 \times 512 \underbrace{\begin{bmatrix}
Q_{1}, K_{1},V_{1} \\
 \vdots \\
Q_{8}, K_{8},V_{8}
\end{bmatrix}}_{\text{Layer }N} \longrightarrow \underbrace{1 \times 512}_{\text{(Last Row)}} \longrightarrow \text{FFN} \longrightarrow \underbrace{\hat{y}}_{\text{Prediction}}
\end{align}$$The reason why we extract the $1 \times 512$, we need to have some flatened representation for the FFN.

### Layer $l$ (View 3):
Let $X \in \mathbb{R}^{1024 \times 512}$ be the input layer:

$$\begin{align}
X_{1024 \times 512} \underbrace{\longrightarrow \quad  \begin{matrix}
\text{Heads} \\
Q,K,V \\
\text{comp}
 \end{matrix}}_{\text{Skip connection}} 
\end{align}$$

### Inside the Head (View $4$)
Here the attention is done on different parts of the feature extracted inputs For our understanding, we can think about the head computations individually. Here we want to look at a __single__ head and see its resulting output. 

$$\begin{align}
X_{1024 \times 512 } \longrightarrow \begin{cases}
XW_{Q_{512 \times 64}}=Q_{1_{1024 \times 64}}^{(l)} \\
XW_{K_{512 \times 64}}=K_{1_{1024 \times 64}}^{(l)} \\
XW_{V_{512 \times 64}}=V_{1_{1024 \times 64}}^{(l)}
\end{cases} \xrightarrow{\text{Attention}} A^{(l)} = \text{softmax}\left( \frac{Q_{1}^{(l) } \cdot K^{(l)^T}  }{\sqrt{ d_{k} }} \right)  \\
\text{output}_{{1}}^{(l)} = \underbrace{A_{1}^{(l)}}_{1024 \times 64}  \cdot \underbrace{V_{1}^{(l)}}_{64 \times 1024} 
\end{align} $$
We want the softmax to be applied rowwise to our attention $A$, we want to have this nice self attention which tells us the similarity of the parameters. We also divide by the dimension to help normalization.

### All Heads at Once (View 5):

$$\begin{align}
X_{1024 \times 512 }   \longrightarrow \begin{matrix} Q \\
K \\
V 
\end{matrix} \longrightarrow \begin{cases}
\text{first }64 \text{ features } \to \boxed{Q_{1}^{(l)},Q_{1}^{(l)},Q_{1}^{(l)}} \to \text{output }1024 \times 64 \\
\vdots \\
\text{last }64 \text{ features } \to \boxed{Q_{8}^{(l)},Q_{8}^{(l)},Q_{8}^{(l)}} \to \text{output }1024 \times 64 \\
\end{cases}  \\ \\
\longrightarrow \text{stack}_{1024 \times 512} \times W_{0} = \text{All Heads Output}_{1024 \times 512}   \end{align} $$
---
# Attention is All You Need 