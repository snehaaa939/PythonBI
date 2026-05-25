#Q. Assign your age to variable my_age and:
# Check if your age is 16
# Check if your age is not 70
# Check if you are a child (age less than 13)
# Check if you are an adult (age 20 or above)
# Check if you are eligible to vote (18+ can vote)
# Check if you are a teenager (age between 13 and 19)
# Check if you lie on passive population (below 5 and over 65 considered passive)
# Check if you are eligible for driving license (age between 18 and 65)

my_age= 23
print("Is my age 16?", my_age == 16)
print("Is my age not 70?", my_age != 70)
print("Am I a child?", my_age < 13)
print("Am I an adult?", my_age >= 20)
print("Am I eligible to vote?", my_age >= 18)
print("Am I a teenager?", 13 <= my_age <= 19)
print("Do I lie on the passive population?", my_age < 5 or my_age > 65)
print("Am I eligible for a driving license?", 18 <= my_age <= 65)