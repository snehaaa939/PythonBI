# Q1. Ask user for name and birth year. Calculate and display if he/she can vote in format: Ram, You are [not] eligible for voting. (Note: 18+ people can vote)
# Q2. Ask user for num_1 and num_2. Display if num_1 is divisible by num_2 in format: 15 is [not] divisible by 3
# Q3. Ask user for name, age and salary. Display if user is eligible for a loan in format: Ram, You are [not] eligible for loan. (Eligibility Rule: Age between 21 and 60, salary at least 30K)
# Q4. Ask user for string and check if it's palindrome in format: "madam" is [not] a palindrome
# Q5. Store customer balance in a variable. Ask user for amount to withdraw. If desired amount is less than total balance display, 123 withdrawn successfully. New Balance: 456 else display Insufficient balance. You only have 123 in your account


# Q1. Ask user for name and birth year. Calculate and display if he/she can vote in format: Ram, You are [not] eligible for voting. (Note: 18+ people can vote)
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year  # Assuming current year is 2026
if age >= 18:
    print(f"{name}, You are eligible for voting.")
else:
    print(f"{name}, You are not eligible for voting.")

# Q2. Ask user for num_1 and num_2. Display if num_1 is divisible by num_2 in format: 15 is [not] divisible by 3
num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))
if num_2 != 0 and num_1 % num_2 == 0:
    print(f"{num_1} is divisible by {num_2}")
else:
    print(f"{num_1} is not divisible by {num_2}")

# Q3. Ask user for name, age and salary. Display if user is eligible for a loan in format: Ram, You are [not] eligible for loan. (Eligibility Rule: Age between 21 and 60, salary at least 30K)
name = input("Enter your name:")
age = int(input("Enter your age:"))
salary = int(input("Enter your Salary:"))
if age >= 21 and age <= 60 and salary >= 30000:
    print(f"{name}, You are eligible for loan.")
else:
    print(f"{name}, You are not eligible for loan.")
    
# Q4. Ask user for string and check if it's palindrome in format: "madam" is [not] a palindrome
string= input("Enter a string:")
if string == string[::-1]:
    print(f'"{string}" is a palindrome')
else:
    print(f'"{string}" is not a palindrome')


# Q5. Store customer balance in a variable. Ask user for amount to withdraw. If desired amount is less than total balance display, 123 withdrawn successfully. New Balance: 456 else display Insufficient balance. You only have 123 in your account
balance=123
amount=float(input("Enter amount to withdraw:"))
if amount<balance:
    balance = balance- amount
    print(f"{amount} withdrawn successfully. New balance: {balance}")
else:
    print(f"Insufficient balance. You only have {balance} in your account")