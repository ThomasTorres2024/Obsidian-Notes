---
title: Git
tags:
draft: "False"
---
# Git 
Git is a version control system which allows devs to manage different versions and to collaborate on their codebase without conflict. GitHub allows us to host, share, and collaborate on repos, GitHub is built around Git. 

Version control helps teams work together very efficiently, avoids conflicts, and maintain a history of changes to our projects.

Git tracks changes in the codebase, the changes in the files. We can snapshot how our code looked at certain points in time, and how we can roll back our code to another version if necessary. 

---
# Principles of Version Control

Git works off of the idea of branching, we begin at some root node version 1. When we word on the file, we make a branch off of it and we begin to make our changes to the files. We may have a unique branch for our own feature, which differs from the master branch. 

At some later point someone else might need their own feature, so we make our own [[branch]] of the repository. Git allows to then take all of these features and add them to the [[master branch]] or trunk. 

# Benefits of Git 
Git allows us to see how work merges.

For instance, if there's a bug very early on, we can go back to see where the error is, we can go back to before the feature and we have the resolved version. 

Each snapshot in time is known as a version. Different people contribute to changes altogether. We need to be able to deal with merge conflicts. 

Git allows us to develop simultaneously and offside. We can't collaborate together in real time really bad idea. We have our own local versions on our computer, and when they are good, we push them at last. They don't need to pull our changes unless they are ready. 

We can have many versions and branches available at the same time. 

---
# Practices of Version Control

The first thing we do is we clone a repository into the area we are working in. We then start making edits to the files. 

We make changes, and then we commit them with a specific message that is intended to be helpful, what did we add to the program etc. Once a project is on a machine, we can continue to pull stuff from GitHub, and then when they are done we can push them back up.

# Git Setup
If we are logged in, Git is automatically synced. We need to sign in using our Github info. 

First we need to mae a Github repo or to be able to connect to a Github one. We need to use the Command Line Interface CLI, to clone a repo:

```git clone url```

We need to stage our files
```git add . ```
We might make changes to files we don't want to send. If we want all files, then add a  "." . Most commands using ".", we mean all commands. 

```Git
git commit -m "Message"
```

Then we push our command to GIthub:
```
git push
```

We don't add our files until we Commit into Github. We need to make sure we have really good Github commit messages. We want to be specific and note what we actually did. Copilot can write commit messages, and reads through what we changed. 

Commits are very cheap, so do it quite often 