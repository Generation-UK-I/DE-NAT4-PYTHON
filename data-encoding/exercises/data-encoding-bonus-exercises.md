# Data Encoding - Bonus Exercises

## CSV

Use python to read in the data from `ford_escort.csv`.

### CSV Exercise 1

Sort the data by price, from highest to lowest and print out the sorted data.

### CSV Exercise 2

Group the cars by year, and print the count, so that for example we can answer the question "How many cars do we have available that were made in 1997?".

## JSON

### JSON Exercise 1

Given the following JSON data:

```json
{
  "library": {
    "books": [
      {
        "title": "Python Programming",
        "author": {
          "first_name": "John",
          "last_name": "Doe",
          "birth_year": 1975
        },
        "genres": ["Programming", "Technology"]
      },
      {
        "title": "Data Science Handbook",
        "author": {
          "first_name": "Jane",
          "last_name": "Smith",
          "birth_year": 1980
        },
        "genres": ["Data Science", "Machine Learning"]
      }
    ]
  }
}
```

- Write a Python function to parse the JSON data out of a file, and print out the full name of each author.
- Extract and print the titles of books that belong to the "Programming" genre.
- Create a list of authors born before the year 1980 and print it.

### JSON Exercise 2

Given the following JSON data:

```json
{
  "users": [
    {
      "user_id": 1,
      "name": "Alice",
      "activities": [
        {"type": "login", "timestamp": "2024-01-01T12:00:00Z"},
        {"type": "purchase", "item": "Laptop", "amount": 1200},
        {"type": "purchase", "item": "Books", "amount": 45}
      ]
    },
    {
      "user_id": 2,
      "name": "Bob",
      "activities": [
        {"type": "login", "timestamp": "2024-01-02T15:00:00Z"},
        {"type": "login", "timestamp": "2024-01-02T16:00:00Z"},
        {"type": "purchase", "item": "Phone", "amount": 800}
      ]
    },
    {
      "user_id": 3,
      "name": "Charlize",
      "activities": [
        {"type": "login", "timestamp": "2024-01-01T12:00:00Z"},
        {"type": "login", "timestamp": "2024-02-02T12:00:00Z"}
        {"type": "login", "timestamp": "2024-03-02T12:00:00Z"}
      ]
    },
  ]
}
```

- Write a Python function to parse the JSON data from a file and print the names of users who have made a purchase.
- Calculate the total amount spent by each user and print a summary.
- Identify and print the user who has logged in the most number of times.
