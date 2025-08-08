print()
# Step 1: Arithmetic Operators
a, b = 15, 4
print ("a:",a, "b:",b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("\n---\n")

# Step 2: Assignment Operators
x = 10
print("x", x)
x += 5
print("After += 5:", x)
x -= 5
print("After -= 5:", x)
x *= 5
print("After *= 5:", x)
x /= 5
print("After /= 5:", x)
print("\n---\n")

# Step 3: Comparison Operators
print ("a:",a, "b:",b)
print("After a==b:", a == b)
print("After a!=b:", a != b)
print("After a>b:", a > b)
print("After a<b:", a < b)
print("After a≥b:", a >= b)
print("After a≤b:", a <= b)
print("\n---\n")

# Step 4: Logical Operators
is_python_fun = True
is_java_fun = False
print("Is python fun?", is_python_fun)
print("Is java fun?",is_java_fun)
print("Is python and java fun?", is_python_fun and is_java_fun)
print("Is python or java fun?", is_python_fun or is_java_fun)
print("Is python not fun?", not is_python_fun)
print("Is java not fun?", not is_java_fun)
print("\n---\n")

# Step 5: Identity Operators
list1 = [1,2,3]
list2 = list1
list3 = [1,2,3]
print("List 1:", list1)
print("List 2:", list2)                   #list2 = list1
print("List 3:", list3)
print("Checking if List 1 is List 2:", list1 is list2)
print("Checking if List 1 is not List 2:", list1 is not list2)
print("Checking if List 1 is List 3:", list1 is list3)
print("\n---\n")

# Step 6: Membership Operators
text = "python programming is fun!"
print("Printing Text:", text)
print("Checking if the text contain word 'python':", "python" in text)
print("Checking if the text contain word 'java':", "java" in text)
print("\n---\n")

# Step 7: Bitwise Operators (Bonus)
d, e = 5, 3
print("d:", d, "e:", e)
print("Bitwise AND:", d & e)
print("Bitwise OR:", d | e)
print("Bitwise XOR:", d ^ e)
print("Bitwise left shift:", d << 1)
print("Bitwise right shift:", e >> 1)
print("\n---\n")

# Step 8: Operator Precedence
result1 =  2 + 3 * 4 ** 2
print ("Result of 2 + 3 * 4 ** 2 without parentheses:", result1)
result2 =  (2 + 3) * (4 ** 2)
print ("Result of (2 + 3) * (4 ** 2) with parentheses:", result2)
print("\n---\n")