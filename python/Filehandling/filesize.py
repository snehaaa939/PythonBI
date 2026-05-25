#Calculate and display the size of python.txt and java.txt in KB. (Hint: use os module & AI)
# ANS:
import os

python_file = r"C:\Users\User\Desktop\python.txt"
java_file = r"C:\Users\User\Desktop\java.txt"

python_size = os.path.getsize(python_file)
java_size = os.path.getsize(java_file)

# Convert bytes to KB
python_kb = python_size / 1024
java_kb = java_size / 1024

# Display sizes
print(f"python.txt size: {python_kb:.2f} KB")
print(f"java.txt size: {java_kb:.2f} KB")