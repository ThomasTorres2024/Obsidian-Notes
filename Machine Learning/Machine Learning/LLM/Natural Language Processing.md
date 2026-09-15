---
title: Natural Language Processing
tags:
  - Machine_Learning
  - LLMs
draft: "False"
---
# Natural Language Processing 
Generally NLP falls into two different two types of text problems, for instance classification, given some text assign a label. 

A common example is the twitter sentiment analysis dataset, where we try to produce one out of many possible results (the dataset likely had multiple labels and we do multinomial stuff). This is an example of __supervised__ learning. 

Another commo task is __Generation__, given a prompt or document, we want to generate new text based on the previous text. 

---
### Tokenization 

The basis of ML requires conversion of input into data. Since text is generally not numeric it needs to be tokenized ([[Tokenization]]) We feed it through a model, and obtain some output as a set of numbers. 

