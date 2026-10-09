"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
amount = int(input("Enter the amount you want to save every month in £:"))

# Validate that they have entered an integer.
try:
  amount = int(amount)
  print(amount)
except: 
  print("Invalid amount please enter numbers only.")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
annual_total = amount * 12
# print this out for the user with a suitable message.
print(f"You will have saved £{annual_total} by the end of the year.")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
including_interest = annual_total * 1.008
# print this out in the format £X.XX (to two decimal places).
print(f"Including interest, you will have saved £{including_interest:.2f}by the end of the year.")
