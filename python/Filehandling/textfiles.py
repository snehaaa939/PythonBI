# Create a text file python.txt on your desktop and write short essay about python on it.
essay = """
Python is a popular programming language created by Guido van Rossum.
It is easy to learn and widely used in web development, data science,
artificial intelligence, automation, and software development.

Python has a simple syntax that makes programming easier for beginners.
It supports object-oriented programming and has a large collection of
libraries and frameworks. Because of its readability and versatility,
Python is one of the most widely used programming languages in the world.
"""
with open(r"C:\Users\User\Desktop\python.txt", "w", encoding="utf-8") as file_obj:
    file_obj.write(essay)
print("python.txt file created successfully")

#Open this file python.txt. Add text I will learn Error Handling Next at end
with open(r"C:\Users\User\Desktop\python.txt", "a", encoding="utf-8") as file_obj:
    file_obj.write("\nI will learn Error Handling Next")
print("Text added successfully")
