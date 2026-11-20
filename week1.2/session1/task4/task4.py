# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#only tomato will be printed because intersection() prints common elements in both sets
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#because union() combines all unique items from both sets including shared items once like 'tomato' but not duplicates(2 tomatoes in this case)
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("strawberry")
print(fruit)
# Remove an item from vegetables
vegetables.remove("potato")
print(vegetables)
# Find and display symmetric difference of the two sets(which combines two sets and removes everything they have in common completely like 'tomato')
diff = fruit.symmetric_difference(vegetables)
print(diff)