# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter grade in the range 0 to 100:")
try:
    grade = int(grade)
except ValueError:
    print("Grade must be an integer between 0 and 100")
    sys.exit()

if grade < 0 or grade > 100:
    print("Grade must be an integer between 0 and 100")
    sys.exit()

if grade <= 39:
    result = "Fail"
elif grade >= 40 and grade  <= 69:
    result = "Pass"
else:
    result = "Distinction"
print(f"{grade} is a {result}")
