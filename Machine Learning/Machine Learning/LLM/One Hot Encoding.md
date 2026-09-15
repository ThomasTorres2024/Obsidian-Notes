---
title:
draft: "False"
tags:
  - LLMs
  - Machine_Learning
---
### One Hot Encoding Process

The basis of ML requires conversion of input into data. Since text is generally not numeric it needs to be encoded ([[Tokenization]]) We feed it through a model, and obtain some output as a set of numbers. 

For the sake of simplicity, begin with the assumptions that we have some dataset of Wikipedia articles $D$. Assume that they have a finite number of unique words. Our input will never have words or pronouns outside of tis set of words (__this is a very unrealistic assumption__). 

1. First we want to count the number of the unique words in the dataset. Say for example we have 20,501 unique words.

2. Secondly we want to assign each word a numeric index:

| word     | index    |
| -------- | -------- |
| all      | 0        |
| apple    | 1        |
| $\vdots$ | $\vdots$ |
| zebra    | 20,500   |
* In the third step we want to perform a [[One Hot Encoding]], which we represent by a vector $\vec{x} \in \mathbb{Z}_{2}^{20,500}$ (consisting of only 0's, and 1's) such that if we have a $0$ where some word exists, then it does not exist in the sample. If there is a $1$, then it does exist:

$$\begin{align}
\text{"all"} \to  [1 \quad  \dots \quad 0]^T \\
\text{"apple"} \to  [0  \quad 1 \quad  \dots \quad 0]^T
\end{align}$$
__How could a sentence be encoded?__
Take for example the sentence, "Hello there how are you". From this sentence, we encode each word in the sentence into a vector of size $20,500 \times 1$ resulting in $5$ vectors of this type. 

* __Step 4__, now we convert every word in a sentence into a __One Hot Embedding Vector__. The embedding vector is a "feature representation of the word"

The size of the embedding vector is a fixed model parameter. We want to reduce the size of the vector and give it "more significance" while meaning more ([[Sparse Matrix]]). 

$$\mathbb{Z}_{2}^{20,501}\to \mathbb{R}^{512}$$
The amount here $512$ is the __embedding size__ which is something researchers generally determine that "just works". This is a [[Linear Algebra/Linear Algebra/Matrix Factorizations/SVD/Dimension Reduction|Dimension Reduction]] that occurs. In order to accomplish this we use a "simple linear network", that can be represented as a matrix multiplication. 

Our one hot encoded input word $x \in \mathbb{R}^{20,501}$ can be reduced by multiplication with the following weight matrix $W \in \mathbb{R}^{20,501 \times 512}$. 

The weight matrix is learnable. At the start of the training process its values are randomized. Say if the problem is classified, we then modify the weight matrix after the first through classification and keep iterating on this process. 

Because of the fact that we operate on [[Tensor]]s instead of merely vectors, we can store them, in which there are two classical ways to make the tensor. One option is row wise

in the row wise option we get a representation for the sentence, for the following sentence, "hello how are you", $\mathbb{R}^{5 \times 20,501}$ and in the column wise sense we get $\mathbb{R}^{20,501 \times 5}$. Let us denote this matrix (in both cases, dimensions will be specified) by $X$. 

If we multiply this by the weights then:
$$\begin{align}
X_{{5 \times 20,501}} \cdot W_{20,501 \times 512}
\end{align} = E_{5 \times 512}$$


### Design Question 1.
Why not just feed the vector raw into the model instead of embedding it? 

_Ans_ We want to reduce the dimensionality of the input making algorithms more efficient and secondly making the procedure more "feature rich". 

### Design Question 2. 
If we know $x$ and $W$ why not skip the matrix multiplication to its embedded representation? 

_Ans_ This is because $W$ is a learnable matrix. As we train the LLM numbers in $W$ are also updated and changed, which requires the matrix multiplication approach. We cannot pivot to a static lookup table until _after_ training has concluded. 

### Design Question 3. 
How do we choose the _embedding dimension_? 

It is a design choice. There isn't a good mathematical theory on this, this is essentially determined through some architecture and results showing that this figure performs the best. 

### Coding Question
Assume $16 \times 5 \times 20,501$ is our input. The tail is the size of the word encoding, this is the size of the one hot encoding for a single word. $5$ is the number of the words in each of the sentences. 

Here $16$ is related to the GPU, which allows many operations to occur in parallel. This is the [[Batch Size]], the number of $5 \times 20,501$ input sentences that can be run at the same time, this represents the number of sentences in total. 

How would we code a linear layer in order to flatten this to $512?$ 

In PyTorch, the linear layer operates on the last dimension always. The "in_features" represents the dimension of the input the first dimensions of the mtrix. The "out_features" would be 512, so here we would indicate:

```python
(20501,512)
```

In order to determine the size of the output tensor is to consider the last dimension always. Our trick is to ignore the first index:

$$X_{16 \times 5 \times 20,501} \cdot W_{20,501 \times 512} \in \mathbb{R}^{16 \times 5 \times 512} $$

Why do we care about tensor sizes? 

* 1. Theoretically it helps us understand our model better
* 2. It helps us debug Pytorch 

---
### Historical Approaches 

In the modern day, the process of converting words to numbers typically coincides in [[One Hot Encoding]]. This is the modern standard


### Bag of Words 
Take a sentence, "Inga goes hiking". BW will assign the words to the following arbitrarily

| word   | index |
| ------ | ----- |
| inga   | 1     |
| goes   | 2     |
| hiking | 3     |
| dog    | 4     |

Let's create a null vector and by each index we get:
$$[1,1,1,0]$$

Now in the sentence "Inga goes hiking hiking hiking" we run into the following problem, our sentence becomes:
$$[1,1,3,0]$$
This model isn't particularly great because the order of words matters, for example "dog eats man" and "man eats dog". Both sentences under BW would have the __exact same representation__ despite having a different meaning. We want a conversion model to __not__ be agnostic about the order of words. 

If the number of unique words in our dataset grows too large, then each sentence grows too. We also lose our on orderedness. 

---
### Term Frequency-inverse document (TF-IDF) frequency
Important in measuring how similar two documents off. 
$$\text{idf}(t,D)= \log\left(  \frac{N}{n_{t}} \right)$$
Here $t$ is a word, $D$ is the set of documents, $N$ is the number of documents, and $N_t$ is the number of documents with $t$. 

(in hiking dog examples)
In IDF model the word "hiking" appears in all sentences, so it isn't particularly relevant according to this model. IDF is not generally used alone to create numerical representations of words, instead it's used as a weighting factor. We can combine this with BW and get a weighted amount for each word used. 

#### Model Drawbacks 
A high number of unique words in the dataset leads to poor performance, and secondly is also not context dependent again. 

---
## Word Embedding 
We can train a model that takes a feature vector for each word. One of the most popular techniques is [[Word2Vec]]. How does it work? We count the number of words and assign each a number. We then convert each into a one hot encoding vector. 

This is the same as one hot encoding, now we begin with another route.

4. Come up with a scoring measure to measure similarity between words
5. Train a model with input from step 3 and target for 4  (for instance cold should be low or 0 if the input is hot, words like warm should be high)
6. Use the trained model to create feature vectors from one hot encoded vectors (from each word in the input vector, create an output vector such that we have a similarity score for each vector in the input vector)
7. After we finish training the model, we chop off the output layer, and we take the output from the hidden layer 
8. In the end step once we have the weight matrix $W$, then we product it by some input vector and get a resulting vector 

### Advantages and Disadvantages - 
If the unique number of words grows large, we do not need to worry as much with previous models since the embedding stage forces the output vector to remain normally sized. 

On the topic of order consider the sentence, "man eats dog", which results in a $3 \times 300$ embedding. Now consider $\text{"dog eats man"}$, which results in another $3 \times 300$ embedding. Each word is fed __independently__ into the model. Every time this occurs we do not do it with respect to the entire sentence. The same vector representation in the output is the __same__. 

Even in the embedding approach, the one we currently use, we run into the same issue. As a big difference, the weight matrix here that we use, $W$ is not customizable, we are stuck to using it.  