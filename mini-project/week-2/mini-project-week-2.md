# Mini Project Week 2

So far we've been using one-dimensional lists of data, however, this won't work for orders. We need to store more information such as the customer's name, address and phone number, as well as the status of the order. To solve this we'll use a two-dimensional data structure, a `dictionary`. We won't be able to read/write this structure to a text file anymore, but we'll fix this later.

For now we'll also skip adding products to the order.

## Goals

As a user I want to:

- create a product or order, and add it to the relevant list
- view all products or orders
- _STRETCH_ I want to be able to update or delete a product or order

## Spec

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
PRINT main menu options
GET user input for main menu option

IF user input is 0:
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

# orders menu
ELSE IF user input is 2:
    IF user input is 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT orders list (of dictionaries)

    ELSE IF user input is 2:
        GET user input for customer name
        GET user input for customer address
        GET user input for customer phone number

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
