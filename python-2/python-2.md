---
title: Python 2
---

## Python 2

---

### Overview

- Loops
- Dictionaries
- Exceptions
- Functions
- Googling!

Notes:

Mentions the layout for the day(s) at this point.

- We have 3 teaching blocks for python 2 today so we will aim to cover one topic in each teaching block. Loops, dictionaries and exceptions

---

### Learning Objectives

- Understand and implement loops
- Understand and implement dictionaries
- Understand what exceptions are and how to handle them
- Understand and implement functions
- Understand good Googling practices

---

## Loops

![](img/loop.png)<!-- .element: class="centered" -->

Notes:
Could ask "Does anyone have any ideas about what loops are or how they might be useful in python?"
(Try to get engagement and would help gauge any pre-requisite knowledge)

---

### Loops

- Programming construct that allow us to **iterate** over a sequence of values
- Execute the same block of code a number of times
- Python has two built-in loop commands: _for_ and _while_

Notes:
Iterate meaning to repeat a process in order to generate an outcome.

---

### For Loops

Used when you want to repeat a block of code a **fixed** number of times:

```py
for x in [0,1,2]:
  print(f'current number is {x}')

# Output
# current number is 0
# current number is 1
# current number is 2
```

Notes:
Some modifications for this example when demoing in vs code are:

- add more numbers to the list
- change x to another name
- iterate over a string instead

---

### While Loops

We can execute a block of code as long as a condition is _true_:

```py
i = 0

while i < 5:
  print(i)
  i += 1

# Output will be 0, 1, 2, 3, 4
```

Notes:
Ask someone why it stops printing after 4.

It should be noted that the constructs such as continue, break and nesting can still be used with a while loop when shown in the next few slides.

---

### Emoji Check:

Do you feel you understand Loops? Say so if not!

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

### Range

```py
for x in range(0, 3):
  print(f'current number is {x}')
```

Returns a sequence of numbers in the specified range, which increments by 1 each time (by default).

Notes:
Ask the class, why does it not print 3?

It's important to note that range generates values between the arguments, but not inclusive of the second argument. Value generated will be one less.

Demonstrate this.

These are helpful if you want to loop over a block of code a specified number of times.

You can also increment by more than 1 but don't need to worry about that right now.

---

### Nested Loops

You can _nest_ as many loops inside one another as you like:

```py
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjectives:
  for fruit in fruits:
    print(adj, fruit)
```

Notes:
Again ask the class what will happen here.

It's important to note that while you can nest as many as you like, it's good practise to limit that amount as the time it takes to execute the entire thing will take exponentially longer with each nested loop.

You'll also notice that we don't use range() here, if we use the in <-list-> the default is to loop through the entire list.

---

### Break Keyword

With the _break_ keyword we can stop the loop before it has looped through all of the items

```py
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)
  if fruit == "banana":
    break
```

Notes:
The break keyword is used to break out a for loop, or a while loop.

Ask the class what will happen here.

---

### Continue Keyword

With the _continue_ keyword we can end the current iteration of the loop early and move to the next

```py
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  if fruit == "banana":
    continue
  print(fruit)
```

Notes:
Ask the class what will happen here.

---

### Emoji Check:

Do you feel you can use Loop keywords now? Say so if not!

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

### For Else

You can also use the keyword _else_ to execute code after the loop is finished

```py
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

Notes:
Only really useful when used in conjunction with a break statement as the else block will NOT be executed if the loop is stopped by a break statement.

Ask the class what will be printed out.

You might notice that range() has only taken one argument, rather than two in previous slides.

When the range() function takes one argument the default starting index position is 0, the argument then specifies which position to stop iterating. In this case index position 6.

Why `for-else` exists, as opposed to just putting the `else:` code after the loop?

Answer: can `break;` out of the loop to prevent the `else:` from executing. Only useful in conjunction with `break` e.g:

```py
some_list = ["item", "thing", "required"]

for i in some_list:
    if i == "required":
        break # We found what we were looking for
else:
    raise ValueError("Required not found.")

print("Required was found.")
```

https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops

---

### Quiz Time! 🤓

---

**Given the below code, what are the range of values that will be printed?**

```py
for x in range(0, 5):
  print (x)
```

1. `0-4`
1. `0-5`
1. `1-4`
1. `1-5`

Answer: `1`<!-- .element: class="fragment" -->

---

**Given the below code, what are the range of values that will be printed?**

```py
i = 0
while i < 5:
  i += 1
  print(i)
```

1. `0-5`
1. `1-5`
1. `0-4`
1. `1-4`

Answer: `2`<!-- .element: class="fragment" -->

---

### Exercise prep

> Instructor to give out the zip file of exercises for `python-2`
>
> Everyone please unzip the file

---

### Exercise time

> From the zip, you should have a file `exercises/loop-exercises.md`
>
> Let's all do the exercises included in this file

---

### Emoji Check:

How did the exercises go? Are Loops making more sense now?

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

## Dictionaries

![](img/dictionary.png)<!-- .element: class="centered" -->

---

### Dictionaries

- A collection of values, similar to a list
- Used to store values as key-value pairs

```py
car = {
  # key    # value
  'make': 'Jaguar',
  'model': 'XF',
  'year' : 2019,
  'isNew': False
}

print (car['make'], car['year'])
# Jaguar, 2019
```

Notes:

Copy paste into chat:

Dictionary: A dictionary is a collection which is ordered* (Only for Python version 3.7 and above), changeable and do not allow duplicates.

Ask learners how they THINK a dictionary would be different to a list, how they would look up in one versus the other.

Python dictionaries work pretty much like a regular dictionary: you use a word (key) to lookup the meaning (value). Programmatic dictionaries come with a few more quirks but the comparison is mostly sound.

Make sure to denote the fact that you use x['y'] to access a key's value.

---

### Dictionary Keys & Values

#### Keys

We use keys to unlock values, the most common key types are strings and numbers:

```py
d = {
  'a': 'b',
  1: 'c',
  0.75: 'test',
  'd': [ 1, 2, 3 ],
  'e': { 'f': 'g' }
}
```

#### Values

Values can be pretty much anything! They can even be another dictionary.

Notes:
Keys must only be immutable (technically hash-able - they must have `__hash__` method attached) which means you can use tuples and functions (for example) as dictionary key, but not other dictionaries or lists.

---

### Dictionary Exceptions

If you try to access a value with a key that does not exist, an error will be raised

```py
d = {'a': 1, 'b': 2}
>>> d['c']

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'
```

---

### Dictionary Mutations

Add an entry:

```py
car['colour'] = 'Red'
```

Update an entry:

```py
car['colour'] = 'Blue'
```

Delete an entry:

```py
del car['colour']
```

---

### Emoji Check:

Do you feel you understand Dictionaries? Say so if not!

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

### Built-In Functions

Python dictionaries have some built-in functions to help us work with them.

> Can you think of any examples?

Notes:
We can mention here that in this case, the functions associated to dictionaries would be called methods.

---

### Built-In Functions

What might this do?

```py
>>> car.get(x)
```

Returns the value for a key if it exists.<!-- .element: class="fragment" -->

Notes:

Ask the learners what they think this will do.

N.B The get() function will either return:

1. The value for the specified key if key is in dictionary
1. 'None' if the key is not found and value is not specified, more robust than dict[x], no KeyError
1. The optional second parameter value if the key is not found and value is specified. ie you provide a default value if it's missing in the dict

---

How about this code?

```py
>>> car.items()
```

Returns a list of the key-value pairs.<!-- .element: class="fragment" -->

Notes:

Ask the learners what they think this will do.

`items()` is useful to get a list to iterate

---

And this one?

```py
>>> car.clear()
```

Empties a dictionary<!-- .element: class="fragment" -->

Notes:

Ask the learners what they think this will do.

---

### Built-In Functions

```py
>>> car.keys()
```

Returns a list of keys<!-- .element: class="fragment" -->

```py
>>> car.values()
```

Returns a list of values<!-- .element: class="fragment" -->

---

### Other useful things

```py
# check if key exists
>>> 'colour' in car
True

# count how many keys there are
>>> len(car)
6

```

---

### Quiz Time! 🤓

**Given the below code, how would you access the _value_ of the fruit's colour?**

```py
fruit = {
  'type': 'apple',
  'color': 'green'
}
```

1. `fruit['type']`
1. `color['green']`
1. `fruit['color']`
1. `fruit['color']['green']`

Answer: `3`<!-- .element: class="fragment" -->

---

### Dictionary vs List

✅ Both mutable

✅ Both dynamic (can change in size)

✅ Can be nested

❌ List elements are accessed by position in list (indexed), dictionary elements are accessed by their keys

Notes:
Nested: List can contain another list, dictionary can contain another dictionary. A dictionary can contain a list and vice versa.

What do you think will happen if we try to access the dictionary using an index number?
Answer: KeyError

---

### Dictionary vs List

When might you use a dictionary versus a list?

Scenario: You want to store the first name of every student in a class

- List<!-- .element: class="fragment" -->

Scenario: You need to store detailed information about a specific vehicle, including make, model and colour<!-- .element: class="fragment" -->

- Dictionary<!-- .element: class="fragment" -->

Scenario: You need to store information about a number of different vehicles, and be able to look up each of those sets of information using the vehicle's number-plate<!-- .element: class="fragment" -->

- Dictionary of dictionaries<!-- .element: class="fragment" -->

Notes:
Student names:

- List probably sufficient because it's single-value items
- List allows duplicate values (More than one person may be called 'John' for example)
- How else could we handle duplicate values? (dictionary of Name:Count)

Detailed info:

- Why not a list? Because it is hard to access the info without a key into it, it would require searching the list for an item with particular values

List of detailed info:

- Why not a LIST of dictionaries? Could be but we'd need to search through the whole list to find the information
- Ask: Would it be possible to use driver name as a good way to index into the vehicle information? Is there any problem with this?

```py
  car1 = {
    'numberplate' : 'CP69 MAA',
    'brand': 'Jaguar',
    'model': 'XF',
    'color': 'Silver'
  }

  car2 = {
    'numberplate' : 'MA59 AVD',
    'brand': 'Ford',
    'model': 'Mustang',
    'colour': 'Red'
  }

  cars = {
    'CP69 MAA' : car1,
    'MA59 AVD' : car2
  }
```

- Lists are ordered sets of objects (ordered by index, not alphabetically though they can be sorted) whereas dictionaries are unordered sets.
- Items in dictionaries are accessed via keys and not via their position.

So entirely depends on the use-case.
If we need ordering, definitely lists

- Ordered by insertion order, not by sorted order (but you can sort a list, you can't sort a dictionary)

If we need to store duplicate values, also list (keys can't be duplicated)
If we want to look-up values by their key then dict

---

### Emoji Check:

Do you feel you understand Dictionaries vs Lists? Say so if not!

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

### Exercise time

> From the same Exercises zip, you should have a file `exercises/dictionary-exercises.md`
>
> Let's all do the exercises included in this file

---

### Emoji Check:

How did the exercises go? Are Dictionaries making more sense now?

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

## Exceptions

![](data-persistence/img/exception.png)<!-- .element: class="centered" -->

---

### Example

```py
>>> numbers = [1,3,5,7,9]
>>> numbers[5]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

What happened?

Notes:
Ask the learners if they understand what the problem was.

---

### Exceptions

An **exception** is an error from which your application cannot recover.

Exceptions are thrown when something unexpected happens in your program.

> Can you think of any examples?

Notes:
What exceptions can the learners think of?

Examples in the following slides...

---

### Types of Exceptions

Trying to change the type of some variable when it doesn't make sense, e.g. casting a string to a integer

```py
>>> '2' + 2

TypeError: can only concatenate str (not "int") to str
```

Getting the sixth item from a list that only has 5 items

```py
>>> numbers = [1,3,5,7,9]
>>> numbers[5]

IndexError: list index out of range
```

---

### Types of Exceptions

Opening a file that doesn't exist

```py
>>> f = open('does_not_exist.py')

FileNotFoundError:
  [Errno 2] No such file or directory: 'does_not_exist.py'
```

Dividing by zero:

```py
>>> 1 / 0

ZeroDivisionError: division by zero
```

And more!

---

### Handling Exceptions

Python has a built-in construct called `try-except` to handle exceptions.

The code we would normally run is placed inside the `try` block.

If an exception is raised inside the block, it immediately jumped to the `except` block to handle the exception.

```py
try:
  x = 1 / 0
except:
  print("You can't do that!")
  print("We can still run the program after this though")

...
# More code carries on
```

Notes:

Can mention here that the except block can be modified to only catch specific exceptions, e.g.

```py
try:
x = 1 / 0
except ZeroDivisionError:
print("You can't do that!")
print("We can still run the program after this though")
```

This will prevent us from accidentally catching unexpected exceptions.

---

### Emoji Check:

Do you feel you understand Exceptions? Say so if not!

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

### A few pointers about exceptions

1. Minimise the amount of code you put in your exceptions, i.e. no try-except around your entire app, _just in case_.
1. Exceptions should be used **sparingly**, as they are no substitute for adequate input handling
1. When handling an exception, print out helpful messages explaining what happened and why in detail

Notes:

1. You want to be as specific as possible with the type of exception you need to handle.
2. Input handling refers to checking the inputs of a function or passed to the program as args.
3. Helps us debug programs quicker!

---

### Syntax errors vs Exceptions

Syntax errors occur when Python detects a statement has been written incorrectly:

```py
>>> print('hello'))
  File "<stdin>", line 1
    print('hello'))
                  ^
SyntaxError: unmatched ')'
```

These are different to exceptions. Exceptions happen when syntactically correct code fails.

Other types of 'Error' ?

Notes:

Can mention Logic Errors here - a mistake in the logic in the code that won't raise an exception or prevent it running, but will cause the code to give us the wrong output.

---

### Quiz Time! 🤓

---

**True or false: this code snippet will raise an exception.**

```py
stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    for x in stuff:
        print (stuff[x + 1])
except:
    print ('Something went wrong!')
```

Answer: `True`<!-- .element: class="fragment" -->

---

### Exceptions as Variables

Inside the `except` block, you can contain the details of the exception in a variable:

```py
try:
  x = 1 / 0
except Exception as e:
  print(e)
```

```sh
$ division by zero
```

---

### Emoji Check:

Do you feel you could use Exceptions? Say so if not!

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

### Exercise

1. Write a small program that will purposefully throw an exception, causing your program to crash
1. Update it to include exception handling with a `try-except` block
1. Update it to print the error generated by the exception
1. Add an additional code path in your application which can generate another exception of of a different type and handle it separately if it occurs
1. Add functionality to print out the stack trace for an exception to see where in code it occurs (Hint: `traceback`)

Notes:
This one can be a fun code-along or ask a learner to show their code.

---

### Emoji Check:

How did the exercises go? Are Exceptions making more sense now?

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

## Functions

![](img/function.png)<!-- .element: class="centered" -->

---

### Functions

- Allow you to break up your program into a number of **reusable** chunks
- Functions work on variables that you pass it, which are known as arguments
- A function may take zero or more arguments
- Defined by the _def_ keyword

```py
# With arguments
def add_numbers(a, b):
  return a + b

# Without arguments
def get_name():
  return 'Alice'
```

---

### Return Statement

You may have noticed the _return_ keyword:

```py
def get_name():
  return 'Alice'

name = get_name()
print(name) # Alice
```

- A function always has the option to return a value, but it doesn't have to return anything
- You can either use the `return` keyword without a value, or omit entirely

Notes:
If you use `return` without a value the program returns a `none` value and continues to execute.

---

### Calling a Function

Simply use the name of the function!

```py
def add_numbers(a, b):
  print (a + b)

add_numbers(1, 2)
# 3
```

---

### Function Arguments

- Information can be passed to a function as _arguments_
- Arguments are the variable names specified after the function name
- You can have as many as you need

```py
def my_function(a, b, c):
  print(a, b, c)

my_function('hello', 'world', '!')
# hello world !
```

Notes:
These arguments are also known as positional arguments.
Again it's important to note that while you can have as many arguments as you want, it's always good practice to limit the amount you use.

---

### Emoji Check:

Do you feel you understand Functions? Say so if not!

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

### Default Arguments

- You can provide a default value for an argument to make it optional
- Also known as **keyword arguments**

```py
def my_function(a, b, c='!'):
  print(a, b, c)

my_function('hello', 'world')
# hello world !

my_function('hello', 'world', '?')
# hello world ?
```

Notes:
The order of the arguments matters here - keyword arguments must come after normal/required arguments

---

### Quiz Time! 🤓

---

**Given the below code, how would you call this function and store the result in a variable?**

```py
def add_numbers(a, b, c):
    return a + b + c
```

1. `add_numbers()`
1. `add_numbers(1, 2, 3)`
1. `result = add_numbers()`
1. `result = add_numbers(1, 2, 3)`

Answer: `4`<!-- .element: class="fragment" -->

---

### Named Arguments

You can also use the names of arguments when calling a function:

```py
def fave_food(person, food):
  print(f"{person}'s favourite food is {food}")

fave_food(food = "Curry", person = "Mark")
```

Note how we can specify these in any order!

> Named arguments are also known as keyword arguments.

---

### Keyword-only Arguments

It can be enforced that an argument should be passed as keyword-only:

```py
def greet(name, *, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet(name="Alice") # Hello, Alice!

greet(name="Alice", greeting="Hi") # Hi, Alice!

greet("Alice", "Hi") # TypeError
```

> All arguments after * must be passed as keyword or an error will be produced

Notes:
This can be useful in cases where certain arguments being passed must be specified.

Last line in example greet("Alice", "Hi") produces an error as greeting has not been passed as a keyword argument

---

### Positional-only Arguments

It can be enforced that an argument should be not be passed with a keyword:

```py
def rectangle_area(length, width, /):
    print(length * width)

rectangle_area(10, 20) #200

rectangle_area(width=20, length=10) #TypeError
```

> All arguments before / must be passed as a standard argument or an error will be produced

Notes:
This can be useful for when order of arguments matters in a function.

---

### Arbitrary Arguments

You can create a function with any number of arguments using `*args`. Effectively, `*args` creates a list of arguments for you inside the function:

```py
def my_function(*people):
  for person in people:
    print(person)

my_function("Alice", "Bob", "John")
```

> *args are useful when you don't know how many arguments will be passed.

Notes:
E.g. the print function might receive varying amounts of arguments at different times e.g.
print(1, 2, 3) could be print(1, 2, 3, 4, 5).

---

### Arbitrary Named Arguments

There is a similar keyword `**kwargs` which accepts _named_ arguments, It stands for "key Word Arguments".

`**kwargs` creates a dictionary of key-value arguments inside the function:

```py
def describe(**kwargs):
  # Iterating over the Python kwargs dictionary
  for key_value_pair in kwargs.items():
    print(key_value_pair)

describe(name="Dora", type="Cat", hungry="Always")
```

Notes:
`**kwargs` or Key Word Arguments creates a dictonary of keyword arguments passed.

Similar to `*args`, `**kwargs` are useful when you don't know how many key word arguments you will be passed.

**kwargs have the added advantage that the arguments are named using key words.

E.g. configuring a database connection to override any defaults. For example, if there is a default database name of `Development-DB`, you might add a kwarg of `db-name = Cafe_Database` where it is a `**kwarg` in the function call.

---

### Ordering of Arguments

Ordering of arguments is important in Python. The correct order is:

1. Standard arguments
2. `*args` arguments
3. `**kwargs` arguments

```py
def my_function(a, b, *args, **kwargs)
```

```py
def my_function(a, b, c='default', *args, **kwargs)
```

Notes:
Other arguments not mentioned here to keep it simple.

There's other forms of arguments such as positional-only and keyword-only arguments which are similar to the default/keyword arguments. Positional-only arguments go after the standard arguments, keyword-only arguments go between *args and **kwargs, but these haven't been mentioned here to keep it more straightforward.

Full order of arguments:

```py
#Standard | positional only | *args | keyword-only | **kwargs
def my_function(name, /,  *arg, greeting="Hello", punctuation=".", **kwargs):
    print(name)
    print(arg)
    print(greeting)
    print(kwargs)
    print(punctuation)

my_function("Alice", "anything", "even more", greeting="greet", meta_data="random")
```

---

### Emoji Check:

Do you feel you understand Function Arguments? Say so if not!

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

### Exercise time

> From the same Exercises zip, you should have a file `exercises/function-exercises.md`
>
> Let's all do the exercises included in this file
>
> If you finish early, there's also two bonus exercises at the end of the file

---

### Emoji Check:

How did the exercises go? Are Functions making more sense now?

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

## Googling

---

### Google-fu (or your search engine of choice)

Learning how to learn and adapt is just as important as remembering everything we're throwing at you here!

The best tool for this is Google, and knowing what to Google and how to interpret results is valuable

Notes:
While there are jokes about software engineering just being "Googling stuff", doing so in the right way is difficult

---

### Worked example

I, as a developer, want to know how to remove the item `Tractor` from the following list, but I don't know how

```py
luxury_cars = ['Ferrari', 'Lamborghini', 'Tractor', 'Porsche']
```

...what search terms might we use to get useful results?

Notes:
Instructor demonstration: Show how you would Google removing an item from a list in Python, and how you would interpret the result - can potentially ask a learner to demonstrate on this or the next one. Get people participating with suggestions! Add "python3..." to the start of the search and so on.

---

### Errors!

Knowing how to Google is especially important for errors! Let's say I've run the following code and got the following error output:

```py
func = "ThisIsNotAFunc"
print(func())
```

```py
TypeError: 'str' object is not callable
```

...what search terms might we use to get useful results?

Notes:
Again, go through how you might solve this issue, focusing more on interpreting wordy results here. Add "python3..." to the start of the search and so on.

---

### Emoji Check:

How do you feel about googling errors? Are you able to google and debug errors more efficiently?

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

**Loop**: A programming construct that allow us to iterate over a sequence of values

**Dictionary**: A collection of key-value pairs, where the keys are _usually_ text, used to access the values

**Function**: Allow you to break up your program into a number of reusable chunks, with each performing a particular task

**Argument**: A value that must be provided to the function

**Iteration**: The repetition of a process in order to generate an outcome; It is used both to mean iterating over a list to do calculations, and iterating our code (doing improvements)

---

### Further Reading

[Loops](https://www.learnpython.org/en/Loops)

[Dictionaries](https://www.learnpython.org/en/Dictionaries)

[Functions](https://www.w3schools.com/python/python_functions.asp)

[*args and **kwargs explained](https://realpython.com/python-kwargs-and-args/)

---

### Overview - recap

- Loops
- Dictionaries
- Exceptions
- Functions
- Googling!

---

### Learning Objectives - recap

- Understand and implement loops
- Understand and implement dictionaries
- Understand what exceptions are and how to handle them
- Understand and implement functions
- Understand good Googling practices

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
