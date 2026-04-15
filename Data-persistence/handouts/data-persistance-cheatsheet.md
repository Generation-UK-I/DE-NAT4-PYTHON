# Python Data Persistence cheatsheet

## Access Modes

1. `r`: read-only
1. `r+`: both read and write
1. `w`: write-only - overwrites the file
1. `w+`: both read and write - overwrites the file
1. `a`: write-only - appends to the file
1. `a+`: both read and write - appends to the file

## Opening a file

`open(file_name, *access_mode)` opens a file

```python
file = open("my_file.txt", "r")

```

## Reading a file

`read()` reads a files contents
`readlines()` reads the contents as a list (each line is a string in the list)

```python
file = open("hello.txt", "r")
contents = file.read()
print(contents)

file = open("people.txt", "r")
lines = file.readlines()
for line in line:
    print(line) 

```

## Writing a file

`write()` writes to the file with no accessor mode, will write at the end of the file.

```py
file = open('people.txt', 'w')
file.write('Susan')
```

## Closing a file

`close()`

```python
file = open('people.txt', 'w')
file.write('Susan\n')
file.close()
```

## Context Manager

`with` python keyword for creating a context manager

```python
items = ['apple', 'grapes', 'orange', 'banana']
with open('people.txt', 'w') as items_file:
    for item in items:
      items_file.write(item + '\n')
```
