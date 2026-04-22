# Data encoding bonus exercises

## CSV Bonus Solution

- Part 1 - Sort the data by price, from highest to lowest and print out the sorted data.
- Part 2 - Group the cars by year, and print the count

```py
import csv

def clean_header(header):
    return header.strip().replace('"', '').replace("'", '')

cars = []

with open('ford_escort.csv', newline='') as file:
    reader = csv.DictReader(file)
    reader.fieldnames = [clean_header(header) for header in reader.fieldnames]

    for row in reader:
        row['Year'] = int(row['Year'])
        row['Mileage (thousands)'] = int(row['Mileage (thousands)'])
        row['Price'] = int(row['Price'])
        cars.append(row)

    # Part 1 - Sort the data by price from highest to lowest
    sorted_cars = sorted(cars, key=lambda x: x['Price'], reverse=True)
    print('Data sorted by price (highest to lowest):')
    for car in sorted_cars:
        print(car)

    # Part 2 - Group the cars by year, and print the count
    cars_by_year = {}
    for car in cars:
        year = car['Year']
        if year in cars_by_year:
            cars_by_year[year] += 1
        else:
            cars_by_year[year] = 1

    print('\nCount of cars by year:')
    for year, count in cars_by_year.items():
        print(f'Year {year}: {count} cars available')
```

## JSON Bonus Solution 1

- Write a Python function to parse the JSON data out of a file, and print out the full name of each author.
- Extract and print the titles of books that belong to the "Programming" genre.
- Create a list of authors born before the year 1980 and print it.

```py
import json

# Load books
with open('books.json', 'r') as books_file:
    file_content = books_file.read()
    books_data = json.loads(file_content)

    books_list = books_data['library']['books']

    # 1 Author names
    for book in books_list:
        author = book['author']
        full_name = f'{author['first_name']} {author['last_name']}'
        title = book['title']
        print(f'{full_name} wrote {title}')

    # 2 Titles of programming books
    programming_title = 'Programming'
    for book in books_list:
        if programming_title in book['genres']:
            title = book['title']
            print(f'{title} is in {programming_title}')

    # 3 Authors before 1980
    max_year = 1980
    for book in books_list:
        author = book['author']
        if author['birth_year'] < max_year:
            full_name = f'{author['first_name']} {author['last_name']}'
            print(f'{full_name} was born before {max_year}')
```

## JSON Bonus Solution 2

- Write a Python function to parse the JSON data from a file and print the names of users who have made a purchase.
- Calculate the total amount spent by each user and print a summary.
- Identify and print the user who has logged in the most number of times.

```py
import json

# Load users
with open('users.json', 'r') as users_file:
    file_content = users_file.read()
    users_data = json.loads(file_content)

    # 1 - Users with Purchases
    user_list = users_data['users']
    purchase_type = 'purchase'
    for user in user_list:
        name = user['name']
        for activity in user['activities']:
            if purchase_type == activity['type']:
                print(f'{name} has a {purchase_type}')
                break

    # 2 - Totals sales per user
    user_totals = {}
    for user in user_list:
        name = user['name']
        user_totals[name] = 0
        for activity in user['activities']:
            if 'purchase' == activity['type']:
                user_totals[name] += activity['amount']

    print('Users Totals = ', user_totals)

    # 3 Most logins - one of many ways
    # ...make a list of user objects, then sort the objects in the list by user.logins
    user_logins = []
    for user in user_list:
        name = user['name']
        logins = 0
        for activity in user['activities']:
            if 'login' == activity['type']:
                logins += 1
        user_logins.append({'name': name, 'logins': logins})

    print('Unsorted Users Logins = ', user_logins)
    print('Highest user logins first:')
    print(sorted(user_logins, key=lambda x: x['logins'], reverse=True))

    # 3 Most logins - another way:
    # ...make a dictionary of user_name:count and sort by the values
    user_logins = {}
    for user in user_list:
        name = user['name']
        user_logins[name] = 0
        for activity in user['activities']:
            if 'login' == activity['type']:
                user_logins[name] += 1

    print('All Users Logins = ', user_logins)
    max_logins_user = max(user_logins, key=user_logins.get)
    print(f'User with max logins = {max_logins_user}')
```
