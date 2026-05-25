# Store Employee's salary as: (20000, 25000, 30000) and name as ('Rabindra', 'Bob', 'Charlie')
# Find and display total number of employees
# Find and display total, average, highest and lowest salary of employees
# Name of employee with highest salary
# Name of employee with lowest salary
# Number of employees with salary 25000
# Update salary at index 1 to 35000 and display updated salary tuple
# Unpack employee name and salary tuples into separate variables and display them
# zip employee name and salary tuples into a single list of tuples and display it

# Store Employee's salary as: (20000, 25000, 30000) and name as ('Rabindra', 'Bob', 'Charlie')
salary = (20000, 25000, 30000)
name = ("Rabindra", "Bob", "Charlie")

# Find and display total number of employees
total_employees = len(name)
print(f"Total number of employees:{total_employees}")

# Find and display total, average, highest and lowest salary of employees
total_salary = sum(salary)
print(f"The total salary of employees: {total_salary}")
average_salary = total_salary / 3
print(f"The average salary of employees: {average_salary}")
highest_salary = max(salary)
print(f"The highest salary of employees: {highest_salary}")
lowest_salary = min(salary)
print(f"The lowest salary of employees: {lowest_salary}")

# Name of employee with highest salary
max_salary = salary.index(max(salary))
print(f"Employee with highest salary:{name[max_salary]}")

# Name of employee with lowest salary
min_salary = salary.index(min(salary))
print(f"Employee with lowest salary:{name[min_salary]}")

# Number of employees with salary 25000
count_25000 = salary.count(25000)
print(f"Number of employees with salary 25000: {count_25000}")

# Update salary at index 1 to 35000 and display updated salary tuple
salary_list = list(salary)
salary_list[1] = 35000
salary = tuple(salary_list)
print(f"Updated salary tuple:{salary}")

# Unpack employee name and salary tuples into separate variables and display them
n1, n2, n3 = name
s1, s2, s3 = salary
print("Employee 1:", n1, "-", s1)
print("Employee 2:", n2, "-", s2)
print("Employee 3:", n3, "-", s3)

# zip employee name and salary tuples into a single list of tuples and display it
combined = zip(name, salary)
print(f"Zipped list:{list(combined)}.")
