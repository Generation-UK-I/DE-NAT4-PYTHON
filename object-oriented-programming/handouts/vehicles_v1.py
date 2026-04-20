# A list of all the vehicles owned by the company
vehicles = [
    {
        'make': 'Skoda',
        'model': 'Octavia',
        'engine': 1.4,
        'mileage': 16100,
    },
    {
        'make': 'Toyota',
        'model': 'Corolla',
        'engine': 1.6,
        'mileage': 32900,
    }
]

def print_report(vehicle):
    # Calculate carbon emissions for a vehicle based on engine size and mileage
    emissions = vehicle['engine'] * vehicle['mileage'] / 100

    # Print all details for a single vehicle
    print(f"MAKE     : {vehicle['make']}")
    print(f"MODEL    : {vehicle['model']}")
    print(f"ENGINE   : {vehicle['engine']} litres")
    print(f"MILEAGE  : {vehicle['mileage']} miles")
    print(f"EMISSIONS: {emissions} cubic litres")
    print(f"")

# Generate a report for all vehicles in the fleet
for vehicle in vehicles:
    print_report(vehicle)
