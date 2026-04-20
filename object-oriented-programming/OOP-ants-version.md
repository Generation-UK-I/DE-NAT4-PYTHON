# Introduction to Object Oriented Programming (OOP)

This guide explores the concept of OOP, specifically in relation to Python classes.

## What is Object-Oriented Programming?

Python is an example of an object-oriented programming language.

In OOP we create and work with `objects`, which are unique instances of *something*!

Examples:

- If I want to create an app for managing my pet's worm and flea treatments, I need *something* (an object) in the app which represents and stores info for each pet.
- If I want to create a game which has lots of enemies, I need objects to represent each one, allowing each individual bad-guy to have their own characteristics like a health bar, different weapons, special attacks, etc.
- If I make an app for a coffee shop, each individual coffee, with it's specific options, needs to be tracked from ordering to completion.

These are all examples where object-oriented programming can be useful. 

- Each pet can be an object
- Each enemy in the game can be an object
- Each coffee can be an object
- *Anything can be an object*

This approach allows us to then write code which works with our objects, and write functions specific to those objects.

So, if a customer selects Caramel Syrup in their coffee, we can write a line of code which adds that option to the specific object that requires it, but not every object/coffee - OOP allows individual objects to be handled differently, and call different functions against them.

## Python Classes

In Python, `classes` are how we make objects, they're like object __constructors__, or a blueprint for creating new objects.

```py
class Dog():
    #an attempt to model a dog
    def __init__(self, name, age):
        #assign the dog's name and age
        self.name = name
        self.age = age

    def eat(self): # Method
        # Dogs can eat
        print(f"{self.name} is eating, as usual!")

    def sleep(self): # Method
        # Dog can sleep
        print(f"Sssshhh!! {self.name} is fast asleep!")
```

In the example above we've created three methods `def __init__(self, name, age)`, `def eat(self)` and `def sleep(self)`, but the first one is likely the most unfamiliar.

>A function that is within a class is called a `method` and is available to objects created by the class. We've called many methods previously, because everything in Python is actually an object, with associated methods.

We can create as many methods for our classes as we want, but the first one is always `def __init__(self,...)`.

### The `__init__()` Method

```py
class Dog():
    # modelling a dog
    def __init__(self, name, age):
        #assign the dogs name and age
        self.name = name
        self.age = age
```

All classes require a method called `__init__()`, which is always executed when the class is being _initiated_, and is used to *construct* each new object, therefore it's often called a `constructor`.

In our case the `__init__()` method has three attributes: `self`, `name`, and `age`. Self is required, but we don't need to provide a value for it (*we'll come back to `self` shortly*), the remaining attributes represent the attributes of the object being created. So creating a dog object with the class above, just requires a name and an age.

When you call your class you provide values for the attributes, and the `__init__()` method passes them through to individual object being constructed (Just like arguments/parameters when creating functions).

You can call the class as many times as you want, pass different values through to the attributes, and create as many unique objects as you want.

### The `self` Parameter

The `self` parameter is a reference to the instance itself, this can be a litle confusing at first.

__Remember: The purpose of classes is to make unique objects - and each object needs to be able to reference it's own unique attributes.__

Think of the game example again, your class creates enemies and each enemy might start the same, but they each need their own health bar; perhaps you want them to be different colours; perhaps each individual can dodge when you target them. Self gives each individual instance access to it's own set of attributes, and access to it's own methods.

So, if you give your enemies a method allowing them to dodge out of your way (`dodge()`), they won't all dodge at the same time, only the unique object that called it's `dodge()` method.

Looking at our example again

```py
class Dog():
    # modelling a dog
    def __init__(self, name, age):
        #assign the dogs name and age
        self.name = name
        self.age = age
```

You can see that each dog created by our class can have it's own name and age, we can add more attributes if we wish: breed, weight, fur_colour, etc... By adding attributes as key-value pairs in this manner, we can model almost anything as a class (*similar to dictionaries*).

To call our class and create a dog, we just need to provide the name and age of the dog(s) we want to create.

```py
... # Omitted code

sausage_1 = Dog("frankie", 6)
sausage_2 = Dog("scout", 3)

print(sausage_1, sausage_2) # Returns info about the created objects
```

### Calling Methods

We've also gave our dogs the ability to eat and sleep.

```py
... # Omitted code

    def eat(self):
        #dogs can eat
        print(f"{self.name} is eating, as usual!")

    def sleep(self):
        #The dog can sleep
        print(f"Sssshhh!! {self.name} is fast asleep!")
```

These methods, since they're within a class, are available to each dog that is created via the `self` attribute. In this case each method just prints out a message which includes the specific instance's `name` attribute, saying what the dog is doing. However, the code in the method could do something much more complex, and use any of the object's attributes.

To call a method simply give the name of the object and method you want to call, separated by a dot, as we've done with string methods, list methods, dictionary methods, and so on, we call this dot notation. If your method requires any parameters, provide them in the brackets.

```py
... # Omitted code

sausage_1 = Dog("frankie", 6)
sausage_2 = Dog("scout", 3)

sausage_1.eat()
sausage_2.sleep()
```

>If you call a class or method without providing the necessary arguments, you'll receive a TypeError relating to positional arguments.

### Accessing Attributes

Dot notation also allows us to access the instance's individual attributes directly.

```py
...

sausage_1 = Dog("frankie", 6)
sausage_2 = Dog("scout", 3)

print(f"My oldest dog's name is {sausage_1.name}")
print(f"My youngest dog is {sausage_2.age} years old")
```

### Default Values for an Attribute

If we want the instances created by a class to have another attribute, which is the same for all or most of the instances, we can add it with a default value.

```py
class Dog():
    # modelling a dog
    def __init__(self, name, age):
        #assign the dogs name and age
        self.name = name
        self.age = age
        self.animal_type = 'dog'
        self.animal_voice = 'woof'
```

Now we have an additional attributes for `animal_type` and `animal_voice` with default values of `dog` and 'woof'. Since this class makes dogs, so it makes sense that these attributes are assigned every dog object.

We can add a new method, and call upon these attributes just like the others

```py
...

    def animal_species(self):
            print(f"{self.name} is a {self.animal_type}")

    def animal_sound(self):
        print(f"{self.name} is {self.animal_voice}ing")
...

sausage_1.animal_species()
sausage_2.animal_sound()
```

### Modifying Attribute Values

An attributes values may be modified directly by simply defining a new value to it using dot notation

```py
...

sausage_1 = Dog("frankie", 6)
print(f"{sausage_1.name} is {sausage_1.age}")

sausage_1.age = 5 
print(f"{sausage_1.name} is {sausage_1.age}")
```

You may also create a method to update the value of an attribute which you can call when needed

```py
...

    def animal_species(self):
        print(f"{self.name} is a {self.animal_type}")

    def animal_sound(self):
        print(f"{self.name} is {self.animal_voice}ing")

    def change_species(self, species):
        self.animal_type = species
        
sausage_1 = Dog("frankie", 6)
print(f"{sausage_1.name} is a {sausage_1.animal_type}")

sausage_1.change_species('cat')
print(f"{sausage_1.name} is a {sausage_1.animal_type}")
```

Here the animal_species method has an additional parameter, not included in the `__init__` method, for which we need to provide an argument dog when we call it.

### Type Hinting

Type hinting allows you to indicate the expected data types of variables, function parameters, and return values. In OOP, it is particularly useful for ensuring parameters used by class methods are passed with the correct data type. By defining within the __init__ method, you can avoid repetition and unnecessary code by doing type conversions within the individual methods.

- When defining a function, you can define what type the arguments are
  - The type for each argument is defined after the colon `a: int`
  - The return type of the function is shown by the arrow `-> int`

```py
# Arguments a and b are of type int; returns an int
def add_numbers(a: int, b: int) -> int:
    return a + b

# Arguments a and b are of type string; returns a str
def add_strings(a: str, b: str) -> str:
    return a + b

add_numbers(1, 2)
add_strings("hello", " world")
```

Another example:

```py
class Product:
    def __init__(self, price: float, is_available: bool) -> None:
        self.price = price
        self.is_available = is_available
```

## The Four Principles of OOP

The four fundamental principles of OOP are:

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

These principles help create organized, reusable, and maintainable code.

### Encapsulation

Encapsulation is about bundling properties (date), and methods that operate on that data within a single unit (class). 

We can control access to properties, and how they're used by providing specific methods for accessing or modifying them.

>For example, in one of our earlier examples, we implemented a method to change the species attribute for the dog class.

Encapsulation provides context to variables and functions, imagine you have a **dog** class and a **cat** class; a dog barks while a cat meows. We can ensure that the `bark()` method and the `meow()` method can only be called by the relevant class, preventing you calling the wrong function with the wrong type.

### Abstraction

Abstraction is about hiding complex implementation details, and showing only essential features to the user.

- The user does not need to know how things work in order to use them
- They just need to know that they exist, and how they should be used
- Implementation specifics can be hidden and changed, as long as they continue to provide a consistent user interface.

**Example**: Looks at the [abstraction.py](./handouts/abstraction.py) file in the `./handouts` folder.

- Run the code and observe the output.
- Notice how few lines of code need to be presented to the user on the main page.

>In reality, this user facing code is more likely to be a user facing GUI, and the classes and functions are called by pressing buttons instead (the button will still just call `my_class(attributes)` in the background).

Some of the benefits of Abstraction include:

- Simplifies user interaction
- Reduces cognitive load for developers deciphering your code later
- Allows you to implement changes without affecting users

### Inheritance

Inheritance in OOP allows us to create new classes (`child` classes) based on existing classes (`parent` classes).

The child class __inherits__ the attributes & methods of the parent, making code reuseable, as you don't have to re-write methods that both the parent and child need access to. __However, child classes can override or extend parent class methods to allow for different behaviours__.

```py
# Define our base type
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"

# Derive a sub-type
class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title

    def describe_profession(self):
        return f"I work as a {self.job_title}"

employee_1 = Employee("Ant", "Instructor")
print(employee_1.introduce()) # Ant can call the Person method 'introduce'
print(employee_1.describe_profession()) # Ant can call the Employee method 'describe_profession'

person_1 = Person("Bob")
print(person_1.introduce()) # Bob can call the Person method 'introduce' 
print(person_1.describe_profession()) # Bob cannot call the Employee method
```

In the above code the last line fails with the error: `AttributeError 'Person' object has no attribute 'describe_profession'`, the Employee object inherits the methods of the Person class, but the Person object is not able to access the Employee methods.

#### The `super().__init__()` Function

- The `super()` function helps Python make connections between a parent it's child class.
- The `__init__` method links the attributes required for the child class and the parent.

```py
class Person:
    def __init__(self, name): # A Person only requires the attribute 'name'
        self.name = name

    def introduce(self):
        return f"I am {self.name}"

class Employee(Person):
    def __init__(self, name, job_title): # An Employee has an additional attribute compared to a Person
        super().__init__(name) # 'name' in the child class is linked to 'name' in the parent class, allowing the parent's method to be called.
        self.job_title = job_title
```

### Polymorphism

Polymorphism is the ability of objects of different classes to respond to the same method call in their own way.

Key Concepts:

- The same method can take many forms - Providing the same interface, but with different implementations
- Method overriding - Child classes provide specific implementations
- Duck typing - "If it walks like a duck and quacks like a duck..."

#### Overriding Methods

We can override methods from the parent class, if we want the child to do it differently. Below we want Employees to introduce themselves differently to a Person.

```py
class Employee(Person):
    def __init__(self, name, job_title): # An Employee has an additional attribute compared to a Person
        super().__init__(name) # 'name' in the child class is linked to 'name' in the parent class, allowing the parent's method to be called.
        self.job_title = job_title

    def introduce(self):
        return f"I am {self.name}, and I am a {self.job_title}"

staff_1 = Employee("Ant", "Instructor")
print(staff_1.introduce()) # Calls the Employee's 'introduce' method

person_1 = Person("Bob")
print(person_1.introduce()) # Calls the Person's 'introduce' method
```

Another classic scenario to illustrate this concept is to consider shapes for which you want to calculate the area, by calling a `calc_area()` method. The problem is that the calculation is different for every shape, so every shape needs to implement `calc_area()` differently.

[See an example of this scenario here](./handouts/polymorphism.py)

# OOP Challenge

- Create a class to represent an adult
  - Include as many attributes as you can for an adult.
  - Create methods utilising these attributes (print statements will suffice), such as `def current_task(self, job_title): print(f"adult_1 is currently at their job as a {job_title}")`
- Create a child class to represent a 'child'
  - Add additional attributes such as `favourite_toy`
  - Add child specific methods, including at least one override method.

You may wish to review code examples from the Accenture OOP slides for further guidance.
