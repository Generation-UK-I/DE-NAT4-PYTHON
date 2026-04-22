# Data encoding exercises

## Part 1 - Reading and writing CSV

1. Read the `ford_escort.csv` example file using the Python csv library and print each row. Remember there's a header line!

2. Extend the above so that the data is read into a dictionary.

3. Write the following data as CSV to a file. Add a header row with likely column titles.

```py
['Joe', 'Bloggs', 40]
['Jane', 'Smith', 50]
```

4. Write another block of code that will **append** the following data to the file created in #3.

```py
['Mike', 'Wazowski', 40]
```

## Part 2 - Reading and writing JSON

1. Read the `menu_items.json` handout file using the native Python json library. Print the object that is created.

2. Print the "id" of all the items in the menu.

3. Write the following data as JSON to a file:

```py
{
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}
```

### Part 3 Bonus Exercises

If you finish these, there are extra CSV and JSON exercises available in [data-encoding-bonus-exercises.md](./data-encoding-bonus-exercises.md).
