# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")

print(f"Modified String 1: {user_string.lower()}") #converts all characters to lowercase
print(f"Modified String 2: {user_string.upper()}") #converts all characters to uppercase
print(f"Modified String 3: {user_string.strip()}") #removes whitespace from beginning and end of the string
print(f"Modified String 4: {user_string.replace('a', '@')}") #replaces every 'a' with "@"
print(f"Modified String 5: {user_string.capitalize()}")  #capitalizes only the first character of the string
print(f"Modified String 6: {user_string[::-1]}") #reverses the string 
print(f"Modified String 7: {user_string.title()}") #capitalizes the first character of every string
print(f"Modified String 8: {len(user_string)}") #returns the total number of characters
print(f"Modified String 9: {user_string.find('a')}")#returns the index of 'a' in the string and if not found returns '-1'
print(f"Modified String 10: {user_string.count('a')}")#returns the number of times 'a' appears in the string
print(f"Modified String 11: {user_string.startswith('Hello')}")#checks and returns true if the string starts with "Hello" if not Falseprint(f"Modified String 12: {user_string.endswith('!')}")
print(f"Modified String 13: {user_string.isalnum()}") #checks and returns true if the string contains only letters and numbers, if not returnsFalse
print(f"Modified String 14: {user_string.isalpha()}")#checks and returns true if the string contains only letters, if not returns False
print(f"Modified String 15: {user_string.isdigit()}")#checks and returns true if the string contains only digits, if not returns False




######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!