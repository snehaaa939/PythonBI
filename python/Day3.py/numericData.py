#Q. Create two variables num_1 as 7, num_2 as 3.5 and:
#Display their data types
# Display their sum
# Display their difference
# Display their product
# Display their division
# Convert both num_1 and num_2 into string and display sum again
num_1 = 7
num_2 = 3.5
print("Data type of num_1:", type(num_1))
print("Data type of num_2:", type(num_2))
print("Sum of num_1 and num_2:", num_1 + num_2)
print("Difference of num_1 and num_2:", num_1 - num_2)
print("Product of num_1 and num_2:", num_1 * num_2)
print("Division of num_1 by num_2:", num_1 / num_2)
num_1_str = str(num_1)
num_2_str = str(num_2)
print("Sum of num_1 and num_2 as strings:", num_1_str + num_2_str)



#Q. Repeat above exercise but with storing both variables with a complex number
num_1 = complex(7, 0)
num_2 = complex(3.5, 0)
print("Data type of num_1:", type(num_1))
print("Data type of num_2:", type(num_2))
print("Sum of num_1 and num_2:", num_1 + num_2)
print("Difference of num_1 and num_2:", num_1 - num_2)
print("Product of num_1 and num_2:", num_1 * num_2)
print("Division of num_1 by num_2:", num_1 / num_2)
num_1_str = str(num_1)
num_2_str = str(num_2)
print("Sum of num_1 and num_2 as strings:", num_1_str + num_2_str)


#Q. Create variable num_3 as 15 and num_4 as 4. Swap their values and display the result
num_3 = 15
num_4 = 4
num_3, num_4 = num_4, num_3
print("After swapping, num_3:", num_3)
print("After swapping, num_4:", num_4)

#another method to swap values without using a temporary variable
num_3 = 15  
num_4 = 4
temp= num_3
num_3= num_4
num_4= temp
print("After swapping, num_3:", num_3)
print("After swapping, num_4:", num_4)