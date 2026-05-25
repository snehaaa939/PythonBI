# Q1. Ask user for name and price of a pen. display in format: Ram bought a pen for $ 10.56
name = input("Enter your name:")
price = float(input("Enter price of a pen:"))
print(f"Ram bought a pen for ${price:.2f}")

# Q2. Ask user for name, price of three product. Display it in format as:
# Item        Price
# --------------------
# Apple       Rs.   3
# Banana      Rs.  10
# Orange      Rs. 200
item = "Item"
price = "Price"
product1 = input("Enter name of the product1:")
product2 = input("Enter name of the product2:")
product3 = input("Enter name of the product3:")
price1 = int(input("Enter price of the product1:"))
price2 = int(input("Enter price of the product2:"))
price3 = int(input("Enter price of the product3:"))
print(f"{item:15}{price}")
print("-" * 25)
print(f"{product1:<12} Rs. {price1:>3}")
print(f"{product2:<12} Rs. {price2:>3}")
print(f"{product3:<12} Rs. {price3:>3}")

# Q3. Ask user for current year, month and day. Display it in format: Today's Date: 2023-03-12
year = input("Enter current year:")
month = input("Enter current month:")
day = input("Enter current day:")
print(f"Today's Date: {year}-{month:0>2}-{day}")

# Q4. Ask user for name and marks in 3 subject. Display result as: Hari scored 85.5% in exam.
name = input("Enter your name:")
subject_1 = input("Enter Subject1:")
sub1_mark = float(input("Enter the mark of Subject1:"))

subject_2 = input("Enter Subject2:")
sub2_mark = float(input("Enter the mark of Subject2:"))

subject_3 = input("Enter Subject3:")
sub3_mark = float(input("Enter the mark of Subject3:"))
total = sub1_mark + sub2_mark + sub3_mark
percentage = total / 3
print(f"{name} scored {percentage:.2f}% in exam.")
