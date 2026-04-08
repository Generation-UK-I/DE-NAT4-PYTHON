# Python Continued

## Loops

In the previous module we learned about lists, a container for multiple individual data items, which we can then retrieve as needed

```py
people_list = ['Ant', 'Rachel', 'Segun', 'Sarmistha']
# retrieve individual items with 
print('the person's name is ' + people_list[0])
print(f'the person's name is {people_list[1]}')
print(f'the person's name is {people_list[2]}')
print('the person's name is ' + people_list[3])
```

It works, but it's not good code - why?

<details><summary>Answer:</summary>It's repetitive, we need a loop.</details>

In addition to storing and recalling values, lists can be used to hold items for processing elsewhere in our code. The most common method of processing items in a list is using a `for` loop.

### For Loops

The for loop is a function which iterates through any given input, until all of the items are processed; when it has reached the end of the input the loop automatically stops.

```py
people_list = ['Ant', 'Rachel', 'Segun', 'Sarmistha']

for name in people_list:
    print(f'the person's name is {name}')
```

- **for**: initiate a for loop
- **name**: a temporary variable, it's value updates for each iteration of the loop
- **people_list**: the name of the list input

After initiating the loop with `for` the operation needs a temporary variable, in the above case `name`, which represents the value in question for each iteration of the loop. During each iteration any code indented within the for loop is run, which can be print statements, comparison operators, if statements, anything we want to run against each item. Again, referencing the example above:

1. On the first loop the temporary variable `name` has the value 'Ant', and the string 'the person's name is Ant' is printed.
2. On the second loop the temporary variable `name` has the value 'Rachel', and the string 'the person's name is Rachel' is printed...
3. and so on...

#### The Range() Function

Python has many different built in functions, print() is one we've used many times, as well as input(), str(), there are many available, you can view some here: [w3schools](https://www.w3schools.com/python/python_ref_functions.asp).

The range() function can return a range of numbers, based on the conditions we provide. We can use the following options when we call the function `range(start, stop, step[optional])` i.e. where should the range start, when should it stop, and do you want to go up in increments (steps). The steps value is optional, the default is to increment by 1.

```py
for x in range(0, 11, 2):
    print(x)

# Returns >>> 0 2 4 6 8 10
```

We commonly use range in our `for` loops as in the above example, when we want to run the loop a set number of times, without having to create a separate list or input with the number of items/loops we need.

#### Loops with Multiple Lists

Review the below example, and see if you can unpack the logic, then reveal the explanation below.

```py
Learners = ['Yousaf', 'Marcel', 'Katerina', 'Mohammed', 'Sahour', 'Ric', 'Ammar']

Daily_openings = ['Marcel', 'Mohammed', 'Sahour', 'Ric']

for name in Learners:
    if name in Daily_openings:
        print(f'{name} you have signed up for a daily opening, thank you')
    else:
        print(f'{name} you still need to sign up for a daily opening')
```

<details><summary>Answer:</summary>A for loop is initiated against the Learners list; for each learner the if statement checks whether the value of name exists in the Daily_openings list; if True it prints a confirmation message, otherwise it prints a message reminding them to sign up.</details>

#### Nested Loops

We can add multiple layers of loops, but it does start to get complex trying to keep track of the logic in your brain. **Make sure you pay attention to your indentation**.

```py
cars = ['Audi', 'BMW', 'Ford', 'VW']
colours = ['Red', 'Black', 'Grey']

prompt = 'Welcome to AntoTrader' # **
prompt += 'We have the following cars available:'
print(prompt)
for car in cars: # Each item in the first list...
    for colour in colours: # ...loops through each item in the second list
        print(colour, car)

print('Thank you for browsing our stock') # This print statement is outside of our loops, so only executes when they've all finished.
```

** This `prompt` approach of string concatenation is sometimes preferable, because you only need one `print()` statement. This can be useful if you later want to output to a file, because you only need to change the one print statement.

### While Loops

The next type of loop is the While loop, rather than iterating a set number of times based on the length of the input, it will loop until a specified condition is met. While loops are initiated with the while command, followed by a condition that will stop it, or we can simply run it forever, and have our user stop it manually when they're ready.

The examples below demonstrate some ways we can control while loops.

#### Using a Counter

In this example the while loop will run for as long as the counter variable is not equal to 0, the loop prints out a message, and reduces the counter by one each iteration until it reaches 0 and the loop stops.

```py
counter = 10

while counter != 0:
    print(f'T-minus {counter}')
    counter -= 1

print('Blast off!!!') # Click Reveal below for a bonus add on
```

- **while**: initates the loop
- **counter**: name of the monitored variable
- **!= 0**: not equal to zero
- **-= 1**: reduce counter by one

<details><summary>Reveal:</summary>That countdown was too fast - you could make it more dramatic by importing the time module by adding 'import time' at the top of your python script, then add this line below the countdown print statement 'time.sleep(1)' which tells it to wait for a second after each loop.</details>

#### Using a Flag

The next example gets a little trickier, because we want to let the user decide when to stop the loop, which means we need to capture some input, and check that input with an if statement.

```py
flag = True

while flag:
    choice = input('Enter a name, or type 'quit' to end the program')
    if choice.lower() != 'quit': # Why use the lower() method here? Click reveal to check.
        print(f'Hello {choice}, would you like to play a game?')
    else:
        print(f'goodbye {choice}!')
        flag = False
```

<details><summary>Reveal:</summary>We cannot be sure what format the user will provide the input, UPPERCASE, lowercase, or Titlecase. So we turn it to lowercase for our comparison operator to match all variations.</details>

#### Breaking the Loop

The last way to control our while loop is using a break statement which allows you to add a condition to your code which breaks the while loop whenever the user chooses.

This is particularly useful for user interfaces, where we basically start an infinite loop, with no condition to meet, or flag to change, we simply write a line of code which runs the break statement. This is particularly useful for creating user interfaces which you want to run indefinitely, until the user wants to close the app.

>**WARNING** - be careful with infinite loops, your app can literally get stuck running round and round with no way to close it beyond forcing it from the terminal (CTRL + C) or task manager.

```py
while True:
    prompt = 'Welcome to my app\n'
    prompt += '1. Menu option 1\n'
    prompt += '2. Menu option 2\n'
    prompt += '3. Menu option 3\n'
    prompt += '0. Quit' # Ensure you tell the user how to stop the app
    print(prompt) # if you only copy to here and run the code, it will be an infinite loop.
    choice = input('Please make a choice from the menu\n>')
    if choice != '0':
        print(f'You chose option {choice}')
    else:
        break # The loop runs as long as the user input is not '0', then breaks whenever the user chooses to.
```

#### Skipping an Iteration with Continue

There may be occasions when you want to pass over one of the items to be processed, we can do this with the `continue` statement, which jumps straight to the next iteration.

```py
# Katerina wants to send a message to everyone except herself

Learners = ['Yousaf', 'Marcel', 'Katerina', 'Mohammed', 'Sahour', 'Ric', 'Ammar']

for person in Learners:
    if person == 'Katerina':
        continue
    else:
        print(f'Hey {person} party at my house')
else:
    print('All people invited')

# The output should include a message to everyone except Katerina
```

>**Notice**: we can also use the `else` statement to add some code to be executed once the `for` loop has finished.

### Loops Exercises

[Click here to complete the loop exercises](./exercises/loop-exercises.md)

## Dictionaries

We looked at dictionaries briefly in module 1, just simple to identify them as another way of storing values. In fact, they're a very powerful data structure, which allows us to model complex objects in our code.

A dictionary is comprised of key-value pairs, separated by a colon `'key':'value'`. Each KVP is akin to an item in a list, and we can have as many KVPs in our dictionary as we want, separating each one with a colon, just like a list.

```py
# We can use strings or numbers as keys
phonetic_dict = {
    'a' : 'alpha',
    2 : 'bravo',
    'c' : 'charlie',
    4 : 'delta'
}

# Dictionaries can be used to model real world objects
dog_dict = {
    'name' : 'Frankie',
    'Age' : 6,
    'breed' : 'miniature-dachshund',
    'colour' : 'shaded-red'
}

# Values can be multiple different data types
cake_dict = {
    'name' : 'Chocolate Fudge Cake',
    'servings' : 12,
    'layers' : 4,
    'frosting' : True,
    'ingredients' : ['flour', 'milk', 'eggs', 'butter', 'cocoa powder', 'sugar'] # A value can also be a list, a tuple, or another dictionary - see further down.
}

# We can add as many key-value pairs as we want to describe objects in as much detail as needed
car_dict = {
    'make' : 'Audi',
    'model' : 'A6',
    'year' : 2013,
    'doors' : 4,
    'type' : 'Saloon',
    'fuel' : 'diesel',
    'engine_size' : 3.0,
    'power (bhp)' : 320,
    'torque (nm)' : 650,
    '0 - 62mph' : 5.1,
    'AWD' : True
}
```

### Accessing Values in a Dictionary

We can access individual values from within our dictionaries using a similar syntax to lists, however KVPs are not indexed, so we can use the key name to retrieve the value like this: `dictionary[key_name]`. If you try to retrieve a value for a non existent key you will receive a `KeyError`.

```py
cake_dict = {
    'name' : 'Chocolate Fudge Cake',
    'servings' : 12,
    'layers' : 4,
    'frosting' : True,
    'ingredients' : ['flour', 'milk', 'eggs', 'butter', 'cocoa powder', 'sugar'] # A value can also be a list, a tuple, or another dictionary - see further down.
}

print(cake_dict['name'])
```

### Modifying Dictionaries

We can modify the keys and values in the dictionary using the following methods.

#### Adding Key-Value Pairs

```py
# Start with an empty dictionary
learner1 = {}
# call the dictionary, provide the new key in square brackets, then the value.
learner1['name'] = "Rick James"
learner1['age'] = 78
learner1['description'] = 'super freak'
# Print the dictionary to verify
print(learner1)
```

#### Updating Key-Value Pairs

```py
# Start with a dictionary
learner1 = {
    'name' : "Rick James",
    'age' : 78,
    'description' : 'super freak'
}

# Update an existing value with the same syntax as above, but providing an existing key
learner1['age'] = 56

# Print the dictionary to verify
print(learner1)
```

#### Delete a Key-Value Pair

Delete a value using the `del` keyword, the dictionary name, and the key.

```py
# Start with a dictionary
learner1 = {
    'name' : "Rick James",
    'age' : 78,
    'description' : 'super freak'
}

# Delete a value
del learner1['description']

# Print the dictionary to verify
print(learner1)
```

### Looping Through a Dictionary

We've seen how to access individual key-value pairs, very similar to a list, we simply call the name of the object, then provide the index number or key within square brackets.

We also saw how we can loop through all of the values in a list, using a for loop.

```py
people_list = ['Ant', 'Rachel', 'Segun', 'Sarmistha']

for name in people_list:
    print(f'the person's name is {name}')
```

This for loop utilises a temporary variable `name`, which takes the value of each element in the list as the function loops through them. We can do the same thing with our dictionaries, with one small addition. Since each element in a dictionary is comprised of two components `[key]:[value]`, we need to tell our for loop which component to loop through using either the `keys()` or `values()` methods.

```py
cake_dict = {
    'name' : 'Chocolate Fudge Cake',
    'servings' : 12,
    'layers' : 4,
    'frosting' : True,
    'ingredients' : ['flour', 'milk', 'eggs', 'butter', 'cocoa powder', 'sugar']
}

print("The keys are:")
# Loop through the keys
for key in cake_dict.keys():
    print(f"- {key}")

print("The values are:")
# Loop through the values
for key in cake_dict.values():
    print(f"- {key}")
```

This syntax is very similar to looping through lists, but what if we want to loop through both the keys and values?

To do so we need to make a couple of different additions to our code: Our for loop will require two temporary variables, one for the key and one for the value in each loop; we also need to use the `items()` method rather than `keys()` or `values()`.

```py
...

# Create two temp' variables, and use the items() method to loop through both keys and values
for key, value in cake_dict.items():
    print(f"The key is: {key}\nThe value is: {value}\n")
```

### Nested Dictionaries

The value for a key value pair could also be a nested dictionary.

```py
car_stock = {
    'car_1' : {
        'make' : 'Audi',
        'model' : 'A6',
        'year' : 2013,
        'doors' : 4,
        'type' : 'Saloon',
        'fuel' : 'diesel',
    },
    'car_2' : {
        'make' : 'Smart',
        'model' : 'ForTwo',
        'year' : 2010,
        'doors' : 2,
        'type' : 'hatch',
        'fuel' : 'Petrol',
    },
    'car_3' : {
        'make' : 'Porsche',
        'model' : '911',
        'year' : 2009,
        'doors' : 2,
        'type' : 'Convertible',
        'fuel' : 'Petrol',
    }
}

prompt = 'Welcome to AntoTrader'
prompt += 'We have the following cars available:'
print(prompt)

for car in car_stock.values():
    print(car['make'])
'''On the first loop the temporary 'car' variable takes the VALUE associated with first KEY (car_1) in the 'car_stock' dictionary; The print statement then prints the value associated with the key 'make' in that car_1 dictionary; On the second loop 'car' takes the value of the second dictionary, and so on...'''

print('Thank you for browsing our stock')
```

### Dictionary Functions

Python includes a number of built in functions to help you work with dictionaries.

```py
...
# Return the value for a key if it exists (rather than erroring)
print(cake_dict.get('servings'))
# Return all key-value pairs
print(cake_dict.items())
# Return all keys
print(cake_dict.keys())
# Return all keys
print(cake_dict.values())

# Check if a key exists
if 'name' in cake_dict: # Returns True
    print("key found")

# Count the number of keys
print(len(cake_dict))
```

### Dictionary Exercises

[click here to complete the dictionary exercises](./exercises/dictionary-exercises.md)

## Exceptions

You have likely seen multiple exceptions already, they are errors which cause your application to crash, because something unexpected happened.

There are a number of different errors, some examples are illustrated below.

```py
print('2' + 2)
# TypeError: can only concatenate str...

print(10 / 0)
# ZeroDivisionError:

names = ["Ant", "Segum", "Sarmistha", "Rachel", "Proscovia"]
print(names[7])
# IndexError: list index out of range

f = open('does_not_exist.csv')
# FileNotFoundError:
```

**Pay attention to your errors**, Python does it's best to highlight where the error occured, and provides you a line number to begin your debugging.

Ideally we would not have any errors in our code, and we can certainly try to anticipate avoid many of them. One example is remembering when we need to change numbers to strings and vice-versa, to avoid TypeErrors when inserting variables into strings.

However, some error conditions may be harder or impractical to account for, or could simply be related to a missing feature or function that hasn't yet been added on the development path.

### Try-Except

Python has a built-in construct called `try-except` to handle exceptions. The code we would normally run is placed inside the `try` block. If an exception is raised inside the block, it immediately jumped to the
`except` block to handle the exception.

```py
try:
  x = 1 / 0
except ZeroDivisionError:
  print("You can't do that!")
  print("We can still run code after this though...")

# Instead of crashing, Python will continue running any code following the try-except block
print("I told you so")
```

**Tips:**:

- Don't put try-except around big blocks of code *just in case* it doesn't replace actual de-bugging
- Use sparingly, they're not a short-cut to avoid proper input handling.
- Ensure your except block provides a helpful message explaining what went wrong.

#### Syntax Errors

Different to exceptions, which occur when correctly written code fails, syntax errors arise when a statement has been written incorrectly.

```py
print("Hello world)

# SyntaxError: unterminated string literal
```

## Functions

So far you've written an awful lot of code, but it all runs in a specified order; the Python interpreter starts at the top, and works it's way down your lines of code. Even our loops and if statements, there may be code that doesn't run, but when you run your code, the if statement **will** execute.

What if we want more flexibility? What if we want to let the user choose which code runs, and when? We can achieve this with functions.

Functions are re-useable blocks of code that typically perform a single task, which is likely to be needed more than once. Consider an `add-user` function - You don't necessarily know when you need to add new users but you will need to do it regularly, and it needs to work the same way each time.

```py
# Start with an empty list
user_list = []

def add_user(name):
    user_list.append(name) # Append 'name' to list
    print(user_list) # Verify
    print(f"{name} has been added to the user list") # Print confirmation message

add_user('Ant') # Call the function by it's name, and provide required 'parameters'
```

>This function is not very useful, because it can only add one user, fix this.

- **def**: declare a function
- **add_user**: name the function
- **name**: the argument the function requires

We create a function using the `def` keyword, followed by the function name, and a pair of parenthesis. Similar to variable names, your function names should be descriptive, but not too long. Avoid conflicting with the names of existing Python functions, don't call your function `print` for example.

### Arguments and Parameters

Arguments and Parameters are essential for making useful functions; Arguments are the variables we use inside our functions; Parameters are the values we pass through to the arguments.

#### Arguments

When declaring a function, we can identify any variables we want to use within the function inside the parenthesis, in the previous example we used name: `def add_user(name)`. These variables, when declared in a function, are called `arguments`; typically these are the data items to be processed by the function.

```py
def make_drink(drink, size, ice): # The function has three arguments
    print(f"selecting {size} glass...") # The arguments can be used throughout the function, just like any other variable.
    print(f"pouring {drink}...")
    if ice == 'yes':
        print("adding ice...")
        print(f"Your {size} {drink} with ice is ready, enjoy")
    else:
        print(f"Your {size} {drink} is ready, enjoy")
```

#### Parameters

To call our function we simply use it's name, and pass through the values for the arguments. The default behaviour is for parameters to be passed through to the arguments in the order they appear - this can cause unexpected results if you're not careful.

```py
...
make_drink('coke', 'large', 'yes')
```

<details><summary>Challenge:</summary>Our function will be much more useful if the user could make these selections. Can you modify the code to enable this functionality?</details>

#### Return Values

The previous two examples of functions simply printed out a message, nothing persisted after the function. In real-world apps we're often working with data objects which we want to pass through a function for some processing, but then return the object back, perhaps in a modified state.

For this we can use the return statement.

```py
def combine_name(first, last):
    full_name = (f"{first} {last}") # Create a new string from the two arguments
    return full_name # Return the new string object

f_name = 'antony'
l_name = 'foy'

full_name = combine_name(f_name, l_name)
print(full_name.title()) # The new object is not printed until after the function has finished and returned it
```

### Working with Arguments and Parameters

Arguments, and the parameters we pass through to them, are a powerful feature permitting lots of flexibility in how we add functionality to our apps. However, it is important that our functions and arguments are called correctly, or Python will fail with an error like: `TypeError: [function_name]() missing 1 required positional argument`.

To account for the different ways we may want to use our functions, there are a range of methods for creating and populating our arguments.

#### Default Arguments

Also known as **keyword arguments**, we can provide default values for arguments, which will be used if a new value is not provided when calling. This strategy can also be used to make arguments optional.

```py
def combine_name(first, last, middle=''): # The optional argument should be the last one declared
    if middle != '': # 'middle' is empty by default, so if provided this statement is 'True'
        full_name = (f"{first} {middle} {last}") # Create a new string from the two arguments
    else:
        full_name = (f"{first} {last}")
    return full_name

f_name = 'antony'
m_name = 'james'
l_name = 'foy'

full_name = combine_name(f_name, l_name, m_name)
print(full_name.title())
```

#### Named Arguments

As mentioned above, the default behaviour is to pass parameters through to arguments in the order they appear, but with named arguments we specify the argument we're passing an parameter for, so the order doesn't matter.

```py
def combine_name(first, last, middle=''): # The optional argument should be the last one declared
    if middle != '': # 'middle' is empty by default, so if provided this statement is 'True'
        full_name = (f"{first} {middle} {last}") # Create a new string from the two arguments
    else:
        full_name = (f"{first} {last}")
    return full_name

f_name = 'antony'
m_name = 'james'
l_name = 'foy'

full_name = combine_name(middle = m_name, last = l_name, first = f_name)
print(full_name.title())
```

#### Keyword-Only Arguments

Using keyword-only arguments ensures that selected arguments can *only* be given new values if they're named.

```py
def combine_and_greet(first, last, *, greeting = 'hello'): # All arguments after the * must be passed as keyword-arguments or an error will be produced
    greeting = (f"{greeting} {first} {last}")
    return greeting

f_name = 'antony'
l_name = 'foy'

full_name = combine_and_greet(f_name, l_name)
print(full_name.title())

# Override the keyword argument
change_greet = combine_and_greet(f_name, l_name, greeting = 'Welcome')
print(change_greet.title())

# Will generate a positional-arguments error
test_greet = combine_and_greet(f_name, l_name, 'Welcome')
print(test_greet.title())
```

#### Positional-only Arguments

Allows you to prevent arguments being passed as keywords

```py
def combine_name(first, last, /): # Arguments before / must be standard arguments
    greeting = (f"{first} {last}")
    return greeting

f_name = 'antony'
l_name = 'foy'

# Generates a TypeError
full_name = combine_name(first = f_name, last =  l_name) 
print(full_name.title())
```

#### Arbitrary Arguments

In some circumstances you may not know how many arguments need to be passed, in these cases you can use `*[argument]`, generally referenced as `*args`, which will create a `list` from any parameters passed through.

```py
def my_function(*people):
  people_list = people
  return people_list

names_list = my_function("Alice", "Bob", "John")
print(names_list)
```

#### Arbitrary Named Arguments

There is a similar option: `**kwargs` which allows you to pass as many named arguments as you wish. Because the arguments are named, kwargs can create a dictionary, with the name as key, and the parameter as the value.

```py
def build_person(**attributes):
    person_dict = attributes
    return person_dict

new_user = build_person(name = 'Ant', age = 43, height = 6.0)
print(new_user)
```

#### Ordering of Arguments

You can mix the various types of arguments to create flexible and powerful functions, but the order that you declare the arguments is important.

1. Standard Arguments
2. *args
3. **kwargs

`def my_function(a, b = 'value', *args, **kwargs)`

### Functions Exercises

[Click here to complete the functions exercises](./exercises/function-exercises.md)

## Additional Practice Exercises

- [Loops](./additional-exercises/user-input-while-exercises.md)
- [Dictionaries](./additional-exercises/dictionaries-exercises.md)
- [Functions](./additional-exercises/functions-exercises.md)
