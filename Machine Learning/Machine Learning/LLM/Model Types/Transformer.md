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
# More on Masking
During the training process of a transformer, if we have an $n$ word sentence and want to predict the $n$th word from $n-1$ words, we would have each word in a sequence predict a new word, that is to say we would see the following:

$$\begin{align}
\text{hello} \longrightarrow \text{there} \\
\text{hello there } \longrightarrow \text{how} \\
\vdots \quad \quad \quad \quad \quad \quad  \vdots \\
\text{hello there how are} \longrightarrow \text{you} \\

\end{align}$$
We do this both during the training process and the feed forward process to predict. The way that we train the model is the same way we use it for inference. Since we train the model in this manner, we need to sue the same procedure in order to predict our values. 

---
# Attention is All you Need

In the original attention paper, they define [[Attention]] differently, namely:
$$A=\text{softmax}\left( \frac{QK^T}{\sqrt{ d_{k} }} \right)\cdot V$$ But for us this is $"\text{out}"$. The original context of the paper was in the task of language translation from French to English. 

![[Pasted image 20261013102550.png]]

The transformer consists of two main components.

1. A stack of [[Encoder (Transformer)]]s
2. A stack of [[Decoder (Transformers)]]s

The output of the encoder is processed by the decoder. The decoder's output is then translated by the sentence. Input from one encoder is continually fed into another from some original sentence. 

![[Pasted image 20261013102940.png]]

If we pass in $3$ words and they an have an embedding of size $3 \times 512$, then the input and output for each layer is likewise $3 \times 512$. 

Each encoder block consists of some self [[Attention]] component followed by a [[FFN]], which finally produces some output $Z$:

![[Pasted image 20261013103217.png]]

If we look inside of the self attention at each layer, we will see the typical computations for $Q,K,V$ inside of a single head:

![[Pasted image 20261013103339.png]]

Now examining these values stacked looking at all $8$ of the heads:

![[Pasted image 20261013103410.png]]

We then combine all of the heads and multiply them by a large weight matrix $W_{0}$:

![[Pasted image 20261013103543.png]]

For the Self-Attention computation, we can summarize the previous components we looked at with the following:

![[Pasted image 20261013110457.png]]

We can add the additional changes as well like [[Positional Encoding]], layer normalization, and a FFN as well:

![[Pasted image 20261013112019.png]]

### What was modified about the Transformer Architecture?

1. We added [[Positional Encoding]] to make the different positions matter 
2. The dashed lines are [[Skip-Connections]] which prevent problems involving a vanishing gradient during training
3. Layer Normalization just means better performance in general

In some transformer architecture we do positional encoding at each layer. But for a lot of them, we only do it on the first. We are currently on the __encoder stack__ 

For one we added a [[Positional Encoding]] layer before the [[Attention]] computation. 

---
# Big Idea

We are feeding our original data through various layers of encoding in order to obtain a latent representation which is easy to do translation with. Part of the last Encoder Computation is fed into each of the decoders, the decoders then generate a translation in an __Auto Regressive Manner__. 

In step one we pass through the entire sentence to be translated through the encoder. 

![[Pasted image 20261019144634.png]]

Once everything is fed through the, we feed the last latent $K,V$ representation of the entire sentence into the decoder architecture. 

We should ask ourselves what does the decoder take as an inputs during training? It takes a translation of our sentence: 


![[Pasted image 20261019145044.png]]

Here we have a target output that we are expecting from our input. 

```
salloc -p gpu -t 08:00:00 --nodes=1  --gpus=v100:4 --mem=

salloc -p gpu -t 08:00:00 gpus=rtx8000 --mem=50G

unity-slurm-gpu-usage --sort free

unity-slurm-gpu-usage -h
```

* What does the decoder architecture look like?
* How is $K,V$ used in the encoders?

---
#### Decoder Architecture 

We have a self attention computation alongside an "add and normalize" layer. 

![[Pasted image 20261019145418.png]]

### Encoder-Decoder Attention

In the Decoder stack, we have $XW_0=Q$.  $Q$ here is the English we have translated, and $K,V$ are french encodings of the original french message. 

Secondly, during this stage we have the normal attention computation:

$$Z=\text{softmax}\left( \frac{QK^T}{\sqrt{ d_{k} }} \right)V$$

Notice that we are interestingly mixing the French and English parts together. The way we have defined Attention is the "similarity between words", whereas here the attention we think of as the quantity $Z$ (that is the original self attention multiplied by $V$, also we did not mix words in different languages in our original). 

Here this computation is known as "Cross-Attention" since we mix the two parts. 

#### What does the decoder architecture look like?

![[Pasted image 20261019150936.png]]

We have a normal self attention, normalizing/adding, and then the cross attention. Lastly we have the feed forward neural network with some adding and normalization again. 

Let us examine an example with $2$ encoders and and decoders and see the details of how data is processed:

![[Pasted image 20261019151313.png]]

---
# Understanding Decoder Encoder Architecture 

Let $a$ be the encoding dimension, we will have $3$ encoders $3$ decoders, with 1 head per layer. We want to examine the operations during training. 

We have the following input and output:

* $\text{Input}=$ Je Suis Etudiant
* $\text{Output} =$ I am a student 

$$\begin{align}
3 \times 512  \xrightarrow{\text{Positional Encoding }\oplus } \boxed{\text{Encoder 1}}
\end{align} \xrightarrow{} 3 \times 512 \text{ output} \\
\longrightarrow  \boxed{\text{Encoder 2}} \xrightarrow{} 3 \times 512 \text{ output} \longrightarrow \boxed{\text{Encoder 3}} \longrightarrow K,V \in \mathbb{R}^{3 \times 512} $$
On the last layer of the encoder we only care about getting $K,V$ not the output, which yields, taking in output $2$ from the second encoder layer $\text{Output}^{(2)}$ and $W_{K}^{(3)},W_{V}^{(3)}$ as weight matrices, we can obtain:

$$K_{E}^{(3)}=\text{Output}^{(2)} \cdot W_{K}^{(3)}$$
$$V_{E}^{(3)}=\text{Output}^{(2)} \cdot W_{V}^{(3)}$$
Both of which are in $3 \times 512$ as we would expect.

Now let us look at the decoder. If we look at what's going into decoder $1$ we have the following layout:

$$\begin{align}
K_{E}^3, V_{E}^3  \longrightarrow \boxed{\text{Decoder 1}} \longrightarrow  \\
\begin{cases}
\underbrace{x_{0} \longrightarrow \boxed{\text{Self Attention}}}_{{\text{Skip Connection } \oplus }  } \oplus  \longrightarrow 
\end{cases}
\end{align}$$

(I Wrote this out on paper, TODO, write this down as mermaid diagram too)

# Self Attention Computations:

$$\begin{align}
Q=X_{D} \cdot W_{QD}^{(1)} \\
K=X_{D} \cdot W_{KD}^{(1)} \\
V=X_{D} \cdot W_{VD}^{(1)} \\
S = \text{Softmax}\left( \frac{QK^T}{\sqrt{ d_{k} }} \right) \cdot V \\
A = \frac{QK^T}{\sqrt{ d_{k} }}
\end{align}$$

Let's write out the $S$ matrix:

|         | (start) | i       | am      | a       | student |
| ------- | ------- | ------- | ------- | ------- | ------- |
| (start) | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| i       | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| am      | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| a       | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| student | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
This is the $A$ matrix, the self [[Attention]] component where $A \in  \mathbb{R}^{5 \times 5}$

$V$ is the matrix which is given by the $V$ representation of the sentence "(Start) I am a student" where $V \in \mathbb{R}^{5 \times 512}$.

We need to use masking in order to cover up words from seeing the words that we want to predict. We want to hide parts of the sequence in order for this to properly work as a translator. 

If we feed in "start and I" into the matrix, we should not be able to see all of the other words. Going row by column 

Start should be able to see start, but nothing else in the row since we want a translation. It should NOT depend on anything else.

We can have a row for start with "I" since start came before. But "am", "a", and a student should all be $0$. 

Going row by column, we should see that 
 
|         | (start) | i       | am      | a       | student |
| ------- | ------- | ------- | ------- | ------- | ------- |
| (start) | $\dots$ | 0       | 0       | 0       | 0       |
| i       | $\dots$ | $\dots$ | 0       | 0       | 0       |
| am      | $\dots$ | $\dots$ | $\dots$ | 0       | 0       |
| a       | $\dots$ | $\dots$ | $\dots$ | $\dots$ | 0       |
| student | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
We get a corresponding matrix where each row corresponds to a representation of the attention of the words and their $V$ representation where we only take in input from the words which have non-zero entries per row. 

---
# 2. Encoder Decoder Attention

Each decoder in the transformer architecture has 2 parts, self attention (normal, which uses masking the one we have seen so far). The second attention operation uses $K,V$ from french $Q$ from English. 

Our input sentence here is "I am a Student", from which we can construct $Q$:
$$Q= S \cdot W_{Q_{ED}}^{(1)}$$
Since $S \in 5\times 512$ and $W_{Q_{ED}}^{(1)} \in 512 \times 512$  we obtain that $S \in 5 \times 512$ as well. Recall that $S$ is from the self attention part.

For $K,V$ we also have that they are $3 \times 512$ where $3$ is the number of words in French in "Je Suis Etudiant". The French words are $3$ but the English translation is $5$ words. 

When we do $QK^TV$ we get $QK^T \in 3 \times 5$ and then for $V \in 5 \times 512$  we get $3 \times 512$ for the whole matrix.  

__Is Masking necessary here during this computation__? 
Let us examine $Q\cdot K_{E}^T$ computation:

$$\underbrace{  \begin{bmatrix}
\dots \text{Start Q Rep} \dots  \\
\dots  \text{I Q Rep} \dots  \\
\dots \text{Am Q Rep} \dots \\
\dots \text{A Q Rep} \dots \\ 
\dots \text{Student Q Rep} \dots
\end{bmatrix}}_{Q, Q \in 5 \times 512} \times \underbrace{  \begin{bmatrix}
\dots \text{Je V  Rep} \dots  \\
\dots  \text{Suis V Rep} \dots  \\
\dots \text{Etudiant V Rep} \dots \\
\end{bmatrix}^T}_{K, K \in 3 \times 512}$$
Due to the transpose we have the col representations in $K$ instead of rows. Secondly, we have $5 \times 3$ attention matrix. We get the following output matrix: 

|         | je      | suis    | etudiant |
| ------- | ------- | ------- | -------- |
| (start) | $\dots$ | ...     | ...      |
| i       | $\dots$ | $\dots$ | ...      |
| am      | $\dots$ | $\dots$ | $\dots$  |
| a       | $\dots$ | $\dots$ | $\dots$  |
| student | $\dots$ | $\dots$ | $\dots$  |
Now we want to take $QK^T$ (above) and multiply it by $V$:

$$QK^T \underbrace{\begin{bmatrix}
\dots \text{je as } V\dots  \\
\dots \text{suis as }V \dots \\
\dots \text{estudiant as } V\dots
\end{bmatrix}}_{V, V \in \mathbb{R}^{5 \times 512}}$$

Since we are interested in producing English words we do __not need to hide any of the French words, so we do not need to mask them__. We are only interested in producing __English Words__ from this model.

We can conclude that English words are based __solely__ off of French input, and not English. This means that we do not need to use Masking. 

### Encoder-Decoder Architecture Questions about Masking in Translation

- Consider the concept of masking in the Transformer. For translation do we need masking in the encoder layers? Do we need masking in the decoder layers? Why or why not.
	- We do not need masking in the Encoder layers since we are not trying to predict the next word from some sequence of characters in the same language, whereas we do in the decoder since we want to generate output based on the input and get an understanding of where words are located
	- Answer:
		- For translation for the encoder we don't want to break up our original input sentence in the original language. The encoder is trying to make a meaningful representation of the sentence, so it should see the whole input, so we do __not use masking__.
		- Decoder solution, decoder is auto regressive (which means one word at a time). Therefore we need masking. In theory we can make a decoder produce  sentence but this increases the number of trainable parameters significantly. 
- Assume an embedding dimension of $512$ and one head per attention layer. Consider the Chinese sentence "Yuan Fen" which has an English translation of "unspoken fate brought us together". What will be the output dimensions of $K$ and $V$ for the encoder? What will be the dimension of $Q$ in the decoder? Would you be able to compute the cross attention, if so what are the dimensions? 
	- 6 words counting the start token __IMPORTANT TO NOT LEAVE THIS OUT__
	- $K,V \in 2 \times 512$. $Q \in 6 \times 512$. 
	- We can compute the cross attention:
	- $QK^T \in 6 \times 2$ and $(QK^T) \cdot V \in 6 \times 512$


---
# Training vs Inference in Encoder-Decoder

### Training
We have multiple training samples $(x,y)$. We give our model $x$ and have it learn to predict $y$. The full sentence for a training sample is passed in to the encoder. The full output $y$ is passed into the decoder and masking is used.

### Inference 
After the model has been trained we are given a sample $x'$ and we want our model to translate $x'$ to a different language. We continue to generate a word at a time until a stop token is reached. 

We pass $K^T,V$ into each of the decoder layers. We compute a single word for the sentence "je ne sais quoi".
 
![[Pasted image 20261019172247.png]]

We take $K^T,V$ and then feed them into a decoder with a start token and the word we used: 

![[Pasted image 20261019172454.png]]

Then we get quality from the next word. We pass the words "indescrible quality" in, and get a stop token.

![[Pasted image 20261019172544.png]]

This means we are done with the translation. 

# Takeaways from Attention is Al You Need
- Most modern architectures __only really use an encoder or a decoder__ 
- For example [[ChatGPT]] uses decoders and masking. 