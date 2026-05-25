# Q1. Display numbers from 1 to 10 using both for and while loops.
# for loop
for i in range(1, 11):
    print(i)
# While loop
count = 1
while count < 11:
    print(count)
    count = count + 1

# Q2. Assign num_tuple as (1, 4, 7, 12, 20). Using loop, find even numbers and their sum
num_tuple = (1, 4, 7, 12, 20)
even_sum = 0
for num in num_tuple:
    if num % 2 == 0:
        print(num)
        even_sum = even_sum + num
print("Sum of even numbers is: ", even_sum)

# Q3. Assign num_set as {1, 3, 5, 7, 9}. Using loop, find odd numbers and their product
num_set = {1, 3, 5, 7, 9}
product = 1
print("Odd numbers are:")
for num in num_set:
    if num % 2 != 0:
        print(num)
        product = product * num
print("Product of odd numbers is: ", product)

# Q4. Assign num as 7. Display it's factorial using both for and while loops.
num = 7
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f"factorial of 7 is {factorial}")

# While loop
num = 7
factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i = i + 1
print(f"factorial of 7 is {factorial}")

# Q5. Assign list with numbers. Find the second largest number in it using for loop.
numbers = [10, 25, 5, 30, 20]
largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest number is:", second_largest)

# Q6. Assign set as {1, 4, 5, 7, 8, 12}. Generate new list evaluated_data using for loop such that odd number is doubled and even number is tripled. If you encounter 4, skip evaluation for this and it you see 8, stop the loop.
set = {1, 4, 5, 7, 8, 12}
evaluated_data = []
for data in set:
    if data == 4:
        continue
    if data == 8:
        break
    if data % 2 != 0:
        evaluated_data.append(data * 2)
    else:
        evaluated_data.append(data * 3)
print(f"Evaluated data is: {evaluated_data}")
