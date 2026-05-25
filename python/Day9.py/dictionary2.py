# Q1. Courses offered by college is stored in dictionary as 'course': ['DS', 'SQL', 'Python'], 'duration': [40, 50, 60]. Check if Python is offered in college
# Q2. College_1 has course as {'python': {'duration': 3, 'type': 'basic'}, 'java': {'duration': 4, 'type': 'medium'}}. College_2 has course as {'multimedia': {'duration': 2, 'type': 'basic'}, 'javascript': {'duration': 5, 'type': 'advanced'}}. College_1 acquired College_2. Update College_1 course with College_2's and display the updated result
# Q3. Assign translation_dict as {'hello': 'hola', 'thank you': 'gracias', 'goodbye': 'adios', ...}. Ask user to input a word in English and display its translation in Spanish. If word is not found, display Translation not found
# Q4. Using range function, generate a list of even numbers from 0 to 20 and display the result
# Q5. Using range, generate and display multiplicate of 3 from 30 to 1 in descending order


# Q1. Courses offered by college is stored in dictionary as 'course': ['DS', 'SQL', 'Python'], 'duration': [40, 50, 60]. Check if Python is offered in college
courses = {"course": ["DS", "SQL", "Python"], "duration": [40, 50, 60]}
print(courses.get("course"))
is_python_offered = "Python" in courses.get("course", [])
print("Python is offered in the college:", is_python_offered)

# Q2. College_1 has course as {'python': {'duration': 3, 'type': 'basic'}, 'java': {'duration': 4, 'type': 'medium'}}. College_2 has course as {'multimedia': {'duration': 2, 'type': 'basic'}, 'javascript': {'duration': 5, 'type': 'advanced'}}. College_1 acquired College_2. Update College_1 course with College_2's and display the updated result
college_1 = {
    "python": {"duration": 3, "type": "basic"},
    "java": {"duration": 4, "type": "medium"},
}
college_2 = {
    "multimedia": {"duration": 2, "type": "basic"},
    "javascript": {"duration": 5, "type": "advanced"},
}
college_1.update(college_2)
print("Updated College_1 courses:", college_1)

# Q3. Assign translation_dict as {'hello': 'hola', 'thank you': 'gracias', 'goodbye': 'adios', ...}. Ask user to input a word in English and display its translation in Spanish. If word is not found, display Translation not found
translation_dict = {
    "hello": "hola",
    "thank you": "gracias",
    "goodbye": "adios",
    "please": "por favor",
    "yes": "sí",
    "no": "no",
}
word = input("Enter a word in English: ").strip().lower()
translation = translation_dict.get(word, "Translation not found")
print("Spanish translation:", translation)

# Q4. Using range function, generate a list of even numbers from 0 to 20 and display the result
even_numbers = list(range(0, 21, 2))
print("Even numbers from 0 to 20:", even_numbers)

# Q5. Using range, generate and display multiplicate of 3 from 30 to 1 in descending order
multiples_of_3 = list(range(30, 0, -3))
print("Multiples of 3 from 30 to 1:", multiples_of_3)
