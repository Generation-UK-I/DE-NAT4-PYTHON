---
title: Data Persistence
---

## Data Persistence

---

### Overview

- Opening and closing files
- Reading data from files
- Writing data to files

---

### Learning Objectives

- Identify the importance of various file handling procedures
- Implement file handling using Python

Notes:
More to just files than reading and writing.

Also cover how Python handles files and how to prevent it from causing errors.

---

### Input and Output

![](img/io.png)<!-- .element: class="centered" -->

---

### I / O

**Input** is the data you feed into your application.

**Output** is the new data that your application produces.

Notes:
Introduce Input and Output.

It covers more than just data persistence.

input() and print() are also input and output.

---

### Types of I / O

- Hardware such as a keyboard and monitor
- User commands and program text on the console
- Files
- Network

Notes:
Ask for other types of I/O, e.g. gaming console controllers, webcams

---

### Saving data permanently

- Any data that is not hardcoded into the application will be lost when the application stops
- Data needs to be saved into a file for it to outlive the application

---

### File Handling

Some of the main things you want to do with a file are:

- Create
- Open
- Read
- Write
- Close

Notes:
What else can we do with files? e.g. delete, change file name

---

### Opening a File

```py
file = open("my_file.txt", "r")
```

`open`: built-in function to create or open a file

`my_file.txt`: path to the file, relative to the program

`"r"`: file access mode (read)

Notes:
There are more file modes we will look at in the next slide.

---

### File Access Mode

A file access mode is a character that specifies the mode in which the file is opened. The default is `r`.

1. `r`: read-only
1. `r+`: both read and write
1. `w`: write-only - overwrites the file
1. `w+`: both read and write - overwrites the file
1. `a`: write-only - appends to the file
1. `a+`: both read and write - appends to the file

More exist but these are the ones we need to know for now.

---

### Reading from a File

```sh
# hello.txt:
Hello!
```

```py
# hello.py:
file = open("hello.txt", "r")
contents = file.read()
print(contents)
```

```sh
# Mac/Unix
$ python3 hello.py
# or on Windows
$ py hello.py
Hello!
```

Notes:
Demonstrate what happens if there is text on more than one line.
Ask the learners to say what happens.

---

### Quiz Time! 🤓

---

I have a file called `file.txt` which has a single line of text - **"hello world!"**. I open the file using `file.open("file.txt", "r+")`. I then immediately close the file. What is now the content of my file?

1. **"hello world!"**
1. **"hello world!"** \n
1. The file is blank
1. The file has been deleted

Answer: `1`<!-- .element: class="fragment" -->

Notes:
This question illustrates that opening with 'r+' does not alter the contents of the file - it just opens an existing file

---

I have a file called `file.txt` which has a single line of text - **"hello world!"**. I open the file using `file.open("file.txt", "w+")`. I then immediately close the file. What is now the content of my file?

1. **"hello world!"**
1. **"hello world!"** \n
1. The file is blank
1. The file has been deleted

Answer: `3`<!-- .element: class="fragment" -->

Notes:
This question illustrates that opening with 'w+' overwrites an existing file - so we have actually created a new file called `file.txt` and written over the old `file.txt`. As we have added no content to the new `file.txt`, the contents will be blank.

Worth also noting here that using 'w+' will create the file if it didn't already exist.

---

I have a file called `file.txt` which has a single line of text - **"hello world!"**. I open the file using `file.open("file.txt", "r+")`. I then run `contents = file.read()` followed by `print(contents)`. What is my output?

1. **"hello world!"**
1. A blank line
1. I will get an error

Answer: `1`<!-- .element: class="fragment" -->

Notes:
This question illustrates that, if you open with 'r+', you open at the beginning of the file. So using `file.read()` will read the first line of content

Answer: `1`<!-- .element: class="fragment" -->

---

I have a file called `file.txt` which has a single line of text - **"hello world!"**. I open the file using `file.open("file.txt", "a+")`. I then run `contents = file.read()` followed by `print(contents)`. What is my output?

1. **"hello world!"**
1. A blank line
1. I will get an error

Answer: `2`<!-- .element: class="fragment" -->

Notes:
This question illustrates that, if you open with 'a+', you open at the end of the file. So using `file.read()` will result in just reading a blank line

---

### Emoji Check:

Do you feel you understand opening files? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content

---

### Reading Line-by-Line

You can read the contents of the file line by line:

```sh
# people.txt
Lisa
John
```

```py
# people.py
file = open("people.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
```

```sh
# Mac/Unix
$ python3 people.py
# or on Windows
$ py people.py
Lisa
John
```

---

### Exercise

1. Create a text file in your text editor and add some names of people on each line
1. Read the names from the file in your application and populate an empty list with the names
1. Print out the list!
1. Did you notice something weird?

Notes:
Do a code-along or ask for a volunteer.

---

### Solution

```py
items = []
file = open("people.txt", 'r')
for line in file.readlines():
    items.append(line)

print(items)
```

```sh
$ python app.py
['Lisa\n', 'John\n', 'Bob\n']
```

Every line in the file is terminated by a newline character '`\n`'. We need to trim that off.

---

### Exercise

Find a way to trim off the newline character from every line you read in your app.

Google is your friend here!

Notes:
Another good way to engage learners for an answer.

---

### Solution

Python has some built-in functions to help us with this:.

`rstrip()` will strip all trailing whitespace characters:

```py
>>> 'test string \n \r\n\n\r \n\n'.rstrip()
'test string'
```

`strip()` will strip off all whitespace characters around any characters:

```py
>>> s = "   \n\r\n  \n  abc   def \n\r\n  \n  "
>>> s.strip()
'abc   def'
```

Notes:
\n is newline.

\r is a return carriage.

---

### Opening Files Safely

Remember our good friend, the `try-except` block?

```py
try:
  file = open('file.txt', 'r')

except FileNotFoundError as fnfe:
  print(f'Unable to open file: {fnfe}')

except Exception as e:
  print(f'An error occurred: {e}'))
```

**Note**: you can chain `except` blocks!

Notes:
An example of catching errors programmatically.

Where else could this be used?

---

### Writing to files

If for example we wrote only these two lines of code:

```py
file = open('people.txt', 'w')
file.write('Susan')
```

...then what could be an issue here?

Notes:
Open the file for the users.

Put a break point on the line after the write, so we've written data but we haven't closed the file off.

It will be blank as the file has not been released and the data is stored in memory.

---

### Always Close Your Files

```py
file = open('people.txt', 'w')
file.write('Susan\n')
file.close()
```

When we close a file, we release our handle on it, and push our changes to disk. This allows other programs to read from or write to the latest version of the document.

Notes:
Repeat the example to show the data is written after a close.

---

### try-except-finally

The `finally` keyword can be used with `try` or `try-except` to execute a block of code, no matter what the outcome is.

```py
file = None

try:
    file = open(filepath, 'w')
    for item in items:
        file.write(item + '\n')

except FileNotFoundError as fnfe:
    print(f'Unable to open file: {fnfe}')

finally:
    if file:
        file.close()
```

Notes:
Usually used to perform operations to release resources handling a file or a database connection.

In this case, we set file to None first and then check if file is not None in the finally block to close it.

The next slide on context managers offers an alternative to having to write this finally block to manually close files.

---

### Emoji Check:

Do you feel you understand writing to and closing files? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content

---

### File context managers

Allows for the previous slide to be made even easier by automatically setting up and tearing down resources. For this we use the `with` keyword in combination with the `open()` function:

```py
items = ['apple', 'berry', 'banana']

try:
  with open(filepath, 'w') as items_file:
    for item in items:
      items_file.write(item + '\n')
except:
  print('Failed to open file')
```

Notes:
Context managers are great to prevent accidentally holding onto resources longer than necessary.

---

### Open - recap

- `open()` is a [built-in function](https://docs.python.org/3/library/functions.html#open) that allows us to open a file and read it's contents, returning us a [file object](https://docs.python.org/3/glossary.html#term-file-object).
- `open()` takes two main arguments:
    - The name of the file
    - The 'file mode' which we discussed earlier (e.g. `'r'`, `'w'`, `'a'`, and more)
- `as` takes whatever object is returned from the `open` function and aliases it to a temporary variable called `file`.

E.g.

```py
with open(filepath, 'w') as file:
    ...
```

---

### Exercise prep

> Instructor to give out the zip file of exercises for `data-persistence`
>
> Everyone please unzip the file

---

### Exercise time

> From the zip, you should have a file `exercises/data-persistence-exercises.md`
>
> Let's all do the exercises included in this file

---

### Emoji Check:

How did the exercises go? Is file handling making more sense now?

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content

---

### Terms and Definitions - recap

**Persistence**: The characteristic of state of a system that outlives the process that created it.

**Exception**: Code that breaks the normal flow of execution and executes a pre-registered exception handler.

**I / O**: The communication between an information processing system, such as a computer, and the outside world, possibly a human or another information processing system.

---

### Overview - recap

- Opening and closing files
- Reading data from files
- Writing data to files

---

### Learning Objectives - recap

- Identify the importance of various file handling procedures
- Implement file handling using Python

---

### Further Reading

- [Exceptions](https://realpython.com/python-exceptions)
- [File Handling](https://www.programiz.com/python-programming/file-operation)

---

### Emoji Check:

On a high level, do you think you understand the main concepts of this session? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content
