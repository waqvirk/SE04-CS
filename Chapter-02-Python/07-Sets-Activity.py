print()
#  1. Create a Set
fruits = {"Pineapple", "Banana", "Kiwi", "Mango", "Watermelon"}
print("Fruits set:", fruits)
print("\n---\n")

# 2. Check Membership
if "Kiwi" in fruits:
    print ("Kiwi Found")
else:
    print("Kiwi not found")
print("\n---\n")

# 3. Add and Update Items
fruits.add("Pear")
print("After adding the 'Pear' using add():", fruits)
more_fruits = {"Apricot", "Blueberry", "Lychee"}
fruits.update(more_fruits)
print("After updating more fruits to fruits using update():", fruits)
print("\n---\n")

# 4. Remove Items
fruits.remove("Pineapple")
print("After removing the 'Pineapple' using remove():", fruits)
fruits.discard("Avocado")
print("Attempting to remove the 'Avocado' using discard():", fruits)
fruits.pop()
print("Removing arbitrary fruit using pop():", fruits)
temp_fruits = fruits.copy()
temp_fruits.clear()
print("Empty set after clearing temp_fruits using clear():", temp_fruits)
print("\n---\n")

# 5. Set Operations 
set_a = {"Mango", "Pear", "Kiwi", "Banana"}
set_b = {"Dragon Fruit", "Passion Fruit", "Orange", "Kiwi", "Banana"}
        
print("Fruits:", fruits)
print("Set A of fruits:", set_a)
print("Set B of fruits:", set_b)
print()
set_ab = set_a.union(set_b)
print("Union of set A & B:", set_ab)
intersection_ab = set_a.intersection(set_b)
print("Intersection of set A & B to find common fruits:", intersection_ab)
difference_ab = set_a.difference(set_b)
print("Difference of set A & B to find fruits from set A that are not in set B:", difference_ab)
symmetric_diff_ab = set_a.symmetric_difference(set_b)
print("Symmetric diff of set A & B to find unique fruits from each set:", symmetric_diff_ab)
print("\n---\n")

# 6. In-place Set Operations
print("Original Fruits:", fruits)
print("Set A of fruits:", set_a)
print("Set B of fruits:", set_b)
set_a.difference_update(set_b)
print("Difference update of set A to remove items that are also in set B:", set_a)
set_b.intersection_update(fruits)
print("Intersection update of set B to only keep items that are also in Original Fruit set:", set_b)
set_a.update(set_b)
print("Adding set B in set A using update():", set_a)
print("\n---\n")

# 7. Relational Methods
small_set = {1,2,3,4}
large_set = {1,2,3,4,5,6,7}
print("Small set:", small_set)
print("Large set:", large_set)
print("Is small set subset of larget set:", small_set.issubset(large_set))
print("Is large set superset of small set:", large_set.issuperset(small_set))
print("Are both sets disjoint:", small_set.isdisjoint(large_set))
print("\n---\n")