# Python Cheatsheet

## For Loops

```python
some_list = [1,2,3,4,5]
for x in list:
    print(x)
```

`x` in the above example can be named anything as this is just a variable name to assign the value

```py
some_list = ["item", "thing", "required"]

for i in some_list:
    if i == "required":
        break # We found what we were looking for
    else:
    raise ValueError("Required not found.")

print("Required was found.")
```

<note>If you change `required` from the above list to `abandoned` you will enter the else</note>

### Nested

```py
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjectives:
  for fruit in fruits:
    print(adj, fruit)
```

### While

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

```python
while True:
    print("When will it end??")
```

<note>WARNING - the above is an infinite loop.</note>

### Keywords

#### break

```python
while True:
    print("When will it end?")
    break
```

#### continue

```py
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
```

### Dictionaries

```py
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : 1964,
    'isNew': False
}

#Get an entry:
car_make = car['make']
car_year = car.get('year')

#Add an entry:
car['colour'] = 'Red'

#Update an entry:
car['colour'] = 'Blue'

# Delete an entry:
del car['colour']

# dictionary functions
car_properties_list = car.items()
car_keys = car.keys()
car_values =  car.values()
#Empty the directory
car.clear()

#check if key is in dictionary
if 'colour' in car:
    print("yes")
```

### Functions

```py
# With arguments
def add_numbers(a, b):
  return a + b

# Without arguments
def get_name():
  return 'Alice'

# invoke a function
my_sum = add_numbers(1, 2)
print(my_sum)

name = get_name()
print(name) # Alice

# arbitrary arguments
def print_names(*args):
    for person in args:
        print(person)

print_names("Alice", "Bob", "John")

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    print (result)

concatenate(a="Real", b="Python", c="Is", d="Great", e="!")

```
