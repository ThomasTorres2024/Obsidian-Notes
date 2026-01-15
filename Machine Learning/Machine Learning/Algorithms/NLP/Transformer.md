---
title:
tags:
draft: "false"
---
# Transformers Overview

Given some sequence of words, we can produce a response and understand the given prompt much easier through the use of [[Transformer]]. [[Transformer]]s encode the position of a word in a high dimensional space, but go beyond previous methods for word embeddings to include information about surrounding words in the sentence. This information has to be parsed by a decoder in the transform

Transformers begin by vectorizing all words in a sentence, obtaining an [[Embedding]] of the words. This is known as [[Tokenization]]. We want to determine the [[Positional Encoding]]s of each word, which is how much they relate to other words in the sentence. There is some cleverness surrounding the idea, and it relies upon encoding using cosine and sine. 

Each word in the sequence is assigned an odd or an even time step, which is to say the first word has time step 1, the second word time step 2, and so on. Our resulting encodings are given by the following:
$$\begin{cases} \text{pos is even}  & PE(\text{pos},2i+1)= \sin\left(\frac{\text{pos}}{10,000^{2i/\text{dmodel}}} \right)\\

\text{pos is odd}  & PE(\text{pos},2i)= \cos\left(\frac{\text{pos}}{10,000^{2i/\text{dmodel}}} \right)
\end{cases}$$



Positional encoding satisfies all of these conditions. 
### Positional Encoding/Embedding