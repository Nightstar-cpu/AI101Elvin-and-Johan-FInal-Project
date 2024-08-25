import csv
import json

csv_file_path = 'Churn_Modelling.csv'
json_file_path = 'Churn_Modelling.json'

data = []
with open(csv_file_path, mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

with open(json_file_path, mode='w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV data successfully converted to JSON and saved to {json_file_path}")