# Q. Assign str_1 as "Hello", str_2 as "12345", str_3 as "##abc123##" and str_4 as " "
# Check and display if str_1 has alphabetic characters only.
# Check and display if str_1 has numeric characters only.
# Check and display if str_2 has alphanumeric characters only.
# Check and display if str_4 is empty.
# Check and display if str_3 starts with abc
# Check and display if str_3 ends with 3
# Check and display if str_1 starts with He and ends with lo
# Remove leading and trailing # from str_3 and display the result
# Remove leading # from str_3 and display the result

str_1 = "Hello"
str_2 = "12345"
str_3 = "##abc123##"
str_4 = " "

str_1_A = str_1.isalpha()
print(str_1_A)  # True

str_1_N = str_1.isnumeric()
print(str_1_N)  # False

str_2_AN = str_2.isalnum()
print(str_2_AN)  # True

str_4_E = str_4.isspace()
print(str_4_E)  # True

str_3_start = str_3.startswith("abc")
print(str_3_start) # False

str_3_ends = str_3.endswith("3")
print(str_3_ends) # False

str_1_start = str_1.startswith("He")
print(str_1_start) # True
str_1_ends = str_1.endswith("lo")
print(str_1_ends) # True

stripped_str3= str_3.strip("#")
print(stripped_str3) #abc123

lstripped_str3= str_3.lstrip("#")
print(lstripped_str3) #abc123##