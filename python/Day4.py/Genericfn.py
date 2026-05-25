# Q. Create a variable str_1 that stores Hello, str_2 that stores World and:
# Display HelloWorld by concatenating both strings.
# Assign greetings variable as Hello World by concatenating both strings and display it.
# Assign my_str as HelloHelloHello using str_1 repetition.
# Find and display number of characters in string my_str.
# Change value of greetings variable to uppercase and display it.
# Change value of greetings variable to lowercase and display it.
# Change value of greetings variable to title case and display it.
# Swap the case of characters in greetings variable and display it.

str_1 = "Hello"
str_2 = "World"
print(str_1 + str_2)

greetings = str_1 + " " + str_2
print(greetings)

my_str= str_1*3
print(my_str)

my_str_length= len(my_str)
print(my_str_length)

greetings_upper= greetings.upper()
print(greetings_upper)

greetings_lower= greetings.lower()
print(greetings_lower)

greetings_title= greetings.title()
print(greetings_title)

greetings_swap= greetings.swapcase()
print(greetings_swap)
