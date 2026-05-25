# #Indexing and Slicing
# Q. Create a variable my_str that stores We are learning Python and it's fun! and
# Find and display the first character.
# Find and display the character at index 8.
# Find and display the last character (using negative indexing).
# Find word Python using slicing and display it.
# Find word fun using negative slicing and display it.
# Find text lrn (i.e. only some part of text learning) and display it.
# Reverse the string and display it.
# Find sub-string that lies from 5th index till end and display it.
# Find sub-string that lies from start till 10th index and display it.

# Solution:
# Indexing
my_str = "We are learning Python and it's fun!"
first_Char = my_str[0]
print(first_Char)  # W

eighth_Char = my_str[8]
print(eighth_Char)  # e

last_char = my_str[-1]
print(last_char)  #!

# Slicing
slicing = my_str[16:22]
print(slicing)  # Python

slicing2 = my_str[-4:-1]
print(slicing2)  # fun

slicing3 = my_str[7:15]  # learning
print(slicing3[::3])  # lrn

print(my_str[::-1])

sub_string1= my_str[5:]
print(sub_string1)

sub_string2= my_str[:11]
print(sub_string2)