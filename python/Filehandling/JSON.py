#Store 5 students data in dict as {"9843": {"name": "Rabindra", "age": 30, "course": "Python"}, "9844": {"name": "Hari", "age": 25, "course": "Java"}....}. Save this data in file info.json.
import json
students = {
    "9843": {
        "name": "Rabindra",
        "age": 30,
        "course": "Python"
    },
    "9844": {
        "name": "Hari",
        "age": 25,
        "course": "Java"
    },
    "9845": {
        "name": "Sita",
        "age": 22,
        "course": "Django"
    },
    "9846": {
        "name": "Gita",
        "age": 28,
        "course": "Data Science"
    },
    "9847": {
        "name": "Ram",
        "age": 24,
        "course": "Machine Learning"
    }
}
with open (r"C:\Users\User\Desktop\info.json", "w", newline="", encoding="utf-8") as file:
    json.dump(students, file, indent=4)
print("info.json created successfully!")

#Load info.json file. Convert the data in list of dictionary like [{"phone": "9843", "name": "Rabindra", "age": 30, "course": "Python"}, ....]. Save coverted data in info.csv file.
import json

    