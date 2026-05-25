# # ############## Day1 question's solution by using user input method #################

# # Q1. Ask user for temperature in fahrenheit and convert it into celsius then print the result.
# temperature_F = float(input("What is the Normal human temperature in fahrenheit?: "))
# celsius = (temperature_F - 32) / 1.8
# print(f"The Normal human temperature in celsius is: {celsius:.2f} °C")

# # Q.2 Ask user for principal amount, rate and time, Calculate the simple interest and display the result.
# principal = int(input("Enter principal amount(P)= "))
# rate = float(input("Enter the rate(R)= "))
# time = float(input("Enter the time(T)= "))
# SI = (principal * time * rate) / 100
# print(f"The Simple interest is(SI)= {SI:.2f}")

# # Q3. Ask user for diameter of the circle and find it's area and perimeter then display the result.
# diameter = float(input("Enter the diameter of the circle: "))
# PI = 3.14159
# radius = diameter / 2
# area = PI * (radius**2)
# print(f"Area of the circle is: {area:.2f}")
# perimeter = 2 * PI * radius
# print(f"Perimeter of the circle is: {perimeter:.2f}")

# # Q4. Ask user for hours, minutes and seconds then print the total seconds.
# hours = int(input("Enter the hours:"))
# minutes = int(input("Enter the minutes:"))
# seconds = int(input("Enter the seconds:"))
# total_seconds = (hours * 3600) + (minutes * 60) + (seconds)
# print(f"The total seconds of your given time is: {total_seconds} seconds.")

# # Q5. Ask student for his/her marks in 5 subjects and print the average of the total marks.
# sub1_mark = float(input("Enter you mark in subject1: "))
# sub2_mark = float(input("Enter you mark in subject2: "))
# sub3_mark = float(input("Enter you mark in subject3: "))
# sub4_mark = float(input("Enter you mark in subject4: "))
# sub5_mark = float(input("Enter you mark in subject5: "))
# total_marks = sub1_mark + sub2_mark + sub3_mark + sub4_mark + sub5_mark
# average = total_marks / 5
# print(f"The average marks of the student is: {average:.2f}")

# # Q6. Ask user for distance in kilometers and convert it into miles then print the result.
# distance = int(input("Enter distance in kilometer: "))
# miles = distance * 0.621371
# print(f"the distance in miles is: {miles:.2f}")

# # Q7. Ask user for his/her height and weight and calculate the BMI of that user then display the result.
# height = float(input("Enter your height: "))
# weight = float(input("Enter your weight: "))
# BMI = weight / (height**2)
# print(f"Your BMI is: {BMI:.2f}")


# num1 = -5
# if num1 > 0 and num1 % 2 == 0:
#     print("num_1 is positive even number.")
# elif num1 > 0 and num1 % 2 != 0:
#     print("num1 is positive odd number")
# elif num1 < 0:
#     print("num1 is negative number")
# else:
#     print("num1 is 0")


# def product(a, b):
#     result= a*b
#     return result

# result=product(3,4)
# print("reult", result)

# def area_of_circle(diameter):
#     if diameter > 0:
#         PI = 3.1415
#         radius = diameter / 2
#         area = PI * radius**2
#         print("Area of the circle:", area)
#     else:
#         print("Invalid diameter! Must be a positive number.")

# diameter = float(input("Enter the diameter of the circle: "))
# area_of_circle(diameter)

# is_even = lambda number: number % 2 == 0
# num = int(input("Enter a number: "))
# print(is_even(num))

# age_list = [10, 30, 25, 28, 60, 39, 15]


# def age_filter(age):
#     return age > 16


# filtered_ages = list(filter(age_filter, age_list))
# print("Ages 16+:", filtered_ages)

# age_list = [1, 3, 4, 8, 12, 20]
# def categorize_age(age):
#     if 0 <= age <= 1:
#         return "infant"
#     elif 2 <= age <= 11:
#         return "child"
#     elif 12 <= age <= 20:
#         return "teen"
#     else:
#         return "adult"
# age_category = list(map(categorize_age, age_list))
# print(age_category)


# lambda funtion
# number = int(input("Enter a number:"))


# def check_number(number):
#     if number % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")


# check_number(number)

# lambda number: "Even" if number % 2 == 0 else "Odd"
# adder = lambda num_1, num_2: num_1 + num_2
# total = adder(4, 5)
# print(total)

# number = int(input("Enter a number:"))
# square = lambda x: x**2
# print(square(number))

# my_numbers = [1, 4, 6, 10]
# odd_even_chk = lambda my_numbers: "Even" if my_numbers % 2 == 0 else "Odd"
# result= list(map(odd_even_chk, my_numbers))
# print(result)

# WAF that returns true if number is even else returns false.
# number= int(input("enter a number:"))
# odd_even = lambda num: "True" if num % 2 == 0 else "False"
# print(odd_even(number))
# print (type(number))

# num1=10
# num2='30'
# num2_type=int(num2)
# sum=num1+num2_
# type
# print(sum)

# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_1.extend(list_2)
# print(list_1)  # [1, 2, 3, 4, 5, 6]


# original_set = {1, 2, 3}
# copied_set = original_set.copy()
# copied_set.add(4)
# print(original_set)  # {1, 2, 3}
# print(copied_set)

# def calculate_area(radius, height):
# 	pi = 3.14
# 	area = pi * radius ** 2* height
# 	return area
# print(calculate_area(5,10))  # 78.5

# def factorial(n):
# 	if n == 0:
# 		return 1  # Exit condition
# 	else:
# 		return n * factorial(n - 1)  # Recursive call
# print(factorial(0))

for i in range(10):
	if i == 5:
		continue
	print(i)
 
i = 10
while i > 0:
	i = i - 1
	if i % 2 == 0:
		continue
	print(i)

