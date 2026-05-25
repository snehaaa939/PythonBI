# Create a csv file std_1.csv with columns: Name, Age, Grade. Add 5 records to it using list of list.
import csv

Students = [
    ["Name", "Age", "Grade"],
    ["Ram", 20, "A"],
    ["Sita", 18, "B"],
    ["Sneha", 21, "A"],
    ["Preeti", 21, "A"],
    ["Krishna", 20, "B+"],
]
with open(r"C:\Users\User\Desktop\std1.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(Students)
print("std_1.csv created successfully.")


# Create a csv file std2.csv with columns: Name, Age, Grade. Add 5 records to it using list of dict.
Studentsdict = [
    {"Name": "Ram", "Age": 20, "Grade": "A"},
    {"Name": "Sita", "Age": 18, "Grade": "B"},
    {"Name": "Sneha", "Age": 21, "Grade": "A"},
    {"Name": "Preeti", "Age": 21, "Grade": "A"},
    {"Name": "Krishna", "Age": 20, "Grade": "B+"},
]
with open(r"C:\Users\User\Desktop\std2.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "Grade"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(Studentsdict)
print("std2.csv created successfully!")

# Read file 2022-01-03.csv and display records as list of list.

with open(r"C:\Users\User\Downloads\2022-01-03.csv", "r", encoding="utf=8") as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)
print(data)
for row in data:
    print(row)

# Read file 2022-01-03.csv and display records as list of dict.
with open(r"C:\Users\User\Downloads\2022-01-03.csv", "r", encoding="utf=8") as file:
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)
    print(data)
for row in data:
    print(row)
