# Introduction to Python

## What is Python?

Python is a high-level programming language, which is accessible for beginners, but very powerful and flexible through the use of plugin modules, making it very popular for working with AI models, data science applications, and many other areas.

Programming is the act of writing commands i.e. lines of code, which instruct the computer to carry out an operation. Computers operate on binary (1s and 0s), and of course, humans don't speak binary, therefore we need abstraction layers to translate instructions we provide with Python commands, into binary operations the computer can run; we also rely upon translation layers in the other direction, to take binary output, and turn it into something humans can understand.

>Python is an interpreted language, which means when you run it the Python 'interpreter' reads each line of code, in sequence, and translates the code into operations that the computer can process. By comparison, a compiled language does all of the translation in advance before you run your code. Apps developed in a compiled language can often run faster and use less resources, but they can also be more challenging during development, because compiling can be a slow process.

## Programming in Python

There are several paradigms for how you can approach writing code:

- Procedural: code which is executed, in order, sequentially.
- Event-Driven: code which is executed in response to events; these can be key presses, mouse clicks, mouse movement, etc. You code a response to the action, and it is triggered when the action occurs. A key difference vs. procedural coding is that actions in event-driven applications may happen in any order.
- Object-Oriented Programming (OOP): A more complex approach, but common and powerful. Diffferent elements within your program and environment are represented by objects (a logical representation of the element), and you code the various actions (functions) that can be performed with these objects; different types of objects, can have different functions available to them.

### What is a Program

We can write programs to carry out a range of different operations, however they all share some concepts. They need to:

- Accept input, from the user, from events, from API calls, etc.
- Process the input, which may involve operating on the input, or it may be a trigger to process other elements.
- The application will need access to storage: fast RAM for the duration of the application's runtime; persistent storage if data needs to outlive the application.
- Finally the application needs to produce some form of output. The output could be text based, more complex apps can produce other visual elements such as graphics and audio, such as in a game; the application may not need to produce any obvious visual output, it may just be a confirmation or error message, or even just a status code.

### Python Modes

Windows (or MacOS, or Linux) doesn't come with Python available by default, Microsoft doesn't make Python, so we need to install it like any other application. Once you have done so, you can use it in two different ways:

- Interactive mode: from a Terminal run the command python, you will see a few lines of text indicating your Python version, and a few help commands. Then you see the Python prompt `>>>`, from where you can run individual lines of code. This mode is useful for quickly validating or testing something, you can also use it like a simple calculator. But this environment is very limited, for example saving you code to re-run it later is difficult. Exit interactive mode with `exit()`.
- Script mode: we write our Python commands in plain text, in a file Python file, which ends with a `.py` extension. We can write our code in this file, edit and maintain it just like any text file. This is how we'll write our applications.

>Do NOT write code in a word processor, use a text editor such as Notepad++, or even better, an integrated development environment (IDE) such as Visual Studio Code. This is because word processors include hidden characters to facilitate the different formatting you apply, and these characters can be included when you copy/paste code, resulting in unexpected errors when running it.

## Variables

Beyond entering expressions using specific values, like using a calculator (e.g. `3 * 9 + 5`), the first thing we need to learn to use to make our code more useful are variables.

Variables are simply containers for data, we can assign values to variables which we can then re-use over and over throughout our app. This provides lots of benefits you will appreciate as you write your own code, but to begin with they allow us to reduce repetition, and also provide consistency, because the value will always be what you last set it to. They can also reduce errors, because relying upon humans to recall and enter the correct values manually is always going to be prone to errors.

We can assign any data we need to our variables using the = symbol

```py
age = 30
name = 'John'
is_adult = True
height_meters = 1.8
```

Python support a number of different data types, three are demonstrated above:

- Integers (positive or negative whole numbers)
- Strings (text values)
- Boolean (True or False)
- Float (positive or negative decimal numbers)

In Python some of the other objects we create, such as `lists`, `tuples`, `dictionaries`, and more are also considered data types.

You can query the type of data stored in a variable with the `type()` method

We can utilise a range of built in operators against the values in our code, usually when they're assigned to variables. Below you can see examples of the most common arithmetic and comparison operators.

```py
age = 30
print(type(age))
```

```py
a = 5
b = 10

print(type(a))
print(type(b))

# Arithmetic Operators - returns values
print(a + b)
print(a - b)
print(b / a)
print(a * b)
print(a ** b)
print(b % a)

# Comparison Operators - returns boolean
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

'''Some comparison operators can also be used against strings; they can be compared for a match of mis-match; following the logic of a = 1, b = 2, c = 3... and so on, you can also use `<` and `>` comparisons'''
```

The below operators are used to quickly update the value of a variable, without having to add unnecessary variables, or lines of code.

```py
my_var = 10

# If I need to add 5 to the above value I could...
# 1.
add_num = 5
new_val = my_var + add_num
print(new_val)

# 2.
my_var = my_var + 5
print(my_var)

# 3. Using an Assignment operator
my_var += 5
print(my_var)

# More assignment operators
my_var += 5 # add 5 to my_var
my_var -= 5 # subtract 5 from my_var
my_var *= 5 # multiple my_var by 5
my_var /= 5 # divide my_var by 5
my_var %= 5 # return the modulus of my_var / 5
my_var **= 5 # raise my_var to the power of 5
```

>Notice in the above code blocks, we can add comments to our Python script files using the `#` symbol, as Python interprets each line, it ignores everything that comes after a `#`. We can add multi-line comments by enclosing the lines in triple-single quotes `'''my long comment'''`

## Working with Strings

Although some of the comparison and assignment operators can be used with strings, we do need to think about them differently. Numbers don't have upper and lowercase characters, for example.

Strings are text based data, but that doesn't mean only letters and words, for example dates, times, and phone numbers are values we want to treat as text. We don't want to divide our phone number by two, or round it up. We need to ensure that Python knows these values are treated as strings.

Declare a string by enclosing it in single or double speech marks

```py
my_string = "Hello world" # assign a variable to a string
print(my_string)
print('Goodbye moon') # we don't need to declare a variable to create a string 

# Use either single or double quotes, often you'll choose based on the required string
string_1 = "Ant's dogs are mini-dachshunds"
string_2 = 'Ant said "my dogs are mini-dachshunds"'

print(string_1)
print(string_2)
```

### String Concatenation

Concatenation is a techy word for linking things together; if we add two numbers together we get a new number; if we add two strings together (concatenate them) we get a new longer string, comprised of the original strings.

```py
a = "hello "
b = "world"
print(a + b)

# the below code does the same thing
c = "goodbye "
c += "moon"
print(c)
```

### String Interpolation

A common task is combining strings with your variables in order to customise the output, there are two ways to do so.

```py
a = "Frankie"
b = "Scout"

print("Ant's sausages are called " + a  + " and " + b)
print(f"Ant's sausages are called {a} and {b}")
```

The first method requires you to separate each element of your desired output, the fixed text, and the variables, and combine them together manually. The second method is to use f-strings, which is a more modern approach, and allows you to embed your variables without opening and closing your strings frequently.

There is another way that f-strings make life slightly easier, which is that they don't require you to specify the data type.

```py
a = "Frankie"
b = "Scout"
age_a = 3
age_b = 6

print(a + " is " + age_a + " and " + b + " is " + age_b) # This one fails
print(f"{a} is {age_a} and {b} is {age_b}") # This one succeeds
```

To make the first example work, you need to explicitly convert the numeric values into strings using the `str()` method.

```py
a = "Frankie"
b = "Scout"
age_a = 3
age_b = 6

print(a + " is " + str(age_a) + " and " + b + " is " + str(age_b)) # This one fails
```

We can also do the opposite, if we have a value declared as a string but need to use it as an integer we can use `int()`.

### String Methods

There is one more important concept to understand early on, it applies to many different object types in Python, called `methods`. Methods are the built in functionality available to the objects we create, there are different methods available for lists, for dictionaries, and in this below case, strings.

```py
name = "antony foy"

print(name.upper()) # Convert to uppercase
print(name.title()) # Capitalise every word
print(name.split(" ")) # Split at the specified separator and return a list
```

There are many more string methods you can review here: [W3Schools](https://www.w3schools.com/python/python_ref_string.asp)

## Input and Output

To make our code more interactive and allow us to pass data into it, we can use it the `input()` function. As Python interprets each line, as it encounters the input function it pauses, and waits for the user to provide some data; when the user presses enter the app continues.

To improve the user interface we can provide a prompt string in the input function to let the user know what is expected.

```py
name = input("Please enter your name\n>")
# Notice the 'escape character' `\n` which doesn't print out, but does affect the output, in this case it starts a new line.

print(f"Nice to meet you {name}, would you like to play a game?")
```

Once we have captured the user input, we can then assign it to a variable, and process that input like any other value.

## Working with Lists

So far we've been working with and assigning single values to our variables; lists are containers in which we can store zero or more values. The elements in a list can be any data type, and mixed within the same list; elements are also ordered by their index number.

### List Indexing

Elements in a list (and in other data structures) are automatically assigned an index number according to their place in the list. The first item is index 0, the next is index 1, and so on...

```py
empty_list = []
numbers_list = [1, 2, 3, 4, 5]
people_list = ["Ant", "Rachel", "Segun", "Sarmistha"]
mixed_types = ["Ant", 43, 6.0, "Brown", True]
# Notice the syntax: square brackets, each element separated by a comma
```

>It is very important to be aware of index numbers, and in particular that they start at 0. This is a common cause of unexpected output, it's so common that it's referred to as an *off by one error*.

The index number allows us to retrieve single or multiple items from a list using `list_name[index_number]`

```py
people_list = ["Ant", "Rachel", "Segun", "Sarmistha"]
# retrieve individual items with 
print(people_list[0])
print(people_list[1])
print(people_list[2])
print(people_list[3])
```

#### Slicing a List

We can use the index numbers to select multiple adjacent items at once, called a slice, we provide the starting and ending index, and a colon `[x:y]`

**IMPORTANT**: The slice starts at the first index number, and stops at the item before the second index, like the off-by-one error, incorrect indexing can produce unexpected results.

```py
people_list = ["Ant", "Rachel", "Segun", "Sarmistha"]
# retrieve a slice with:
print(people_list[1:3])
# if you omit the first or last index your slice will go to the beginning/end
print(people_list[2:])
print(people_list[:3])
print(people_list[:-1])
# sometimes you might not know how long your list is, so you can also use minus numbers, -1 = one from the end, -2 = two from the end, and so on
print(people_list[:-2])
```

>Lists are a powerful and commonly used Python data type, we can use them for storing values, but we can also process the values in the list automatically using loops, which we'll return to in the next module.

### Populating an Empty List

We may often start with an empty list, which we want to populate during the running of our code. Below we're combining a few different concepts we've covered so far to fill a list.

```py
names_list = [] # Create an empty list

# Capture 3x names
first_name = input("Enter your name\n>")
second_name = input("Enter your name\n>")
third_name = input("Enter your name\n>")

# Confirm the list is empty
print(names_list)

# Add names to list using the append() method
names_list.append(first_name)
names_list.append(second_name)
names_list.append(third_name)

# Confirm the list is now populated
print(names_list)
```

>The code above is very poor! How could it be improved?

<details><summary>Answer:</summary>Reduce repetition with loops - to be covered in the next module</details>

## If statements

So far our code has been pretty much following the procedural paradigm, we've written lines of code, and each one is processed, and the expected output is returned. However, we quickly hit limits with this approach because there is only one path from start to end, so our code cannot account for different scenarios.

If statements allow us to make decisions in our code, by providing different outputs depending upon the result of a test you can define. If the outcome of the test is True then some code is run, if the test is False, something else can happen.

The most commonly used tests will utilise the comparison operators that we reviewed earlier, but more complex tests can be created. However, the output of your test should always be a boolean value (True/False).

We can use `if` and `else` statements to run different lines of code depending upon the output of the test in the if statement.

```py
age = int(input("Please enter your age: "))

if age < 29:
    print("You're Gen-Z")
else:
    print("You're old!'")
```

We can provide more than two possible outputs for our if statements by using `elifs` (else if)

```py
age = int(input("Please enter your age: "))

if age < 30:
    print("You're Gen-Z")
elif age < 46:
    print("You're a Millenial")
elif age < 62:
    print("You're a Gen-X")
else:
    print("You're a Boomer")
```

## Indentation

Reviewing one of our previous examples again, notice that each line following an if statement is indented from it's parent.

```py
age = int(input("Please enter your age: "))

if age < 30:
    print("You're Gen-Z")
elif age < 46:
    print("You're a Millenial")
elif age < 62:
    print("You're a Gen-X")
else:
    print("You're a Boomer")
```

This is how Python (and other environments) identify which lines of code are related. In this case when one of the conditions evaluates to True, the indented line of code is run, but if it's False the indented line is skipped.

## Logical Operators

Particularly useful for if statements, and many other scenarios, logical operators allow us to combine multiple conditional operators to create more complex tests.

|Operator|Description|Example|
|---|---|---|
|`and`|true if both conditions are true|`x > 5 and x < 10`|
|`or`|true if at least one condition is true|`x > 5 or x < 10`|
|`not`|reverse the result i.e. if `a` exists return false, and vice-versa|`not x`|

A common tool to understand logical operators is to look at [Binary Truth Tables](https://www.realdigital.org/doc/e127ebfa82dbc904b5c0dac5d1adce8e)

Examples:

```py
age = 17
film_rating = 15

if (age < 18 and film_rating == 18): # Both conditions must be true
    print("You're too young, this film might disturb you!")
else:
    print("Come on in, the trauma is on you!")
```

We can also use logical operators to simplify complex if statements

```py
age = 17
film_rating = 15

if  (age < 12 and film_rating == 12) or \
    (age < 15 and film_rating == 15) or \
    (age < 18 and film_rating == 18):
    print("You're too young, this film might disturb you!")
else:
    print("Come on in, the trauma is on you!")
```

Some of the last examples we've used have started to relate a bit more to the real, giving different responses to different people, or checking film ratings. If statements are one of the ways we can start to represent or **model** more complex scenarios through our code.

## Exercises

Below are some exercises to reinforce some of the different concepts we've covered.

[variables exercises](./exercises/variables-exercise.md)
[lists exercises](./exercises/intro-lists-exercises.md)
[python exercises](./exercises/python-1-exercises.md)
