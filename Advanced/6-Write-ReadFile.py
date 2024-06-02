import json

# Sample data to write to a JSON file
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Python", "Data Science", "Machine Learning"]
}

# Write the data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been written to data.json")

# Read the data from the JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

print("Data read from data.json:")
print(data)
