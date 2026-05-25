# Q1. Record of student is stored as {'9843': {'course': 'Python', 'name': 'Ram', 'present': False}, {'9844': {'course': 'Java', 'name': 'Shyam', 'present': True}}. Using loop, display name of student who are absent in Python class.

student_record = {
    "9843": {"course": "Python", "name": "Ram", "present": False},
    "9844": {"course": "Java", "name": "Shyam", "present": True},
}
for student_id, details in student_record.items():
    if details["course"] == "Python" and details["present"] == False:
        print(details["name"])


# Q2. Store a fruits names in a list. Generate a new list from it such that if fruit name starts with a/A then it has to be converted to uppercase else it has to be converted to lowercase. Use both for loop and list comprehension.
fruits_list = ["Apple", "Banana", "Avocado", "Mango", "Apricot"]
fruits = []
# For loop
for fruit in fruits_list:
    if fruit.lower().startswith("a"):
        fruits.append(fruit.upper())
    else:
        fruits.append(fruit.lower())
print("New list:", fruits)

# List comprehension
new_list = [
    fruit.upper() if fruit.lower().startswith("a") else fruit.lower()
    for fruit in fruits_list
]
print("New_list:", new_list)

# Q3. Write function to check if a number is prime or not. Using this function, generate list of first 20 prime numbers.


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Q4. Write function that accepts string from user and returns a dictionary for occurrences of a character in it. Ex: apple => {'a': 1, 'p': 2, 'l': 1, 'e': 1}.
result = {}


def character(text):
    for char in text:
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    return result


user_input = input("Enter a string: ")
output = character(user_input)
print(output)

