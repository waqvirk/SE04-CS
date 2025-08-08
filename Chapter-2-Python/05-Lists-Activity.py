# Step 1: Create and Print a List
fruits = ["Mango", "Pineapple", "Banana", "Kiwi", "Grape"]
print("My Favorite Fruits:", fruits)
print("\n---\n")

# Step 2: Access Elements by Index and Negative Index
print("First fruit is", fruits[0], "last fruit is", fruits[4], "and 2nd last fruit with negative index is", fruits[-2])
print("\n---\n")

# Step: 3 Slice a List
print("Subset of the list from index 1 to 3:", fruits[1:3])
print("From beginning upto index 2:", fruits[:2])
print("From index 2 to the end:", fruits[2:])
print("\n---\n")

# Step 4: Check if an Item Exists
if "apple" in fruits:
    print("Apple in list: Found")
else:
    print("Apple in list: Not Found")
print("\n---\n")

# Step 5: Add Items
fruits.append("Watermelon")
print("Adding Watermelon to the end of fruits list:",fruits)
fruits.insert(1,"Pear")
print("Adding Pear to the 1 index of fruits list:",fruits)
print("\n---\n")

# Step 6: Change Items
fruits[1:3] = "Peach", "Coconut"
print("Updated fruits list after chaning value from index 1:3:", fruits)
print("\n---\n")

# Step 7: Remove items
fruits.remove("Banana")
print("Removing specific item by value 'Banana' form list:",fruits)
fruits.pop()
print("Removing specific item by index 'last by default using pop is watermelon' from list:",fruits)
fruits_temp = fruits.copy()
print("Temp fruits list:", fruits_temp)
fruits_temp.clear()
print("Temp fruits list cleared:", fruits_temp)
print("\n---\n")

# Step 8: Copy a list
fruits_copy = fruits.copy()
print("Fruits copy:",fruits_copy)
fruits.append("Blueberry")
print("Adding Blueberry to the original fruits list:",fruits)
print("printing both original and copy of fruits list:",fruits,fruits_copy)
print("\n---\n")

# Step 9: Concatenate and Extend
list1, list2, list3 = [1,2,3],[4,5,6], [7,8,9]
print("List 1:",list1)
print("List 2:",list2)
print("List 3:",list3)
combined_list1 = list1 + list2
print("List 1 + List 2:",combined_list1)
list1.extend(list3)
print("Extending list 1 with List 3:",list1)
print("\n---\n")

# Step 10: Sort and Reverse
print("Original unsorted:",fruits)
fruits.sort()
print("Original sorted:",fruits)
fruits.reverse()
print("Original reversed:",fruits)
fruits_sorted = sorted(fruits)
print("New sorted list, diff than original:",fruits_sorted)
print("\n---\n")

# Count and Index
print("Fruits:",fruits)
print("Count of Kiwi in fruits list:", fruits.count("Kiwi"))
print("Poisition of Kiwi in fruits list:", fruits.index("Kiwi"))
print("\n---\n")

# List comprehension
print("Fruits:",fruits)
smaller_fruits = [fruit.lower() for fruit in fruits if len(fruit) <= 5]
print("Fruits that are ≤ 5 characters in lowercase:", smaller_fruits)
bigger_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]
print("Fruits that are > 5 characters in uppercase", bigger_fruits)
print("\n---\n")

print("Numbers list:", list1)
evens_doubled = [n * 2 for n in list1 if n % 2 == 0]
print("Evens Doubled:", evens_doubled)