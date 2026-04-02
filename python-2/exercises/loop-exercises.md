# Python 2 Exercises

## Loops

1. Print the numbers 0 to 10 using a for loop.
2. Print the numbers 0 to 10 using a while loop.
3. Print the list of numbers below using a for loop.

    ```py
    numbers_list = [0, 2, 8, 20, 43, 82, 195, 204, 367]
    ```

4. Print the message 'Done!' after printing the numbers 0 to 10 with a for loop. Hint: use the `for-else` construct.

5. Take the below two lists and use a nested for loop to determine if any elements from the first list are in the second. If it finds a match, print out the name of the element.

    ```py
    list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
    list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
    ```

6. Using a while loop, on every iteration generate a random number. If it's a multiple of 5, **break** from the loop. If it's a multiple of 3, end the current iteration with **continue** and print a message to show you are skipping. If it's neither, print the number and continue the loop.

    When the loop has been broken, print a message indicating that this has happened before the program exits.

    Hint:

    ```py
    import random
    x = random.randint(1,100)
    ```
