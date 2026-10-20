


The next word depends on the first word as [[conditional probability]], namely given $p(w_{1})$ we have $p(w_{2}|w_{1})$. The probability value of the third word is based off of the first $2$ so we obtain that $p(w_{3}|w_{1},w_{2})$. 

Given this arrangement we can express that:
$$p(w_{_{1}},w_{2},\dots,w_{n}) = p(w_{1}) \cdot p(w_{2} | w_{1}) \cdot \dots \cdot p(w_{n}|w_{1},\dots,w_{n-1}) $$
Or more succinctly:
$$p(w_{1},w_{2},\dots,w_{n})= \prod_{i=1}^n p(w_{i} | w_{1},\dots,w_{i-1} )$$
Let us compute the probability of the sentence "a red fox.", using the above identity we have the following computation:

$$P(\text{"a red fox"})=P(\text{a})\cdot P(\text{red}|\text{a}) \cdot P(\text{fox} | \text{a},\text{red}) \cdot P(.|\text{a,red,fox})$$

Visually we begin with a start token, take it through a transformer layer. 
(TODO Later)

Let us assume that the model correctly predicts the next word most of the time. 

---
# Metric for Measuring the Quality of a LLM

We are going to develop [[Perplexity]].

We want to develop a metric for the quality of an LLM. We can start with the conditional probabilities of all of the words. As we tend to use smaller numbers, we would get a number that approaches $0$ continually, and we get a very small value in the end. 

We could take the reciprocal of the word if we wanted to. Sentences also tend to have different numbers of words per sentence. There are two ways this can be solved, one we could cumulatively measure the correctness of the model with some kind of average function in either a standard [[mean]] or a [[Geometric Mean]]. 

The mean formula doesn't penalize outliers significantly. Say we want to predict the sentence "I am happy", but it predicts "I am sad". It was really good for everything except for "sad":

$$P(\text{I})=0.99, P(\text{Am} | \text{I})=0.99, P(\text{Happy|I am })=0.01$$
Here if we did an average with the standard [[mean]] and geometric we would obtain:

$$\text{Geometric Mean} = (0.99 \cdot 0.99 \cdot 0.01)^{1/3} = 0.2140 $$
$$\text{Arithmetic Mean} = \frac{0.99 + 0.99 \cdot 0.01}{3} \approx 0.6$$

No we will take the geometric mean with a reciprocal:
$$\text{Perplexity}(W) = \left(\frac{1}{\prod_{i=1}^n p(w_{i} | w_{1},\dots,w_{i-1} )}\right)^{1/n}$$
This metric is equivalent to:
$$\text{Perplexity}(W)=2^{(-1/n) \cdot p(w_{1},w_{2},\dots,w_{n}) }$$
### Understanding Perplexity 

We can obtain the perplexity measure in one of two ways. It is the __"inverse geometric mean of the language model's confidence in predicting words in a sentence"__.

We can also obtain the perplexity measure in an Information Theory way. We will introduce Entropy, Cross Entropy, and then Perplexity. 

What is Entropy? In Information Theory, this is the average level of "uncertainty". Take [[Random Variables]] $X$, then:

$$H(X) = -\sum_{x \in X} p(x)\log(p(x))$$
# Cross Entropy
[[Cross Entropy]] is a [[Loss Function]] used to train a model. We have two distributions $p$ the target, and $q$ the predicted model:

$$H(p,q) = -\sum_{x \in X} p(x) \log(q(x))

$$
To understand this metric we need to understand KL-Divergence. For a given input we want to predict the next word, what is our model outputting? A probability distribution:

$$\begin{align}
p=[0.3,0.0,0.4,0.3] \\
q=[0.0,1.0,0.0,0.0]
\end{align}$$
How do we measure the difference between two different distributions? We use the [[Kullback-Leibler Divergence]]:

$$D_{KL}(p||q) = \sum_{x \in X} p(x) \log()$$
How does KL Divergence relate to cross entropy?

$$H(p,q) = -\sum_{x \in X} p(x) \log(q(x)) = -\sum_{x \in X} p(x)(\log(q(x)) + \log(p(x)) - \log(p(x)))$$ $$= -\sum_{x \in X} p(x) \left( \log\left( p(x) + \frac{\log(q(x))}{p(x)}  \right) \right) = -\sum_{x \in X}p(x) \log(p(x)) - \sum_{x \in X} p(x) \log\left( \frac{q(x)}{p(x)} \right) $$
The left term is the entropy and the KL divergence. When we minimize the [[Cross Entropy]] loss we are minimizing the statistical distance between our target distribution and our model's distribution. 

In total cross entropy is essentially entropy plus [[Kullback-Leibler Divergence]]. 

---

When predicting a word our model outputs a probability vector. Assume that we have $C$ words in our dictionary. Then we can write the entropy associated with predicting one word:

$$H(p,q)=-\sum_{x \in X} p(x) \log(q(x))$$

This is the loss associated with the loss for one word. A more idiomatic way to write this expression in machine learning is:

$$l= -\sum_{c=1}^C \underbrace{y_{c}}_{\text{target prob}} \cdot \log( \underbrace{p_{c}}_{\text{prob pred}} ) $$

Here $C$ is the total number of words in the dictionary. $p_c$ is what comes out of the model for the $c$th word. Recall that $y_c=1$ for the correct class label $j$, and that $y_{c}=0$ for all other class labels (words). 

In the following, "Hello there how are you", suppose that the word "there" has $j=32$. We would have that $y_{32}=1$ =and all other $y_{i}$ will be $0$. 

We can simplify this significantly since $y_{j}=1$, so:
$$l = -\log(p_{j})$$
Our loss function only cares about the computation for computing $p_{j}$. 

Our loss value is computed with respect to not just one predicted word but multiple predicted words. If we look at the sequence of words we are feeding in, then we will see:

$$l_{n}= -\frac{1}{N} \sum_{p=1}^N \log(p_{i,j})$$
Here $p_{i,j(i)}$ is the __model's probability for the correct word__. So when $j(i)=32$, we are looking for the probability that its probability. We want to get a probability that is high in order to minimize our loss.  This formula here is the [[mean]] of the [[Entropy]] across all of the words. 

How is the loss function we are training on related to our cross entropy? 

$$\exp(l_{n})= \exp\left( -\frac{1}{N} \sum_{i=1}^N \log(p_{i,j(i)}) \right) = \exp\left( -\frac{1}{N} \log( (p(i,j(i)))^{1/n}) \right) = \prod_{i=1}^N (p_{i},j(i))^{-1/N} $$
We can think of this overall as $e$ to the power of [[Cross Entropy]] is [[Perplexity]]. We generally __do not train on perplexity__, but we do use [[Cross Entropy]] as our value. 

---
# Why do we use Perplexity instead of [[Cross Entropy]]?

Generally because it is a lot more human interpretable to deal with these values than cross entropy. 

---
