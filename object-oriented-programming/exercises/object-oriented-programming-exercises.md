## OOP Exercises

# Part 1

1. Create a `Vehicle` class without any attribute and methods.

2. Extend the `Vehicle` class to contain attributes for max speed and colour. Instantiate the class and print out the attributes.

3. Extend the `Vehicle` class to contain methods for the below. Instantiate the class and call the two methods to update the attributes. Print the changes out.
    - Change the value of max speed
    - Change the car colour

# Part 2

1. Create a child class `Bus` that will inherit all of the variables and methods of the Vehicle class and nothing else. Instantiate a `Bus` instance and print out the attributes.

2. Use one of the built-in Python functions to print out the underlying object type of the `Bus` object.

3. Use one of the built-in Python functions to print out if the `Bus` object is an instance of `Vehicle`.

4. Extend the `Bus` class to also contain an attribute of `seating_capacity`. Add a method to calculate the price of a ticket. This is calculated as `seating_capacity * 0.05`, with an extra 10% of the total of `seating_capacity * 0.05` on top. Instantiate a `Bus` instance and print the ticket price.

5. Research how to print a `Bus` object in a printable representation. Hint: Look up overriding the `__str__` function. It should print something like `Bus: Max speed: 120, Colour: white, Seating capacity: 40`.
