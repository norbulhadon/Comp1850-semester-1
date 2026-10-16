# Worksheet 1.2: Task 1 Solution
import sys
grade = input()
try:
    grade = int(grade)
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
   

if grade <= 39:
    result = "Fail"
elif grade >= 40 and grade  <= 69:
    result = "Pass"
else:
    result = "Distinction"
print(f"{grade} is a {result}")
