gcc -wall -std=c11 dir/cfile.c -o name 
The -o is an option flag. We output the file to the current directory we are in. If we want to put the file in another file inside of our current directory, we would specify a location, for example:

```
gcc -wall -std=c11 dir/cfile.c -o scripts/name 
```

If we are in a folder, and we want to move back up, we would add two dots in front our current directory to navigate out of it, and back into the main directory

```gcc -wall -std=c11 ../dir/cfile.c -o scripts/name ```