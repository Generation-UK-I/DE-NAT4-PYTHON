# Mini Project Week 4

Now that we've learned how to work with two-dimensional data, let's refactor our app to use dictionaries for both product and courier.

Building upon our use of a courier index within our order, let's create a list of product indexes now for order items.

We'll also need to refactor our storage layer to use `.csv` files rather than `.txt` to bring back our persistence functionality.

To show that our code works, we will also need to write unit tests to prove that our app works correctly.

## Goals

As a user I want to:

- create a product, courier, or order dictionary and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data
- _STRETCH_ update or delete a product, order, or courier
- _BONUS_ list orders by status or courier

## Spec

- A `product` should be a `dict`, i.e:

    ```json
    {
        "name": "Coke Zero",
        "price": 0.8 // Float
    }
    ```

- A `courier` should be a `dict`, i.e:

    ```json
    {
        "name": "Bob",
        "phone": "0789887889"
    }
    ```

- An `order` should be a `dict`, i.e:

    ```json
    {
        "customer_name": "John",
        "customer_address": "Main Street, LONDON",
        "customer_phone": "0789887334",
        "courier": 2, // Courier index
        "status": "preparing",
        "items": "1, 3, 4" // Product indexes
    }
    ```

- Data should be persisted to a `.csv` file on a new line for each `courier`, `order`, or `product`, ie:

    ```csv
    # ORDER
    John,"Main Street, LONDON",2,preparing,"1,3,4"
    ```

- Couriers, Products and Orders should all be saved in different files

## Pseudo Code

```txt
LOAD products from products.csv
LOAD couriers from couriers.csv
LOAD orders from orders.csv
CREATE order status list

PRINT main menu options
GET user input for main menu option

IF user input is 0:
    SAVE products list to products.csv
    SAVE couriers list to couriers.csv
    SAVE orders list to order.csv
    EXIT app

# products menu
ELSE IF user input is 1:
    PRINT product menu options
    GET user input for product menu option

    IF user inputs 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT products list

    # WEEK 4 UPDATE
    ELSE IF user input is 2:
        # CREATE new product

        GET user input for product name
        GET user input for product price
        CREATE new product dictionary with above properties
        APPEND product dictionary to products list

    # WEEK 4 UPDATE
    ELSE IF user input is 3:
        # STRETCH GOAL - UPDATE existing product

        PRINT products with their index values
        GET user input for product index value

        # iterate over the (key: value) pairs in the selected dictionary
        FOR EACH key-value pair in selected product dictionary:
            GET user input for updated property
            IF user input is blank:
                do not update this property and skip
            ELSE:
                update the property value with user input

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE product

        PRINT products list
        GET user input for product index value
        DELETE product dictionary at index in products list

# couriers menu
ELSE IF user input is 2:
    PRINT courier menu options
    GET user input for courier menu option

    IF user inputs 0:
        RETURN to main menu

    ELIF user inputs 1:
        PRINT couriers list

    # WEEK 4 UPDATE
    ELSE IF user input is 2:
        # CREATE new courier

        GET user input for courier name
        GET user input for courier phone number
        CREATE new courier dictionary with above properties
        APPEND courier dictionary to courier list

    # WEEK 4 UPDATE
    ELSE IF user input is 3:
        # STRETCH GOAL - UPDATE existing courier

        PRINT courier with their index values
        GET user input for courier index value

        # iterate over the (key: value) pairs in the selected dictionary
        FOR EACH key-value pair in selected courier dictionary:
            GET user input for updated property
            IF user input is blank:
                do not update this property and skip
            ELSE:
                update the property value with user input

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE courier

        PRINT courier list
        GET user input for courier index value
        DELETE courier dictionary at index in courier list

# orders menu
ELSE IF user input is 3:
    IF user input is 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT orders list

    # WEEK 4 UPDATE
    ELSE IF user input is 2:
        GET user input for customer name
        GET user input for customer address
        GET user input for customer phone number

        PRINT products list with its index values
        GET user inputs for comma-separated list of product index values
        CONVERT above user input to a string e.g. "2,1,3"

        PRINT couriers list with index value for each courier
        GET user input for courier index
        SET order status to be 'PREPARING'

        CREATE new order dictionary with above properties
        APPEND order dictionary to orders list

    ELSE IF user input is 3:
        # UPDATE existing order status

        PRINT orders list with its index values
        GET user input for order index value

        PRINT order status list with index values
        GET user input for order status index value
        UPDATE status for order

    ELSE IF user input is 4:
        # STRETCH - UPDATE existing order

        PRINT orders list with its index values
        GET user input for order index value

        # iterate over the (key: value) pairs in the selected dictionary
        FOR EACH key-value pair in selected order dictionary:
            GET user input for updated property
            IF user input is blank:
                do not update this property
            ELSE:
                update the property value with user input

    ELSE IF user input is 5:
        # STRETCH GOAL - DELETE order

        PRINT orders list with its index values
        GET user input for order index value
        DELETE order at index in order list
```
