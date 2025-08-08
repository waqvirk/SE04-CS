# Step 1: Create variables:
name = "Waqar Virk"
age = 30
height = 1.78

# Step 2: Print the variables:
print(name)
print(age)
print(height)
print(name,age,height)

# Step 3: Check the type of the variables:
print(name, type(name))
print(age, type(age))
print(height, type(height))

# Step 4: Casting
age_str = str(age)
print("My name is", name, "and I am", age_str, "years old.")
print(f"My name is {name} and I am {age} years old.")             #using f-strings without casting

# Bonus: Global Variable (Bonus)
global_message = "AI is Here"
print(global_message)
# Inside Function
def modified_message():
    global global_message                                         #telling python to use global variable
    global_message = "well kind of"
modified_message()                                                #calling the function to modify global variable
