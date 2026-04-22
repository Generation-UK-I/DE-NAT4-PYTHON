import csv

with open('pirates.csv.txt', 'w') as file:  
    keys = ['name', 'ship', 'bounty']  # define our column names
    writer = csv.DictWriter(file, keys)  

    writer.writeheader()  # Write column names as the first row

    # Adding pirates to the CSV using dictionaries
    writer.writerow({'name': 'Blackbeard', 'ship': "Queen Anne's Revenge", 'bounty': 1200000})
    writer.writerow({'name': 'Angelica Teach', 'ship': "Queen Anne's Revenge", 'bounty': 950000})
    writer.writerow({'name': 'James Norrington', 'ship': 'Dauntless', 'bounty': 300000})
    writer.writerow({'name': 'Bartholomew Roberts', 'ship': 'Royal Fortune', 'bounty': 850000})
    writer.writerow({'name': 'Calico Jack Rackham', 'ship': 'Ranger', 'bounty': 400000})
    


