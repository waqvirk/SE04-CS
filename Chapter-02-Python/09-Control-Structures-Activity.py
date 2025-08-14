print()
# 1. Basic If Condition
number = 18
if number > 0:
    print("Positive number:", number)
elif number < 0:
    print("Negative number:", number)
else:
    print("Zero:", number)
print("\n---\n")

# 2. Grade Calculator
score = 84
if score >=90:
    print("Grade A:", score)
elif score >=80:
    print("Grade B:", score)
elif score >=70:
    print("Grade C:", score)
elif score >=60:
    print("Grade D:", score)
else:
    print("Grade F:", score)
print("\n---\n")

# 3. Ternary Operator Practice
user_age = 16
user_status = "Adult" if user_age >= 18 else "Minor"
print("User status is:", user_status)
print("\n---\n")

# 4. For Loop over a List
vehicles = ["BMW", "Toyota", "Ford", "BYD"]
for vehicle in vehicles:
    print(f" I like to ride a {vehicle}")
print("\n---\n")

# 5. For Loop with Conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print("Even number:", number)
print("\n---\n")

# 6. While Loop Summation
num = 1
total = 0
while num <= 100:
    total += num
    num += 1
print("Total sum:", total)
print("\n---\n")

# 7. Break out of a Loop
words = ["Sky", "Air", "Land", "Universe", "Moon", "Earth", "Planet"]
print("list of words:", words)
for word in words:
    if len(word) > 5:
        print("Word bigger than 5 letters found:", word)
        break
print("\n---\n")

# 8. Nested Loops
peoples = ["Alex", "John", "Kim", "Peterson", "Mike",]
pets = ["Cat", "Dog", "Parrot", "Snake", "Rabbit",]
print("People:", peoples)
print("Pets:", pets)
for people in peoples:
    for pet in pets:
        print(f"Possible combination of pet for {people}: {pet}")
print("\n---\n")

# 9. Loop with Else Clause
print("Pets:", pets)
value_to_find = "Snake"
for pet in pets:
    if pet == value_to_find:
        print(f"{value_to_find} is found")
        break
else:
    print(f"{value_to_find} is not found")
print("\n---\n")

# 10. Pass Statement Usage
print("People:", peoples)
for people in peoples:
    pass
print("\n---\n")

# 11. Pattern matching
fruits = ["Apple", "Banana", "Cherry", "Dragonfruit",]
veggies = ["Tomato", "Onion", "Carrot", "Eggplant",]
meat = ["Lamb", "Beef", "Chicken", "Duck",]
item = "Onion"
match item:
    case x if item in fruits:
        print(f"{item} is a fruit")
    case x if item in veggies:
        print(f"{item} is a veggie")
    case x if item in meat:
        print(f"{item} is a meat")
    case _:
        print(f"{item} doesn't belong to any known category")
print("\n---\n") 