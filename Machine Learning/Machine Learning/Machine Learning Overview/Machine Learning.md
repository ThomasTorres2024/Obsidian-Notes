---
title: Machine Learning
tags:
draft: "false"
---
# Definition
Machine learning consists of programs that improve with experience, or with data.

Artificial intelligence $\supseteq$ Machine learning. Deep learning is a subset of machine learning, and generative AI is a subset of deep learning, all LLM type models, image generation etc. 

### Notes and General History 
[[Support Vector Machines]] are generally outdated, but we need to be able to use them and understand what they are. 

[[Neural Nets]] significantly outcompeted other traditional methods in data science around 2012, pretty much all computer vision goes to neural nets and deep learning for some time. 

[[GANS]], generative networks came out a couple years later, which would try and distinguish generated images from images that are not real. These things are outdated, as well. 

We have RNNs and LSTMs, [[Residual Nets]], which is something we will cover, still important, [[Gradients]] tend to get smaller and smaller until they are not useful. 

In 2022 we get to [[Stable Diffusion]], and being able to generate images.

In 2023 we get generative AI and LLMs generally. There is a good chance that many of the techniques here will not be valid, but we need to understand things like [[loss functions]] and the very fundamentals of AI. Things move absurdly fast, and many things are no longer relevant. 

---
# What actually is ML?
Generally computing algorithms that perform a task given some amount of data/experience, and a metric, and then the ability to improve our score. 

There are many performance measures, and these things generally last very long. 

Being able to label images was very important for initially driving advancement in AI. 

---
# Machine Learning Applications

In media, we like to create recommendation algorithms, very important for advertising, as of 2025 we tend to use the same techniques as in the last 3-4 years. 

We have autonomous vehicles as well, way too many issues here.

We also have security and defense, like face detection, video surveillance, an satellite imagery. 

Medicine and biology is a huge area as well. 

There's a lot of sports betting technology as well z

---
# Major Paradigms in ML 
1. Supervised Learning, we have labeled data 
2. Unsupervised Learning, finding patterns in unlabeled data 
3. Semi-Supervise Learning, learn from labeled and unlabeled data, small amount of really well labeled data and really poorly labeled data, how do we alternate based on what we learn on
4. Reinforcement Learning, mostly used in robotics, increasingly used in other areas 
5. Transfer learning, taking data from one area and using it somewhere else, like we have a tree neural network, can we use that network to ID bushes? 
6. Zero/Few Shot learning, how do we learn from very few examples? Very hard to make work. We have a lot of data makes things easy, but here it's a lot harder. Being able to do something with little data is very important 
7. Generative Modeling/Learning, stable diffusion llms, etc 