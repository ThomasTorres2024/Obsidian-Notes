---
title: Inode
tags:
  - Operating_Systems
draft: "False"
---
# Inodes 
Inodes essentially  contain all of the meta data for a [[File]], however it does not include the file's name. In [[Unix]] the ls command knows how to access the name of the file in the directory and its respective inode number as a sort of key map pair ([[Hashing]]). We can get both directly by doing ls -i.  

From the file name we can get the file meta data, and from the file name we can get the file contents. But, we cannot go from the meta data back to the fiile name. 

Actual meta data captured in the file system versus the meta data available may differ. In such a case, this system will default to the contents of the inode. 
#### Meta Data Captured
Depending upon the protocol for access metadata, the following tend to be stored and can be accessed with the "gstat file_name.txt" or "stat file_name.txt" commands:

* Size 
* Blocks
* IO Block
* File Type
* Device
* Inode
* Links
* Access Permissions
* Access Date
* Modify Date
* Change Date 
* Birth Date

## [[Hardlinks]]
If two files are hard linked, when we examine their meta data we will see that they have at least 2 links and furthermore point to the same inode and will have the same key pair link. 
## [[Symlink]]
If we are to run gstat on two different files where one is a symbolic link of the other, the two files will __not__ share the same inode. This is because the symlink is a completely different file type, and represent different file types. 