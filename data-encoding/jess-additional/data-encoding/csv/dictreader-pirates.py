import csv

with open('pirates.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
