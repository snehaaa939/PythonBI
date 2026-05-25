# Q1. Store student info as: [[name_1, age_1], [name_2, age_2], ...]. Display 2nd student's age.

student_1 = [["Ram", 22], ["Sita", 20], ["Sneha", 23]]
print(student_1[1] [1])

# Q2. Assign marks in five subjects to mark_list and subject names in subject_list. Display:
# total, average, highest and lowest marks obtained by student
# Change name of 2nd subject (1st index) to Python and display updated list
# Marks obtained in subject at 3rd position (2nd index) as Mark obtained in English is 89
# Marks obtained in subject at second last position with similar format as above.
# Marks obtained in last two subjects
# Marks in first three subjects
# Name of subject in which student scored highest marks
# Name of subject in which student scored lowest marks
# Number of subjects in which student scored 80

subject_list = ["Science", "Maths", "English", "Chemistry", "Physics"]
marks_list = [80, 90, 85, 83, 75]

# total, average, highest and lowest marks obtained by student
total = sum(marks_list)
print(f"total marks of the student :{total}")
average = total / 5
print(f"average mark of the student:{average}")
highest = max(marks_list)
print(f"highest marks obtained by student is:{highest}")
lowest = min(marks_list)
print(f"lowest marks obtained by student is:{lowest}")

# Change name of 2nd subject (1st index) to Python and display updated list
subject_list[1] = "Python"
print(subject_list)

# Marks obtained in subject at 3rd position (2nd index) as Mark obtained in English is 89
print(f"marks obtained in {subject_list[2]} is {marks_list[2]}")

# Marks obtained in subject at second last position with similar format as above.
print(f"marks obtained in {subject_list[-2]} is {marks_list[-2]}")

# Marks obtained in last two subjects
print(marks_list[-2:])

# Marks in first three subjects
print(marks_list[0:3])

# Name of subject in which student scored highest marks
max_index = marks_list.index(max(marks_list))
print(subject_list[max_index])

# Name of subject in which student scored lowest marks
min_index = marks_list.index(min(marks_list))
print(subject_list[min_index])

# Number of subjects in which student scored 80
count_80 = marks_list.count(80)
print(count_80)
