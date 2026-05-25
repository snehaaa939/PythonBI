import csv
import json

with open("202301.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)
print("Conversion completed!")
