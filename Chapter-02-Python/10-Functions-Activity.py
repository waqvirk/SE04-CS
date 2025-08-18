print()
# 1. Sum of List Elements
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example
my_numbers = [1, 2, 3, 4, 5]
print("List of numbers:", my_numbers)
print("Sum of list of numbers by calling function:", sum_list(my_numbers))
print("\n---\n")

# 2. Repeated Greeting
def repeat_greeting(name, times):
    for i in range(times):
        print(f"Hello, {name}!")

# Example
repeat_greeting("John", 3)
print("\n---\n")

# 3. Factorial Calculation
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
print(f"Factorial:", factorial(5))
print("\n---\n")

# 4. Fibonacci Sequence Generator
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    return fib_sequence

# Example:
print("Fibonacci Sequence:", fibonacci(5))
print("\n---\n")

# 5. Maximum of Two Numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# Example
print("Bigger no:", max_of_two(10, 5))
print("\n---\n")

# 6. Print a Pattern with Nested Loops
def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end = "")
        print()

# Example
print_triangle(5)
print("\n---\n")
