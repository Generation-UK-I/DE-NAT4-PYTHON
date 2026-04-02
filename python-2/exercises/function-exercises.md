# Python 2 Exercises

## Functions

1. Create a function that takes two numbers as arguments and return the sum. Print the result.
2. Extend the above by passing an arbitrary amount of integers to a function and return the result. Print the result. Hint: use `*args`.
3. Pass an arbitrary amount of named arguments to a function and create a dictionary. The keys will be the names of the arguments and the values are assigned values of the named arguments. Hint: use `**kwargs`.

### Bonus - basic calculator

1. Create a scientific/basic calculator that makes use of separate functions to perform calculations, such as: `add`, `divide`, `area_of_a_circle` etc...
2. Add some form of user interface to allow the user to perform calculations
3. Print out a nice result / log to the screen

### Bonus - fibonacci sequence

Create a fibonacci function that returns `fib(n)`. So if i request `fib(100)` it returns the 100th position in the sequence. `n` is undetermined so working out a finite sequence beforehand is not acceptable ;)

```py
# The fibonacci sequence is the sum of the previous two values
# 1, 1, 2, 3, 5, 8, 13...

fib(7) # 13
fib(50) # ?
