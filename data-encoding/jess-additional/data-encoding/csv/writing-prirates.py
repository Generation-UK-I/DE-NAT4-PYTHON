import csv

with open('pirate-sample.txt', mode='w') as file:  #remember a!
    writer = csv.writer(file, delimiter=',')

    writer.writerow(['Anne Bonny', 'William', 600000])
    writer.writerow(['Charles Vane', 'The Ranger', 750000])
