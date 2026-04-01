# Python 1 Cheatsheet

## Interactive Mode

```bash
# Windows
$ py

# (MacOS / Unix)
$ python3

# (GitBash)
$ python3

>>> exit() # currently inside the interpreter
$          # back to the original terminal
```

## Script Mode

Python files have the `.py` extension

## Arithmetic Operators

```py
#add
print(1 + 3)
#minus
print(10 - 4)
#divide
print(20 / 2)
#multiply
print(3 * 7)
#modulus
print(4 % 40)
#brackets
print((5 * 10) - (20 + 10))
```

## Comparison Operators

```python
#is equal to
print(30 == 30)
print(30 == 10)
#is not equal to
print(30 != 10)
print(30 != 30)
#greater than
print(10 > 5)
print(10 > 15)
print(10 > 10)
#less than
print(5 < 10)
print(5 < 4)
print(5 < 5)
#greater than or equals
print(6 >= 4)
print(6 >= 6)
print(6 >= 7)
#less than or equals
print(8 <= 10)
print(8 <= 8)
print(8 <= 3)
```

## Variables

### Naming standards

[here](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)

```py
age = 30
name = 'John'
is_adult = True

#print the variable
print(age)

#change the variable value
age = 40
print(age)

```

### Data Types

```py
a = 100 # Integer (int)

b = 2.5 # Decimal (float)

name = 'Bob' # String (str)

is_active = True # Boolean (bool)

position = (12.33, -122.34) # Tuple

colours = ["Cyan", "Magenta", "Yellow", "Black"] # List

numbers = {1, 2, 3, 4, 5, 6} # Set

# Dictionary (dict)
data = {
    "key": "value",
    "another_key": False,
    "some_items": [1, 2, 3]
}
```

### Strings

```py
# Basic String
first_name = 'John'
last_name = 'Doe'
bank_name = 'DigiBank'
# Multi-Line String
main_menu = '''
    Please choose from the following:

    [1]: View Balance
    [2]: View Account Details
'''

#String concatenation
print(first_name + last_name)

#String interpolation
print(f'Welcome {first_name} {last_name} to the {bank_name}')

```

### List

```py
empty_list = []
numbers = [1, 2, 3, 4, 5]
people = ["John", "Jane", "Janet", "Sally", "Mark", "Lisa"]
mixed = ["John", 2, "Jane", 3, False]

#List Indexing
print(people[0]) # John
print(people[1]) # Jane
print(people[2]) # Janet

#List Selection
print(people[1:3])
# Get last item
print(people[-1])
# Omitting left-hand side means "start from the beginning"
print(people[:-1])
# Get all items but the first, Omitting right-hand side means "end of the list"
print(people[1:])
```

### Built-in functions

```python
#input with no prompt
text = input()
print("You entered:" + text)

#input with a prompt
name = input("What is your name? ")
print("Nice to meet you, " + name)

#convert string to int
input_value = input('Enter a number: ') # input always returns a string
num = int(input_value)
print(f'This square of this value is {num * num}')

```

### If statements

```py
# If
a = 12
if a > 5:
    print("a is greater than 5")


# If/Else
a = 3
if a > 5:
    print('a is greater than 5')
else:
    print('a is less than 5')


# If/Elif
a = 6
if a > 10:
    print('a is greater than 10')
elif a > 5:
    print('a is greater than 5')
elif a > 0:
    print('a is greater than 0')


# If/Elif/Else
a = 3
if a > 10:
    print('a is greater than 10')
elif a > 5:
    print('a is greater than 5')
else:
    print('a is less than 5')


#Nested If
a = 10
b = 20
if a >= 10:
    if b >= 10:
        print ('a and b are greater than or equal to 10')

```

### Logical Operators

```py
x = 6
y = 9
z = True

# true if both statements are true
if x > 5 and y < 10:
    print("Statement is true")


# true if either or both statements are true
if x > 5 or y < 10:
print("Statement is true")


# reverse of the result
if not z:
    print("Statement is true")
```
