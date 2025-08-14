print()
# Step 1: Create a list colors = ["red", "green", "blue"]
colors = ["red", "green", "blue"]
print("Colors:", colors)
print("\n---\n")
# Print the first item using indexing.
print("First item using indexing:", colors[0])
# Change "green" to "yellow".
colors[1] = "yellow"
print("Updated colors after changing green to yellow:", colors)
# Add "green", "purple" and "red".
colors.extend(["green", "purple", "red"])
# Print the updated list.
print("Updated colors after adding more colors:", colors)
print("\n---\n")

# Step 2: Slice "red", "yellow" and "blue" and store them into the variable primary_colors.
primary_colors = colors[0:3]
# Print the new list.
print("New primary colors list:", primary_colors)
# Slice "purple" and "red" and store them into the variable warm_colors.
warm_colors = colors[-2:]
# Print the new list.
print("New warm colors list:", warm_colors)
# Slice "blue" and "green" and store them into the variable cold_colors.
cold_colors = colors[2:4]
# Print the new list.
print("New cold colors list:", cold_colors)
print("\n---\n")
# Step 3: Concatenate the list primary_colors to warm_colors.
print("Primary colors:", primary_colors)
print("Warm Colors:", warm_colors)
warm_colors = warm_colors + primary_colors
# Print warm_colors.
print("Concatenated warm Colors list after adding primary colors:", warm_colors)
# Find the index of any color that is not warm.
print("Index of blue which is not a warm color:", warm_colors.index("blue"))
# Using the index you find out in the last step, update the items to warm colors.
warm_colors[4] = "warm blue"
print("Updated warm colors list after replacing blue with warm blue:", warm_colors)
print("\n---\n")