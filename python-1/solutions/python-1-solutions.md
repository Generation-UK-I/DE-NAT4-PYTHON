# Python 1 Exercises

Please note that your answer does not have to match the below answers like-for-like. As long as it generally follows the same patterns and has the same outputs, then there is no problem with that.

## Part 1

### Strings

1. Create a variable which will store your first name. Print out the variable.

    ```py
    first_name = 'John'
    print(first_name)
    ```

2. Create a second variable which will store your last name. Concatenate the two variables and print out the result.

    There are two ways of solving this:

    ```py
    first_name = 'John'
    last_name = ' Smith'
    print(first_name + last_name)
    ```

    ```py
    first_name = 'John'
    last_name 'Smith'
    print(f'{first_name} {last_name}')
    ```

3. Extend the above to print the following using an `f-string`: `Hi, my name is {first_name} {last_name}`.

    ```py
    first_name = 'John'
    last_name 'Smith'
    print(f'Hi, my name is {first_name} {last_name}')
    ```

### Integers

1. Create two variables that store integer values. Calculate the product of the two integers and store it in a third variable. Print the value of this variable.

    ```py
    x = 10
    y = 20
    result = x * y
    print(result)
    ```

2. Extend the above to print out the following: `The product of {x} and {y} is {product}`, replacing `x, y, product` with the values for the above.

    ```py
    x = 10
    y = 20
    result = x * y
    print(f'The product of {x} and {y} is {result}')
    ```

### Lists

```py
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
```

1. Retrieve the third element, `Mark` (the second-indexed element) and store it in its own variable. Print the variable.

    ```py
    third_person = people[2]
    print(third_person)
    ```

2. Retrieve the element third from the back, `Joe`, and store it in its own variable. Print the variable.

    ```py
    third_to_last_person = people[-3]
    print(third_to_last_person)
    ```

3. Split the list into a new list with just the names `Mark`, `Lisa`, `Joe` and `Barry`.

    ```py
    sub_list = people[2:6]
    print(sub_list)
    ```

4. Compare the first and last element in the list, and print out the result of comparing them.

    ```py
    print(people[0] == people[-1])
    ```

### Input

1. Accept input from the user by asking for their name. Print their name out.

    ```py
    name = input('What is your name? ')
    print(name)
    ```

2. Accept two integers inputs from the user and calculate the product. Print out the product.

    ```py
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))
    product = num1 * num2
    print(product)
    ```

3. Accept two integer inputs from the user. Use the comparison operator to print out if the two values are equal (`True`), or if they're not (`False`).

    ```py
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))
    print(num1 == num2)
    ```

## Part 2

### Input and Numbers

1. Accept an integer input from the user. If the number is even, print out an appropriate message, and vice versa if it even odd.

    ```py
    num = int(input('Please input a number: '))
    mod = num % 2

    if mod > 0:
        print('You picked an odd number')
    else:
        print('You picked an even number')
    ```

2. Extend the above to print a different message if the number is a multiple of four.

    ```py
    num = int(input('Please input a number: '))

    if num % 4 == 0:
        print('You picked a multiple of 4')
    elif num % 2 == 0:
        print('You picked an even number')
    else:
        print('You picked an odd number')
    ```

3. Accept an integer input from the user. If the number is a multiple of three, print the word `fizz`. If the number is a multiple of five, print `buzz`. If it is neither of these, do nothing.

    ```py
    num = int(input('Please input a number: '))

    if num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    ```

### Temperature Conversion

1. Write a program that will convert celsius to fahrenheit, and vice versa. Accept two inputs from the user. The first will be a letter which is either `c`, which means you should convert from fahrenheit to celsius, or `f` which is vice versa. For the second input, accept an integer value representing the temperature. Print out the converted value, along with the correct temperature type.

    ```py
    temperature_type = input('Which temperature scale would you like to convert to? ')
    temperature_value = int(input('Input your temperature: '))

    if temperature_type == 'c':
        converted_temp = (temperature_value - 32) * (5 / 9)
        print(f'{temperature_value}f is {converted_temp}c')

    elif temperature_type == 'f':
        converted_temp = (temperature_value * 1.8) + 32
        print(f'{temperature_value}c is {converted_temp}f')
    else:
        print('Temperature scale was neither c or f.')
    ```

## Part 3

1. In your own words, describe each of the following logical operators: `and`, `or` and `not`.

    > `OR` dictates that as long as at least one condition is true, the whole expression is true.
    If at least one of a or b is true, then the whole expression is true.
    If both are false, then the whole expression is false.
    > `AND` dictates that all conditions of an expression must be true, for the whole expression to be true.
    If a AND b are both true, then the whole expression is true.
    If either a or b, or both, are false, then whole expression is false.
    > `NOT` dictates that any value or condition will be inverted.
    True becomes false, false becomes true.

2. Consider the below code. Write down what you think the expected output will be.

    Expected output:
    > False
    True
    True
    True

3. Consider the below code. Write down what you think the expected output will be.

    Expected output:
    > False
    False
    False
    True

4. Without referring back to the slides, write down the truth table for each of the three logical operators.

    **AND**:
    | a   | b   | AND |
    | --- | --- | --- |
    | T   | T   | T   |
    | T   | F   | F   |
    | F   | T   | F   |
    | F   | F   | F   |

    **OR**:
    | a   | b   | OR  |
    | --- | --- | --- |
    | T   | T   | T   |
    | T   | F   | T   |
    | F   | T   | T   |
    | F   | F   | F   |

    **NOT**:
    | a   | NOT |
    | --- | --- |
    | T   | F   |
    | F   | T   |

5. Create a program for the following Bank Loan specification...

    ```py
    age = int(input('Please enter your age: '))
    salary = int(input('Please enter your salary: '))

    if age >= 30 and salary >= 50000:
        print('We can offer a loan of up to £100,000')
    elif age >= 30 and salary >= 30000:
        print('We can offer a loan of up to £75,000')
    elif age >= 21 and salary >= 21000:
        print('We can offer a loan of up to £50,000')
    else:
        print('Sorry, we cannot offer you a loan')
    ```
