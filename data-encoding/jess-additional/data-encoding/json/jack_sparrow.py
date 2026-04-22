import json

# Our JSON object representing Jack Sparrow
jack_sparrow = {
    "name": "Jack Sparrow",
    "role": "Pirate Captain",
    "ship": "Black Pearl",
    "bounty": 5000000,
    "traits": ["Cunning", "Resourceful", "Unpredictable"],
    "allies": [
        {"name": "Will Turner", "role": "Blacksmith turned Pirate"},
        {"name": "Elizabeth Swann", "role": "Pirate Lord of the South China Sea"}
    ]
}

# Writing the JSON data to a file
with open('jack_sparrow.json', 'w') as json_file:
    json.dump(jack_sparrow, json_file, indent=4) #mention indent=4 here after running

print("Jack Sparrow's data has been saved to jack_sparrow.json")

#Show Empty JSON file before runnin
#reading the file and decode its contents
with open('jack_sparrow.json', 'r') as json_file:
    jack_data = json.load(json_file)

# Print the data to verify
print("Name:", jack_data["name"])
print("Ship:", jack_data["ship"])
print("Allies:", [ally["name"] for ally in jack_data["allies"]])

