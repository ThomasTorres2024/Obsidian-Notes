---
title: Symlink
tags:
  - Operating_Systems
draft: "False"
---
# Symlink

Short for symbolic link. Symlinks are a special [[File]] type that point to another existing file. 

If two [[Symlink]]s point to each other, the contents of each file will not be accessible namely the __ELOOP__ error, where there are "too many symbolic links". Note that this error isn't necessarily always caused by this as it can occuur iif there are too many symbolic links in general.