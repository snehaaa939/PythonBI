# cities = ["kathmandu", "Butwal", "banepa"]
# for item in cities:
#     print(item.upper())
#     print("----")

# # write a for loop that divides and prints each number in a list by 2
# # [1,4,4,7,9]
# # number = [1, 4, 4, 7, 9]
# # for num in number:
# #     print(num / 2)

# # user_input = int(input("Enter a number:"))
# # for i in range(1, 11):
# #     print(f"{user_input} * {i} = {user_input * i}")
# # i = 10
# # while i > 0:
# # 	i = i - 1
# # 	if i % 2 == 0:
# # 		continue
# # 	print(i)

# # for i in range(3):
# # 	for j in range(2):
# # 		print(f"i: {i}, j: {j}")
# # for i in range(1, 4):
# # 	for j in range(1, 4):
# # 		print(f"{i} x {j} = {i * j}")

# for i in range(1, 5):
#     if i % 2 == 0:
#         print(f"{i} is even")

# even_number= [i for i in range(1,5) if i%2==0]
# print(even_number)

# cities=["kathmandu", "Pokhara", "Dharan"]
# # for city in cities:
# #     upper_city= city.upper()
# #     print(upper_city)

# city= [ city.upper() for city in cities]
# print(city)

# cities2=["kathmandu", "Pokhara", "Dharan", "Janakpur", "kalaiya"]
# city2=[city2.upper() for city2 in cities2 if city2.lower().startswith("k")]
# print(city2)


# Revision class
# Loop
# num_list = range(1, 6)
# for number in num_list:
#     square_of_num = number**2
#     print(f"{number}^2 ={square_of_num:>2}")

# num_list = range(1, 11)
# for number in num_list:
#     cube_of_num = number**3
#     print(f"{number} ^ 3 ={cube_of_num:4}")

# country_names = [
#     "Australia",
#     "Nepal",
#     "america",
#     "Bhutan",
#     "Austria",
#     "England",
#     "spain",
# ]
# # Diaplay only the names of countries that starts with letter A/a
# # for country in country_names:
# #     if country.lower().startswith('a'):
# #         print(country.title())
# # Diaplay only the names of countries that doesn't start with letter A/a
# for country in country_names:
#     if not country.lower().startswith("a"):
#         print(country.title())

# While loop
num = 1
while num <= 10:
    cube_of_num = num**3
    print(f"{num:>2} ^ 3 ={cube_of_num:>4}")
    num = num + 1

my_dict = {"one": "uno", "two": "des", "three": "thress"}
for key, value in my_dict.items():
    print(f"Translation for {key.title():6} => {value.title()}")

# for num in range(2, 5):
#     i = 1
#     print()
#     print(f"Table of {num}")
#     while True:
#         print(f"{num}*{i}= {num*i}")
#         i += 1
#         if i >= 4:
#             break
# num = 10
# while num > 0:
# 	print(num)
# 	num = num - 2

# for i in range(10):
# 	if i == 5:
# 		break
# 	print(i)
# i = 10
# while i > 0:
# 	i = i - 1
# 	if i % 2 == 0:
# 		continue
# 	print(i)

# for i in range(5):
# 	print(i)
# else:
# 	print("Loop completed successfully")

# for i in range(5):
# 	if i == 3:
# 		break
# 	print(i)
# else:
# 	print("Loop completed successfully")

# Date:- 2026/05/05
# Assign num_list variable as [6,12,22,10]
# Create a new list half_list such that all these numbers are half
# desired value for print (half_list):[3,6,11,5]

num_list = [6, 12, 22, 10]
half_list = []
triple_list = []
# for num in num_list:
#     half_list.append(num // 2)
# print(half_list)

# # Using map
# num_list = [6, 12, 22, 10]
# half_list = list(map(lambda x: x // 2, num_list))
# print(half_list)

# # using list comprehension
# half_list_comp = [number // 2 for number in num_list]
# print(half_list_comp)

# using loop
for number in num_list:
    triple_list.append(number * 3)
print(triple_list)

# Using map
triple_list = list(map(lambda x: x * 3, num_list))
print(triple_list)

# using list comprehension
triple_list_comp = [number * 3 for number in num_list]
print(triple_list_comp)


my_list = ["Apple", "nepal", "Cat", "Banana", "python", "lalitpur", "bHaktapur"]
lower_name = []
# using loop
for item in my_list:
    if item[0].islower():
        lower_name.append(item)
print(lower_name)
# using list comprehension
lower_name_comp = [item for item in my_list if item[0].islower()]
print(lower_name_comp)

my_nums = [4, 6, 8, 10, 15, 19, 21]
# If number is multiple of 3 then double it else half it
new_list = [num * 2 if num % 3 == 0 else num // 2 for num in my_nums]
print(new_list)

brand_names = ['Apple', 'Samsung', 'LG', 'Hitachi', 'Baltra']
brand_dict = {}
for name in brand_names:
    brand_dict[name] = len(name)
print(brand_dict)


#Filehandling writing textfiles.
content_lines=["asdaf\n", "asda\n", "asdafv"]
content="""
This is test
It will be written on file
Thanks.
"""
with open(r'C:\Users\User\Desktop\python BI Rabindra sir\python\filehandling.py\myfile.txt', 'w') as file_obj:
    file_obj.writelines(content)
    file_obj.writelines(content_lines)
