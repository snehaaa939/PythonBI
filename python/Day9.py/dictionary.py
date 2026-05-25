# Q1. Assign student_info as {'name': 'Ram', 'age': 22, 'grade': 'A', 'courses': ['DS', 'SQL']}
# Find and display student's name, age, grade and courses enrolled with proper formatting
# Update student's grade to 'A+' and display updated dictionary
# Add 'level' key with value 'Beginner' and display updated dictionary
# Add one more course 'Python' to student's courses and display updated dictionary
# Remove age from student information and display updated dictionary
# Check if 'address' key is present in student information
# Find and display total number of items in student information
# Create a copy of this dictionary, update name to 'Bob', grade to 'B' and display both dictionary

student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}

# Find and display student's name, age, grade and courses enrolled with proper formatting
print(f"Student Name: {student_info['name']}")
print(f"Age: {student_info['age']}")
print(f"Grade: {student_info['grade']}")
print(f"Courses Enrolled:{', '.join(student_info['courses'])}")

# Update student's grade to 'A+' and display updated dictionary
student_info["grade"] = "A+"
print("Updated Student Info:", student_info)

# Add 'level' key with value 'Beginner' and display updated dictionary
student_info["level"] = "Beginner"
print("Updated Student Info:", student_info)

# Add one more course 'Python' to student's courses and display updated dictionary
student_info["courses"].append("Python")
print("Updated Student Info:", student_info)

# Remove age from student information and display updated dictionary
student_info.pop("age")
print("Updated Student Info:", student_info)

# Check if 'address' key is present in student information
address = student_info.get("address")
print(address)

# Find and display total number of items in student information
total_items = len(student_info)
print("Total number of items in student information:", total_items)

# Create a copy of this dictionary, update name to 'Bob', grade to 'B' and display both dictionary
student_copy = student_info.copy()
student_copy["name"] = "Bob"
student_copy["grade"] = "B"
print("Original Dictionary:", student_info)
print("Updated Copy:", student_copy)