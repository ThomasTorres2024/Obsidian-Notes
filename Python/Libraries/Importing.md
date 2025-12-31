# Importing Across Different Levels of the Directories 
When importing something from a higher place in the directory, we don't need to worry about pathing, an ```__init__``` file can  be created in a folder and it is treated as a package that we can import from anywhere. 

To execute such a file, we do: 
```
python -m Folder.Filename
```
Where ```-m``` tells the program to start here but not from the root. If we specify a directory without this flag, we launch from that specific directory. 