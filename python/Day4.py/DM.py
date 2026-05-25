# Q1. Assign file_name as report_2026.pdf. Split it to get file name and extension and display them.
file_name = "report_2026.pdf"
print(file_name.split("."))

# Q2. Store my_date as 2026-03-05. Split it into list of year, month, day and display result
my_date = "2026-03-05"
YMD = my_date.split("-")
print(YMD)

# Q3. Store my_str as PYTHON. Use join function to display P.Y.T.H.O.N
my_str = "PYTHON"
print(".".join(my_str))

# Q4.Store laptop_names as ['Dell', 'HP', 'Apple']. Use join function to display Dell-HP-Apple
laptop_names = ["Dell", "HP", "Apple"]
print("-".join(laptop_names))

# Q5.Assign str_1 as Hello, World!. Replace World with Python and display the result.
str_1 = "Hello, World!"
print(str_1.replace("World", "Python"))

# Q6. Assign str_2 as 2026-03-01.csv. Replace - with / and display the result.
str_2 = "2026-03-01.csv"
replaced_str2 = str_2.replace("-", "/")
print(replaced_str2)

# Q7.Assign str_3 as Pineapple. Find at which index apple starts and display the result.
str_3 = "Pineapple"
index_str_3 = str_3.find("apple")
print(index_str_3)

# Q8. Assign my_name as your name. Count the number of vowels in it and display the result.
my_name = "Sneha Yadav"
my_name = my_name.lower()
print(
    my_name.count("a")
    + my_name.count("e")
    + my_name.count("i")
    + my_name.count("o")
    + my_name.count("u")
)

# Q9. Assign my_str as Hello, World!. Count and display occurrence of letter l in it.
my_str = "Hello, World!"
print(my_str.count("l"))
