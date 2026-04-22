---
title: Data Encoding
---

## Data Encoding

---

### Overview

- What is data encoding and why do we do it?
- CSV
- XML
- JSON

---

### Learning Objectives

- To be able to explain what data encoding is and why we do it
- To gain an understanding of what CSV, XML & JSON are

---

### What is data encoding?

**Encoding** is the process of converting data into a specified format.

**Decoding** is the reverse process - to extract information from the converted format.

Common formats:

- JPG, MP4, AVI
- Morse code, Braille
- JSON, XML, CSV
- Analog, Digital

Notes:
The process of converting data into a format required for a number of information processing needs - e.g. transmission, storage.

During session - will learn about some of most common formats that data is stored in - will use in your career!

---

### Why do we encode data?

- Easier to store for computers (humans work with text, computers work with bytes)
- Removes redundancies from data (such as whitespace) so data size decreases
- Smaller data means it's more efficient to store and retrieve data

Notes:
We encode our data as a means of organizing our data.

Not about keeping information secret, but rather about ensuring that the data is able to be properly consumed - we're not encrypting.

---

### CSV (Comma Separated Values)

- A plain text file that uses specific structuring to arrange **tabular** data
- Only contains text data
- Each line of the file is a data record
- Is separated by a _delimiter_ (comma, colon, tab etc.)

```csv
first_name, last_name, age
John,       Smith,     20
Sally,      Bloggs,    30
```

Notes:
Each encoding format has its own rules and special characters (reserved characters used for special purposes) - like human language, where we have grammatical rules and an alphabet.

Excel will allow you to convert from csv to xls (and vice-versa).

---

### CSV - Dealing with commas

What about data that contains a comma?

Well, in that scenario, we quote the data

```csv
first_name, last_name, age, test_scores
John,       Smith,     20,  "80, 76, 92"
Sally,      Bloggs,    30,  "72, 84, 90"
```

Notes:

The quotes prevent the comma inside of the value from being interpreted as a separator

---

### CSV - Dealing with double quotes

How about data that contains a double quote?

We 'escape' the quote by using two of them together

```csv
tv,        size
"Samsung", "24"" TV"
"LG",      "41"" TV"
```

Notes:

Escape characters are special characters that have to be written in a certain way to overcome the limitations of the programming language's syntax.

The compiler knows to translate the double quote to a " within the value instead of the end of the string

---

### CSV in Python

Luckily for us, Python has its own [csv library](https://docs.python.org/3/library/csv.html) to read and write to/from CSV files.

Notes:

A library contains bundles of code that can be used repeatedly in different programs. It makes Python Programming simpler and convenient for the programmer.

---

### CSV - Reading a File

Looking back to the previous module, opening a CSV can be done in a few lines like so:

```py
import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
```

`reader` is a function in the CSV library which returns an object which will iterate over the lines in the given file.

Notes:
with open etc will have been covered in data persistence already

csv.reader will return a `reader object` that will process lines from the given csvfile.

---

### Reading to a Dictionary

We can read our CSV directly into a dictionary using `DictReader`:

```py
import csv
with open('people.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)
```

Output:

```py
{'first_name': 'John', 'last_name': 'Smith', 'age:' 20}
{'first_name': 'Sally', 'last_name': 'Bloggs', 'age:' 30}
```

---

### CSV - Writing to a File

```py
import csv

with open('people.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',')

    writer.writerow(['Joe', 'Bloggs', 40])
    writer.writerow(['Jane', 'Smith', 50])
```

Notes:
'w' will over write the whole file
use 'a' for append new line

---

### Writing from a Dictionary to CSV

```py
with open('people.csv', mode='w') as file:
    fieldnames = ['first_name', 'last_name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({
        'first_name': 'Jan',
        'last_name': 'Smith',
        'age': 60
    })
```

`fieldnames` is required when writing from dictionary to csv.

---

### Emoji Check:

Do you feel you understand CSV encoding format and how to utilise it with Python? Say so if not!

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

### Quiz Time! 🤓

---

**When data is encoded in CSV format, what do we call the character (such as a comma or tab), which is used to separate different fields within a record?**

1. `separator`
1. `limiter`
1. `fielder`
1. `delimiter`

Answer: `4`<!-- .element: class="fragment" -->

---

**You want to import the contents of a CSV file, and view the imported contents in dictionary format. Which of the following lines is likely to appear in your code?**

1. `reader = csv.reader(file, delimiter=',')`
1. `csv_file = csv.DictReader(file)`
1. `writer = csv.writer(file, delimiter=',')`
1. `writer = csv.DictWriter(file, fieldnames=fieldnames)`

Answer: `2`<!-- .element: class="fragment" -->

---

### Exercise - 15 mins

> Distribute exercise file: `exercises/data-encoding-exercises.md`.
>
> Utilise the `exercises/ford_escort.csv` file for the exercise.
>
> Let's all do **"Part 1 - Reading and writing CSV"**, taking a look at working with CSV files.

---

### Emoji Check:

How did you find exercises on using CSV file encoding with Python?

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

### XML

- Stands for 'eXtensible Markup Language'
- Like HTML but for storing data rather than displaying data
- Multidimensional
- A form of semi-structured data

Notes:
Both HTML and XML are XML markup languages that are designed to be both human-readable and machine-readable.

XML documents can be validated against a schema (constrain which elements & attributes may be used & their allowable parent/child relationships).

Semi-structured because data does not reside in fixed fields or records, but does contain elements that can separate data into various hierarchies.

---

### XML Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<people>
  <person>
    <first_name>John</first_name>
    <last_name>Cole</last_name>
    <age>20</age>
  </person>
  <person>
    <first_name>Sally</first_name>
    <last_name>Bloggs</last_name>
    <age>30</age>
  </person>
</people>
```

Notes:
First line is the XML declaration - not mandatory.

Tags - start and end for elements (content shown in between).

Attributes are designed to contain data related to a specific element.

---

### XML Advantages

- Can store highly structured data
- Human readable
- Well understood and used

---

### XML Disadvantages

- 'Wordy' - metadata takes up a lot of space
- Becomes progressively inefficient the more complicated the structure of the data

Notes:
An element links to metadata by referencing each applicable metadata element's ID in inherited attributes.

---

### Emoji Check:

Do you feel you understand XML encoding format? Say so if not!

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

### JSON

- JavaScript Object Notation
- A file format that uses human-readable text to store and transmit data objects
- Can also store semi-structured data like XML
- Also maps to multidimensional data
- Can hold any combination of objects using `{}` and lists using `[]`

Notes:
Lightweight data interchange format.

Easy for humans to read and write.

Easy for machines to parse (taking a big lump and breaking into meaningful chunks) and generate.

Based on Javascript, but completely language independent.

---

### JSON Example - Object

JSON objects start with `{` and end with `}`. JSON files often contain a root object, like so:

```json
{
  "person": {
    "first_name": "John"
  }
}
```

<aside class="notes">
  Key/Value pairs separated by ':'.

  Different pairs separated by ','.

  Key is a string in double quotes.

  Value can be string, boolean, another JSON object, an array or null.

  JSON objects are surrounded in {}.

  Arrays are surrounded in [].
</aside>

---

### JSON Example - List

JSON lists start with `[` and end with `]`. JSON files can contain lists, like so:

```json
[
    {
        "first_name": "John",
        "last_name": "Smith"
    },
    {
        "first_name": "Sally",
        "last_name": "Matthews"
    }
]
```

This would be analogous to the CSV data we saw before. The above would be a valid json file.

<aside class="notes">
  Key/Value pairs separated by ':'.

  Different pairs separated by ','.

  Key is a string in double quotes.

  Value can be string, boolean, another JSON object, an array or null.

  JSON objects are surrounded in {}.

  Arrays are surrounded in [].
</aside>

---

### JSON Example

JSON files can be arbitrarily complex, depending on your needs; This would be analogous to the XML example we saw before:

```json
{
  "people": [
    {
      "person": {
        "first_name": "John"
      }
    },
    {
      "person": {
        "first_name": "Sally"
      }
    }
  ]
}
```

Notes:
Key/Value pairs separated by ':'.

Different pairs separated by ','.

Key is a string in double quotes.

Value can be string, boolean, another JSON object, an array or null.

JSON objects are surrounded in {}.

Arrays are surrounded in [].

---

### JSON Example - Code

```py
import json

person = {
    "name": "Rob",
    "phone": 123456
}
# encode & write to a file
with open('example.json', 'w') as f:
    json.dump(person, f)
```

```py
# read file and decode its content
with open('example.json', 'r') as f:
    my_data = json.load(f)
```

---

### Python objects and their equivalent conversion to JSON

| <span style="color:green">Python</span>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         | <span style="color:red">JSON Equivalent</span>  |
| :---------------- | :--------------: |
| dict              | object          |
| str               | string          |
| list, tuple       | array           |
| int, float        | number          |
| True              | true            |
| False             | false           |
| None              | null            |

---

### JSON Advantages

- Human readable and much less wordy than XML
- Has become a data transfer and storage "standard"

---

### JSON Disadvantages

- JSON isn't as robust a data structure as XML is (although there are third party tools for JSON schema validation).
- Can't use comments

Notes:
JSON has become the standard because its simple design and flexibility makes it easy to read and understand. Also easy to manipulate in the programming language of your choice.

No ability to add comments or attribute tags, which limits ability to annotate data structure or add useful metadata.

---

### Emoji Check:

Do you feel you understand JSON encoding format and how to utilise it with Python? Say so if not!

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

### Quiz Time! 🤓

---

**Which of these is valid JSON?**
<table>
<tr>
<!-- <th>Json 1</th>
<th>Markdown</th> -->
</tr>
<tr>
<td>

```json
// 1
{
  person: {
    first_name : "John"
  }
}

// 2
{
  "person": {
    "first_name" = "John"
  }
}
```

</td>
<td>

```json
// 3
{
  "person": {
    "first_name": "John"
  }
}

// 4
{
  "person": [
    "first_name": ["John"]
  ]
}
```

</td>
</tr>
</table>

Answer: `3`<!-- .element: class="fragment" -->

---

### Exercise - 15 mins

> Continue working with: `exercises/data-encoding-exercises.md`.
>
> Utilise the `exercises/menu_items.json` file for the exercise.
>
> Lets all do **"Part 2 - Reading and writing JSON"**, taking a look at working with JSON files.

---

### Emoji Check:

How did you find exercises on using JSON file encoding with Python?

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

### JSON Validation

Can use tools like https://jsonchecker.com/ to validate JSON format.

- Useful for troubleshooting JSON data
- There are also JSON schema validators out there too

⚠️ Client and sensitive data must NEVER be uploaded to any online tools

Notes:
Client data (whether real or synthetic) must NEVER be uploaded to any online tools (unless approved by the client with sensitive data removed)

---

### Terms and Definitions - recap

**CSV**: A delimited text file that uses commas to separate values.

**XML**: a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.

**JSON**: An open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute-value pairs and array data types (or any other serializable value).

---

### Terms and Definitions - recap

**Encoding**: A system of rules to convert information into another form for communication through a communication channel or storage in a storage medium.

**Parse**: The process of analysing a string of symbols, either in natural language, computer languages or data structures, conforming to the rules of a formal grammar.

---

### Overview - recap

- What is data encoding and why do we do it?
- CSV
- XML
- JSON

---

### Learning Objectives - recap

- To be able to explain what data encoding is and why we do it
- To gain an understanding of what CSV, XML & JSON are

---

### Further Reading

[Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

[Reading and Writing XML Files in Python](https://stackabuse.com/reading-and-writing-xml-files-in-python/)

[Working with JSON Data in Python](https://realpython.com/python-json/)

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
