# Step 1: Create Strings
first_name, last_name, age = "Waqar", "Virk", 30
bio = """I am Waqar Virk, a curious mind exploring programming and tech. Always learning, always experimenting.
I enjoy turning complex ideas into simple solutions."""
print()

# Step 2: Access Characters and Slice Strings
print("First character of first_name:",first_name[0],"and last character of last_name:",last_name[-1])
print("First 10 characters of bio are:",bio[:10])
print("\n---\n")


# Step 3: Loop Through a String
print("Characters in first_name:")
for char in first_name:
    print(char)
print("\n---\n")

# Step 4: String Length
print("The length of bio is:",len(bio))
print("\n---\n")

# Step 5: Check Substrings
print("is 'python' in bio?:", "python" in bio)
print("is 'java' not in bio?:", "java" not in bio)
print("\n---\n")

# Step 6: Modify Strings
print("First name in uppercase is:", first_name.upper())
print("Last name in lowercase is:", last_name.lower())
print("Removing extra spaces while replacing programming with coding:", bio.strip().replace("programming","coding"))
print("Splitted bio:", bio.split())
print("\n---\n")

# Step 7: Concatenate Strings
full_name = first_name + " " + last_name
print("Full name:", full_name)
print("\n---\n")

# Step 8: String Formatting
print("Using f-string:", f"Hello, my name is {full_name} and I love Python!")
print("Using format method:", "My full name is {} and I am {} years old.".format(full_name,age))
print("\n---\n")

# Step 9: Escape Characters
print("He said, \"Python's is great!\"")         # \" > escapes the double quotes
print('He said, "Python\'s is great!"')          # ' > single quptes don't need escaping inside double quoted string
print("\n---\n")

# Bonus: Use String Methods
print("Bio string centered within 50 characters:", bio.center(50))
print("Count of letter 'a' in your full name:", full_name.count("a"))
print("\n---\n")
