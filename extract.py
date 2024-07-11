import csv
import json

# Define the path to your input text file
file_path = "GB.txt"

# Define the path to the output JSON file
output_file = "places_gb.json"

# Initialize an empty dictionary to store results
gb_places_dict = {}

# Open and read the text file
with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")

    # Iterate through each line in the file
    for row in reader:
        # Ensure the entry is a populated place (feature class 'P')
        if row[6] == "P":  # Ensure it's a populated place
            # Extract relevant data: name, latitude, longitude
            name = row[1]
            latitude = float(row[4])
            longitude = float(row[5])

            # Add to dictionary with name as key and (latitude, longitude) as value
            gb_places_dict[(name.lower())] = {
                "latitude": latitude,
                "longitude": longitude,
            }

# Save the dictionary to a JSON file
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(gb_places_dict, json_file, indent=4)

print(f"Saved {len(gb_places_dict)} places to {output_file}")
