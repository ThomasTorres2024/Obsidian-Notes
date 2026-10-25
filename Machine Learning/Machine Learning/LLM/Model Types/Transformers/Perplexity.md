---
title: Perplexity
tags:
  - Machine_Learning
  - LLMs
draft: "False"
---
# Perplexity Derivation

The following shows two methods for the derivation of the [[Perplexity]] metric. It allows us to score the confidence of some sequence of [[Token]]s by an LLM. We can interpret [[Perplexity]] as  metric which tells us the inverse geometric mean of the conditional probability of $n$ words produced. 

### Conditional Probability and [[Baye's Rule]]

$$P(A|B) = \frac{P(A \cap B)}{P(B)} $$
$$P(A \cap B) = P(A|B) \cdot P(B)$$

LLMs produce words in a sequence where the next word is based off of the previous words generated:
$$\underbrace{\text{where are we }}_{\text{previous words}} \quad \underbrace{going}_{{\text{next }}}$$
A __symbol__ here can be a word, a character, a sub-word. It depends. We can let "walking" be divided into two separate symbols e.g. "walk" and "ing" if we want to do so, consider the following sequence:
$$(w_{1},w_{2},\dots ,w_{n})$$

LLMS operate to produce sub-words. Sub-words can be seen as one type of [[Token]] that LLMs produce.

### Relationship between Conditional Probability and NLP

Since words are produced based on the previous word, we want to write the models confidence overall as some probability value. We can begin by feeding the first word $w_0$ into the LLM ([[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]]) from which we obtain $p(w_{1})$ the probability of the first word. 
 
The next word depends on the first word as [[conditional probability]], namely given $p(w_{1})$ we have $p(w_{2}|w_{1})$. The probability value of the third word is based off of the first $2$ so we obtain that $p(w_{3}|w_{1},w_{2})$. 

Each word is given as some conditional probability. The probability of some $n$ words being produced is the probability of the first word on top of the probability of the second word and so on to the $n$th degree. 

Given this arrangement we can express that:
$$p(w_{_{1}},w_{2},\dots,w_{n}) = p(w_{1}) \cdot p(w_{2} | w_{1}) \cdot \dots \cdot p(w_{n}|w_{1},\dots,w_{n-1}) $$
Or more succinctly:
$$p(w_{1},w_{2},\dots,w_{n})= \prod_{i=1}^n p(w_{i} | w_{1},\dots,w_{i-1} )$$
#### Concrete Example of Word Probability

In terms of model architecture of [[Machine Learning/Machine Learning/LLM/Model Types/Transformers/Transformer|Transformer]]s we are actually doing the following:
$$\text{Input} \xrightarrow{} \boxed{\text{Transformer Layers}} \to \boxed{\text{Latent Word Representation}} \xrightarrow{\text{Output Next Word}} \begin{pmatrix}
\boxed{\text{ a } } \\
\boxed{\text{the}} \\
\boxed{\text{red}} \\
\boxed{\text{fox}} \\
\boxed{\text{dog}} \\
\boxed{\text{ . }}
\end{pmatrix}  $$

Let us compute the probability of the sentence "a red fox.", using the above identity we have the following computation using the [[Probability]] function for a set of words:

$$P(\text{"a red fox"})=P(\text{a})\cdot P(\text{red}|\text{a}) \cdot P(\text{fox} | \text{a},\text{red}) \cdot P(.|\text{a,red,fox})$$

Visually we begin with a start token, take it through a transformer layer, latent word representation, and obtain [[Softmax]] probabilities:

![[Pasted image 20261024151427.png]]

Let us assume that the model correctly predicts the next word most of the time. Here we have $6$ probability measures for each word produced. 

The first value is $0.4$. When we compute $P(w_{2}|\text{a})$ and we look for the word $w_{2}=\text{red}$, then we  get some other distribution of words. Here we would get $0.27$ for the second 

![[Pasted image 20261024151618.png]]

Likewise for the $3$rd with our training set we obtain $P(\text{fox}|\text{a, red})=0.55$ and one more time with our next word (a ".") to obtain $0.79$ so on until we get our sequence of words. This produces the following:

$$\begin{align}
P(\text{a red fox .})=P(\text{a}) \cdot P(\text{red} | \text{a}) \cdot P(\text{fox}|\text{ a red}) \cdot P(\text{. | a red fox} ) \\
= 0.4 \cdot 0.27 \cdot 0.55 \cdot 0.79 = 0.0469
\end{align} $$
---
# Metric for Measuring the Quality of a LLM

We are going to develop [[Perplexity]] now as a metric. 

#### Decaying Probabilities - Issue 1
If we assumed that the models both correctly predict the next word __most__ of the time and then want to compare two models and their respective conditional probability measures we will run into some issues using raw [[Conditionality Probability]] values. 

Since each probability is less than $1$, as the length of the sequence grows the number tends towards $0$ and becomes less meaningful as a metric to interpret. We could use the reciprocal of the conditional probability of the sequence of words instead. We will get a larger number. This makes computation much nicer to work with.

So we do the following:

$$p(w_{1},w_{2},\dots ,w_{n}) = \prod_{i=1}^n p(w_{i}|w_{1},\dots,w_{n}) \longrightarrow \frac{1}{p(w_{1},w_{2},\dots ,w_{n})} = \frac{1}{\prod_{i=1}^n p(w_{i}|w_{1},\dots,w_{n}) }   $$
#### Number of Words in Sentence - Issue 2 

Sentences also tend to have different numbers of words per sentence. For example in a sentence such as "hello there how are you" we have $5$ words and in a sentence like "the quick brown fox jumped over the lazy dog" we have $9$ words. We should have an equitable representation among the $2$ that doesn't favor or disfavor based on length. 

There are two ways this can be solved, one we could cumulatively measure the correctness of the model with some kind of average function in either a standard [[Arithmetic Mean]] or a [[Geometric Mean]]. 

The mean formula doesn't penalize outliers significantly. 

Say we want to predict the sentence "I am happy", but it predicts "I am sad". It was really good for everything except for "sad":

$$P(\text{I})=0.99, P(\text{Am} | \text{I})=0.99, P(\text{Happy|I am })=0.01$$

Here if we did an average with the standard [[mean]] and geometric we would obtain:
$$\begin{align}
\text{Geometric Mean} = (0.99 \cdot 0.99 \cdot 0.01)^{1/3} = 0.2140  \\

\text{Arithmetic Mean} = \frac{0.99 + 0.99 \cdot 0.01}{3} \approx 0.6
\end{align}$$

We want a score that is __low__, so we obviously prefer the [[Geometric Mean]]. It much more severely punishes the outlier score than does the [[Arithmetic Mean]]. 

No we will take the geometric mean with respect to the reciprocal from issue 1. This yields the __Perplexity__ measure. 

$$\text{Perplexity}(W) = \frac{1}{ (\prod_{i=1}^n p(w_{i} | w_{1},\dots,w_{i-1} ))^{1/n} }$$
Note that this metric is also equivalent to:
$$\text{Perplexity}(W)= 2^{(-1/n) \cdot \log(p(w_{1},w_{2},\dots,w_{n}) )}$$
This comes from:
$$\begin{align}
2^{-1/n \cdot \log(p(w_{1},w_{2},\dots,w_{n}))} = 2^{\log( p(w_{1},w_{2},\dots,w_{n}) )^{-1/n} } = p(w_{1},w_{2},\dots,w_{n})^{-1/n} \\
= \left( \prod_{i=1}^n p(w_{i}|p_{1},p_{2},\dots,p_{n})  \right)^{-1/n} = \frac{1}{\left[ \prod_{i=1}^n p(w_{i}|p_{1},p_{2},\dots,p_{n})  \right]^{1/n}}
\end{align}  $$
Through this manner of derivation we obtain that [[Perplexity]] through raw probabilities. 
### Understanding Perplexity 

We can obtain the perplexity measure in one of two ways. It is the __"inverse geometric mean of the language model's confidence in predicting words in a sentence"__.

We can also obtain the perplexity measure in an Information Theory way. We will introduce Entropy, Cross Entropy, and then Perplexity. Generally a smaller value for perplexity indicates better model performance. Larger models tend to do worse. In the following the model with 

# Information Theory Derivation of Perplexity 

It can be shown that we can derive [[Perplexity]] from information theory by examining first [[Entropy]] and then [[Cross Entropy]]. 
## 1). Understanding Entropy 
What is Entropy? In Information Theory, this is the average level of "uncertainty". Take [[Random Variables]] $X$, then:

$$H(X) = -\sum_{x \in X} p(x)\log(p(x))$$
#### Entropy Examples 
For a biased coin with probability $0.99$ of the time it lands on hands, let $X$ be the outcome of the coin. What is the entropy of $X$? 

$$H(x) = -(0.99 \cdot \log(0.99) + 0.01 \log(0.01)) \approx 0.0808$$
This has a low entropy and is almost a guaranteed head. 

Instead let $p$ heads be $0.5$ and recompute:

$$H(x) = -(0.5 \cdot \log(0.5) + 0.5 \log(0.5) = -\log\left( \frac{1}{2} \right)=\log(2)=1 \quad (\text{Assume base }2)$$
This has a high entropy and we do not have a guaranteed head or tails. We are at a maximal state of entropy here. 

---
## 2). Understanding Cross Entropy

[[Cross Entropy]] is a [[Loss Function]] used to train a model. We have two distributions $p$ the target, and $q$ the predicted model:

$$H(p,q) = -\sum_{x \in X} p(x) \log(q(x))

$$

To understand this metric we need to understand KL-Divergence. For a given input we want to predict the next word, what is our model outputting? A probability distribution:

$$\begin{align}
p=[0.3,0.0,0.4,0.3] \\
q=[0.0,1.0,0.0,0.0]
\end{align}$$
Recall here that $p$ is our target distribution and $q$ is our model of $p$. We want to know how far apart our two [[Probability Mass Function]]s/[[Probability Density Function]]s are from one another. One such [[Metric]] which can be used for this is the [[Kullback-Leibler Divergence]] 

### Kullback-Leibler (KL) Divergence 

How do we measure the difference between two different distributions? We can use a [[Metric]] from statistics known as the [[Kullback-Leibler Divergence]]. Here $p(x)$ is our target distribution and $q(x)$ is our model of $p(x)$. 

$$D_{KL}(p||q) = \sum_{x \in X} p(x) \log( p(x)-q(x) ) = D_{KL}(p||q) = \sum_{x \in X} p(x) \log\left( \frac{p(x)}{q(x)} \right) $$
The second identity is obtained through simple log properties. 

### How does KL Divergence relate to cross entropy?

Recall the formula for [[Cross Entropy]]:
$$H(p,q)= - \sum_{x \in X} p(x) \log(q(x)) $$
Let use add and subtract an additional $p(x)\log(p(x))$ term:
$$H(p,q) = -\sum_{x \in X} p(x) \log(q(x)) = -\sum_{x \in X} p(x)(\log(q(x)) + \log(p(x)) - \log(p(x)))$$ $$= -\sum_{x \in X} p(x) \left( \log\left( p(x) + \log\left( \frac{q(x)}{p(x)} \right)  \right) \right) = -\sum_{x \in X}p(x) \log(p(x)) - \sum_{x \in X} p(x) \log\left( \frac{q(x)}{p(x)} \right) $$
$$= -(\text{Entropy}(X)+ D_{KL}(p||q) )$$

The left term is the entropy and right is the KL divergence. When we minimize the [[Cross Entropy]] loss we are minimizing the statistical distance between our target distribution and our model's distribution. 

$$H(p,q) = \underbrace{-\sum_{x \in X}p(x) \log(p(x))}_{\text{Entropy}} + \underbrace{-\sum_{x \in X} p(x) \log\left(  \frac{q(x)}{p(x)}  \right)}_{\text{KL-Divergence}}$$

In total cross entropy is essentially [[Entropy]] plus [[Kullback-Leibler Divergence]]. We can conclude here that when we minimize for [[Cross Entropy]] during training that we are minimizing the statistical distance between our target $p(x)$ and our approximation of the target $q(x)$. 

---
### 3). Obtaining [[Perplexity]] from [[Entropy]] and [[Kullback-Leibler Divergence]]

Since we are applying these topics to machine learning we can make some simplifying assumptions about our problem. 

When predicting a word our model outputs a probability vector. Assume that we have $C$ words in our dictionary. Then we can write the entropy associated with predicting one word:

$$H(p,q)=-\sum_{x \in X} p(x) \log(q(x))$$

This is the loss associated with the loss for one word. A more idiomatic way to Machine Learning is to write this expression in machine learning is:

$$\ell = -\sum_{c=1}^{C} \underbrace{y_c}_{\text{target}} \; \underbrace{\log p_c}_{\text{predicted}}   $$
$p_c$ is the probability of the model for the $c$th word in the dictionary. $y_{c}$ is the target probability we want to achieve. 

Here $C$ is the total number of words in the dictionary. $p_c$ is what comes out of the model for the $c$th word. Recall that $y_c=1$ for the correct class label $j$, and that $y_{c}=0$ for all other class labels (words). This significantly simplifies the loss function by essentially deleting all other terms in the series, so our loss here on word $j$ becomes:

$$\ell = -y_{j} \log(p_{j})=-\log(p_{j})$$

In the following, "Hello there how are you", suppose that the word "there" has $j=32$. We would have that $y_{32}=1$ and all other $y_{i}$ will be $0$ for $i\neq j$.  

We can simplify this significantly since $y_{j}=1$, so:
$$l = -\log(p_{j})$$
Our loss function only cares about the computation for computing $p_{j}$. 

Our loss value here is computed with respect to not just one predicted word. But, if we want to evaluate a model, we want to predict it with respect to $N$ many words we have to use a different approach. For the sake of assumption say $N$ is the number of predicted words for some sequence. 

If we look at the sequence of words we are feeding in. This gives us the __Average Cross Entropy__ for our model on some predicted words 

$$\ell_{n}= \underbrace{-\frac{1}{N} \sum_{p=1}^N \log(p_{i,j(i)})}_{\text{Average Cross Entropy}}$$

Here $p_{i,j(i)}$ is not the probability that the model will predict the correct word, it is the __model's probability for the correct word__. So, if we input the word "hello", we are looking at the value that is being assigned to the next following word. Say if the word "there" follows, we are looking for the probability that there is assigned next. This is the probability of times we assign the word there next. 

If the word there is close to $1$ we are happy. However, if the value is small we want to penalize the model. 


So when $j(i)=32$, we are looking for the probability that its probability. We want to get a probability that is high in order to minimize our loss.  This formula here is the [[mean]] of the [[Entropy]] across all of the words. 

How is the loss function we are training on related to our cross entropy? 

$$\exp(\ell_{n})= \exp\left( -\frac{1}{N} \sum_{i=1}^N \log(p_{i,j(i)}) \right) = \exp\left( -\frac{1}{N} \log( (p(i,j(i)))^{1/n}) \right) = \prod_{i=1}^N (p_{i},j(i))^{-1/N} $$
We can think of this overall as $e$ to the power of [[Cross Entropy]] is [[Perplexity]]. We generally __do not train on perplexity__, but we do use [[Cross Entropy]] as our value. 

---
# Why do we use Perplexity instead of [[Cross Entropy]]?

Generally because it is a lot more human interpretable to deal with these values than cross entropy. 

---
