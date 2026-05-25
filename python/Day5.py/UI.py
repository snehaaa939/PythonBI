# Q1. Ask user for his/her name and display: Hello, <name>!
name = input("Enter Your Name:")
print(f"Hello, <{name}>!")

# Q2. Ask user for his/her birth year. Calculate and display his/her age
birth_Year = int(input("Enter your birth year: "))
current_Year = 2026
age = current_Year - birth_Year
print(f"Your age is {age}")

# Q3. Ask user for mass and length of a cube. Calculate and display its density (d = m/v)
mass = float(input("enter mass of the cube:"))
length = float(input("enter length of the cube:"))
volume = length**3
density = mass / volume
print(f"density of the cube is:{density:.3f}")

# Q4. Ask user for length in feet and convert and display its value in meter (1 ft = 0.3048 m)
length = float(input("Enter length in feet:"))
ft_in_m = length * 0.3048  # converting feet into meter
print(f"{length} feet is equal to {ft_in_m:.3f}")

# Q5. Ask user for a file name in format file.ext. Extract and display file extension from it
filename = input("Enter file name:")
extension = filename.split(".")[-1]
print(f"The extension of the {filename} is {extension}")

# Q6. Ask user for a sentence and display number of words in it.
sentence = input("enter any sentence you know or like: ")
words = sentence.split()
number = len(words)
print(f"The number of words in sentence is {number}")

# Q7. Ask user for two numbers and display their sum, difference, product and quotient.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print(f"Sum is: {sum}")
print(f"Difference is: {difference}")
print(f"Product is: {product}")
print(f"Quotient is: {quotient}")
