# Mini Project Week 3

Now that our app can create and list products, and handle orders it should be simple enough to do the same for couriers. We'll also dump our data into `.txt` files so we don't lose it. Try to ensure code that writes or reads from a text file is separated from the code that prints a list for example.

## Goals

As a user I want to:

- create a product, courier, or order and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data (products and couriers)
- _STRETCH_ update or delete a product, order, or courier

## Spec

- A `courier` should just be a `string` containing its name, i.e: `"John"`
- A list of `couriers` should be a list of `strings`, i.e: `["John"]`
- Data should be persisted to a `.txt` file on a new line for each `courier` or `product`, ie:

    ```txt
    John
    Claire
    ```

- A `product` should just be a `string` containing its name, i.e: `"Mocha"`
- A list of `products` should be a list of `strings`, i.e: `["Mocha", "Americano"]`
- An `order` should be a `dictionary`, i.e:

    ```json
    {
        "customer_name": "John Jones",
        "customer_address": "Main Street, LONDON",
        "customer_phone": "07987654321",
        "status": "preparing"
    }
    ```

- A list of `orders` should be a `list` of `dictionary` objects, i.e: `[{...},{...}]`

## Pseudo Code

```txt
LOAD products list from products.txt
LOAD couriers list from couriers.txt
CREATE orders list of dictionaries
CREATE order status list

PRINT main menu options
GET user input for main menu option

IF user input is 0:
    SAVE products list to products.txt
    SAVE couriers list to couriers.txt
    EXIT app

# products menu
ELSE IF user input is 1:
    PRINT product menu options
    GET user input for product menu option

    IF user inputs 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT products list

    ELSE IF user input is 2:
        # CREATE new product
        GET user input for product name
        APPEND product name to products list

    ELSE IF user input is 3:
        # STRETCH GOAL - UPDATE existing product

        PRINT product names with its index value
        GET user input for product index value
        GET user input for new product name
        UPDATE product name at index in products list

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE product

        PRINT products list
        GET user input for product index value
        DELETE product at index in products list

# couriers menu
ELSE IF user input is 2:
    PRINT courier menu options
    GET user input for courier menu option

    IF user inputs 0:
        RETURN to main menu

    ELIF user inputs 1:
        PRINT couriers list

    ELSE IF user input is 2:
        # CREATE new courier
        GET user input for courier name
        APPEND courier name to couriers list

    ELSE IF user input is 3:
        # STRETCH GOAL - UPDATE existing courier

        PRINT courier names with its index value
        GET user input for courier index value
        GET user input for new courier name
        UPDATE courier name at index in couriers list

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE courier

        PRINT courier list
        GET user input for courier index value
        DELETE courier at index in courier list
# orders menu
ELSE IF user input is 3:
    IF user input is 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT orders list

    ELSE IF user input is 2:
        GET user input for customer name
        GET user input for customer address
        GET user input for customer phone number

        PRINT couriers list with index value for each courier
        GET user input for courier index to select courier
        SET order status to be 'PREPARING'
        APPEND order to orders list

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

        FOR EACH key-value pair in selected order:
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
