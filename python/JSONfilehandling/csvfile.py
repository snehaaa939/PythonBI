import csv

data = [
    ["name", "age", "city"],
    ["Sneha", 21, "Kathmandu"],
    ["Ram", 25, "Lalitpur"],
    ["Shyam", 30, "Janakpur"],
]
with open("202301.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created!")
