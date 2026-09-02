# File Read/Write Basics

A Python script demonstrating basic file handling: writing to a file, reading it back, and processing the contents into a new output file.

## What it does
- Creates a sample `names.txt` file with a list of names
- Reads the names back from the file
- Cleans up each name and writes a personalized greeting to `greetings.txt`
- Prints each greeting to the console as it's generated

## How to run
```bash
python file_greetings.py
```
This creates `names.txt` and `greetings.txt` in the same folder when run.

## What I learned
- Using `with open(...)` to safely open and automatically close files
- Writing to a file in `"w"` mode vs. reading in `"r"` mode
- Using `.readlines()` to get each line as a list item
- Using `.strip()` to remove trailing newline characters from file lines
