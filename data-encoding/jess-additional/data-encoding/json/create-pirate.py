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
with open('pirate-db.json', 'w') as json_file:
    json.dump(jack_sparrow, json_file, indent=4)

print("Jack Sparrow's data has been saved to pirate-db.json")

