# Q1. Write a function get_simple_interest(principal, rate, time) to calculate and return simple interest based on given principal, rate and time.

def get_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest
print(f"The simple interest is: {get_simple_interest(50000, 6.5, 2)}")

# Q2. Write a function get_rectangle_area_perimeter(length, width) to calculate and return area and perimeter of a rectangle based on length and width.

def get_rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
print(f"area and perimeter of a rectangle are: {get_rectangle_area_perimeter(20,40)}")

# Q3. Write a function is_palindrome(string) to check if a given string is palindrome or not. Return True if it is palindrome else return False.

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print(is_palindrome("madam"))
print(is_palindrome("hello"))


# Q4. Write a function count_vowels(string) return the number of vowels in a given string.
def count_vowels(string):
    string = string.lower()
    return (
        string.count("a")
        + string.count("e")
        + string.count("i")
        + string.count("o")
        + string.count("u")
    )


print(count_vowels("Hello"))


# Q5.  Write a function  get_square_root(num) to return the square root of a given number.
def get_square_root(num):
    sqrt = num ** (1 / 2)
    return sqrt
print(f"The square root of a given number is:{get_square_root(36)}")
