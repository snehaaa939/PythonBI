#Create a new file java.txt. Copy the content of python.txt to java.txt but replacing the text python with java.

essay = """
Python is a popular programming language created by Guido van Rossum.
It is easy to learn and widely used in web development, data science,
artificial intelligence, automation, and software development.

Python has a simple syntax that makes programming easier for beginners.
It supports object-oriented programming and has a large collection of
libraries and frameworks. Because of its readability and versatility,
Python is one of the most widely used programming languages in the world.
"""
with open(r"C:\Users\User\Desktop\python.txt", "r", encoding="utf-8") as file_obj:
    file_obj.read()
    
# Replace 'Python' with 'Java'
new_content = essay.replace("Python", "Java").replace("python", "java")

with open(r"C:\Users\User\Desktop\java.txt", "w", encoding="utf-8") as file_obj:
    file_obj.write(new_content)

print("java.txt created successfully")
 