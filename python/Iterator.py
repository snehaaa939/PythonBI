#Iterator

# my_variable = range(1, 10000)
# my_iter=iter(my_variable)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

#Generator

# Create a generator that gives cube of one billion records
cube_of_numbers = (number**3 for number in range(1, 100000001))
print(next(cube_of_numbers))
print(next(cube_of_numbers))
print(next(cube_of_numbers))
print(next(cube_of_numbers))
print(next(cube_of_numbers))
print(next(cube_of_numbers))
# n = 1
# for number in cube_of_numbers:
#     print(number)
#     n = n + 1
#     if n == 10:
#         break


def custom_generator(x, y):
    while x <= y:
        yield x
        x = x + 2
my_generator = custom_generator(2,10)
value= next(my_generator)
print(value)
for item in my_generator:
    print(item)
