# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
#Displaying error message when the no. is not provided
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")
#finding the minimum, maximum and mean
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

#finding median when the no. of float number provided is even and when it is odd
numbers.sort()
l = len(numbers)
#note: the index starts with 0 
if l % 2 == 1:
    median = numbers[l//2]
else:
    median = (numbers[l//2] + numbers[(l//2)-1]) / 2

#displaying the min,max,mean and median
print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")
