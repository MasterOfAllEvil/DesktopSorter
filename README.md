# Desktop Sorter
This may use modules that only work on Windows at the present time. This repo has not been looked after for over 6 months and its content may not work.

## What is this?
This repository contains a python program that could be used to sort files on a personal desktop. It currently will not work out of the box.

## How does this work?
The program will start by checking if the configuration file exists, if it does, it will move unsorted files to a folder titled 'Sort', then move the files within based on the rules defined in the config. Otherwise it will create a default configuration file and move the unsorted files to a folder titled 'Sort'.

# Current Rule Definition
As stated above, the configuration file contains all the rules for moving files. If a file does not match a rule, it will remain in the 'Sort' directory. The format of the rules are intended to be simple. The format is as follows:
```
keyword = Destination
suffix* = Destination
*.prefix = Destination
```
## Future Rule Changes
I intend to have a special operation for ignoring files before it moves them. Right now this can be done by adding the file name to the ignoredFiles array in DeskSort.py. I am considering making different implementations of configuration files, but the existing method will regardless. If you have specific type like XML, JSON, or SQLITE; make a feature request and I will look into it.
