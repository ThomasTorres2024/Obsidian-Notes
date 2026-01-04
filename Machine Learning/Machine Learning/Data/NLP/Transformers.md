---
title:
tags:
draft: "false"
---
# Transformers 

Transformers begin by vectorizing all words in a sentence. This is known as tokenization. We need to be able to know the position of each word within the sequence in order to handle it. We need to incorporate positional information in these vectors. 

We want our transformer to satisfy the following conditions, each unique position in our sentence should have a different value. Our algorithm should also produce some consistent underlying result and thereby be deterministic. We also need to be able to estimate distance between tokens. Models also need to be generalizable, and should work on sequences of words longer than the ones it is trained on and has encountered before. 

Positional encoding satisfies all of these conditions. 
### Positional Encoding/Embedding