# # Q1. Ask user for marks and display grade in format: Your grade is A. (Rule: 90+ => A, 80-90 => B, 70-80 => C, 60-70 => D, below 60 F)

# # marks = float(input("Enter your marks:"))
# # if marks >= 90:
# #     grade = "A"
# # elif marks >= 80 and marks < 90:
# #     grade = "B"
# # elif marks >= 70 and marks < 80:
# #     grade = "C"
# # elif marks >= 60 and marks < 70:
# #     grade = "D"
# # else:
# #     grade = "F"
# print(f"Your grade is {grade}.")

# # Q2. Ask user for birth year and display life stage in format: You are a teenager. (Rule: 0-12 => Child, 13-19 => Teenager, 20-59 => Adult, 60+ => Senior)

# birth_year = int(input("Enter your birth year:"))
# if birth_year > 2026:
#     print("Invalid birth year!")
# else:
#     age = 2026 - birth_year
#     if 0 <= age <= 12:
#         stage = "Child"
#     elif 13 <= age <= 19:
#         stage = "Teenager"
#     elif 20 <= age <= 59:
#         stage = "Adult"
#     else:
#         stage = "Senior"
#     print(f"You are a {stage}.")

# # Q3. Ask user for three sides of a triangle and display type of triangle in format: This is an isosceles triangle. (Rule: All sides equal => Equilateral, Two sides equal => Isosceles, No sides equal => Scalene)

# side1 = float(input("Enter first side of the triangle: "))
# side2 = float(input("Enter second side of the triangle: "))
# side3 = float(input("Enter third side of the triangle: "))

# if side1 == side2 == side3:
#     triangle = "Equilateral"
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     triangle = "Isosceles"
# else:
#     triangle = "Scalene"
# print(f"This is an {triangle} triangle.")

# # Q4. Ask user for two numbers and display the largest in format: The largest number is 5

# num_1 = float(input("Enter first number:"))
# num_2 = float(input("Enter second number:"))
# if num_1 > num_2:
#     largest = num_1
# else:
#     largest = num_2

# print(f"The largest number is {largest}")

# Q5. Ask user for hour of the day (0-23) and display appropriate greeting in format: Good Morning. (Rule: 5-12 => Good Morning, 12-17 => Good Afternoon, 17-21 => Good Evening, 21-5 => Good Night, else invalid time)

hour = int(input("Enter the hour of the day: "))
if 5 <= hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 17:
    greeting = "Good Afternoon"
elif 17 <= hour < 21:
    greeting = "Good Evening"
elif (21 <= hour <= 23) or (0 <= hour < 5):
    greeting = "Good Night"
else:
    greeting = "Invalid Time"

print(f"{greeting}.")
