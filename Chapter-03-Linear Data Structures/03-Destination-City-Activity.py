### Destination City ###
def destination_city(paths):
    starting_cities = set()
    for path in paths:                      # collect all cities that appear as starting points
        starting_cities.add(path[0])

    for path in paths:
        destination = path[1]
        if destination not in starting_cities:
            return destination
    

# Example 1
paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print()
print("All the possible paths:", paths)
print("Destination city that has no outgoing path:", destination_city(paths))
print()
print("-"*100)


# Example 2
paths = [["City_B", "City_C"], ["City_D", "City_B"], ["City_C", "City_A"]]
print()
print("All the possible paths:", paths)
print("Destination city that has no outgoing path:", destination_city(paths))
print()
print("-"*100)

# Example 3
paths = [["City_A", "City_Z"]]
print()
print("All the possible paths:", paths)
print("Destination city that has no outgoing path:", destination_city(paths))
print()
print("-"*100)