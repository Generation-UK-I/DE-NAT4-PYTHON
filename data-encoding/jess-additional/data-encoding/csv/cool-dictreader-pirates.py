import csv

# Read the CSV into a list of dictionaries; emppty at top
pirates = []
with open('pirates.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        pirates.append(row)  # Store each row (dictionary) in a list

# Function to filter pirates by bounty; greater than threshold
def filter_by_bounty(pirates, threshold):
    return [pirate for pirate in pirates if int(pirate['bounty']) > threshold]

# Function to display pirate details
def display_pirates(pirates):
    for pirate in pirates:
        print(f"Pirate {pirate['name']} commands the ship {pirate['ship']} with a bounty of {pirate['bounty']}.")

# Display all pirates first
print("All Pirates:")
display_pirates(pirates)

# filter the pirates with a bounty greater than 600,000 and display them
high_bounty_pirates = filter_by_bounty(pirates, 600000)
print("\nHigh Bounty Pirates:")
display_pirates(high_bounty_pirates)

# Modify the bounty of the first pirate and display the updated list
pirates[0]['bounty'] = '1000000'  # Change bounty of the first pirate
print("\nUpdated Pirates with Modified Bounty:")
display_pirates(pirates)
