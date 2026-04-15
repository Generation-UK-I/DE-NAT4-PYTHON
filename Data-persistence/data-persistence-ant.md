# Persistence

In computing, persistence refers to the ability of data to outlive the process that created it. Without persistence, all data stored in variables, lists, objects, etc., is lost when the program terminates.

- Input is the data you feed into your application (from keyboard, files, network, sensors, etc.)
- Output is the new data that your application produces (results, logs, transformed data)

## Types of I / O

|I/O Type|Examples|Persistence?|
|---|---|---|
|Hardware|Keyboard, mouse, monitor, touchscreen|No|
|Console|input(), print() – user commands, text output|No|
|Files|.txt, .csv, .json, .db, images|Yes (disk)|
|Network|HTTP requests, sockets, APIs|Maybe (remote storage)|

## Saving data permanently

- Any data that is not hardcoded into the application will be lost
when the application stops
- Data needs to be saved into a file for it to outlive the application

Common formats for persisting data include:

- Raw text (.txt) – for logs, configs
- CSV – tabular data
- JSON – structured, human-readable, widely used in APIs
- SQLite / databases – for complex queries and relationship

## File Handling

Some of the main things you want to do with a file are:

|Operation|Function/Method|Description|
|---|---|---|
|Create|`open("file.txt", "x")`|Exclusive creation (fails if exists)|
|Open|`open("file.txt", "r")`|Opens existing file for reading|
|Read|`.read()`, `.readline()`, `.readlines()`|Extract file content|
|Write|`.write()`, `.writelines()`|Add content to file|
|Close|`.close()`|Flush buffers + free system resources|

## Opening a File

```py
file = open("my_file.txt", "r")
```

- `open`: built-in function to return a file object
- `my_file.txt`: path to the file, relative to the current working directory
- `r`: file access mode (read-only)

## File Access Mode

A file access mode is a character that specifies the mode in which the
file is opened. The default is `r`.

- `r`: read-only
- `r+`: both read and write - overwrites the content
- `w`: write-only - overwrites the file
- `w+`: both read and write - overwrites the file
- `a`: write-only - appends to the file
- `a+`: both read and write - appends to the file

More exist but these are the ones we need to know for now.

## Working with Files Lab

### Reading from files

1. Create `data.txt` containing:

```text
Line 1: Apples
Line 2: Bananas
Line 3: Cherries
```

2. Read entire file as one string:

```py
file = open("data.txt", "r")
# Read entire file as one string
contents = file.read() 
print(contents)

# Expected Output:
Line 1: Apples
Line 2: Bananas
Line 3: Cherries
```

3. Read line-by-line (memory efficient for large files)

```py
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() removes \n
```

4. Read all lines into a list:

```py
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

5. Read a fixed number of characters:

```py
with open("data.txt", "r") as f:
    first_10_chars = f.read(10)
    print(first_10_chars)
```

### Writing to files

6. Overwrite entire file (w mode):

```py
with open("output.txt", "w") as f: # File will be created if it doesn't exist
    f.write("First line\n")
    f.write("Second line\n")
    # Check new file to verify
```

7. Append to existing file (a mode):

```py
with open("log.txt", "a") as f:
    f.write("New log entry at end\n") # Run script several times to append additional lines.
    # Check new file to verify
```

8. Write multiple lines at once:

```py
lines = ["alpha\n", "beta\n", "gamma\n"]
with open("list.txt", "w") as f:
    f.writelines(lines)
    # Check new file to verify
```

### Always Close Your Files

When we close a file, we release our handle on it, and push our changes to disk. This allows other programs to read from or write to the latest version of the document. If you don't close:

- Data may remain in buffer (not actually written to disk), so data maybe lost in the case of a crash
- Other programs may be locked out (especially on Windows)

When you use the `file.close()` method:

- Flush internal buffers - force write to disk
- OS can reclaim resource
- Make file available to other processes

**Bad practice (works but risky):**

```py
file = open('people.txt', 'w') 
file.write('Susan\n') 
file.close() # If app crashes on line 2, line 3 wont run, file may remain open.
```

**Good practice:**

```py
f = open("test.txt", "w")
try:
    f.write("Hello")
finally:
    f.close()  # always executes
```

**Using try-except-finally:**

The finally keyword can be used with try or try-except to execute a block of code, no matter what the outcome is.

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

### File context managers

Allows for the previous example to be made even easier by automatically setting up and tearing down resources. For this we use the with keyword in combination with the open() function:

```py
items = ['apple', 'berry', 'banana'] 
 
try: 
  with open(filepath, 'w') as items_file: 
    for item in items: 
      items_file.write(item + '\n') 
except: 
  print('Failed to open file')
```

## Data Persistence Lab

Follow the below instructions to demonstrate and practice reading and writing to external files.

1. Create a working directory for the lab and open it in VSCode:

```bash
mydir data-persistence-lab
```

2. Create a new Python file called `diary.py`, add the following code into it.

```py
# Creates and writes to a file
with open("diary.txt", "w") as file:
    file.write("Today I learned about file persistence!\n")

print("Entry saved!")
```

- `open("diary.txt", "w")`: Creates a file called diary.txt
- `"w"`: means write mode (creates/overwrites file)
- `with`: automatically closes the file when done
- `\n`: adds a new line

3. Manually verify by viewing the newly created `diary.txt` file.,

4. Read back what you wrote:

```py
# Read the entire file
with open("diary.txt", "r") as file:
    content = file.read()

print("My diary contains:")
print(content)

# Expected output:
# My diary contains:
# Today I learned about file persistence!
```

5. The problem with `"w"` mode is it overwrites everything::

```py
# First write
with open("diary.txt", "w") as file:
    file.write("First entry\n")

# Second write - This overwrites!
with open("diary.txt", "w") as file:
    file.write("Second entry\n")

# Read it back
with open("diary.txt", "r") as file:
    print(file.read())
```

6. Use `"a"` (append) mode:

```py
# Clear the file first
with open("diary.txt", "w") as file:
    file.write("")  # Empty the file

# Add first entry
with open("diary.txt", "a") as file:
    file.write("First entry\n")

# Add second entry - this ADDS to the file
with open("diary.txt", "a") as file:
    file.write("Second entry\n")

# Read it back
with open("diary.txt", "r") as file:
    print("After appending:")
    print(file.read())
```

---

The operations and functions in this guide will be particularly useful for Sprint 3 of your mini-project; However, if you're struggling, an additional sample diary app has been provided which may provide hints for your own development tasks. [Review it here](./data-persistence-sample-app.md).
