print()

# 1. Create a Tuple
my_tuple = ("Berlin", "Hamburg", "Munich", "Frankfurt", "Bielefeld")

# 2. Print the Tuple
print("Cities of Germany:", my_tuple)
print("\n---\n")

# 3. Access Tuple Items
print("Cities of Germany:", my_tuple)
print("First city in tuple:", my_tuple[0])
print("Last city in tuple:", my_tuple[-1])             # Ironic that you called Bielefeld with Negative Index
print("\n---\n")

# 4. Slice the Tuple
print("Cities of Germany:", my_tuple)
print("Cities from index 2:4 in tuple:", my_tuple[2:4])
print("Cities from start upto index 3 in tuple:", my_tuple[:3])
print("Cities from index 1 to the end in tuple:", my_tuple[1:])
print("\n---\n")

# 5. Check if an Item Exists
print("Cities of Germany:", my_tuple)
if "Munich" in my_tuple:
    print("City of Munich in tuple: Found")
else:
    print("City of Munich in tuple: Not Found")
if "Bonn" in my_tuple:
    print("City of Bonn in tuple: Found")
else:
    print("City of Bonn in tuple: Not Found")
print("\n---\n")

# 6. Count and Index
print("Cities of Germany:", my_tuple)
print("Frankfurt count in tuple:", my_tuple.count("Frankfurt"))
print("Frankfurt index in tuple:", my_tuple.index("Frankfurt"))
print("\n---\n")

# 7. Packing and Unpacking
print("Cities of Germany:", my_tuple)
print("Unpacking")
city1, city2, city3, city4, city5 = my_tuple
print("Variable city 1:", city1)
print("Variable city 2:", city2)
print("Variable city 3:", city3)
print("Variable city 4:", city4)
print("Variable city 5:", city5)
print()
print("Unpacking with asterisk *")
city_a, *city_others, city_e = my_tuple
print("Variable city a:", city_a)
print("Variable city others:", city_others)
print("Variable city e:", city_e)
print("\n---\n")

# 8. Joining Tuples
another_tuple = ("Vienna", "Salzburg", "Linz", "Graz")
print("Cities of Germany:", my_tuple)
print("Cities of Austria:", another_tuple)
print("Joining with concatenate")
cities_combined = my_tuple + another_tuple
print("Cities of DE & AT:", cities_combined)
print()
print("Multiplying")
print("Cities of AT repeated 3 times:", 3 * another_tuple)
print("\n---\n")