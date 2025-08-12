print()
# Step 1: Create a list named shopping_list with the items milk, oranges, coffee, sugar and butter.
shopping_list = ["milk", "oranges", "coffee", "sugar", "butter"]
# Output the whole list.
print("Shopping List:", shopping_list)
print("\n---\n")

# Add honey at the end of the list.
shopping_list.append("honey")
print("Updated shopping list with honey:", shopping_list)
# Remove milk by passing its value.
shopping_list.remove("milk")
print("Updated shopping list after removing milk:", shopping_list)
# Add  soy sauce in the list as the third item.
shopping_list.insert(2, "soy sauce")
print("Updated shopping list with soy sauce as third item:", shopping_list)
# Remove the last item of the list.
shopping_list.pop()
print("Updated shopping list after removing last item pop():", shopping_list)
print("\n---\n")

# Create a second list named last_minute_items with the items blueberries, potatos and chicken.
last_minute_items = ["blueberries", "potatoes", "chicken"]
print("Last minute items:", last_minute_items)
# Add the items in last_minute_items to shopping_list.
shopping_list.extend(last_minute_items)
print("Extended shopping list:", shopping_list)
print("\n---\n")

# Remove all the items in both lists.
shopping_list.clear()
print("Cleared shopping list:", shopping_list)
print("\n---\n")