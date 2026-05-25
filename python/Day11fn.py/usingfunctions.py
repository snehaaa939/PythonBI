# Q1. Write a lambda function to calculate cube of a number.
number = int(input("Enter a number: "))
cube = lambda number: number**3
print(f"cube of a number is:{cube(number)}")

# Q2. Store my_num as [1, 4, 7, 9, 12, 18]. Used filter function to select multiple of 3.
my_num = [1, 4, 7, 9, 12, 18]
multiple_of_3 = lambda x: x % 3 == 0
result = list(filter(multiple_of_3, my_num))
print(result)

# Q3. Store my_num as [1, 4, 7]. Used map function to calculate cube of each number.
my_num = [1, 4, 7]
cube = lambda my_num: my_num**3
mapped_cube = list(map(cube, my_num))
print(mapped_cube)

# Q4. Store my_num as [1, 5, 7, 9]. Used reduce function to calculate product of these.
from functools import reduce

my_num = [1, 5, 7, 9]
product = reduce(lambda x, y: x * y, my_num)
print(product)


# Q5. Write a function get_product_remainder(num_1, num_2) that returns product and remainder of two numbers
def get_product_remainder(num_1, num_2):
    product = num_1 * num_2
    remainder = num_1 % num_2
    return product, remainder


print(f"{get_product_remainder(16,4)}")


# Q6. Write a function sum_all() that takes n number of arguments and returns their sum.
def sum_all(*args):
    total = 0
    for num in args:
        total = total + num
    return total


# Q7. Write a function greet() that takes name of student and course enrolled. It has to return Hello, {name}, Welcome to {course} class. Note: If course is not passed it has to be Python in default
def greet(name, course="Python"):
    return f"Hello, {name}, welcome to {course} class."
print(greet("Ram"))
