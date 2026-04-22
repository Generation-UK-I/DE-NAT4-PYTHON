# Data encoding exercises

## Part 1 - Reading and writing CSV

1. Read the `ford_escort.csv` example file using the Python csv library and print each row. Remember there's a header line!

    ```py
    import csv

    with open('ford_escort.csv') as file:
        reader = csv.DictReader(file, delimiter=',')
        next(reader) # skips the header
    for row in reader:
        print(row)
    ```

2. Extend the above so that the data is read into a dictionary.

    ```py
    import csv

    # DictReader skips the headers automatically
    with open('ford_escort.csv') as file:
        reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row)
    ```

3. Write the following data as CSV to a file. Add a header row with likely column titles.

    ```py
    import csv

    with open('people.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')

        writer.writerow(['Joe', 'Bloggs', 40])
        writer.writerow(['Jane', 'Smith', 50])
    ```

4. Write another block of code that will **append** the following data to the file created in #3.

    ```py
    import csv

    with open('people.csv', mode='a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Sally', 'Doe', 30])
    ```

## Part 2 - Reading and writing JSON

1. Read the `menu_items.json` handout file using the native Python json library. Print the object that is created.

    ```py
    import json

    with open('example.json', 'r') as file:
        data = json.load(file)

    print(data)
    ```

2. Print the "id" of all the items in the menu.

    ```py
    import json
    with open('example.json', 'r') as file:
        data = json.load(file)

    for item in data['menu']['items']:
        print(item['id'])
    ```

3. Write the following data as JSON to a file:

    ```py
    import json

    data = {
        'president': {
            'name': 'Zaphod Beeblebrox',
            'species': 'Betelgeusian'
        }
    }

    with open('data_file.json', 'w') as write_file:
        json.dump(data, write_file)
    ```
